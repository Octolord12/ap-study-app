P = "ap-calc-u6-mcq-"

PAD = {
    P + "1": ["The slope of a tangent line at a single point on the curve", "The derivative of a function, evaluated at several sample points along the interval", "The domain of a function, written as an interval of x-values"],
    P + "2": ["The approximation becomes less accurate, because every additional rectangle adds error to the total", "The approximation stays exactly the same no matter how many rectangles are used, since the area is fixed", "Increasing the number of rectangles has no logical connection to the process at all, so accuracy is unaffected"],
    P + "3": ["The derivative of f at x=a, evaluated using the limit definition of the derivative", "A single rectangle's area only, using the height at the midpoint of [a,b]", "The value of f at x=b minus the value of f at x=a, computed directly with no limiting process involved at all"],
    P + "6": ["The function's value at the exact midpoint of each subinterval, which balances the over- and under-estimates", "The function's minimum value over the entire interval, for a conservative estimate", "The function's average value over the entire interval, for a smoothed estimate"],
    P + "7": ["The integral is always exactly zero whenever f is negative anywhere on the interval, because the positive and negative areas always cancel", "The integral cannot be computed if f is ever negative, since negative area has no meaning", None],
    P + "8": ["Meters/second (the same as f(x) itself, since the integrand's units are kept)", "Seconds² (the square of the time units)", "Meters/second² (the units of acceleration)"],
    P + "9": ["Derivatives and integrals are completely unrelated concepts that happen to share the same notation", "Integration always gives a constant value, whatever the function", "Differentiation always gives zero, whatever the function"],
    P + "19": ["Because \"+C\" makes the answer look more complete, even though it serves no real mathematical reason", "Because C always equals zero in the end, so the constant is a placeholder that drops out of the final answer", "Because indefinite integrals never actually have a solution without it, since the antiderivative would be undefined at every point of the domain"],
    P + "24": ["To make an integral more complicated on purpose, so that its structure is easier to see", "To avoid ever needing an antiderivative, by turning the integral into a numerical estimate", "To convert every integral into a derivative instead, so that it can be evaluated by differentiation alone"],
    P + "29": ["It's just an arbitrary trick with no real mathematical justification, which happens to give correct answers", "It only works for polynomial functions, since other functions cannot be substituted", "It works because all integrals are secretly the same, once a suitable variable is chosen"],
    P + "30": ["The bounds should be left unchanged as x-values, even after switching the integrand to the variable u", "The bounds should always become 0 and 1, regardless of the original problem or substitution", "Bounds are irrelevant for u-substitution and can be ignored entirely once u is defined"],
}

PADC = {
    P + "2": "The approximation generally becomes more accurate, approaching the exact area as the number of rectangles grows without bound",
    P + "7": "The integral represents signed area: area above the x-axis counts positively, while area below counts negatively",
    P + "8": "Meters (integrating velocity over time gives displacement)",
    P + "19": "Because the derivative of any constant is 0, so infinitely many antiderivatives (differing only by a constant) share the same derivative f(x)",
    P + "24": "To simplify a complicated integral by replacing part of the expression with a new variable u, making it easier to integrate",
    P + "29": "It is essentially the reverse of the Chain Rule, undoing a composite function's derivative to find the antiderivative",
    P + "30": "The bounds must be converted from x-values to the matching u-values (here x=0 becomes u=1, and x=2 becomes u=5)",
}

PADW = {}
