from common import *

B = bank(2, "unit-2-using-objects")
T_OOP, T_CRE, T_CALL, T_STR, T_MATH = ("object-oriented-programming", "creating-and-storing-objects", "calling-methods", "string-objects", "wrapper-classes-and-math")
Q = "What is printed as a result of executing the following code segment?"

POINT = "class Point {\n    private int x, y;\n    public Point(int x, int y) { this.x = x; this.y = y; }\n    public void move(int dx, int dy) { x += dx; y += dy; }\n    public int getX() { return x; }\n    public int getY() { return y; }\n}\n"

trace(B, T_STR, Q, body='String s = "programming";\nSystem.out.println(s.substring(3, 7) + s.indexOf("m") + s.charAt(s.length() - 2));',
      mutants=[("s.substring(3, 7)", "s.substring(3, 6)", "This stops the substring one character early. The end index of `substring` is exclusive, so `substring(3, 7)` includes the characters at indexes 3 through 6, \"gram\"."),
               ("s.indexOf(\"m\")", "s.lastIndexOf(\"m\")", "This finds the last \"m\" (index 7). `indexOf` returns the index of the first occurrence, 6."),
               ("s.length() - 2", "s.length() - 1", "This takes the last character, \"g\". `s.length() - 2` is the index of the second-to-last character, \"n\".")],
      correct_expl="`substring(3, 7)` is \"gram\". The first \"m\" is at index 6. The string has length 11, so `charAt(9)` is \"n\". The three values are concatenated.",
      explanation="`substring(a, b)` includes index `a` and excludes index `b`. `indexOf` finds the first occurrence, and `charAt` takes a zero-based index.")

trace(B, T_STR, Q, body='String a = "hello";\nString b = a;\na = a.toUpperCase();\na.concat("!");\nb = b + "?";\nSystem.out.println(a + " " + b);',
      mutants=[("a.concat(\"!\");", "a = a.concat(\"!\");", "This assumes `concat` changes `a`. `String` objects are immutable, so `a.concat(\"!\")` returns a new string that is discarded here."),
               ("a = a.toUpperCase();", "a.toUpperCase();", "This ignores the assignment. `toUpperCase` returns a new string; without `a = ...`, `a` is unchanged.")],
      manual=[("HELLO HELLO?", "This assumes that `b` follows `a` because `b = a`. Strings are immutable, so `a = a.toUpperCase()` makes `a` refer to a new string while `b` still refers to \"hello\".")],
      correct_expl="`a = a.toUpperCase()` makes `a` refer to \"HELLO\"; `b` still refers to \"hello\". `a.concat(\"!\")` creates a new string that is thrown away. `b = b + \"?\"` makes `b` \"hello?\".",
      explanation="Strings never change. A method that appears to modify a string returns a new one, and a variable changes only when it is assigned.")

trace(B, T_STR, Q, body='String s1 = "hi";\nString s2 = "hi";\nString s3 = new String("hi");\nSystem.out.println((s1 == s2) + " " + (s1 == s3) + " " + s1.equals(s3));',
      mutants=[("s1 == s3", "s1.equals(s3)", "This assumes `==` compares the characters. For objects, `==` compares references, and `new String(\"hi\")` creates a separate object.")],
      manual=[("false false true", "This assumes that two string literals are different objects. Identical literals in the same program refer to the same `String` object, so `s1 == s2` is true."),
              ("true false false", "This assumes `equals` compares references. `String`'s `equals` compares the characters, so it is true.")],
      correct_expl="The two literals \"hi\" refer to the same object, so `s1 == s2` is true. `new String(\"hi\")` creates a different object, so `s1 == s3` is false, but the characters are equal, so `equals` is true.",
      explanation="`==` compares references; `equals` compares contents. Use `equals` to compare strings.")

trace(B, T_CRE, Q, body="Point p = new Point(1, 2);\nPoint q = p;\nq.move(3, 3);\nPoint r = new Point(4, 5);\nSystem.out.println(p.getX() + \" \" + (p == q) + \" \" + (p == r) + \" \" + p.equals(r));",
      classes=POINT,
      mutants=[("Point q = p;", "Point q = new Point(1, 2);", "This treats `q` as a separate copy. `Point q = p;` copies the reference, so `p` and `q` name the same object and `q.move(3, 3)` changes `p` too.")],
      manual=[("4 false false false", "This is half right: it shows the move through `p`, but `p == q` is true because `p` and `q` are references to the same object."),
              ("4 true false true", "This assumes `equals` compares the fields. `Point` does not override `equals`, so it compares references, and `p` and `r` are different objects.")],
      correct_expl="`q` and `p` refer to the same object, so after `q.move(3, 3)` the x-coordinate seen through `p` is 4, and `p == q` is true. `r` is a different object, so `p == r` is false, and since `Point` does not override `equals`, `p.equals(r)` is also false.",
      explanation="An assignment between object variables copies the reference, not the object. `==` and the default `equals` test whether two references name the same object.")

