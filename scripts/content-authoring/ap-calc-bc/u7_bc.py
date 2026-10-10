"""Unit 7, BC-only topics: Euler's method and logistic models.
Writes content/ap-calc-bc/{questions,frqs}/unit-7-bc.json."""
from lib import *

B = Bank(7, "unit-7-differential-equations")
T_EU, T_LOG = "eulers-method", "logistic-models"
R = Rational


def euler(f, x0, y0, h, steps):
    """Euler's method with exact rational arithmetic: the list of (x, y) points, starting with (x0, y0)."""
    pts = [(sympify(x0), sympify(y0))]
    for _ in range(steps):
        xx, yy = pts[-1]
        pts.append((expand(xx + sympify(h)), expand(yy + sympify(h) * f(xx, yy))))
    return pts


def dec(v):
    """A short decimal for a rational value that is exactly representable (the problems are built so they are)."""
    s = f"{float(v):.6f}".rstrip("0").rstrip(".")
    return s


def D(v):
    return "$" + dec(v) + "$"


# ---------------------------------------------------------------- Euler's method
p = euler(lambda xx, yy: xx + yy, 0, 1, R(1, 2), 2)
assert p[-1] == (1, R(5, 2)) and p[1][1] == R(3, 2)
one_step = euler(lambda xx, yy: xx + yy, 0, 1, 1, 1)[-1][1]
no_h = 1 + (0 + 1)
no_h2 = no_h + (R(1, 2) + no_h)
assert (one_step, no_h2) == (2, R(9, 2))
B.mcq(T_EU, "Let $\\dfrac{dy}{dx}=x+y$ with $y(0)=1$. Euler's method with two steps of equal size is used to approximate $y(1)$. What is the approximation?",
      ch(D(p[-1][1]), "The step size is $\\Delta x=0.5$. At $(0,1)$ the slope is $0+1=1$, so $y(0.5)\\approx1+0.5(1)=1.5$. At $(0.5,1.5)$ the slope is $0.5+1.5=2$, so $y(1)\\approx1.5+0.5(2)=2.5$."),
      [ch(D(p[1][1]), "This is the value after one step, the approximation of $y(0.5)$. Two steps are needed to reach $x=1$."),
       ch(D(one_step), "This takes a single step of size 1, but the problem uses two steps of equal size, each of size 0.5."),
       ch(D(no_h2), "The slope has to be multiplied by the step size each time: $y_{n+1}=y_n+\\Delta x\\cdot f(x_n,y_n)$. This adds the slopes themselves.")],
      "Euler's method repeats $y_{\\text{new}}=y_{\\text{old}}+\\Delta x\\cdot\\frac{dy}{dx}$, with the slope computed at the old point, moving one step at a time from the initial condition.",
      difficulty="easy")

q = euler(lambda xx, yy: 2 * yy, 0, 3, R(1, 10), 1)[-1][1]
assert q == R(18, 5)
B.mcq(T_EU, "Let $\\dfrac{dy}{dx}=2y$ with $y(0)=3$. Using Euler's method with one step of size 0.1, what is the approximation of $y(0.1)$?",
      ch(D(q), "The slope at $(0,3)$ is $2(3)=6$, so $y(0.1)\\approx3+0.1(6)=3.6$."),
      [ch(D(3 + R(1, 10) * 2), "The slope is $2y=2(3)=6$, not 2. The right side depends on $y$."),
       ch(D(3 + 6), "The slope has to be multiplied by the step size: $3+0.1\\cdot6$, not $3+6$."),
       ch(D(3 + R(1, 10) * 3), "This uses $y$ as the slope. The differential equation says the slope is $2y$.")],
      "Evaluate the right-hand side at the initial point to get the slope, then move one step along that tangent line.",
      difficulty="easy")

