from common import code, finish

finish(7, [
("arraylist-intro", r"""
### The idea
An `ArrayList` is a list that can grow and shrink as you add and remove items. It solves the main limitation of an array, whose size is fixed.

### Key facts
- Create one with the element type in angle brackets: `ArrayList<String> names = new ArrayList<String>();`. Put `import java.util.ArrayList;` at the top of the file.
- It holds **objects** only. For numbers, use the wrapper types, as in `ArrayList<Integer>`, and Java converts automatically (autoboxing).
- `size()` returns how many elements it holds. An array uses `length` and a `String` uses `length()`. An `ArrayList` uses `size()`.
- Elements are indexed from `0`, like an array.
- A new list is empty. Printing a list shows its elements in square brackets, such as `[Ada, Linus]`.
- You cannot use `[]` on an `ArrayList`. Use methods such as `get`.

### Watch out for
Mixing up the three ways to get a size: `a.length` for an array, `s.length()` for a `String`, and `list.size()` for an `ArrayList`.

### Worked example
""" + code('''
ArrayList<String> names = new ArrayList<String>();
names.add("Ada");
names.add("Linus");
System.out.println(names.size() + " " + names);
''', out="2 [Ada, Linus]") + r"""

The list starts empty, and each `add` puts a new element at the end. It prints `2 [Ada, Linus]`.
"""),
("arraylist-methods", r"""
### The idea
Five `ArrayList` methods do almost everything. The tricky part is how adding and removing shift the other elements.

### Key facts
- `add(obj)` adds to the end. `add(index, obj)` inserts at `index` and shifts later elements one place toward the end.
- `get(index)` returns the element at that position without changing the list.
- `set(index, obj)` replaces the element and **returns the old one**.
- `remove(index)` deletes the element and **returns it**. Later elements shift one place toward the front, so the list gets shorter.
- `size()` gives the current number of elements.
- A bad index (negative, or `size()` or more) throws an `IndexOutOfBoundsException`. The one exception is `add(index, obj)`, which also allows `index` equal to `size()`, and that adds at the end.

### Watch out for
Forgetting that indexes change after an add or remove. The element that was at index `2` may be at index `1` once something earlier is removed.

### Worked example
""" + code('''
ArrayList<String> list = new ArrayList<String>();
list.add("A");
list.add("B");
list.add("C");
list.add(1, "X");
System.out.println(list);
String removed = list.remove(0);
String old = list.set(2, "Z");
System.out.println(removed + " " + old + " " + list);
''', out="[A, X, B, C]\nA C [X, B, Z]") + r"""

After the three adds the list is `[A, B, C]`, and inserting `"X"` at index `1` gives `[A, X, B, C]`. Then `remove(0)` returns `"A"` and leaves `[X, B, C]`. Next, `set(2, "Z")` returns the old `"C"` and leaves `[X, B, Z]`. The second line prints `A C [X, B, Z]`.
"""),
("traversing-arraylists", r"""
### The idea
You can traverse an `ArrayList` like an array, with an index loop or an enhanced `for`. The danger is changing the list while you are walking through it.

### Key facts
- Index loop: `for (int i = 0; i < list.size(); i++)` with `list.get(i)`.
- Enhanced loop: `for (String s : list)`. It is read-only in practice: **do not add or remove** inside it, or Java throws a `ConcurrentModificationException`.
- Removing while looping **forward** is a classic bug. After `remove(i)`, the next element slides into position `i`, and then `i++` skips over it.
- Fix 1: loop **backward**, from `list.size() - 1` down to `0`. Removing an element only shifts the ones you have already visited.
- Fix 2: loop forward but do `i--` after each removal, so you look at the same index again.
- `list.size()` is re-evaluated each pass, so it changes as you remove.

### Watch out for
Removing every element that matches in a forward loop. Two matches in a row means the second is skipped.

### Worked example
""" + code('''
ArrayList<Integer> nums = new ArrayList<Integer>();
nums.add(2);
nums.add(4);
nums.add(5);
nums.add(6);
for (int i = 0; i < nums.size(); i++) {
    if (nums.get(i) % 2 == 0) {
        nums.remove(i);
    }
}
System.out.println(nums);
''', out="[4, 5]") + r"""

The goal was to remove the even numbers, but the result is `[4, 5]`. When `2` is removed at index `0`, the `4` slides into index `0`, and `i` moves on to `1`, so the `4` is never tested. Going backward fixes it:

""" + code('''
ArrayList<Integer> nums = new ArrayList<Integer>();
nums.add(2);
nums.add(4);
nums.add(5);
nums.add(6);
for (int i = nums.size() - 1; i >= 0; i--) {
    if (nums.get(i) % 2 == 0) {
        nums.remove(i);
    }
}
System.out.println(nums);
''', out="[5]") + r"""

Now every even number is removed, and the output is `[5]`.
"""),
("arraylist-algorithms", r"""
### The idea
The array algorithms you already know (totals, counts, searches) work on an `ArrayList` too, using `get` and `size`. The new parts are removing and inserting while keeping the list in order.

### Key facts
- Replace `a[i]` with `list.get(i)`, and `a.length` with `list.size()`.
- **Count or total:** loop over the list and update a counter or running sum.
- **Remove all items that match:** loop **backward** and call `remove(i)`, so no element is skipped.
- **Insert in order:** find the first element that should come after the new one, then use `add(index, obj)`.
- **Compare objects with `.equals`**, not `==`. This matters for `String` and for the `Integer` objects in an `ArrayList<Integer>`, because `==` on two `Integer` objects compares references.
- To do something to every element, an enhanced `for` is fine as long as you do not change the list's size.

### Watch out for
Comparing two `Integer` objects from a list with `==`. It can give the wrong answer for larger values. Use `equals`, or unbox one side first.

### Worked example
""" + code('''
ArrayList<Integer> data = new ArrayList<Integer>();
data.add(-3);
data.add(8);
data.add(-1);
data.add(8);
data.add(5);
int count = 0;
for (int n : data) {
    if (n == 8) {
        count++;
    }
}
for (int i = data.size() - 1; i >= 0; i--) {
    if (data.get(i) < 0) {
        data.remove(i);
    }
}
System.out.println(count + " " + data);
''', out="2 [8, 8, 5]") + r"""

The first loop counts the `8`s (here `n` is a plain `int`, so `==` is safe) and finds `2`. The backward loop removes the negatives `-1` and `-3`, leaving `[8, 8, 5]`. It prints `2 [8, 8, 5]`.
"""),
])
