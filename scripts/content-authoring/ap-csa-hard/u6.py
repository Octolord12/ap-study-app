from common import *

B = bank(6, "unit-6-array")
T_CRE, T_TRA, T_ENH, T_ALG = ("array-creation-and-access", "traversing-arrays", "enhanced-for-arrays", "array-algorithms")
Q = "What is printed as a result of executing the following code segment?"

trace(B, T_CRE, Q, body='int[] a = new int[4];\nString[] s = new String[2];\nboolean[] b = new boolean[2];\na[1] = 5;\na[a.length - 1] = a[1] + 1;\nSystem.out.println(a[0] + " " + a[1] + " " + a[3] + " " + a.length + " " + s[0] + " " + b[1]);',
      manual=[("0 5 6 3 null false", "`a.length` is the number of elements (4), not the index of the last element. The last index is 3, which is where 6 is stored."),
              ("0 5 0 4 null false", "`a[a.length - 1]` is `a[3]`, so the 6 is stored in the last element, and printing `a[3]` shows 6."),
              ("0 5 6 4 null true", "A `boolean` array is created with every element `false`.")],
      correct_expl="A new `int` array is filled with 0s, `String` arrays with `null` and `boolean` arrays with `false`. Then a[1] = 5 and a[3] = 6, and `a.length` is 4.",
      explanation="Array elements get default values when the array is created. The length is the number of elements, and the last index is one less.")

trace(B, T_TRA, Q, body='int[] a = {4, 7, 1};\nint sum = 0;\ntry {\n    for (int i = 0; i <= a.length; i++)\n        sum += a[i];\n    System.out.println("done " + sum);\n} catch (ArrayIndexOutOfBoundsException e) {\n    System.out.println("caught " + sum);\n}',
      manual=[("done 12", "This assumes the loop stays within the array. The condition `i <= a.length` lets `i` reach 3, and `a[3]` is out of bounds for an array of length 3."),
              ("caught 0", "This assumes the exception happens before anything is added. The first three passes (i = 0, 1, 2) succeed, so `sum` is 12 when `a[3]` throws."),
              ("The code does not compile.", "`<=` with `a.length` compiles; the problem appears only at run time, when `i` equals 3.")],
      correct_expl="The first three passes add 4, 7 and 1 (sum 12). When `i` is 3, `a[3]` throws an `ArrayIndexOutOfBoundsException`, so \"done\" is skipped and the handler prints the sum so far.",
      explanation="Valid indexes are 0 through `length - 1`. The condition `i <= a.length` goes one past the end.")

trace(B, T_ENH, Q, body='int[] a = {1, 2, 3};\nfor (int x : a)\n    x *= 2;\nint s1 = 0;\nfor (int x : a)\n    s1 += x;\nfor (int i = 0; i < a.length; i++)\n    a[i] *= 2;\nint s2 = 0;\nfor (int x : a)\n    s2 += x;\nSystem.out.println(s1 + " " + s2);',
      mutants=[("for (int x : a)\n    x *= 2;", "for (int i = 0; i < a.length; i++)\n    a[i] *= 2;", "This assumes the enhanced `for` changes the array's elements. The loop variable `x` is a copy of each element, so `x *= 2` does not change the array.")],
      manual=[("6 6", "This assumes the indexed loop does not change the array. `a[i] *= 2` changes the elements themselves, so their sum doubles."),
              ("12 12", "Both loops change the array differently from this: the enhanced `for` leaves it alone (sum 6), and the indexed loop doubles every element (sum 12).")],
      correct_expl="In the first loop, `x` is a copy of each element, so the array is unchanged: its sum `s1` is 1 + 2 + 3 = 6. The indexed loop doubles the elements to 2, 4, 6, so `s2` is 12.",
      explanation="An enhanced `for` loop variable holds a copy of a primitive element. To change the elements, use an indexed loop.")

