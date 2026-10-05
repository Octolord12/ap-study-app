from common import *

B = bank(1, "unit-1-primitive-types")
T_VT, T_EXP, T_CC = ("variables-and-data-types", "expressions-and-assignment", "compound-assignment-and-casting")

# 1. integer division and remainder
trace(B, T_EXP, "What is printed as a result of executing the following code segment?",
      body="int a = 17, b = 5;\nSystem.out.println(a / b * b + a % b);",
      mutants=[("a % b", "0", "This leaves out the remainder term: `a / b * b` is 15 with integer division, and the remainder 2 is then missing."),
               ("a / b * b", "a / (b * b)", "This groups the division as `a / (b * b)`. Division and multiplication have equal precedence and are evaluated left to right, so it is `(a / b) * b`."),
               ("int a = 17, b = 5;", "double a = 17, b = 5;", "This treats the division as exact (3.4) instead of integer division (3), and so does not recover `a` exactly.")],
      correct_expl="`a / b` is integer division: 3. Then `3 * b` is 15, and `a % b` is the remainder 2. 15 + 2 = 17.",
      explanation="Integer division truncates, `*` and `/` associate left to right, and the remainder is added last. For positive values, `a / b * b + a % b` always equals `a`.")

# 2. cast placement
trace(B, T_CC, "What is printed as a result of executing the following code segment?",
      body="double d = 7 / 2;\nint n = (int) 3.9 + (int) (2.6 + 1.6);\nSystem.out.println(d + \" \" + n);",
      mutants=[("7 / 2", "7 / 2.0", "The initial value uses integer division because both operands are `int`; it happens before the result is stored in the `double`. With `2.0` it would be 3.5."),
               ("(int) 3.9 + (int) (2.6 + 1.6)", "(int) (3.9 + 2.6 + 1.6)", "This applies a single cast to the whole sum. In the original, `(int) 3.9` truncates to 3 and `(int) (2.6 + 1.6)` truncates 4.2 to 4 separately.")],
      manual=[("3.5 8", "This makes both mistakes: it treats `7 / 2` as exact division, and it applies one cast to the whole sum or rounds 3.9 up. A cast truncates toward zero, it does not round."),],
      correct_expl="`7 / 2` is integer division, 3, stored in `d` as 3.0. `(int) 3.9` is 3 and `(int) (2.6 + 1.6)` is `(int) 4.2`, which is 4. So `n` is 7.",
      explanation="A cast truncates toward zero and applies only to the expression directly after it. Integer division happens before the assignment converts the result to `double`.")

# 3. overflow
trace(B, T_VT, "What is printed as a result of executing the following code segment?",
      body="int x = Integer.MAX_VALUE;\nint y = x + 1;\nlong z = x + 1;\nlong w = x + 1L;\nSystem.out.println(y + \" \" + z + \" \" + w);",
      mutants=[("long z = x + 1;", "long z = x + 1L;", "This assumes that storing the sum in a `long` avoids the overflow. The addition `x + 1` is done with `int` arithmetic first, so it overflows before the assignment.")],
      manual=[("2147483648 2147483648 2147483648", "This assumes that Java integers never overflow. An `int` cannot hold 2147483648, so `x + 1` wraps around."),
              ("2147483647 2147483647 2147483648", "This assumes the value stops at the largest `int` (saturates). Java's `int` arithmetic wraps around instead.")],
      correct_expl="`x + 1` overflows in `int` arithmetic and wraps to Integer.MIN_VALUE, -2147483648. `y` and `z` both hold that value (for `z` the overflowed `int` is only then widened to `long`). `x + 1L` is computed as a `long`, so `w` is 2147483648.",
      explanation="Overflow happens in the type of the arithmetic, not in the type of the variable that receives the result. Widening to `long` after an `int` operation does not recover lost information.")

