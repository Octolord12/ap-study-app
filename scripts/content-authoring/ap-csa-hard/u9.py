from common import *

B = bank(9, "unit-9-inheritance")
T_SUP, T_CON, T_OVR, T_POLY = ("superclasses-and-subclasses", "subclass-constructors", "overriding-methods", "polymorphism")
Q = "What is printed as a result of executing the following code segment?"

# 1. constructor chaining order
VEH = '''class Vehicle {
    public Vehicle() {
        System.out.print("V");
    }
    public Vehicle(int w) {
        this();
        System.out.print("V" + w);
    }
}

class Car extends Vehicle {
    public Car() {
        System.out.print("C");
    }
    public Car(int w) {
        super(w);
        System.out.print("C" + w);
    }
}

class Taxi extends Car {
    public Taxi() {
        this(4);
        System.out.print("T");
    }
    public Taxi(int w) {
        System.out.print("T" + w);
    }
}
'''
trace(B, T_CON, Q, body='new Taxi();\nSystem.out.print("|");\nnew Car(2);\nSystem.out.println();', classes=VEH,
      mutants=[("this();\n        System.out.print(\"V\" + w);", "System.out.print(\"V\" + w);", "This leaves out the `V` printed by `this()`. `Vehicle(int)` begins with `this()`, which runs `Vehicle()` before the rest of its own body."),
               ("super(w);\n        System.out.print(\"C\" + w);", "super();\n        System.out.print(\"C\" + w);", "This assumes `Car(int)` runs only the no-argument `Vehicle()` constructor. `super(w)` runs `Vehicle(int)`, which calls `this()` and then prints V2.")],
      manual=[("VCTT4|VV2C2", "This prints T before T4. `Taxi()` first calls `this(4)`, so `Taxi(int)` finishes (printing T4) before `Taxi()` prints its own T.")],
      correct_expl="`new Taxi()` calls `this(4)`, and `Taxi(int)` implicitly calls `super()`: `Car()` calls `Vehicle()`, which prints V; then C; then T4; then `Taxi()` prints T, giving VCT4T. `new Car(2)` calls `super(2)`, i.e. `Vehicle(int)`, which calls `this()` (V) and prints V2; then C2.",
      explanation="A constructor first runs another constructor (`this(...)` or `super(...)`, or an implicit `super()`), and only then its own statements, so output appears from the top of the hierarchy down.")

# 2. super chains and dynamic dispatch inside a superclass method
ABC = '''class A {
    public String f() {
        return "A";
    }
    public String g() {
        return f() + "g";
    }
}

class B extends A {
    public String f() {
        return super.f() + "B";
    }
}

class C extends B {
    public String f() {
        return "C" + super.f();
    }
    public String g() {
        return super.g() + "!";
    }
}
'''
trace(B, T_OVR, Q, body="A x = new C();\nSystem.out.println(x.f() + \" \" + x.g() + \" \" + new B().g());", classes=ABC,
      mutants=[("return \"C\" + super.f();", "return super.f() + \"C\";", "This puts the `C` after the result of `super.f()`. `C.f()` returns `\"C\" + super.f()`, so the `C` comes first."),
               ("return f() + \"g\";", "return \"A\" + \"g\";", "This assumes the call to `f()` inside `A.g()` runs `A`'s own version. The call is made on the actual object, so an overriding `f()` in `B` or `C` runs instead.")],
      manual=[("CAB CABg ABg", "This leaves out the `+ \"!\"` that `C.g()` appends after calling `super.g()`.")],
      correct_expl="`x` refers to a `C`. `x.f()` is `\"C\" + super.f()`, and `B.f()` is `super.f() + \"B\"`, which gives CAB. `x.g()` runs `C.g()`, which calls `A.g()` (B does not override `g`); inside it `f()` is `C`'s version, so it returns CABg, and `!` is added. For a `B`, `A.g()` calls `B.f()`, giving ABg.",
      explanation="`super.method()` runs the superclass version on the same object, and any call to an overridden method made inside it still uses the object's actual class.")

# 3. overloads are chosen at compile time from declared types; overrides at run time
ANI = '''class Animal {
    public String meet(Animal a) {
        return "A-A";
    }
}

class Dog extends Animal {
    public String meet(Animal a) {
        return "D-A";
    }
    public String meet(Dog d) {
        return "D-D";
    }
}
'''
trace(B, T_POLY, Q, body="Animal a = new Dog();\nDog d = new Dog();\nAnimal a2 = new Animal();\nSystem.out.println(a.meet(a2) + \" \" + a.meet(d) + \" \" + d.meet(a) + \" \" + d.meet(d) + \" \" + a2.meet(d));", classes=ANI,
      mutants=[("    public String meet(Animal a) {\n        return \"D-A\";\n    }\n", "", "This ignores `Dog`'s version of `meet(Animal)`. It overrides the one in `Animal`, so it runs whenever the object is a `Dog`.")],
      manual=[("D-A D-D D-A D-D A-A", "`a` is declared as `Animal`, and the compiler can choose only among the methods of `Animal`, which has just `meet(Animal)`. `Dog`'s `meet(Dog)` cannot be reached through an `Animal` variable."),
              ("D-A D-A D-D D-D A-A", "The overloaded method is chosen from the declared type of the argument: `a` is declared `Animal`, so `d.meet(a)` uses `meet(Animal)`, not `meet(Dog)`.")],
      correct_expl="Which overload is used is decided at compile time from the declared types; which version of it runs is decided by the object. `a.meet(a2)` and `a.meet(d)`: only `meet(Animal)` is visible through `Animal`, and the object is a `Dog`, so D-A. `d.meet(a)`: the argument is declared `Animal`, so `meet(Animal)`, D-A. `d.meet(d)`: `meet(Dog)`, D-D. `a2.meet(d)`: A-A.",
      explanation="Overloading is resolved from the declared types at compile time; overriding is resolved from the actual object at run time.")

