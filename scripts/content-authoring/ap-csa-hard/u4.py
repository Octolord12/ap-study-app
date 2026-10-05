from common import *

B = bank(4, "unit-4-iteration")
T_WH, T_FOR, T_NEST, T_INFO = ("while-loops", "for-loops", "nested-iteration", "informal-code-analysis")
Q = "What is printed as a result of executing the following code segment?"

trace(B, T_WH, Q, body="int n = 6;\nint steps = 0;\nwhile (n > 1) {\n    if (n % 2 == 0)\n        n /= 2;\n    else\n        n = 3 * n + 1;\n    steps++;\n}\nSystem.out.println(steps + \" \" + n);",
      mutants=[("steps++;", "if (n % 2 == 0) steps++;", "This counts only some of the iterations. In the original, `steps++` is outside the `if`/`else`, so every pass through the loop is counted, including the ones that multiply by 3 and add 1."),
               ("while (n > 1)", "while (n > 2)", "This stops one pass early. The loop condition is `n > 1`, so the loop continues until `n` is 1.")],
      manual=[("9 1", "This counts one pass too many. The sequence is 6, 3, 10, 5, 16, 8, 4, 2, 1, which is 8 changes, and the loop ends as soon as `n` is 1.")],
      correct_expl="n goes 6, 3, 10, 5, 16, 8, 4, 2, 1. That is 8 passes through the loop, and the loop stops when `n` becomes 1.",
      explanation="Trace the value of the loop variable and count every pass. The loop ends when its condition first becomes false.")

trace(B, T_FOR, Q, body="int c1 = 0, c2 = 0;\nfor (int i = 1; i <= 20; i *= 2)\n    c1++;\nfor (int j = 0; j < 20; j += 6)\n    c2++;\nSystem.out.println(c1 + \" \" + c2);",
      mutants=[("i *= 2", "i += 2", "This adds 2 each time (1, 3, 5, ..., 19). The loop multiplies: 1, 2, 4, 8, 16.")],
      manual=[("4 4", "This stops before 16. `i` takes the values 1, 2, 4, 8 and 16, and 16 <= 20 is true, so the body runs 5 times."),
              ("5 3", "This leaves out `j = 0`. The first loop pass uses `j = 0`; the values are 0, 6, 12 and 18, which is 4 passes.")],
      correct_expl="`i` takes the values 1, 2, 4, 8, 16 (five values <= 20). `j` takes 0, 6, 12, 18 (four values < 20).",
      explanation="List the values of the loop variable. A loop that starts at 0 includes 0; one that multiplies doubles each time.")

trace(B, T_NEST, Q, body="for (int i = 1; i <= 4; i++) {\n    for (int j = i; j <= 4; j++)\n        System.out.print(j);\n    System.out.println();\n}",
      mutants=[("int j = i;", "int j = 1;", "This starts every inner loop at 1. In the original the inner loop starts at the current value of `i`, so each line is shorter."),
               ("j <= 4; j++)", "j <= i; j++)", "This ends the inner loop at `i`, so each line would print only the digits from `i` up to `i`: a single digit."),
               ("int i = 1; i <= 4", "int i = 1; i < 4", "This runs the outer loop only three times. The condition `i <= 4` includes 4, so there is a fourth line.")],
      correct_expl="Row `i` prints the digits from `i` through 4: 1234, 234, 34, 4.",
      explanation="The inner loop restarts for each outer pass, and here its starting value depends on the outer variable.")

trace(B, T_FOR, Q, body="String s = \"mississippi\";\nString out = \"\";\nfor (int i = 0; i < s.length(); i++) {\n    if (i == 0 || s.charAt(i) != s.charAt(i - 1))\n        out += s.charAt(i);\n}\nSystem.out.println(out);",
      mutants=[("s.charAt(i) != s.charAt(i - 1)", "s.charAt(i) == s.charAt(i - 1)", "This keeps only the characters that repeat the previous one. The code keeps a character only when it differs from the previous one.")],
      manual=[("misp", "This removes every duplicate letter. The code removes only *consecutive* repeats, so the \"s\" and \"i\" appear again after other letters."),
              ("mississippi", "This assumes nothing is removed. The repeated \"ss\", \"ss\" and \"pp\" are collapsed to single letters.")],
      correct_expl="Consecutive repeats are skipped: m, i, s (skip s), i, s (skip s), i, p (skip p), i, giving \"misisipi\".",
      explanation="`i == 0 ||` protects the first character, which has no previous character. Only consecutive duplicates are removed.")

