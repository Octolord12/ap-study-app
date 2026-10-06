P = "ap-csa-u9-mcq-"

PAD = {
    P + "3": ["Only private fields of the superclass, and none of its methods", "Only the constructor of the superclass, with none of its fields", None],
    P + "5": ["Yes, using commas to list multiple superclasses after the extends keyword, as in C++", "Yes, but only up to 3 classes at a time", "Only if all of the classes are in the same package"],
    P + "7": ["No, subclasses can never access superclass fields, even public ones", "Only if Dog redeclares the field itself first", "Only through a getter method, never directly"],
    P + "9": ["A compile error always occurs, since the call is missing", "The object is created without initializing any inherited fields, leaving them undefined", "The subclass cannot be instantiated until super is called"],
    P + "12": ["It's just a stylistic convention, not a real requirement, and the compiler accepts it anywhere in the body", "It has no particular reason; it could be placed anywhere in the constructor body", "It only matters for static methods that are called from constructors"],
    P + "13": ["Nothing; Java provides a working default constructor for Dog automatically, and fills in a String for Animal", "Dog silently ignores Animal's constructor requirement and skips the call to the superclass", "It works fine at compile time but crashes at runtime, when the object is created"],
    P + "14": ["Nothing extra is needed, because Java fills in the String", "Dog must be declared abstract, so it is not instantiated", "Dog must not extend Animal at all, and should copy its fields and methods into its own class instead"],
    P + "15": ["No, a constructor can only do one or the other, not both", "Yes, but only if super() is called last in the constructor", "No, subclasses cannot have their own fields, only the ones that they inherit from the superclass"],
    P + "16": ["The subclass deletes the method from the superclass, so that other subclasses of it no longer have it", "The subclass renames the method so that it has a different name", "The subclass calls the method twice, once for itself and once for the parent"],
    P + "18": ["Only the method name, and nothing else needs to match, even the number of parameters", "Only the return type, and nothing else needs to match, not even the name", "Nothing needs to match; any method in a subclass overrides any method in the superclass, whatever its name"],
    P + "20": ["It's required in every override, or the code will not compile", "It has no effect and is purely decorative, like a comment", "It deletes the superclass's version of the method for all objects"],
    P + "22": ["It makes the method run faster, because the compiler can skip the dynamic lookup at runtime", "It automatically calls the superclass method too, before the override's own body runs", "It changes the method's access level to public, whatever it was before"],
    P + "24": ["The ability of a variable to hold values of different, unrelated primitive types, such as int and boolean", "The ability to have multiple classes with the same name in one package", "The ability to delete methods at runtime, once they are no longer needed"],
    P + "26": ["Java always uses the declared (compile-time) type to decide which method runs, never the type of the object itself", "It's a coincidence and unpredictable, and could print something else on another run", "The declared type is changed automatically when the object is assigned to the variable"],
    P + "27": ["Any method defined anywhere in Dog, including ones that Animal does not declare at all", "Only methods defined directly in Dog, not the inherited ones", "No methods at all, since the object type is unknown"],
    P + "28": ["It has no real benefit, since each subclass would still need its own method written separately", "It makes the array store more elements than it otherwise could, because the type is more general", "It prevents any subclass-specific behavior from ever running, since it treats all as Animals"],
    P + "30": ["Whether two objects have equal field values for every one of their fields", "Whether a variable has been initialized before it is used", "Whether a method has been overridden by a subclass"],
}

PADC = {
    P + "7": "Yes, since name is public (it would also work if it were protected)",
    P + "9": "Java automatically inserts a call to the superclass's no-argument constructor first",
    P + "12": "The superclass part of the object must be fully initialized before the subclass's own initialization code runs",
    P + "13": "It is a compile error, because the automatic super() call needs a no-argument Animal constructor, which doesn't exist",
    P + "14": "Dog must explicitly define a constructor that calls super(someString) with a String argument",
    P + "16": "The subclass provides a new implementation of a method with the same signature as one in the superclass",
    P + "22": "The compiler checks that the method really overrides a superclass method, catching typos (e.g., a misspelled name) at compile time",
    P + "24": "A superclass-typed reference can call an overridden method and the subclass's specific version executes",
    P + "26": "Java uses the actual (runtime) type of the object to decide which overridden method runs: dynamic method dispatch",
    P + "27": "Only methods declared in Animal, though the behavior may come from Dog's overrides",
    P + "28": "One method can work with any subclass of Animal (Dog, Cat, etc.) without knowing the specific subclass in advance",
}

PADW = {}
