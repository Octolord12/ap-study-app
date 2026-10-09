P = "ap-calc-u4-mcq-"

PAD = {
    P + "3": ["The particle has infinite speed at that moment, so it moves instantly", "The particle no longer exists after that moment in time", "The particle's position is always 0 from then on, so it stays at the origin"],
    P + "6": ["They are always exactly the same value, no matter how many times the particle reverses direction or how far it travels along its winding path", "Distance is always negative, while displacement is always positive, regardless of which way the particle moves", "There is no meaningful difference between these two concepts, since both measure how far the particle ends up"],
    P + "7": ["The particle's speed is maximum at t=3 and then decreases", "The particle's acceleration is zero everywhere on the interval, so it moves at a constant velocity throughout", "The particle stops permanently after t=3 and never moves again"],
    P + "9": ["Finding the maximum value of a function on a closed interval, using the Extreme Value Theorem", "Finding the area under a curve between two points", "Finding the limit of a sequence as n grows without bound"],
    P + "13": ["Time is irrelevant to related rates problems, which only compare the variables with each other", "The equation should be differentiated with respect to one of the OTHER variables instead, like x or y, since time never appears", "Differentiating with respect to time is optional and can be skipped when the units already match"],
    P + "15": ["Simply add dx/dt and dy/dt together directly, since the two speeds combine linearly into the speed of separation", "Take the square root of dx/dt and dy/dt separately, then multiply the two results together to get dz/dt", "Ignore the Pythagorean relationship and use unrelated formulas for speed and distance"],
    P + "17": ["To find the exact value of f(x) for ALL x, not just values of x near the point a", "To find the area under f's curve between two chosen x-values", "To find the second derivative of f at the point x=a"],
    P + "20": ["Local linearization is always perfectly accurate no matter how far x is from a, since the tangent line equals the curve everywhere on its domain, including at points far from a", "The tangent line formula changes automatically for different x, so it no longer applies to the original point", "f'(a) becomes undefined for x far from a, so the slope of the tangent line no longer exists"],
    P + "23": ["f(x) and g(x) must both be constant functions on a neighborhood of c", "The limit must already be a known finite number before starting", "g(x) must never equal zero anywhere on the number line"],
    P + "27": ["Because L'Hopital's Rule can never be used with linear functions, only with polynomials of degree two or higher", "Because the denominator is never zero anywhere on the real line, so the limit cannot be indeterminate", "Because L'Hopital's Rule only works for trigonometric functions, never for rational functions like this one"],
    P + "28": ["You must immediately conclude the limit does not exist, since the first attempt failed", "You must go back to using algebraic factoring exclusively, abandoning derivatives", "L'Hopital's Rule can only ever be applied exactly once, no matter what form the new limit takes"],
    P + "30": ["The Intermediate Value Theorem, since continuity links the variables", "The definition of a limit, applied separately to each variable", "The Power Rule alone, with no other differentiation rules needed, since every term is a simple power of one variable"],
}

PADC = {
    P + "6": "Total distance counts ALL movement, including back-and-forth motion, while displacement is just the net change in position from start to end",
    P + "13": "Because all the variables in the equation are functions of time, so their rates of change are with respect to t",
    P + "15": "Differentiate z² = x² + y² with respect to time, then substitute the known x, y, dx/dt, dy/dt to solve for dz/dt",
    P + "20": "Because the tangent line only closely matches f(x) very near x=a; farther away, the curve's behavior (concavity, etc.) diverges from the straight tangent line",
    P + "27": "Because direct substitution already gives a well-defined, non-indeterminate value (5), so the rule is not needed or applicable",
}

PADW = {
    "g(x) must never equal zero anywhere on the number line": "g(x) must never equal zero anywhere on the number line, including at the limit point",
    "You must go back to using algebraic factoring exclusively, abandoning derivatives": "You must go back to using algebraic factoring exclusively, abandoning derivatives for the rest of the problem",
    "The limit must already be a known finite number before starting": "The limit must already be a known finite number before you start differentiating",
    "You must immediately conclude the limit does not exist, since the first attempt failed": "You must immediately conclude the limit does not exist, since the first application of the rule failed",
}