# 4. overridden method called from a superclass constructor
BASE = '''class Base {
    public Base() {
        setup();
        show();
    }
    public void setup() {
        System.out.print("B-setup ");
    }
    public void show() {
        System.out.print("B-show ");
    }
}

class Derived extends Base {
    private int n = 7;
    public Derived() {
        super();
        System.out.print("D" + n);
    }
    public void setup() {
        n = 3;
        System.out.print("D-setup ");
    }
    public void show() {
        System.out.print("n=" + n + " ");
    }
}
'''
trace(B, T_CON, Q, body="new Derived();\nSystem.out.println();", classes=BASE,
      mutants=[("private int n = 7;", "private int n;", "This assumes the initializer `n = 7` runs before the superclass constructor. It runs after `super()` returns, so it overwrites the 3 and `n` is 7 when `Derived` prints.")],
      manual=[("B-setup B-show D7", "This runs the superclass versions. `setup()` and `show()` are called on the object being constructed, which is a `Derived`, so the overriding versions run even though the calls are in `Base`'s constructor."),
              ("D-setup n=7 D7", "While `Base`'s constructor runs, `Derived`'s field initializer has not run yet, and `setup()` has just set `n` to 3, so `show()` prints n=3."),
              ("D-setup n=0 D7", "`setup()` assigns 3 to `n` before `show()` is called, so `show()` prints n=3. The default value 0 applies only until `setup()` runs.")],
      correct_expl="`new Derived()` runs `Base()` first. It calls `setup()` and `show()` on the new `Derived` object: `setup()` sets `n` to 3 and prints D-setup, and `show()` prints n=3. Only after `super()` returns does `Derived` run its field initializer (`n = 7`), and then its own constructor prints D7.",
      explanation="Field initializers of a subclass run after the superclass constructor finishes, so an overridden method called from the superclass constructor sees the subclass's fields before they are initialized.")

# 5. polymorphic list and toString calling an overridden method
EMP = '''class Employee {
    private String name;
    private double base;
    public Employee(String n, double b) {
        name = n;
        base = b;
    }
    public String getName() {
        return name;
    }
    public double pay() {
        return base;
    }
    public String toString() {
        return name + ":" + pay();
    }
}

class Manager extends Employee {
    private int reports;
    public Manager(String n, double b, int r) {
        super(n, b);
        reports = r;
    }
    public double pay() {
        return super.pay() + 100 * reports;
    }
}

class Intern extends Employee {
    public Intern(String n) {
        super(n, 500);
    }
    public double pay() {
        return super.pay() / 2;
    }
    public String toString() {
        return "Intern " + super.toString();
    }
}
'''
trace(B, T_POLY, Q, body='ArrayList<Employee> staff = new ArrayList<Employee>();\nstaff.add(new Employee("Ann", 1000));\nstaff.add(new Manager("Bo", 2000, 3));\nstaff.add(new Intern("Cy"));\ndouble total = 0;\nfor (Employee e : staff)\n    total += e.pay();\nSystem.out.println(total + " " + staff.get(1) + " " + staff.get(2));', classes=EMP,
      mutants=[("return super.pay() + 100 * reports;", "return 100 * reports;", "This leaves out the base pay: `Manager.pay()` returns `super.pay() + 100 * reports`."),
               ("return \"Intern \" + super.toString();", "return \"Intern \" + getName();", "This assumes the intern's `toString` prints only the name. It calls `super.toString()`, which adds a colon and the pay.")],
      manual=[("3500.0 Bo:2000.0 Intern Cy:500.0", "This uses every employee's base pay (1000 + 2000 + 500). Each element of the list is a different kind of object, and `pay()` runs that object's own version."),
              ("3550.0 Bo:2300.0 Cy:250.0", "This leaves out the word Intern. `Intern` overrides `toString` and puts `Intern ` in front of `super.toString()`.")],
      correct_expl="The pays are Ann 1000.0, Bo 2000 + 3 * 100 = 2300.0 and Cy 500 / 2 = 250.0, so the total is 3550.0. `Employee.toString()` calls `pay()` on the actual object, so Bo prints as Bo:2300.0. `Intern.toString()` adds `Intern ` to the front: Intern Cy:250.0.",
      explanation="Through an `Employee` reference, each call to an overridden method runs the version belonging to the object's actual class, including a call made inside an inherited method such as `toString`.")

