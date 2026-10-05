from common import *

B = bank(3, "unit-3-boolean-if")
T_BOOL, T_IF, T_IFELSE, T_COMP, T_OBJ = ("boolean-expressions", "if-statements", "if-else-statements", "compound-boolean-expressions", "comparing-objects")
Q = "What is printed as a result of executing the following code segment?"


def equivalent(orig, cand):
    body = f"int bad = 0;\nfor (int a = -2; a <= 12; a++) for (int b = -2; b <= 8; b++) if (({orig}) != ({cand})) bad++;\nSystem.out.println(bad);"
    return run(program(body)) == "0"


# 1. De Morgan
orig = "!(a > 5 || b <= 3)"
opts = [("a <= 5 && b > 3", True, "De Morgan's law: `!(P || Q)` is `!P && !Q`. The negation of `a > 5` is `a <= 5` and the negation of `b <= 3` is `b > 3`."),
        ("a <= 5 || b > 3", False, "This negates each comparison but keeps the `||`. De Morgan's law also changes `||` to `&&`."),
        ("a > 5 && b <= 3", False, "This changes `||` to `&&` but leaves the comparisons un-negated."),
        ("a < 5 && b < 3", False, "This negates the comparisons incorrectly: the negation of `a > 5` is `a <= 5`, not `a < 5`, and the negation of `b <= 3` is `b > 3`.")]
for text, ok, _ in opts:
    assert equivalent(orig, text) == ok, text
B.mcq(T_COMP, "Which of the following expressions is equivalent to `!(a > 5 || b <= 3)`?",
      ch("`" + opts[0][0] + "`", opts[0][2]), [ch("`" + t + "`", e) for t, _, e in opts[1:]],
      "Apply De Morgan's laws: negating a compound condition negates each part and swaps `&&` and `||`.")

# 2. short-circuit evaluation with side effects
trace(B, T_COMP, Q, body="int x = 0;\nboolean r = (x++ > 0) && (x++ > 0);\nboolean s = (x++ >= 0) || (x++ > 0);\nSystem.out.println(x + \" \" + r + \" \" + s);",
      mutants=[("(x++ > 0) && (x++ > 0)", "(x++ > 0) & (x++ > 0)", "This assumes the right operand of `&&` is always evaluated. Because `x++ > 0` is false (0 > 0), the `&&` skips its right operand, so `x` is incremented only once there.")],
      manual=[("4 false true", "This assumes both operands of both `&&` and `||` are always evaluated. Each operator skips its right operand when the left operand already decides the result."),
              ("1 false true", "This counts only one increment. The first `x++` leaves `x` at 1, and the second statement's first `x++` makes it 2.")],
      correct_expl="In the first statement, `x++ > 0` compares 0 > 0 (false) and leaves `x` at 1; the `&&` is short-circuited, so `r` is false. In the second, `x++ >= 0` compares 1 >= 0 (true) and leaves `x` at 2; the `||` is short-circuited, so `s` is true.",
      explanation="`&&` skips its right operand when the left is false and `||` skips it when the left is true, so side effects in the right operand may never happen.")

# 3. dangling else
trace(B, T_IFELSE, Q, body="int a = 4, b = 6, c = 0, d = 0;\nif (a > 3)\n    if (b > 7)\n        c = 1;\n    else\n        c = 2;\nif (a > 5)\n    if (b > 7)\n        d = 1;\n    else\n        d = 2;\nSystem.out.println(c + \" \" + d);",
      mutants=[("if (a > 3)\n    if (b > 7)\n        c = 1;\n    else\n        c = 2;", "if (a > 3) {\n    if (b > 7)\n        c = 1;\n} else\n    c = 2;", "This pairs the `else` with the outer `if (a > 3)`, as the indentation of some code might suggest. In Java an `else` always belongs to the nearest unmatched `if`.")],
      manual=[("0 2", "This pairs each `else` with its outer `if`. An `else` belongs to the nearest `if`, which is `if (b > 7)` in both statements."),
              ("1 0", "This assumes `b > 7` is true. Here `b` is 6, so the `else` branch runs when `a > 3`.")],
      correct_expl="The `else` belongs to the inner `if (b > 7)`. In the first statement `a > 3` is true and `b > 7` is false, so the `else` runs: c = 2. In the second, `a > 5` is false, so nothing in that statement runs and d stays 0.",
      explanation="An `else` is matched with the nearest preceding `if` that has no `else`; indentation does not matter.")

