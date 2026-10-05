from common import *

B = bank(7, "unit-7-arraylist")
T_INT, T_METH, T_TRA, T_ALG = ("arraylist-intro", "arraylist-methods", "traversing-arraylists", "arraylist-algorithms")
Q = "What is printed as a result of executing the following code segment?"

trace(B, T_TRA, Q, body="ArrayList<Integer> list = new ArrayList<Integer>();\nint[] vals = {1, 2, 2, 3, 2, 4, 2, 2};\nfor (int v : vals)\n    list.add(v);\nfor (int i = 0; i < list.size(); i++) {\n    if (list.get(i) == 2)\n        list.remove(i);\n}\nSystem.out.println(list);",
      mutants=[("for (int i = 0; i < list.size(); i++) {\n    if (list.get(i) == 2)\n        list.remove(i);\n}", "for (int i = list.size() - 1; i >= 0; i--) {\n    if (list.get(i) == 2)\n        list.remove(i);\n}", "This is what you get by traversing from the end. Going backward, a removal shifts only elements that have already been checked, so every 2 is removed."),
               ("list.remove(i);", "list.remove(Integer.valueOf(2));", "This assumes that each removal deletes the *first* 2 in the list. The code calls `remove(int index)`, which removes the element at position `i`.")],
      manual=[("[1, 3, 4, 2]", "This assumes only the last 2 survives. After each removal the elements shift left, and the loop then moves on to the next index, skipping the element that moved into position `i`.")],
      correct_expl="After a removal the later elements shift one position to the left, but `i` still increments, so the element that moved into position `i` is skipped. Consecutive 2s are therefore not all removed: the list ends as [1, 2, 3, 4, 2].",
      explanation="When removing while traversing forward, either decrement the index after a removal or traverse the list from the end.")

trace(B, T_METH, Q, body="ArrayList<String> a = new ArrayList<String>();\na.add(\"A\");\na.add(\"B\");\na.add(1, \"C\");\nString old = a.set(0, \"D\");\na.add(a.size(), \"E\");\nString gone = a.remove(2);\nSystem.out.println(a + \" \" + old + \" \" + gone + \" \" + a.size());",
      mutants=[("a.add(1, \"C\");", "a.set(1, \"C\");", "This treats `add(1, \"C\")` as a replacement. `add(index, element)` inserts and shifts the later elements to the right, so the list grows."),
               ("a.remove(2)", "a.remove(1)", "This removes index 1 instead of index 2. After the earlier operations the list is [D, C, B, E], so index 2 is \"B\".")],
      manual=[("[D, C, E] D B 3", "`set(0, \"D\")` returns the value that was replaced, \"A\", not the new value.")],
      correct_expl="After the adds, the list is [A, C, B] (C is inserted at index 1). `set(0, \"D\")` replaces A and returns it: [D, C, B]. `add(3, \"E\")` appends. `remove(2)` removes and returns B, leaving [D, C, E].",
      explanation="`add(i, x)` inserts and shifts, `set` replaces and returns the old value, and `remove(i)` removes and returns the element.")

trace(B, T_METH, Q, body="ArrayList<Integer> a = new ArrayList<Integer>();\nfor (int v : new int[] {10, 20, 30, 1, 2})\n    a.add(v);\na.remove(1);\na.remove(Integer.valueOf(1));\nSystem.out.println(a + \" \" + a.indexOf(30) + \" \" + a.contains(20));",
      mutants=[("a.remove(1);", "a.remove(Integer.valueOf(1));", "This reads `a.remove(1)` as removing the value 1. With an `int` argument, `remove` removes the element at *index* 1 (the 20), not the value 1."),
               ("a.remove(Integer.valueOf(1));", "a.remove(1);", "This makes both calls remove by index. The second call passes an `Integer` object, which removes the first element equal to 1.")],
      manual=[("[10, 30, 1, 2] 1 false", "This stops after the first removal. The second call, `remove(Integer.valueOf(1))`, also removes the value 1.")],
      correct_expl="`a.remove(1)` removes the element at index 1 (20), leaving [10, 30, 1, 2]. `a.remove(Integer.valueOf(1))` removes the value 1, leaving [10, 30, 2]. Then 30 is at index 1, and 20 is no longer in the list.",
      explanation="On an `ArrayList<Integer>`, `remove(int)` removes by index and `remove(Object)` removes by value; an `Integer` argument selects the second.")

