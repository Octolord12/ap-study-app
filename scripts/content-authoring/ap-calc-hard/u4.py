from lib import *

B = Bank(4, "unit-4-contextual-applications-of-differentiation")
T_MO, T_RR, T_LL, T_LH = ("straight-line-motion", "related-rates", "local-linearization", "lhopitals-rule")

# 1. speeding up and slowing down
s = t**3 - 9 * t**2 + 24 * t - 5
v = diff(s, t)
a_ = diff(s, t, 2)
assert expand(v - 3 * (t - 2) * (t - 4)) == 0 and expand(a_ - (6 * t - 18)) == 0
B.mcq(T_MO, "A particle moves along a line so that its position for $t\\ge0$ is $s(t)=t^3-9t^2+24t-5$. For which values of $t$ is the speed of the particle increasing?",
      ch("$2<t<3$ and $t>4$", "$v(t)=3(t-2)(t-4)$ and $a(t)=6(t-3)$. Speed increases when $v$ and $a$ have the same sign. On $(2,3)$ both are negative; on $(3,4)$ $v<0<a$; on $(4,\\infty)$ both are positive. So speed increases on $(2,3)$ and $(4,\\infty)$."),
      [ch("$0<t<2$ and $t>4$", "These are the intervals where the velocity is positive (moving right). Speeding up depends on the signs of velocity and acceleration together."),
       ch("$0<t<2$ and $3<t<4$", "On these intervals the velocity and acceleration have opposite signs, so the particle is slowing down, not speeding up."),
       ch("$t>3$", "This is where acceleration is positive. A positive acceleration only speeds the particle up when the velocity is also positive, which is not true on $(3,4)$.")],
      "Speed increases exactly when velocity and acceleration have the same sign. Make a sign chart for $v=3(t-2)(t-4)$ and $a=6(t-3)$.")

# 2. total distance using turning points
sv = {tt: s.subs(t, tt) for tt in (0, 2, 4, 5)}
assert sv == {0: -5, 2: 15, 4: 11, 5: 15}
dist = abs(sv[2] - sv[0]) + abs(sv[4] - sv[2]) + abs(sv[5] - sv[4])
assert dist == 28
B.mcq(T_MO, "A particle moves along a line with position $s(t)=t^3-9t^2+24t-5$ for $0\\le t\\le5$. What is the total distance the particle travels in that time?",
      ch(28, "$v(t)=3(t-2)(t-4)$ is zero at $t=2$ and $t=4$, where the particle turns around. Positions: $s(0)=-5$, $s(2)=15$, $s(4)=11$, $s(5)=15$. Distance: $20+4+4=28$."),
      [ch(20, "This is the net displacement $s(5)-s(0)$. Total distance adds the lengths of each leg of the trip; the particle moves backward from $t=2$ to $t=4$, which cancels part of the displacement but still counts as distance traveled."),
       ch(24, "This stops at $t=4$ and leaves out the last leg from $t=4$ to $t=5$ (a distance of 4)."),
       ch(15, "$s(5)=15$ is the particle's position at the end, not the distance it traveled.")],
      "Find where $v=0$ and split the interval there. Add the absolute change in position over each piece.")