# 4. separate ifs versus else-if
trace(B, T_IF, Q, body="System.out.println(f(15) + \",\" + f(10) + \",\" + f(9));",
      members='    public static String f(int n) {\n        String s = "";\n        if (n % 3 == 0) s += "Fizz";\n        if (n % 5 == 0) s += "Buzz";\n        else s += n;\n        return s;\n    }\n',
      mutants=[("if (n % 5 == 0) s += \"Buzz\";", "else if (n % 5 == 0) s += \"Buzz\";", "This treats the two tests as one `if`/`else if` chain. The second `if` is independent of the first, so both \"Fizz\" and \"Buzz\" can be added.")],
      manual=[("FizzBuzz15,Buzz,Fizz9", "This adds the number even when the `Buzz` branch ran. The `else` belongs to the second `if`, so `n` is appended only when `n % 5 != 0`."),
              ("FizzBuzz,Buzz10,Fizz", "This pairs the `else` with the first `if`. In the code, the `else` follows the second `if`, so for 9 the `else` appends 9.")],
      correct_expl="For 15 both `if` statements add text (\"FizzBuzz\"); the `else` is skipped. For 10, only the second `if` is true: \"Buzz\". For 9, the first `if` adds \"Fizz\", and the second `if` is false, so its `else` appends 9: \"Fizz9\".",
      explanation="Consecutive `if` statements are independent; only the `else` that directly follows an `if` is tied to that `if`.")

# 5. precedence of && and ||
trace(B, T_COMP, Q, body="int x = 7;\nboolean b1 = x > 5 && x < 10 || x == 12 && x > 20;\nboolean b2 = x > 5 && (x < 10 || x == 12) && x > 20;\nboolean b3 = !(x > 5) || x < 10 && x != 7;\nSystem.out.println(b1 + \" \" + b2 + \" \" + b3);",
      manual=[("false false false", "This evaluates `||` before `&&` in `b1`. `&&` has higher precedence, so `b1` is `(x > 5 && x < 10) || (x == 12 && x > 20)`, which is true."),
              ("true true false", "This overlooks `x > 20` in `b2`. All three parts must be true for the `&&` chain, and `7 > 20` is false."),
              ("true false true", "This overlooks `x != 7` in `b3`. The right side is `x < 10 && x != 7`, which is false for 7.")],
      correct_expl="`&&` binds tighter than `||`. `b1` is `(7 > 5 && 7 < 10) || (...)`, which is true. `b2` requires `7 > 20`, so it is false. `b3` is `false || (7 < 10 && 7 != 7)`, which is false.",
      explanation="`!` is evaluated first, then `&&`, then `||`. Use parentheses to be sure of the grouping.")

# 6. overridden equals
CL = 'class Person {\n    private String name;\n    private int age;\n    public Person(String n, int a) { name = n; age = a; }\n    public boolean equals(Object o) {\n        if (!(o instanceof Person)) return false;\n        Person p = (Person) o;\n        return name.equals(p.name);\n    }\n}\n'
trace(B, T_OBJ, Q, body='Person a = new Person("Ann", 20);\nPerson b = new Person("Ann", 31);\nPerson c = a;\nPerson d = new Person("Bob", 20);\nSystem.out.println(a.equals(b) + " " + (a == b) + " " + (a == c) + " " + a.equals(d) + " " + a.equals("Ann"));',
      classes=CL,
      mutants=[("return name.equals(p.name);", "return name.equals(p.name) && age == p.age;", "This assumes `equals` compares both fields. The class's `equals` compares only the names, so two people with the same name are equal even when their ages differ.")],
      manual=[("false false false false false", "This assumes the default `Object.equals`, which compares references. `Person` overrides `equals` to compare names, so `a.equals(b)` is true."),
              ("true true true false false", "`==` always compares references and never calls `equals`, so `a == b` is false: they are two different objects.")],
      correct_expl="`equals` compares only names, so `a.equals(b)` is true. `a == b` is false (different objects). `a == c` is true (the same object). `a.equals(d)` is false (different names), and `a.equals(\"Ann\")` is false because a `String` is not a `Person`.",
      explanation="`==` compares references, whatever `equals` does. An overridden `equals` defines what it means for two different objects to be equal.")

