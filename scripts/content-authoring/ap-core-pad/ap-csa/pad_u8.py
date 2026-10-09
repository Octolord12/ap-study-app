P = "ap-csa-u8-mcq-"

PAD = {
    P + "11": ["A single for loop that runs once over every element of the array", "A while loop only, with no counters", "A do-while loop only, never a for loop"],
    P + "14": ["No, all rows must always have the exact same length, or the program will not compile", "Only if declared with the keyword \"jagged\" in front of the array type", "Only for arrays of Strings, never for numbers"],
    P + "18": ["The array is never going to be used again after the loop", "The array only has one row and no columns", "It never matters; a fixed number always works fine, whatever the shape"],
    P + "23": ["Whether every element equals target, in every row", "The number of times target appears in the grid", "The position of target in the grid, as a row and column"],
    P + "26": ["grid.length gives the total number of elements in the grid, one sum for each", "It's an arbitrary, unrelated size choice that happens to work", "grid.length gives the number of columns, and we need one sum per column"],
    P + "29": ["It has no particular meaning in the traversal", "It checks whether the grid is empty before it is traversed", "It counts the total number of rows in the grid"],
}

PADC = {
    P + "14": "Yes, Java allows jagged arrays, where each row can have a different length",
}

PADW = {
    "3 columns and 4 rows": "3 columns and 4 rows, in that order",
}
