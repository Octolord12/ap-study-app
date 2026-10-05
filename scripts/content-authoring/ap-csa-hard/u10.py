from common import *

B = bank(10, "unit-10-recursion")
T_REC, T_SRCH = ("recursion-basics", "recursive-searching-sorting")
Q = "What is printed as a result of executing the following code segment?"

# 1. two recursive calls with output before and after
F1 = '''public static void f(int n) {
    if (n <= 0) {
        return;
    }
    System.out.print(n + " ");
    f(n - 2);
    f(n - 1);
    System.out.print("* ");
}'''
trace(B, T_REC, Q, body="f(3);\nSystem.out.println();", members="    " + F1.replace("\n", "\n    ") + "\n",
      mutants=[("f(n - 2);\n        f(n - 1);", "f(n - 1);\n        f(n - 2);", "This calls `f(n - 1)` before `f(n - 2)`. The method makes the call with `n - 2` first."),
               ("n <= 0", "n < 0", "This lets the call with `n` equal to 0 print a 0 and continue. The base case `n <= 0` returns immediately for 0.")],
      manual=[("3 1 * *", "This stops after the first recursive call. After `f(n - 2)` returns, the method also calls `f(n - 1)`, and each call prints a star when both calls are finished.")],
      correct_expl="`f(3)` prints 3, then `f(1)` prints 1 (its calls with -1 and 0 print nothing) and a star; then `f(2)` prints 2, calls `f(0)` (nothing) and `f(1)` (prints 1 and a star), and prints a star; finally `f(3)` prints a star. Output: 3 1 * 2 1 * * *.",
      explanation="Output printed before a recursive call comes out in call order; output printed after it comes out as the calls return.")

# 2. recurrence
G2 = '''public static int g(int n) {
    if (n < 3) {
        return n;
    }
    return g(n - 1) + g(n - 3);
}'''
trace(B, T_REC, "What is printed as a result of executing the following code segment?", body="System.out.println(g(7));", members="    " + G2.replace("\n", "\n    ") + "\n",
      mutants=[("return n;", "return 1;", "This treats every base case as returning 1. For `n` less than 3, the method returns `n` itself: g(0) is 0, g(1) is 1 and g(2) is 2."),
               ("n < 3", "n <= 3", "This returns 3 for g(3). The base case applies only to `n < 3`; g(3) is g(2) + g(0)."),
               ("g(n - 3)", "g(n - 2)", "This reads the second call as `g(n - 2)`, which gives a different recurrence. The method adds `g(n - 1)` and `g(n - 3)`.")],
      correct_expl="g(0) = 0, g(1) = 1 and g(2) = 2 are base cases. Then g(3) = g(2) + g(0) = 2, g(4) = g(3) + g(1) = 3, g(5) = g(4) + g(2) = 5, g(6) = g(5) + g(3) = 7 and g(7) = g(6) + g(4) = 10.",
      explanation="Evaluate a recurrence from the base cases upward, keeping a table of the values you have already found.")

# 3. count the calls
FIB = '''static int calls = 0;

public static int fib(int n) {
    calls++;
    if (n <= 1) {
        return n;
    }
    return fib(n - 1) + fib(n - 2);
}'''
trace(B, T_REC, Q, body='System.out.println(fib(5) + " " + calls);', members="    " + FIB.replace("\n", "\n    ") + "\n",
      mutants=[("calls++;", "if (n <= 1) calls++;", "This counts only the calls that reach the base case. Every call is counted, including those that go on to make two more calls.")],
      manual=[("5 5", "This counts one call for each value of `n` from 1 to 5. The same values are computed again and again: `fib(3)` runs twice and `fib(2)` three times."),
              ("5 7", "7 is the number of calls that make further calls. The 8 calls that stop at the base case also increment `calls`.")],
      correct_expl="`fib(5)` returns 5. Let c(n) be the number of calls made by `fib(n)`, including itself: c(0) = c(1) = 1 and c(n) = 1 + c(n - 1) + c(n - 2), which gives 3, 5, 9 and 15 for n = 2 to 5. So `calls` is 15.",
      explanation="A recursive method that makes two calls recomputes the same values many times; count all calls in the tree, not just the distinct arguments.")