# 7. assignment inside a condition
trace(B, T_IFELSE, Q, body='boolean done = false;\nif (done = true)\n    System.out.println("A");\nelse\n    System.out.println("B");\nSystem.out.println(done);',
      mutants=[("done = true", "done == true", "This reads the condition as a comparison. A single `=` assigns, and the value of an assignment expression is the value assigned (`true`).")],
      manual=[("A\nfalse", "The assignment `done = true` does change `done`, so the second statement prints `true`."),
              ("The code does not compile.", "A condition must be a `boolean` expression, and `done = true` is one (an assignment of a `boolean` value has type `boolean`), so this compiles.")],
      correct_expl="`done = true` assigns true to `done` and evaluates to true, so the `if` branch prints A, and `done` is true afterward.",
      explanation="An assignment is an expression whose value is the assigned value. With `boolean`, `if (flag = true)` compiles but is almost always a bug.")

# 8. equivalent expression
for text, ok in [("a == b", True), ("a != b", False), ("a || b", False), ("a && b", False)]:
    body = "int bad = 0;\nboolean[] v = {true, false};\nfor (boolean a : v) for (boolean b : v) if (((a && b) || (!a && !b)) != (" + text + ")) bad++;\nSystem.out.println(bad);"
    assert (run(program(body)) == "0") == ok, text
B.mcq(T_BOOL, "Which of the following is equivalent to `(a && b) || (!a && !b)`, where `a` and `b` are `boolean` variables?",
      ch("`a == b`", "The expression is true exactly when `a` and `b` are both true or both false, which is when they have the same value."),
      [ch("`a != b`", "This is true when exactly one of them is true, the opposite."),
       ch("`a || b`", "This is also true when only one is true, which the original expression rejects."),
       ch("`a && b`", "This is true only when both are true. The original is also true when both are false.")],
      "A truth table shows that the expression is true when `a` and `b` agree.")

# 9. which inputs reach a branch
body9 = 'int hits = 0;\nint lo = 1000, hi = -1000;\nfor (int n = 0; n <= 120; n++) {\n    String g = "";\n    if (n >= 90) g = "A";\n    else if (n >= 80) g = "B";\n    if (n >= 70 && n < 80) g = "C";\n    if (n < 70) g = "F";\n    if (g.equals("B")) { hits++; lo = Math.min(lo, n); hi = Math.max(hi, n); }\n}\nSystem.out.println(hits + " " + lo + " " + hi);'
assert run(program(body9)) == "10 80 89"
B.mcq(T_IF, "Assume `n` is an `int` variable. For which values of `n` does the following code segment assign \"B\" to `g`?\n\n" + code('String g = "";\nif (n >= 90)\n    g = "A";\nelse if (n >= 80)\n    g = "B";\nif (n >= 70 && n < 80)\n    g = "C";\nif (n < 70)\n    g = "F";'),
      ch("80 through 89, inclusive", "\"B\" is assigned when `n >= 80` and `n < 90` (the `else if` runs only when `n >= 90` is false). None of the later `if` statements reassigns `g` for those values."),
      [ch("80 through 100, inclusive", "For `n >= 90` the first branch assigns \"A\", so the `else if` is skipped."),
       ch("70 through 89, inclusive", "For 70 through 79 the next `if` assigns \"C\", and values below 80 never satisfy `n >= 80`."),
       ch("80 through 90, inclusive", "At `n = 90` the first condition `n >= 90` is true, so \"A\" is assigned and the `else if` is skipped.")],
      "Track the later `if` statements as well: separate `if` statements can overwrite earlier assignments, while an `else if` runs only when the previous condition was false.")

# 10. missing return on some path
src10 = program(members="    public static int sign(int n) {\n        if (n > 0)\n            return 1;\n        else if (n < 0)\n            return -1;\n    }\n")
err = compile_error(src10)
assert err and "missing return statement" in err
B.mcq(T_IFELSE, "Consider the following method.\n\n" + code("public static int sign(int n) {\n    if (n > 0)\n        return 1;\n    else if (n < 0)\n        return -1;\n}") + "\n\nWhich of the following best describes the result of compiling this method?",
      ch("The method does not compile, because there is a path (when `n` is 0) that reaches the end without returning a value.", "The compiler requires every path through a non-`void` method to return a value. Here the case `n == 0` falls through both conditions, which is a compile-time error (missing return statement)."),
      [ch("The method compiles and returns 0 when `n` is 0.", "A method does not return a default value; if no `return` runs, it is a compile-time error."),
       ch("The method compiles, but it throws an exception when `n` is 0.", "The compiler rejects the method; it never gets a chance to throw anything."),
       ch("The method compiles and returns -1 for every value of `n` that is not positive.", "The `else if (n < 0)` only returns -1 for negative values, and 0 reaches no return statement.")],
      "Every path through a method with a return type must end in a `return` (or a thrown exception).")