# 6. compile-time errors
SH = 'class Shape {\n    public String name() {\n        return "shape";\n    }\n}\n\nclass Circle extends Shape {\n    public double radius() {\n        return 1.0;\n    }\n    public String name() {\n        return "circle";\n    }\n}\n'
cands6 = {
    "bad": "Shape s = new Circle();\ndouble r = s.radius();",
    "a": "Shape s = new Circle();\nString n = s.name();",
    "b": "Circle c = (Circle) new Shape();",
    "c": "Shape[] arr = {new Circle(), new Shape()};",
    "d": "Object o = new Circle();\nString t = o.toString();",
}
for k, v in cands6.items():
    err = compile_error(program(v, classes=SH))
    assert (err is not None) == (k == "bad"), f"{k}: {err}"
try:
    run(program(cands6["b"], classes=SH))
    raise AssertionError("expected ClassCastException")
except RuntimeError as e:
    assert "ClassCastException" in str(e)
B.mcq(T_POLY, "Consider the following classes.\n\n" + code(SH) + "\n\nWhich of the following code segments will cause a compile-time error?",
      ch("`Shape s = new Circle();\ndouble r = s.radius();`".replace("\n", " "), "The compiler checks method calls against the declared type. `s` is declared as `Shape`, which has no `radius()` method, so the call does not compile (a cast to `Circle` would be needed)."),
      [ch("`Shape s = new Circle();\nString n = s.name();`".replace("\n", " "), "This compiles and runs. `name()` is declared in `Shape`, and at run time `Circle`'s version is used."),
       ch("`Circle c = (Circle) new Shape();`", "This compiles, because the cast from a superclass to a subclass is allowed at compile time. It throws a `ClassCastException` at run time, since the object is not a `Circle`, but that is not a compile-time error."),
       ch("`Shape[] arr = {new Circle(), new Shape()};`", "This compiles and runs. A `Circle` is a `Shape`, so it can be stored in an array of `Shape`."),
       ch("`Object o = new Circle();\nString t = o.toString();`".replace("\n", " "), "This compiles and runs. Every class inherits `toString()` from `Object`.")],
      "The compiler only allows calls to methods in the declared type of a variable; a downcast compiles but may fail at run time.")

# 7. casting
ANIM = '''class Animal {
    public String sound() {
        return "...";
    }
}

class Dog extends Animal {
    public String sound() {
        return "Woof";
    }
}

class Puppy extends Dog {
    public String sound() {
        return "Yip";
    }
}
'''
trace(B, T_POLY, Q, body='Animal a = new Animal();\nAnimal b = new Dog();\nString out = "";\ntry {\n    Dog d = (Dog) b;\n    out += "1";\n} catch (ClassCastException e) {\n    out += "x";\n}\ntry {\n    Dog d = (Dog) a;\n    out += "2";\n} catch (ClassCastException e) {\n    out += "y";\n}\ntry {\n    Puppy p = (Puppy) b;\n    out += "3";\n} catch (ClassCastException e) {\n    out += "z";\n}\nout += ((Animal) b).sound();\nSystem.out.println(out);', classes=ANIM,
      mutants=[("Animal b = new Dog();", "Animal b = new Puppy();", "This assumes `b` refers to a `Puppy`. It was created with `new Dog()`, so the cast to `Puppy` fails, and `Dog`'s `sound()` runs at the end.")],
      manual=[("12zWoof", "`a` was created with `new Animal()`, so casting it to `Dog` throws a `ClassCastException` (y); an object can be cast only to its own class or to one of its superclasses."),
              ("1yz...", "Casting to `Animal` does not change the object. `b` still refers to a `Dog`, so `Dog`'s `sound()` runs and returns Woof.")],
      correct_expl="`b` refers to a `Dog`, so `(Dog) b` works (1). `a` refers to an `Animal`, which is not a `Dog`, so the second cast throws (y). A `Dog` is not a `Puppy`, so the third cast throws (z). The final upcast does not change the object, so `Dog.sound()` returns Woof.",
      explanation="A cast succeeds at run time only if the object is an instance of the target type (its own class or a subclass of it).")