# 4. weaving strings
W4 = '''public static String weave(String a, String b) {
    if (a.length() == 0) {
        return b;
    }
    return a.charAt(0) + weave(b, a.substring(1));
}'''
trace(B, T_REC, Q, body='System.out.println(weave("abc", "XYZ") + " " + weave("ab", "XYZ") + " [" + weave("", "Q") + "]");', members="    " + W4.replace("\n", "\n    ") + "\n",
      mutants=[("weave(b, a.substring(1))", "weave(a.substring(1), b)", "This keeps the strings in the same order in each call, so the characters are not interleaved. The call swaps them: `weave(b, a.substring(1))`."),
               ("return b;", "return \"\";", "This drops the letters left in `b` when `a` is empty. The base case returns `b`, so the leftover letters are added to the end.")],
      manual=[("aXbYcZ aXbYZ []", "`weave(\"\", \"Q\")` has an empty first string, so the base case returns the second string, \"Q\".")],
      correct_expl="Each call takes the first letter of `a`, then swaps the roles of the strings. `weave(\"abc\", \"XYZ\")` gives a, X, b, Y, c, Z. For `weave(\"ab\", \"XYZ\")`: a, X, b, Y, and then `a` is empty (after the swap) with \"Z\" left, which the base case returns: aXbYZ. `weave(\"\", \"Q\")` returns \"Q\".",
      explanation="When two arguments swap roles in each call, track which string is currently `a` and which is `b`, and remember what the base case returns.")

# 5. recursive binary search: results and number of calls
BS = '''static int calls = 0;

public static int bs(int[] a, int t, int lo, int hi) {
    calls++;
    if (lo > hi) {
        return -1;
    }
    int mid = (lo + hi) / 2;
    if (a[mid] == t) {
        return mid;
    }
    if (a[mid] < t) {
        return bs(a, t, mid + 1, hi);
    }
    return bs(a, t, lo, mid - 1);
}'''
trace(B, T_SRCH, Q, body="int[] a = {3, 8, 12, 15, 21, 27, 34, 40, 52};\nint x = bs(a, 27, 0, a.length - 1);\nint y = bs(a, 10, 0, a.length - 1);\nSystem.out.println(x + \" \" + y + \" \" + calls);", members="    " + BS.replace("\n", "\n    ") + "\n",
      mutants=[("(lo + hi) / 2", "(lo + hi + 1) / 2", "This rounds the midpoint up, which changes which elements are examined and adds a call. The method uses integer division, `(lo + hi) / 2`, which rounds down."),
               ("lo > hi", "lo >= hi", "This stops when `lo` equals `hi`, so a one-element range is never examined and 27 is not found. The method stops only when `lo > hi`.")],
      manual=[("5 -1 4", "`calls` is a static variable shared by both searches, so it also includes the 3 calls made for 27."),
              ("5 -1 3", "`calls` counts the calls for both searches, 3 for 27 and 4 for 10.")],
      correct_expl="Searching for 27 examines index 4 (21), then index 6 (34), then index 5 (27): found at index 5 after 3 calls. Searching for 10 examines index 4 (21), index 1 (8), index 2 (12), and then `lo` (2) is greater than `hi` (1): -1 after 4 calls. `calls` is 3 + 4 = 7.",
      explanation="Binary search halves the range each call; trace `lo`, `hi` and `mid` carefully, and note that a static counter accumulates across all searches.")