# 11. a null-safe condition
tests = {"str.length() > 0 && str != null": "EXC", "str != null && str.length() > 0": "ok", "str.length() > 0 || str != null": "EXC", "str == null && str.length() > 0": "EXC"}
for cond, expect in tests.items():
    try:
        run(program(f'String str = null;\nSystem.out.println({cond});'))
        got = "ok"
    except Exception:
        got = "EXC"
    assert got == expect, cond
B.mcq(T_COMP, "The variable `str` is a `String` that may be `null`. Which of the following conditions evaluates to `true` when `str` refers to a non-empty string, and to `false` (without throwing an exception) when `str` is `null`?",
      ch("`str != null && str.length() > 0`", "When `str` is `null`, `str != null` is false and `&&` skips the right operand, so `str.length()` is never called. For a non-empty string both parts are true."),
      [ch("`str.length() > 0 && str != null`", "The `length()` call is evaluated first, so it throws a `NullPointerException` when `str` is `null`."),
       ch("`str.length() > 0 || str != null`", "The left operand `str.length() > 0` is evaluated first and throws when `str` is `null`."),
       ch("`str == null && str.length() > 0`", "When `str` is `null` the left operand is true, so `&&` evaluates `str.length()`, which throws. For a non-null string it is false even if the string is non-empty.")],
      "Put the `null` check first so that short-circuit evaluation protects the method call.")

# 12. an unreachable branch
body12 = 'int count = 0;\nfor (int x = -20; x <= 40; x++) {\n    int r;\n    if (x > 0) { r = 1; } else if (x > 10) { r = 2; } else { r = 3; }\n    if (r == 2) count++;\n}\nSystem.out.println(count);'
assert run(program(body12)) == "0"
B.mcq(T_IFELSE, "Assume `x` is an `int` variable. For which values of `x` does the following code segment assign 2 to `r`?\n\n" + code("int r;\nif (x > 0)\n    r = 1;\nelse if (x > 10)\n    r = 2;\nelse\n    r = 3;"),
      ch("There is no such value of `x`.", "Any `x` greater than 10 is also greater than 0, so the first condition is true and the `else if` is never reached. The second condition can only be tested when `x <= 0`, and then `x > 10` is false."),
      [ch("Every `x` greater than 10", "These values satisfy `x > 0`, so `r` is assigned 1 and the `else if` is skipped."),
       ch("Every `x` from 1 through 10", "These values also satisfy `x > 0`, so `r` is assigned 1; and `x > 10` is false for them anyway."),
       ch("Every `x` that is greater than 0 and also greater than 10", "The `else if` is evaluated only if `x > 0` is false, so it can never be reached by such a value.")],
      "An `else if` condition is evaluated only when every earlier condition was false. Here the order makes the second branch unreachable.")

# 13. accumulating independent conditions
trace(B, T_COMP, Q, body="int n = 12;\nint score = 0;\nif (n % 2 == 0) score += 1;\nif (n % 3 == 0) score += 2;\nelse if (n % 4 == 0) score += 4;\nif (n % 4 == 0 && n % 6 == 0) score += 8;\nif (!(n % 5 == 0) || n > 10) score += 16;\nSystem.out.println(score);",
      mutants=[("else if (n % 4 == 0) score += 4;", "if (n % 4 == 0) score += 4;", "This treats `else if (n % 4 == 0)` as a separate `if`. Since `n % 3 == 0` is true, the `else if` is skipped and 4 is not added."),
               ("(!(n % 5 == 0) || n > 10)", "(!(n % 5 == 0 || n > 10))", "This moves the negation to the whole condition. In the code the `!` applies only to `n % 5 == 0`, which is true for 12 (12 is not a multiple of 5).")],
      manual=[("19", "This treats `n % 4 == 0 && n % 6 == 0` as false. 12 is divisible by both 4 and 6, so 8 is added.")],
      correct_expl="12 is even: +1. 12 % 3 == 0: +2 (and the `else if` is skipped). 12 is divisible by 4 and 6: +8. 12 is not a multiple of 5: +16. The total is 27.",
      explanation="Independent `if` statements each add their own amount, while an `else if` is skipped when the previous condition is true.")