trace(B, T_FOR, Q, body="int sum = 0;\nfor (int i = 1; i < 10; i++) {\n    if (i % 3 == 0 || i % 4 == 0)\n        sum += i;\n}\nSystem.out.println(sum);",
      mutants=[("i < 10", "i <= 12", "This lets the loop run through 12, so it also adds 12 (a multiple of both 3 and 4). The actual loop stops at 9, so values above 9 are never tested."),
               ("||", "&&", "This requires both conditions. Using `||` adds every number that is a multiple of 3 or of 4 (or both).")],
      manual=[("18", "This adds only the multiples of 3 (3 + 6 + 9). The multiples of 4 (4 and 8) also satisfy the condition.")],
      correct_expl="The values from 1 through 9 that are multiples of 3 or 4 are 3, 4, 6, 8 and 9. Their sum is 30.",
      explanation="`||` is true if either condition is true, and the loop condition `i < 10` excludes 10.")

trace(B, T_WH, Q, body="int x = 5, loops = 0;\nwhile (x < 30) {\n    x += 4;\n    if (x % 3 == 0)\n        x++;\n    loops++;\n}\nSystem.out.println(loops + \" \" + x);",
      mutants=[("x += 4;", "x += 3;", "This adds 3 each pass. The code adds 4, so `x` grows faster and the loop ends sooner."),
               ("x % 3 == 0", "x % 2 == 0", "This adds the extra 1 when `x` is even instead of when it is a multiple of 3, so the values of `x` differ from the actual trace.")],
      manual=[("5 32", "This is one pass short. The sequence of `x` is 9 (then 10), 14, 18 (then 19), 23, 27 (then 28), 32: six passes.")],
      correct_expl="x goes 5 to 9 (a multiple of 3, so 10), then 14, 18 (multiple of 3, so 19), 23, 27 (multiple of 3, so 28), 32. That is six passes, and 32 is not less than 30.",
      explanation="Update the variable in the same order as the code, including the conditional adjustment in the body.")

trace(B, T_NEST, Q, body="int n = 6, count = 0;\nfor (int i = 0; i < n; i++)\n    for (int j = i; j < n; j++)\n        count++;\nSystem.out.println(count);",
      mutants=[("int j = i;", "int j = 0;", "This runs the inner loop n times for each of the n outer passes (36). Here the inner loop starts at `i`, so later passes are shorter."),
               ("int j = i;", "int j = i + 1;", "This starts the inner loop one value later, which skips the pair where `j == i` on every pass."),
               ("j < n", "j < i", "This condition is false immediately because `j` starts at `i`; the inner body would never run.")],
      correct_expl="Pass `i` of the outer loop runs the inner loop for `j = i` through 5, which is 6 - i times: 6 + 5 + 4 + 3 + 2 + 1 = 21.",
      explanation="Count the inner iterations for each value of the outer variable and add them: it is a triangular number.")

trace(B, T_INFO, Q, body="int count = 0;\nfor (int i = 1; i <= 5; i++)\n    for (int j = 1; j <= i * 2; j++)\n        count++;\nSystem.out.println(count);",
      mutants=[("j <= i * 2", "j < i * 2", "This stops one pass early on each outer pass (1, 3, 5, 7, 9). The condition `j <= i * 2` includes `i * 2`."),
               ("j <= i * 2", "j <= i", "This runs the inner loop `i` times instead of `2 * i` times."),
               ("i <= 5", "i < 5", "This leaves out the last outer pass (`i = 5`, which contributes 10).")],
      correct_expl="The inner loop runs 2i times for i = 1 through 5: 2 + 4 + 6 + 8 + 10 = 30.",
      explanation="Sum the inner loop counts for each value of the outer variable.")

trace(B, T_FOR, Q, body="String s = \"\";\nfor (char c = 'a'; c < 'h'; c += 3)\n    s += c + \"\" + (int) c % 10;\nSystem.out.println(s);",
      mutants=[("c += 3", "c += 2", "This steps by 2 instead of 3, visiting a, c, e and g."),
               ("c + \"\" + (int) c % 10", "c + (int) c % 10", "This leaves out the empty string. Without it, `c + (int) c % 10` is an `int` addition (the character's code plus the digit), not a concatenation.")],
      manual=[("a97d100g103", "This leaves out the `% 10`. The expression `(int) c % 10` is the last digit of the character code: 97 gives 7, 100 gives 0, 103 gives 3.")],
      correct_expl="`c` takes 'a' (97), 'd' (100) and 'g' (103); 'j' is not less than 'h'. Each pass appends the character and the last digit of its code: a7, d0, g3.",
      explanation="A `char` loop variable steps through character codes. `(int) c % 10` takes the last digit of the code, and `c + \"\"` forces concatenation.")

