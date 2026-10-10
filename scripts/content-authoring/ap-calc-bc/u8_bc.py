"""Unit 8, BC-only topic: arc length and distance traveled.
Writes content/ap-calc-bc/{questions,frqs}/unit-8-bc.json."""
from lib import *

B = Bank(8, "unit-8-applications-of-integration")
T_AL = "arc-length-and-distance-traveled"
R = Rational


def length(f, lo, hi):
    return Integral(sqrt(1 + diff(f, x) ** 2), (x, lo, hi))


# 1. which integral (easy)
B.mcq(T_AL, "Which integral gives the length of the curve $y=x^2$ from $x=0$ to $x=2$?",
      ch("$\\displaystyle\\int_0^2\\sqrt{1+4x^2}\\,dx$", "The length is $\\int_a^b\\sqrt{1+\\left(\\frac{dy}{dx}\\right)^2}\\,dx$. Here $\\frac{dy}{dx}=2x$, so the integrand is $\\sqrt{1+(2x)^2}=\\sqrt{1+4x^2}$."),
      [ch("$\\displaystyle\\int_0^2\\sqrt{1+x^4}\\,dx$", "This puts $y=x^2$ itself into the formula. The formula uses the derivative of $y$, not $y$."),
       ch("$\\displaystyle\\int_0^2\\left(1+4x^2\\right)dx$", "The expression $1+\\left(\\frac{dy}{dx}\\right)^2$ must be under a square root."),
       ch("$\\displaystyle\\int_0^2\\sqrt{1+2x}\\,dx$", "The derivative $2x$ must be squared inside the root: $\\left(\\frac{dy}{dx}\\right)^2=4x^2$.")],
      "Arc length is the integral of $\\sqrt{1+\\left(\\frac{dy}{dx}\\right)^2}$ over the interval: the Pythagorean theorem applied to a tiny piece with run $dx$ and rise $dy$.",
      difficulty="easy")

# 2. a perfect-root case
f = R(2, 3) * x ** R(3, 2)
v = integrate(sqrt(1 + diff(f, x) ** 2), (x, 0, 3))
assert simplify(v - R(14, 3)) == 0
B.mcq(T_AL, "What is the length of the curve $y=\\frac23x^{3/2}$ from $x=0$ to $x=3$?",
      ch(R(14, 3), "$\\frac{dy}{dx}=x^{1/2}$, so $\\sqrt{1+\\left(\\frac{dy}{dx}\\right)^2}=\\sqrt{1+x}$. Then $\\int_0^3\\sqrt{1+x}\\,dx=\\frac23(1+x)^{3/2}\\Big|_0^3=\\frac23(8-1)=\\frac{14}{3}$."),
      [ch(R(16, 3), "This is the antiderivative at $x=3$ only. The value at the lower limit, $\\frac23(1)^{3/2}=\\frac23$, still has to be subtracted."),
       ch(2 * sqrt(3), "This drops the 1 under the root: $\\int_0^3\\sqrt x\\,dx$. The integrand is $\\sqrt{1+x}$."),
       ch(7, "The antiderivative of $\\sqrt{1+x}$ is $\\frac23(1+x)^{3/2}$. Leaving out the $\\frac23$ gives 7.")],
      "Differentiate, square, add 1, and look for a simplification. Here the integrand is a simple root of $1+x$.",
      difficulty="easy")

# 3. cosh
f = (exp(x) + exp(-x)) / 2
assert simplify(1 + diff(f, x) ** 2 - f**2) == 0
v = integrate(f, (x, 0, log(2)))
assert simplify(v - R(3, 4)) == 0
B.mcq(T_AL, "What is the length of the curve $y=\\dfrac{e^x+e^{-x}}{2}$ from $x=0$ to $x=\\ln2$?",
      ch(R(3, 4), "$\\frac{dy}{dx}=\\frac{e^x-e^{-x}}{2}$, and $1+\\left(\\frac{dy}{dx}\\right)^2=\\left(\\frac{e^x+e^{-x}}{2}\\right)^2$, so the root is $\\frac{e^x+e^{-x}}{2}$. The length is $\\left[\\frac{e^x-e^{-x}}{2}\\right]_0^{\\ln2}=\\frac{2-\\frac12}{2}-0=\\frac34$."),
      [ch(R(5, 4), "This evaluates the integrand $\\frac{e^x+e^{-x}}{2}$ at $\\ln2$ instead of its antiderivative."),
       ch(R(3, 2), "The antiderivative is $\\frac{e^x-e^{-x}}{2}$. Dropping the denominator 2 doubles the answer."),
       ch(log(2), "This treats $\\sqrt{1+\\left(\\frac{dy}{dx}\\right)^2}$ as 1, which would be the length of the horizontal projection. The curve is longer than its projection.")],
      "After squaring the derivative and adding 1, the expression under the root is a perfect square, so the root disappears.",
      difficulty="medium")