# 8. a super call inside a subclass method still dispatches on the actual object
CNT = '''class Counter {
    private int n = 0;
    public void inc() {
        n += step();
    }
    public int step() {
        return 1;
    }
    public int get() {
        return n;
    }
}

class Skipper extends Counter {
    public int step() {
        return 2;
    }
    public void inc() {
        super.inc();
        super.inc();
    }
}
'''
trace(B, T_OVR, Q, body='Counter c = new Skipper();\nc.inc();\nc.inc();\nSystem.out.println(c.get() + " " + c.step());', classes=CNT,
      mutants=[("    public void inc() {\n        super.inc();\n        super.inc();\n    }\n", "", "This ignores `Skipper`'s own `inc()`. The variable's declared type is `Counter`, but the object is a `Skipper`, so `Skipper.inc()` runs and calls `super.inc()` twice.")],
      manual=[("8 1", "The declared type does not decide which method runs. `c` refers to a `Skipper`, so `c.step()` returns 2."),
              ("4 1", "`c.inc()` runs `Skipper`'s `inc()`, which adds twice per call, and `step()` inside it is the `Skipper`'s version (2), so each call adds 4."),
              ("2 2", "Each call to `inc()` runs `super.inc()` twice, and each of those adds `step()`, which is 2 for a `Skipper`. Two calls add 8, not 2.")],
      correct_expl="`c.inc()` runs `Skipper.inc()`, which calls `Counter.inc()` twice. Each of those adds `step()` on the same object, so it is `Skipper`'s `step()`, 2. Each call adds 4, so after two calls `get()` is 8. `c.step()` also returns 2.",
      explanation="`super.inc()` runs the superclass code, but a call to `step()` inside it still uses the version of `step()` belonging to the object's actual class.")

# 9. equals overload vs override
PT = '''class Point {
    private int x;
    private int y;
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
    public boolean equals(Point p) {
        return x == p.x && y == p.y;
    }
}
'''
trace(B, T_OVR, Q, body='Point a = new Point(1, 2);\nPoint b = new Point(1, 2);\nObject o = b;\nSystem.out.println(a.equals(b) + " " + a.equals(o) + " " + o.equals(a) + " " + a.equals((Object) b));', classes=PT,
      mutants=[("public boolean equals(Point p) {\n        return x == p.x && y == p.y;\n    }", "public boolean equals(Object obj) {\n        Point p = (Point) obj;\n        return x == p.x && y == p.y;\n    }", "This treats `equals(Point)` as an override of `equals(Object)`. A method with a different parameter type overloads it; calls whose argument is declared `Object` still use the inherited version.")],
      manual=[("true true false false", "In `a.equals(o)`, `o` is declared as `Object`, so the compiler picks `equals(Object)` (inherited from `Object`), which compares references: false."),
              ("true false true false", "`o.equals(a)` is called through an `Object` variable, which has only `equals(Object)`. That method compares references, and `b` and `a` are different objects: false.")],
      correct_expl="`equals(Point)` overloads, rather than overrides, `Object.equals(Object)`. `a.equals(b)`: the argument is declared `Point`, so `equals(Point)` runs: true. In the other three calls the argument is declared `Object` or the call is made through an `Object` variable, so the inherited `equals(Object)` compares references, and `a` and `b` are different objects: false false false.",
      explanation="To override a method, the name and the parameter types must match exactly; otherwise it is an overload, chosen from the declared types.")

# 10. toString chains through three levels
ITEM = '''class Item {
    private String id;
    public Item(String id) {
        this.id = id;
    }
    public String toString() {
        return "Item(" + id + ")";
    }
}

class Book extends Item {
    private int pages;
    public Book(String id, int pages) {
        super(id);
        this.pages = pages;
    }
    public String toString() {
        return super.toString() + "[" + pages + "]";
    }
}

class Ebook extends Book {
    public Ebook(String id) {
        super(id, 0);
    }
    public String toString() {
        return "E-" + super.toString();
    }
}
'''
trace(B, T_SUP, Q, body='Item[] items = {new Item("a"), new Book("b", 200), new Ebook("c")};\nString s = "";\nfor (Item i : items)\n    s += i + ";";\nSystem.out.println(s);', classes=ITEM,
      mutants=[("return super.toString() + \"[\" + pages + \"]\";", "return \"[\" + pages + \"]\";", "This leaves out `super.toString()` in `Book`. The call adds `Item(...)` in front of the page count, and `Ebook` calls it too."),
               ("return \"E-\" + super.toString();", "return super.toString() + \"-E\";", "This puts the `E-` after the text. `Ebook.toString()` returns `\"E-\" + super.toString()`, so it comes first.")],
      manual=[("Item(a);Item(b)[200];Item(c)[0];", "This ignores the override in `Ebook`, which adds the prefix `E-` in front of the text from `Book`.")],
      correct_expl="Each element is converted with its own class's `toString()`. `Item` gives Item(a). `Book` adds the page count to its superclass's text: Item(b)[200]. `Ebook` adds a prefix to `Book`'s text, which itself includes `Item`'s: E-Item(c)[0].",
      explanation="Each level of a hierarchy can call `super.toString()` to build on the text of the level above.")