p = euler(lambda xx, yy: xx**2 - yy, 1, 2, R(1, 2), 2)
assert p[-1] == (2, R(15, 8))
stuck = euler(lambda xx, yy: 1 - yy, 1, 2, R(1, 2), 2)[-1][1]  # x never advances: slope uses x = 1 each time
single = euler(lambda xx, yy: xx**2 - yy, 1, 2, 1, 1)[-1][1]
assert (p[1][1], stuck, single) == (R(3, 2), R(5, 4), 1)
B.mcq(T_EU, "Let $\\dfrac{dy}{dx}=x^2-y$ with $y(1)=2$. Euler's method with a step size of $0.5$ is used to approximate $y(2)$. What is the approximation?",
      ch(D(p[-1][1]), "At $(1,2)$ the slope is $1-2=-1$, so $y(1.5)\\approx2+0.5(-1)=1.5$. At $(1.5,1.5)$ the slope is $2.25-1.5=0.75$, so $y(2)\\approx1.5+0.5(0.75)=1.875$."),
      [ch(D(p[1][1]), "This is the approximation of $y(1.5)$, after one step. Going from $x=1$ to $x=2$ with $\\Delta x=0.5$ takes two steps."),
       ch(D(stuck), "In the second step the slope must use the new point $(1.5,1.5)$. Using $x=1$ again gives the wrong slope."),
       ch(D(single), "This takes one step of size 1. The problem asks for steps of size 0.5.")],
      "Each step uses the slope at the point you are leaving. Keep track of both coordinates: $x$ goes up by $\\Delta x$ and $y$ by $\\Delta x\\cdot\\frac{dy}{dx}$.",
      difficulty="medium")

q = euler(lambda xx, yy: yy, 0, 1, R(1, 2), 2)[-1][1]
assert q == R(9, 4) and q < E
B.mcq(T_EU, "Let $\\dfrac{dy}{dx}=y$ with $y(0)=1$, whose solution is $y=e^x$. Euler's method with a step size of $0.5$ is used to approximate $y(1)$. Which statement is true?",
      ch("The approximation is $2.25$, which is less than $y(1)$, because the solution is concave up", "Two steps: $y(0.5)\\approx1.5$ and $y(1)\\approx1.5+0.5(1.5)=2.25$. The true value is $e\\approx2.718$. Since $y''=y>0$, the solution is concave up, so each tangent line lies below the curve and the approximation is too small."),
      [ch("The approximation is $2.25$, which is greater than $y(1)$, because the solution is concave up", "Tangent lines to a concave-up curve lie below it, so the approximation is smaller than the true value, not greater."),
       ch("The approximation is $2$, which is less than $y(1)$, because the solution is concave up", "This takes one step of size 1. With two steps of size 0.5 the approximation is $2.25$."),
       ch("The approximation is $2.25$, which equals $y(1)$, because Euler's method is exact when the slope is $y$", "Euler's method follows tangent lines, which agree with the curve only at the starting point of each step. For $y=e^x$ the true value is $e$, not $2.25$.")],
      "To decide over- or underestimate, find the concavity of the solution: with $y''>0$ tangent lines lie below the curve, and with $y''<0$ they lie above it.",
      difficulty="medium")

p = euler(lambda xx, yy: xx * yy / 2, 0, 2, 1, 3)
assert p[-1][1] == 6
early = p[2][1]
right_end = euler(lambda xx, yy: (xx + 1) * yy / 2, 0, 2, 1, 3)[-1][1]  # slope taken at the right endpoint's x
drop_half = euler(lambda xx, yy: xx * yy, 0, 2, 1, 3)[-1][1]
assert (early, right_end, drop_half) == (3, 15, 12)
B.mcq(T_EU, "Let $\\dfrac{dy}{dx}=\\dfrac{xy}{2}$ with $y(0)=2$. Euler's method with a step size of 1 is used to approximate $y(3)$. What is the approximation?",
      ch(D(p[-1][1]), "Step 1: slope at $(0,2)$ is $0$, so $y(1)\\approx2$. Step 2: slope at $(1,2)$ is $1$, so $y(2)\\approx3$. Step 3: slope at $(2,3)$ is $3$, so $y(3)\\approx3+3=6$."),
      [ch(D(early), "This is the approximation of $y(2)$. Reaching $x=3$ with steps of size 1 takes three steps."),
       ch(D(drop_half), "The slope is $\\frac{xy}{2}$. Dropping the factor $\\frac12$ doubles every slope after the first step."),
       ch(D(right_end), "The slope must come from the point where the step starts, $(x_n,y_n)$, not from the point where it ends.")],
      "Make a small table of $x$, $y$ and the slope $\\frac{xy}{2}$, and fill it in one row at a time.",
      difficulty="medium")

