from common import *

B = bank(5, "unit-5-writing-classes")
T_ANA, T_CON, T_ACC, T_WM, T_STAT, T_SCOPE = ("anatomy-of-a-class", "constructors", "accessor-and-mutator-methods", "writing-methods", "static-variables-and-methods", "scope-and-this")
Q = "What is printed as a result of executing the following code segment?"

ITEM = 'class Item {\n    private static int count = 0;\n    private int id;\n    public Item() {\n        count++;\n        id = count;\n    }\n    public int getId() { return id; }\n    public static int getCount() { return count; }\n}\n'
trace(B, T_STAT, Q, body="Item a = new Item();\nItem b = new Item();\nItem c = new Item();\nSystem.out.println(a.getId() + \" \" + b.getId() + \" \" + c.getId() + \" \" + Item.getCount());",
      classes=ITEM,
      mutants=[("id = count;", "id = count * 10;", "This multiplies the id by 10. In the code `id` is set directly to the current value of the shared counter.")],
      manual=[("3 3 3 3", "This assumes `id` is shared by all objects. `id` is an instance variable, so each object keeps the value of `count` at the time it was created."),
              ("1 1 1 3", "This assumes each object starts counting from 0. `count` is `static`, so it is shared and keeps increasing across all the objects.")],
      correct_expl="`count` is shared by all `Item` objects, so it becomes 1, 2 and 3 as the objects are created. Each constructor copies the current `count` into that object's own `id`: 1, 2, 3. The final count is 3.",
      explanation="A `static` variable belongs to the class and is shared; an instance variable belongs to each object.")

TALLY = 'class Tally {\n    private static int total = 0;\n    private int local = 0;\n    public void add(int n) {\n        local += n;\n        total += n;\n    }\n    public int getLocal() { return local; }\n    public static int getTotal() { return total; }\n}\n'
trace(B, T_STAT, Q, body="Tally a = new Tally();\nTally b = new Tally();\na.add(5);\nb.add(3);\na.add(2);\nSystem.out.println(a.getLocal() + \" \" + b.getLocal() + \" \" + Tally.getTotal());",
      classes=TALLY,
      manual=[("7 3 7", "This ignores the amounts added through `b`. `total` is shared, so every `add` on any `Tally` contributes to it: 5 + 3 + 2 = 10."),
              ("10 10 10", "This assumes every variable is shared. `local` is an instance variable, so `a` and `b` each keep their own sum."),
              ("7 3 3", "This assumes the shared variable holds only the most recent addition. `total += n` accumulates.")],
      correct_expl="`a.local` gets 5 and 2 (total 7); `b.local` gets 3. The shared `total` accumulates every call: 5 + 3 + 2 = 10.",
      explanation="Instance variables are separate for each object; a `static` variable is a single value shared by the class.")

# 3. this and shadowing
src3 = program(body="Box b = new Box(5);\nSystem.out.println(b.getWidth());", classes='class Box {\n    private int width;\n    public Box(int width) {\n        width = width;\n    }\n    public int getWidth() { return width; }\n}\n')
assert run(src3) == "0"
B.mcq(T_SCOPE, "Consider the following class.\n\n" + code("public class Box {\n    private int width;\n\n    public Box(int width) {\n        width = width;\n    }\n\n    public int getWidth() {\n        return width;\n    }\n}") + "\n\nWhat is the value returned by `getWidth()` for the object created with `new Box(5)`?",
      ch("0", "Inside the constructor, the parameter `width` hides the instance variable `width`, so `width = width;` assigns the parameter to itself. The instance variable keeps its default value, 0. The fix is `this.width = width;`."),
      [ch("5", "This would be correct if the constructor used `this.width = width;`. Without `this`, both sides of the assignment refer to the parameter."),
       ch("The class does not compile.", "The statement `width = width;` is legal (a self-assignment of the parameter), so the class compiles."),
       ch("A `NullPointerException` is thrown.", "`width` is an `int`, which is never `null`; the field simply keeps its default value 0.")],
      "A parameter or local variable with the same name as an instance variable hides it. Use `this.` to refer to the field.")