# 11. static counter across subclass constructors
PART = '''class Part {
    private static int made = 0;
    private int serial;
    public Part() {
        made++;
        serial = made;
    }
    public int getSerial() {
        return serial;
    }
    public static int getMade() {
        return made;
    }
}

class SubPart extends Part {
    public SubPart() {
        super();
    }
    public SubPart(int k) {
        this();
        for (int i = 0; i < k; i++)
            new Part();
    }
}
'''
trace(B, T_CON, Q, body="Part p = new SubPart(2);\nPart q = new SubPart();\nPart r = new Part();\nSystem.out.println(p.getSerial() + \" \" + q.getSerial() + \" \" + r.getSerial() + \" \" + Part.getMade());", classes=PART,
      mutants=[("i < k", "i <= k", "This creates three extra parts instead of two. The loop runs while `i < k`, which is twice for `k` equal to 2.")],
      manual=[("1 2 3 3", "This leaves out the two extra `Part` objects created inside `SubPart(int)`. Each `new Part()` increments the shared `made`, even though the object is not stored."),
              ("1 2 3 5", "The two extra parts are created before `q`, so they take serial numbers 2 and 3, and `q` is the fourth part.")],
      correct_expl="`new SubPart(2)` calls `this()`, which calls `super()` (`Part()`), so `p` has serial 1; the loop then creates two more `Part` objects (serials 2 and 3). `q` is the fourth part (serial 4) and `r` the fifth (serial 5). `made` is shared by all of them, so it is 5.",
      explanation="Every constructor in the chain runs, and a `static` counter in the superclass is shared by objects of all its subclasses.")

# 12. private access and the legal way to change the field
ACC = 'class Account {\n    private double balance;\n    public Account(double b) {\n        balance = b;\n    }\n    public double getBalance() {\n        return balance;\n    }\n    public void deposit(double amt) {\n        balance += amt;\n    }\n}\n\nclass Savings extends Account {\n    private double rate;\n    public Savings(double b, double r) {\n        super(b);\n        rate = r;\n    }\n    public void addInterest() {\n        /* missing code */\n    }\n}\n'
fills = {
    "A": "balance += balance * rate;",
    "B": "deposit(getBalance() * rate);",
    "C": "super.balance = super.balance * (1 + rate);",
    "D": "setBalance(getBalance() * (1 + rate));",
    "E": "return deposit(getBalance() * rate);",
}
for k, v in fills.items():
    src = ACC.replace("/* missing code */", v)
    err = compile_error(program('Savings s = new Savings(200, 0.05);\ns.addInterest();\nSystem.out.println(s.getBalance());', classes=src))
    assert (err is None) == (k == "B"), f"{k}: {err}"
    if k == "B":
        assert run(program('Savings s = new Savings(200, 0.05);\ns.addInterest();\nSystem.out.println(s.getBalance());', classes=src)) == "210.0"
B.mcq(T_SUP, "Consider the following classes. The `Savings` method `addInterest` is intended to add to the balance an amount equal to the current balance times `rate`.\n\n" + code(ACC) + "\n\nWhich of the following statements, when used to replace `/* missing code */`, will cause `addInterest` to work as intended?",
      ch("`deposit(getBalance() * rate);`", "`getBalance()` and `deposit` are public methods inherited from `Account`, so `Savings` can read and change the balance through them."),
      [ch("`balance += balance * rate;`", "`balance` is `private` in `Account`, so it cannot be accessed by name in the subclass. This causes a compile-time error."),
       ch("`super.balance = super.balance * (1 + rate);`", "Using `super.` does not give access to a `private` field. This causes a compile-time error."),
       ch("`setBalance(getBalance() * (1 + rate));`", "`Account` does not have a `setBalance` method, so this does not compile."),
       ch("`return deposit(getBalance() * rate);`", "`deposit` is a `void` method and `addInterest` is `void`, so a `return` with a value is a compile-time error.")],
      "A subclass inherits public methods but cannot use the superclass's private fields by name; it must go through the superclass's public methods.")

# 13. no-argument constructor missing in the superclass
VB = 'class Vehicle {\n    private int wheels;\n    public Vehicle(int w) {\n        wheels = w;\n    }\n    public int getWheels() {\n        return wheels;\n    }\n}\n\nclass Bike extends Vehicle {\n    public Bike() {\n        /* missing code */\n        System.out.println("bike");\n    }\n}\n'
VB_EMPTY = VB.replace("        /* missing code */\n", "")
assert compile_error(program("new Bike();", classes=VB_EMPTY)) is not None
checks = {
    "A": VB.replace("/* missing code */", "super(2);"),
    "B": VB.replace("/* missing code */", "super();"),
    "C": VB.replace("/* missing code */", "Vehicle(2);"),
    "D": VB_EMPTY.replace('System.out.println("bike");', 'System.out.println("bike");\n        super(2);'),
    "E": VB_EMPTY.replace("private int wheels;", "public int wheels;"),
}
for k, src in checks.items():
    err = compile_error(program("new Bike();", classes=src))
    assert (err is None) == (k == "A"), f"{k}: {err}"
