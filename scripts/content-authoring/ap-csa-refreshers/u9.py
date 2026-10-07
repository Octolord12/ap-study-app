from common import code, finish

ANIMAL_DOG = '''
public class Animal {
    private String name;

    public Animal(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}

public class Dog extends Animal {
    public Dog(String name) {
        super(name);
    }

    public void fetch() {
        System.out.println(getName() + " fetches");
    }
}
'''

CHAIN = '''
public class Animal {
    private String name;

    public Animal(String name) {
        this.name = name;
        System.out.println("Animal " + name);
    }

    public String getName() {
        return name;
    }
}

public class Dog extends Animal {
    private int tricks;

    public Dog(String name, int tricks) {
        super(name);
        this.tricks = tricks;
        System.out.println("Dog " + tricks);
    }
}
'''

OVERRIDE = '''
public class Animal {
    public String speak() {
        return "...";
    }
}

public class Dog extends Animal {
    public String speak() {
        return "Woof";
    }
}

public class Puppy extends Dog {
    public String speak() {
        return super.speak() + "!";
    }
}
'''

POLY = '''
public class Animal {
    public String speak() { return "..."; }
}

public class Dog extends Animal {
    public String speak() { return "Woof"; }
    public void fetch() { }
}

public class Cat extends Animal {
    public String speak() { return "Meow"; }
}
'''

finish(9, [
("superclasses-and-subclasses", r"""
### The idea
Inheritance lets a new class reuse and extend an existing one. The existing class is the **superclass**, and the new one is the **subclass**. It models an "is-a" relationship: a `Dog` is an `Animal`.

### Key facts
- Write `class Dog extends Animal` to make `Dog` a subclass. A class can extend only **one** class directly.
- A subclass inherits the superclass's `public` (and `protected`) methods, so they can be called on a subclass object.
- It does **not** get direct access to the superclass's `private` variables. It must use the superclass's public accessors, such as `getName()`.
- A subclass can add its own variables and methods, and can replace inherited methods (overriding).
- Put shared behavior in the superclass so that it is written once. Every class in Java is ultimately a subclass of `Object`.

### Watch out for
Using inheritance when the relationship is not "is-a". A `Car` has an `Engine` (a variable), but a `Car` is not an `Engine`.

### Worked example
""" + code('''
Dog d = new Dog("Rex");
System.out.println(d.getName());
d.fetch();
''', out="Rex\nRex fetches", classes=ANIMAL_DOG, show_classes=True) + r"""

`Dog` never wrote `getName`, but it inherits it from `Animal`, so `d.getName()` works and prints `Rex`. The `fetch` method calls the inherited `getName()` (it cannot read the private `name` directly) and prints `Rex fetches`.
"""),
("subclass-constructors", r"""
### The idea
When you create a subclass object, the superclass part has to be built too. The subclass constructor makes that happen with `super(...)`.

### Key facts
- `super(arguments)` calls a superclass constructor. It must be the **first statement** in the subclass constructor.
- The superclass part is initialized **first**. Then the rest of the subclass constructor runs.
- If you do not write `super(...)`, Java inserts a call to the superclass's **no-argument** constructor automatically.
- If the superclass has no no-argument constructor, leaving out `super(...)` is a **compile error**.
- Pass along only what the superclass needs, and let the subclass constructor set its own new variables.
- A subclass cannot set the superclass's private variables directly. Go through the superclass constructor or its public methods.

### Watch out for
Forgetting `super(name)` when the superclass requires a `String`. The compiler stops with an error, because there is no `Animal()` to call by default.

### Worked example
""" + code('''
Dog d = new Dog("Rex", 3);
''', out="Animal Rex\nDog 3", classes=CHAIN, show_classes=True) + r"""

`new Dog("Rex", 3)` first runs `super(name)`, which prints `Animal Rex`. Only then does the `Dog` constructor continue and print `Dog 3`. The output is `Animal Rex` followed by `Dog 3`.
"""),
("overriding-methods", r"""
### The idea
A subclass can replace an inherited method with its own version. That is called overriding, and it is how a subclass changes behavior while keeping the same method name.

### Key facts
- To **override**, a subclass method has the **same name, parameter list and return type** as the superclass method.
- When you call it on a subclass object, the subclass version runs.
- `super.methodName()` calls the superclass's version from inside the override, which lets you extend rather than replace it.
- **Overloading** is different: the same name with a **different** parameter list. It is resolved by the arguments, and it is not overriding.
- `@Override` above a method is optional, but it makes the compiler check that you really are overriding. A typo then becomes an error instead of a silent new method.
- An overriding method cannot be less accessible than the one it replaces.

### Watch out for
Changing a parameter by accident. `speak(int n)` does not override `speak()`. It is a separate overloaded method, and the original is still used.

### Worked example
""" + code('''
Animal a = new Animal();
Dog d = new Dog();
Puppy p = new Puppy();
System.out.println(a.speak() + " " + d.speak() + " " + p.speak());
''', out="... Woof Woof!", classes=OVERRIDE, show_classes=True) + r"""

`Animal` gives `...`. `Dog` overrides it to return `Woof`. `Puppy` calls `super.speak()` (which is `Dog`'s `Woof`) and adds `!`. It prints `... Woof Woof!`.
"""),
("polymorphism", r"""
### The idea
Polymorphism means one reference type can stand for many actual kinds of objects, and the right version of a method runs for each. It lets you write code that works on a whole family of classes.

### Key facts
- A superclass variable can refer to a subclass object: `Animal a = new Dog();`.
- The **declared type** (`Animal`) decides which methods the compiler lets you call.
- The **actual object type** (`Dog`) decides which version of an overridden method runs. This is chosen **at run time** (dynamic dispatch).
- So `a.speak()` runs `Dog`'s `speak`, even though `a` was declared as an `Animal`.
- You can keep objects of different subclasses together in one array or `ArrayList` of the superclass type, and treat them all the same way.
- A method that exists only in the subclass cannot be called through the superclass variable. The compiler rejects it.

### Watch out for
Calling a subclass-only method through a superclass variable. `a.fetch()` does not compile if `a` is declared `Animal`, even if the object really is a `Dog`.

### Worked example
""" + code('''
Animal[] zoo = {new Animal(), new Dog(), new Cat()};
for (Animal a : zoo) {
    System.out.println(a.speak());
}
''', out="...\nWoof\nMeow", classes=POLY, show_classes=True) + r"""

The array is typed `Animal[]`, but each slot holds a different kind of object. For each one, Java runs that object's own `speak`, so the loop prints `...`, `Woof` and `Meow`.
"""),
])