# 4. local variable hiding a field
GAUGE = 'class Gauge {\n    private int level = 10;\n    public int read(int x) {\n        int level = x * 2;\n        level += 1;\n        return level;\n    }\n    public int getLevel() { return level; }\n}\n'
trace(B, T_SCOPE, Q, body="Gauge g = new Gauge();\nSystem.out.println(g.read(7) + \" \" + g.getLevel());",
      classes=GAUGE,
      mutants=[("int level = x * 2;\n        level += 1;", "level = x * 2;\n        level += 1;", "This assumes `read` changes the instance variable. The declaration `int level` creates a local variable that hides the field, so the field is never modified.")],
      manual=[("14 10", "This leaves out the `level += 1` update. The method returns the local variable, which is 14 + 1 = 15."),
              ("10 10", "This returns the field's value from `read`. The local `level` hides the field, so `read` returns the local value, 15.")],
      correct_expl="Inside `read`, the local variable `level` is 7 * 2 = 14, then 15, and that is returned. The instance variable `level` is untouched, so `getLevel()` returns 10.",
      explanation="A local variable declared with the same name as a field hides the field inside that method; changes to it do not affect the field.")

PERSON = 'class Person {\n    private String name;\n    private int age;\n    public Person() {\n        this("Unknown");\n    }\n    public Person(String name) {\n        this(name, 18);\n    }\n    public Person(String name, int age) {\n        this.name = name;\n        this.age = age;\n    }\n    public String toString() { return name + ":" + age; }\n}\n'
trace(B, T_CON, Q, body="Person p = new Person();\nPerson q = new Person(\"Zed\");\nPerson r = new Person(\"Amy\", 30);\nSystem.out.println(p + \"|\" + q + \"|\" + r);",
      classes=PERSON,
      manual=[("Unknown:0|Zed:0|Amy:30", "This assumes the one- and no-argument constructors leave `age` unset. Each of them calls another constructor with `this(...)`, which supplies 18."),
              ("null:0|Zed:18|Amy:30", "This assumes the no-argument constructor does nothing. It calls `this(\"Unknown\")`, which in turn calls `this(name, 18)`."),
              ("Unknown:18|Zed:18|Amy:18", "This assumes the age is always 18. The three-argument constructor stores the age it receives, 30 for Amy.")],
      correct_expl="`new Person()` calls `this(\"Unknown\")`, which calls `this(name, 18)`, giving Unknown:18. `new Person(\"Zed\")` gives Zed:18. `new Person(\"Amy\", 30)` gives Amy:30. `toString` is called implicitly in the concatenation.",
      explanation="`this(...)` calls another constructor of the same class; the chain ends in the constructor that assigns the fields.")

CALC = 'class Calc {\n    public int add(int a, int b) { return a + b; }\n    public double add(double a, double b) { return a + b + 0.5; }\n}\n'
trace(B, T_WM, Q, body="Calc c = new Calc();\nSystem.out.println(c.add(2, 3) + \" \" + c.add(2, 3.5) + \" \" + c.add(2.0, 3) + \" \" + c.add('a', 1));",
      classes=CALC,
      manual=[("5 5.5 5.0 98", "This ignores the `+ 0.5` in the `double` version. `c.add(2, 3.5)` and `c.add(2.0, 3)` both use `add(double, double)`, which returns the sum plus 0.5."),
              ("5 6.0 5.5 a1", "This treats `'a'` as text. A `char` argument is widened to `int` and `add(int, int)` is used: 97 + 1 = 98."),
              ("5 6.0 6.0 98", "In `c.add(2.0, 3)`, the sum is 2.0 + 3.0 + 0.5 = 5.5, not 6.0.")],
      correct_expl="`add(2, 3)` matches the `int` version: 5. `add(2, 3.5)` and `add(2.0, 3)` have a `double` argument, so the `double` version runs: 2 + 3.5 + 0.5 = 6.0 and 2.0 + 3 + 0.5 = 5.5. A `char` widens to `int`: 97 + 1 = 98.",
      explanation="Overload resolution looks at the argument types: an exact `int` match is preferred, and a `char` widens to `int`.")

