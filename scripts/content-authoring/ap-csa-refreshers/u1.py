from common import code, finish

finish(1, [
("variables-and-data-types", r"""
### The idea
A variable is a named place to keep a value. Java makes you declare its type once, and the type decides what the variable can hold and what you can do with it.

### Key facts
- The three primitive types in this course are `int` (whole numbers), `double` (decimal numbers) and `boolean` (`true` or `false`).
- `String` is not a primitive. It is a class, so a `String` variable holds a reference to an object.
- Declare and set a variable in one line: `int count = 5;`. A name must start with a letter or underscore, and it is case-sensitive.
- A type never changes. `int x = 3.5;` does not compile, because a `double` will not fit in an `int`.
- An `int` holds values from `Integer.MIN_VALUE` to `Integer.MAX_VALUE`, about plus or minus 2.1 billion. Going past either end wraps around (overflow) rather than causing an error.
- A `double` stores an approximation, so some decimals are not exact.

### Watch out for
Mixing up `5`, `5.0` and `"5"`. They are an `int`, a `double` and a `String`, and Java treats them as three different things.

### Worked example
""" + code('''
int wholeNumber = 7;
double price = 19.99;
boolean isOpen = true;
String name = "Ada";
System.out.println(wholeNumber + " " + price + " " + isOpen + " " + name);
''', out="7 19.99 true Ada") + r"""

This prints `7 19.99 true Ada`. Overflow and rounding are real, too:

""" + code('''
int big = Integer.MAX_VALUE;
big = big + 1;
System.out.println(big);
System.out.println(0.1 + 0.2);
''', out="-2147483648\n0.30000000000000004") + r"""

The first line prints `-2147483648` (wrapped to the other end), and the second prints `0.30000000000000004`.
"""),
("expressions-and-assignment", r"""
### The idea
An expression combines values and operators into a single value. An assignment statement works out the right-hand side first and then stores the result in the variable on the left.

### Key facts
- The arithmetic operators are `+`, `-`, `*`, `/` and `%` (remainder).
- Multiplication, division and remainder happen before addition and subtraction. Operators of the same level go left to right. Parentheses override all of this.
- If both operands are `int`, the result is an `int`, so `/` throws away the fractional part. `17 / 5` is `3`, not `3.4`.
- If either operand is a `double`, the result is a `double`.
- `%` gives the remainder: `17 % 5` is `2`. It is the standard way to test divisibility or to wrap a count around.
- In `x = x + 1`, the right side uses the old value of `x`, and then the result is stored back.

### Watch out for
Integer division inside a bigger expression. In `1 / 2 * 4.0` the division happens first, on two `int` values, giving `0`, so the whole thing is `0.0`.

### Worked example
""" + code('''
int a = 17;
int b = 5;
System.out.println(a / b);
System.out.println(a % b);
System.out.println(a / 5.0);
System.out.println(2 + 3 * 4);
System.out.println((2 + 3) * 4);
''', out="3\n2\n3.4\n14\n20") + r"""

This prints `3`, `2`, `3.4`, `14` and `20`. Only the third line uses a `double` operand, so it is the only one with a decimal.
"""),
("compound-assignment-and-casting", r"""
### The idea
Compound assignment operators are shortcuts for updating a variable, and a cast tells Java to convert a value from one type to another on purpose.

### Key facts
- `x += 5` means `x = x + 5`. The same pattern works for `-=`, `*=`, `/=` and `%=`.
- `x++` adds 1 and `x--` subtracts 1.
- `(double) n` converts an `int` to a `double`. `(int) d` converts a `double` to an `int` by **truncating**: it drops the decimal part, it does not round. `(int) 3.9` is `3`, and `(int) -3.9` is `-3`.
- A cast applies to the value right after it, before other operators. So `(double) a / b` converts `a` first and then divides, as `double` division.
- To round a positive `double` to the nearest `int`, use `(int) (x + 0.5)`. For a negative one, use `(int) (x - 0.5)`.

### Watch out for
Casting too late. `(double) (a / b)` divides two `int` values first, and only then converts the already-truncated result.

### Worked example
""" + code('''
int total = 10;
total += 5;
total *= 2;
total++;
double avg = (double) total / 4;
int rounded = (int) (avg + 0.5);
System.out.println(total + " " + avg + " " + rounded);
''', out="31 7.75 8") + r"""

`total` goes `10`, `15`, `30`, `31`. Then `avg` is `31 / 4.0 = 7.75`, and rounding gives `(int) 8.25`, which is `8`. It prints `31 7.75 8`. The timing of a cast matters:

""" + code('''
int a = 7;
int b = 2;
System.out.println((double) a / b);
System.out.println((double) (a / b));
''', out="3.5\n3.0") + r"""

The first prints `3.5`. The second prints `3.0`, because `7 / 2` was already `3` before the cast.
"""),
])
