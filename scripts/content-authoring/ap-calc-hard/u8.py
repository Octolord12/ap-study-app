from lib import *

B = Bank(8, "unit-8-applications-of-integration")
T_AVG, T_AREA, T_XS, T_DW = (
    "average-value-of-a-function",
    "area-between-curves",
    "volume-by-cross-sections",
    "volume-by-disc-washer",
)

# 1. average value with a u-substitution
avg = integrate(x * exp(x**2), (x, 0, 2)) / 2
assert simplify(avg - (exp(4) - 1) / 4) == 0
B.mcq(T_AVG, "What is the average value of $f(x)=xe^{x^2}$ on the interval $[0,2]$?",
      ch("$\\dfrac{e^4-1}{4}$", "Average value $=\\frac{1}{2-0}\\int_0^2xe^{x^2}dx$. With $u=x^2$: $\\int_0^2xe^{x^2}dx=\\frac12\\left(e^4-1\\right)$. Dividing by the interval length 2 gives $\\frac{e^4-1}{4}$."),
      [ch("$\\dfrac{e^4-1}{2}$", "This is the value of the integral. The average value also divides by the length of the interval, $b-a=2$."),
       ch("$e^4-1$", "This misses both the factor $\\frac12$ from the substitution ($du=2x\\,dx$) and the division by the interval length."),
       ch("$\\dfrac{e^4-1}{8}$", "This divides by 2 twice more than needed. The factor $\\frac12$ from the substitution and the factor $\\frac12$ from the average each appear once.")],
      "Average value $=\\frac{1}{b-a}\\int_a^bf(x)\\,dx$. Evaluate the integral with $u=x^2$.")

# 2. average value and total integral
B.mcq(T_AVG, "The function $f$ is continuous on $[1,5]$. The average value of $f$ on $[1,5]$ is 3, and $\\displaystyle\\int_1^3f(x)\\,dx=4$. What is $\\displaystyle\\int_3^5f(x)\\,dx$?",
      ch(8, "The average value gives $\\int_1^5f=3\\cdot(5-1)=12$. Then $\\int_3^5f=12-\\int_1^3f=12-4=8$."),
      [ch(12, "12 is $\\int_1^5f$, the whole integral. Subtract the part from 1 to 3."),
       ch(4, "4 is $\\int_1^3f$, which is given. The remaining part is a different integral."),
       ch(6, "This assumes the average value of $f$ on $[3,5]$ is also 3 ($3\\cdot2=6$). Only the average over the whole interval is known.")],
      "Convert the average value into a total with $\\int_a^bf=\\text{avg}\\cdot(b-a)$, then split the integral.")

# 3. area with a sign change
area = 2 * integrate(x - x**3, (x, 0, 1))
assert area == Rational(1, 2) and integrate(x - x**3, (x, -1, 1)) == 0
B.mcq(T_AREA, "What is the total area of the region enclosed by the graphs of $y=x^3$ and $y=x$?",
      ch(Rational(1, 2), "The graphs meet at $x=-1,0,1$. On $(0,1)$, $x>x^3$; on $(-1,0)$, $x^3>x$. By symmetry the area is $2\\int_0^1(x-x^3)\\,dx=2\\left(\\frac12-\\frac14\\right)=\\frac12$."),
      [ch(0, "$\\int_{-1}^1(x-x^3)\\,dx=0$ because the top and bottom curves swap at $x=0$, so the signed pieces cancel. Area uses the positive distance on each piece."),
       ch(Rational(1, 4), "This is the area of one of the two regions. There is a second region on $(-1,0)$ of equal size."),
       ch(1, "$2\\int_0^1\\left(x-x^3\\right)dx=2\\cdot\\frac14=\\frac12$. A value of 1 would double it again.")],
      "Find all intersection points, determine which curve is on top on each interval, and add the areas.")