trace(B, T_INT, Q, body="ArrayList<String> a = new ArrayList<String>();\nArrayList<String> b = a;\nb.add(\"x\");\nArrayList<String> c = new ArrayList<String>(a);\nc.add(\"y\");\na.add(\"z\");\nSystem.out.println(a.size() + \" \" + b.size() + \" \" + c.size() + \" \" + (a == b) + \" \" + a.equals(c) + \" \" + c);",
      manual=[("1 1 2 true false [x, y]", "This leaves out `a.add(\"z\")`. `a` and `b` are the same list, so after the last statement both have size 2."),
              ("2 1 2 true false [x, y]", "`b = a` copies the reference, so `a` and `b` are one list and always have the same size."),
              ("2 2 2 true true [x, y]", "`a` is [x, z] and `c` is [x, y]; they have the same size but different contents, so `a.equals(c)` is false.")],
      correct_expl="`b` refers to the same list as `a`, so `b.add(\"x\")` is seen through `a`. `new ArrayList<String>(a)` makes an independent copy [x]; adding \"y\" to `c` does not affect `a`, and adding \"z\" to `a` does not affect `c`. `a` and `b` have size 2, `c` is [x, y], and `a.equals(c)` is false because [x, z] differs from [x, y].",
      explanation="Assigning a list variable copies the reference; the copy constructor creates an independent list.")

trace(B, T_ALG, Q, body="ArrayList<Integer> a = new ArrayList<Integer>();\nfor (int v : new int[] {2, 5, 9, 12})\n    a.add(v);\nint x = 7;\nint i = 0;\nwhile (i < a.size() && a.get(i) < x)\n    i++;\na.add(i, x);\nint y = 1;\ni = 0;\nwhile (i < a.size() && a.get(i) < y)\n    i++;\na.add(i, y);\nSystem.out.println(a);",
      manual=[("[2, 5, 9, 12, 7, 1]", "This appends both values. The loops find the position where each value belongs, and `add(i, value)` inserts it there."),
              ("[2, 5, 7, 9, 12, 1]", "This inserts 7 correctly but puts 1 at the end. For 1, the `while` loop stops immediately at index 0, because 2 is not less than 1, so 1 is inserted at the front."),
              ("[1, 2, 5, 9, 7, 12]", "This inserts 7 one position too late. The loop stops at the first element that is not less than 7, which is 9 at index 3, so 7 goes before it.")],
      correct_expl="For 7 the loop advances past 2 and 5 and stops at index 2 (9 is not less than 7), so 7 is inserted there: [2, 5, 7, 9, 12]. For 1 the loop stops at index 0, so 1 is inserted first: [1, 2, 5, 7, 9, 12].",
      explanation="Walk the sorted list until the first element that is not smaller than the new value, and insert at that index. The `i < a.size()` test comes first to avoid going past the end.")

trace(B, T_ALG, Q, body="ArrayList<String> w = new ArrayList<String>();\nfor (String s : new String[] {\"a\", \"a\", \"b\", \"b\", \"b\", \"c\", \"a\"})\n    w.add(s);\nfor (int i = w.size() - 1; i > 0; i--) {\n    if (w.get(i).equals(w.get(i - 1)))\n        w.remove(i);\n}\nSystem.out.println(w);",
      mutants=[("for (int i = w.size() - 1; i > 0; i--) {\n    if (w.get(i).equals(w.get(i - 1)))\n        w.remove(i);\n}", "for (int i = 1; i < w.size(); i++) {\n    if (w.get(i).equals(w.get(i - 1)))\n        w.remove(i);\n}", "This traverses forward, so after a removal the next element is skipped, and one duplicate \"b\" survives. The original loop goes backward.")],
      manual=[("[a, b, c]", "This removes *every* duplicate, including the last \"a\". The code compares each element only with the one just before it, so the final \"a\" (next to \"c\") stays."),
              ("[a, a, b, b, b, c, a]", "The loop does remove consecutive duplicates; the list does not stay unchanged.")],
      correct_expl="Going backward, each element equal to the one before it is removed: the repeated \"b\"s collapse to one and the repeated \"a\" collapses to one. The last \"a\" follows a \"c\", so it stays: [a, b, c, a].",
      explanation="Removing duplicates of adjacent elements is safest when traversing from the end, because removals shift only elements that have already been examined.")