trace(B, T_FOR, Q, body="String s = \"education\";\nint pos = -1;\nfor (int i = 0; i < s.length(); i++) {\n    if (\"aeiou\".indexOf(s.substring(i, i + 1)) >= 0)\n        pos = i;\n}\nSystem.out.println(pos);",
      mutants=[("pos = i;", "if (pos == -1) pos = i;", "This records the *first* vowel (index 0). Without the extra test, every vowel overwrites `pos`, so the final value is the last vowel's index.")],
      manual=[("4", "This is the index of the \"a\", not the last vowel. \"education\" has vowels at indexes 0, 2, 4, 6 and 7, and the last one is \"o\" at index 7."),
              ("8", "This is the last index of the string, which is the \"n\". The assignment happens only when the character is a vowel.")],
      correct_expl="The vowels in \"education\" are at indexes 0 (e), 2 (u), 4 (a), 6 (i) and 7 (o). Each one overwrites `pos`, so the final value is 7.",
      explanation="An assignment inside the loop that is not guarded keeps the value from the last time the condition was true.")

trace(B, T_WH, Q, body="int i = 0;\nwhile (i < 3)\n    i++;\nfor ( ; i < 7; i += 2) {\n}\nSystem.out.println(i);",
      mutants=[("i < 7", "i <= 7", "This continues while `i <= 7`. With `i < 7`, `i` reaches 7 and the loop stops."),],
      manual=[("3", "This ignores the `for` loop. It has no initialization, so it starts with the current value of `i` (3) and keeps adding 2: 5, then 7."),
              ("5", "This stops one pass early. After 5, `i < 7` is still true, so `i` becomes 7.")],
      correct_expl="The `while` loop leaves `i` at 3. The `for` loop has no initializer, so it starts from 3: 3 < 7 (i becomes 5), 5 < 7 (i becomes 7), and 7 < 7 is false. `i` is 7.",
      explanation="A `for` loop may omit its initialization; the loop variable keeps whatever value it already has.")

trace(B, T_INFO, Q, body="int a = 1, b = 1;\nfor (int i = 0; i < 6; i++) {\n    int t = a + b;\n    a = b;\n    b = t;\n}\nSystem.out.println(a + \" \" + b);",
      mutants=[("int t = a + b;\n    a = b;\n    b = t;", "a = b;\n    b = a + b;", "This overwrites `a` before using it, so the new `b` is `b + b`. The temporary variable `t` keeps the old sum."),
               ("i < 6", "i <= 6", "This runs the loop seven times instead of six.")],
      manual=[("8 13", "This is one pass short. After six passes the pairs are (1, 2), (2, 3), (3, 5), (5, 8), (8, 13), (13, 21).")],
      correct_expl="Each pass makes (a, b) become (b, a + b). Starting from (1, 1): (1, 2), (2, 3), (3, 5), (5, 8), (8, 13), (13, 21) after six passes.",
      explanation="Update variables in an order that doesn't destroy a value you still need; a temporary variable holds the old sum.")

trace(B, T_NEST, Q, body="for (int i = 1; i <= 3; i++) {\n    for (int j = 1; j <= 3; j++) {\n        if (i == j)\n            System.out.print(\"X\");\n        else\n            System.out.print(\"-\");\n    }\n    System.out.println();\n}",
      mutants=[("i == j", "i + j == 4", "This marks the other diagonal (where i + j equals 4)."),
               ("i == j", "i < j", "This marks the cells above the main diagonal instead of on it."),
               ("i == j", "i <= j", "This marks the diagonal and everything above it.")],
      correct_expl="An X is printed when the row number equals the column number, so the X's lie on the main diagonal.",
      explanation="Print rows with the inner loop (columns) and end each row with `println`. The condition decides which cells are marked.")