# 3. related rates: cone draining, radius depends on height
V = pi * h**3 / 12
dhdt = symbols("dhdt")
sol = solve(Eq(diff(V, h).subs(h, 4) * dhdt, -8 * pi), dhdt)[0]
assert sol == -2
B.mcq(T_RR, "Water drains from a conical tank (vertex down) with radius 6 ft and height 12 ft at a rate of $8\\pi$ cubic feet per minute. How fast is the water level falling at the instant the water is 4 ft deep?",
      ch("2 ft per minute", "The water's radius is proportional to its depth: $r=\\frac h2$. So $V=\\frac13\\pi r^2h=\\frac{\\pi h^3}{12}$ and $\\frac{dV}{dt}=\\frac{\\pi h^2}{4}\\frac{dh}{dt}$. With $\\frac{dV}{dt}=-8\\pi$ and $h=4$: $-8\\pi=4\\pi\\frac{dh}{dt}$, so $\\frac{dh}{dt}=-2$. The level falls at 2 ft/min."),
      [ch("$\\dfrac23$ ft per minute", "This treats the radius as the constant 6 ft. The surface of the water has a radius that shrinks with the depth, $r=\\frac h2$, so $V$ is not $12\\pi h$."),
       ch("$\\dfrac12$ ft per minute", "This uses $r=h$, as if the cone's radius equaled its height. Here $\\frac rh=\\frac{6}{12}=\\frac12$."),
       ch("$\\dfrac29$ ft per minute", "This substitutes $h=12$ (the full height of the tank) into $\\frac{\\pi h^2}{4}$. The instant in question has the water 4 ft deep.")],
      "Use similar triangles to write $r$ in terms of $h$ before differentiating the volume.")

# 4. angle of elevation
th = symbols("th")
# tan(th) = h/30; sec^2 th * th' = h'/30 ; at h=40, h'=5
sec2 = 1 + Rational(40, 30) ** 2
thp = Rational(5, 30) / sec2
assert thp == Rational(3, 50)
B.mcq(T_RR, "An observer stands 30 m from the base of a launch tower. A rocket rises straight up at 5 m/s. At the instant the rocket is 40 m above the ground, how fast is the observer's angle of elevation $\\theta$ to the rocket changing, in radians per second?",
      ch(Rational(3, 50), "$\\tan\\theta=\\frac{h}{30}$, so $\\sec^2\\theta\\frac{d\\theta}{dt}=\\frac1{30}\\frac{dh}{dt}$. At $h=40$: $\\tan\\theta=\\frac43$ and $\\sec^2\\theta=1+\\frac{16}9=\\frac{25}9$. Then $\\frac{d\\theta}{dt}=\\frac{5/30}{25/9}=\\frac{3}{50}$."),
      [ch(Rational(25, 54), "$\\sec^2\\theta$ is in the denominator on the other side: $\\frac{d\\theta}{dt}=\\frac{1}{30}\\frac{dh}{dt}\\div\\sec^2\\theta$, not multiplied by it."),
       ch(Rational(1, 6), "This is $\\frac{1}{30}\\cdot5$, the rate with the factor $\\sec^2\\theta$ ignored. The derivative of $\\tan\\theta$ is $\\sec^2\\theta\\frac{d\\theta}{dt}$."),
       ch(Rational(9, 25), "This is $\\frac{1}{\\sec^2\\theta}$ alone, which leaves out the factor $\\frac{1}{30}\\frac{dh}{dt}=\\frac16$.")],
      "Relate the angle to the height with a tangent, differentiate with respect to $t$, then use the right triangle with legs 30 and 40 to get $\\sec^2\\theta$.")

# 5. sphere volume to surface area rate
r = symbols("r")
drdt = Rational(36) / (4 * 9)
assert drdt == 1
dSdt = 8 * 3 * drdt
assert dSdt == 24
B.mcq(T_RR, "The volume of a sphere is increasing at a constant rate of $36\\pi$ cubic centimeters per second. At the instant the radius is 3 cm, how fast is the surface area $S=4\\pi r^2$ increasing?",
      ch("$24\\pi$ cm$^2$/s", "$\\frac{dV}{dt}=4\\pi r^2\\frac{dr}{dt}$, so $36\\pi=36\\pi\\frac{dr}{dt}$ and $\\frac{dr}{dt}=1$ cm/s. Then $\\frac{dS}{dt}=8\\pi r\\frac{dr}{dt}=8\\pi(3)(1)=24\\pi$."),
      [ch("$12\\pi$ cm$^2$/s", "This differentiates $4\\pi r^2$ as $4\\pi r$. The power rule gives $2\\cdot4\\pi r=8\\pi r$."),
       ch("$36\\pi$ cm$^2$/s", "$36\\pi$ is the given rate for the volume. The surface area changes at a different rate."),
       ch("$8\\pi$ cm$^2$/s", "This is $8\\pi r$ with $r$ replaced by $\\frac{dr}{dt}=1$. The radius is 3 and the rate of change of the radius is 1; both are needed.")],
      "Use the volume's rate to find $\\frac{dr}{dt}$ first, then differentiate the surface area formula.")