# k such that two steps of size 1 give y(2) = 9 for dy/dx = x + y, y(0) = k
kk = symbols("kk")
sol = solve(Eq(euler(lambda xx, yy: xx + yy, 0, kk, 1, 2)[-1][1], 9), kk)
assert sol == [2]
B.mcq(T_EU, "Let $\\dfrac{dy}{dx}=x+y$ with $y(0)=k$. Euler's method with two steps of size 1 gives the approximation $y(2)\\approx9$. What is $k$?",
      ch(2, "The slope at $(0,k)$ is $k$, so $y(1)\\approx k+k=2k$. The slope at $(1,2k)$ is $1+2k$, so $y(2)\\approx2k+(1+2k)=4k+1$. Setting $4k+1=9$ gives $k=2$."),
      [ch(R(9, 2), "This uses only the first step ($2k=9$). Two steps are used."),
       ch(R(9, 4), "In the second step the slope is $x+y=1+2k$. This leaves out the $x=1$, giving $4k=9$."),
       ch(R(5, 4), "In the first step the slope is evaluated at $x=0$, giving $k$. Using $x=1$ there as well gives $4k+4=9$.")],
      "Work forward symbolically: write $y(1)$ in terms of $k$, then $y(2)$, and solve the resulting equation.",
      difficulty="hard")

p = euler(lambda xx, yy: 2 - yy, 0, 0, 1, 2)
assert p[-1][1] == 2 and 2 * (1 - exp(-2)) < 2
stale = euler(lambda xx, yy: 2, 0, 0, 1, 2)[-1][1]
assert stale == 4
B.mcq(T_EU, "Let $\\dfrac{dy}{dx}=2-y$ with $y(0)=0$, whose solution is $y=2\\left(1-e^{-x}\\right)$. Euler's method with a step size of 1 is used to approximate $y(2)$. Which statement is true?",
      ch("The approximation is $2$, which is greater than $y(2)$, because the solution is concave down", "Step 1: slope $2-0=2$, so $y(1)\\approx2$. Step 2: slope $2-2=0$, so $y(2)\\approx2$. The true value is $2(1-e^{-2})\\approx1.73$. The solution has $y''=-e^{-x}\\cdot2<0$, so it is concave down and tangent lines lie above it."),
      [ch("The approximation is $2$, which is less than $y(2)$, because the solution is concave down", "Tangent lines to a concave-down curve lie above it, so the approximation is greater than the true value, not less."),
       ch("The approximation is $4$, which is greater than $y(2)$, because the slope stays at 2", "The slope has to be recomputed at each new point. At $(1,2)$ it is $2-2=0$, not 2."),
       ch("The approximation is $2$, which equals $y(2)$, because the solution levels off at $y=2$", "The solution approaches 2 as $x\\to\\infty$ but never reaches it: $y(2)=2(1-e^{-2})\\approx1.73$.")],
      "Check the sign of $y''$ along the solution. When $y$ rises toward a horizontal asymptote it is concave down, so Euler's method overshoots.",
      difficulty="hard")

# ---------------------------------------------------------------- logistic models
B.mcq(T_LOG, "A population satisfies $\\dfrac{dP}{dt}=0.2P\\left(1-\\dfrac{P}{500}\\right)$. What is the carrying capacity?",
      ch(500, "The growth rate is zero when $1-\\frac{P}{500}=0$, that is, at $P=500$. For $0<P<500$ the population increases toward it."),
      [ch(D(R(1, 5)), "0.2 is the growth-rate constant. It is not a population size."),
       ch(100, "This multiplies $0.2\\times500$. The carrying capacity is the value of $P$ where $\\frac{dP}{dt}=0$, which is 500."),
       ch(250, "250 is the population at which growth is fastest, half the carrying capacity.")],
      "In $\\frac{dP}{dt}=kP\\left(1-\\frac PK\\right)$, the constant $K$ is the carrying capacity.",
      difficulty="easy")