trace(B, T_ALG, Q, body='int[] a = {10, 20, 30, 40, 50};\nint idx = 1;\nfor (int i = idx; i < a.length - 1; i++)\n    a[i] = a[i + 1];\na[a.length - 1] = 0;\nString s = "";\nfor (int x : a)\n    s += x + " ";\nSystem.out.println(s.trim());',
      mutants=[("a[i] = a[i + 1];", "a[i + 1] = a[i];", "This copies each element to the right, so the value at the removal index spreads along the array. To delete an element, elements to its right move *left*.")],
      manual=[("10 30 40 50 50", "This leaves the last element unchanged. The statement `a[a.length - 1] = 0;` clears the now-duplicated last element."),
              ("10 20 30 40 0", "This removes the last element instead of the one at index 1. The loop starts at `idx`, so `a[1]` is overwritten by `a[2]`.")],
      correct_expl="Starting at index 1, each element is replaced by its right neighbor: 20 is overwritten by 30, 30 by 40, 40 by 50. The last element is then set to 0, giving 10 30 40 50 0.",
      explanation="Deleting an element from an array by shifting moves the later elements left and leaves the last position to be cleared.")

trace(B, T_ALG, Q, body='int[] a = {1, 2, 3, 4, 5};\nfor (int i = 0; i < a.length / 2; i++) {\n    int t = a[i];\n    a[i] = a[a.length - 1 - i];\n    a[a.length - 1 - i] = t;\n}\nString s = "";\nfor (int x : a)\n    s += x;\nSystem.out.println(s);',
      mutants=[("i < a.length / 2", "i < a.length", "This swaps every pair twice, so the array ends up back in its original order. The loop must stop at the middle.")],
      manual=[("52341", "This stops one swap early. For length 5, `a.length / 2` is 2, so both the swap of positions 0 and 4 and the swap of positions 1 and 3 happen."),
              ("54345", "This describes a swap without the temporary variable `t`. With the temporary, the old value is saved and written to the other position.")],
      correct_expl="Two swaps are done (i = 0 and i = 1): positions 0 and 4, and positions 1 and 3. The middle element stays, giving 5 4 3 2 1.",
      explanation="Reversing in place swaps symmetric pairs and stops at the middle; going all the way would undo the work.")

trace(B, T_CRE, Q, body='int[] a = {1, 2, 3};\nint[] b = a;\nint[] c = a.clone();\nb[0] = 99;\nc[1] = -5;\nSystem.out.println(a[0] + " " + a[1] + " " + b[1] + " " + c[0] + " " + (a == b) + " " + (a == c));',
      manual=[("1 2 2 1 false false", "This assumes `b = a` copies the array. It copies the *reference*, so `b` and `a` are the same array, and `a == b` is true."),
              ("99 -5 -5 99 true true", "This assumes `clone()` returns the same array. It creates a new, independent array whose elements are copied, so `c[1] = -5` does not affect `a`."),
              ("99 2 2 1 true true", "`a == c` is false: `clone()` creates a different array object, even though its contents were equal at that moment.")],
      correct_expl="`b` and `a` refer to one array, so `b[0] = 99` changes `a[0]` too, and `a == b` is true. `c` is a separate copy made before the changes: c[0] is still 1, and the change `c[1] = -5` does not affect `a`. `a == c` is false.",
      explanation="Assigning an array variable copies the reference; `clone()` copies the elements into a new array.")

trace(B, T_ALG, Q, body="int[] a = {3, 7, 2, 8, 5, 5};\nint count = 0;\nfor (int i = 0; i < a.length; i++)\n    for (int j = i + 1; j < a.length; j++)\n        if (a[i] + a[j] == 10)\n            count++;\nSystem.out.println(count);",
      mutants=[("int j = i + 1;", "int j = 0;", "This lets `j` start at 0, so each pair is counted twice and a value can be paired with itself (5 + 5, 5 + 5 for each 5)."),
               ("int j = i + 1;", "int j = i;", "This lets each element pair with itself, so each 5 counts (5 + 5 = 10) in addition to the pair of 5s."),
               ("a.length; j++", "a.length - 1; j++", "This leaves out the last element as a partner, so the pair (5, 5) is missed.")],
      correct_expl="Pairs summing to 10: 3 + 7, 2 + 8, and 5 + 5 (the two 5s). Starting `j` at `i + 1` counts each pair once and never pairs an element with itself. The count is 3.",
      explanation="A nested loop with `j = i + 1` visits each pair of positions exactly once.")

