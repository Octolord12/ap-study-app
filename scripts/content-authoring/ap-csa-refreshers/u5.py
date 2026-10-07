from common import code, finish

COUNTER = '''
public class Counter {
    private int count;

    public Counter() {
        count = 0;
    }

    public void increment() {
        count++;
    }

    public int getCount() {
        return count;
    }
}
'''

RECT = '''
public class Rectangle {
    private int width;
    private int height;

    public Rectangle(int width, int height) {
        this.width = width;
        this.height = height;
    }

    public Rectangle() {
        width = 1;
        height = 1;
    }

    public int area() {
        return width * height;
    }
}
'''

ACCOUNT = '''
public class BankAccount {
    private double balance;

    public BankAccount(double start) {
        balance = start;
    }

    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }
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

PLAYER = '''
public class Player {
    private static int count = 0;
    private String name;

    public Player(String name) {
        this.name = name;
        count++;
    }

    public static int getCount() {
        return count;
    }
}
'''

PET = '''
public class Pet {
    private String name;

    public Pet(String name) {
        name = name;
    }

    public String getName() {
        return name;
    }
}
'''

finish(5, [
("anatomy-of-a-class", r"""
### The idea
A class bundles data and the actions on that data. Writing one means deciding what each object remembers and what it can do.

### Key facts
- A class has **instance variables** (the data), **constructors** (which set the object up) and **methods** (the behavior).
- Instance variables are normally `private`, and the methods other code should use are `public`. This is **encapsulation**: outside code cannot reach in and change the data directly.
- Every object built from the class has its own copy of each instance variable.
- Methods inside the class can use the instance variables directly, by name.
- A class that holds the data and exposes only the needed methods is easier to change later, because the inside can be rewritten without breaking the code that uses it.

### Watch out for
Making instance variables `public` to save a few lines. It works, but it lets any code change the object into an invalid state.

### Worked example
""" + code('''
Counter c = new Counter();
c.increment();
c.increment();
System.out.println(c.getCount());
''', out="2", classes=COUNTER, show_classes=True) + r"""

The `private int count` is the state. The constructor sets it to `0`. The `increment` method changes it, and `getCount` reads it. After two `increment` calls the program prints `2`.
"""),
("constructors", r"""
### The idea
A constructor runs when an object is created with `new`. Its job is to give the object's instance variables their starting values.

### Key facts
- A constructor has the **same name as the class** and **no return type**, not even `void`.
- It usually takes parameters and uses them to set the instance variables.
- A class can have several constructors with different parameter lists (**overloading**). Java picks the one that matches the call.
- If you write no constructor at all, Java supplies a default one with no parameters that does nothing extra.
- An instance variable that no constructor sets gets a default value: `0` for `int`, `0.0` for `double`, `false` for `boolean`, and `null` for objects.
- If a parameter has the same name as an instance variable, use `this.name = name;` so Java knows which is which.

### Watch out for
Writing a return type by accident. `public void Rectangle()` is an ordinary method that happens to share the class name, not a constructor.

### Worked example
""" + code('''
Rectangle r = new Rectangle(3, 4);
Rectangle unit = new Rectangle();
System.out.println(r.area() + " " + unit.area());
''', out="12 1", classes=RECT, show_classes=True) + r"""

`new Rectangle(3, 4)` uses the two-parameter constructor, so the area is `12`. `new Rectangle()` uses the no-parameter constructor, which sets both sides to `1`, so the area is `1`. It prints `12 1`.
"""),
("accessor-and-mutator-methods", r"""
### The idea
When instance variables are private, other code needs a controlled way to read or change them. Accessors read, and mutators change.

### Key facts
- An **accessor** (getter) returns the value of an instance variable. It is non-void and usually has no parameters: `getBalance()`.
- A **mutator** (setter or modifier) changes an instance variable. It is usually `void` and takes the new value or an amount: `deposit(amount)`.
- Because the change goes through a method, the class can check the value first and refuse a bad one.
- A `toString` method returns a `String` describing the object, and it is used automatically when you print the object.
- An accessor should not change anything. A mutator that returns nothing is called for its effect, not for a value.

### Watch out for
Returning a private object reference from a getter, which lets outside code change the inside. For primitives and `String`, this is not a problem.

### Worked example
""" + code('''
BankAccount acct = new BankAccount(50.0);
acct.deposit(25.5);
acct.deposit(-10);
System.out.println(acct.getBalance());
''', out="75.5", classes=ACCOUNT, show_classes=True) + r"""

The first deposit adds `25.5`, giving `75.5`. The second deposit of `-10` is ignored, because the mutator checks `amount > 0` first. The balance printed is `75.5`.
"""),
("writing-methods", r"""
### The idea
A method is a named, reusable block of code. Writing one means choosing what it takes in, what it gives back, and who may call it.

### Key facts
- A header has an access modifier, a return type (or `void`), a name and a parameter list: `public int area(int w, int h)`.
- A non-void method must `return` a value of the declared type on every path. A void method returns nothing, though `return;` ends it early.
- Execution leaves the method at the first `return` it reaches.
- Java **passes by value**. A primitive parameter is a copy, so changing it inside the method does not change the caller's variable.
- For an object, the parameter is a copy of the **reference**. The method can change the object's contents through it, but making the parameter point to a new object does not affect the caller.
- Several methods can share a name if their parameter lists differ (overloading).

### Watch out for
Expecting a method to change the caller's primitive variable. It cannot, so return the new value and assign it instead.

### Worked example
""" + code('''
int x = 5;
reset(x);
Box box = new Box(3);
grow(box);
replace(box);
System.out.println(x + " " + box.getSize());
''', out="5 4", classes=BOX, members='''
static void reset(int n) { n = 0; }
static void grow(Box b) { b.grow(); }
static void replace(Box b) { b = new Box(100); }
''', show_members=True) + r"""

`reset` changes only its own copy, so `x` is still `5`. `grow` changes the real box, so its size becomes `4`. `replace` only points its own parameter at a new box, so the caller's `box` is untouched. It prints `5 4`.
"""),
("static-variables-and-methods", r"""
### The idea
Most data belongs to each object, but sometimes one value should be shared by the whole class, such as a count of how many objects exist. That is what `static` means.

### Key facts
- A **static variable** belongs to the class, not to any one object. There is exactly one copy, shared by all objects.
- A **static method** also belongs to the class. Call it with the class name: `Player.getCount()`.
- A static method has no object to work on, so it **cannot** use instance variables or `this`.
- An instance method can use static variables.
- Constants are often declared `public static final`, which means one shared value that never changes.
- `Math.abs` and `Math.sqrt` are static methods, so you never create a `Math` object.

### Watch out for
Using an instance variable inside a static method. It does not compile, because the method does not know which object's variable you mean.

### Worked example
""" + code('''
new Player("Ana");
new Player("Ben");
System.out.println(Player.getCount());
''', out="2", classes=PLAYER, show_classes=True) + r"""

Each `new Player(...)` runs the constructor, and every constructor call does `count++` on the **same** shared variable. After two objects, it prints `2`.
"""),
("scope-and-this", r"""
### The idea
Scope is the part of a program where a variable can be used. The keyword `this` refers to the object whose method is running, and it settles name clashes.

### Key facts
- A **local variable** (declared inside a method or block) exists only from its declaration to the end of that block. Method parameters are local too.
- An **instance variable** can be used by every method of the class.
- If a local variable or parameter has the same name as an instance variable, the local one **shadows** it inside that method.
- `this.name` always means the instance variable. `this` by itself means the current object.
- `private` members can be used only inside their own class. `public` ones can be used anywhere.
- A variable declared in a `for` header, or in a loop body, is not available after the loop.

### Watch out for
Shadowing in a constructor. In the example below, `name = name;` assigns the parameter to itself, so the instance variable is never set.

### Worked example
""" + code('''
Pet p = new Pet("Mo");
System.out.println(p.getName());
''', out="null", classes=PET, show_classes=True) + r"""

The constructor's `name = name;` does nothing useful, so the instance variable keeps its default value `null`, and the program prints `null`. The fix is to write `this.name = name;`, which prints `Mo`.
"""),
])