trace(B, T_ALG, Q, body="ArrayList<Integer> a = new ArrayList<Integer>();\nfor (int v : new int[] {1, 2, 3, 4, 5})\n    a.add(v);\nfor (int i = 0; i < a.size() / 2; i++) {\n    int t = a.get(i);\n    a.set(i, a.get(a.size() - 1 - i));\n    a.set(a.size() - 1 - i, t);\n}\nSystem.out.println(a);",
      mutants=[("i < a.size() / 2", "i < a.size()", "This swaps every pair twice, which restores the original order. The loop must stop at the middle.")],
      manual=[("[5, 4, 3, 4, 5]", "This leaves out the temporary variable. Without `t`, the first `set` overwrites a value before it can be copied to the other position."),
              ("[5, 2, 3, 4, 1]", "This stops after one swap. For size 5, `a.size() / 2` is 2, so the positions 1 and 3 are swapped as well.")],
      correct_expl="Two swaps (i = 0 and i = 1) exchange positions 0 and 4, and positions 1 and 3; the middle element stays: [5, 4, 3, 2, 1].",
      explanation="Reversing a list in place swaps symmetric pairs and uses a temporary variable (or the value returned by `set`).")

trace(B, T_METH, Q, body="ArrayList<Integer> a = new ArrayList<Integer>();\na.add(4); a.add(5); a.add(6);\nString out = \"\";\ntry { a.add(3, 7); out += \"A\" + a.size(); } catch (IndexOutOfBoundsException e) { out += \"X\"; }\ntry { a.add(5, 8); out += \"B\" + a.size(); } catch (IndexOutOfBoundsException e) { out += \"Y\"; }\ntry { a.get(a.size()); out += \"C\"; } catch (IndexOutOfBoundsException e) { out += \"Z\"; }\ntry { a.set(a.size() - 1, 0); out += \"D\"; } catch (IndexOutOfBoundsException e) { out += \"W\"; }\nSystem.out.println(out);",
      manual=[("XYZD", "`add(index, element)` allows an index equal to the size (it appends), so `a.add(3, 7)` on a list of size 3 succeeds."),
              ("A4B5ZD", "`add(5, 8)` on a list of size 4 is out of range: valid indexes for `add` are 0 through the size."),
              ("A4YCD", "`get(a.size())` is out of bounds. For `get` and `set`, valid indexes are 0 through size - 1.")],
      correct_expl="`add(3, 7)` on a list of size 3 is allowed (index equal to the size), so the list has size 4 and the first block prints A4. `add(5, 8)` is beyond the size, so Y. `get(4)` is out of bounds on a list of size 4: Z. `set(3, 0)` is the last valid index, so D.",
      explanation="`add(i, x)` accepts 0 through `size()`; `get(i)`, `set(i, x)` and `remove(i)` accept 0 through `size() - 1`.")

trace(B, T_TRA, Q, body="ArrayList<Integer> in = new ArrayList<Integer>();\nfor (int v : new int[] {5, 12, 7, 20, 3, 18})\n    in.add(v);\nArrayList<Integer> out = new ArrayList<Integer>();\nfor (int i = 0; i < in.size(); i++)\n    if (in.get(i) % 2 == 0 || i == 0)\n        out.add(in.get(i) / 2);\nin.set(0, -1);\nSystem.out.println(out + \" \" + in);",
      manual=[("[5, 12, 20, 18] [-1, 12, 7, 20, 3, 18]", "This leaves out the division by 2. The code adds `in.get(i) / 2`, which for the first element 5 is integer division, 2."),
              ("[6, 10, 9] [-1, 12, 7, 20, 3, 18]", "This leaves out the first element. The condition has `|| i == 0`, so index 0 is included even though 5 is odd."),
              ("[2, 6, 10, 9] [5, 12, 7, 20, 3, 18]", "This assumes `set` has no effect. `in.set(0, -1)` replaces the first element of `in`.")],
      correct_expl="Indexes 1 (12), 3 (20) and 5 (18) are even, and index 0 is included by `i == 0`; halved with integer division they give 2, 6, 10, 9. The later `in.set(0, -1)` changes only `in`, not `out`.",
      explanation="Values added to a second list are independent of later changes to the first list when the elements are immutable `Integer` objects.")