# 6. linear approximation and concavity
f = cbrt(x)
fp8 = diff(f, x).subs(x, 8)
assert fp8 == Rational(1, 12) and diff(f, x, 2).subs(x, 8) < 0
approx = 2 + Rational(3, 10) * fp8
assert approx == Rational(81, 40)
B.mcq(T_LL, "The tangent line to $f(x)=\\sqrt[3]{x}$ at $x=8$ is used to approximate $\\sqrt[3]{8.3}$. Which is the approximation, and is it an overestimate or an underestimate?",
      ch("2.025, an overestimate", "$f'(x)=\\frac13x^{-2/3}$, so $f'(8)=\\frac{1}{12}$ and $L(8.3)=2+\\frac{1}{12}(0.3)=2.025$. Since $f''(x)=-\\frac29x^{-5/3}<0$, the graph is concave down and lies below its tangent lines, so the tangent line value is too large."),
      [ch("2.025, an underestimate", "The value is right, but the graph is concave down ($f''<0$), so it lies below the tangent line and the tangent value overestimates."),
       ch("2.05, an overestimate", "This uses $f'(8)=\\frac16$, from $\\frac13\\cdot\\frac{1}{2}$. The derivative is $\\frac13\\cdot8^{-2/3}=\\frac13\\cdot\\frac14=\\frac1{12}$."),
       ch("2.0083, an underestimate", "This uses $f'(8)=\\frac1{36}$, which is $\\frac13\\cdot\\frac1{12}$. The exponent $-\\frac23$ applies to 8, giving $\\frac14$, not $\\frac1{12}$.")],
      "Compute $L(x)=f(8)+f'(8)(x-8)$ and use the sign of $f''$ to decide whether the tangent line sits above or below the graph.")

# 7. concavity, general statement
B.mcq(T_LL, "The function $f$ is twice differentiable with $f''(x)<0$ for all $x$. Let $L$ be the line tangent to the graph of $f$ at $x=3$. Which statement is true?",
      ch("$L(x)>f(x)$ for every $x\\neq3$", "When $f''<0$ the graph is concave down, so it lies below every one of its tangent lines (except at the point of tangency). The tangent line overestimates $f$ on both sides of 3."),
      [ch("$L(x)<f(x)$ for every $x\\neq3$", "That is the concave-up case ($f''>0$), where the graph lies above its tangent lines."),
       ch("$L(x)>f(x)$ for $x>3$ and $L(x)<f(x)$ for $x<3$", "Concavity does not change sign here ($f''<0$ everywhere), so the tangent line stays on the same side of the graph on both sides of 3."),
       ch("$L(x)=f(x)$ for every $x$ near 3", "The tangent line agrees with $f$ only at $x=3$ unless $f$ is linear. Since $f''<0$, $f$ is never linear.")],
      "A concave-down graph lies below its tangent lines; a concave-up graph lies above them.")

# 8. L'Hopital twice
e = (exp(2 * x) - 1 - 2 * x) / x**2
assert limit(e, x, 0) == 2
B.mcq(T_LH, "What is $" + LIM(r"\frac{e^{2x}-1-2x}{x^2}", 0) + "$?",
      ch(2, "The form is $\\frac00$. L'Hôpital: $\\frac{2e^{2x}-2}{2x}=\\frac{e^{2x}-1}{x}$, still $\\frac00$. Apply it again: $\\frac{2e^{2x}}{1}\\to2$."),
      [ch(0, "After one application the form $\\frac{2e^{2x}-2}{2x}$ is still $\\frac00$, so L'Hôpital must be applied a second time."),
       ch(1, "This applies the derivative of $e^{2x}$ as $e^{2x}$, missing the chain-rule factor 2 each time."),
       ch(4, "This does not divide by the 2 that comes from differentiating $x^2$. The second application gives $\\frac{4e^{2x}}{2}$.")],
      "Apply L'Hôpital's Rule as long as the form remains $\\frac00$.")