# 14. comparing strings
trace(B, T_OBJ, Q, body='String a = "Banana", b = "apple", c = "apple";\nSystem.out.println((a.compareTo(b) < 0) + " " + (b.compareTo(c) == 0) + " " + (b == c) + " " + a.equalsIgnoreCase("BANANA") + " " + (a.toLowerCase().compareTo(b) > 0));',
      mutants=[("a.compareTo(b) < 0", "a.compareTo(b) > 0", "This assumes alphabetical order ignoring case, so \"Banana\" would come after \"apple\". `compareTo` compares character codes, and uppercase letters have smaller codes than lowercase ones.")],
      manual=[("true true false true true", "This assumes two string literals with the same characters are different objects. Identical literals refer to the same `String` object, so `b == c` is true."),
              ("true true true false true", "`equalsIgnoreCase` ignores case, so \"Banana\" and \"BANANA\" are equal.")],
      correct_expl="'B' (66) is less than 'a' (97), so `\"Banana\".compareTo(\"apple\")` is negative. `b.compareTo(c)` is 0 and `b == c` is true because the two literals are the same object. `equalsIgnoreCase` is true, and lowercase \"banana\" comes after \"apple\".",
      explanation="`compareTo` is case-sensitive and orders by character code; `equalsIgnoreCase` ignores case.")

# 15. boundary conditions in a chain
trace(B, T_IFELSE, Q, body="System.out.println(g(11) + g(10) + g(6) + g(5));",
      members='    public static String g(int x) {\n        if (x > 10)\n            return "A";\n        else if (x >= 10)\n            return "B";\n        else if (x > 5)\n            return "C";\n        else\n            return "D";\n    }\n',
      mutants=[("if (x > 10)", "if (x >= 10)", "This treats the first condition as `x >= 10`, so 10 returns \"A\" instead of falling through to the second test."),
               ("else if (x > 5)", "else if (x >= 5)", "This treats the third condition as `x >= 5`, so 5 returns \"C\". The code tests `x > 5`, so 5 reaches the `else`.")],
      manual=[("AACC", "This makes both boundary mistakes: 10 is treated as greater than 10, and 5 is treated as greater than 5.")],
      correct_expl="11 > 10: \"A\". 10 is not greater than 10 but is >= 10: \"B\". 6 > 5: \"C\". 5 is not > 5, so it reaches the `else`: \"D\".",
      explanation="Check each boundary value against `>` and `>=` carefully; the chain is evaluated top to bottom, and the first true condition wins.")

# ------------------------------------------------------------------ FRQs
members_a = '''
    public static boolean isLeapYear(int year) {
        return (year % 4 == 0 && year % 100 != 0) || year % 400 == 0;
    }

    public static int daysInMonth(int month, int year) {
        if (month < 1 || month > 12) {
            return -1;
        }
        if (month == 2) {
            if (isLeapYear(year)) {
                return 29;
            }
            return 28;
        }
        if (month == 4 || month == 6 || month == 9 || month == 11) {
            return 30;
        }
        return 31;
    }
'''
verify(members_a, [("isLeapYear(2024)", "true"), ("isLeapYear(1900)", "false"), ("isLeapYear(2000)", "true"), ("isLeapYear(2023)", "false"),
                   ("daysInMonth(2, 2024)", 29), ("daysInMonth(2, 2023)", 28), ("daysInMonth(4, 2023)", 30), ("daysInMonth(12, 2023)", 31), ("daysInMonth(13, 2023)", -1), ("daysInMonth(0, 2023)", -1)])
B.frq(T_COMP,
      "A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years unless they are also divisible by 400. For example, 2024 and 2000 are leap years, but 1900 and 2023 are not.\n\nThe class `Calendar` contains the two methods described below.\n\n```java\npublic class Calendar {\n    /** Returns true if year is a leap year and false otherwise. */\n    public static boolean isLeapYear(int year)\n    { /* to be implemented in part (a) */ }\n\n    /** Returns the number of days in the given month (1 = January through 12 = December)\n     *  of the given year, or -1 if month is not between 1 and 12. */\n    public static int daysInMonth(int month, int year)\n    { /* to be implemented in part (b) */ }\n}\n```\n\n**(a)** Write the method `isLeapYear`.\n\n**(b)** Write the method `daysInMonth`, using `isLeapYear` as appropriate. For example, `daysInMonth(2, 2024)` returns 29, `daysInMonth(4, 2023)` returns 30, and `daysInMonth(13, 2023)` returns -1.",
      [(1, "(a) Tests divisibility by 4 and excludes multiples of 100"),
       (1, "(a) Makes multiples of 400 leap years, with correct grouping of `&&` and `||`, and returns a `boolean`"),
       (1, "(b) Returns -1 for a month that is not between 1 and 12"),
       (1, "(b) Returns 30 for April, June, September and November"),
       (1, "(b) Returns 31 for the remaining months"),
       (1, "(b) Calls `isLeapYear` to return 29 or 28 for February")],
      "```java\npublic static boolean isLeapYear(int year) {\n    return (year % 4 == 0 && year % 100 != 0) || year % 400 == 0;\n}\n\npublic static int daysInMonth(int month, int year) {\n    if (month < 1 || month > 12) {\n        return -1;\n    }\n    if (month == 2) {\n        if (isLeapYear(year)) {\n            return 29;\n        }\n        return 28;\n    }\n    if (month == 4 || month == 6 || month == 9 || month == 11) {\n        return 30;\n    }\n    return 31;\n}\n```\nThe parentheses in `isLeapYear` matter: `&&` binds tighter than `||`, so a year divisible by 400 is a leap year even though it is also divisible by 100.")