# 6. merge sort: output order
MS = '''public static void sort(int[] a, int lo, int hi) {
    if (lo >= hi) {
        return;
    }
    int mid = (lo + hi) / 2;
    sort(a, lo, mid);
    sort(a, mid + 1, hi);
    merge(a, lo, mid, hi);
    String s = "";
    for (int i = lo; i <= hi; i++) {
        s += a[i];
    }
    System.out.print(s + " ");
}'''
MG = '''public static void merge(int[] a, int lo, int mid, int hi) {
    int[] t = new int[hi - lo + 1];
    int i = lo, j = mid + 1, k = 0;
    while (i <= mid && j <= hi) {
        if (a[i] <= a[j]) {
            t[k++] = a[i++];
        } else {
            t[k++] = a[j++];
        }
    }
    while (i <= mid) {
        t[k++] = a[i++];
    }
    while (j <= hi) {
        t[k++] = a[j++];
    }
    for (k = 0; k < t.length; k++) {
        a[lo + k] = t[k];
    }
}'''
trace(B, T_SRCH, Q + "\n\nThe method `merge` merges the sorted ranges `a[lo..mid]` and `a[mid + 1..hi]` into one sorted range `a[lo..hi]`.", body="int[] a = {5, 2, 4, 1, 3};\nsort(a, 0, a.length - 1);\nSystem.out.println();", members="    " + MS.replace("\n", "\n    ") + "\n\n    " + MG.replace("\n", "\n    ") + "\n",
      mutants=[("sort(a, lo, mid);\n        sort(a, mid + 1, hi);", "sort(a, mid + 1, hi);\n        sort(a, lo, mid);", "This sorts the right half before the left half. The method sorts `a[lo..mid]` first, so the ranges are reported from the left."),
               ("merge(a, lo, mid, hi);\n        String s = \"\";\n        for (int i = lo; i <= hi; i++) {\n            s += a[i];\n        }\n        System.out.print(s + \" \");", "String s = \"\";\n        for (int i = lo; i <= hi; i++) {\n            s += a[i];\n        }\n        System.out.print(s + \" \");\n        merge(a, lo, mid, hi);", "This reports each range before it is merged, so the digits appear in their unsorted order. The method merges first and then prints the sorted range.")],
      manual=[("245 13 12345", "This leaves out the range 0 to 1. The call `sort(a, 0, 2)` first sorts the range 0 to 1 (which merges 5 and 2 and prints 25) before merging in the element at index 2.")],
      correct_expl="`sort(a, 0, 4)` calls `sort(a, 0, 2)` first. That calls `sort(a, 0, 1)`, which merges 5 and 2 and prints 25; then it merges in 4 and prints 245. Next `sort(a, 3, 4)` merges 1 and 3 and prints 13. Finally the whole array is merged and prints 12345. Output: 25 245 13 12345.",
      explanation="Merge sort prints a range only after both of its halves are sorted and merged, so smaller ranges are reported before the ranges that contain them.")

# 7. fast exponentiation: result and calls
P7 = '''static int calls = 0;

public static int pow(int b, int e) {
    calls++;
    if (e == 0) {
        return 1;
    }
    if (e % 2 == 0) {
        int h = pow(b, e / 2);
        return h * h;
    }
    return b * pow(b, e - 1);
}'''
trace(B, T_REC, Q, body='System.out.println(pow(3, 10) + " " + calls);', members="    " + P7.replace("\n", "\n    ") + "\n",
      mutants=[("h * h", "h + h", "This adds the half-power to itself instead of squaring it. The method multiplies, `h * h`.")],
      manual=[("59049 11", "This would be the number of calls if the exponent went down by 1 each time. For an even exponent the method halves it, so the exponents are 10, 5, 4, 2, 1 and 0."),
              ("59049 5", "The call with `e` equal to 0 is also a call, and it increments `calls`; the calls are for 10, 5, 4, 2, 1 and 0.")],
      correct_expl="3 to the 10th power is 59049. The calls use the exponents 10 (even, halve), 5 (odd, subtract 1), 4, 2, 1 and 0, which is 6 calls.",
      explanation="Using the exponent's parity, the method needs only about log2 of the exponent calls instead of one per unit.")

# 8. converting to a base
C8 = '''public static String conv(int n, int base) {
    if (n < base) {
        return "" + n;
    }
    return conv(n / base, base) + n % base;
}'''
trace(B, T_REC, Q, body='System.out.println(conv(37, 3) + " " + conv(37, 2) + " " + conv(2, 3));', members="    " + C8.replace("\n", "\n    ") + "\n",
      mutants=[("conv(n / base, base) + n % base", "n % base + conv(n / base, base)", "This puts each remainder in front of the result of the recursive call, so the digits come out reversed. The remainder is appended after it."),
               ("conv(n / base, base) + n % base", "conv(n % base, base) + n / base", "This swaps `/` and `%`. The recursive call is on the quotient, `n / base`, and the remainder `n % base` is appended."),
               ("n < base", "n <= base", "This treats `n` equal to the base as a single digit, which gives a digit that is not valid in that base. The base case is `n < base`.")],
      correct_expl="37 = 1 * 27 + 1 * 9 + 0 * 3 + 1, so `conv(37, 3)` is 1101. 37 in base 2 is 100101. `conv(2, 3)`: 2 < 3, so it returns \"2\". Each recursive call computes the digits of the quotient first, and the remainder is appended last.",
      explanation="Appending the remainder after the recursive result gives digits in the correct order (most significant first).")