# 9. x - sin x over x^3
e = (x - sin(x)) / x**3
assert limit(e, x, 0) == Rational(1, 6)
B.mcq(T_LH, "What is $" + LIM(r"\frac{x-\sin x}{x^3}", 0) + "$?",
      ch(Rational(1, 6), "Apply L'Hôpital three times: $\\frac{1-\\cos x}{3x^2}\\to\\frac{\\sin x}{6x}\\to\\frac{\\cos x}{6}\\to\\frac16$."),
      [ch(0, "The first two applications still give $\\frac00$. Keep going until the denominator is nonzero at 0."),
       ch(Rational(1, 3), "This takes $\\frac{1-\\cos x}{x^2}\\to1$ and divides by 3. That limit is $\\frac12$, not 1."),
       ch(Rational(1, 2), "This is $\\lim\\frac{1-\\cos x}{x^2}$. After the first application the denominator is $3x^2$, so the limit is $\\frac13\\cdot\\frac12=\\frac16$.")],
      "Three applications are needed: the denominators become $3x^2$, $6x$, then $6$.")

# 10. 0 * infinity
e = x * log(x)
assert limit(e, x, 0, "+") == 0
B.mcq(T_LH, "What is $\\displaystyle\\lim_{x\\to0^+}x\\ln x$?",
      ch(0, "The form is $0\\cdot(-\\infty)$. Rewrite as $\\frac{\\ln x}{1/x}$, which is $\\frac{-\\infty}{\\infty}$. L'Hôpital: $\\frac{1/x}{-1/x^2}=-x\\to0$."),
      [ch("$-\\infty$", "$\\ln x\\to-\\infty$, but $x\\to0$ pulls the product the other way. Power functions beat logarithms: the product tends to 0."),
       ch(-1, "After L'Hôpital the expression is $-x$, which tends to 0, not $-1$."),
       ch(1, "A product of a number tending to 0 and one tending to $-\\infty$ is an indeterminate form; it is resolved by rewriting as a quotient, and the result here is 0.")],
      "Rewrite the indeterminate product $0\\cdot\\infty$ as a quotient so that L'Hôpital's Rule applies.")

# 11. L'Hopital does not apply
e = (x + sin(x)) / x
assert limit(e, x, oo) == 1
B.mcq(T_LH, "What is $\\displaystyle\\lim_{x\\to\\infty}\\frac{x+\\sin x}{x}$?",
      ch(1, "Divide by $x$: $1+\\frac{\\sin x}{x}$. Since $-\\frac1x\\le\\frac{\\sin x}{x}\\le\\frac1x$, the second term tends to 0 and the limit is 1."),
      [ch("The limit does not exist, because L'Hôpital's Rule gives $\\lim(1+\\cos x)$, which oscillates", "L'Hôpital's Rule only says that if the limit of the derivative quotient exists, it equals the original limit. When the derivative quotient has no limit, the rule is silent; the original limit can still exist."),
       ch(0, "The numerator grows like $x$, so the quotient does not go to 0."),
       ch(2, "$\\sin x$ is bounded, so it adds nothing in the limit. The terms $x$ in the numerator and denominator give a ratio of 1.")],
      "L'Hôpital's Rule is not the right tool here. Use algebra and the Squeeze Theorem.")

