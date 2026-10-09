P = "ap-csa-u3-mcq-"

PAD = {
    P + "9": ["All statements indented at the same level as the if, regardless of braces", "All statements until the next blank line in the source file", "All statements until the end of the method, ignoring indentation"],
    P + "17": ["Logical OR -- true if either operand is true, or both", "Logical NOT -- inverts a boolean value from true to false", "Bitwise addition of two integers"],
    P + "22": ["It makes the division happen faster by running the check in parallel", "It guarantees the division will always be evaluated first, before the check", "It has no effect on whether the division is evaluated at all"],
    P + "28": ["Nothing; it correctly prints nothing since name is null and so the test is never true", "It is a compile error because the variable is assigned null", "It always prints \"found\" because null matches any String"],
}

PADC = {
    P + "22": "If x != 0 is false, Java skips the division, avoiding a divide-by-zero error",
    P + "28": "It throws a NullPointerException, since you cannot call .equals() on a null reference",
}

PADW = {
    "Bitwise addition of two integers": "Bitwise addition -- adds the bits of two integers together",
}