trace(B, T_ALG, Q, body="int[] a = {5, 9, 9, 3, 7};\nint max = a[0], second = Integer.MIN_VALUE;\nfor (int i = 1; i < a.length; i++) {\n    if (a[i] > max) {\n        second = max;\n        max = a[i];\n    } else if (a[i] > second)\n        second = a[i];\n}\nSystem.out.println(max + \" \" + second);",
      manual=[("9 7", "This reports the second largest *distinct* value. When the second 9 is reached, `a[i] > max` is false, but `a[i] > second` (9 > 5) is true, so `second` becomes 9."),
              ("9 5", "This keeps the value that `max` had before. The second 9 also updates `second` through the `else if`."),
              ("9 3", "This takes the smallest of the values after the maximum. `second` is raised, never lowered, so later smaller values do not replace it.")],
      correct_expl="The first 9 makes `max` 9 and `second` 5. The second 9 is not greater than `max`, but it is greater than `second`, so `second` becomes 9. The 3 and 7 are smaller than 9, so nothing changes.",
      explanation="This algorithm finds the second largest element counting duplicates; with a repeated maximum, both equal the maximum.")

trace(B, T_TRA, Q, body='String[] w = {"kiwi", "banana", "fig", "cherry", "plum"};\nString best = w[0];\nfor (int i = 1; i < w.length; i++)\n    if (w[i].length() > best.length())\n        best = w[i];\nSystem.out.println(best + " " + best.length());',
      mutants=[("w[i].length() > best.length()", "w[i].length() >= best.length()", "This replaces the current best on a tie. \"cherry\" has the same length as \"banana\", and with `>` the first one found is kept.")],
      manual=[("kiwi 4", "This assumes `best` never changes. The test `w[i].length() > best.length()` is true for \"banana\" (6 > 4)."),
              ("banana 5", "\"banana\" has 6 letters: b, a, n, a, n, a.")],
      correct_expl="`best` starts as \"kiwi\" (4). \"banana\" (6) is longer, so it replaces it. \"fig\" is shorter, \"cherry\" (6) is not longer than 6, and \"plum\" is shorter. The result is banana 6.",
      explanation="With a strict `>` comparison, the first of several longest elements is the one kept.")

trace(B, T_ENH, Q, body="int[] a = {1, 2, 3};\ndoubleAll(a);\nreset(a);\nSystem.out.println(a[0] + \" \" + a[1] + \" \" + a[2]);",
      members="    public static void doubleAll(int[] arr) {\n        for (int i = 0; i < arr.length; i++)\n            arr[i] *= 2;\n    }\n    public static void reset(int[] arr) {\n        arr = new int[arr.length];\n        arr[0] = -1;\n    }\n",
      mutants=[("arr = new int[arr.length];\n        arr[0] = -1;", "for (int i = 0; i < arr.length; i++)\n            arr[i] = 0;", "This replaces `reset`'s body with a loop that zeroes the *elements* of the caller's array. In the original, `arr` is a copy of the reference, so the new array is seen only inside `reset`.")],
      manual=[("-1 0 0", "This assumes `reset` replaces the caller's array. Assigning a new array to the parameter `arr` changes only the local copy of the reference."),
              ("1 2 3", "`doubleAll` changes the elements of the array that the caller passed, so the doubling is visible afterward.")],
      correct_expl="`doubleAll` changes the elements of the caller's array: 2, 4, 6. In `reset`, `arr = new int[...]` makes the *parameter* refer to a new array, so the caller's array is unchanged.",
      explanation="A method can change an array's contents through its reference, but reassigning the parameter has no effect on the caller.")

trace(B, T_ENH, Q, body="Counter[] cs = new Counter[3];\nfor (int i = 0; i < cs.length; i++)\n    cs[i] = new Counter();\nfor (Counter c : cs)\n    c.inc();\nfor (Counter c : cs)\n    c = new Counter();\ncs[0].inc();\nSystem.out.println(cs[0].get() + \" \" + cs[1].get() + \" \" + cs[2].get());",
      classes="class Counter {\n    private int n = 0;\n    public void inc() { n++; }\n    public int get() { return n; }\n}\n",
      mutants=[("for (Counter c : cs)\n    c = new Counter();", "for (int i = 0; i < cs.length; i++)\n    cs[i] = new Counter();", "This replaces the array elements with new objects. In the original, `c = new Counter()` changes only the loop variable, so the elements still refer to the old objects.")],
      manual=[("1 1 1", "This leaves out the final `cs[0].inc()`. That call increments the first counter a second time."),
              ("2 2 2", "This applies the last increment to every counter. `cs[0].inc()` is called only on the first element.")],
      correct_expl="The first enhanced `for` calls `inc()` on each object (each count is 1). The second only reassigns the loop variable `c`, so the array is unchanged. Finally `cs[0].inc()` makes the first count 2.",
      explanation="In an enhanced `for`, the loop variable is a copy of the reference: calling methods on it affects the object, but assigning to it does not change the array.")

