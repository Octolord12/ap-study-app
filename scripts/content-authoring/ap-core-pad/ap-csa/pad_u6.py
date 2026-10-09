P = "ap-csa-u6-mcq-"

PAD = {
    P + "6": ["It returns 0, the default value of an int", "It returns the last valid element in the array", "It automatically resizes the array to fit"],
    P + "13": ["Nothing, it works correctly and prints every element of the array exactly once, in order", "The starting value of i is wrong, since it should begin at 1", "arr.length should be arr.size(), as with an ArrayList"],
    P + "16": ["It's always a mistake and never intentional, since it skips the last element and loses data", "It makes the loop faster by skipping an unnecessary final pass", "arr.length - 1 always equals 0, so the loop never runs"],
    P + "19": ["It cannot read array elements at all, only write to them", "It only works on arrays of Strings, not primitive types", "It always traverses the array backward, starting from the last element and ending at the first"],
    P + "21": ["Enhanced for-loops are read-only in every situation and cannot be used at all with arrays of numbers", "Arrays cannot be traversed with a for-each loop, only with an index", "It always throws a runtime exception when you reassign the loop variable"],
    P + "23": ["When you need to modify array elements as you go along, replacing each one", "When you need to traverse the array backward, from the last index to the first", "When you need to skip every other element while you traverse it"],
    P + "24": ["The sum of all of the negative numbers in the array", "The index of the first negative element found", "The largest negative number in the array"],
    P + "27": ["It returns the value of target itself; -1 if not found", "It returns true or false depending on whether the target was found; false if not found", "It returns the count of matches in the array; 0 if not found"],
    P + "28": ["Nothing is wrong; it correctly reverses the array in place, since each pair of elements is swapped exactly once", "arr.length - 1 - i is an invalid index, which throws an exception on the first pass", "temp should be declared outside the loop, or the swap will not compile"],
}

PADC = {
    P + "16": "To intentionally stop one element early, often to compare arr[i] with arr[i+1] without going out of bounds",
    P + "21": "The loop variable holds a copy of each element's value; reassigning it does not change the array",
    P + "28": "The loop runs through the whole array, so each pair is swapped twice, undoing the reversal (it should stop at arr.length / 2)",
}

PADW = {
    "The largest negative number in the array": "The largest negative number found in the array",
}