trace(B, T_CALL, Q, body="Counter c = new Counter();\nbump(c);\nreset(c);\nSystem.out.println(c.getCount());",
      members="    public static void bump(Counter k) { k.increment(); k.increment(); }\n    public static void reset(Counter k) { k = new Counter(); k.increment(); }\n",
      classes="class Counter {\n    private int count;\n    public void increment() { count++; }\n    public int getCount() { return count; }\n}\n",
      mutants=[("k = new Counter(); k.increment();", "k.increment();", "This assumes `reset` increments the caller's object. In the original, `k = new Counter()` points the *parameter* at a new object, so the increment applies to that new object, not to `c`.")],
      manual=[("1", "This assumes `reset(c)` replaces the caller's counter with a new one that has been incremented once. The assignment `k = new Counter()` changes only the local parameter, not `c`."),
              ("0", "This assumes `reset` resets `c` to zero. Reassigning a parameter does not change the caller's variable.")],
      correct_expl="`bump(c)` increments the object `c` refers to twice. In `reset`, `k = new Counter()` only changes the local parameter, so the following increment affects the new object and `c` still has a count of 2.",
      explanation="Java passes a copy of the reference. A method can change the object through that copy, but reassigning the parameter does not affect the caller's variable.")

trace(B, T_STR, Q, body='System.out.println("apple".compareTo("banana") + " " + "Zebra".compareTo("apple") + " " + "app".compareTo("apple"));',
      mutants=[("\"apple\".compareTo(\"banana\")", "\"banana\".compareTo(\"apple\")", "This reverses the order. `\"apple\".compareTo(\"banana\")` is negative because \"apple\" comes before \"banana\"; it is the difference of the first differing characters, 'a' - 'b'.")],
      manual=[("-1 25 -2", "This ignores case. Uppercase letters have smaller character codes than lowercase ones, so \"Zebra\" comes *before* \"apple\": 'Z' (90) - 'a' (97) is -7."),
              ("-1 -7 -1", "When one string is a prefix of the other, the result is the difference in lengths: 3 - 5 = -2.")],
      correct_expl="The first differing characters are 'a' and 'b': 97 - 98 = -1. For \"Zebra\" and \"apple\", 'Z' - 'a' is 90 - 97 = -7. \"app\" is a prefix of \"apple\", so the result is the length difference, 3 - 5 = -2.",
      explanation="`compareTo` returns the difference of the first differing characters, or the difference in lengths if one string is a prefix of the other.")

a, b = run(program('int lo = (int) (0.0 * 6) + 3;\nint hi = (int) (Math.nextDown(1.0) * 6) + 3;\nSystem.out.println(lo + " " + hi);')).split()
assert (a, b) == ("3", "8")
B.mcq(T_MATH, "Which of the following best describes the possible values of `r` after the statement below is executed?\n\n" + code("int r = (int) (Math.random() * 6) + 3;"),
      ch("Any integer from 3 through 8, inclusive", "`Math.random()` returns a value from 0.0 up to but not including 1.0. Multiplying by 6 gives a value from 0.0 up to but not including 6.0, so the cast gives 0 through 5. Adding 3 gives 3 through 8."),
      [ch("Any integer from 3 through 9, inclusive", "The largest value of `(int) (Math.random() * 6)` is 5, since the product never reaches 6.0. So the largest value of `r` is 8."),
       ch("Any integer from 0 through 8, inclusive", "The `+ 3` is applied after the cast, so the smallest value is 3, not 0."),
       ch("Any real number from 3.0 up to but not including 9.0", "The cast to `int` happens before the 3 is added, so `r` is always an integer.")],
      "`(int) (Math.random() * n)` is an integer from 0 through n - 1; adding an offset shifts the range.")