trace(B, T_ALG, Q, body='int[] a = {2, 4, 1, 3};\nint[] p = new int[a.length];\np[0] = a[0];\nfor (int i = 1; i < a.length; i++)\n    p[i] = p[i - 1] + a[i];\nString s = "";\nfor (int x : p)\n    s += x + " ";\nSystem.out.println(s.trim());',
      mutants=[("p[i] = p[i - 1] + a[i];", "p[i] = p[i - 1] + a[i - 1];", "This adds the previous element of `a` instead of the current one, so each running total lags behind."),
               ("p[0] = a[0];", "", "This leaves out the initialization `p[0] = a[0]`. A new `int` array contains zeros, so every running total is missing the first element.")],
      manual=[("The code throws an `ArrayIndexOutOfBoundsException`.", "The loop starts at `i = 1`, so `p[i - 1]` is `p[0]` at the first pass, which is valid; no index is out of range.")],
      correct_expl="The array `p` holds running totals: 2, 2 + 4 = 6, 6 + 1 = 7, 7 + 3 = 10.",
      explanation="A prefix-sum array stores, at each index, the sum of the elements up to and including that index.")

trace(B, T_TRA, Q, body="int[] a = {1, 1, 2, 2, 2, 1, 3, 3};\nint runs = 1;\nfor (int i = 1; i < a.length; i++)\n    if (a[i] != a[i - 1])\n        runs++;\nSystem.out.println(runs);",
      mutants=[("int runs = 1;", "int runs = 0;", "This starts the count at 0, missing the first run. A non-empty array always has at least one run."),
               ("a[i] != a[i - 1]", "a[i] == a[i - 1]", "This counts positions that repeat the previous value, not the places where a new run starts.")],
      manual=[("8", "This is the number of elements. The code counts a new run only where an element differs from the one before it.")],
      correct_expl="The runs are 1 1 | 2 2 2 | 1 | 3 3. A new run begins at each change of value: the count starts at 1 and the code adds one for each of the 3 changes, giving 4.",
      explanation="The number of runs is one more than the number of adjacent positions where the value changes.")

trace(B, T_ALG, Q, body='int[] a = {1, 2, 3, 4};\nint last = a[a.length - 1];\nfor (int i = a.length - 1; i > 0; i--)\n    a[i] = a[i - 1];\na[0] = last;\nString s = "";\nfor (int x : a)\n    s += x;\nSystem.out.println(s);',
      mutants=[("for (int i = a.length - 1; i > 0; i--)\n    a[i] = a[i - 1];", "for (int i = 1; i < a.length; i++)\n    a[i] = a[i - 1];", "This shifts in the wrong order. Going forward, each element is overwritten before it is copied, so the first value spreads across the array.")],
      manual=[("2341", "This rotates left. The code moves each element one position to the *right* and puts the last element in front."),
              ("1234", "The loop and the final assignment do change the array: the last element moves to index 0.")],
      correct_expl="The last element 4 is saved. Going from the end, each element is copied one position right: 1 2 3 3, 1 2 2 3, 1 1 2 3. Then a[0] is set to 4: 4 1 2 3.",
      explanation="When shifting elements right in place, move from the end of the array toward the front so no value is overwritten before it has been copied.")

cands = [("a = {1, 2, 3};", False), ("int len = a.length();", False), ("int[] e = new int[3.0];", False), ("int n = c.length;", True)]
assert compile_error(program("int[] a = new int[3];\na = {1, 2, 3};")) is not None
assert compile_error(program("int[] a = {1, 2, 3};\nint len = a.length();")) is not None
assert compile_error(program("int[] e = new int[3.0];")) is not None
assert compile_error(program("int[] c = {1, 2, 3};\nint n = c.length;")) is None
B.mcq(T_CRE, "Which of the following code segments compiles without error?",
      ch("`int[] c = {1, 2, 3}; int n = c.length;`", "`length` is a field of an array, not a method, so it is written without parentheses, and an initializer list may be used in the declaration."),
      [ch("`int[] a = new int[3]; a = {1, 2, 3};`", "An initializer list `{1, 2, 3}` can be used only in the declaration of the array. A later assignment needs `new int[] {1, 2, 3}`."),
       ch("`int[] a = {1, 2, 3}; int len = a.length();`", "For an array, `length` is a field, so the parentheses make this a compile-time error (for a `String`, `length()` is a method)."),
       ch("`int[] e = new int[3.0];`", "The size of an array must be an `int`. A `double` is not accepted without a cast.")],
      "Array `length` has no parentheses, and an initializer list is allowed only in a declaration.")