# 4. compound assignment truncates the result, not the operand
trace(B, T_CC, "What is printed as a result of executing the following code segment?",
      body="int x = 10;\nx *= 2.5;\nx -= 0.9;\nSystem.out.println(x);",
      mutants=[("int x = 10;", "double x = 10;", "This treats `x` as a `double`. Because `x` is an `int`, each compound assignment casts its result back to `int`."),
               ("x *= 2.5;", "x *= 2;", "This truncates the operand 2.5 to 2 before multiplying. The cast is applied to the *result* of the whole operation, so `10 * 2.5` is 25.0 first.")],
      manual=[("25", "This assumes `x -= 0.9` has no effect because 0.9 truncates to 0. The cast applies to the result, `(int) (25 - 0.9)`, which is `(int) 24.1`, or 24.")],
      correct_expl="`x *= 2.5` means `x = (int) (x * 2.5)`, so x is 25. Then `x -= 0.9` means `x = (int) (x - 0.9)`, which is `(int) 24.1`, or 24.",
      explanation="A compound assignment performs the operation in the wider type, then casts the result back to the type of the variable (truncating). It does not truncate the right-hand operand first.")

# 5. side effects of increments
trace(B, T_EXP, "What is printed as a result of executing the following code segment?",
      body="int i = 3;\nint j = i++ + ++i;\nSystem.out.println(i + \" \" + j);",
      mutants=[("i++ + ++i", "i++ + i++", "This treats `++i` like `i++`. The second operand, `++i`, increments first and then yields the new value (5), not the old value (4)."),
               ("i++ + ++i", "++i + ++i", "This treats `i++` like `++i`. The first operand, `i++`, yields the old value (3) before incrementing."),
               ("i++ + ++i", "i + i", "This ignores the side effects of the increments, which change `i` twice.")],
      correct_expl="`i++` yields 3 and makes `i` 4. `++i` makes `i` 5 and yields 5. So `j` is 3 + 5 = 8, and `i` ends as 5.",
      explanation="Post-increment yields the old value and then increments; pre-increment increments and then yields the new value. Operands are evaluated left to right.")

# 6. char arithmetic
trace(B, T_VT, "What is printed as a result of executing the following code segment?",
      body="char c = 'a';\nc += 2;\nint n = c + 1;\nSystem.out.println(c + \" \" + n + \" \" + (char) n);",
      mutants=[("c + \" \"", "(int) c + \" \"", "This prints the numeric code of `c`. Concatenating a `char` with a string appends the character itself, `c`."),
               ("(char) n", "n", "This leaves out the cast, so the last item is printed as a number. `(char) n` converts 100 back to the character `d`.")],
      manual=[("c 99 c", "This forgets the `+ 1`: `c + 1` is the int 100, since `c` has code 99.")],
      correct_expl="`'a'` has code 97, and `c += 2` makes it `'c'` (99). `n = c + 1` is the `int` 100. Concatenation prints the char `c`, then 100, then `(char) 100`, which is `d`.",
      explanation="A `char` is a numeric code. Arithmetic on it produces an `int`, and a cast converts it back to a character.")

# 7. string concatenation precedence
trace(B, T_EXP, "What is printed as a result of executing the following code segment?",
      body="System.out.println(1 + 2 + \"3\" + 4 + 5);",
      mutants=[("1 + 2 + \"3\"", "\"\" + 1 + 2 + \"3\"", "This starts the expression with a string, so every `+` is concatenation. The original begins with two numbers, so `1 + 2` is added first."),
               ("4 + 5", "(4 + 5)", "This adds 4 and 5 first. Without parentheses, once the expression has become a `String`, each `+` appends text.")],
      manual=[("15", "This adds all the numbers. As soon as a `String` operand is reached, the rest of the expression is concatenation.")],
      correct_expl="`+` is evaluated left to right. `1 + 2` is 3 (an int). `3 + \"3\"` is the string \"33\", and then `4` and `5` are appended one at a time, giving \"3345\".",
      explanation="Operators of equal precedence evaluate left to right. The first `+` that has a `String` operand switches the rest of the chain to concatenation.")