trace(B, T_FOR, Q, body="String s = \"to be  or not\";\nint spaces = 0, words = 0;\nfor (int i = 0; i < s.length(); i++) {\n    if (s.charAt(i) == ' ')\n        spaces++;\n    if (s.charAt(i) != ' ' && (i == 0 || s.charAt(i - 1) == ' '))\n        words++;\n}\nSystem.out.println(words + \" \" + (spaces + 1));",
      manual=[("5 5", "This takes `spaces + 1` as the number of words. The double space between \"be\" and \"or\" is counted as two spaces but does not create an extra word."),
              ("4 4", "This leaves out the `+ 1`: the second number printed is `spaces + 1`, and there are 4 spaces."),
              ("3 5", "This misses the first word. The test `i == 0 ||` counts a word that begins at the start of the string.")],
      correct_expl="The string \"to be  or not\" has four words (to, be, or, not) and four spaces (two of them next to each other). The code counts a word each time a non-space follows a space or the start: 4. Then `spaces + 1` is 5.",
      explanation="Counting spaces overcounts when spaces repeat; counting where a word begins is reliable.")

trace(B, T_INFO, Q, body="int n = 49, checks = 0;\nboolean prime = n > 1;\nfor (int d = 2; d * d <= n; d++) {\n    checks++;\n    if (n % d == 0)\n        prime = false;\n}\nSystem.out.println(prime + \" \" + checks);",
      mutants=[("d * d <= n", "d * d < n", "This stops before `d = 7`, the divisor that proves 49 composite. With `d * d <= n` the loop includes d = 7 because 49 <= 49."),
               ("d * d <= n", "d < n / 2", "This tests many more divisors than needed. The loop in the code stops once `d * d` exceeds `n`.")],
      manual=[("true 6", "This assumes 49 is prime. 49 = 7 * 7, so when `d` is 7 the test `n % d == 0` is true.")],
      correct_expl="`d` runs from 2 through 7 (7 * 7 = 49 <= 49): six passes. At d = 7, 49 % 7 == 0, so `prime` becomes false.",
      explanation="Using `d * d <= n` (not `<`) is what makes the loop test the square root of a perfect square.")

# ------------------------------------------------------------------ FRQs
members_a = '''
    public static String compress(String s) {
        String result = "";
        int i = 0;
        while (i < s.length()) {
            char c = s.charAt(i);
            int count = 0;
            while (i < s.length() && s.charAt(i) == c) {
                count++;
                i++;
            }
            result += c + "" + count;
        }
        return result;
    }

    public static int longestRun(String s) {
        int best = 0;
        int run = 0;
        for (int i = 0; i < s.length(); i++) {
            if (i > 0 && s.charAt(i) == s.charAt(i - 1)) {
                run++;
            } else {
                run = 1;
            }
            if (run > best) {
                best = run;
            }
        }
        return best;
    }
'''
verify(members_a, [('compress("aaabcc")', "a3b1c2"), ('compress("x")', "x1"), ('compress("")', ""), ('compress("aabbbaa")', "a2b3a2"),
                   ('longestRun("aaabccddddd")', 5), ('longestRun("")', 0), ('longestRun("abc")', 1), ('longestRun("aabbb")', 3)])
B.frq(T_WH,
      "The class `RunTools` contains the two methods described below. In both methods, a *run* is a sequence of one or more identical consecutive characters.\n\n```java\npublic class RunTools {\n    /** Returns a String in which each run in s is replaced by the character followed by\n     *  the length of the run. For example, compress(\"aaabcc\") returns \"a3b1c2\".\n     *  compress(\"\") returns \"\". */\n    public static String compress(String s)\n    { /* to be implemented in part (a) */ }\n\n    /** Returns the length of the longest run in s, or 0 if s is empty.\n     *  For example, longestRun(\"aaabccddddd\") returns 5. */\n    public static int longestRun(String s)\n    { /* to be implemented in part (b) */ }\n}\n```\n\n**(a)** Write the method `compress`.\n\n**(b)** Write the method `longestRun`.",
      [(1, "(a) Traverses the whole string with a loop that handles one run at a time"),
       (1, "(a) Counts the length of each run correctly, including the last run"),
       (1, "(a) Appends each character followed by its count to the result"),
       (1, "(a) Returns the correct String, including `\"\"` for an empty string"),
       (1, "(b) Traverses the string and compares each character with the previous one without going out of bounds"),
       (1, "(b) Maintains the length of the current run, restarting it at 1 when a new run begins"),
       (1, "(b) Tracks and returns the maximum run length (0 for an empty string)")],
      "```java\npublic static String compress(String s) {\n    String result = \"\";\n    int i = 0;\n    while (i < s.length()) {\n        char c = s.charAt(i);\n        int count = 0;\n        while (i < s.length() && s.charAt(i) == c) {\n            count++;\n            i++;\n        }\n        result += c + \"\" + count;\n    }\n    return result;\n}\n\npublic static int longestRun(String s) {\n    int best = 0;\n    int run = 0;\n    for (int i = 0; i < s.length(); i++) {\n        if (i > 0 && s.charAt(i) == s.charAt(i - 1)) {\n            run++;\n        } else {\n            run = 1;\n        }\n        if (run > best) {\n            best = run;\n        }\n    }\n    return best;\n}\n```\nIn `compress`, the inner loop's first test `i < s.length()` prevents an out-of-bounds access at the end of the string, and `c + \"\" + count` forces string concatenation.")