# 9. which call terminates
F9 = 'public static int f(int n) {\n    if (n == 0) {\n        return 0;\n    }\n    return n + f(n - 3);\n}'
def f9(n):
    try:
        return run(program(f"System.out.println(f({n}));", members="    " + F9.replace("\n", "\n    ") + "\n"))
    except RuntimeError as e:
        assert "StackOverflowError" in str(e), str(e)[:300]
        return None
res9 = {n: f9(n) for n in (14, 16, 18, 20, 22)}
assert res9[18] == "63" and all(res9[n] is None for n in (14, 16, 20, 22)), res9
B.mcq(T_REC, "Consider the following method.\n\n" + code(F9) + "\n\nWhich of the following calls will return a value without causing a `StackOverflowError`?",
      ch("`f(18)`", "The argument goes 18, 15, 12, 9, 6, 3, 0, so it reaches the base case, and the method returns 18 + 15 + 12 + 9 + 6 + 3 = 63."),
      [ch("`f(14)`", "The argument goes 14, 11, 8, 5, 2, -1, -4, ... It skips 0, so the base case is never reached and the recursion continues until the stack overflows."),
       ch("`f(16)`", "The argument goes 16, 13, 10, 7, 4, 1, -2, ... It skips 0, so the base case is never reached."),
       ch("`f(20)`", "The argument goes 20, 17, 14, 11, 8, 5, 2, -1, ... It skips 0, so the base case is never reached."),
       ch("`f(22)`", "The argument goes 22, 19, 16, 13, 10, 7, 4, 1, -2, ... It skips 0, so the base case is never reached.")],
      "The base case `n == 0` is reached only when the argument is a multiple of 3, since each call subtracts 3; otherwise the argument passes 0 and keeps decreasing.")

# 10. palindrome with an incomplete base case
P10 = '''public static boolean isPal(String s) {
    if (s.length() == 0) {
        return true;
    }
    if (s.charAt(0) != s.charAt(s.length() - 1)) {
        return false;
    }
    return isPal(s.substring(1, s.length() - 1));
}'''
b10 = 'String out = "";\nString[] words = {"abba", "abca", "aba"};\nfor (String w : words) {\n    try {\n        out += isPal(w) + " ";\n    } catch (StringIndexOutOfBoundsException e) {\n        out += "error ";\n    }\n}\nSystem.out.println(out);'
trace(B, T_REC, Q, body=b10, members="    " + P10.replace("\n", "\n    ") + "\n",
      mutants=[("s.length() == 0", "s.length() <= 1", "This is the result if a one-letter string were also a base case. Here the only base case is the empty string, so for \"aba\" the recursion reaches \"b\" and then calls `substring(1, 0)`, which throws an exception.")],
      manual=[("true true error", "For \"abca\", the first and last letters match, but the call on \"bc\" compares `b` and `c`, which differ, so the result is false."),
              ("true false false", "\"aba\" is a palindrome, so no call returns false. But the recursion reaches the one-letter string \"b\", which is not an empty string, and then calls `substring(1, 0)`, which throws an exception.")],
      correct_expl="\"abba\" reduces to \"bb\" and then \"\", which is the base case: true. \"abca\" reduces to \"bc\", whose first and last letters differ: false. \"aba\" reduces to \"b\"; the base case only covers the empty string, so the method compares the letter with itself and calls `substring(1, 0)`, which throws a `StringIndexOutOfBoundsException`, caught and recorded as error.",
      explanation="A recursive method that removes two characters per call needs a base case for both even and odd lengths (length 0 and length 1).")