# 8. negative operands
trace(B, T_EXP, "What is printed as a result of executing the following code segment?",
      body="System.out.println(-7 % 3 + \" \" + 7 % -3 + \" \" + -7 / 2);",
      mutants=[("-7 % 3", "Math.floorMod(-7, 3)", "This uses a mathematical modulus that is never negative for a positive divisor. In Java the sign of `%` follows the dividend, so `-7 % 3` is -1."),
               ("-7 / 2", "Math.floorDiv(-7, 2)", "This rounds -3.5 down to -4. Java's integer division truncates toward zero, giving -3."),
               ("7 % -3", "Math.floorMod(7, -3)", "This takes the sign from the divisor. In Java the sign of `%` follows the dividend, so `7 % -3` is 1.")],
      correct_expl="Java's `%` takes the sign of the left operand: `-7 % 3` is -1 and `7 % -3` is 1. Integer division truncates toward zero: `-7 / 2` is -3.",
      explanation="In Java, `a % b` has the sign of `a`, and integer division truncates toward zero, so `(a / b) * b + a % b == a` always holds.")

# 9. rounding and casting
trace(B, T_CC, "What is printed as a result of executing the following code segment?",
      body="int r = (int) Math.round(2.5) + (int) Math.round(-2.5) + (int) Math.pow(2, 3);\nSystem.out.println(r);",
      mutants=[("(int) Math.round(2.5)", "(int) 2.5", "This truncates 2.5 to 2 instead of rounding it to 3. `Math.round(2.5)` rounds half up, giving 3."),
               ("(int) Math.pow(2, 3)", "(int) Math.pow(3, 2)", "This swaps the base and exponent: `Math.pow(2, 3)` is 2 cubed, which is 8, not 9."),
               ("Math.round(-2.5)", "Math.round(2.5)", "This ignores the sign. `Math.round(-2.5)` rounds toward positive infinity (half up), giving -2, not 3.")],
      correct_expl="`Math.round(2.5)` is 3. `Math.round(-2.5)` rounds half up toward positive infinity, giving -2. `Math.pow(2, 3)` is 8.0, which casts to 8. The sum is 3 - 2 + 8 = 9.",
      explanation="`Math.round` rounds ties up (toward positive infinity), so -2.5 becomes -2. `Math.pow` returns a `double`.")

# 10. mixed arithmetic and comparisons
trace(B, T_EXP, "What is printed as a result of executing the following code segment?",
      body="int a = 5;\ndouble b = a / 2;\ndouble c = a / 2.0;\nboolean t = (b == 2) && (c == 2.5);\nSystem.out.println(t + \" \" + (a / 2 * 2.0));",
      mutants=[("double b = a / 2;", "double b = a / 2.0;", "This treats `a / 2` as exact. Both operands are `int`, so the division is integer division and `b` holds 2.0."),
               ("(a / 2 * 2.0)", "(a / 2.0 * 2)", "This evaluates the division in `double`. In `a / 2 * 2.0` the division is performed first with two `int` operands, giving 2, and only then multiplied by 2.0.")],
      manual=[("false 5.0", "Both mistakes: `b` holds 2.0 (integer division), and `a / 2 * 2.0` is 4.0, not 5.0.")],
      correct_expl="`a / 2` is integer division: 2, so `b` is 2.0. `c` is 2.5. Both comparisons are true. In `a / 2 * 2.0`, `a / 2` is 2 and `2 * 2.0` is 4.0.",
      explanation="The type of a division depends only on its operands. Where the result is stored does not change how it is computed.")

# 11. which statement compiles
cands = [("int a = 7 / 2.0;", False), ("float f = 3.14;", False), ("long m = 3000000000;", False), ("double d = 'x' * 2;", True)]
for stmt, ok in cands:
    assert (compile_error(program(stmt)) is None) == ok, stmt