B.mcq(T_LOG, "A population satisfies $\\dfrac{dP}{dt}=0.1P\\left(1-\\dfrac{P}{800}\\right)$. At what population size is the growth rate $\\dfrac{dP}{dt}$ greatest?",
      ch(400, "$\\frac{dP}{dt}$ as a function of $P$ is the parabola $0.1P-\\frac{P^2}{8000}$, whose maximum is halfway between its zeros 0 and 800, at $P=400$."),
      [ch(800, "At $P=800$ the population has reached its carrying capacity and $\\frac{dP}{dt}=0$."),
       ch(80, "This is $0.1\\times800$, which has no meaning here."),
       ch(0, "At $P=0$ the growth rate is 0: there is no population to grow.")],
      "Treat the right-hand side as a function of $P$. It is a downward parabola with zeros at $P=0$ and $P=K$, so its vertex is at $P=\\frac K2$.",
      difficulty="easy")

B.mcq(T_LOG, "A population satisfies $\\dfrac{dy}{dt}=0.3y\\left(1-\\dfrac{y}{12}\\right)$ with $y(0)=20$. What is $\\displaystyle\\lim_{t\\to\\infty}y(t)$?",
      ch(12, "Since $y(0)=20>12$, the factor $1-\\frac{y}{12}$ is negative, so $y$ decreases. It approaches the equilibrium $y=12$ from above."),
      [ch(20, "The initial value is not a limit: $\\frac{dy}{dt}=0.3(20)\\left(1-\\frac{20}{12}\\right)\\ne0$, so $y$ is changing at $t=0$."),
       ch("The limit does not exist because $y$ grows without bound", "Growth without bound would need $\\frac{dy}{dt}>0$ for large $y$. For $y>12$ the derivative is negative."),
       ch(0, "$y=0$ is also an equilibrium, but it is unstable: with $y(0)=20$ the solution moves away from 0.")],
      "Identify the equilibria ($y=0$ and $y=12$) and use the sign of $\\frac{dy}{dt}$ at the starting value to see which one the solution approaches.",
      difficulty="medium")

B.mcq(T_LOG, "A population satisfies $\\dfrac{dP}{dt}=0.04P(100-P)$ with $P(0)=10$. What is the carrying capacity?",
      ch(100, "The growth rate is 0 when $100-P=0$, so $P=100$ is the carrying capacity. Written as $4P\\left(1-\\frac{P}{100}\\right)$ the same equation shows $K=100$."),
      [ch(4, "$4=0.04\\times100$ is the constant $k$ in the form $kP\\left(1-\\frac PK\\right)$, not the carrying capacity."),
       ch(D(R(1, 25)), "0.04 is the constant in front of the product $P(100-P)$, not a population size."),
       ch(10, "10 is the initial population. The population keeps growing past it.")],
      "Find where the right-hand side equals zero for $P>0$. The same logistic equation can be written $kP(K-P)$ or $kP\\left(1-\\frac PK\\right)$.",
      difficulty="medium")

rate = R(1, 2) * 40 * (1 - R(40, 200))
assert rate == 16
B.mcq(T_LOG, "A population satisfies $\\dfrac{dP}{dt}=0.5P\\left(1-\\dfrac{P}{200}\\right)$. What is the rate of change of the population when $P=40$?",
      ch(16, "$\\frac{dP}{dt}=0.5(40)\\left(1-\\frac{40}{200}\\right)=20(0.8)=16$."),
      [ch(20, "This is $0.5P$ with no logistic factor. The factor $1-\\frac{P}{200}=0.8$ slows the growth."),
       ch(D(R(2, 5)), "This drops the factor $P$: $0.5(0.8)=0.4$."),
       ch(4, "This uses $\\frac{P}{200}=0.2$ in place of $1-\\frac{P}{200}=0.8$: $20(0.2)=4$.")],
      "Substitute $P=40$ into the right-hand side and compute.",
      difficulty="medium")