# 7. exposing a private array
SCORES = 'class Scores {\n    private int[] data = {10, 20, 30};\n    public int[] getData() { return data; }\n    public int first() { return data[0]; }\n    public int copyFirst() {\n        int[] copy = data.clone();\n        copy[0] = -1;\n        return data[0];\n    }\n}\n'
trace(B, T_ACC, Q, body="Scores s = new Scores();\nint[] d = s.getData();\nd[0] = 99;\nSystem.out.println(s.first() + \" \" + s.copyFirst());",
      classes=SCORES,
      manual=[("10 10", "This assumes `getData` returns a copy. It returns the reference to the object's own array, so `d[0] = 99` changes the private data."),
              ("99 -1", "This assumes `clone()` shares the array. `clone` makes a separate copy, so `copy[0] = -1` does not change `data`."),
              ("10 -1", "Both mistakes: `getData` returns the actual array (so the 99 is stored), and the clone is independent of it.")],
      correct_expl="`getData()` returns a reference to the private array itself, so `d[0] = 99` changes the object's data: `first()` is 99. In `copyFirst`, `clone()` creates an independent copy, so setting `copy[0]` does not change `data`, and `data[0]` is still 99.",
      explanation="Returning a reference to a private mutable object lets callers change it. A defensive copy protects the data.")

# 8. toString
POINT = 'class Point {\n    private int x, y;\n    public Point(int x, int y) { this.x = x; this.y = y; }\n    public String toString() { return "(" + x + "," + y + ")"; }\n}\n'
trace(B, T_ANA, Q, body="Point p = new Point(3, -4);\nPoint q = null;\nString s = \"P=\" + p + \" Q=\" + q;\nSystem.out.println(s);\nSystem.out.println(p);",
      classes=POINT,
      manual=[("A `NullPointerException` is thrown.", "Concatenating a `null` reference with a string does not throw: it appends the text \"null\". An exception would occur only if a method were called on `q`."),
              ("P=(3,-4) Q=null", "This leaves out the second line. `System.out.println(p)` also calls `p.toString()` and prints `(3,-4)`."),
              ("P=(3,-4) Q=(null)\n(3,-4)", "A `null` reference is converted to the text `null`, with no parentheses; `toString` is not called on `null`.")],
      correct_expl="In `\"P=\" + p`, `p.toString()` is called implicitly, giving (3,-4). A `null` reference is converted to the text \"null\". `println(p)` also uses `toString`.",
      explanation="Concatenation and `println` call `toString()` on objects automatically, and print `null` for a null reference.")

# 9. static context
src9 = program(classes='class T {\n    private int n = 3;\n    public static int get() { return n; }\n}\n')
assert "non-static variable n cannot be referenced from a static context" in compile_error(src9)
B.mcq(T_STAT, "Consider the following class.\n\n" + code("public class T {\n    private int n = 3;\n\n    public static int get() {\n        return n;\n    }\n}") + "\n\nWhich of the following best describes the result of compiling this class?",
      ch("It does not compile, because a `static` method cannot refer to an instance variable.", "A `static` method belongs to the class and runs without any particular object, so it has no `n` to refer to. The compiler reports that a non-static variable cannot be referenced from a static context."),
      [ch("It compiles, and `T.get()` returns 3.", "There is no object whose `n` could be returned; the compiler rejects the code."),
       ch("It compiles, and `T.get()` returns 0.", "The method does not compile, so it can't return anything."),
       ch("It does not compile, because `n` is `private` and cannot be accessed within the class.", "A `private` member is accessible anywhere inside its own class. The problem is the `static` context.")],
      "Instance variables belong to objects; a `static` method has no object to read them from.")