B.mcq(T_VT, "Which of the following statements compiles without error?",
      ch("`double d = 'x' * 2;`", "`'x' * 2` is an `int` (the char is promoted to its numeric code), and an `int` can be assigned to a `double` by widening."),
      [ch("`int a = 7 / 2.0;`", "`7 / 2.0` is a `double`. Assigning a `double` to an `int` is a narrowing conversion and needs an explicit cast, such as `(int) (7 / 2.0)`."),
       ch("`float f = 3.14;`", "`3.14` is a `double` literal. Assigning it to a `float` is a narrowing conversion; the literal would need an `f` suffix (`3.14f`)."),
       ch("`long m = 3000000000;`", "The literal `3000000000` is an `int` literal that is too large for an `int`, which is a compile-time error. It needs an `L` suffix.")],
      "Widening conversions (`int` to `double`) are automatic, but narrowing conversions need a cast, and a literal is an `int` or `double` unless its suffix says otherwise.")

# 12. the mean of three numbers
trace(B, T_VT, "What is printed as a result of executing the following code segment?",
      body="int total = 7 + 8 + 10;\ndouble avg = total / 3;\ndouble avg2 = total / 3.0;\ndouble avg3 = (double) (total / 3);\ndouble avg4 = (double) total / 3;\nSystem.out.println(avg + \" \" + avg2 + \" \" + avg3 + \" \" + avg4);",
      mutants=[("(double) (total / 3)", "(double) total / 3", "This treats `(double) (total / 3)` like `(double) total / 3`. In the original, the division is done in integer arithmetic before the cast, so the cast happens too late."),],
      manual=[("8.333333333333334 8.333333333333334 8.333333333333334 8.333333333333334", "This assumes that storing the quotient in a `double` makes the division exact. For `avg` and `avg3` the division is between two `int` values, so it truncates first."),
              ("8.0 8.0 8.0 8.0", "This assumes that dividing by `3.0` or casting `total` to `double` still truncates. A `double` operand makes the division a `double` division.")],
      correct_expl="`total / 3` is integer division (25 / 3 = 8), so `avg` is 8.0. `total / 3.0` is a `double` division, 8.333333333333334. `(double) (total / 3)` casts the already-truncated 8 to 8.0. `(double) total / 3` casts `total` first, so the division is exact.",
      explanation="A cast applies only to the expression immediately after it. To get an exact quotient, a cast must happen before the division.")

# 13. an assignment whose right side has a side effect on the same variable
trace(B, T_CC, "What is printed as a result of executing the following code segment?",
      body="int x = 5;\nx = x++ * 2 + x;\nSystem.out.println(x);",
      mutants=[("x++ * 2 + x", "++x * 2 + x", "This treats `x++` as `++x`. The post-increment yields the old value, 5, so the product is 10, not 12."),
               ("x++ * 2 + x", "x * 2 + x++", "This reads `x` before the increment for the final `+ x`. In the original, the increment from `x++` has already happened by the time the right operand `x` is evaluated.")],
      manual=[("10", "This forgets the final `+ x` term. The expression is `x++ * 2 + x`, with the new value of `x` (6) added at the end.")],
      correct_expl="Operands are evaluated left to right: `x++` yields 5 and makes `x` 6, then `5 * 2` is 10, and the final `x` is already 6, so 10 + 6 = 16. This value is then assigned to `x`.",
      explanation="Side effects take place during evaluation. The incremented value is visible to later operands in the same expression, but the final assignment overwrites `x`.")

# 14. floating-point representation
trace(B, T_CC, "What is printed as a result of executing the following code segment?",
      body="System.out.println((int) (0.29 * 100) + \" \" + (0.1 + 0.2 == 0.3) + \" \" + Math.round(0.29 * 100));",
      mutants=[("(int) (0.29 * 100)", "(int) Math.round(0.29 * 100)", "This rounds before casting. The original truncates 0.29 * 100, which is not exactly 29 because 0.29 cannot be stored exactly."),
               ("0.1 + 0.2 == 0.3", "Math.abs(0.1 + 0.2 - 0.3) < 1e-9", "This assumes `0.1 + 0.2` is exactly 0.3. In `double` arithmetic the sum is 0.30000000000000004, so the `==` test is false.")],
      manual=[("29 true 29", "Both mistakes: `0.29 * 100` evaluates to 28.999999999999996, which truncates to 28, and `0.1 + 0.2 == 0.3` is false.")],
      correct_expl="`0.29 * 100` is 28.999999999999996, which `(int)` truncates to 28, while `Math.round` rounds it to 29. And `0.1 + 0.2` is 0.30000000000000004, so it does not equal 0.3.",
      explanation="Many decimal fractions cannot be stored exactly in binary, so `double` results can be slightly off. Compare with a tolerance and use `Math.round` rather than a cast to round.")