fP = R(1, 10) * x - x**2 / 600
assert simplify(fP - R(1, 10) * x * (1 - x / 60)) == 0
fp = diff(fP, x)
second = factor(fp * fP)
up = [r_ for r_ in (30, 60)]  # sign changes of P'' = f'(P) f(P) at P = 30 and P = 60
assert fP.subs(x, 10) > 0 and fp.subs(x, 10) > 0           # 0 < P < 30  -> concave up
assert fP.subs(x, 45) > 0 and fp.subs(x, 45) < 0           # 30 < P < 60 -> concave down
assert fP.subs(x, 80) < 0 and fp.subs(x, 80) < 0           # P > 60      -> concave up
B.mcq(T_LOG, "A population satisfies $\\dfrac{dP}{dt}=0.1P\\left(1-\\dfrac{P}{60}\\right)$. For which values of $P$ is the graph of the solution $P(t)$ concave up?",
      ch("$0<P<30$ and $P>60$", "Differentiate with respect to $t$: $\\frac{d^2P}{dt^2}=f'(P)\\cdot f(P)$ with $f(P)=0.1P-\\frac{P^2}{600}$ and $f'(P)=0.1-\\frac{P}{300}$. For $0<P<30$ both factors are positive. For $30<P<60$ only $f$ is positive. For $P>60$ both are negative, so the product is positive again."),
      [ch("$0<P<30$", "This is the region where the population is growing faster and faster. A solution that starts above the carrying capacity ($P>60$) decreases, and its graph is also concave up."),
       ch("$30<P<60$", "In this region the population is still increasing but its growth is slowing, so the graph is concave down."),
       ch("$0<P<60$", "This is where $P$ is increasing. Increasing and concave up are different: concavity depends on the sign of $\\frac{d^2P}{dt^2}$.")],
      "Concavity is the sign of $\\frac{d^2P}{dt^2}=\\frac{d}{dt}\\left[f(P)\\right]=f'(P)\\frac{dP}{dt}=f'(P)f(P)$. Use a sign chart on $P$.",
      difficulty="hard")

Pt = 500 / (1 + 4 * exp(-R(1, 5) * t))
assert simplify(diff(Pt, t) - R(1, 5) * Pt * (1 - Pt / 500)) == 0 and Pt.subs(t, 0) == 100
bad1 = 500 / (1 + 5 * exp(-R(1, 5) * t))
bad2 = 500 / (1 + 4 * exp(R(1, 5) * t))
bad3 = 500 / (1 + exp(-R(1, 5) * t) / 4)
assert bad1.subs(t, 0) != 100 and bad3.subs(t, 0) != 100
assert simplify(diff(bad2, t) - R(1, 5) * bad2 * (1 - bad2 / 500)) != 0
B.mcq(T_LOG, "The population $P(t)$ satisfies $\\dfrac{dP}{dt}=0.2P\\left(1-\\dfrac{P}{500}\\right)$ with $P(0)=100$. Which is $P(t)$?",
      chv("\\dfrac{500}{1+4e^{-0.2t}}", "The logistic solution has the form $\\frac{K}{1+Ae^{-kt}}$ with $K=500$, $k=0.2$ and $A=\\frac{K-P_0}{P_0}=\\frac{400}{100}=4$. Check: $P(0)=\\frac{500}{5}=100$ and $P\\to500$.", Pt),
      [chv("\\dfrac{500}{1+5e^{-0.2t}}", "This takes $A=\\frac{K}{P_0}=5$. Then $P(0)=\\frac{500}{6}\\approx83.3$, not 100. The constant is $\\frac{K-P_0}{P_0}$.", bad1),
       chv("\\dfrac{500}{1+4e^{0.2t}}", "With $e^{+0.2t}$ the denominator grows, so $P\\to0$. The population in this model increases toward 500, which needs $e^{-0.2t}$.", bad2),
       chv("\\dfrac{500}{1+\\frac14e^{-0.2t}}", "This inverts the constant: $P(0)=\\frac{500}{1.25}=400$, not 100.", bad3)],
      "Use the standard logistic solution $P(t)=\\frac{K}{1+Ae^{-kt}}$ and fit $A$ to the initial condition: $A=\\frac{K-P(0)}{P(0)}$.",
      difficulty="hard")