trace(B, T_MATH, Q, body='String s = "12";\nint n = Integer.parseInt(s) + s.length();\nString t = s + n;\nSystem.out.println(t + t.length() * 2);',
      mutants=[("t + t.length() * 2", "t.length() * 2 + t", "This puts the product first. In `t + t.length() * 2` the string comes first, so the product is converted to text and appended; here the product would be added first and then joined to the string."),
               ("Integer.parseInt(s) + s.length()", "Integer.parseInt(s + s.length())", "This joins \"12\" and 2 into \"122\" before parsing. In the original, `Integer.parseInt(s)` is 12 and `s.length()` is 2, and they are added as numbers.")],
      manual=[("26", "This adds the numbers 12 and 14. Because `t` is a string, `t + ...` is concatenation, not addition.")],
      correct_expl="`n` is 12 + 2 = 14. `t` is \"12\" + 14 = \"1214\", which has length 4. `t + t.length() * 2` is \"1214\" + 8 = \"12148\" (the product is computed first, then concatenated).",
      explanation="Multiplication has higher precedence than `+`. Once either operand of `+` is a `String`, the operation is concatenation.")

trace(B, T_CALL, Q, body='String s = null;\nString t = "abc";\nint n = 0;\ntry {\n    if (t.length() > 2 || s.length() > 2) n += 1;\n    if (s != null && s.length() > 2) n += 10;\n    if (s.length() > 2 && t.length() > 2) n += 100;\n    n += 1000;\n} catch (NullPointerException e) {\n    n += 5;\n}\nSystem.out.println(n);',
      manual=[("5", "This assumes both operands of the first `||` are evaluated, so `s.length()` throws immediately. The `||` is short-circuit: since `t.length() > 2` is true, the right operand is never evaluated."),
              ("1001", "This assumes no exception is thrown. The third condition calls `s.length()` while `s` is `null`, which throws a `NullPointerException`."),
              ("1006", "This assumes execution continues after the exception. Once the exception is thrown inside the `try`, the rest of the `try` block is skipped.")],
      correct_expl="The first `||` is short-circuited, so n is 1. The second condition's `s != null` is false, so its right operand is skipped. The third condition evaluates `s.length()` with `s == null`, which throws `NullPointerException`, so `n += 1000` is skipped and the `catch` adds 5: 1 + 5 = 6.",
      explanation="`&&` and `||` skip the right operand when the left operand decides the result. An exception skips the rest of the `try` block.")

trace(B, T_CALL, "What is printed as a result of executing the following code segment?", body='show(5);\nshow(5.0);\nshow(\'a\');\nshow(5L);\nshow("5");',
      members='    public static void show(int x) { System.out.print("int "); }\n    public static void show(double x) { System.out.print("double "); }\n    public static void show(String x) { System.out.print("String "); }\n',
      manual=[("int double String double String", "A `char` is not a `String`. `show('a')` uses the `int` version because `char` widens to `int`."),
              ("int double int int String", "A `long` cannot be converted to `int` without a cast, so `show(5L)` uses `show(double x)`, which a `long` widens to."),
              ("double double double double String", "`show(5)` matches `show(int)` exactly, and the compiler prefers an exact match over a widening conversion.")],
      correct_expl="`show(5)` is an exact match for `int`. `show(5.0)` matches `double`. A `char` widens to `int`, so `show('a')` prints int. A `long` widens to `double` (but not to `int`), so `show(5L)` prints double. `show(\"5\")` matches `String`.",
      explanation="Java chooses the overload with the most specific applicable parameter type, using widening conversions (such as `char` to `int` and `long` to `double`) when there is no exact match.")

trace(B, T_STR, Q, body='String s = "banana";\nint first = s.indexOf("a");\nint second = s.indexOf("a", first + 1);\nint last = s.lastIndexOf("a");\nSystem.out.println(first + " " + second + " " + last + " " + s.indexOf("n", 4) + " " + s.indexOf("x"));',
      manual=[("1 1 5 4 -1", "`indexOf(\"a\", first + 1)` starts searching at index 2, so it finds the second \"a\" at 3, not the first one again."),
              ("1 3 5 2 -1", "`indexOf(\"n\", 4)` starts the search at index 4, so the \"n\" at index 2 is skipped; the next \"n\" is at index 4."),
              ("1 3 5 4 0", "`indexOf` returns -1, not 0, when the string is not found.")],
      correct_expl="In \"banana\" the \"a\"s are at indexes 1, 3 and 5. `indexOf(\"a\")` is 1, searching from index 2 finds 3, `lastIndexOf` is 5. Searching for \"n\" from index 4 finds the one at 4. \"x\" is not found, so -1.",
      explanation="`indexOf(str, from)` searches starting at index `from`. It returns -1 when there is no match.")

