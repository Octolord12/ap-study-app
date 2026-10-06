P = "ap-csa-u2-mcq-"

PAD = {
    P + "3": ["Only the object's methods, not its data, which each object stores elsewhere", "Only the object's data, not its methods, which are defined separately", None],
    P + "5": ["They automatically share the same field values, since both come from one class", "Changing dog1's fields always changes dog2's fields too, because they share memory", None],
    P + "6": ["Making all fields and methods public so that any other class can read or use them directly without restriction", "Compiling code faster by skipping the steps that are not needed", "Removing all comments from code to make the program shorter"],
    P + "8": ["Declares a variable's type before any value is assigned to it", "Deletes an existing object and frees its memory for reuse", "Converts a primitive to an object so that it can be passed around"],
    P + "16": ["Void methods can't take parameters, while non-void methods can take as many as the programmer chooses", "Non-void methods can only be called once in a program, while void methods can be called repeatedly", "There is no difference; the terms are interchangeable in Java, and the compiler treats them identically"],
    P + "18": ["x is assigned 0, the default value for an int", "x is assigned null, since no value was returned", "The program compiles but crashes at runtime, when the call to the void method finishes"],
    P + "19": ["Adds their lengths together as a number (an int)", "Compares them for equality and returns a boolean", "Causes a compile error, since + only works on numbers"],
    P + "25": ["It replaces the int primitive type entirely, so int is no longer used", "It only exists for backward compatibility and is never used in modern programs", "It makes arithmetic faster than it would be with plain primitives"],
}

PADC = {
    P + "6": "Hiding implementation details behind a simpler interface, like calling a method without knowing how it works inside",
    P + "16": "A void method performs an action but returns no value; a non-void method returns a value you can use",
}

PADW = {}
