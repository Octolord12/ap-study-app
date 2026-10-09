P = "ap-calc-u7-mcq-"

PAD = {
    P + "1": ["An equation with no variables at all, only numbers and operations", "An equation that only involves constants and arithmetic, with no unknown function in it", "An equation describing a straight line only, like y = mx + b"],
    P + "2": ["A quantity that never changes over time, whatever its initial value", "A quantity whose rate of change is constant, regardless of its current value or the time", None],
    P + "4": ["The order is the highest power the variable y is raised to; this equation is order 2, because of the x² term", "The order refers to how many terms are in the equation; this one has three terms, so it is order 3", "There is no such thing as the \"order\" of a differential equation, since all of them are alike"],
    P + "5": ["They can only describe static, unchanging quantities, never anything that varies over time or responds to its surroundings", "They have no real-world applications, since every real process is modeled by a plain formula", "They only apply to purely abstract mathematical concepts with no connection to reality or to any physical process"],
    P + "6": ["A single specific numerical value of x for which both sides of the equation are equal", "A graph with no mathematical meaning, drawn only to illustrate the equation's general shape", "An equation with no y or x terms at all, obtained by cancelling every variable from both sides"],
    P + "7": ["They are always exactly identical, differing only in the notation used to write the constant of integration", "A particular solution never satisfies the differential equation, so it is only an approximation of the general one", "A general solution can never be found, while a particular solution is always easy to compute from the equation"],
    P + "8": ["To calculate exact numerical solutions with perfect precision at every point", "To find the antiderivative of a function by reading off its slope", "To graph a single specific function with no connection to differential equations, such as a polynomial"],
    P + "9": ["The y-intercept of the solution curve that passes through the point (x,y)", "The x-intercept of the solution curve that passes through the point (x,y)", "A random, arbitrary slope with no connection to the differential equation or to the solution curve"],
    P + "10": ["Vertical segments (undefined slope), since the slope blows up", "Segments with a slope of 1, since dy/dx = 1 there", "Segments with a slope of -1, since dy/dx = -1 there"],
    P + "11": ["The slopes stay exactly the same everywhere, regardless of y, since the slope depends only on x", "The slopes become flatter (closer to zero) as y increases, since the rate falls with y", "The slopes become negative as y increases, since the solution curves bend downward"],
    P + "12": ["Slope fields cannot help sketch solution curves at all, since they only show isolated segments that never connect into a curve", "By ignoring the initial point entirely and drawing any curve that looks smooth", "By only looking at segments far away from the initial point, where the field is simplest"],
    P + "13": ["The exact numerical value of any specific solution at any point, with complete precision and no approximation of any kind", "Nothing useful; slope fields provide no meaningful insight about any differential equation", "Only the color of the resulting graph and its overall shading"],
    P + "14": ["Never separating any terms at all, and integrating the whole equation in one step with respect to x", "Immediately guessing a solution with no algebraic work, then checking it by substitution", "Setting all variables equal to zero and solving for the constant that remains"],
    P + "19": ["f(x,y) must always be a constant, so the right-hand side contains neither x nor y at all", "The equation must have no y term at all, so that only x remains on the right-hand side", None],
    P + "20": ["Ignore the initial condition entirely, since the general solution is already complete", "Immediately conclude no solution exists, since the initial condition has not yet been used in the integration", "Multiply both sides by zero to remove the constant from the equation"],
    P + "29": ["The negative sign has no particular meaning or purpose; it is only a convention of notation that could be dropped", "Because temperature can never be positive in this model, so the rate must carry a minus sign to compensate", "Because k must always be negative for this to make sense, so the minus sign is part of the constant"],
}

PADC = {
    P + "4": "The order is the highest derivative present; this equation has only dy/dx (a first derivative), so it is first-order",
    P + "5": "They describe how a quantity's rate of change relates to the quantity itself or other variables, capturing dynamic processes over time",
    P + "6": "A function that satisfies the differential equation when it and its derivatives are substituted in",
    P + "7": "A general solution includes an arbitrary constant (like +C), while a particular solution fixes that constant using an initial condition",
    P + "12": "By following the direction of the segments from the initial point, tracing a curve that stays tangent to the local slopes throughout",
    P + "14": "Rearranging so all y-terms (with dy) are on one side and all x-terms (with dx) are on the other, then integrating both sides",
    P + "29": "Because if T > T_a (object warmer than surroundings), the object should be COOLING (T decreasing), requiring a negative rate",
}

PADW = {
    "The order is the highest power the variable y is raised to; this equation is order 2, because of the x² term": "The order is the highest power the variable y is raised to; this equation is order 2, because of the x² term in the equation",
    "They can only describe static, unchanging quantities, never anything that varies over time or responds to its surroundings": "They can only describe static, unchanging quantities, never anything that varies over time or responds to its surroundings or to any outside influence",
    "An equation with no y or x terms at all, obtained by cancelling every variable from both sides": "An equation with no y or x terms at all, obtained by cancelling every variable from both sides and leaving only constants behind",
    "A particular solution never satisfies the differential equation, so it is only an approximation of the general one": "A particular solution never satisfies the differential equation, so it is only an approximation of the general one and never an exact function",
    "Slope fields cannot help sketch solution curves at all, since they only show isolated segments that never connect into a curve": "Slope fields cannot help sketch solution curves at all, since they only show isolated segments that never connect into a curve, so no solution can be sketched from them",
    "The exact numerical value of any specific solution at any point, with complete precision and no approximation of any kind": "The exact numerical value of any specific solution at any point, with complete precision and no approximation of any kind, even for equations with no formula",
    "Never separating any terms at all, and integrating the whole equation in one step with respect to x": "Never separating any terms at all, and integrating the whole equation in one step with respect to x, then solving for the constant at the end of the process",
    "Separation of variables works for absolutely any differential equation, with no restrictions": "Separation of variables works for absolutely any differential equation, with no restrictions, which makes the technique a universal method",
    "The negative sign has no particular meaning or purpose; it is only a convention of notation that could be dropped": "The negative sign has no particular meaning or purpose; it is only a convention of notation that could be dropped without changing the meaning of the equation",
    "An equation describing a straight line only, like y = mx + b": "An equation describing a straight line only, like y = mx + b with a constant slope",
    "A quantity with no relationship between its rate and its value": "A quantity with no relationship between its rate and its value at any moment in time",
    "A single specific numerical value of x for which both sides of the equation are equal": "A single specific numerical value of x for which both sides of the equation are equal at one particular input",
    "Segments with a slope of 1, since dy/dx = 1 there": "Segments with a slope of 1, since dy/dx = 1 there along the line x=0",
    "The slopes become negative as y increases, since the solution curves bend downward": "The slopes become negative as y increases, since the solution curves bend downward toward the axis",
    "A quantity that never changes over time, whatever its initial value": "A quantity that never changes over time, no matter what its initial value happens to be",
}