# 12. (1 - cos x)/(x sin x)
e = (1 - cos(x)) / (x * sin(x))
assert limit(e, x, 0) == Rational(1, 2)
B.mcq(T_LH, "What is $" + LIM(r"\frac{1-\cos x}{x\sin x}", 0) + "$?",
      ch(Rational(1, 2), "$\\frac{\\sin x}{\\sin x+x\\cos x}$ is still $\\frac00$. Apply L'Hôpital again: $\\frac{\\cos x}{2\\cos x-x\\sin x}\\to\\frac{1}{2}$."),
      [ch(0, "After the first application the form is still $\\frac00$. Substituting 0 into only the numerator gives a false 0."),
       ch(1, "This stops after one step by cancelling $\\sin x$ against only part of the denominator $\\sin x+x\\cos x$. The term $x\\cos x$ also tends to 0, so the form is still $\\frac00$ and one more application is needed."),
       ch(2, "This is the reciprocal of the correct value; the numerator's derivative $\\cos x$ gives 1 and the denominator's gives 2.")],
      "Use L'Hôpital's Rule twice. Be careful with the product rule on $x\\sin x$.")

# 13. maximum speed on a closed interval
vt = t**3 - 3 * t**2 - 9 * t + 5
assert [vt.subs(t, q_) for q_ in (0, 3, 5)] == [5, -22, 10]
B.mcq(T_MO, "A particle moves along a line with velocity $v(t)=t^3-3t^2-9t+5$ for $0\\le t\\le5$. What is the greatest speed of the particle on this interval?",
      ch(22, "Speed is $|v(t)|$. $v'(t)=3(t-3)(t+1)$ is 0 at $t=3$ in the interval. Compare $|v|$ at $t=0,3,5$: $5$, $22$ and $10$. The greatest is 22."),
      [ch(10, "10 is the largest value of $v$, but speed is $|v|$. At $t=3$ the velocity is $-22$, which is a speed of 22."),
       ch(-22, "Speed is never negative. The velocity $-22$ at $t=3$ corresponds to a speed of 22."),
       ch(5, "This is the speed only at $t=0$. The extreme values of $|v|$ can occur at critical points of $v$ as well as at endpoints.")],
      "Find the critical points of $v$ (zeros of the acceleration), then compare $|v|$ at those points and at the endpoints.")

# 14. changing direction needs a sign change
vt = (t - 1) ** 2 * (t - 3) * (t + 2)
B.mcq(T_MO, "A particle moves along the $x$-axis with velocity $v(t)=(t-1)^2(t-3)(t+2)$ for $t\\ge0$. How many times does the particle change direction?",
      ch(1, "The velocity is zero at $t=1$ and $t=3$. At $t=1$ the factor $(t-1)^2$ does not change sign, so $v$ keeps the same sign. At $t=3$, $v$ changes from negative to positive. The particle changes direction once."),
      [ch(2, "$v=0$ at both $t=1$ and $t=3$, but a particle changes direction only where $v$ changes sign. The double factor at $t=1$ means no sign change there."),
       ch(3, "Counting every zero of $v$, including $t=-2$, is a common slip. $t=-2$ is outside $t\\ge0$ and $t=1$ is a double zero; only $t=3$ is a sign change."),
       ch(0, "The velocity changes sign at $t=3$ (negative before, positive after), so the particle does change direction.")],
      "A zero of the velocity is a turnaround only if the velocity changes sign there. Zeros from squared factors do not.")

# 15. shadow length
x1 = symbols("x1")
sh = Rational(2, 3) * x1
assert diff(sh, x1) * 5 == Rational(10, 3)
B.mcq(T_RR, "A 6-foot-tall person walks away from the base of a 15-foot lamppost at 5 feet per second. How fast is the length of the person's shadow increasing?",
      ch("$\\dfrac{10}{3}$ ft/s", "Let $x$ be the person's distance from the post and $s$ the shadow length. Similar triangles: $\\frac{15}{x+s}=\\frac6s$, so $9s=6x$ and $s=\\frac23x$. Then $\\frac{ds}{dt}=\\frac23\\cdot5=\\frac{10}3$."),
      [ch("$\\dfrac{25}{3}$ ft/s", "This is the speed of the tip of the shadow: $\\frac{d}{dt}(x+s)=5+\\frac{10}3$. The question asks for the length of the shadow."),
       ch("5 ft/s", "5 ft/s is the person's own speed. The shadow length changes at a different rate."),
       ch("$\\dfrac23$ ft/s", "This is the ratio $\\frac{ds}{dx}=\\frac23$ without the factor $\\frac{dx}{dt}=5$.")],
      "Draw the similar triangles formed by the lamp and the person, relate $s$ to $x$, and differentiate.")