trace(B, T_MATH, Q, body='System.out.println(Math.max(Math.min(7, 3), Math.abs(-5 / 2)) + " " + (int) Math.ceil(7 / 2) + " " + Math.ceil(7 / 2.0));',
      mutants=[("Math.abs(-5 / 2)", "Math.abs(-5 / 2.0)", "This treats `-5 / 2` as exact (-2.5). Both operands are `int`, so it is integer division, -2, and `Math.abs` gives 2."),
               ("(int) Math.ceil(7 / 2)", "(int) Math.ceil(7 / 2.0)", "This treats `7 / 2` as 3.5. It is integer division: 3, so `Math.ceil(3)` is 3.0.")],
      manual=[("3 3 3.0", "`Math.ceil` rounds *up*: `7 / 2.0` is 3.5, so `Math.ceil` gives 4.0, not 3.0.")],
      correct_expl="`Math.min(7, 3)` is 3. `-5 / 2` is -2 (integer division), so `Math.abs` gives 2, and `Math.max(3, 2)` is 3 (an `int`). `7 / 2` is 3, so `(int) Math.ceil(3)` is 3. `Math.ceil(3.5)` is 4.0.",
      explanation="`Math.max`, `Math.min` and `Math.abs` return the same type as their arguments here (`int`), while `Math.ceil` always returns a `double`.")

trace(B, T_STR, Q, body='String d = "2024-10-05";\nString mid = d.substring(d.indexOf("-") + 1, d.lastIndexOf("-"));\nint m = Integer.parseInt(mid) + 1;\nSystem.out.println(mid + " " + m + " " + d.substring(d.lastIndexOf("-")));',
      mutants=[("d.indexOf(\"-\") + 1", "d.indexOf(\"-\")", "This starts the substring at the first hyphen, so `mid` is \"-10\". The `+ 1` skips the hyphen.")],
      manual=[("10 11 05", "`substring(d.lastIndexOf(\"-\"))` starts *at* the last hyphen, so the hyphen is included: \"-05\"."),
              ("10 101 -05", "`Integer.parseInt(mid) + 1` adds numbers: both operands are `int`, so the result is 11, not the text \"101\".")],
      correct_expl="The first hyphen is at index 4 and the last at index 7, so `substring(5, 7)` is \"10\". `Integer.parseInt(\"10\") + 1` is 11. `substring(7)` runs from the last hyphen to the end: \"-05\".",
      explanation="Add 1 to skip the delimiter at the start; `substring(from)` includes the character at `from`.")

trace(B, T_CRE, Q, body="Rectangle r = new Rectangle(2, 3);\nRectangle s = r.scaled(2);\nr.scale(3);\nSystem.out.println(r.area() + \" \" + s.area());",
      classes="class Rectangle {\n    private int w, h;\n    public Rectangle(int w, int h) { this.w = w; this.h = h; }\n    public void scale(int k) { w *= k; h *= k; }\n    public Rectangle scaled(int k) { return new Rectangle(w * k, h * k); }\n    public int area() { return w * h; }\n}\n",
      mutants=[("Rectangle s = r.scaled(2);", "Rectangle s = r;", "This treats `s` as an alias of `r`. `scaled` returns a *new* object, so `s` is independent of later changes to `r`."),
               ("r.scale(3);", "r.scaled(3);", "This assumes `r.scale(3)` has no effect, as if the result were discarded. `scale` is a `void` method that modifies `r` itself."),
               ("Rectangle s = r.scaled(2);\nr.scale(3);", "r.scale(3);\nRectangle s = r.scaled(2);", "This reverses the order of the two statements. In the original, `s` is created before `r` is scaled by 3.")],
      correct_expl="`r.scaled(2)` creates a new 4 by 6 rectangle for `s` (area 24) without changing `r`. Then `r.scale(3)` changes `r` itself to 6 by 9 (area 54).",
      explanation="A method that returns a new object leaves the original unchanged; a `void` mutator changes the object it is called on.")