# 11. towers of Hanoi move order
H11 = '''public static void move(int n, char from, char to, char spare) {
    if (n == 0) {
        return;
    }
    move(n - 1, from, spare, to);
    System.out.print(from + "" + to + " ");
    move(n - 1, spare, to, from);
}'''
trace(B, T_REC, Q, body="move(3, 'A', 'C', 'B');\nSystem.out.println();", members="    " + H11.replace("\n", "\n    ") + "\n",
      mutants=[("move(n - 1, from, spare, to);", "move(n - 1, from, to, spare);", "This moves the smaller stack to the target instead of the spare peg first. The first recursive call uses the spare peg as its destination: `move(n - 1, from, spare, to)`."),
               ("move(n - 1, spare, to, from);", "move(n - 1, from, to, spare);", "This moves the smaller stack from the original peg again. The second recursive call moves the stack from the spare peg onto the target: `move(n - 1, spare, to, from)`."),
               ("System.out.print(from + \"\" + to + \" \");\n        move(n - 1, spare, to, from);", "move(n - 1, spare, to, from);\n        System.out.print(from + \"\" + to + \" \");", "This prints the move for the largest disk after the smaller stack has been moved on top of it. The move is printed between the two recursive calls.")],
      correct_expl="`move(3, A, C, B)` first moves two disks from A to B (using C as the spare): AC, AB, CB. Then it prints AC for the largest disk. Then it moves the two disks from B to C (using A as the spare): BA, BC, AC. Output: AC AB CB AC BA BC AC.",
      explanation="In the towers of Hanoi recursion, the roles of the three pegs (`from`, `to`, `spare`) change with each recursive call, so trace each call's parameters carefully.")

# 12. grid paths with a blocked cell
PA = '''static boolean[][] blocked = {
    {false, false, false},
    {false, true, false},
    {false, false, false}
};

public static int paths(int r, int c) {
    if (r < 0 || c < 0 || blocked[r][c]) {
        return 0;
    }
    if (r == 0 && c == 0) {
        return 1;
    }
    return paths(r - 1, c) + paths(r, c - 1);
}'''
trace(B, T_REC, Q, body='System.out.println(paths(2, 2) + " " + paths(1, 2) + " " + paths(0, 2) + " " + paths(1, 1));', members="    " + PA.replace("\n", "\n    ") + "\n",
      mutants=[("blocked[r][c]", "false", "This ignores the blocked cell in the middle of the grid, so more paths are counted. A blocked cell returns 0.")],
      manual=[("2 1 1 2", "`paths(1, 1)` is the blocked cell, so it returns 0 even though its neighbors can be reached."),
              ("2 2 1 0", "`paths(1, 2)` is `paths(0, 2) + paths(1, 1)`, that is 1 + 0, because the cell (1, 1) is blocked.")],
      correct_expl="Paths can only reach (r, c) from above or from the left, and (1, 1) is blocked. `paths(0, 2)` = 1 (straight along the top row), `paths(1, 1)` = 0 (blocked), `paths(1, 2)` = 1 + 0 = 1, and `paths(2, 2)` = `paths(1, 2)` + `paths(2, 1)` = 1 + 1 = 2.",
      explanation="A recursive count of paths adds the counts from each neighboring cell, with 0 for a cell that is off the grid or blocked.")

# 13. permutations in a nonstandard order
PE = '''public static void permute(String prefix, String rest) {
    if (rest.length() == 0) {
        System.out.print(prefix + " ");
        return;
    }
    for (int i = 0; i < rest.length(); i++) {
        permute(prefix + rest.charAt(i), rest.substring(i + 1) + rest.substring(0, i));
    }
}'''
trace(B, T_REC, Q, body='permute("", "abc");\nSystem.out.println();', members="    " + PE.replace("\n", "\n    ") + "\n",
      mutants=[("rest.substring(i + 1) + rest.substring(0, i)", "rest.substring(0, i) + rest.substring(i + 1)", "This is the usual order, which removes the chosen letter and keeps the others in their original order. This method puts the letters after the chosen one first, so the remaining letters are rotated."),
               ("rest.substring(i + 1) + rest.substring(0, i)", "rest.substring(i + 1)", "This drops the letters before the chosen one. The method keeps them by adding `rest.substring(0, i)` at the end.")],
      manual=[("abc acb bca bac cba cab", "In `permute(\"c\", \"ab\")`, the loop takes the letters of \"ab\" in order: `a` first (cab) and then `b` (cba).")],
      correct_expl="Each call tries every letter of `rest` as the next letter, passing on the other letters rotated so that the letters after the chosen one come first. From the empty prefix: a with \"bc\" gives abc and acb; b with \"ca\" gives bca and bac; c with \"ab\" gives cab and cba.",
      explanation="Trace the recursion tree with the exact string passed in each call; the order of the output depends on how the remaining letters are arranged.")