trace(B, T_ALG, Q, body="ArrayList<Integer> a = new ArrayList<Integer>();\nArrayList<Integer> b = new ArrayList<Integer>();\nfor (int v : new int[] {1, 4, 6}) a.add(v);\nfor (int v : new int[] {2, 3, 7, 9}) b.add(v);\nArrayList<Integer> m = new ArrayList<Integer>();\nint i = 0, j = 0;\nwhile (i < a.size() && j < b.size()) {\n    if (a.get(i) <= b.get(j)) { m.add(a.get(i)); i++; }\n    else { m.add(b.get(j)); j++; }\n}\nwhile (i < a.size()) { m.add(a.get(i)); i++; }\nSystem.out.println(m + \" \" + i + \" \" + j);",
      manual=[("[1, 2, 3, 4, 6, 7, 9] 3 4", "This assumes the leftover elements of `b` (7 and 9) are appended. The code has a loop for the leftover elements of `a` only, so they are never added to `m`."),
              ("[1, 2, 3, 4] 2 2", "The first loop continues until one list is exhausted. It stops only when `a` is used up (i = 3), so 6 is added too."),
              ("[1, 2, 3, 4, 6] 3 4", "`j` is 2 when the loop ends, because the loop stops as soon as `a` is exhausted, before 7 and 9 are examined.")],
      correct_expl="The merge loop takes 1, 2, 3, 4, 6 in order and ends when `a` is exhausted (i = 3, j = 2). The remaining loop copies leftovers of `a`, but `a` has none; the leftovers of `b` (7 and 9) are never copied.",
      explanation="A merge needs a final loop for the leftovers of *each* list; this code has only one, so elements are lost.")

trace(B, T_INT, Q, body="ArrayList<String> words = new ArrayList<String>();\nfor (String s : new String[] {\"to\", \"be\", \"or\", \"not\", \"to\", \"be\"})\n    words.add(s);\nArrayList<String> seen = new ArrayList<String>();\nint dup = 0;\nfor (String w : words) {\n    if (seen.contains(w))\n        dup++;\n    else\n        seen.add(w);\n}\nSystem.out.println(seen + \" \" + dup);",
      mutants=[("if (seen.contains(w))\n        dup++;\n    else\n        seen.add(w);", "if (!seen.contains(w))\n        seen.add(w);\n    dup++;", "This counts every word as a duplicate. In the original, `dup++` is only the `if` branch, which runs when the word has been seen.")],
      manual=[("[to, be, or, not, to, be] 0", "This assumes `seen.contains(w)` is always false. After \"to\" and \"be\" are added to `seen`, their second occurrences are found."),
              ("[to, be, or, not] 4", "There are only two repeated words (\"to\" and \"be\"), so `dup` is 2.")],
      correct_expl="`seen` collects each word the first time it appears: to, be, or, not. The second \"to\" and the second \"be\" are already in `seen`, so `dup` is 2.",
      explanation="`contains` uses `equals` to look for a matching element, so identical strings are found.")

CL = 'class P {\n    private int x;\n    public P(int x) { this.x = x; }\n}\nclass Q {\n    private int x;\n    public Q(int x) { this.x = x; }\n    public boolean equals(Object o) { return o instanceof Q && ((Q) o).x == x; }\n}\n'
trace(B, T_METH, Q, body="ArrayList<P> ps = new ArrayList<P>();\nps.add(new P(1));\nArrayList<Q> qs = new ArrayList<Q>();\nqs.add(new Q(1));\nP keep = new P(2);\nps.add(keep);\nSystem.out.println(ps.contains(new P(1)) + \" \" + qs.contains(new Q(1)) + \" \" + ps.contains(keep) + \" \" + ps.indexOf(keep) + \" \" + qs.indexOf(new Q(9)));",
      classes=CL,
      manual=[("true true true 1 -1", "`P` does not override `equals`, so `contains` and `indexOf` compare references. A new `P(1)` is a different object from the one in the list."),
              ("false false true 1 -1", "`Q` overrides `equals` to compare the field `x`, so a different `Q(1)` object is found by `contains`."),
              ("false true false 1 -1", "`ps.contains(keep)` is true: the list holds the same object that was added (the reference is equal)."),
              ]
      , correct_expl="`ArrayList.contains` and `indexOf` use `equals`. `P` does not override it, so a new `P(1)` is not found, but the same object `keep` is. `Q` overrides `equals` to compare `x`, so `new Q(1)` is found, and `new Q(9)` is not (-1).",
      explanation="`contains` and `indexOf` rely on `equals`; without an override, objects are equal only if they are the same object.")