trace(B, T_CRE, Q, body="Point[] pts = new Point[3];\nPoint shared = new Point(0, 0);\npts[0] = shared;\npts[1] = shared;\npts[2] = new Point(0, 0);\npts[0].move(2, 2);\npts[2].move(1, 1);\nSystem.out.println(pts[0].getX() + \" \" + pts[1].getX() + \" \" + pts[2].getX());",
      classes=POINT,
      mutants=[("pts[1] = shared;", "pts[1] = new Point(0, 0);", "This treats `pts[1]` as a separate object. `pts[1] = shared;` stores the same reference as `pts[0]`, so a move through `pts[0]` is also visible through `pts[1]`."),
               ("pts[2] = new Point(0, 0);", "pts[2] = shared;", "This makes all three elements refer to one object. `pts[2]` refers to a separate `Point` created by `new`, so moving it does not change the shared object.")],
      manual=[("0 0 1", "This assumes `pts[0].move(2, 2)` moves a copy. The array holds references, so the call changes the object that `shared` and `pts[1]` also refer to.")],
      correct_expl="`pts[0]` and `pts[1]` hold the same reference, so moving through `pts[0]` by 2 changes both: x is 2 for each. `pts[2]` is a separate object that moves by 1.",
      explanation="An array of objects holds references. Elements that hold the same reference name the same object.")

# ------------------------------------------------------------------ FRQs
members_a = '''
    public static String removeVowels(String str) {
        String result = "";
        for (int i = 0; i < str.length(); i++) {
            String ch = str.substring(i, i + 1);
            if ("aeiouAEIOU".indexOf(ch) < 0) {
                result += ch;
            }
        }
        return result;
    }

    public static int countSub(String str, String sub) {
        int count = 0;
        int pos = str.indexOf(sub);
        while (pos >= 0) {
            count++;
            pos = str.indexOf(sub, pos + 1);
        }
        return count;
    }
'''
verify(members_a, [('removeVowels("Programming")', "Prgrmmng"), ('removeVowels("AEIOU")', ""), ('removeVowels("sky")', "sky"), ('removeVowels("Education")', "dctn"),
                   ('countSub("banana", "ana")', 2), ('countSub("aaaa", "aa")', 3), ('countSub("abc", "x")', 0), ('countSub("abcabc", "abc")', 2)])
B.frq(T_STR,
      "The class `TextTools` contains the two methods described below.\n\n```java\npublic class TextTools {\n    /** Returns a String containing the characters of str, in their original order,\n     *  with every vowel (a, e, i, o, u, in either upper or lower case) removed. */\n    public static String removeVowels(String str)\n    { /* to be implemented in part (a) */ }\n\n    /** Returns the number of times sub appears in str. Occurrences may overlap.\n     *  Precondition: sub.length() > 0 */\n    public static int countSub(String str, String sub)\n    { /* to be implemented in part (b) */ }\n}\n```\n\n**(a)** Write the method `removeVowels`. For example, `removeVowels(\"Programming\")` returns `\"Prgrmmng\"`, and `removeVowels(\"AEIOU\")` returns the empty string.\n\n**(b)** Write the method `countSub`. The only `String` methods you may use are `length`, `substring`, `indexOf` (either form) and `equals`. For example, `countSub(\"banana\", \"ana\")` returns 2 (the occurrences start at indexes 1 and 3), `countSub(\"aaaa\", \"aa\")` returns 3 and `countSub(\"abc\", \"x\")` returns 0.",
      [(1, "(a) Traverses every character (index) of `str`"),
       (1, "(a) Isolates each character correctly (`charAt` or `substring(i, i + 1)`)"),
       (1, "(a) Tests for a vowel in either case"),
       (1, "(a) Builds the result with only the non-vowels, in order, and returns it"),
       (1, "(b) Finds an occurrence with `indexOf` and loops until none is found (`-1`)"),
       (1, "(b) Searches again from an index that allows overlapping matches (`pos + 1`, not `pos + sub.length()`)"),
       (1, "(b) Counts each match and returns the count")],
      "```java\npublic static String removeVowels(String str) {\n    String result = \"\";\n    for (int i = 0; i < str.length(); i++) {\n        String ch = str.substring(i, i + 1);\n        if (\"aeiouAEIOU\".indexOf(ch) < 0) {\n            result += ch;\n        }\n    }\n    return result;\n}\n\npublic static int countSub(String str, String sub) {\n    int count = 0;\n    int pos = str.indexOf(sub);\n    while (pos >= 0) {\n        count++;\n        pos = str.indexOf(sub, pos + 1);\n    }\n    return count;\n}\n```\nIn (b), searching again from `pos + 1` (not `pos + sub.length()`) is what lets overlapping matches be counted.")