# ------------------------------------------------------------------ FRQs
members_a = '''
    public static int mostFrequent(int[] a) {
        int best = a[0];
        int bestCount = 0;
        for (int i = 0; i < a.length; i++) {
            int count = 0;
            for (int j = 0; j < a.length; j++) {
                if (a[j] == a[i]) {
                    count++;
                }
            }
            if (count > bestCount || (count == bestCount && a[i] < best)) {
                best = a[i];
                bestCount = count;
            }
        }
        return best;
    }

    public static int[] rotateLeft(int[] a, int k) {
        int n = a.length;
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            result[i] = a[(i + k) % n];
        }
        return result;
    }

    public static String str(int[] a) {
        String s = "";
        for (int x : a) s += x + " ";
        return s.trim();
    }
'''
verify(members_a, [("mostFrequent(new int[]{4, 1, 4, 2, 1, 4})", 4), ("mostFrequent(new int[]{3, 5, 3, 5})", 3), ("mostFrequent(new int[]{7})", 7), ("mostFrequent(new int[]{9, 2, 2, 9, 5})", 2),
                   ("str(rotateLeft(new int[]{1, 2, 3, 4, 5}, 2))", "3 4 5 1 2"), ("str(rotateLeft(new int[]{1, 2, 3, 4, 5}, 7))", "3 4 5 1 2"), ("str(rotateLeft(new int[]{1, 2, 3}, 0))", "1 2 3"), ("str(rotateLeft(new int[]{1, 2, 3}, 3))", "1 2 3")])
B.frq(T_ALG,
      "The class `ArrayTools` contains the two methods described below.\n\n```java\npublic class ArrayTools {\n    /** Returns the value that occurs most often in a. If more than one value occurs the\n     *  greatest number of times, returns the smallest of those values.\n     *  Precondition: a.length > 0\n     *  Example: mostFrequent(new int[] {4, 1, 4, 2, 1, 4}) returns 4 and\n     *           mostFrequent(new int[] {3, 5, 3, 5}) returns 3. */\n    public static int mostFrequent(int[] a)\n    { /* to be implemented in part (a) */ }\n\n    /** Returns a new array of the same length as a in which the elements are those of a\n     *  moved k positions to the left. Elements that move off the front are placed at the\n     *  end, in order. The array a is not changed.\n     *  Preconditions: a.length > 0, k >= 0 (k may be larger than a.length)\n     *  Example: if a is {1, 2, 3, 4, 5}, then rotateLeft(a, 2) returns {3, 4, 5, 1, 2},\n     *           and rotateLeft(a, 7) also returns {3, 4, 5, 1, 2}. */\n    public static int[] rotateLeft(int[] a, int k)\n    { /* to be implemented in part (b) */ }\n}\n```\n\n**(a)** Write the method `mostFrequent`.\n\n**(b)** Write the method `rotateLeft`.",
      [(1, "(a) Counts occurrences of each value (for example with a nested loop)"),
       (1, "(a) Keeps track of the value with the greatest count"),
       (1, "(a) Resolves a tie by choosing the smaller value"),
       (1, "(a) Returns the correct value"),
       (1, "(b) Creates a new array of the same length and does not modify `a`"),
       (1, "(b) Computes the source index for each position with correct wraparound (for example `(i + k) % n`)"),
       (1, "(b) Handles `k` larger than `a.length` and returns the new array")],
      "```java\npublic static int mostFrequent(int[] a) {\n    int best = a[0];\n    int bestCount = 0;\n    for (int i = 0; i < a.length; i++) {\n        int count = 0;\n        for (int j = 0; j < a.length; j++) {\n            if (a[j] == a[i]) {\n                count++;\n            }\n        }\n        if (count > bestCount || (count == bestCount && a[i] < best)) {\n            best = a[i];\n            bestCount = count;\n        }\n    }\n    return best;\n}\n\npublic static int[] rotateLeft(int[] a, int k) {\n    int n = a.length;\n    int[] result = new int[n];\n    for (int i = 0; i < n; i++) {\n        result[i] = a[(i + k) % n];\n    }\n    return result;\n}\n```\nIn `rotateLeft`, the element that ends up at index `i` came from index `(i + k) % n`, and the remainder makes the index wrap around, including when `k` is larger than the array.")

