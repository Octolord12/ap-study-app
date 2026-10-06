P = "ap-csa-u10-mcq-"

PAD = {
    P + "1": ["A method that never returns a value to its caller", "A method that runs in a loop until a condition fails", "A method with no parameters of any kind"],
    P + "3": ["The case that causes infinite recursion if it is ever reached, which is why it must be avoided", "The very first time the method is ever called by the program", "A case that always throws an exception and ends the program"],
    P + "4": ["It runs once and returns immediately with a default value, since there is nothing to repeat", "It automatically stops after 100 calls, whatever the method does", "Java detects this at compile time and refuses to compile the class"],
    P + "8": ["It doesn't always reach the base case, and the method often recurses forever as a result of the argument", "Java automatically stops after a fixed number of calls, whatever the argument", "The base case is reached randomly, whatever the argument values are"],
    P + "10": ["Nothing would change, since the call still passes the same kind of value on to the next level", "It would count down twice as fast, since each call now skips one of the values", "It would count up instead of down, ending at the largest value the int can hold"],
    P + "13": ["One base case: n == 0, which stops the recursion", "No base case; it's pure recursion with nothing to stop it", "Three base cases: n == 0, n == 1 and n == 2"],
    P + "14": ["Nothing is wrong; it works correctly for every positive number that is passed to it", "The modulo operator cannot be used in recursive methods at all", "It should use a for loop instead, because recursion is not allowed here"],
    P + "15": ["Adding a for loop inside the method before the return", "Removing the % operator from the return statement", "Making the method private instead of public"],
    P + "17": ["Check every element one by one from the start of the array until a match is found or the end is reached", "Randomly guess indices until the target happens to be found", "Sort the array first, then use linear search on the sorted result"],
    P + "18": ["Index 0 (value 1), the first element", "The last index (value 11), at the far end", "Every index in order, from the first to the last"],
    P + "22": ["It checks every element, just in a different order, and the order happens to be faster in practice", "It doesn't actually check any elements, so no comparisons are needed", "It only works on arrays with fewer than 10 elements, so it is quicker"],
    P + "23": ["Repeatedly find the smallest remaining element and move it to the front of the array", "Check every possible ordering of the array until a sorted one is found", "Pick a random element and only compare every other element to that one"],
    P + "25": ["When the array has exactly 100 elements, since it is then large enough", "When every element is the same value as the one before it", "There is no base case in merge sort, since it always halts by itself"],
    P + "26": ["Concatenating them and then sorting the combined result from scratch with a different algorithm", "Randomly interleaving their elements until they appear sorted", "Reversing both arrays first, then comparing their last elements"],
    P + "27": ["It doesn't matter whether they're sorted first, since the merge step sorts the elements as it combines them", "Merging always re-sorts everything anyway, so it doesn't matter whether they were sorted", "Only one of the two halves needs to be sorted, and the other can be in any order"],
    P + "30": ["Linear search is also faster when the array is sorted, so this doesn't really matter much in practice", "Sorting is required for all searching algorithms, including linear search, which would otherwise miss elements that sit out of order", "Linear search cannot be used on sorted arrays, since it relies on the elements being in random order"],
}

PADC = {
    P + "3": "The condition under which the method stops calling itself and returns directly",
    P + "8": "The argument n decreases by 1 with each call, so it eventually reaches the base case (n <= 0)",
    P + "10": "Infinite recursion, since n never decreases toward the base case, causing a StackOverflowError",
    P + "14": "It has no base case, so it recurses infinitely (eventually causing a StackOverflowError)",
    P + "23": "Recursively divide the array in half, sort each half, then merge the sorted halves",
    P + "25": "When the array (or sub-array) has 0 or 1 elements, since it's already sorted",
    P + "27": "Merging compares the front (smallest remaining) elements of each half; this only works if each half is already in order",
    P + "30": "Binary search compares against the middle element to eliminate half the remaining elements; this only works if the order lets it infer which half holds the target",
}

PADW = {}