# 10. final
src10 = program(classes='class T {\n    private final int x;\n    public T(int x) { this.x = x; }\n    public void bump() { x++; }\n}\n')
assert "cannot assign a value to final variable x" in compile_error(src10)
B.mcq(T_ANA, "Consider the following class.\n\n" + code("public class T {\n    private final int x;\n\n    public T(int x) {\n        this.x = x;\n    }\n\n    public void bump() {\n        x++;\n    }\n}") + "\n\nWhich of the following best describes the result of compiling this class?",
      ch("It does not compile, because the `final` variable `x` is modified in `bump`.", "A `final` instance variable can be assigned only once, in its declaration or in a constructor. `x++` assigns it again, which is a compile-time error."),
      [ch("It compiles, but `bump` throws an exception when it is called.", "The error is detected at compile time, not at run time."),
       ch("It compiles, and `bump` increments `x`.", "`final` means that the variable cannot be reassigned after it has been given a value."),
       ch("It does not compile, because the constructor assigns `x`.", "Assigning a `final` instance variable in the constructor is allowed; it is the standard way to initialize it.")],
      "A `final` instance variable may be assigned only when the object is constructed.")

# 11. primitive versus object parameters
trace(B, T_WM, Q, body="int a = 3, b = 8;\nswap(a, b);\nPair p = new Pair(3, 8);\nswap(p);\nSystem.out.println(a + \" \" + b + \" \" + p.getFirst() + \" \" + p.getSecond());",
      members='    public static void swap(int x, int y) { int t = x; x = y; y = t; }\n    public static void swap(Pair p) { int t = p.getFirst(); p.set(p.getSecond(), t); }\n',
      classes='class Pair {\n    private int first, second;\n    public Pair(int f, int s) { first = f; second = s; }\n    public int getFirst() { return first; }\n    public int getSecond() { return second; }\n    public void set(int f, int s) { first = f; second = s; }\n}\n',
      manual=[("8 3 8 3", "This assumes the `int` version swaps the caller's variables. Parameters are copies of the values, so `swap(a, b)` leaves `a` and `b` unchanged."),
              ("3 8 3 8", "This assumes the `Pair` version has no effect. `swap(Pair)` calls `set` on the object the caller passed, which changes the object itself."),
              ("8 3 3 8", "This reverses the effects. The `int` swap changes only local copies, and the `Pair` swap changes the object.")],
      correct_expl="`swap(int, int)` swaps only its own parameter copies, so `a` and `b` stay 3 and 8. `swap(Pair)` changes the fields of the shared object through its reference, so the pair becomes (8, 3).",
      explanation="Primitive arguments are copied; object arguments are references, so a method can change the object they refer to.")

# 12. a buggy comparison method
DATE = 'class Date {\n    private int month, day;\n    public Date(int m, int d) { month = m; day = d; }\n    public boolean isBefore(Date other) {\n        return month < other.month || day < other.day;\n    }\n}\n'
trace(B, T_WM, Q, body="Date a = new Date(3, 15);\nDate b = new Date(5, 10);\nSystem.out.println(a.isBefore(b) + \" \" + b.isBefore(a));",
      classes=DATE,
      mutants=[("return month < other.month || day < other.day;", "return month < other.month || (month == other.month && day < other.day);", "This is what a correct `isBefore` would print. The code compares the days even when the months differ, so it is wrong: `b.isBefore(a)` is true because 10 < 15.")],
      manual=[("false true", "March 15 is before May 10, and the `month < other.month` test is true for `a.isBefore(b)`, so that call is true."),
              ("false false", "Both calls are true: `a.isBefore(b)` because 3 < 5, and `b.isBefore(a)` because the second test, `day < other.day`, compares 10 < 15.")],
      correct_expl="`a.isBefore(b)`: 3 < 5 is true. `b.isBefore(a)`: 5 < 3 is false, but `day < other.day` is 10 < 15, which is true, so the result is true. The method wrongly reports each date as before the other.",
      explanation="A date comparison must compare the days only when the months are equal.")