B.mcq(T_CON, "Consider the following classes. The code does not compile as written.\n\n" + code(VB_EMPTY) + "\n\nWhich of the following changes will allow the code to compile?",
      ch("Adding `super(2);` as the first statement of the `Bike` constructor.", "A constructor that does not begin with `this(...)` or `super(...)` implicitly calls `super()`, which fails because `Vehicle` has no no-argument constructor. An explicit `super(2);` as the first statement calls the one `Vehicle` constructor that exists."),
      [ch("Adding `super();` as the first statement of the `Bike` constructor.", "This is exactly what the compiler already inserts. `Vehicle` has no constructor without parameters, so it still does not compile."),
       ch("Adding `Vehicle(2);` as the first statement of the `Bike` constructor.", "A superclass constructor is called with `super(...)`, not by its class name. `Vehicle(2);` is not a valid statement."),
       ch("Adding `super(2);` as the last statement of the `Bike` constructor.", "A call to `super(...)` must be the first statement in a constructor. A call placed later is a compile-time error, and the implicit `super()` is still inserted."),
       ch("Changing `private int wheels;` to `public int wheels;` in `Vehicle`.", "The error is about the missing no-argument constructor, not the access of `wheels`, so changing the access does not help.")],
      "If a subclass constructor does not call `super(...)` explicitly, the compiler inserts `super()`, so the superclass needs a no-argument constructor or the subclass must call one of its other constructors first.")

# 14. polymorphic array with super in a method that is inherited further down
PIECE = '''class Piece {
    public int value() {
        return 1;
    }
    public String label() {
        return "P" + value();
    }
}

class Rook extends Piece {
    public int value() {
        return 5;
    }
}

class Queen extends Rook {
    public int value() {
        return super.value() + 4;
    }
    public String label() {
        return "Q" + super.label();
    }
}
'''
trace(B, T_POLY, Q, body='Piece[] ps = {new Piece(), new Rook(), new Queen()};\nint sum = 0;\nString s = "";\nfor (Piece p : ps) {\n    sum += p.value();\n    s += p.label() + ",";\n}\nSystem.out.println(sum + " " + s);', classes=PIECE,
      mutants=[("return super.value() + 4;", "return 4;", "This leaves out `super.value()`, which is `Rook`'s 5.")],
      manual=[("3 P1,P1,QP1,", "This assumes every call runs `Piece`'s own `value()`. Each call is made on the actual object, so `Rook` and `Queen` use their own versions."),
              ("15 P1,P5,P9,", "This leaves out the `Q` that `Queen`'s `label()` puts in front of the result of `super.label()`.")],
      correct_expl="The values are 1, 5 and `super.value() + 4` = 9, so the sum is 15. `Rook` does not override `label()`, so it uses `Piece`'s, which calls the object's own `value()`: P5. `Queen.label()` is `\"Q\"` plus the inherited `label()` on the same object, whose `value()` is 9: QP9.",
      explanation="An inherited method that calls an overridden method runs the overriding version for each object, and a `super` call walks up only one level at a time.")

# 15. constructor arguments and overridden methods through a three-level chain
MET = '''class Meter {
    private int v;
    public Meter(int v) {
        this.v = v;
    }
    public int get() {
        return v;
    }
    public void bump() {
        v += 10;
    }
}

class Odometer extends Meter {
    public Odometer(int v) {
        super(v * 2);
    }
    public int get() {
        return super.get() + 1;
    }
}

class Trip extends Odometer {
    public Trip(int v) {
        super(v + 1);
    }
    public void bump() {
        super.bump();
        super.bump();
    }
}
'''
trace(B, T_CON, Q, body="Meter m = new Trip(3);\nm.bump();\nSystem.out.println(m.get());", classes=MET,
      mutants=[("super(v * 2);", "super(v);", "This leaves out the doubling in `Odometer`'s constructor. `Trip(3)` passes 4 up, and `Odometer` doubles it to 8 before `Meter` stores it.")],
      manual=[("28", "`m.get()` runs `Odometer`'s `get()`, which `Trip` inherits, and that version adds 1 to the stored value."),
              ("19", "`Trip.bump()` calls `super.bump()` twice, so 20 is added, not 10."),
              ("9", "The stored value is not the constructor argument 3. The value passes through `v + 1` and `v * 2` before it is stored, and `bump()` adds 20.")],
      correct_expl="`new Trip(3)` passes 3 + 1 = 4 to `Odometer`, which passes 4 * 2 = 8 to `Meter`, so the stored value is 8. `Trip.bump()` calls `Meter.bump()` twice (`Odometer` does not override `bump`), adding 20: 28. `get()` is `Odometer`'s version, which returns 28 + 1 = 29.",
      explanation="Trace constructor arguments up the chain, then work out which class's version of each method the object uses.")

