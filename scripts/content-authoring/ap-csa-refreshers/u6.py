from common import code, finish

finish(6, [
("array-creation-and-access", r"""
### The idea
An array stores a fixed number of values of the same type in numbered slots. It is the basic way to handle a list of things in Java.

### Key facts
- Create one with `new`: `int[] scores = new int[4];` makes four slots. Or give the values directly: `int[] primes = {2, 3, 5, 7};`.
- The size is **fixed** when the array is created. It cannot grow or shrink.
- Indexes start at `0`. An array of length `n` has valid indexes `0` through `n - 1`.
- `scores.length` is the number of slots. There are no parentheses, because it is a field, not a method.
- A new array starts with default values: `0` for `int`, `0.0` for `double`, `false` for `boolean`, `null` for objects such as `String`.
- Using an index outside the valid range throws an `ArrayIndexOutOfBoundsException`.

### Watch out for
The last index. For an array of length `4`, the last valid index is `3`, so `scores[4]` is an error.

### Worked example
""" + code('''
int[] scores = new int[4];
scores[0] = 90;
scores[3] = 75;
String[] names = new String[2];
int[] primes = {2, 3, 5, 7};
System.out.println(scores[1] + " " + names[0] + " " + primes.length + " " + primes[3]);
''', out="0 null 4 7") + r"""

`scores[1]` was never set, so it is `0`. `names[0]` is `null`. `primes.length` is `4` and `primes[3]` is `7`. It prints `0 null 4 7`.
"""),
("traversing-arrays", r"""
### The idea
Traversing an array means visiting its elements one at a time, usually with a `for` loop that uses the index.

### Key facts
- The standard loop is `for (int i = 0; i < a.length; i++)`, using `a[i]` inside.
- The condition is `i < a.length`, not `i <= a.length`. The latter reaches an index that does not exist.
- To go backward, start at `a.length - 1` and count down while `i >= 0`.
- You can read an element (`a[i]`) or change it (`a[i] = ...`) while you traverse.
- To visit every other element, change the step, as in `i += 2`.
- Use the index loop whenever you need to know the position, or to change elements, or to look at neighbors such as `a[i + 1]`.

### Watch out for
Going one step too far. If a loop looks at `a[i + 1]`, it must stop one position earlier, at `i < a.length - 1`.

### Worked example
""" + code('''
int[] a = {4, 8, 15, 16};
int sum = 0;
for (int i = 0; i < a.length; i++) {
    sum += a[i];
}
System.out.println(sum);
for (int i = a.length - 1; i >= 0; i--) {
    System.out.print(a[i] + " ");
}
''', out="43\n16 15 8 4") + r"""

The first loop adds `4 + 8 + 15 + 16` and prints `43`. The second loop starts at the last index, `3`, and prints the elements in reverse: `16 15 8 4`.
"""),
("enhanced-for-arrays", r"""
### The idea
The enhanced `for` loop (for-each) walks through every element of an array without using an index. It is shorter, but it can only read.

### Key facts
- Syntax: `for (int v : a) { ... }`, read as "for each `v` in `a`".
- On each pass, `v` holds a **copy** of the next element, in order, from first to last.
- Changing `v` does **not** change the array when the elements are primitives or `String`.
- You cannot get the index, skip elements, or go backward with it.
- For an array of objects, `v` is a copy of the reference, so you **can** call a method on `v` that changes that object.
- Use it when you only need to read every element. Use the indexed loop when you need the position or want to change the array.

### Watch out for
Trying to double every value with `v = v * 2;` inside an enhanced loop. It changes only the loop variable.

### Worked example
""" + code('''
int[] a = {1, 2, 3};
for (int v : a) {
    v = v * 2;
}
System.out.println(a[0] + " " + a[1] + " " + a[2]);
for (int i = 0; i < a.length; i++) {
    a[i] = a[i] * 2;
}
System.out.println(a[0] + " " + a[1] + " " + a[2]);
''', out="1 2 3\n2 4 6") + r"""

After the enhanced loop the array is still `1 2 3`, because only the copy `v` changed. The indexed loop assigns into `a[i]`, so the array becomes `2 4 6`.
"""),
("array-algorithms", r"""
### The idea
A few patterns come up again and again: totals, finding the biggest, counting matches, searching, and rearranging. Learn the pattern and you can write most array code.

### Key facts
- **Sum or average:** keep a running total in a variable, then divide by `a.length` for the average (cast to `double` to avoid integer division).
- **Maximum or minimum:** start with the first element, then update when a later one is bigger (or smaller). Start from `a[0]`, not from `0`.
- **Count matches:** keep a counter and add `1` each time a test is true.
- **Search:** loop until you find the item, and return the index (or `-1` if you reach the end).
- **Swap two elements:** you need a temporary variable, or one value is lost.
- **Reverse** or **shift** an array by swapping or copying elements in the right order.

### Watch out for
Swapping without a temporary variable. Writing `a[0] = a[3]; a[3] = a[0];` makes both positions equal to the old `a[3]`.

### Worked example
""" + code('''
int[] a = {3, 9, 4, 7};
int max = a[0];
for (int i = 1; i < a.length; i++) {
    if (a[i] > max) {
        max = a[i];
    }
}
int temp = a[0];
a[0] = a[a.length - 1];
a[a.length - 1] = temp;
System.out.println(max + " " + a[0] + " " + a[3]);
''', out="9 7 3") + r"""

The maximum is `9`. The swap moves the old last value `7` to the front and the old first value `3` to the end, so `a[0]` is `7` and `a[3]` is `3`. It prints `9 7 3`.
"""),
])