# 4. area integrated in y
y_ = y
area = integrate((y_ + 2) - y_**2, (y_, -1, 2))
assert area == Rational(9, 2)
B.mcq(T_AREA, "What is the area of the region bounded by the parabola $x=y^2$ and the line $x=y+2$?",
      ch(Rational(9, 2), "Intersections: $y^2=y+2$ gives $y=-1$ and $y=2$. Integrating with respect to $y$, the line is to the right of the parabola: $\\int_{-1}^2\\left((y+2)-y^2\\right)dy=\\left[\\frac{y^2}{2}+2y-\\frac{y^3}{3}\\right]_{-1}^2=\\frac92$."),
      [ch(Rational(-9, 2), "The order of subtraction is reversed (parabola minus line). The right curve minus the left curve is positive."),
       ch(9, "This doubles the area, perhaps by integrating on both sides of a symmetry that does not exist here. The region is not symmetric."),
       ch(Rational(15, 2), "This is $\\int_{-1}^{2}(y+2)\\,dy$, the line's contribution alone. The parabola's $x$-values $y^2$ must be subtracted.")],
      "The curves are given as $x$ in terms of $y$, so integrate with respect to $y$ from the lower to the upper intersection, subtracting left from right.")

# 5. square cross-sections
V = integrate((4 - x**2) ** 2, (x, -2, 2))
assert V == Rational(512, 15)
B.mcq(T_XS, "The base of a solid is the region between the graph of $y=x^2$ and the line $y=4$. Cross-sections of the solid perpendicular to the $x$-axis are squares. What is the volume of the solid?",
      ch(Rational(512, 15), "The graphs meet at $x=\\pm2$. A cross-section at $x$ has side $4-x^2$, so area $(4-x^2)^2$. $V=\\int_{-2}^2(4-x^2)^2dx=2\\int_0^2\\left(16-8x^2+x^4\\right)dx=\\frac{512}{15}$."),
      [ch(Rational(256, 15), "This only integrates from 0 to 2. The region extends from $x=-2$ to $x=2$."),
       ch(Rational(32, 3), "This integrates the side length, $\\int_{-2}^{2}(4-x^2)\\,dx$. A cross-section's area is the side squared."),
       ch(64, "This is $4\\times16$, using $(4-0)^2=16$ for every cross-section. The side shrinks as $x$ moves away from 0.")],
      "Volume $=\\int A(x)\\,dx$. Find the side length as a function of $x$, square it for the area, and integrate across the base.")

# 6. equilateral triangle cross-sections
V = sqrt(3) / 4 * integrate((1 - x**2) ** 2, (x, -1, 1))
assert simplify(V - 4 * sqrt(3) / 15) == 0
B.mcq(T_XS, "The base of a solid is the region between the $x$-axis and the graph of $y=1-x^2$. Cross-sections perpendicular to the $x$-axis are equilateral triangles, each with one side in the base. What is the volume of the solid?",
      ch("$\\dfrac{4\\sqrt3}{15}$", "The side of the triangle at $x$ is $s=1-x^2$, and an equilateral triangle of side $s$ has area $\\frac{\\sqrt3}{4}s^2$. $V=\\frac{\\sqrt3}4\\int_{-1}^1(1-x^2)^2dx=\\frac{\\sqrt3}{4}\\cdot\\frac{16}{15}=\\frac{4\\sqrt3}{15}$."),
      [ch("$\\dfrac{16}{15}$", "This is $\\int_{-1}^1(1-x^2)^2dx$, the integral of side squared. The area of an equilateral triangle is $\\frac{\\sqrt3}{4}s^2$, not $s^2$."),
       ch("$\\dfrac{8\\sqrt3}{15}$", "This uses $\\frac{\\sqrt3}{2}s^2$ for the triangle's area. The area of an equilateral triangle of side $s$ is $\\frac{\\sqrt3}{4}s^2$."),
       ch("$\\dfrac{4}{15}$", "This loses the factor $\\sqrt3$ from the triangle's area $\\frac{\\sqrt3}{4}s^2$.")],
      "The area of an equilateral triangle with side $s$ is $\\frac{\\sqrt3}{4}s^2$. Here $s$ is the length of the base segment at $x$.")