members_b = '''
    public static int longestPlateau(int[] a) {
        int best = 0;
        int run = 0;
        for (int i = 0; i < a.length; i++) {
            if (i > 0 && a[i] == a[i - 1]) {
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

    public static void shiftZerosToEnd(int[] a) {
        int next = 0;
        for (int i = 0; i < a.length; i++) {
            if (a[i] != 0) {
                a[next] = a[i];
                next++;
            }
        }
        while (next < a.length) {
            a[next] = 0;
            next++;
        }
    }

    public static String str(int[] a) {
        String s = "";
        for (int x : a) s += x + " ";
        return s.trim();
    }
'''
verify(members_b, [("longestPlateau(new int[]{1, 3, 3, 3, 2, 2})", 3), ("longestPlateau(new int[]{5})", 1), ("longestPlateau(new int[]{})", 0), ("longestPlateau(new int[]{1, 2, 3})", 1),
                   ("longestPlateau(new int[]{4, 4, 4, 4})", 4)],)
b = run(program('int[] a = {0, 3, 0, 5, 7, 0};\nshiftZerosToEnd(a);\nSystem.out.println(str(a));\nint[] b = {1, 2};\nshiftZerosToEnd(b);\nSystem.out.println(str(b));\nint[] c = {0, 0, 1};\nshiftZerosToEnd(c);\nSystem.out.println(str(c));', members_b))
assert b == "3 5 7 0 0 0\n1 2\n1 0 0", b
B.frq(T_TRA,
      "The class `ArrayTools2` contains the two methods described below.\n\n```java\npublic class ArrayTools2 {\n    /** Returns the length of the longest sequence of consecutive elements of a that are all\n     *  equal, or 0 if a is empty.\n     *  Example: if a is {1, 3, 3, 3, 2, 2}, longestPlateau(a) returns 3. */\n    public static int longestPlateau(int[] a)\n    { /* to be implemented in part (a) */ }\n\n    /** Rearranges the elements of a so that all of the nonzero values come first, in their\n     *  original order, followed by all of the zeros. No other array is created.\n     *  Example: if a is {0, 3, 0, 5, 7, 0}, after the call a is {3, 5, 7, 0, 0, 0}. */\n    public static void shiftZerosToEnd(int[] a)\n    { /* to be implemented in part (b) */ }\n}\n```\n\n**(a)** Write the method `longestPlateau`.\n\n**(b)** Write the method `shiftZerosToEnd`. You may not create another array or use any `ArrayList`.",
      [(1, "(a) Traverses the array comparing each element with the previous one without going out of bounds"),
       (1, "(a) Maintains the length of the current plateau, resetting to 1 when a different value occurs"),
       (1, "(a) Tracks and returns the longest length (0 for an empty array)"),
       (1, "(b) Traverses the array and moves each nonzero value forward to the next open position, preserving order"),
       (1, "(b) Does not overwrite a nonzero value before it has been copied"),
       (1, "(b) Fills the remaining positions with zeros"),
       (1, "(b) Modifies the array in place without creating another array")],
      "```java\npublic static int longestPlateau(int[] a) {\n    int best = 0;\n    int run = 0;\n    for (int i = 0; i < a.length; i++) {\n        if (i > 0 && a[i] == a[i - 1]) {\n            run++;\n        } else {\n            run = 1;\n        }\n        if (run > best) {\n            best = run;\n        }\n    }\n    return best;\n}\n\npublic static void shiftZerosToEnd(int[] a) {\n    int next = 0;\n    for (int i = 0; i < a.length; i++) {\n        if (a[i] != 0) {\n            a[next] = a[i];\n            next++;\n        }\n    }\n    while (next < a.length) {\n        a[next] = 0;\n        next++;\n    }\n}\n```\nIn `shiftZerosToEnd`, `next` is never ahead of `i`, so copying `a[i]` to `a[next]` cannot overwrite a nonzero value that has not been read yet.")

B.save()
B.brief()