# 15. compound assignment on an int
trace(B, T_CC, "What is printed as a result of executing the following code segment?",
      body="int a = 7;\na /= 2;\na *= 3.5;\na %= 4;\nSystem.out.println(a);",
      mutants=[("int a = 7;", "double a = 7;", "This treats `a` as a `double`. Because `a` is an `int`, `a /= 2` is integer division (3) and `a *= 3.5` truncates its result."),
               ("a *= 3.5;", "a *= 3;", "This truncates the operand 3.5 to 3 before multiplying. The result of `3 * 3.5` is truncated: `(int) 10.5` is 10.")],
      manual=[("10", "This skips the last statement. After `a *= 3.5`, `a` is 10, and then `a %= 4` leaves the remainder 2.")],
      correct_expl="`a /= 2` gives 3 (integer division). `a *= 3.5` means `a = (int) (3 * 3.5)`, which is `(int) 10.5`, or 10. Then `a %= 4` gives 10 % 4, which is 2.",
      explanation="Each compound assignment truncates its result to the variable's type before the next statement runs.")

# ------------------------------------------------------------------ FRQs
members_a = '''
    public static int digitSum(int n) {
        int sum = 0;
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }

    public static boolean isHarshad(int n) {
        if (n <= 0) {
            return false;
        }
        return n % digitSum(n) == 0;
    }
'''
verify(members_a, [("digitSum(4083)", 15), ("digitSum(0)", 0), ("digitSum(7)", 7), ("isHarshad(18)", "true"), ("isHarshad(19)", "false"), ("isHarshad(0)", "false"), ("isHarshad(21)", "true"), ("isHarshad(11)", "false")])
B.frq(T_EXP,
      "A *Harshad number* is a positive integer that is evenly divisible by the sum of its digits. For example, 18 is a Harshad number because its digit sum is $1+8=9$ and 18 is divisible by 9, while 19 is not (its digit sum is 10).\n\nThe class `DigitTools` contains the two methods below. You may not use `String` methods in either part.\n\n```java\npublic class DigitTools {\n    /** Returns the sum of the digits of n. Precondition: n >= 0 */\n    public static int digitSum(int n)\n    { /* to be implemented in part (a) */ }\n\n    /** Returns true if n > 0 and n is evenly divisible by digitSum(n); false otherwise. */\n    public static boolean isHarshad(int n)\n    { /* to be implemented in part (b) */ }\n}\n```\n\n**(a)** Write the method `digitSum`. For example, `digitSum(4083)` returns 15 and `digitSum(0)` returns 0.\n\n**(b)** Write the method `isHarshad`, using `digitSum` as appropriate. For example, `isHarshad(18)` returns `true`, `isHarshad(19)` and `isHarshad(0)` return `false`.",
      [(1, "(a) Uses a loop that continues while digits remain"),
       (1, "(a) Extracts the last digit with `n % 10`"),
       (1, "(a) Removes the last digit with `n / 10`"),
       (1, "(a) Accumulates the sum correctly and returns it (returns 0 for input 0)"),
       (1, "(b) Returns false when `n <= 0` (and does not divide by zero)"),
       (1, "(b) Calls `digitSum(n)`"),
       (1, "(b) Tests divisibility with `%` and returns the correct boolean")],
      "```java\npublic static int digitSum(int n) {\n    int sum = 0;\n    while (n > 0) {\n        sum += n % 10;\n        n /= 10;\n    }\n    return sum;\n}\n\npublic static boolean isHarshad(int n) {\n    if (n <= 0) {\n        return false;\n    }\n    return n % digitSum(n) == 0;\n}\n```\nIn `digitSum`, `n % 10` is the last digit and `n /= 10` drops it, so the loop visits every digit. In `isHarshad`, the `n <= 0` test must come first, because `digitSum(0)` is 0 and `n % 0` would throw an `ArithmeticException`.")