# 4. calculator
f = log(x)
vals = {
    "ok": N(length(f, 1, 3), 15),
    "uses_y": N(Integral(sqrt(1 + f**2), (x, 1, 3)), 15),
    "no_root": N(Integral(1 + diff(f, x) ** 2, (x, 1, 3)), 15),
    "no_one": N(Integral(sqrt(diff(f, x) ** 2), (x, 1, 3)), 15),
}
txt = {k_: num(v_) for k_, v_ in vals.items()}
assert len(set(txt.values())) == 4, txt
B.mcq(T_AL, "A graphing calculator is allowed. What is the length of the curve $y=\\ln x$ from $x=1$ to $x=3$, to three decimal places?",
      ch(f"${txt['ok']}$", f"The length is $\\int_1^3\\sqrt{{1+\\left(\\frac1x\\right)^2}}\\,dx\\approx{txt['ok']}$."),
      [ch(f"${txt['uses_y']}$", f"This integrates $\\sqrt{{1+(\\ln x)^2}}$, using $y$ in place of $y'$ ($\\approx{txt['uses_y']}$)."),
       ch(f"${txt['no_root']}$", f"This integrates $1+\\frac{{1}}{{x^2}}$ without the square root ($\\approx{txt['no_root']}$)."),
       ch(f"${txt['no_one']}$", f"This integrates $\\sqrt{{\\left(\\frac1x\\right)^2}}=\\frac1x$ and leaves out the 1 under the root ($\\approx{txt['no_one']}$).")],
      "Set up $\\int_1^3\\sqrt{1+\\left(\\frac{dy}{dx}\\right)^2}\\,dx$ and evaluate it numerically. Write the setup as well as the result.",
      difficulty="medium")

# 5. distance traveled vs displacement
vel = x**2 - 4
dist = integrate(4 - x**2, (x, 0, 2)) + integrate(x**2 - 4, (x, 2, 3))  # |v| split at the sign change t = 2
disp = integrate(vel, (x, 0, 3))
assert (dist, disp) == (R(23, 3), -3)
B.mcq(T_AL, "A particle moves along the $x$-axis with velocity $v(t)=t^2-4$ for $0\\le t\\le3$. What is the total distance the particle travels?",
      ch(R(23, 3), "The velocity changes sign at $t=2$, so split the interval. $\\int_0^2(4-t^2)\\,dt=\\frac{16}{3}$ and $\\int_2^3(t^2-4)\\,dt=\\frac73$. The total distance is $\\int_0^3|v(t)|\\,dt=\\frac{23}{3}$."),
      [ch(-3, "This is the displacement $\\int_0^3v(t)\\,dt$. Distance is never negative; it uses $|v|$."),
       ch(R(16, 3), "This is the distance traveled on $[0,2]$ only. The particle also moves between $t=2$ and $t=3$."),
       ch(3, "This takes the absolute value of the displacement. When velocity changes sign, the distance is larger than $|\\text{displacement}|$.")],
      "Total distance traveled is the integral of speed, $\\int|v(t)|\\,dt$. Find where $v$ changes sign and integrate each piece with the sign that makes it positive.",
      difficulty="medium")

# 6. root disappears with f'(x) = sqrt(e^x - 1)
fp = sqrt(exp(x) - 1)
assert simplify(sqrt(1 + fp**2) - exp(x / 2)) == 0
v = integrate(exp(x / 2), (x, 0, log(4)))
assert simplify(v - 2) == 0
B.mcq(T_AL, "The function $f$ satisfies $f'(x)=\\sqrt{e^x-1}$ for $x\\ge0$. What is the length of the graph of $f$ from $x=0$ to $x=\\ln4$?",
      ch(2, "$1+\\left(f'(x)\\right)^2=1+e^x-1=e^x$, so the integrand is $\\sqrt{e^x}=e^{x/2}$. The length is $\\left[2e^{x/2}\\right]_0^{\\ln4}=2(2)-2(1)=2$."),
      [ch(3, "This integrates $e^x$, which is $1+(f')^2$ without the square root: $\\int_0^{\\ln4}e^x\\,dx=3$."),
       ch(1, "The antiderivative of $e^{x/2}$ is $2e^{x/2}$. Without the 2, the value is $e^{\\ln2}-e^0=1$."),
       ch(4, "This evaluates $2e^{x/2}$ at the upper limit only, $2e^{\\ln 2}=4$, and leaves out the lower limit.")],
      "Square the derivative that is given, add 1, and simplify before integrating: the root usually disappears in designed problems.",
      difficulty="hard")