trace(B, T_METH, Q, body="ArrayList<String> list = new ArrayList<String>();\nlist.add(\"x\");\nadd2(list);\nreset(list);\nSystem.out.println(list + \" \" + list.size());",
      members="    public static void add2(ArrayList<String> l) {\n        l.add(\"y\");\n        l.add(\"z\");\n    }\n    public static void reset(ArrayList<String> l) {\n        l = new ArrayList<String>();\n        l.add(\"new\");\n    }\n",
      manual=[("[new] 1", "This assumes `reset` replaces the caller's list. Assigning a new list to the parameter `l` changes only the local copy of the reference."),
              ("[x] 1", "`add2` changes the list that the caller passed, so the elements \"y\" and \"z\" are added."),
              ("[x, y, z, new] 4", "`reset` creates a *new* list for its parameter, so \"new\" is added to that new list, not to the caller's.")],
      correct_expl="`add2` adds to the caller's list: [x, y, z]. In `reset`, the parameter `l` is made to refer to a new list, so the caller's list is unchanged.",
      explanation="A method can modify the list it is passed, but reassigning the parameter does not change the caller's variable.")

trace(B, T_ALG, Q, body="ArrayList<Integer> a = new ArrayList<Integer>();\nfor (int v : new int[] {3, 1, 4, 1, 5})\n    a.add(v);\nfor (int i = 1; i < a.size(); i++)\n    a.set(i, a.get(i) + a.get(i - 1));\nfor (int i = a.size() - 1; i > 0; i--)\n    a.set(i, a.get(i) - a.get(i - 1));\na.add(0, a.remove(a.size() - 1));\nSystem.out.println(a);",
      mutants=[("for (int i = a.size() - 1; i > 0; i--)\n    a.set(i, a.get(i) - a.get(i - 1));", "for (int i = 1; i < a.size(); i++)\n    a.set(i, a.get(i) - a.get(i - 1));", "This undoes the running totals from the front. Each subtraction then uses an element that has already been changed, so the original values are not recovered; the code works from the end."),
               ("a.add(0, a.remove(a.size() - 1));", "a.add(a.remove(0));", "This moves the *first* element to the end. The code removes the last element and inserts it at index 0, which rotates the list to the right.")],
      manual=[("[3, 1, 4, 1, 5]", "The last statement rotates the list: the final 5 is removed and inserted at index 0, so the output does not match the original order.")],
      correct_expl="The first loop turns the list into running totals [3, 4, 8, 9, 14]. The second loop, working from the end, subtracts each previous total to recover [3, 1, 4, 1, 5]. Finally the last element, 5, is removed and inserted at index 0: [5, 3, 1, 4, 1].",
      explanation="Prefix sums can be undone by subtracting from the end of the list. Removing the last element and inserting it at index 0 rotates the list right.")

for stmt, ok in [("ArrayList<Integer> a = new ArrayList<Integer>();\nint n = a.length;", False), ("ArrayList<Integer> a = new ArrayList<Integer>();\nint n = a.length();", False), ("ArrayList<Integer> a = new ArrayList<Integer>();\nint n = a.size();", True), ("ArrayList<int> a = new ArrayList<int>();", False)]:
    assert (compile_error(program(stmt)) is None) == ok, stmt