members_b = '''
    public static String clock(int totalSeconds) {
        int hours = totalSeconds / 3600;
        int minutes = (totalSeconds % 3600) / 60;
        int seconds = totalSeconds % 60;
        String result = hours + ":";
        if (minutes < 10) {
            result += "0";
        }
        result += minutes + ":";
        if (seconds < 10) {
            result += "0";
        }
        return result + seconds;
    }

    public static int roundToMultiple(int value, int unit) {
        return (value + unit / 2) / unit * unit;
    }
'''
verify(members_b, [('clock(3725)', "1:02:05"), ('clock(59)', "0:00:59"), ('clock(36000)', "10:00:00"), ('clock(0)', "0:00:00"), ('clock(3599)', "0:59:59"),
                   ("roundToMultiple(47, 5)", 45), ("roundToMultiple(48, 5)", 50), ("roundToMultiple(45, 10)", 50), ("roundToMultiple(44, 10)", 40), ("roundToMultiple(7, 3)", 6), ("roundToMultiple(6, 4)", 8)])
B.frq(T_CC,
      "The class `TimeTools` contains the two methods described below. Use only integer arithmetic and `String` concatenation in your solutions.\n\n```java\npublic class TimeTools {\n    /** Returns a clock-style String for a duration of totalSeconds seconds,\n     *  in the form h:mm:ss. The hours have no leading zero; the minutes and\n     *  seconds are always two digits. Precondition: totalSeconds >= 0 */\n    public static String clock(int totalSeconds)\n    { /* to be implemented in part (a) */ }\n\n    /** Returns the multiple of unit that is closest to value. If value is exactly halfway\n     *  between two multiples, returns the larger one.\n     *  Preconditions: value >= 0, unit > 0 */\n    public static int roundToMultiple(int value, int unit)\n    { /* to be implemented in part (b) */ }\n}\n```\n\n**(a)** Write the method `clock`. For example, `clock(3725)` returns `\"1:02:05\"`, `clock(59)` returns `\"0:00:59\"` and `clock(36000)` returns `\"10:00:00\"`.\n\n**(b)** Write the method `roundToMultiple`. For example, `roundToMultiple(47, 5)` returns 45, `roundToMultiple(48, 5)` returns 50 and `roundToMultiple(45, 10)` returns 50.",
      [(1, "(a) Computes hours using integer division by 3600"),
       (1, "(a) Computes minutes using the remainder after hours, divided by 60"),
       (1, "(a) Computes seconds using `totalSeconds % 60`"),
       (1, "(a) Adds a leading zero for minutes and seconds that are less than 10"),
       (1, "(a) Builds and returns the string in the form h:mm:ss"),
       (1, "(b) Uses integer division and multiplication by `unit` to produce a multiple of `unit`"),
       (1, "(b) Adds half of `unit` before dividing so that values are rounded to the nearest multiple, with exact ties going up")],
      "```java\npublic static String clock(int totalSeconds) {\n    int hours = totalSeconds / 3600;\n    int minutes = (totalSeconds % 3600) / 60;\n    int seconds = totalSeconds % 60;\n    String result = hours + \":\";\n    if (minutes < 10) {\n        result += \"0\";\n    }\n    result += minutes + \":\";\n    if (seconds < 10) {\n        result += \"0\";\n    }\n    return result + seconds;\n}\n\npublic static int roundToMultiple(int value, int unit) {\n    return (value + unit / 2) / unit * unit;\n}\n```\nIn (b), adding `unit / 2` moves values that are at least halfway to the next multiple past it, and integer division then truncates down to a multiple of `unit`. For an exact tie such as 45 with a unit of 10, `(45 + 5) / 10 * 10` is 50, the larger multiple.")

B.save()
B.brief()
