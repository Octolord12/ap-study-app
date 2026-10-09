P = "ap-calc-u1-mcq-"

PAD = {
    P + "1": ["f(c) = L exactly, at the point x = c", "f is undefined at c, so L is only a placeholder", "The derivative of f at c is L, the slope at that point"],
    P + "6": ["A two-sided limit can exist even if the one-sided limits disagree, as long as one of them is defined", "One-sided limits are irrelevant to two-sided limits, which are computed separately", "A two-sided limit always exists regardless of one-sided behavior, as long as f is defined"],
    P + "13": ["Only that f(c) is defined, since a value at the point is all that continuity requires", "Only that the limit exists, since the value at the point itself does not matter", "f must be a polynomial, since only polynomials can be continuous at a point"],
    P + "14": ["Yes, because f(3) is defined and equals 10", "Yes, because the limit exists as x approaches 3", "No, because f(3) is undefined at that point"],
    P + "18": [None, "f must be increasing on all of [a, b], never turning around", "f is undefined at the endpoints a and b, where the graph stops"],
    P + "21": ["The numerator equals zero, so the whole fraction equals zero there", "The function is at its maximum value, so the graph peaks there", "x equals zero, since the function is undefined at the origin"],
    P + "23": ["The function's behavior at a single specific finite x-value, such as x = 0", "Points where the function crosses the x-axis or touches it", "The function's maximum height over the whole domain"],
    P + "25": ["f must be increasing on [a,b], rising from f(a) to f(b)", "f(a) must equal f(b) at the two endpoints of the interval", "f has no maximum or minimum anywhere on [a,b], because a continuous function can never attain either"],
    P + "26": ["f must be differentiable everywhere on the interval and beyond", "f must be a polynomial of degree at least two", "f must be linear, with a constant slope"],
    P + "27": ["f(c) = 0 has no solutions in [1,4], so f never reaches zero", None, None],
    P + "28": ["Because $x^3$ is always positive on [1,2], so no sign change can occur", "Because the equation has degree 3, and every cubic polynomial has a root between any two consecutive integers", "Because f(1) equals f(2), so the function must cross zero somewhere between them"],
    P + "29": ["Continuity has no real bearing on whether the IVT's conclusion holds for any function", "Jump discontinuities always make functions equal every intermediate value automatically, even across a gap", "The IVT works identically whether or not a function is continuous on the interval"],
    P + "30": ["f(-1) equals f(1), and a function with equal endpoint values can never have a root between them", "1/x is always positive, so its graph stays above the x-axis and never reaches zero on any interval", "The IVT guarantees a root does exist here, because f(-1) and f(1) have opposite signs and f is a simple function"],
}

PADC = {
    P + "30": "f(x) = 1/x is not continuous on [-1,1] because it is undefined at x=0, so the IVT's continuity requirement is not met",
}

PADW = {
    "f must be linear, with a constant slope": "f must be linear, with a constant slope throughout the interval",
    "f(c) = L exactly, at the point x = c": "f(c) = L exactly, at the single point x = c",
    "f must be a polynomial, since only polynomials can be continuous at a point": "f must be a polynomial, since only polynomials are ever continuous at a point",
    "f must be a polynomial of degree at least two": "f must be a polynomial of degree at least two on the interval",
    "Yes, but only because g is linear on both pieces": "Yes, but only because g is linear on both pieces of its definition",
    "Ignoring the denominator entirely": "Ignoring the denominator, using only the numerator",
}