# 14. completing a recursive method
S14 = 'public static int sumDigits(int n) {\n    if (n < 10) {\n        return n;\n    }\n    /* missing code */\n}'
opts14 = {
    "A": "return n % 10 + sumDigits(n / 10);",
    "B": "return n / 10 + sumDigits(n % 10);",
    "C": "return n % 10 + sumDigits(n % 10);",
    "D": "return sumDigits(n / 10);",
    "E": "return n % 10 * sumDigits(n / 10);",
}
r14 = {}
for k, v in opts14.items():
    src = S14.replace("/* missing code */", v)
    r14[k] = run(program("System.out.println(sumDigits(4821) + \" \" + sumDigits(7));", members="    " + src.replace("\n", "\n    ") + "\n"))
assert r14 == {"A": "15 7", "B": "483 7", "C": "2 7", "D": "4 7", "E": "64 7"}, r14
B.mcq(T_REC, "The method `sumDigits` is intended to return the sum of the digits of a non-negative integer. For example, `sumDigits(4821)` should return 15.\n\n" + code(S14) + "\n\nWhich of the following statements, when used to replace `/* missing code */`, will make the method work as intended?",
      ch("`return n % 10 + sumDigits(n / 10);`", "`n % 10` is the last digit and `n / 10` removes it, so the method adds the last digit to the sum of the digits of the rest. For 4821: 1 + (2 + (8 + 4)) = 15."),
      [ch("`return n / 10 + sumDigits(n % 10);`", "This adds the number without its last digit (482) to the digit sum of only the last digit, and `sumDigits(4821)` returns 483."),
       ch("`return n % 10 + sumDigits(n % 10);`", "The recursive call uses the last digit again instead of the remaining digits, so the other digits are never added. `sumDigits(4821)` returns 2."),
       ch("`return sumDigits(n / 10);`", "This discards the last digit in every call without adding it, so only the first digit remains. `sumDigits(4821)` returns 4."),
       ch("`return n % 10 * sumDigits(n / 10);`", "This multiplies the digits instead of adding them. `sumDigits(4821)` returns 64.")],
      "A recursive digit method splits `n` into its last digit (`n % 10`) and the rest (`n / 10`), combines the last digit with the result for the rest, and has a base case for a single digit.")

# 15. recursive selection sort
SS = '''public static void selSort(int[] a, int start) {
    if (start >= a.length - 1) {
        return;
    }
    int min = start;
    for (int i = start + 1; i < a.length; i++) {
        if (a[i] < a[min]) {
            min = i;
        }
    }
    int t = a[start];
    a[start] = a[min];
    a[min] = t;
    String s = "";
    for (int v : a) {
        s += v;
    }
    System.out.print(s + " ");
    selSort(a, start + 1);
}'''
trace(B, T_SRCH, Q, body="int[] a = {4, 3, 1, 5, 2};\nselSort(a, 0);\nSystem.out.println();", members="    " + SS.replace("\n", "\n    ") + "\n",
      mutants=[("System.out.print(s + \" \");\n        selSort(a, start + 1);", "selSort(a, start + 1);\n        System.out.print(s + \" \");", "This prints after the recursive call, so the states come out in reverse order. The method prints the array before making the recursive call."),
               ("a[i] < a[min]", "a[i] > a[min]", "This selects the largest remaining element instead of the smallest, which gives a descending order. The method looks for the smallest with `<`."),
               ("start >= a.length - 1", "start >= a.length - 2", "This stops one level early and omits the last print. The recursion continues while `start` is less than `a.length - 1`, so it runs for `start` values 0 to 3.")],
      correct_expl="Each call moves the smallest remaining element to position `start` and prints the array. Start 0: swap 1 into place: 13452. Start 1: swap 2 into place: 12453. Start 2: swap 3 into place: 12354. Start 3: swap 4 into place: 12345. For `start` equal to 4 the base case returns.",
      explanation="Recursive selection sort places one element per call; the output shows the array after each placement, from the first call to the last.")