B.mcq(T_LOG, "A population has a carrying capacity of 1200. When the population is small, it grows at a rate approximately proportional to its size, with $\\dfrac{dP}{dt}\\approx0.3P$. Which differential equation models this?",
      ch("$\\dfrac{dP}{dt}=0.3P\\left(1-\\dfrac{P}{1200}\\right)$", "For small $P$ the factor $1-\\frac{P}{1200}$ is close to 1, so $\\frac{dP}{dt}\\approx0.3P$. It equals 0 at $P=1200$."),
      [ch("$\\dfrac{dP}{dt}=0.3P(1200-P)$", "This is zero at $P=1200$, but for small $P$ it is about $0.3(1200)P=360P$, not $0.3P$."),
       ch("$\\dfrac{dP}{dt}=0.3\\left(1-\\dfrac{P}{1200}\\right)$", "Without the factor $P$ the growth is about 0.3 per unit time for small $P$, not proportional to $P$."),
       ch("$\\dfrac{dP}{dt}=0.3P\\left(1+\\dfrac{P}{1200}\\right)$", "The factor $1+\\frac{P}{1200}$ increases with $P$, so growth speeds up with no limit. It never reaches zero for positive $P$.")],
      "A logistic equation is exponential growth multiplied by a factor that falls to zero at the carrying capacity.",
      difficulty="medium")

# ---------------------------------------------------------------- free response
pts = euler(lambda xx, yy: xx / yy, 1, 2, R(1, 2), 2)
assert pts[1][1] == R(9, 4) and pts[2][1] == R(31, 12)
ysq = lambda xx: sqrt(xx**2 + 3)
assert simplify(diff(ysq(x), x) - x / ysq(x)) == 0 and ysq(1) == 2
ypp = simplify(diff(x / y, x) + diff(x / y, y) * x / y)
assert simplify(ypp - (y**2 - x**2) / y**3) == 0
assert simplify(ypp.subs(y, ysq(x)) - 3 / ysq(x) ** 3) == 0
assert float(R(31, 12)) < float(ysq(2))
B.frq(T_EU,
      "Consider the differential equation $\\dfrac{dy}{dx}=\\dfrac{x}{y}$ with the initial condition $y(1)=2$.\n\n**(a)** Use Euler's method, starting at $x=1$ with two steps of equal size, to approximate $y(2)$. Show the work that leads to your answer.\n\n**(b)** Find the particular solution $y=f(x)$ to the differential equation with $y(1)=2$.\n\n**(c)** Find $\\dfrac{d^2y}{dx^2}$ in terms of $x$ and $y$. Use it, together with your answer to part (b), to determine whether your approximation in part (a) is less than or greater than $f(2)$. Give a reason for your answer.",
      [(1, "(a) Step size 0.5; slope at $(1,2)$ is $\\frac12$, giving $y(1.5)\\approx2.25$"),
       (1, "(a) Slope at $(1.5,2.25)$ is $\\frac{1.5}{2.25}=\\frac23$"),
       (1, "(a) $y(2)\\approx2.25+0.5\\cdot\\frac23=\\frac{31}{12}\\approx2.583$"),
       (1, "(b) Separates the variables: $y\\,dy=x\\,dx$"),
       (1, "(b) Antidifferentiates both sides and includes a constant: $\\frac{y^2}{2}=\\frac{x^2}{2}+C$"),
       (1, "(b) Uses $y(1)=2$ to get $C=\\frac32$ and gives $y=\\sqrt{x^2+3}$ (positive root)"),
       (1, "(c) Differentiates $\\frac xy$ with the quotient rule and substitutes $\\frac{dy}{dx}=\\frac xy$"),
       (1, "(c) $\\frac{d^2y}{dx^2}=\\frac{y^2-x^2}{y^3}$ (equivalent forms accepted)"),
       (1, "(c) Concludes the approximation is less than $f(2)$ because the solution is concave up ($y^2-x^2=3>0$ and $y>0$ along the solution, so $y''>0$)")],
      "(a) $\\Delta x=0.5$. At $(1,2)$: $\\frac{dy}{dx}=\\frac12$, so $y(1.5)\\approx2+0.5\\cdot\\frac12=2.25$. At $(1.5,2.25)$: $\\frac{dy}{dx}=\\frac{1.5}{2.25}=\\frac23$, so $y(2)\\approx2.25+0.5\\cdot\\frac23=\\frac{31}{12}\\approx2.583$.\n(b) $y\\,dy=x\\,dx\\Rightarrow\\frac{y^2}{2}=\\frac{x^2}{2}+C$. With $y(1)=2$: $2=\\frac12+C$, so $C=\\frac32$ and $y^2=x^2+3$. Since $y(1)=2>0$, $f(x)=\\sqrt{x^2+3}$, and $f(2)=\\sqrt7\\approx2.646$.\n(c) $\\frac{d^2y}{dx^2}=\\frac{y-x\\frac{dy}{dx}}{y^2}=\\frac{y-\\frac{x^2}{y}}{y^2}=\\frac{y^2-x^2}{y^3}$. Along the solution $y^2-x^2=3>0$ and $y>0$, so $\\frac{d^2y}{dx^2}=\\frac{3}{y^3}>0$. The graph is concave up, so tangent lines lie below it and the Euler approximation $2.583$ is less than $f(2)\\approx2.646$.")

