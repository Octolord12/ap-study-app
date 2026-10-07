from common import code, finish

finish(10, [
("recursion-basics", r"""
### The idea
A recursive method solves a problem by calling itself on a smaller version of the same problem. It stops when the problem is small enough to answer directly.

### Key facts
- Every recursive method needs a **base case**: a condition where it returns an answer without calling itself.
- Every other path makes a **recursive call** with an argument that moves **toward** the base case.
- Each call has its own copy of the parameters and local variables. The calls wait on a **call stack**, and they finish in the opposite order from how they started.
- If there is no base case, or the argument never reaches it, the calls never stop, and Java throws a `StackOverflowError`.
- To trace one, write out each call and its returned value, then substitute back up from the base case.
- A recursive solution can always be written with a loop. Recursion is often shorter for problems that split into smaller copies of themselves.

### Watch out for
A recursive call that does not change the argument, such as `factorial(n)` instead of `factorial(n - 1)`. It never reaches the base case.

### Worked example
""" + code('''
System.out.println(factorial(4));
''', out="24", members='''
static int factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}
''', show_members=True) + r"""

The base case is `n <= 1`. The calls go `factorial(4)`, then `4 * factorial(3)`, then `3 * factorial(2)`, then `2 * factorial(1)`, and `factorial(1)` is `1`. Working back up: `2 * 1 = 2`, then `3 * 2 = 6`, then `4 * 6 = 24`. It prints `24`.
"""),
("recursive-searching-sorting", r"""
### The idea
Searching and sorting are where recursion pays off most, because both can be solved by repeatedly cutting the problem in half.

### Key facts
- **Linear search** checks each element in turn. It works on any array, but it may need to look at all `n` elements.
- **Binary search** works only on a **sorted** array. Compare the target with the middle element, then discard the half that cannot contain it, and repeat. It takes about `log2(n)` steps, so it is much faster for large arrays.
- Recursive binary search has two base cases: the range is empty (return `-1`), or the middle element is the target (return its index).
- **Merge sort** splits an array in half, recursively sorts each half, then **merges** the two sorted halves into one sorted array. The base case is an array of `0` or `1` elements, which is already sorted.
- Merge sort is faster than selection or insertion sort on large arrays, but it needs extra space for the merging.

### Watch out for
Using binary search on an unsorted array. The comparison with the middle tells you nothing about which half to keep, so the answer can be wrong.

### Worked example
""" + code('''
int[] a = {2, 5, 8, 12, 16, 23, 38};
System.out.println(search(a, 23, 0, a.length - 1) + " " + search(a, 7, 0, a.length - 1));
''', out="5 -1", members='''
static int search(int[] a, int target, int lo, int hi) {
    if (lo > hi) {
        return -1;
    }
    int mid = (lo + hi) / 2;
    if (a[mid] == target) {
        return mid;
    } else if (a[mid] < target) {
        return search(a, target, mid + 1, hi);
    } else {
        return search(a, target, lo, mid - 1);
    }
}
''', show_members=True) + r"""

For `23`: the middle of indexes `0` to `6` is index `3` (value `12`), which is too small, so search `4` to `6`. The middle is index `5`, which holds `23`, so it returns `5`. For `7`, the range keeps shrinking until `lo` is greater than `hi`, and it returns `-1`. The output is `5 -1`.
"""),
])