# ------------------------------------------------------------------ FRQs
ACCOUNT = '''
class Account {
    private double balance;
    public Account(double initial) { balance = initial; }
    public double getBalance() { return balance; }
    public void deposit(double amt) { balance += amt; }
    public boolean withdraw(double amt) {
        if (amt > balance) {
            return false;
        }
        balance -= amt;
        return true;
    }
}

class CheckingAccount extends Account {
    private double fee;
    private int withdrawals;

    public CheckingAccount(double initial, double fee) {
        super(initial);
        this.fee = fee;
        withdrawals = 0;
    }

    public boolean withdraw(double amt) {
        if (super.withdraw(amt + fee)) {
            withdrawals++;
            return true;
        }
        return false;
    }

    public int getWithdrawals() { return withdrawals; }
}
'''
PROC = '''
    public static int processAll(ArrayList<Account> accounts, double amt) {
        int count = 0;
        for (Account a : accounts) {
            if (a.withdraw(amt)) {
                count++;
            }
        }
        return count;
    }
'''
tb = ('CheckingAccount c = new CheckingAccount(100, 2);\nSystem.out.println(c.withdraw(50) + " " + c.getBalance());\n'
      'System.out.println(c.withdraw(48) + " " + c.getBalance());\nSystem.out.println(c.withdraw(46) + " " + c.getBalance());\nSystem.out.println(c.getWithdrawals());\n'
      'ArrayList<Account> list = new ArrayList<Account>();\nlist.add(new CheckingAccount(100, 2));\nlist.add(new Account(30));\nlist.add(new CheckingAccount(10, 2));\n'
      'System.out.println(processAll(list, 20));\nSystem.out.println(list.get(0).getBalance() + " " + list.get(1).getBalance() + " " + list.get(2).getBalance());')
got = run(program(tb, members=PROC, classes=ACCOUNT))
assert got == "true 48.0\nfalse 48.0\ntrue 0.0\n2\n2\n78.0 10.0 10.0", got
B.frq(T_OVR,
      "The class `Account` models a simple bank account. A checking account charges a fixed fee for each successful withdrawal.\n\n```java\npublic class Account {\n    private double balance;\n\n    public Account(double initial)\n    { /* implementation not shown */ }\n\n    public double getBalance()\n    { /* implementation not shown */ }\n\n    public void deposit(double amt)\n    { /* implementation not shown */ }\n\n    /** Removes amt from the balance and returns true if amt <= balance.\n     *  Otherwise leaves the balance unchanged and returns false. */\n    public boolean withdraw(double amt)\n    { /* implementation not shown */ }\n}\n```\n\n**(a)** Write the complete class `CheckingAccount`, a subclass of `Account`. A `CheckingAccount` has the following behavior.\n\n- The constructor `CheckingAccount(double initial, double fee)` creates an account with the given starting balance that charges `fee` for each successful withdrawal.\n- The method `withdraw(double amt)` is overridden. A withdrawal succeeds only if the account holds at least `amt + fee`; in that case `amt + fee` is removed from the balance and the method returns true. Otherwise the balance is unchanged and the method returns false.\n- The method `getWithdrawals()` returns the number of successful withdrawals made so far.\n\nFor example, for `new CheckingAccount(100, 2)`, `withdraw(50)` returns true and leaves a balance of 48.0; `withdraw(48)` then returns false because 50.0 is needed.\n\n**(b)** Write the method `processAll`, which attempts to withdraw `amt` from every account in `accounts` (some of which are `CheckingAccount` objects) and returns the number of withdrawals that succeeded.\n\n```java\npublic static int processAll(ArrayList<Account> accounts, double amt)\n```",
      [(1, "(a) Class header declares `CheckingAccount extends Account` and has instance variables for the fee and the withdrawal count"),
       (1, "(a) Constructor calls `super(initial)` and initializes the fee (and the count)"),
       (1, "(a) Overrides `withdraw` with the same signature (`public boolean withdraw(double amt)`)"),
       (1, "(a) Decides success using `amt + fee` and removes `amt + fee` from the balance (for example with `super.withdraw(amt + fee)`) without accessing `balance` directly"),
       (1, "(a) Increments the withdrawal count only on a successful withdrawal and returns the correct boolean; `getWithdrawals` returns the count"),
       (1, "(b) Traverses all accounts and calls `withdraw(amt)` on each one (no type tests or casts needed)"),
       (1, "(b) Counts the successful withdrawals and returns the count")],
      "```java\npublic class CheckingAccount extends Account {\n    private double fee;\n    private int withdrawals;\n\n    public CheckingAccount(double initial, double fee) {\n        super(initial);\n        this.fee = fee;\n        withdrawals = 0;\n    }\n\n    public boolean withdraw(double amt) {\n        if (super.withdraw(amt + fee)) {\n            withdrawals++;\n            return true;\n        }\n        return false;\n    }\n\n    public int getWithdrawals() {\n        return withdrawals;\n    }\n}\n\npublic static int processAll(ArrayList<Account> accounts, double amt) {\n    int count = 0;\n    for (Account a : accounts) {\n        if (a.withdraw(amt)) {\n            count++;\n        }\n    }\n    return count;\n}\n```\nThe subclass cannot use `balance` directly because it is `private`; calling `super.withdraw(amt + fee)` reuses the superclass's check and update. In `processAll`, each call to `withdraw` runs the version belonging to the actual object.")