# 7. classic perfect square
f = x**3 / 6 + 1 / (2 * x)
inside = simplify(1 + diff(f, x) ** 2 - (x**2 / 2 + 1 / (2 * x**2)) ** 2)
assert inside == 0
v = integrate(x**2 / 2 + 1 / (2 * x**2), (x, 1, 2))
assert v == R(17, 12)
wrong_a = integrate(1 + diff(f, x), (x, 1, 2))
wrong_b = integrate(diff(f, x), (x, 1, 2))
wrong_c = (x**3 / 6 - 1 / (2 * x)).subs(x, 2)
assert (wrong_a, wrong_b, wrong_c) == (R(23, 12), R(11, 12), R(13, 12))
B.mcq(T_AL, "What is the length of the curve $y=\\dfrac{x^3}{6}+\\dfrac{1}{2x}$ from $x=1$ to $x=2$?",
      ch(R(17, 12), "$\\frac{dy}{dx}=\\frac{x^2}{2}-\\frac{1}{2x^2}$, and $1+\\left(\\frac{dy}{dx}\\right)^2=\\left(\\frac{x^2}{2}+\\frac{1}{2x^2}\\right)^2$. The length is $\\int_1^2\\left(\\frac{x^2}{2}+\\frac{1}{2x^2}\\right)dx=\\left[\\frac{x^3}{6}-\\frac{1}{2x}\\right]_1^2=\\frac{13}{12}-\\left(-\\frac13\\right)=\\frac{17}{12}$."),
      [ch(R(23, 12), "This integrates $1+\\frac{dy}{dx}$. The formula has $\\sqrt{1+\\left(\\frac{dy}{dx}\\right)^2}$, and $\\sqrt{1+u^2}\\ne1+u$."),
       ch(R(11, 12), "This is $\\int_1^2\\frac{dy}{dx}\\,dx=y(2)-y(1)$, the change in height. Arc length is greater than the change in height."),
       ch(R(13, 12), "This is the antiderivative at $x=2$ only. The value at $x=1$, $\\frac16-\\frac12=-\\frac13$, still has to be subtracted.")],
      "Look for $1+\\left(\\frac{dy}{dx}\\right)^2$ to be a perfect square. Expanding $\\left(\\frac{x^2}{2}-\\frac{1}{2x^2}\\right)^2$ and adding 1 turns it into $\\left(\\frac{x^2}{2}+\\frac{1}{2x^2}\\right)^2$.",
      difficulty="hard")

# free response
y_ = R(1, 3) * (x**2 + 2) ** R(3, 2)
yp = diff(y_, x)
assert simplify(yp - x * sqrt(x**2 + 2)) == 0
assert simplify(1 + yp**2 - (x**2 + 1) ** 2) == 0
L_ = integrate(x**2 + 1, (x, 0, 3))
assert L_ == 12
avg = integrate(yp, (x, 0, 3)) / 3
assert simplify(avg - (11 * sqrt(11) - 2 * sqrt(2)) / 9) == 0
B.frq(T_AL,
      "Consider the curve $y=\\dfrac13\\left(x^2+2\\right)^{3/2}$ for $0\\le x\\le3$.\n\n**(a)** Find $\\dfrac{dy}{dx}$, and show that $1+\\left(\\dfrac{dy}{dx}\\right)^2=\\left(x^2+1\\right)^2$.\n\n**(b)** Find the length of the curve.\n\n**(c)** Find the average value of $\\dfrac{dy}{dx}$ on the interval $0\\le x\\le3$.",
      [(1, "(a) $\\frac{dy}{dx}=x\\sqrt{x^2+2}$ (chain rule, $\\frac13\\cdot\\frac32=\\frac12$ and $\\frac{d}{dx}(x^2+2)=2x$)"),
       (1, "(a) $1+\\left(\\frac{dy}{dx}\\right)^2=1+x^2\\left(x^2+2\\right)$"),
       (1, "(a) $=x^4+2x^2+1=\\left(x^2+1\\right)^2$"),
       (1, "(b) Sets up the length as $\\int_0^3\\sqrt{1+\\left(\\frac{dy}{dx}\\right)^2}\\,dx$"),
       (1, "(b) Simplifies the integrand to $x^2+1$ (since $x^2+1>0$) and finds an antiderivative $\\frac{x^3}{3}+x$"),
       (1, "(b) Length $=12$"),
       (1, "(c) Average value $=\\frac{1}{3-0}\\int_0^3\\frac{dy}{dx}\\,dx$"),
       (1, "(c) Evaluates the integral by the Fundamental Theorem, $y(3)-y(0)$ (or by substitution)"),
       (1, "(c) $\\frac{11\\sqrt{11}-2\\sqrt2}{9}\\approx3.739$")],
      "(a) $\\frac{dy}{dx}=\\frac13\\cdot\\frac32\\left(x^2+2\\right)^{1/2}\\cdot2x=x\\sqrt{x^2+2}$. Then $1+\\left(\\frac{dy}{dx}\\right)^2=1+x^2\\left(x^2+2\\right)=x^4+2x^2+1=\\left(x^2+1\\right)^2$.\n(b) Length $=\\int_0^3\\sqrt{\\left(x^2+1\\right)^2}\\,dx=\\int_0^3\\left(x^2+1\\right)dx=\\left[\\frac{x^3}{3}+x\\right]_0^3=9+3=12$.\n(c) Average value $=\\frac13\\int_0^3\\frac{dy}{dx}\\,dx=\\frac13\\big(y(3)-y(0)\\big)=\\frac13\\left(\\frac{11^{3/2}}{3}-\\frac{2^{3/2}}{3}\\right)=\\frac{11\\sqrt{11}-2\\sqrt2}{9}\\approx3.739$.")

B.save()
B.brief()
