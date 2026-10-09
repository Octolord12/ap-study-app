P = "ap-csa-u7-mcq-"

PAD = {
    P + "3": ["ArrayLists can only ever be empty, and so no type of value can ever be stored in one", "It's not true; ArrayLists store primitives directly with no conversion, as arrays do", "ArrayLists are only for Strings, so int values cannot be stored in them, though other objects can"],
    P + "4": ["The maximum capacity of the list, before it must grow", "The index of the last element in the list", "Always 0, for any list that has been created"],
    P + "20": ["It's never risky and always works correctly, because ArrayList adjusts the loop index automatically after each removal", "ArrayLists cannot have elements removed during a loop, and it always crashes the program at once", "It only works with ArrayLists of Strings, because other element types cannot be shifted down"],
    P + "23": ["The sum of all of the elements equal to target", "The index of target in list, or -1 if absent", "Whether target is in list at least once"],
    P + "24": ["Nothing; == always works correctly for comparing Integer content, whatever the values, because Java unboxes both", "It always throws a compile error, since the == operator cannot be used with Integer objects at all", "It only works for ArrayLists of Strings, because other object types cannot be compared with =="],
    P + "26": ["Crashes every time it finds a negative number, since removal breaks the loop index and the program stops", "Removes only the first negative number found, then stops", "Removes all elements regardless of sign, leaving an empty list"],
    P + "27": ["It doesn't actually avoid the bug; backward and forward traversal behave identically when elements are removed from the list", "Backward traversal never actually visits every element, so it skips the first one", "ArrayLists cannot be traversed backward, since the index cannot be decremented"],
}

PADC = {
    P + "3": "ArrayLists store objects, so primitives are autoboxed into their wrapper class (e.g. int becomes Integer)",
    P + "20": "Removing an element shifts all later elements down one index, so the loop can skip the element that moved into the removed spot",
    P + "24": "For Integer values outside the cached range, == may compare object references instead of values, giving wrong results",
    P + "26": "Safely removes all negative numbers, because it traverses backward and avoids the index-shifting bug",
    P + "27": "Removing an element only shifts elements AFTER it, so going backward leaves the already-visited indices before it unaffected",
}

PADW = {
    "Whether target is in list at least once": "Whether target is in list at least once (yes or no)",
}
