from common import code, finish

finish(3, [
("boolean-expressions", r"""
### The idea
A boolean expression is a question that has a yes-or-no answer. It evaluates to `true` or `false`, and it is what every `if` statement and loop uses to decide what to do.

### Key facts
- The relational operators are `==` (equal), `!=` (not equal), `<`, `>`, `<=` and `>=`.
- The result is a `boolean` value, so it can be stored in a `boolean` variable or printed.
- `=` assigns and `==` compares. Mixing them up is a very common mistake.
- To test whether `x` is even, use `x % 2 == 0`.
- To check that a value is in a range, you need two comparisons joined with `&&`. Writing `1 < x < 10` does not work in Java.
- Using `==` on objects compares references, not contents (see the topic on comparing objects).

### Watch out for
Floating-point comparisons. Because a `double` is an approximation, `0.1 + 0.2 == 0.3` is `false`. Avoid testing two computed decimals for exact equality.

### Worked example
""" + code('''
int x = 7;
System.out.println((x > 5) + " " + (x % 2 == 0) + " " + (x != 7));
''', out="true false false") + r"""

`7 > 5` is true. `7 % 2` is `1`, so `x % 2 == 0` is false. And `x != 7` is false. It prints `true false false`.
"""),
("if-statements", r"""
### The idea
An `if` statement runs a block of code only when its condition is `true`. It lets a program make choices.

### Key facts
- Syntax: `if (condition) { statements }`. The condition must be a `boolean` expression.
- When the condition is `false`, the whole block is skipped and execution continues after it.
- Separate `if` statements are independent. Each one is checked on its own, even if an earlier one was true.
- Without braces, `if` controls **only the next single statement**. Indentation does not matter to Java.
- An `if` can contain another `if`. The inner one is checked only when the outer condition is true.
- Always using braces avoids the next problem.

### Watch out for
A second statement under an unbraced `if`. In the example below, the "Done" line looks like part of the `if`, but it is not, so it runs every time.

### Worked example
""" + code('''
int score = 82;
if (score >= 90) {
    System.out.println("A");
}
if (score >= 80) {
    System.out.println("B");
}
if (score > 100)
    System.out.println("Too high");
    System.out.println("Done");
''', out="B\nDone") + r"""

The first condition is false, so nothing prints. The second is true, so it prints `B`. The third condition is false, so only the single line after it is skipped, and `Done` is printed anyway. The output is `B` then `Done`.
"""),
("if-else-statements", r"""
### The idea
`if-else` chooses between two paths, and `else if` extends that to several. Exactly one path runs.

### Key facts
- In `if (c) { A } else { B }`, block `A` runs when `c` is true, and block `B` runs otherwise. Never both.
- In an `if / else if / else` chain, Java checks the conditions **in order** and runs the first one that is true. The rest are skipped, even if they would also be true.
- A final `else` with no condition catches everything that did not match.
- Because the first match wins, the order of the conditions matters. Put the most specific test (for example, the highest cutoff) first.
- A chain of separate `if` statements is not the same as an `else if` chain. Separate ones can all run.

### Watch out for
Putting a broad condition first. If `score >= 60` were tested before `score >= 90`, a score of `95` would match the first test and never reach the second.

### Worked example
""" + code('''
int score = 85;
String grade;
if (score >= 90) {
    grade = "A";
} else if (score >= 80) {
    grade = "B";
} else if (score >= 70) {
    grade = "C";
} else {
    grade = "F";
}
System.out.println(grade);
''', out="B") + r"""

`85 >= 90` is false, so Java moves on. `85 >= 80` is true, so `grade` becomes `"B"` and the remaining tests are skipped. It prints `B`.
"""),
("compound-boolean-expressions", r"""
### The idea
Logical operators combine boolean expressions into more complex questions. Java also stops evaluating as soon as the answer is decided, which you can use on purpose.

### Key facts
- `!` is NOT, `&&` is AND (true only if **both** sides are true), and `||` is OR (true if **either** side is true).
- Precedence: `!` first, then `&&`, then `||`. Parentheses override it.
- **Short-circuit evaluation:** with `&&`, if the left side is `false`, the right side is never evaluated. With `||`, if the left side is `true`, the right side is skipped.
- That lets you guard a risky test: `d != 0 && 10 / d > 2` never divides by zero.
- **De Morgan's laws:** `!(a && b)` is the same as `!a || !b`, and `!(a || b)` is the same as `!a && !b`. When you negate, flip the operator **and** negate each part.

### Watch out for
Negating only one part. The opposite of `x > 3 && x < 10` is `x <= 3 || x >= 10`, not `x <= 3 && x >= 10`.

### Worked example
""" + code('''
int d = 0;
if (d != 0 && 10 / d > 2) {
    System.out.println("big");
} else {
    System.out.println("safe");
}
int x = 5;
System.out.println(!(x > 3 && x < 10));
System.out.println(x <= 3 || x >= 10);
''', out="safe\nfalse\nfalse") + r"""

`d != 0` is false, so the right side `10 / d` is never evaluated and no error happens. It prints `safe`. For `x = 5`, the two expressions on the last lines are equivalent by De Morgan's law, and both are `false`.
"""),
("comparing-objects", r"""
### The idea
For objects, `==` and `.equals` mean different things. Knowing which to use is one of the most tested ideas in this course.

### Key facts
- `==` on object variables asks "are these the **same object**?" It compares references.
- `.equals(other)` asks "do these have the **same contents**?" For `String`, it compares the characters.
- Two separate objects with identical contents are `equals` but not `==`.
- `==` is the right choice for primitives, and for checking whether a reference is `null` (`obj == null`).
- Always call `equals` on a variable you know is not `null`, or you will get a `NullPointerException`.
- Equivalent boolean expressions give the same result for every input. For example, `!(x == y)` is the same as `x != y`.

### Watch out for
Using `==` to compare strings. It can seem to work for string literals, but it is not reliable. Use `equals`.

### Worked example
""" + code('''
String a = new String("hi");
String b = new String("hi");
System.out.println(a == b);
System.out.println(a.equals(b));
String c = a;
System.out.println(a == c);
''', out="false\ntrue\ntrue") + r"""

`a` and `b` are two different objects that happen to hold the same text, so `a == b` is `false` and `a.equals(b)` is `true`. `c` is an alias for `a`, so `a == c` is `true`. It prints `false`, `true`, `true`.
"""),
])