# ------------------------------------------------------------------ FRQs
TOOLS = '''
class Tools {
    public static String removeChar(String s, char c) {
        if (s.length() == 0) {
            return "";
        }
        if (s.charAt(0) == c) {
            return removeChar(s.substring(1), c);
        }
        return s.charAt(0) + removeChar(s.substring(1), c);
    }

    public static int findFirst(int[] a, int t, int lo, int hi) {
        if (lo > hi) {
            return -1;
        }
        int mid = (lo + hi) / 2;
        if (a[mid] < t) {
            return findFirst(a, t, mid + 1, hi);
        }
        if (a[mid] > t) {
            return findFirst(a, t, lo, mid - 1);
        }
        int left = findFirst(a, t, lo, mid - 1);
        if (left != -1) {
            return left;
        }
        return mid;
    }
}
'''
tb = ('System.out.println(Tools.removeChar("banana", \'a\') + " " + Tools.removeChar("aaa", \'a\').length() + " " + Tools.removeChar("xyz", \'a\') + " [" + Tools.removeChar("", \'q\') + "]");\n'
      'int[] arr = {1, 3, 3, 3, 5, 8, 8, 9};\n'
      'System.out.println(Tools.findFirst(arr, 3, 0, 7) + " " + Tools.findFirst(arr, 8, 0, 7) + " " + Tools.findFirst(arr, 1, 0, 7) + " " + Tools.findFirst(arr, 9, 0, 7) + " " + Tools.findFirst(arr, 4, 0, 7) + " " + Tools.findFirst(arr, 0, 0, 7) + " " + Tools.findFirst(arr, 3, 2, 7));')
got = run(program(tb, classes=TOOLS))
assert got == "bnn 0 xyz []\n1 5 0 7 -1 -1 2", got
B.frq(T_SRCH,
      "This question involves recursive methods in a class named `StringAndSearch`. The methods must be recursive; a solution that uses a loop to do the work will not earn full credit.\n\n**(a)** Write the method `removeChar`, which returns a new string that contains the characters of `s` in their original order, with every occurrence of the character `c` removed.\n\n```java\npublic static String removeChar(String s, char c)\n```\n\nExamples:\n\n| Call | Returns |\n|---|---|\n| `removeChar(\"banana\", 'a')` | `\"bnn\"` |\n| `removeChar(\"xyz\", 'a')` | `\"xyz\"` |\n| `removeChar(\"aaa\", 'a')` | `\"\"` |\n\n**(b)** Write the method `findFirst`, which uses recursion to return the index of the **first** occurrence of `t` in the sorted (ascending) array `a` within the range `a[lo]` through `a[hi]`, inclusive, or -1 if `t` does not appear in that range. The array may contain duplicate values. The method should use a binary-search strategy (it should not examine every element).\n\n```java\n/** Precondition: a is sorted in ascending order; 0 <= lo and hi < a.length (but lo > hi is possible) */\npublic static int findFirst(int[] a, int t, int lo, int hi)\n```\n\nFor example, if `arr` is {1, 3, 3, 3, 5, 8, 8, 9}, then `findFirst(arr, 3, 0, 7)` returns 1, `findFirst(arr, 8, 0, 7)` returns 5, and `findFirst(arr, 4, 0, 7)` returns -1.",
      [(1, "(a) Base case: returns the empty string when `s` is empty"),
       (1, "(a) When the first character equals `c`, recurs on the rest of the string without that character"),
       (1, "(a) Otherwise returns the first character concatenated with the result of the recursive call on the rest"),
       (1, "(a) Recursive calls make progress toward the base case (for example `s.substring(1)`), and no loops are used"),
       (1, "(b) Base case: returns -1 when `lo > hi`"),
       (1, "(b) Computes a middle index and recurs on the correct half when `a[mid]` is less than or greater than `t`"),
       (1, "(b) When `a[mid]` equals `t`, searches the left part for an earlier occurrence and returns that index if there is one, and otherwise returns `mid`")],
      "```java\npublic static String removeChar(String s, char c) {\n    if (s.length() == 0) {\n        return \"\";\n    }\n    if (s.charAt(0) == c) {\n        return removeChar(s.substring(1), c);\n    }\n    return s.charAt(0) + removeChar(s.substring(1), c);\n}\n\npublic static int findFirst(int[] a, int t, int lo, int hi) {\n    if (lo > hi) {\n        return -1;\n    }\n    int mid = (lo + hi) / 2;\n    if (a[mid] < t) {\n        return findFirst(a, t, mid + 1, hi);\n    }\n    if (a[mid] > t) {\n        return findFirst(a, t, lo, mid - 1);\n    }\n    int left = findFirst(a, t, lo, mid - 1);\n    if (left != -1) {\n        return left;\n    }\n    return mid;\n}\n```\nWhen `a[mid]` equals `t`, the first occurrence is either `mid` itself or somewhere to its left, so the method searches `a[lo..mid - 1]` and falls back on `mid` if nothing is found there.")