# 13. no default constructor
src13 = program(body="Foo f = new Foo();", classes='class Foo {\n    private int v;\n    public Foo(int v) { this.v = v; }\n}\n')
assert "constructor Foo in class Foo cannot be applied to given types" in compile_error(src13)
B.mcq(T_CON, "Consider the following class and statement.\n\n" + code("public class Foo {\n    private int v;\n\n    public Foo(int v) {\n        this.v = v;\n    }\n}") + "\n\n" + code("Foo f = new Foo();") + "\n\nWhich of the following best describes the result of the statement?",
      ch("It does not compile, because the class has no constructor with no parameters.", "Java supplies a default no-argument constructor only when a class declares no constructors at all. `Foo` declares one with a parameter, so `new Foo()` has no matching constructor."),
      [ch("It compiles, and `v` is set to 0.", "There is no default constructor to run, since the class has declared its own constructor."),
       ch("It compiles, and `v` is set to `null`.", "`v` is an `int`, and the code does not compile in any case."),
       ch("It compiles but throws an exception at run time.", "The problem is detected at compile time.")],
      "The default constructor exists only when no constructor is written.")

# 14. default values
trace(B, T_ANA, Q, body="Defaults d = new Defaults();\nSystem.out.println(d.a + \" \" + d.b + \" \" + d.c + \" \" + d.d + \" \" + d.e);",
      classes='class Defaults {\n    int a;\n    double b;\n    boolean c;\n    String d;\n    int[] e;\n}\n',
      manual=[("0 0 false null null", "A `double` instance variable is initialized to 0.0, which is printed with its decimal point."),
              ("0 0.0 false  null", "An uninitialized `String` is `null`, not an empty string, so the output contains the text \"null\"."),
              ("0 0.0 true null null", "A `boolean` instance variable defaults to `false`.")],
      correct_expl="Instance variables get default values: 0 for `int`, 0.0 for `double`, `false` for `boolean`, and `null` for every reference type (`String`, arrays).",
      explanation="Unlike local variables, instance variables are given default values when an object is created.")

# 15. methods that return this
trace(B, T_WM, Q, body="Counter c = new Counter();\nint r = c.inc().inc().add(5).get();\nCounter d = c.inc();\nSystem.out.println(r + \" \" + c.get() + \" \" + (c == d));",
      classes='class Counter {\n    private int n = 0;\n    public Counter inc() { n++; return this; }\n    public Counter add(int k) { n += k; return this; }\n    public int get() { return n; }\n}\n',
      manual=[("7 8 false", "`inc` returns `this`, the same object, so `d` and `c` are references to one object and `c == d` is true."),
              ("7 7 true", "`d = c.inc()` increments `c` too (it returns the same object), so `c.get()` is 8."),
              ("1 1 false", "Each method modifies and returns the same object, so the calls accumulate: 1 + 1 + 5 = 7.")],
      correct_expl="Every call changes the same object and returns it, so the chain gives 0 + 1 + 1 + 5 = 7, which is stored in `r`. Then `c.inc()` makes the count 8 and returns `this`, so `d` is the same object as `c`.",
      explanation="A method that returns `this` allows chaining; all the calls act on the same object.")