P = 80 / (1 + 7 * exp(-R(1, 5) * t))
assert simplify(diff(P, t) - R(1, 5) * P * (1 - P / 80)) == 0 and P.subs(t, 0) == 10
fm = R(1, 5) * 40 * (1 - R(40, 80))
assert fm == 4
B.frq(T_LOG,
      "The number of fish $P(t)$, in hundreds, in a lake $t$ years after stocking satisfies the logistic differential equation $\\dfrac{dP}{dt}=0.2P\\left(1-\\dfrac{P}{80}\\right)$, with $P(0)=10$.\n\n**(a)** Find $\\displaystyle\\lim_{t\\to\\infty}P(t)$. Justify your answer.\n\n**(b)** For what value of $P$ is the number of fish growing most rapidly? What is that greatest rate of growth?\n\n**(c)** Use separation of variables to find the particular solution $P(t)$.",
      [(1, "(a) Limit is 80"),
       (1, "(a) Justification: $\\frac{dP}{dt}>0$ for $0<P<80$ and $=0$ at $P=80$, so $P$ increases toward the equilibrium 80 (a bounded increasing function)"),
       (1, "(b) $P=40$ (half the carrying capacity, vertex of the parabola $\\frac{dP}{dt}=0.2P-\\frac{P^2}{400}$)"),
       (1, "(b) Greatest rate $=0.2(40)\\left(1-\\frac{40}{80}\\right)=4$ hundred fish per year"),
       (1, "(c) Separates: $\\frac{dP}{P\\left(1-\\frac{P}{80}\\right)}=0.2\\,dt$ and writes $\\frac{80}{P(80-P)}$ as partial fractions $\\frac1P+\\frac{1}{80-P}$"),
       (1, "(c) Antidifferentiates both sides: $\\ln|P|-\\ln|80-P|=0.2t+C$"),
       (1, "(c) Uses $P(0)=10$ to get $C=\\ln\\frac{10}{70}=-\\ln7$"),
       (1, "(c) Solves for $P$"),
       (1, "(c) $P(t)=\\dfrac{80}{1+7e^{-0.2t}}$")],
      "(a) For $0<P<80$ the factor $1-\\frac{P}{80}$ is positive, so $\\frac{dP}{dt}>0$ and $P$ increases; it cannot pass the equilibrium $P=80$ where $\\frac{dP}{dt}=0$. Therefore $\\lim_{t\\to\\infty}P=80$.\n(b) $\\frac{dP}{dt}=0.2P-\\frac{P^2}{400}$ is a downward parabola in $P$ with its maximum at $P=40$, where $\\frac{dP}{dt}=0.2(40)\\left(1-\\frac12\\right)=4$ hundred fish per year.\n(c) $\\frac{dP}{P(1-P/80)}=0.2\\,dt$, and $\\frac{1}{P(1-P/80)}=\\frac{80}{P(80-P)}=\\frac1P+\\frac{1}{80-P}$. Integrating: $\\ln|P|-\\ln|80-P|=0.2t+C$. At $t=0$: $\\ln\\frac{10}{70}=C$. So $\\frac{P}{80-P}=\\frac17e^{0.2t}$, which gives $P=\\frac{80}{1+7e^{-0.2t}}$.")

B.save()
B.brief()
