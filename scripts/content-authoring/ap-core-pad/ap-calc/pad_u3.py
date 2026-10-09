P = "ap-calc-u3-mcq-"

PAD = {
    P + "1": ["Only polynomial functions, never anything else", None, "Functions with no variables in them at all"],
    P + "8": ["It isn't necessary; composite functions can be differentiated by any method, since every method gives the same result as the product of f'(x) and g'(x)", "Because composite functions have no derivatives, so the Chain Rule is used to approximate them instead", "Because f(g(x)) is always equal to f(x)·g(x), and the Chain Rule is a shortcut for the product rule"],
    P + "10": ["dx/dy (since x is a function of y)", "No extra factor is needed when y appears in a power", None],
    P + "14": ["y is simply treated as a constant and ignored entirely, so any term containing y differentiates to zero and drops out of the equation", "x and y are swapped throughout the entire process, so the equation is solved for x first", "Implicit differentiation only works for equations with no y terms at all, because y cannot be differentiated"],
    P + "21": ["Because f'(x) is always zero for invertible functions, so the formula needs a different point where the derivative is nonzero and defined", "Because dividing is always required in calculus when two functions are composed with each other", "There's no real reason; it's an arbitrary convention that textbooks adopted long ago"],
    P + "23": ["The derivative taken twice as fast as the first", "f(x) divided by 2, the half-value of the function", "The average of f(x) and f'(x) at each input"],
}

PADC = {
    P + "8": "Because the inner function g(x) is itself changing with respect to x, and that rate of change must be accounted for alongside the outer function's sensitivity",
    P + "14": "Every time you differentiate a term containing y, you multiply by dy/dx (by the chain rule, since y is treated as a function of x)",
    P + "21": "Because the inverse function's rate of change at x depends on the ORIGINAL function's rate of change at the corresponding point g(x), not at x",
}

PADW = {
    "Only sums of functions": "Only sums of functions, such as f(x) + g(x) and nothing else",
    "dx/dy (since x is a function of y)": "dx/dy (since x is a function of y) and must be multiplied in",
    "The average of f(x) and f'(x) at each input": "The average of f(x) and f'(x) at each input over the interval",
    "y itself, with no derivative notation": "y itself, with no derivative notation attached to the term",
    "The object's velocity": "The object's velocity at time t",
}
