from common import code, finish

DOG = '''
public class Dog {
    private String name;
    private int age;

    public Dog(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() { return name; }
    public int getAge() { return age; }
    public void birthday() { age++; }
}
'''

BOX = '''
public class Box {
    private int size;

    public Box(int size) { this.size = size; }
    public void grow() { size++; }
    public int getSize() { return size; }
}
'''

finish(2, [
("object-oriented-programming", r"""
### The idea
A **class** is a blueprint that describes what a kind of thing knows and can do. An **object** is one actual thing built from that blueprint. Object-oriented programming organizes a program as objects that work together.

### Key facts
- A class defines **attributes** (the data an object keeps, called instance variables) and **behaviors** (the actions it can perform, called methods).
- Many objects can be built from one class. Each object keeps its **own** copy of the instance variables, so changing one object does not change another.
- You use an object by calling its methods with dot notation: `object.method()`.
- The public methods of a class are how other code is allowed to use it. The details inside can change without breaking the code that uses it.
- A variable of a class type holds a reference to an object, not the object itself.

### Watch out for
Treating the class and the object as the same thing. `Dog` is the blueprint. `new Dog("Rex", 3)` makes one particular dog.

### Worked example
Suppose a `Dog` class stores a name and an age, with a constructor that sets both.

""" + code('''
Dog a = new Dog("Rex", 3);
Dog b = new Dog("Fido", 5);
System.out.println(a.getName() + " is " + a.getAge());
System.out.println(b.getName() + " is " + b.getAge());
''', out="Rex is 3\nFido is 5", classes=DOG) + r"""

This prints `Rex is 3` and `Fido is 5`. Two objects from the same class, each with its own data.
"""),
("creating-and-storing-objects", r"""
### The idea
You create an object with `new`, which runs a constructor, and you keep track of it with a reference variable. Understanding what the variable really holds explains most of the surprises with objects.

### Key facts
- `ClassName variable = new ClassName(arguments);` creates the object and stores a **reference** to it.
- The arguments must match a constructor's parameters in number, order and type.
- Assigning one object variable to another copies the **reference**, not the object. Both variables then point to the same object (an alias).
- The special value `null` means "refers to no object". Calling a method on `null` throws a `NullPointerException`.
- An uninitialized object variable that is a field defaults to `null`.

### Watch out for
Thinking `second = first` makes a copy. It does not. Changing the object through `second` is visible through `first`, because it is one object.

### Worked example
""" + code('''
Box first = new Box(3);
Box second = first;
second.grow();
System.out.println(first.getSize());
Box third = new Box(10);
third.grow();
System.out.println(first.getSize() + " " + third.getSize());
''', out="4\n4 11", classes=BOX) + r"""

`second` is an alias for `first`, so growing it makes `first.getSize()` print `4`. `third` is a separate object, so it ends at `11` and does not disturb the others. The second line prints `4 11`.

If a variable is `null`, a call like `box.grow()` fails at run time with a `NullPointerException`.
"""),
("calling-methods", r"""
### The idea
Calling a method asks an object (or a class) to do something. Some methods only do something, and some also give back a value.

### Key facts
- A **void** method performs an action and returns nothing. You call it as a statement on its own.
- A **non-void** method returns a value, and you should use that value: store it, print it, or use it in an expression.
- The values you pass in are **arguments**. They must match the method's parameters in number, order and type.
- Call a method on an object with `object.method(arguments)`. Call a static method on its class with `ClassName.method(arguments)`, as in `Math.abs(-7)`.
- Methods with the same name but different parameter lists are **overloaded**. Java picks the one that matches the call.

### Watch out for
Trying to use the result of a void method. `int x = d.birthday();` does not compile if `birthday` is void, because there is no value to store.

### Worked example
""" + code('''
Dog d = new Dog("Rex", 3);
d.birthday();
int age = d.getAge();
System.out.println(age);
System.out.println(Math.abs(age - 10));
''', out="4\n6", classes=DOG) + r"""

`d.birthday()` is void, so it stands alone as a statement. `d.getAge()` returns `4`, which is stored in `age`. `Math.abs(age - 10)` is `Math.abs(-6)`, which is `6`. It prints `4` and `6`.
"""),
("string-objects", r"""
### The idea
A `String` is an object that holds a sequence of characters. Strings are used constantly, so a few of their methods are worth knowing exactly.

### Key facts
- A `String` is **immutable**: its methods never change it. They return a new `String`, and you must store or use that result.
- `length()` returns the number of characters.
- `substring(a, b)` returns the characters from index `a` up to but **not including** `b`. `substring(a)` goes to the end. Indexes start at `0`.
- `indexOf(str)` returns the index of the first match, or `-1` if there is none.
- `equals(other)` tests whether the contents are the same. `compareTo(other)` returns a negative number, zero or a positive number depending on alphabetical order.
- With `+`, evaluation goes left to right. Once one operand is a `String`, the rest are joined as text. Use `\n` for a new line and `\"` for a quotation mark.

### Watch out for
Calling `word.substring(1);` and expecting `word` to change. The new string is thrown away unless you assign it, as in `word = word.substring(1);`.

### Worked example
""" + code('''
String s = "computer";
System.out.println(s.length());
System.out.println(s.substring(0, 3));
System.out.println(s.substring(3));
System.out.println(s.indexOf("put"));
System.out.println(s.indexOf("z"));
System.out.println(1 + 2 + "a" + 1 + 2);
''', out="8\ncom\nputer\n3\n-1\n3a12") + r"""

This prints `8`, `com`, `puter`, `3`, `-1` and `3a12`. In the last line, `1 + 2` is added as numbers first to give `3`, and then everything after the `"a"` is joined as text. Now immutability:

""" + code('''
String word = "hello";
word.substring(1);
System.out.println(word);
word = word.substring(1);
System.out.println(word);
''', out="hello\nello") + r"""

The first line prints `hello`, because the result of `substring` was discarded. After the assignment it prints `ello`.
"""),
("wrapper-classes-and-math", r"""
### The idea
Wrapper classes let a primitive value be treated as an object, which matters because collections like `ArrayList` can only hold objects. The `Math` class bundles common calculations as static methods.

### Key facts
- `Integer` wraps an `int`, and `Double` wraps a `double`.
- **Autoboxing** converts a primitive to its wrapper automatically (`Integer boxed = 42;`). **Unboxing** converts back (`int plain = boxed;`).
- `Integer.MAX_VALUE` and `Integer.MIN_VALUE` are the largest and smallest `int` values.
- `Math.abs(x)` gives the absolute value. `Math.pow(base, exponent)` and `Math.sqrt(x)` return a `double`.
- `Math.random()` returns a `double` from `0.0` up to but **not including** `1.0`.
- To get a random whole number from `low` to `high` inclusive, use `(int) (Math.random() * (high - low + 1)) + low`.

### Watch out for
Forgetting that `Math.pow` and `Math.sqrt` return `double`. `Math.pow(2, 3)` is `8.0`, not `8`, so it will not fit in an `int` without a cast.

### Worked example
""" + code('''
Integer boxed = 42;
int plain = boxed;
System.out.println(Math.pow(2, 3));
System.out.println(Math.sqrt(16));
System.out.println(Math.abs(-7));
System.out.println(Integer.MAX_VALUE);
System.out.println(plain + 1);
''', out="8.0\n4.0\n7\n2147483647\n43") + r"""

This prints `8.0`, `4.0`, `7`, `2147483647` and `43`. A die roll from `1` to `6`:

""" + code('''
int roll = (int) (Math.random() * 6) + 1;
''') + r"""

`Math.random() * 6` is at least `0.0` and below `6.0`. Truncating gives `0` through `5`, and adding `1` gives `1` through `6`.
"""),
])