classes_b = "class Rectangle {\n    private double width, height;\n    public Rectangle(double w, double h) { width = w; height = h; }\n    public double getWidth() { return width; }\n    public double getHeight() { return height; }\n    public double area() { return width * height; }\n    public Rectangle scaled(double factor) { return new Rectangle(width * factor, height * factor); }\n}\n"
members_b = '''
    public static Rectangle larger(Rectangle a, Rectangle b) {
        if (b.area() > a.area()) {
            return b;
        }
        return a;
    }

    public static Rectangle stacked(Rectangle a, Rectangle b) {
        return new Rectangle(Math.max(a.getWidth(), b.getWidth()), a.getHeight() + b.getHeight());
    }

    public static Rectangle scaleToArea(Rectangle r, double targetArea) {
        return r.scaled(Math.sqrt(targetArea / r.area()));
    }
'''
verify(members_b + "\n    public static String d(Rectangle r) { return r.getWidth() + \"x\" + r.getHeight(); }\n",
       [("d(larger(new Rectangle(2, 3), new Rectangle(1, 7)))", "1.0x7.0"), ("d(larger(new Rectangle(2, 3), new Rectangle(3, 2)))", "2.0x3.0"),
        ("d(stacked(new Rectangle(4, 1), new Rectangle(2, 3)))", "4.0x4.0"), ("d(scaleToArea(new Rectangle(2, 3), 24))", "4.0x6.0")], classes=classes_b)
B.frq(T_CALL,
      "The `Rectangle` class is shown below. You may assume it is already written and works as described.\n\n```java\npublic class Rectangle {\n    public Rectangle(double w, double h)      // creates a w by h rectangle\n    public double getWidth()\n    public double getHeight()\n    public double area()                      // width times height\n    public Rectangle scaled(double factor)    // returns a NEW rectangle whose width and\n                                              // height are each multiplied by factor\n}\n```\n\nThe class `RectTools` contains the three static methods described below. You may not change any `Rectangle` object that is passed to a method.\n\n```java\npublic class RectTools {\n    /** Returns whichever of a and b has the greater area. If the areas are equal, returns a. */\n    public static Rectangle larger(Rectangle a, Rectangle b)\n    { /* to be implemented in part (a) */ }\n\n    /** Returns a new Rectangle that could hold a on top of b: its width is the greater\n     *  of the two widths and its height is the sum of the two heights. */\n    public static Rectangle stacked(Rectangle a, Rectangle b)\n    { /* to be implemented in part (b) */ }\n\n    /** Returns a new Rectangle with the same shape as r (the same ratio of width to height)\n     *  whose area is targetArea. Precondition: r.area() > 0 and targetArea > 0 */\n    public static Rectangle scaleToArea(Rectangle r, double targetArea)\n    { /* to be implemented in part (c) */ }\n}\n```\n\n**(a)** Write the method `larger`.\n\n**(b)** Write the method `stacked`.\n\n**(c)** Write the method `scaleToArea`. For example, if `r` is a 2 by 3 rectangle, then `scaleToArea(r, 24)` returns a 4 by 6 rectangle.",
      [(1, "(a) Compares the areas by calling `area()` on both rectangles"),
       (1, "(a) Returns the correct rectangle reference, `a` when the areas are equal"),
       (1, "(b) Creates and returns a new `Rectangle` with the `Rectangle` constructor"),
       (1, "(b) Uses the greater width (`Math.max` or equivalent) and the sum of the heights"),
       (1, "(c) Computes the scale factor as the square root of `targetArea / r.area()`"),
       (1, "(c) Returns a new scaled rectangle (using `scaled` or the constructor) without modifying `r`")],
      "```java\npublic static Rectangle larger(Rectangle a, Rectangle b) {\n    if (b.area() > a.area()) {\n        return b;\n    }\n    return a;\n}\n\npublic static Rectangle stacked(Rectangle a, Rectangle b) {\n    return new Rectangle(Math.max(a.getWidth(), b.getWidth()), a.getHeight() + b.getHeight());\n}\n\npublic static Rectangle scaleToArea(Rectangle r, double targetArea) {\n    return r.scaled(Math.sqrt(targetArea / r.area()));\n}\n```\nScaling both sides by a factor `k` multiplies the area by $k^2$, so to reach `targetArea` the factor is $k=\\sqrt{\\text{targetArea}/\\text{area}}$.")

B.save()
B.brief()
