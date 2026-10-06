P = "ap-calc-u8-mcq-"

PAD = {
    P + "7": ["The car's total distance traveled during the trip", "The car's maximum velocity reached at any moment during the trip", "The car's acceleration at the end of the trip"],
    P + "13": ["Nothing needs to change; you can always integrate f(x)-g(x) as a single integral regardless of crossings, since the signed areas add up correctly", "You should simply ignore the region past the crossing point entirely, since it contributes no area to the total", "You must use only the far endpoints, disregarding the crossing point entirely, because only the ends matter"],
    P + "15": ["Immediately integrate f(x)-g(x) from negative infinity to positive infinity, then divide by two", "Assume the bounds are always 0 and 1, since the region is bounded by the axes", "Differentiate both functions to find where their slopes are equal"],
    P + "16": ["Finding the area under a curve, by summing the areas of many thin rectangles of equal width across the interval", "Finding the slope of a tangent line, by taking the limit of secant slopes as the interval shrinks", "Finding the length of a curve, by integrating the lengths of tiny straight-line segments approximating its path from start to end"],
    P + "20": ["The washer method is used only for solids with no holes at all, where every cross-section is a full disc and no inner radius is ever needed", "There is no difference between the two methods, since a washer is just a disc with a different name", "The washer method never involves integration, since it uses only the formula for a ring's area"],
    P + "25": ["By finding the perimeter of the base region only, then multiplying it by the greatest height of the solid at each point", "By always assuming the solid is a cylinder, whatever the shape of the cross-sections", "By differentiating the base area function with respect to position along the axis"],
    P + "30": ["The shape of the cross-section never matters; every shape has the same area formula, so any shape can be substituted into the integral without changing the volume", "Only square cross-sections are ever used in these problems, so there is no shape to identify before integrating", "The base region's boundaries are irrelevant once the shape is identified, since only the shape matters for the area"],
}

PADC = {
    P + "13": "Split the integral at each crossing point and take the absolute value of (or swap the subtraction in) each piece, since which function is \"on top\" changes",
    P + "15": "Set f(x)=g(x) and solve for the x-coordinates of the intersection points, which become the bounds of integration",
    P + "16": "Finding the volume of a solid formed by rotating a region bounded by a curve and an axis around that axis, by integrating the areas of circular cross-sections (discs)",
    P + "20": "The washer method is used when the solid has a hole through it (the region is bounded away from the axis by an inner curve), so an inner radius is subtracted",
    P + "25": "By integrating the area of the cross-sectional shape (perpendicular to an axis) as a function of position along that axis",
    P + "30": "Because each shape has a different area formula in terms of its side or radius (set by the base region), and the wrong formula gives an incorrect area function to integrate",
}

PADW = {
    "Nothing needs to change; you can always integrate f(x)-g(x) as a single integral regardless of crossings, since the signed areas add up correctly": "Nothing needs to change; you can always integrate f(x)-g(x) as a single integral regardless of crossings, since the signed areas add up correctly on every interval",
    "Always convert to functions of x first, since integrating with respect to y is never valid": "Always convert to functions of x first, since integrating with respect to y is never valid, because only vertical slices can ever give an area",
    "Immediately integrate f(x)-g(x) from negative infinity to positive infinity, then divide by two": "Immediately integrate f(x)-g(x) from negative infinity to positive infinity, then divide by two to obtain the area between them",
    "Finding the length of a curve, by integrating the lengths of tiny straight-line segments approximating its path from start to end": "Finding the length of a curve, by integrating the lengths of tiny straight-line segments approximating its path from start to end, a quantity measured in units of length rather than volume",
    "The washer method is used only for solids with no holes at all, where every cross-section is a full disc and no inner radius is ever needed": "The washer method is used only for solids with no holes at all, where every cross-section is a full disc and no inner radius is ever needed, in any problem or any region",
    "By finding the perimeter of the base region only, then multiplying it by the greatest height of the solid at each point": "By finding the perimeter of the base region only, then multiplying it by the greatest height of the solid at each point in the base region",
    "The shape of the cross-section never matters; every shape has the same area formula, so any shape can be substituted into the integral without changing the volume": "The shape of the cross-section never matters; every shape has the same area formula, so any shape can be substituted into the integral without changing the volume of the solid being measured",
    "The car's acceleration at the end of the trip": "The car's acceleration at the end of the trip, the rate its speed changes",
}