# 7. washer about a horizontal line below the region
V = pi * integrate((sqrt(x) + 1) ** 2 - 1, (x, 0, 4))
assert simplify(V - 56 * pi / 3) == 0
B.mcq(T_DW, "The region bounded by $y=\\sqrt{x}$, the $x$-axis and the line $x=4$ is rotated about the line $y=-1$. What is the volume of the solid generated?",
      ch("$\\dfrac{56\\pi}{3}$", "Washers: outer radius $\\sqrt x+1$ (distance from $y=-1$ to the curve), inner radius $1$ (distance to the $x$-axis). $V=\\pi\\int_0^4\\left[(\\sqrt x+1)^2-1\\right]dx=\\pi\\int_0^4(x+2\\sqrt x)\\,dx=\\pi\\left(8+\\frac{32}3\\right)=\\frac{56\\pi}3$."),
      [ch("$8\\pi$", "This is the volume when the region is rotated about the $x$-axis ($\\pi\\int_0^4x\\,dx$). Rotating about $y=-1$ adds a 1-unit gap."),
       ch("$\\dfrac{68\\pi}{3}$", "This uses the full disk of radius $\\sqrt x+1$ and forgets the hole: the inner radius is 1 because the region sits on the $x$-axis, 1 unit above the axis of rotation."),
       ch("$\\dfrac{4\\pi}{3}$", "This uses radii $\\sqrt x-1$ (subtracting instead of adding the distance to the axis). The axis $y=-1$ is below the region, so distances add.")],
      "Each radius is the distance from the axis of rotation to the curve. Because the axis is below the region, add 1 to each height.")

# 8. region between y=x and y=x^2 about the y-axis
V = pi * integrate(y - y**2, (y, 0, 1))
assert V == pi / 6
B.mcq(T_DW, "The region in the first quadrant bounded by $y=x$ and $y=x^2$ is rotated about the $y$-axis. What is the volume of the solid generated?",
      ch(pi / 6, "Integrate in $y$. At height $y$ the region runs from $x=y$ (the line) to $x=\\sqrt y$ (the parabola). Washers: outer radius $\\sqrt y$, inner radius $y$. $V=\\pi\\int_0^1\\left(y-y^2\\right)dy=\\pi\\left(\\frac12-\\frac13\\right)=\\frac\\pi6$."),
      [ch(pi / 30, "This squares the difference of the radii, $(\\sqrt y-y)^2$. A washer's area is the difference of the squares: $(\\sqrt y)^2-y^2$."),
       ch(pi / 2, "This is the volume of the full disk of radius $\\sqrt y$, with no hole removed."),
       ch(-pi / 6, "This swaps the outer and inner radii. The outer radius is the one farther from the axis, $\\sqrt y$ (since $\\sqrt y\\ge y$ on $[0,1]$), and volumes are not negative.")],
      "When rotating about the $y$-axis with washers, the radii are $x$-values written in terms of $y$.")

# 9. setting up (no evaluating)
B.mcq(T_DW, "The region bounded by $y=e^x$, $y=1$, $x=0$ and $x=1$ is rotated about the line $y=-2$. Which integral gives the volume of the solid generated?",
      ch("$\\pi\\displaystyle\\int_0^1\\left[(e^x+2)^2-3^2\\right]dx$", "Outer radius: distance from $y=-2$ to $y=e^x$, which is $e^x+2$. Inner radius: distance from $y=-2$ to $y=1$, which is 3."),
      [ch("$\\pi\\displaystyle\\int_0^1\\left[(e^x-2)^2-(1-2)^2\\right]dx$", "This uses $e^x-2$ and $1-2$, as if the axis were $y=2$. Distances to $y=-2$ are $y-(-2)=y+2$."),
       ch("$\\pi\\displaystyle\\int_0^1\\left[(e^x+2)^2-1^2\\right]dx$", "The inner radius is the distance from the axis $y=-2$ to the line $y=1$, which is 3, not 1."),
       ch("$\\pi\\displaystyle\\int_0^1\\left(e^x+2-3\\right)^2dx$", "This squares the difference of the radii. For a washer, subtract the squares: $R^2-r^2$.")],
      "Washer method about a horizontal line: $V=\\pi\\int(R^2-r^2)\\,dx$ with $R$ and $r$ the distances from the axis to the outer and inner boundaries.")

# 10. average value of a derivative
B.mcq(T_AVG, "The function $f$ is differentiable on $[1,4]$ with $f(1)=3$ and $f(4)=9$. What is the average value of $f'(x)$ on the interval $[1,4]$?",
      ch(2, "Average value of $f'$ is $\\frac{1}{4-1}\\int_1^4f'(x)\\,dx=\\frac{f(4)-f(1)}{3}=\\frac{9-3}{3}=2$ by the Fundamental Theorem."),
      [ch(6, "6 is $\\int_1^4f'(x)\\,dx=f(4)-f(1)$, the total change. The average value divides by the length of the interval, 3."),
       ch(Rational(3, 2), "This divides by 4, the right endpoint, instead of by the interval length $4-1=3$."),
       ch(12, "This adds the function values. The average value of $f'$ depends on the net change in $f$, which is a difference.")],
      "The average value of a derivative over an interval is the average rate of change of the function.")

