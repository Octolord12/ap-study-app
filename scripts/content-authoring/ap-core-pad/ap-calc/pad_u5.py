P = "ap-calc-u5-mcq-"

PAD = {
    P + "1": ["f'(x) = 0 for every x in (a,b), so the function is constant on the interval", "f(a) must equal f(b), so the function returns to its start", "f has no maximum on [a,b], since f keeps rising"],
    P + "2": ["f must be a polynomial function only, with no other types allowed", "f(a) must equal f(b), so the endpoints have the same height", "f must be increasing throughout [a,b], with positive slope"],
    P + "5": ["f'(x) = 0 for every x in (a,b), not just at one point", "f(x) = 0 for every x in [a,b], so the graph lies on the axis", "There is no critical point in (a,b), so f is monotonic"],
    P + "6": ["The car must travel at a constant speed for the entire trip, never speeding up or slowing down", "The car's average speed must always be zero, because it ends up where it started", "The MVT has no real-world applications, since it describes only abstract functions and never actual motion"],
    P + "7": ["Any point where f(x) = 0, such as an x-intercept of the graph", "The highest point on the entire graph, over the whole domain of the function", "A point where f is discontinuous, such as a jump or hole"],
    P + "11": ["They are always exactly the same thing with no distinction between them, since every extremum is global on its own and no function ever has more than one such point on its domain", "A local extremum only applies to linear functions, while a global extremum applies only to curves with a maximum", "A global extremum can never also be a local extremum, because the two kinds exclude each other on any interval"],
    P + "13": ["The graph is a straight line with constant slope", "The graph curves downward, like a frown (f''(x) < 0 on that interval)", "The function is always positive on that interval, above the x-axis"],
    P + "15": ["f definitely has a local maximum at x=c, because the slope is zero and the concavity is flat there", "f definitely has a local minimum at x=c, because the slope is zero and the concavity is flat there", "f is definitely not differentiable at x=c, since the second derivative is zero"],
    P + "17": ["A point where the function equals zero and crosses the x-axis, changing from positive to negative or the reverse", "A point where the function is undefined, such as a vertical asymptote", "The highest point on the entire graph, where the slope is zero"],
    P + "19": ["To find the derivative of a function for its own sake, with no further purpose or application in mind", "To find the limit of a function as x approaches infinity, whatever its domain", "To determine whether a function is continuous at every point of its domain"],
    P + "20": ["Immediately take the second derivative before doing anything else, since concavity decides which quantity matters", "Ignore any given constraints entirely, since they only complicate the algebra of the problem", "Guess a reasonable-sounding final answer, then test it against the information in the problem"],
    P + "23": ["All critical points are automatically maximums by definition, so no extra check is ever needed in these problems", "Verification is never actually necessary in optimization problems, since any critical point gives the correct answer", "Critical points can never correspond to minimums, only to maximums or to inflection points"],
    P + "24": ["Only the function's y-intercept and its value at x=0", None, "Random guessing of points on the graph, then connecting them"],
    P + "28": ["The first and second derivatives always give exactly the same information about the graph, so combining them is redundant and only wastes time", "Only the second derivative is ever useful; the first derivative can be ignored, since concavity alone determines the whole graph", "Combining them serves no additional purpose beyond using just one of them, because each describes the whole curve alone"],
    P + "29": ["The critical point must be a local maximum, since the slope is zero there", "The critical point must be a local minimum, since the slope is zero there", None],
    P + "30": ["x=0 is a local maximum, because f'(0)=0 and the graph turns around there as the sign of the slope changes", "x=0 is a local minimum, because f'(0)=0 and the graph turns around there as the sign of the slope changes", "f is not differentiable at x=0, because the graph has a sharp corner at the origin where the left and right slopes disagree"],
}

PADC = {
    P + "11": "A local extremum is the highest or lowest value in some neighborhood of that point, while a global extremum is the highest or lowest value over the whole domain",
    P + "20": "Identify the quantity to be maximized or minimized, and write it as a function of one variable (using any given constraints)",
    P + "23": "A critical point could be a maximum, a minimum, or neither, so the First or Second Derivative Test is needed to verify it",
    P + "28": "The first derivative shows where f is increasing or decreasing and locates extrema, while the second shows concavity and inflection points -- together they give a fuller picture",
    P + "30": "f'(x) = 3x² ≥ 0 everywhere and never changes sign, so x=0 is neither a local max nor min (an inflection point with a horizontal tangent)",
}

PADW = {
    "A point where f is discontinuous, such as a jump or hole": "A point where f is discontinuous, such as a jump or hole in its graph",
    "Only at the critical points, never at the endpoints": "Only at the critical points, never at the endpoints of the closed interval",
    "f is definitely not differentiable at x=c, since the second derivative is zero": "f is definitely not differentiable at x=c, since the second derivative is zero at that point as well",
    "To determine whether a function is continuous at every point of its domain": "To determine whether a function is continuous at every point of its domain, and nothing more",
    "Any point where f(x) = 0, such as an x-intercept of the graph": "Any point where f(x) = 0, such as an x-intercept on the graph of f itself",
}