# ------------------------------------------------------------------ FRQs
account = '''
public class Account {
    private static int accountCount = 0;
    private String owner;
    private double balance;

    public Account(String owner, double initialDeposit) {
        this.owner = owner;
        if (initialDeposit > 0) {
            balance = initialDeposit;
        } else {
            balance = 0;
        }
        accountCount++;
    }

    public String getOwner() { return owner; }

    public double getBalance() { return balance; }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }

    public boolean withdraw(double amount) {
        if (amount <= 0 || amount > balance) {
            return false;
        }
        balance -= amount;
        return true;
    }

    public static int getAccountCount() { return accountCount; }
}
'''
verify("", [('new Account("Ann", 100).getBalance()', 100.0), ('new Account("Bo", -5).getBalance()', 0.0), ('Account.getAccountCount()', 2)],
       classes=account.replace("public class Account", "class Account"))
tbody = 'Account a = new Account("Ann", 100);\na.deposit(50);\na.deposit(-20);\nboolean w1 = a.withdraw(30);\nboolean w2 = a.withdraw(500);\nboolean w3 = a.withdraw(0);\nSystem.out.println(a.getBalance() + " " + w1 + " " + w2 + " " + w3 + " " + a.getOwner() + " " + Account.getAccountCount());'
assert run(program(tbody, classes=account.replace("public class Account", "class Account"))) == "120.0 true false false Ann 1"
B.frq(T_ANA,
      "Write a complete class named `Account` that models a simple bank account. The class must have the following behavior.\n\n- A private `String` instance variable for the owner's name and a private `double` instance variable for the balance.\n- A constructor `Account(String owner, double initialDeposit)` that sets the owner and sets the balance to `initialDeposit`, or to 0 if `initialDeposit` is not positive.\n- Accessor methods `getOwner` and `getBalance`.\n- A method `deposit(double amount)` that adds `amount` to the balance. If `amount` is not positive, the balance is unchanged.\n- A method `boolean withdraw(double amount)` that, if `amount` is positive and not greater than the balance, subtracts it from the balance and returns `true`. Otherwise the balance is unchanged and the method returns `false`.\n- A `static` method `getAccountCount` that returns the total number of `Account` objects that have been created.\n\nThe following code segment shows an example of the class in use.\n\n```java\nAccount a = new Account(\"Ann\", 100);\na.deposit(50);\na.deposit(-20);                      // ignored\nboolean w1 = a.withdraw(30);         // true; balance is now 120.0\nboolean w2 = a.withdraw(500);        // false; balance is unchanged\nboolean w3 = a.withdraw(0);          // false; balance is unchanged\nSystem.out.println(a.getBalance() + \" \" + Account.getAccountCount());   // 120.0 1\n```",
      [(1, "Declares the class with private instance variables for the owner and the balance, and a `static` counter"),
       (1, "Constructor assigns the owner and sets the balance correctly (0 if the deposit is not positive)"),
       (1, "Constructor increments the static counter"),
       (1, "Provides correct accessor methods `getOwner` and `getBalance`"),
       (1, "`deposit` adds only positive amounts"),
       (1, "`withdraw` tests that the amount is positive and not greater than the balance"),
       (1, "`withdraw` subtracts and returns `true` on success; returns `false` with no change otherwise"),
       (1, "`getAccountCount` is declared `static` and returns the counter")],
      "```java\npublic class Account {\n    private static int accountCount = 0;\n    private String owner;\n    private double balance;\n\n    public Account(String owner, double initialDeposit) {\n        this.owner = owner;\n        if (initialDeposit > 0) {\n            balance = initialDeposit;\n        } else {\n            balance = 0;\n        }\n        accountCount++;\n    }\n\n    public String getOwner() { return owner; }\n\n    public double getBalance() { return balance; }\n\n    public void deposit(double amount) {\n        if (amount > 0) {\n            balance += amount;\n        }\n    }\n\n    public boolean withdraw(double amount) {\n        if (amount <= 0 || amount > balance) {\n            return false;\n        }\n        balance -= amount;\n        return true;\n    }\n\n    public static int getAccountCount() { return accountCount; }\n}\n```\nThe counter is `static` so that it is shared by every `Account`; the constructor increments it once for each object created.")