COUNT = '''
class Count {
    public static int ways(int n) {
        if (n < 0) {
            return 0;
        }
        if (n == 0) {
            return 1;
        }
        return ways(n - 1) + ways(n - 2) + ways(n - 3);
    }

    public static boolean canMake(int[] vals, int index, int target) {
        if (target == 0) {
            return true;
        }
        if (index >= vals.length) {
            return false;
        }
        return canMake(vals, index + 1, target - vals[index]) || canMake(vals, index + 1, target);
    }
}
'''
tb2 = ('System.out.println(Count.ways(0) + " " + Count.ways(1) + " " + Count.ways(2) + " " + Count.ways(3) + " " + Count.ways(4) + " " + Count.ways(5) + " " + Count.ways(-2));\n'
       'int[] v = {3, 9, 8, 4};\n'
       'System.out.println(Count.canMake(v, 0, 12) + " " + Count.canMake(v, 0, 5) + " " + Count.canMake(v, 0, 0) + " " + Count.canMake(v, 2, 12) + " " + Count.canMake(v, 0, 24) + " " + Count.canMake(v, 0, 25) + " " + Count.canMake(v, 1, 20));')
got = run(program(tb2, classes=COUNT))
assert got == "1 1 2 4 7 13 0\ntrue false true true true false false", got
B.frq(T_REC,
      "This question involves two recursive methods. Both methods must be recursive; a solution that uses a loop to do the work will not earn full credit.\n\n**(a)** A hiker climbs a staircase and, on each move, climbs 1, 2 or 3 steps. Write the method `ways`, which returns the number of different sequences of moves that climb exactly `n` steps. A sequence is different if the numbers of steps in its moves are in a different order. Climbing zero steps can be done in exactly one way (making no moves), and a negative number of steps cannot be climbed at all.\n\n```java\npublic static int ways(int n)\n```\n\nFor example, `ways(3)` returns 4, since the possible sequences are 1+1+1, 1+2, 2+1 and 3. Also `ways(4)` returns 7 and `ways(5)` returns 13.\n\n**(b)** Write the method `canMake`, which returns true if some collection of the values in `vals[index]` through the end of the array (each value used at most once) adds up to exactly `target`, and false otherwise. A collection of no values has a sum of 0. All of the values in `vals` and the value of `target` are non-negative.\n\n```java\n/** Precondition: 0 <= index and target >= 0 */\npublic static boolean canMake(int[] vals, int index, int target)\n```\n\nFor example, if `v` is {3, 9, 8, 4}, then `canMake(v, 0, 12)` returns true (3 + 9, or 8 + 4), `canMake(v, 0, 5)` returns false, and `canMake(v, 2, 12)` returns true (8 + 4).",
      [(1, "(a) Base cases: returns 0 for a negative argument and 1 for zero"),
       (1, "(a) Makes recursive calls for `n - 1`, `n - 2` and `n - 3`"),
       (1, "(a) Adds the results of the three calls and returns the sum"),
       (1, "(b) Returns true when `target` is 0 (before checking whether values remain)"),
       (1, "(b) Returns false when there are no values left (`index` is past the end), without accessing the array out of bounds"),
       (1, "(b) Makes the recursive call that uses `vals[index]`: with `target - vals[index]` and `index + 1`"),
       (1, "(b) Makes the recursive call that skips `vals[index]` and combines the two results so that the method returns true if either one is true")],
      "```java\npublic static int ways(int n) {\n    if (n < 0) {\n        return 0;\n    }\n    if (n == 0) {\n        return 1;\n    }\n    return ways(n - 1) + ways(n - 2) + ways(n - 3);\n}\n\npublic static boolean canMake(int[] vals, int index, int target) {\n    if (target == 0) {\n        return true;\n    }\n    if (index >= vals.length) {\n        return false;\n    }\n    return canMake(vals, index + 1, target - vals[index]) || canMake(vals, index + 1, target);\n}\n```\nIn `ways`, the last move is 1, 2 or 3 steps, so the number of ways to climb `n` steps is the sum of the numbers of ways to climb `n - 1`, `n - 2` and `n - 3` steps. In `canMake`, each value is either used (the target shrinks by that value) or skipped.")

B.save()
B.brief()