B.mcq(T_INT, "Which of the following code segments compiles without error?",
      ch("`ArrayList<Integer> a = new ArrayList<Integer>(); int n = a.size();`", "The number of elements in an `ArrayList` is given by the method `size()`, and `Integer` is the wrapper type used for `int` values in a list."),
      [ch("`ArrayList<Integer> a = new ArrayList<Integer>(); int n = a.length;`", "`length` (without parentheses) belongs to arrays. An `ArrayList` has no `length` field."),
       ch("`ArrayList<Integer> a = new ArrayList<Integer>(); int n = a.length();`", "`length()` is a method of `String`. For an `ArrayList`, use `size()`."),
       ch("`ArrayList<int> a = new ArrayList<int>();`", "The type argument must be a class: use the wrapper class `Integer` rather than the primitive type `int`.")],
      "Array: `length`; `String`: `length()`; `ArrayList`: `size()`. An `ArrayList` holds objects, so `int` values use `Integer`.")

# ------------------------------------------------------------------ FRQs
students = '''
class Student {
    private String name;
    private int grade;
    public Student(String name, int grade) { this.name = name; this.grade = grade; }
    public String getName() { return name; }
    public int getGrade() { return grade; }
}

class Roster {
    private ArrayList<Student> students;
    public Roster() { students = new ArrayList<Student>(); }
    public void add(Student s) { students.add(s); }
    public int size() { return students.size(); }

    public ArrayList<String> namesAtOrAbove(int threshold) {
        ArrayList<String> result = new ArrayList<String>();
        for (Student s : students) {
            if (s.getGrade() >= threshold) {
                result.add(s.getName());
            }
        }
        return result;
    }

    public int removeBelow(int cutoff) {
        int removed = 0;
        for (int i = students.size() - 1; i >= 0; i--) {
            if (students.get(i).getGrade() < cutoff) {
                students.remove(i);
                removed++;
            }
        }
        return removed;
    }

    public String names() {
        String s = "";
        for (Student st : students) s += st.getName() + " ";
        return s.trim();
    }
}
'''
rb = 'Roster r = new Roster();\nr.add(new Student("Ann", 90));\nr.add(new Student("Bo", 55));\nr.add(new Student("Cy", 55));\nr.add(new Student("Di", 70));\nr.add(new Student("Ed", 40));\nSystem.out.println(r.namesAtOrAbove(70));\nSystem.out.println(r.namesAtOrAbove(100));\nSystem.out.println(r.removeBelow(60));\nSystem.out.println(r.names());\nSystem.out.println(r.size());'
assert run(program(rb, classes=students)) == "[Ann, Di]\n[]\n3\nAnn Di\n2"
B.frq(T_TRA,
      "A `Roster` object stores `Student` objects in an `ArrayList<Student>` instance variable named `students`. The `Student` class has the methods `String getName()` and `int getGrade()`.\n\n```java\npublic class Roster {\n    private ArrayList<Student> students;\n\n    /** Returns a new ArrayList containing the names of the students whose grade is at least\n     *  threshold, in the order the students appear in students. Does not change students.\n     *  Returns an empty list if no student qualifies. */\n    public ArrayList<String> namesAtOrAbove(int threshold)\n    { /* to be implemented in part (a) */ }\n\n    /** Removes from students every student whose grade is less than cutoff, keeping the\n     *  remaining students in their original order. Returns the number of students removed. */\n    public int removeBelow(int cutoff)\n    { /* to be implemented in part (b) */ }\n}\n```\n\n**(a)** Write the method `namesAtOrAbove`.\n\n**(b)** Write the method `removeBelow`. Be careful that every qualifying student is removed, including two such students in a row.",
      [(1, "(a) Creates a new `ArrayList<String>` and traverses `students`"),
       (1, "(a) Compares each student's grade (using `getGrade`) with `threshold` correctly (at least)"),
       (1, "(a) Adds each qualifying student's name (using `getName`) and returns the list without modifying `students`"),
       (1, "(b) Traverses `students` in a way that does not skip elements after a removal (for example from the end, or adjusting the index)"),
       (1, "(b) Removes each student whose grade is less than `cutoff`"),
       (1, "(b) Counts and returns the number of students removed")],
      "```java\npublic ArrayList<String> namesAtOrAbove(int threshold) {\n    ArrayList<String> result = new ArrayList<String>();\n    for (Student s : students) {\n        if (s.getGrade() >= threshold) {\n            result.add(s.getName());\n        }\n    }\n    return result;\n}\n\npublic int removeBelow(int cutoff) {\n    int removed = 0;\n    for (int i = students.size() - 1; i >= 0; i--) {\n        if (students.get(i).getGrade() < cutoff) {\n            students.remove(i);\n            removed++;\n        }\n    }\n    return removed;\n}\n```\nIn `removeBelow`, traversing from the end means a removal shifts only elements that have already been examined. (Traversing forward also works if the index is decremented after each removal.)")