fraction = '''
class Fraction {
    private int num;
    private int den;

    public Fraction(int numerator, int denominator) {
        int g = gcd(Math.abs(numerator), Math.abs(denominator));
        if (g == 0) {
            g = 1;
        }
        num = numerator / g;
        den = denominator / g;
        if (den < 0) {
            num = -num;
            den = -den;
        }
    }

    private static int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    public Fraction add(Fraction other) {
        return new Fraction(num * other.den + other.num * den, den * other.den);
    }

    public String toString() {
        if (den == 1) {
            return "" + num;
        }
        return num + "/" + den;
    }
}
'''
verify("", [("new Fraction(2, 4)", "1/2"), ("new Fraction(6, 3)", "2"), ("new Fraction(1, -2)", "-1/2"), ("new Fraction(-3, -6)", "1/2"), ("new Fraction(0, 5)", "0"),
            ("new Fraction(1, 2).add(new Fraction(1, 3))", "5/6"), ("new Fraction(1, 2).add(new Fraction(1, 2))", "1"), ("new Fraction(3, 4).add(new Fraction(-1, 4))", "1/2")], classes=fraction)
B.frq(T_CON,
      "Write a complete class named `Fraction` that represents a rational number. The class must have the following behavior.\n\n- Private `int` instance variables for the numerator and the denominator.\n- A constructor `Fraction(int numerator, int denominator)`, where the denominator is not 0. The fraction is stored in lowest terms, and if it is negative the negative sign is stored in the numerator (so the denominator is always positive). For example, `new Fraction(2, 4)` is stored as 1/2, `new Fraction(1, -2)` is stored as -1/2 and `new Fraction(-3, -6)` is stored as 1/2. You may write a helper method to find the greatest common divisor of two nonnegative integers.\n- A method `Fraction add(Fraction other)` that returns a new `Fraction`, in lowest terms, that is the sum of this fraction and `other`. Neither fraction is changed. For example, 1/2 plus 1/3 is 5/6.\n- A method `toString` that returns the fraction as a `String` in the form `numerator/denominator`, except that when the denominator is 1 it returns only the numerator. For example, the `String` for 6/3 is `\"2\"`, and for 1/-2 it is `\"-1/2\"`.",
      [(1, "Declares a class with private numerator and denominator variables"),
       (1, "Constructor reduces the fraction using a correct greatest-common-divisor computation"),
       (1, "Constructor stores the sign in the numerator so that the denominator is positive"),
       (1, "`add` uses a common denominator (or cross multiplication) to compute the sum"),
       (1, "`add` returns a new reduced `Fraction` and does not modify either operand"),
       (1, "`toString` returns \"numerator/denominator\", or only the numerator when the denominator is 1")],
      "```java\npublic class Fraction {\n    private int num;\n    private int den;\n\n    public Fraction(int numerator, int denominator) {\n        int g = gcd(Math.abs(numerator), Math.abs(denominator));\n        if (g == 0) {\n            g = 1;\n        }\n        num = numerator / g;\n        den = denominator / g;\n        if (den < 0) {\n            num = -num;\n            den = -den;\n        }\n    }\n\n    private static int gcd(int a, int b) {\n        while (b != 0) {\n            int t = a % b;\n            a = b;\n            b = t;\n        }\n        return a;\n    }\n\n    public Fraction add(Fraction other) {\n        return new Fraction(num * other.den + other.num * den, den * other.den);\n    }\n\n    public String toString() {\n        if (den == 1) {\n            return \"\" + num;\n        }\n        return num + \"/\" + den;\n    }\n}\n```\nThe constructor does all of the reducing, so `add` can build the unreduced sum $\\frac{a}{b}+\\frac{c}{d}=\\frac{ad+cb}{bd}$ and pass it to the constructor.")

B.save()
B.brief()