# 11. area between sine and cosine
area = integrate(cos(x) - sin(x), (x, 0, pi / 4)) + integrate(sin(x) - cos(x), (x, pi / 4, pi / 2))
assert simplify(area - 2 * (sqrt(2) - 1)) == 0
assert integrate(cos(x) - sin(x), (x, 0, pi / 2)) == 0
B.mcq(T_AREA, "What is the area of the region bounded by the graphs of $y=\\sin x$ and $y=\\cos x$ and the lines $x=0$ and $x=\\frac\\pi2$?",
      ch("$2\\left(\\sqrt2-1\\right)$", "The graphs cross at $x=\\frac\\pi4$. $\\cos x\\ge\\sin x$ on $[0,\\frac\\pi4]$ and $\\sin x\\ge\\cos x$ on $[\\frac\\pi4,\\frac\\pi2]$. Area $=\\int_0^{\\pi/4}(\\cos x-\\sin x)dx+\\int_{\\pi/4}^{\\pi/2}(\\sin x-\\cos x)dx=(\\sqrt2-1)+(\\sqrt2-1)$."),
      [ch(0, "$\\int_0^{\\pi/2}(\\cos x-\\sin x)\\,dx=0$ because the two pieces have equal area but opposite sign. Area counts both pieces as positive."),
       ch("$\\sqrt2-1$", "This is the area of only one of the two pieces. There is a second, equal piece on $[\\frac\\pi4,\\frac\\pi2]$."),
       ch("$2$", "This is $\\int_0^{\\pi/2}(\\sin x+\\cos x)\\,dx$, the sum instead of the distance between the curves.")],
      "Find where the curves cross, decide which is on top on each part, and integrate (top $-$ bottom) on each part.")

# 12. average speed vs average velocity
v = t**2 - 6 * t + 8
avg_vel = integrate(v, (t, 0, 4)) / 4
dist = integrate(v, (t, 0, 2)) - integrate(v, (t, 2, 4))
assert avg_vel == Rational(4, 3) and dist == 8
B.mcq(T_AVG, "A particle moves along a line with velocity $v(t)=t^2-6t+8$ for $0\\le t\\le4$. What is the average speed of the particle over this interval?",
      ch(2, "$v=(t-2)(t-4)$ is positive on $[0,2)$ and negative on $(2,4]$. Total distance $=\\int_0^2v\\,dt-\\int_2^4v\\,dt=\\frac{20}{3}+\\frac43=8$. Average speed $=\\frac{8}{4}=2$."),
      [ch(Rational(4, 3), "This is the average velocity $\\frac14\\int_0^4v\\,dt=\\frac{16/3}{4}$, which lets the backward motion subtract. Speed is $|v|$."),
       ch(8, "8 is the total distance traveled. The average speed divides by the elapsed time, 4."),
       ch(Rational(16, 3), "$\\int_0^4v\\,dt=\\frac{16}{3}$ is the net displacement, not an average speed.")],
      "Average speed is $\\frac{1}{b-a}\\int_a^b|v(t)|\\,dt$. Split the interval where $v$ changes sign.")

# 13. area enclosed by a cubic and a line
area = 2 * integrate(4 * x - x**3, (x, 0, 2))
assert area == 8
B.mcq(T_AREA, "What is the area of the region enclosed by the graphs of $y=x^3$ and $y=4x$?",
      ch(8, "The graphs meet where $x^3=4x$: $x=-2,0,2$. The region is symmetric about the origin, so the area is $2\\int_0^2(4x-x^3)\\,dx=2\\left[2x^2-\\frac{x^4}{4}\\right]_0^2=2(8-4)=8$."),
      [ch(0, "$\\int_{-2}^2(4x-x^3)\\,dx=0$ because the function is odd. Area uses the positive vertical distance on each piece."),
       ch(4, "This is the area of one lobe, on $[0,2]$. A second lobe of equal size lies on $[-2,0]$."),
       ch(16, "This doubles the total. The area of each lobe is 4, and there are two lobes.")],
      "Find all intersections, and treat the two lobes separately, since the top and bottom curves swap at $x=0$.")

