P = "ap-csa-u5-mcq-"

PAD = {
    P + "1": ["Loops and conditionals (control structures)", "Packages and imports (organizational lines)", None],
    P + "2": ["To store an action the object performs when called", "To import other classes into the file", "To define the name of the class itself"],
    P + "3": ["Declare them public so that any code in any class can directly read and modify them", "Declare them as methods instead of fields, so they can be called", "Never initialize them, leaving them to the compiler's defaults"],
    P + "4": ["A local variable inside the constructor", "A parameter only, of the constructor", "A static variable shared by all cars"],
    P + "5": ["Java requires every class to have exactly one constructor, and no more than that", "It's not possible to have multiple constructors in a single class", "To increase the class's file size and make it harder to read"],
    P + "6": ["To destroy an object when it is no longer needed", "To define a class's methods and their return types", "To import other classes into the file"],
    P + "8": ["void, since it returns nothing", "The same type as the class it constructs", "int, to signal success"],
    P + "10": ["The class cannot be instantiated until you write a constructor yourself", "A compile error always occurs for the missing constructor", "All fields become static automatically, shared across objects"],
    P + "11": ["To change a field's value to something new", "To create a new object of the class", "To delete a field from the object"],
    P + "15": ["It makes the code run faster, since the compiler optimizes access through methods", "It is required by the Java compiler, which refuses to compile any class with public fields", "It has no real benefit; it's purely stylistic and changes nothing about how the program behaves"],
    P + "16": ["Only the method name together with its return type", "Only the return type and the access modifier", "The entire method body along with its parameter types"],
    P + "20": ["A loop that runs at least once before it returns", "A parameter of some kind, used in the return", "A static keyword in its header, before the type"],
    P + "21": ["The field belongs to each individual object separately, with its own copy", "The field cannot ever change its value once it is set", "The field is private by default, hidden from other classes"],
    P + "25": ["A static method can access instance (non-static) fields directly, just like an instance method can", "A static method must always return void, never a value", "An instance method cannot take parameters, only static ones can"],
    P + "26": ["The color scheme that the IDE uses to display Java code", "The size of a source file measured in kilobytes", "The speed at which a program runs on a computer"],
    P + "27": ["It is accessible everywhere in the program, in every class", "It is accessible in every class, once the method has run", "It becomes a field automatically when the method ends"],
    P + "28": ["It isn't needed; it's just decorative and could be removed without changing what the constructor does", "It converts name to a String before assigning it", "It creates a new Dog object each time the constructor runs"],
}

PADC = {
    P + "5": "To let objects be created in different ways, with different initial values",
    P + "10": "Java automatically provides a no-argument default constructor",
    P + "15": "It lets the class control how fields are read and modified, e.g., validating a new value in a setter",
    P + "16": "The method's name and its parameter types, not the return type",
    P + "20": "A return statement that provides a value of the declared type",
    P + "27": "It is accessible only within that method (or block where it's declared)",
}

PADW = {}