# ------------------------------------------------------------------ FRQs
s = t**3 - 6 * t**2 + 9 * t + 2
v = diff(s, t)
assert expand(v - 3 * (t - 1) * (t - 3)) == 0
sp = {q_: s.subs(t, q_) for q_ in (0, 1, 3, 5)}
assert sp == {0: 2, 1: 6, 3: 2, 5: 22}
dist = 4 + 4 + 20
assert abs(sp[1] - sp[0]) + abs(sp[3] - sp[1]) + abs(sp[5] - sp[3]) == 28
vmax = {q_: v.subs(t, q_) for q_ in (0, 2, 5)}
assert vmax == {0: 9, 2: -3, 5: 24}
B.frq(T_MO,
      "A particle moves along the $x$-axis so that its position at time $t\\ge0$ is $s(t)=t^3-6t^2+9t+2$.\n\n**(a)** Find $v(t)$ and $a(t)$. At what times is the particle at rest, and at which of those times does it change direction? Justify your answer.\n\n**(b)** For $0\\le t\\le5$, find all intervals on which the particle is speeding up. Justify your answer.\n\n**(c)** Find the total distance traveled by the particle from $t=0$ to $t=5$.\n\n**(d)** Find the greatest speed of the particle on $0\\le t\\le5$, and the time at which it occurs.",
      [(1, "(a) Finds $v(t)=3t^2-12t+9=3(t-1)(t-3)$ and $a(t)=6t-12$, and $v=0$ at $t=1,3$"),
       (1, "(a) Shows $v$ changes sign at both times (positive, negative, positive), so the particle changes direction at both"),
       (1, "(b) Finds the sign of $a(t)$: negative for $t<2$, positive for $t>2$"),
       (1, "(b) Concludes the particle speeds up on $(1,2)$ and $(3,5)$, because $v$ and $a$ have the same sign there"),
       (1, "(c) Computes $s(0)=2$, $s(1)=6$, $s(3)=2$, $s(5)=22$"),
       (1, "(c) Adds $|s(1)-s(0)|+|s(3)-s(1)|+|s(5)-s(3)|=4+4+20=28$"),
       (1, "(d) Compares $|v|$ at the endpoints and at $t=2$ (where $a=0$): $9,3,24$"),
       (1, "(d) Concludes the greatest speed is 24 at $t=5$")],
      "(a) $v(t)=3t^2-12t+9=3(t-1)(t-3)$ and $a(t)=6t-12$. The particle is at rest at $t=1$ and $t=3$. $v>0$ on $[0,1)$, $v<0$ on $(1,3)$ and $v>0$ on $(3,\\infty)$, so $v$ changes sign at both times and the particle changes direction at both.\n(b) The particle speeds up when $v$ and $a$ have the same sign. $a<0$ for $t<2$ and $a>0$ for $t>2$. On $(0,1)$: $v>0$, $a<0$ (slowing). On $(1,2)$: $v<0$, $a<0$ (speeding up). On $(2,3)$: $v<0$, $a>0$ (slowing). On $(3,5)$: $v>0$, $a>0$ (speeding up). The particle speeds up on $(1,2)$ and $(3,5)$.\n(c) $s(0)=2$, $s(1)=6$, $s(3)=2$, $s(5)=22$. Distance $=4+4+20=28$.\n(d) $v'(t)=a(t)=0$ at $t=2$, where $v(2)=-3$. Compare $|v(0)|=9$, $|v(2)|=3$, $|v(5)|=24$. The greatest speed is 24 at $t=5$.")