# 14. semicircle cross-sections
V = pi / 8 * integrate((2 * x - x**2) ** 2, (x, 0, 2))
assert simplify(V - 2 * pi / 15) == 0
B.mcq(T_XS, "The base of a solid is the region between $y=x^2$ and $y=2x$. Cross-sections perpendicular to the $x$-axis are semicircles whose diameters lie in the base. What is the volume of the solid?",
      ch("$\\dfrac{2\\pi}{15}$", "The curves meet at $x=0$ and $x=2$. The diameter at $x$ is $d=2x-x^2$, so the radius is $\\frac d2$ and the semicircle's area is $\\frac12\\pi\\left(\\frac d2\\right)^2=\\frac\\pi8d^2$. $V=\\frac\\pi8\\int_0^2(2x-x^2)^2dx=\\frac\\pi8\\cdot\\frac{16}{15}=\\frac{2\\pi}{15}$."),
      [ch("$\\dfrac{16\\pi}{15}$", "This uses area $\\pi d^2$, a full circle with radius $d$, instead of $\\frac\\pi8d^2$."),
       ch("$\\dfrac{8\\pi}{15}$", "This uses $\\frac\\pi2d^2$, treating the diameter as the radius of a semicircle."),
       ch("$\\dfrac{4\\pi}{15}$", "This uses $\\frac\\pi4d^2$, the area of a full circle with diameter $d$. A semicircle has half of that.")],
      "The area of a semicircle with diameter $d$ is $\\frac12\\pi\\left(\\frac d2\\right)^2=\\frac{\\pi d^2}8$.")

# 15. washer about the x-axis between two curves
V = pi * integrate((2 * x) ** 2 - (x**2) ** 2, (x, 0, 2))
assert simplify(V - 64 * pi / 15) == 0
B.mcq(T_DW, "The region bounded by $y=2x$ and $y=x^2$ is rotated about the $x$-axis. What is the volume of the solid generated?",
      ch("$\\dfrac{64\\pi}{15}$", "The graphs meet at $x=0$ and $x=2$, with $2x\\ge x^2$ between. Washers: outer radius $2x$, inner radius $x^2$. $V=\\pi\\int_0^2\\left[(2x)^2-(x^2)^2\\right]dx=\\pi\\left[\\frac{4x^3}{3}-\\frac{x^5}{5}\\right]_0^2=\\pi\\left(\\frac{32}{3}-\\frac{32}{5}\\right)=\\frac{64\\pi}{15}$."),
      [ch("$\\dfrac{16\\pi}{15}$", "This squares the difference of the radii, $(2x-x^2)^2$. Subtract the squares instead: $(2x)^2-(x^2)^2$."),
       ch("$\\dfrac{32\\pi}{3}$", "This is the volume of the full solid made by $y=2x$ alone, with no hole removed."),
       ch("$\\dfrac{32\\pi}{5}$", "This is the volume generated by $y=x^2$ alone, which is the volume of the hole, not of the solid.")],
      "Subtract the inner volume from the outer volume: $\\pi\\int(R^2-r^2)\\,dx$.")

# ------------------------------------------------------------------ FRQs
top, bot = 6 - x, x**2
inter = solve(Eq(top, bot), x)
assert sorted(inter) == [-3, 2]
area = integrate(top - bot, (x, 0, 2))
assert area == Rational(22, 3)
vsq = integrate((top - bot) ** 2, (x, 0, 2))
vrot = pi * integrate(top**2 - bot**2, (x, 0, 2))
avg = area / 2
assert avg == Rational(11, 3)
vsq_s, vrot_s = latex(vsq), latex(vrot)
B.frq(T_AREA,
      "Let $R$ be the region in the first quadrant bounded by the graphs of $y=x^2$ and $y=6-x$ and the $y$-axis.\n\n**(a)** Find the $x$-coordinate of the point where the two graphs intersect, and find the area of $R$.\n\n**(b)** The region $R$ is the base of a solid. Cross-sections of the solid perpendicular to the $x$-axis are squares. Write an integral expression for the volume of the solid, and find its value.\n\n**(c)** Region $R$ is rotated about the $x$-axis. Write an integral expression for the volume of the solid, and find its value.\n\n**(d)** Find the average value of the vertical distance between the two graphs, $(6-x)-x^2$, on the interval $0\\le x\\le2$.",
      [(1, "(a) Solves $x^2=6-x$ to get $x=2$ (rejecting $x=-3$)"),
       (1, "(a) Computes the area $\\int_0^2(6-x-x^2)\\,dx=\\frac{22}3$"),
       (1, "(b) Writes $\\int_0^2(6-x-x^2)^2\\,dx$"),
       (1, "(b) Evaluates it correctly"),
       (1, "(c) Writes a washer integral with outer radius $6-x$ and inner radius $x^2$: $\\pi\\int_0^2\\left[(6-x)^2-(x^2)^2\\right]dx$"),
       (1, "(c) Evaluates it correctly"),
       (1, "(d) Uses the average value formula $\\frac1{2-0}\\int_0^2(6-x-x^2)\\,dx=\\frac{11}{3}$")],
      "(a) $x^2=6-x$ gives $x^2+x-6=(x+3)(x-2)=0$; in the first quadrant $x=2$. Area $=\\int_0^2(6-x-x^2)\\,dx=\\left[6x-\\frac{x^2}2-\\frac{x^3}3\\right]_0^2=12-2-\\frac83=\\frac{22}3$.\n(b) The side of each square is the vertical distance $6-x-x^2$, so $V=\\int_0^2(6-x-x^2)^2\\,dx=" + vsq_s + "$.\n(c) On $[0,2]$, $6-x\\ge x^2$. Using washers, $V=\\pi\\int_0^2\\left[(6-x)^2-(x^2)^2\\right]dx=" + vrot_s + "$.\n(d) Average value $=\\frac{1}{2}\\int_0^2(6-x-x^2)\\,dx=\\frac12\\cdot\\frac{22}{3}=\\frac{11}3$.")