STORE = '''
class Item {
    private String name;
    private double price;
    public Item(String name, double price) {
        this.name = name;
        this.price = price;
    }
    public String getName() { return name; }
    public double getPrice() { return price; }
    public String toString() { return name + ": " + getPrice(); }
}

class Perishable extends Item {
    private int daysLeft;

    public Perishable(String name, double price, int daysLeft) {
        super(name, price);
        this.daysLeft = daysLeft;
    }

    public double getPrice() {
        if (daysLeft <= 2) {
            return super.getPrice() / 2;
        }
        return super.getPrice();
    }

    public String toString() {
        return super.toString() + " (" + daysLeft + " days)";
    }
}
'''
CHEAP = '''
    public static Item cheapest(ArrayList<Item> items) {
        Item best = items.get(0);
        for (Item it : items) {
            if (it.getPrice() < best.getPrice()) {
                best = it;
            }
        }
        return best;
    }
'''
tb2 = ('Perishable m = new Perishable("Milk", 4.0, 2);\nPerishable b = new Perishable("Bread", 3.0, 5);\nItem pen = new Item("Pen", 1.5);\n'
       'System.out.println(m.getPrice() + " " + b.getPrice());\nSystem.out.println(m);\nSystem.out.println(b);\nSystem.out.println(pen);\n'
       'ArrayList<Item> list = new ArrayList<Item>();\nlist.add(m);\nlist.add(b);\nlist.add(pen);\nSystem.out.println(cheapest(list).getName());\n'
       'ArrayList<Item> list2 = new ArrayList<Item>();\nlist2.add(new Item("Tea", 3.0));\nlist2.add(new Perishable("Jam", 6.0, 1));\nlist2.add(new Item("Gum", 3.0));\nSystem.out.println(cheapest(list2).getName());')
got = run(program(tb2, members=CHEAP, classes=STORE))
assert got == "2.0 3.0\nMilk: 2.0 (2 days)\nBread: 3.0 (5 days)\nPen: 1.5\nPen\nTea", got
B.frq(T_SUP,
      "The class `Item` represents a product in a store.\n\n```java\npublic class Item {\n    private String name;\n    private double price;\n\n    public Item(String name, double price)\n    { /* implementation not shown */ }\n\n    public String getName()\n    { /* implementation not shown */ }\n\n    public double getPrice()\n    { return price; }\n\n    /** Returns the name, a colon, a space, and the price, e.g. \"Pen: 1.5\" */\n    public String toString()\n    { return name + \": \" + getPrice(); }\n}\n```\n\n**(a)** Write the complete class `Perishable`, a subclass of `Item`. A `Perishable` item also has a number of days left before it spoils.\n\n- The constructor `Perishable(String name, double price, int daysLeft)` sets the item's name, regular price and days left.\n- The method `getPrice` is overridden: when 2 or fewer days are left, the price is half the regular price; otherwise it is the regular price.\n- The method `toString` is overridden to return the text produced by the `Item` version followed by a space and the number of days left in parentheses, for example `\"Milk: 2.0 (2 days)\"` for an item named Milk with a regular price of 4.0 and 2 days left.\n\n**(b)** Write the method `cheapest`, which returns the `Item` in the list with the lowest value of `getPrice()`. If more than one item has the lowest price, return the one that appears first. Precondition: the list contains at least one item.\n\n```java\npublic static Item cheapest(ArrayList<Item> items)\n```",
      [(1, "(a) Class header declares `Perishable extends Item` and declares an instance variable for the days left"),
       (1, "(a) Constructor calls `super(name, price)` and initializes the days left"),
       (1, "(a) `getPrice` overrides with the same signature and returns half the regular price when `daysLeft <= 2`"),
       (1, "(a) `getPrice` otherwise returns the regular price, obtained with `super.getPrice()` (no direct access to the private field)"),
       (1, "(a) `toString` overrides and uses `super.toString()` followed by the days left in the required format"),
       (1, "(b) Traverses the list and compares prices using `getPrice()` (not a field), so discounts apply"),
       (1, "(b) Keeps track of the item (not just the price) with the lowest price, keeps the first on ties, and returns it")],
      "```java\npublic class Perishable extends Item {\n    private int daysLeft;\n\n    public Perishable(String name, double price, int daysLeft) {\n        super(name, price);\n        this.daysLeft = daysLeft;\n    }\n\n    public double getPrice() {\n        if (daysLeft <= 2) {\n            return super.getPrice() / 2;\n        }\n        return super.getPrice();\n    }\n\n    public String toString() {\n        return super.toString() + \" (\" + daysLeft + \" days)\";\n    }\n}\n\npublic static Item cheapest(ArrayList<Item> items) {\n    Item best = items.get(0);\n    for (Item it : items) {\n        if (it.getPrice() < best.getPrice()) {\n            best = it;\n        }\n    }\n    return best;\n}\n```\n`Item.toString()` calls `getPrice()` on the actual object, so a discounted `Perishable` prints its discounted price. The strict `<` keeps the first item when prices tie.")

B.save()
B.brief()