inv = '''
class Item {
    private String name;
    private int qty;
    public Item(String name, int qty) { this.name = name; this.qty = qty; }
    public String getName() { return name; }
    public int getQty() { return qty; }
    public void setQty(int q) { qty = q; }
}

class Inventory {
    private ArrayList<Item> items = new ArrayList<Item>();

    public void restock(String name, int amount) {
        for (Item it : items) {
            if (it.getName().equals(name)) {
                it.setQty(it.getQty() + amount);
                return;
            }
        }
        items.add(new Item(name, amount));
    }

    public int removeEmpty() {
        int count = 0;
        int i = 0;
        while (i < items.size()) {
            if (items.get(i).getQty() == 0) {
                items.remove(i);
                count++;
            } else {
                i++;
            }
        }
        return count;
    }

    public void use(String name, int n) {
        for (Item it : items) {
            if (it.getName().equals(name)) it.setQty(it.getQty() - n);
        }
    }

    public String show() {
        String s = "";
        for (Item it : items) s += it.getName() + ":" + it.getQty() + " ";
        return s.trim();
    }
}
'''
ib = 'Inventory v = new Inventory();\nv.restock("bolt", 5);\nv.restock("nut", 2);\nv.restock("bolt", 3);\nSystem.out.println(v.show());\nv.use("nut", 2);\nv.restock("gear", 0);\nv.restock("cog", 0);\nv.restock("pin", 4);\nSystem.out.println(v.removeEmpty());\nSystem.out.println(v.show());'
assert run(program(ib, classes=inv)) == "bolt:8 nut:2\n3\nbolt:8 pin:4"
B.frq(T_ALG,
      "An `Inventory` object stores `Item` objects in an `ArrayList<Item>` instance variable named `items`. The `Item` class has the following methods.\n\n```java\npublic class Item {\n    public Item(String name, int qty)   // creates an item with the given name and quantity\n    public String getName()\n    public int getQty()\n    public void setQty(int q)\n}\n```\n\nThe `Inventory` class contains the two methods described below.\n\n```java\npublic class Inventory {\n    private ArrayList<Item> items;\n\n    /** If an item named name is in items, adds amount to its quantity. Otherwise adds a new\n     *  Item with that name and the quantity amount to the end of items. At most one item\n     *  in items has any given name. */\n    public void restock(String name, int amount)\n    { /* to be implemented in part (a) */ }\n\n    /** Removes every item whose quantity is 0, keeping the other items in their original\n     *  order, and returns the number of items removed. */\n    public int removeEmpty()\n    { /* to be implemented in part (b) */ }\n}\n```\n\n**(a)** Write the method `restock`.\n\n**(b)** Write the method `removeEmpty`. Be careful that no item with quantity 0 is skipped.",
      [(1, "(a) Traverses `items` and compares names with `equals` (not `==`)"),
       (1, "(a) Updates the quantity of the matching item and stops without adding a new item"),
       (1, "(a) Adds a new `Item` to the end of the list only when no item has that name"),
       (1, "(b) Traverses `items` without skipping elements after a removal"),
       (1, "(b) Removes each item whose quantity is 0 and keeps the others in order"),
       (1, "(b) Counts and returns the number of items removed")],
      "```java\npublic void restock(String name, int amount) {\n    for (Item it : items) {\n        if (it.getName().equals(name)) {\n            it.setQty(it.getQty() + amount);\n            return;\n        }\n    }\n    items.add(new Item(name, amount));\n}\n\npublic int removeEmpty() {\n    int count = 0;\n    int i = 0;\n    while (i < items.size()) {\n        if (items.get(i).getQty() == 0) {\n            items.remove(i);\n            count++;\n        } else {\n            i++;\n        }\n    }\n    return count;\n}\n```\nIn `restock`, the item is changed through its `setQty` method while the enhanced `for` loop is running; the loop only reads the list, so this is safe, and `return` ends the method before the new item is added. In `removeEmpty`, the index advances only when nothing was removed, so the element that shifts into position `i` is examined.")

B.save()
B.brief()