# FRQ 5: ladder
xx = symbols("xx", positive=True)
yy = sqrt(625 - xx**2)
assert yy.subs(xx, 7) == 24
yp = diff(yy, xx).subs(xx, 7)
assert yp == Rational(-7, 24)
B.frq(T_RR,
      "A 25-foot ladder leans against a vertical wall. The bottom of the ladder slides away from the wall at a constant rate of 2 feet per second. Let $x$ be the distance from the bottom of the ladder to the wall and $y$ the height of the top of the ladder, both in feet.\n\n**(a)** Write an equation relating $x$ and $y$. At the instant $x=7$, how fast is the top of the ladder sliding down the wall?\n\n**(b)** At the instant $x=7$, is the area of the triangle formed by the ladder, the wall and the ground increasing or decreasing? Find the rate of change of the area at that instant.\n\n**(c)** Let $\\theta$ be the angle between the ladder and the ground. Find $\\dfrac{d\\theta}{dt}$ at the instant $x=7$.\n\n**(d)** The tangent line to $y=\\sqrt{625-x^2}$ at $x=7$ is used to approximate the height when $x=7.5$. Find this approximation, and say whether it is an overestimate or an underestimate. Justify your answer.",
      [(1, "(a) States $x^2+y^2=625$, finds $y=24$ at $x=7$"),
       (1, "(a) Differentiates to get $\\frac{dy}{dt}=-\\frac{7}{12}$ ft/s (sliding down at $\\frac7{12}$ ft/s)"),
       (1, "(b) Uses $A=\\frac12xy$ and the product rule: $\\frac{dA}{dt}=\\frac12\\left(\\frac{dx}{dt}y+x\\frac{dy}{dt}\\right)$"),
       (1, "(b) Evaluates $\\frac{dA}{dt}=\\frac{527}{24}>0$, so the area is increasing"),
       (1, "(c) Uses $\\cos\\theta=\\frac{x}{25}$ and differentiates, finding $\\sin\\theta=\\frac{24}{25}$ at that instant"),
       (1, "(c) Finds $\\frac{d\\theta}{dt}=-\\frac1{12}$ rad/s"),
       (1, "(d) Computes $L(7.5)=24-\\frac{7}{24}(0.5)=\\frac{1145}{48}\\approx23.85$"),
       (1, "(d) Says overestimate because $y$ is concave down ($y''<0$)")],
      "(a) $x^2+y^2=625$. At $x=7$, $y=24$. Differentiating, $2x\\frac{dx}{dt}+2y\\frac{dy}{dt}=0$, so $\\frac{dy}{dt}=-\\frac{x}{y}\\frac{dx}{dt}=-\\frac{7}{24}(2)=-\\frac7{12}$ ft/s. The top slides down at $\\frac7{12}$ ft/s.\n(b) $A=\\frac12xy$, so $\\frac{dA}{dt}=\\frac12\\left(\\frac{dx}{dt}\\,y+x\\frac{dy}{dt}\\right)=\\frac12\\left(2\\cdot24+7\\cdot\\left(-\\frac7{12}\\right)\\right)=\\frac12\\left(48-\\frac{49}{12}\\right)=\\frac{527}{24}$ square feet per second. This is positive, so the area is increasing.\n(c) $\\cos\\theta=\\frac x{25}$, so $-\\sin\\theta\\frac{d\\theta}{dt}=\\frac1{25}\\frac{dx}{dt}=\\frac2{25}$. At $x=7$, $\\sin\\theta=\\frac{24}{25}$, so $\\frac{d\\theta}{dt}=-\\frac{2/25}{24/25}=-\\frac1{12}$ rad/s.\n(d) The tangent line at $x=7$ is $L(x)=24-\\frac7{24}(x-7)$, so $L(7.5)=24-\\frac{7}{48}=\\frac{1145}{48}\\approx23.85$. The function $y=\\sqrt{625-x^2}$ is concave down ($y''=-\\frac{625}{(625-x^2)^{3/2}}<0$), so its graph lies below its tangent lines and the approximation is an overestimate.")

B.save()
B.show()