members_b = '''
    public static boolean isTriangle(int a, int b, int c) {
        return a > 0 && b > 0 && c > 0 && a + b > c && a + c > b && b + c > a;
    }

    public static String typeOf(int a, int b, int c) {
        if (!isTriangle(a, b, c)) {
            return "invalid";
        }
        if (a == b && b == c) {
            return "equilateral";
        }
        if (a == b || b == c || a == c) {
            return "isosceles";
        }
        return "scalene";
    }
'''
verify(members_b, [("isTriangle(3, 4, 5)", "true"), ("isTriangle(1, 2, 3)", "false"), ("isTriangle(0, 4, 5)", "false"), ("isTriangle(5, 5, 9)", "true"),
                   ("typeOf(3, 3, 3)", "equilateral"), ("typeOf(5, 5, 8)", "isosceles"), ("typeOf(8, 5, 5)", "isosceles"), ("typeOf(3, 4, 5)", "scalene"), ("typeOf(1, 2, 3)", "invalid")])
B.frq(T_IF,
      "Three positive side lengths form a triangle only if the sum of any two of them is greater than the third. For example, 3, 4 and 5 form a triangle, but 1, 2 and 3 do not.\n\nThe class `TriangleTools` contains the two methods described below.\n\n```java\npublic class TriangleTools {\n    /** Returns true if a, b and c are all positive and form a triangle; false otherwise. */\n    public static boolean isTriangle(int a, int b, int c)\n    { /* to be implemented in part (a) */ }\n\n    /** Returns \"invalid\" if a, b and c do not form a triangle. Otherwise returns\n     *  \"equilateral\" if all three sides are equal, \"isosceles\" if exactly two sides are equal,\n     *  and \"scalene\" if no two sides are equal. */\n    public static String typeOf(int a, int b, int c)\n    { /* to be implemented in part (b) */ }\n}\n```\n\n**(a)** Write the method `isTriangle`.\n\n**(b)** Write the method `typeOf`, using `isTriangle` as appropriate. For example, `typeOf(3, 3, 3)` returns `\"equilateral\"`, `typeOf(8, 5, 5)` returns `\"isosceles\"`, `typeOf(3, 4, 5)` returns `\"scalene\"` and `typeOf(1, 2, 3)` returns `\"invalid\"`.",
      [(1, "(a) Checks that all three sides are positive"),
       (1, "(a) Checks all three triangle inequalities (not only one)"),
       (1, "(a) Combines the conditions with the correct logical operators and returns a `boolean`"),
       (1, "(b) Calls `isTriangle` and returns \"invalid\" when it is false"),
       (1, "(b) Tests for equilateral before isosceles, so that three equal sides are not classified as isosceles"),
       (1, "(b) Tests for isosceles by comparing all three pairs of sides"),
       (1, "(b) Returns \"scalene\" otherwise")],
      "```java\npublic static boolean isTriangle(int a, int b, int c) {\n    return a > 0 && b > 0 && c > 0 && a + b > c && a + c > b && b + c > a;\n}\n\npublic static String typeOf(int a, int b, int c) {\n    if (!isTriangle(a, b, c)) {\n        return \"invalid\";\n    }\n    if (a == b && b == c) {\n        return \"equilateral\";\n    }\n    if (a == b || b == c || a == c) {\n        return \"isosceles\";\n    }\n    return \"scalene\";\n}\n```\nThe equilateral test must come before the isosceles test: a triangle with three equal sides also has two equal sides, and the first matching `if` wins.")

B.save()
B.brief()
