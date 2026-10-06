P = "ap-calc-u2-mcq-"

PAD = {
    P + "1": ["The slope of the tangent line at x=a, at the left endpoint", "The value of f at the midpoint of [a,b], found by averaging f(a) and f(b)", "The area under the curve from a to b, above the x-axis"],
    P + "6": ["Because limits are only used for infinite intervals, so a finite interval such as [a,b] can never require one", "Because average rates of change are always more accurate than any limit-based calculation could be", "There is no real distinction between the two concepts, since a small interval gives the same answer"],
    P + "9": ["Yes, continuity always guarantees differentiability, since both describe the same smooth behavior at a point", "Continuity and differentiability are always equivalent conditions for functions of one variable", "Differentiability is a weaker condition than continuity, so it is easier for a function to meet"],
    P + "10": ["|x| is not continuous at x=0, because the graph has a jump at the origin where the left and right branches meet", "f(0) is undefined, so there is no value of the function at the origin from which a derivative could be computed", "|x| has no defined value anywhere on the real line, so it cannot be differentiated at x=0 or at any other point"],
    P + "11": ["A smooth, rounded curve with no breaks", "A straight line segment with a constant, nonzero slope", None],
    P + "12": ["The function is defined at only one point in the interval and nowhere else on it", "The function must be a straight line throughout the interval, with a constant slope", None],
    P + "30": ["The Quotient Rule, since there is division involved in the expression", "The Power Rule alone, without needing any other rule or any expansion", None],
}

PADC = {
    P + "4": "6",
    P + "6": "Because we want the rate of change AT a single point, which requires shrinking the interval to zero width with a limit",
    P + "10": "The left- and right-hand derivatives at x=0 are -1 and 1, so they are not equal and the derivative does not exist despite continuity",
}

PADW = {
    "The area under the curve from a to b, above the x-axis": "The area under the curve from a to b, above the x-axis, which the secant does not measure",
    "Continuity and differentiability are always equivalent conditions for functions of one variable": "Continuity and differentiability are always equivalent conditions for functions of one variable on any interval",
    "A smooth, rounded curve with no breaks": "A smooth, rounded curve with no breaks or sharp turns anywhere",
    "The function's derivative is always zero throughout the interval": "The function's derivative is always zero throughout the interval, so its graph is a flat line",
    "The Sum Rule, since there are multiple terms being added": "The Sum Rule, since there are multiple terms being added together in the expression",
}