members_b = '''
    public static int sumProperDivisors(int n) {
        int sum = 0;
        for (int d = 1; d < n; d++) {
            if (n % d == 0) {
                sum += d;
            }
        }
        return sum;
    }

    public static boolean isPerfect(int n) {
        return sumProperDivisors(n) == n;
    }

    public static int countPerfect(int low, int high) {
        int count = 0;
        for (int n = low; n <= high; n++) {
            if (isPerfect(n)) {
                count++;
            }
        }
        return count;
    }
'''
verify(members_b, [("sumProperDivisors(12)", 16), ("sumProperDivisors(7)", 1), ("sumProperDivisors(1)", 0), ("isPerfect(6)", "true"), ("isPerfect(28)", "true"), ("isPerfect(12)", "false"),
                   ("isPerfect(1)", "false"), ("isPerfect(496)", "true"), ("countPerfect(1, 100)", 2), ("countPerfect(1, 10000)", 4), ("countPerfect(7, 27)", 0)])
B.frq(T_NEST,
      "A *proper divisor* of a positive integer `n` is a positive integer less than `n` that divides `n` evenly. For example, the proper divisors of 12 are 1, 2, 3, 4 and 6. A positive integer is *perfect* if it is greater than 1 and equals the sum of its proper divisors. For example, 6 is perfect because $1+2+3=6$.\n\nThe class `NumberTools` contains the three methods described below.\n\n```java\npublic class NumberTools {\n    /** Returns the sum of the proper divisors of n. Precondition: n >= 1.\n     *  For example, sumProperDivisors(12) returns 16 and sumProperDivisors(1) returns 0. */\n    public static int sumProperDivisors(int n)\n    { /* to be implemented in part (a) */ }\n\n    /** Returns true if n is perfect and false otherwise. */\n    public static boolean isPerfect(int n)\n    { /* to be implemented in part (b) */ }\n\n    /** Returns the number of perfect numbers from low through high, inclusive.\n     *  Precondition: 1 <= low <= high */\n    public static int countPerfect(int low, int high)\n    { /* to be implemented in part (c) */ }\n}\n```\n\n**(a)** Write the method `sumProperDivisors`.\n\n**(b)** Write the method `isPerfect`, using `sumProperDivisors` as appropriate. For example, `isPerfect(28)` returns `true`, and `isPerfect(12)` and `isPerfect(1)` return `false`.\n\n**(c)** Write the method `countPerfect`, using `isPerfect` as appropriate. For example, `countPerfect(1, 100)` returns 2 (the perfect numbers 6 and 28).",
      [(1, "(a) Loops over the candidate divisors from 1 up to but not including n"),
       (1, "(a) Tests divisibility with `%` and accumulates the sum"),
       (1, "(a) Returns the sum (0 for n = 1)"),
       (1, "(b) Calls `sumProperDivisors` and compares the result with n"),
       (1, "(b) Returns the correct boolean for every n, including 1"),
       (1, "(c) Loops through every value from `low` through `high` inclusive"),
       (1, "(c) Calls `isPerfect`, counts the true results and returns the count")],
      "```java\npublic static int sumProperDivisors(int n) {\n    int sum = 0;\n    for (int d = 1; d < n; d++) {\n        if (n % d == 0) {\n            sum += d;\n        }\n    }\n    return sum;\n}\n\npublic static boolean isPerfect(int n) {\n    return sumProperDivisors(n) == n;\n}\n\npublic static int countPerfect(int low, int high) {\n    int count = 0;\n    for (int n = low; n <= high; n++) {\n        if (isPerfect(n)) {\n            count++;\n        }\n    }\n    return count;\n}\n```\nNo special case is needed for 1: its proper divisor sum is 0, which is not equal to 1, so `isPerfect(1)` is already false.")

B.save()
B.brief()
