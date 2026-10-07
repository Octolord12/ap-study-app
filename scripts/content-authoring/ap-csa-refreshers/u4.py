from common import code, finish

finish(4, [
("while-loops", r"""
### The idea
A `while` loop repeats a block of code as long as its condition stays `true`. Use it when you do not know in advance how many repetitions you need.

### Key facts
- Syntax: `while (condition) { statements }`.
- The condition is checked **before every pass**, including the first. If it is false at the start, the body never runs.
- Something inside the loop must eventually make the condition false, or the loop never ends (an **infinite loop**).
- A typical loop has three parts: set up the control variable before the loop, test it in the condition, and change it inside the body.
- A loop can stop early with `return`, and it may be written to stop when it sees a special **sentinel** value.

### Watch out for
Forgetting the update. If `i++` is missing from the loop below, `i` stays `1`, the condition `i <= 5` is always true, and the program never finishes.

### Worked example
""" + code('''
int i = 1;
int sum = 0;
while (i <= 5) {
    sum += i;
    i++;
}
System.out.println(sum);
''', out="15") + r"""

The loop adds `1`, `2`, `3`, `4` and `5` to `sum`. After `i` becomes `6`, the condition `6 <= 5` is false, so the loop ends. It prints `15`.
"""),
("for-loops", r"""
### The idea
A `for` loop packs the setup, the test and the update of a counting loop into one line. Use it when you know how many times to repeat, or when you are counting through a range.

### Key facts
- Syntax: `for (initialization; condition; update) { statements }`.
- The initialization runs once. Then, before each pass, the condition is checked. After each pass, the update runs.
- `for (int i = 0; i < n; i++)` runs exactly `n` times, with `i` taking the values `0` through `n - 1`.
- `for (int i = 1; i <= n; i++)` also runs `n` times, but with `i` from `1` through `n`.
- A step other than one, or counting down, is just a different update: `i += 2` or `i--`.
- A variable declared in the `for` header exists only inside the loop.
- A `for` loop can always be rewritten as a `while` loop, and the reverse.

### Watch out for
Off-by-one errors. Using `<=` where you meant `<` makes the loop run one time too many, which with an array causes an `ArrayIndexOutOfBoundsException`.

### Worked example
""" + code('''
for (int i = 0; i < 5; i++) {
    System.out.print(i + " ");
}
System.out.println();
for (int i = 10; i > 0; i -= 3) {
    System.out.print(i + " ");
}
''', out="0 1 2 3 4 \n10 7 4 1") + r"""

The first loop prints `0 1 2 3 4`. The second starts at `10` and subtracts `3` each time: `10 7 4 1`. After `1` the update gives `-2`, which fails `i > 0`. A loop like `for (int i = 2; i <= 10; i += 2)` runs `5` times (`2, 4, 6, 8, 10`).
"""),
("nested-iteration", r"""
### The idea
A nested loop is a loop inside another loop. The inner loop runs completely, from start to finish, once for every pass of the outer loop.

### Key facts
- If the outer loop runs `n` times and the inner loop runs `m` times each time, the inner body runs `n * m` times in total.
- The inner loop's variable starts over each time the outer loop starts a new pass.
- When the inner loop's limit depends on the outer variable, the counts add up differently. For example, an inner loop that runs `row` times gives `1 + 2 + 3 + ...`.
- Nested loops are how you build grids, tables and patterns, and how you compare every pair of elements.
- Use different variable names for the two loops, and be careful about which one controls the line break.

### Watch out for
Putting `System.out.println()` in the wrong loop. In the pattern below, it belongs in the **outer** loop, after the inner loop finishes, so each row ends with a new line.

### Worked example
""" + code('''
for (int row = 1; row <= 3; row++) {
    for (int col = 1; col <= row; col++) {
        System.out.print("*");
    }
    System.out.println();
}
''', out="*\n**\n***") + r"""

On row `1` the inner loop runs once, on row `2` twice and on row `3` three times. It prints:

```
*
**
***
```
"""),
("informal-code-analysis", r"""
### The idea
You can often work out what a loop does, or how many times a statement runs, without running it. The skill is to trace the values carefully, or to count passes using a pattern.

### Key facts
- **Trace with a table.** Write a column for each variable and a row for each pass, and update it exactly as the code would.
- `for (int i = 0; i < n; i++)` runs `n` times. `for (int i = 1; i <= n; i++)` also runs `n` times. `for (int i = 0; i <= n; i++)` runs `n + 1` times.
- For a loop with a step of `k`, the count is roughly the range divided by `k`, rounded up. Check by listing the values.
- In nested loops, multiply the counts when the limits are fixed. When the inner limit depends on the outer variable, add up the inner counts for each outer value.
- Check the first and last pass by hand, because that is where off-by-one mistakes hide.

### Watch out for
Counting from the wrong start. A loop whose variable starts at `1` and tests `i < 4` runs `3` times (`1, 2, 3`), not `4`.

### Worked example
How many times does `count++` run?

""" + code('''
int count = 0;
for (int i = 0; i < 4; i++) {
    for (int j = 0; j < i; j++) {
        count++;
    }
}
System.out.println(count);
''', out="6") + r"""

Make a table of the inner loop's passes. When `i` is `0`, the inner loop runs `0` times. When `i` is `1`, it runs `1` time. When `i` is `2`, `2` times, and when `i` is `3`, `3` times. The total is `0 + 1 + 2 + 3 = 6`, and the program prints `6`.
"""),
])