F = 12 * t - t**2
tot = integrate(F, (t, 0, 12))
assert tot == 288 and 10 + tot == 298
assert integrate(F, (t, 0, 6)) == 144
avg = tot / 12
assert avg == 24
sol = solve(Eq(F, 24), t)
assert sorted(sol) == [6 - 2 * sqrt(3), 6 + 2 * sqrt(3)]
B.frq(T_AVG,
      "Water is pumped into a tank at a rate of $F(t)=12t-t^2$ cubic feet per hour for $0\\le t\\le12$, where $t$ is measured in hours. The tank contains 10 cubic feet of water at time $t=0$.\n\n**(a)** How much water is in the tank at $t=12$? Show the work that leads to your answer.\n\n**(b)** Find the average rate at which water is pumped into the tank over the 12 hours.\n\n**(c)** At what time $t$ is the pumping rate greatest? What is the greatest rate?\n\n**(d)** Find the amount of water in the tank at $t=6$.\n\n**(e)** Find all times $t$ in $(0,12)$ at which the pumping rate equals the average rate from part (b).",
      [(1, "(a) Sets up $10+\\int_0^{12}(12t-t^2)\\,dt$"),
       (1, "(a) Evaluates to 298 cubic feet"),
       (1, "(b) Uses $\\frac1{12}\\int_0^{12}F(t)\\,dt$"),
       (1, "(b) Gets 24 cubic feet per hour"),
       (1, "(c) Finds $F'(t)=12-2t=0$ at $t=6$ and $F(6)=36$, with justification of a maximum"),
       (1, "(d) Computes $10+\\int_0^6F(t)\\,dt=154$ cubic feet"),
       (1, "(e) Solves $12t-t^2=24$ to get $t=6\\pm2\\sqrt3$, and confirms both are in $(0,12)$")],
      "(a) Amount $=10+\\int_0^{12}(12t-t^2)\\,dt=10+\\left[6t^2-\\frac{t^3}3\\right]_0^{12}=10+(864-576)=298$ cubic feet.\n(b) Average rate $=\\frac1{12}\\int_0^{12}F(t)\\,dt=\\frac{288}{12}=24$ cubic feet per hour.\n(c) $F'(t)=12-2t=0$ at $t=6$. $F'$ changes from positive to negative there (and $F(0)=F(12)=0$), so the maximum rate occurs at $t=6$. $F(6)=72-36=36$ cubic feet per hour.\n(d) Amount at $t=6$: $10+\\int_0^6(12t-t^2)\\,dt=10+\\left[6t^2-\\frac{t^3}3\\right]_0^6=10+(216-72)=154$ cubic feet.\n(e) $12t-t^2=24$ gives $t^2-12t+24=0$, so $t=\\frac{12\\pm\\sqrt{144-96}}{2}=6\\pm2\\sqrt3$. Both are in $(0,12)$ since $2\\sqrt3\\approx3.46$.")

B.save()
B.show()
