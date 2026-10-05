from lib import *

B = Bank(1, "unit-1-limits-and-continuity")
T_DEF, T_ALG, T_CON, T_INF, T_IVT = (
    "limit-definition-and-notation",
    "algebraic-limit-techniques",
    "continuity",
    "infinite-limits-and-asymptotes",
    "intermediate-value-theorem",
)

# 1. conjugate
e = (sqrt(x + 5) - 3) / (x - 4)
v = limit(e, x, 4)
assert v == Rational(1, 6)
B.mcq(T_ALG, "Evaluate $" + LIM(e, 4) + "$.",
      ch(v, "Multiply by the conjugate: $\\dfrac{(x+5)-9}{(x-4)(\\sqrt{x+5}+3)} = \\dfrac{1}{\\sqrt{x+5}+3}$, which approaches $\\dfrac{1}{6}$."),
      [ch(0, "The numerator does go to 0, but so does the denominator. Direct substitution gives $\\frac{0}{0}$, which says nothing about the value, so the limit is not automatically 0."),
       ch(Rational(1, 3), "This uses $\\frac{1}{\\sqrt{9}}$ and forgets the $+3$ that the conjugate puts back in the denominator: it is $\\frac{1}{3+3}$, not $\\frac13$."),
       ch(6, "This is the reciprocal of the correct value. After the factor $x-4$ cancels, the remaining factor $\\sqrt{x+5}+3$ is in the denominator.")],
      "The expression gives $\\frac00$ at $x=4$. Rationalize the numerator, cancel $x-4$, then substitute: $\\lim_{x\\to4}\\frac{1}{\\sqrt{x+5}+3}=\\frac16$.")

# 2. trig limit
e = (1 - cos(2 * x)) / (x * sin(x))
v = limit(e, x, 0)
assert v == 2
B.mcq(T_ALG, "Evaluate $" + LIM(e, 0) + "$.",
      ch(v, "Use $1-\\cos 2x = 2\\sin^2 x$. Then $\\dfrac{2\\sin^2 x}{x\\sin x}=2\\cdot\\dfrac{\\sin x}{x}\\to 2\\cdot 1 = 2$."),
      [ch(0, "Numerator and denominator both go to 0 at the same rate here. The limit of a quotient is not 0 just because the numerator goes to 0."),
       ch(1, "This would be the value of $\\frac{\\sin x}{x}$ alone. The identity $1-\\cos 2x=2\\sin^2x$ contributes a factor of 2."),
       ch(4, "The factor 2 from $2\\sin^2x$ appears once. Squaring it, or doubling it again for the $2x$ inside the cosine, overcounts.")],
      "Rewrite $1-\\cos2x$ as $2\\sin^2x$ so the quotient simplifies to $2\\frac{\\sin x}{x}$, and use $\\lim_{x\\to0}\\frac{\\sin x}{x}=1$.")

# 3. continuity with two parameters
fa = (x**2 + a * x - 6) / (x - 2)
sol_a = solve(Eq((x**2 + a * x - 6).subs(x, 2), 0), a)[0]
assert sol_a == 1
lim_at_2 = limit(fa.subs(a, sol_a), x, 2)
assert lim_at_2 == 5
B.mcq(T_CON,
      "Let $f(x)=\\dfrac{x^2+ax-6}{x-2}$ for $x\\neq 2$ and $f(2)=c$, where $a$ and $c$ are constants. For which values of $a$ and $c$ is $f$ continuous at $x=2$?",
      ch("$a=1,\\ c=5$", "Continuity needs a finite limit, so the numerator must vanish at 2: $4+2a-6=0$ gives $a=1$. Then $f(x)=\\frac{(x-2)(x+3)}{x-2}=x+3\\to5$, so $c=5$."),
      [ch("$a=1,\\ c=0$", "$a=1$ is right, but the limit as $x\\to2$ is 5, so $f(2)$ must be 5, not 0."),
       ch("$a=3,\\ c=5$", "With $a=3$ the numerator at $x=2$ is $4+6-6=4\\neq0$, so $f$ has a vertical asymptote at 2 and no value of $c$ can fix it."),
       ch("$a=-1,\\ c=-5$", "With $a=-1$ the numerator at $x=2$ is $4-2-6=-4\\neq0$, so the limit does not exist as a number. The numerator must be 0 at $x=2$.")],
      "Two conditions: the limit must exist (numerator zero at 2, giving $a=1$) and $f(2)$ must equal that limit ($c=5$).")

# 4. conjugate at infinity
e = sqrt(4 * x**2 + 3 * x) - 2 * x
v = limit(e, x, oo)
assert v == Rational(3, 4)
B.mcq(T_ALG, "Evaluate $" + LIM(r"\sqrt{4x^2+3x}-2x", oo) + "$.",
      ch(v, "Multiply by the conjugate: $\\dfrac{3x}{\\sqrt{4x^2+3x}+2x}$. Divide by $x$: $\\dfrac{3}{\\sqrt{4+3/x}+2}\\to\\dfrac{3}{2+2}=\\dfrac34$."),
      [ch(0, "This treats $\\infty-\\infty$ as cancelling. The two terms grow at the same rate but their difference settles at a nonzero value."),
       ch("$\\infty$", "Each term is unbounded, but the difference is not. Rationalizing shows it is bounded and tends to a finite number."),
       ch(Rational(3, 2), "This forgets that the denominator $\\sqrt{4x^2+3x}+2x$ behaves like $2x+2x=4x$, not $2x$.")],
      "The form is $\\infty-\\infty$. Rationalize, then divide numerator and denominator by $x$ (for $x>0$, $\\sqrt{4x^2+3x}/x=\\sqrt{4+3/x}$).")

# 5. asymptotes with a hole
f5 = (2 * x**2 - 8) / (x**2 - x - 2)
assert factor(f5) == 2 * (x + 2) / (x + 1) or simplify(f5 - 2 * (x + 2) / (x + 1)) == 0
assert limit(f5, x, oo) == 2 and limit(f5, x, 2) == Rational(8, 3)
B.mcq(T_INF, "How many vertical and horizontal asymptotes does the graph of $f(x)=" + L(f5) + "$ have?",
      ch("One vertical asymptote ($x=-1$) and one horizontal asymptote ($y=2$)", "Factor: $f(x)=\\frac{2(x-2)(x+2)}{(x-2)(x+1)}$. The factor $x-2$ cancels, leaving a hole at $x=2$ (at height $\\frac83$), not an asymptote. $x=-1$ is a vertical asymptote and the limit at $\\pm\\infty$ is 2."),
      [ch("Two vertical asymptotes ($x=-1$ and $x=2$) and one horizontal asymptote ($y=2$)", "The denominator is zero at $x=2$, but so is the numerator. That factor cancels, so $x=2$ is a removable discontinuity (a hole), not a vertical asymptote."),
       ch("One vertical asymptote ($x=2$) and one horizontal asymptote ($y=2$)", "This keeps the wrong zero of the denominator. $x=2$ cancels; the surviving factor of the denominator is $x+1$, so the asymptote is at $x=-1$."),
       ch("One vertical asymptote ($x=-1$) and no horizontal asymptote", "The degrees of numerator and denominator are equal (both 2), so $f(x)\\to\\frac{2}{1}=2$ as $x\\to\\pm\\infty$. There is a horizontal asymptote at $y=2$.")],
      "Cancel the common factor first: the cancelled zero is a hole, the remaining zero of the denominator is a vertical asymptote, and equal degrees give a horizontal asymptote at the ratio of leading coefficients.")

# 6. IVT, number of guaranteed zeros
B.mcq(T_IVT,
      "The function $g$ is continuous on $[1,5]$ with $g(1)=-2$, $g(3)=4$ and $g(5)=-1$. Which statement does the Intermediate Value Theorem guarantee?",
      ch("$g(x)=0$ has at least two solutions in $(1,5)$", "$g$ changes sign between $x=1$ and $x=3$ and again between $x=3$ and $x=5$, and each interval contains a zero by the IVT. These intervals do not overlap, so there are at least two zeros."),
      [ch("$g(x)=0$ has exactly two solutions in $(1,5)$", "The IVT only guarantees existence. There could be more zeros (the graph might wiggle across the axis several times); it does not say there are exactly two."),
       ch("$g(x)=0$ has exactly one solution in $(1,5)$", "The IVT gives a zero in $(1,3)$ (values $-2$ and $4$) and another in $(3,5)$ (values $4$ and $-1$). Two different zeros exist, so exactly one is impossible."),
       ch("$g(x)=0$ has at least three solutions in $(1,5)$", "There are only two sign changes among the three given values. The IVT cannot guarantee a third zero from this information.")],
      "Apply the IVT separately on $[1,3]$ and $[3,5]$: $0$ lies between $-2$ and $4$, and between $4$ and $-1$.")

# 7. absolute value / one-sided limits
e = Abs(x + 3) / (x**2 - 9)
left = limit(e, x, -3, "-")
right = limit(e, x, -3, "+")
assert left == Rational(1, 6) and right == -Rational(1, 6)
B.mcq(T_DEF, "What is $" + LIM(e, -3) + "$?",
      ch("The limit does not exist", "For $x<-3$, $|x+3|=-(x+3)$, so the quotient is $\\frac{-1}{x-3}\\to\\frac16$. For $x>-3$ it is $\\frac{1}{x-3}\\to-\\frac16$. The one-sided limits differ, so the two-sided limit does not exist."),
      [ch(Rational(1, 6), "This is only the left-hand limit. The right-hand limit is $-\\frac16$, so the two-sided limit does not exist."),
       ch(-Rational(1, 6), "This is only the right-hand limit. The left-hand limit is $+\\frac16$, so the two-sided limit does not exist."),
       ch(0, "The numerator $|x+3|$ goes to 0, but so does $x^2-9$. After cancelling, the quotient is $\\pm\\frac{1}{x-3}$, which is not near 0.")],
      "Split at $x=-3$: the absolute value changes the sign of the numerator on the two sides, giving limits $\\frac16$ and $-\\frac16$.")

# 8. squeeze
e = x**2 * sin(5 / x)
assert limit(e, x, 0) == 0
B.mcq(T_DEF, "What is $" + LIM(e, 0) + "$?",
      ch(0, "Since $-1\\le\\sin(5/x)\\le1$, we have $-x^2\\le x^2\\sin(5/x)\\le x^2$, and both bounds go to 0. By the Squeeze Theorem the limit is 0."),
      [ch("The limit does not exist, because $\\sin(5/x)$ oscillates as $x\\to0$", "$\\sin(5/x)$ does oscillate, but it is multiplied by $x^2\\to0$, which shrinks the oscillations to nothing. The product is squeezed to 0."),
       ch(5, "This confuses the pattern with $\\frac{\\sin(5x)}{x}\\to5$. Here the argument of the sine goes to infinity rather than to 0."),
       ch(1, "Nothing here approaches 1. The sine stays between $-1$ and $1$, and the factor $x^2$ forces the product to 0.")],
      "A bounded oscillating factor times a factor that tends to 0 tends to 0. Prove it with $-x^2\\le x^2\\sin(5/x)\\le x^2$.")

# 9. classify discontinuities
f9 = (x**2 - 9) / (x**2 - 5 * x + 6)
assert limit(f9, x, 3) == 6 and limit(f9, x, 2, "+") == oo
B.mcq(T_CON, "Let $f(x)=" + L(f9) + "$. Which statement correctly describes the discontinuities of $f$?",
      ch("Removable at $x=3$, infinite (vertical asymptote) at $x=2$", "Factor: $f(x)=\\frac{(x-3)(x+3)}{(x-2)(x-3)}$. The factor $x-3$ cancels, so the limit at 3 exists ($\\frac{3+3}{3-2}=6$) but $f(3)$ is undefined: removable. At $x=2$ the denominator goes to 0 with a nonzero numerator: infinite."),
      [ch("Removable at $x=2$, infinite at $x=3$", "This swaps the two points. The factor that cancels is $x-3$, not $x-2$."),
       ch("Removable at both $x=2$ and $x=3$", "Only a factor that cancels between numerator and denominator gives a removable discontinuity. $x-2$ remains in the denominator."),
       ch("Jump at $x=3$, infinite at $x=2$", "A jump needs unequal finite one-sided limits. At $x=3$ both one-sided limits equal 6, so the discontinuity is removable.")],
      "Factor and cancel. A canceled factor gives a removable discontinuity; a surviving factor in the denominator gives an infinite one.")

# 10. composite limit with one-sided inner behavior
B.mcq(T_DEF,
      "Suppose $\\lim_{x\\to2}g(x)=1$ and $g(x)>1$ for all $x$ near 2 with $x\\neq2$. Suppose also $\\lim_{u\\to1^+}f(u)=7$, $\\lim_{u\\to1^-}f(u)=3$ and $f(1)=5$. What is $\\lim_{x\\to2}f(g(x))$?",
      ch(7, "As $x\\to2$, $g(x)$ approaches 1 from above, so $f(g(x))$ approaches $\\lim_{u\\to1^+}f(u)=7$."),
      [ch(5, "$f(1)=5$ is the value at the point, but $g(x)$ never equals 1 near 2 (it stays above 1), so $f(1)$ is never used."),
       ch(3, "That is the limit of $f$ from the left. $g(x)$ approaches 1 from the right (values above 1)."),
       ch("The limit does not exist", "$f$ does have different one-sided limits at 1, but $g$ only approaches 1 from one side. The composite limit uses only the right-hand limit.")],
      "For a composite, track the side from which the inner function approaches the value. Here that side is the right.")

# 11. factoring a sum of cubes
e = (x**3 + 8) / (x**2 + x - 2)
v = limit(e, x, -2)
assert v == -4
B.mcq(T_ALG, "Evaluate $" + LIM(e, -2) + "$.",
      ch(v, "$x^3+8=(x+2)(x^2-2x+4)$ and $x^2+x-2=(x+2)(x-1)$. After cancelling $x+2$: $\\dfrac{x^2-2x+4}{x-1}\\to\\dfrac{4+4+4}{-3}=-4$."),
      [ch(0, "The $\\frac00$ form does not mean the limit is 0. Factor out $x+2$ from both parts first."),
       ch(4, "The numerator $x^2-2x+4$ is 12 at $x=-2$ and the denominator $x-1$ is $-3$, so the quotient is negative."),
       ch(12, "This evaluates $x^2-2x+4$ at $-2$ but forgets to divide by the remaining factor $x-1=-3$.")],
      "Factor the sum of cubes and the quadratic, cancel the common factor $x+2$, then substitute.")

# 12. limit at -infinity with a radical (sign trap)
e = (3 * x**3 - x) / sqrt(x**6 + 4)
v = limit(e, x, -oo)
assert v == -3
B.mcq(T_INF, "Evaluate $" + LIM(e, -oo) + "$.",
      ch(-3, "For $x<0$, $\\sqrt{x^6}=|x|^3=-x^3$. Dividing top and bottom by $x^3$ (which is negative) gives $\\dfrac{3-1/x^2}{-\\sqrt{1+4/x^6}}\\to\\dfrac{3}{-1}=-3$."),
      [ch(3, "This treats $\\sqrt{x^6}$ as $x^3$. For negative $x$, $x^3<0$ but the square root is positive, so $\\sqrt{x^6}=-x^3$."),
       ch(0, "The degrees match (both behave like $x^3$), so the limit is a nonzero ratio of leading coefficients, not 0."),
       ch(-1, "The numerator's leading term is $3x^3$, not $x^3$. The ratio of leading behaviors is $\\frac{3x^3}{-x^3}$.")],
      "The radical's sign is the trap. For $x\\to-\\infty$, $\\sqrt{x^6}=-x^3$, so the quotient tends to $\\frac{3}{-1}$.")

# 13. continuity with a trig limit
e = (1 - cos(6 * x)) / x**2
assert limit(e, x, 0) == 18
B.mcq(T_CON,
      "Let $f(x)=\\begin{cases}\\dfrac{1-\\cos 6x}{x^2} & x<0\\\\[2mm] 3k-x & x\\ge0\\end{cases}$. For what value of $k$ is $f$ continuous at $x=0$?",
      ch(6, "From the left, $\\frac{1-\\cos 6x}{x^2}=36\\cdot\\frac{1-\\cos6x}{(6x)^2}\\to36\\cdot\\frac12=18$. From the right, $f(0)=3k$. Continuity needs $3k=18$, so $k=6$."),
      [ch(18, "18 is the left-hand limit, but $f(0)=3k$. Setting $3k=18$ gives $k=6$."),
       ch(Rational(1, 6), "This uses $\\frac12$ for the left-hand limit, forgetting the factor $6^2=36$ that comes from the argument $6x$."),
       ch(12, "This takes $36$ as the left-hand limit. The standard limit is $\\frac{1-\\cos u}{u^2}\\to\\frac12$, so the left-hand limit is $36\\cdot\\frac12=18$.")],
      "Continuity at 0 requires left limit $=$ right limit $=f(0)$. Use $\\frac{1-\\cos u}{u^2}\\to\\frac12$ with $u=6x$.")

# 14. exponential limit at -infinity
e = (5 * exp(2 * x) + 1) / (exp(2 * x) - 3 * exp(x))
assert limit(e, x, -oo) == -oo
B.mcq(T_INF, "What is $" + LIM(e, -oo) + "$?",
      ch("$-\\infty$", "As $x\\to-\\infty$, the numerator $5e^{2x}+1\\to1$. The denominator $e^x(e^x-3)$ tends to $0\\cdot(-3)=0$ through negative values. A positive number over a tiny negative number is $-\\infty$."),
      [ch(5, "$5$ is the limit as $x\\to+\\infty$ (leading terms $\\frac{5e^{2x}}{e^{2x}}$). As $x\\to-\\infty$ every exponential term goes to 0 and the behavior is different."),
       ch(0, "The exponential terms do vanish, but the denominator vanishes too, while the numerator tends to 1. A nonzero number over something tending to 0 is unbounded."),
       ch(-Rational(1, 3), "This divides the dominant-looking terms $\\frac{1}{-3e^x}$ and forgets that $e^x\\to0$ as $x\\to-\\infty$. The magnitude grows without bound.")],
      "Check what each piece does at $-\\infty$ separately: numerator tends to 1, denominator tends to 0 from below, so the quotient is $-\\infty$.")

# 15. conjugate in the denominator, two steps
e = (x**2 - 9) / (sqrt(x + 13) - 4)
v = limit(e, x, 3)
assert v == 48
B.mcq(T_ALG, "Evaluate $" + LIM(e, 3) + "$.",
      ch(v, "Multiply by $\\frac{\\sqrt{x+13}+4}{\\sqrt{x+13}+4}$: the denominator becomes $(x+13)-16=x-3$. Then $\\frac{(x-3)(x+3)(\\sqrt{x+13}+4)}{x-3}\\to6\\cdot8=48$."),
      [ch(0, "The numerator goes to 0, but so does the denominator, so this is a $\\frac00$ form that has to be resolved algebraically."),
       ch(6, "This keeps only the factor $x+3=6$. The conjugate factor $\\sqrt{x+13}+4$ equals 8 at $x=3$ and multiplies it."),
       ch(24, "This evaluates the conjugate factor as $4+0=4$ instead of $\\sqrt{16}+4=8$, giving $6\\cdot4$.")],
      "Rationalize the denominator, cancel $x-3$, then substitute $x=3$: $(3+3)(\\sqrt{16}+4)=48$.")

# ------------------------------------------------------------------ FRQs
f = (x**2 - 2 * x - 8) / (x**2 - 16)
assert simplify(f - (x + 2) / (x + 4)) == 0
assert limit(f, x, 4) == Rational(3, 4) and limit(f, x, -4, "-") == oo and limit(f, x, -4, "+") == -oo and limit(f, x, oo) == 1
B.frq(T_CON,
      "Let $f(x)=\\dfrac{x^2-2x-8}{x^2-16}$.\n\n**(a)** Find $\\lim_{x\\to4}f(x)$. Show the algebra.\n\n**(b)** The function $f$ is discontinuous at two values of $x$. Identify each, and classify it as removable or infinite. For the infinite one, find both one-sided limits.\n\n**(c)** Define $g(x)=f(x)$ for $x\\neq4$ and $g(4)=k$. Find the value of $k$ that makes $g$ continuous at $x=4$, and state the three conditions you are using for continuity.\n\n**(d)** Find $\\lim_{x\\to\\infty}f(x)$ and give the equation of the horizontal asymptote.",
      [(1, "(a) Factors the numerator and denominator and cancels $x-4$ to get $\\frac{x+2}{x+4}$"),
       (1, "(a) Evaluates the limit as $\\frac34$"),
       (1, "(b) Identifies $x=4$ as a removable discontinuity (factor cancels) and $x=-4$ as infinite"),
       (1, "(b) Gives $\\lim_{x\\to-4^-}f(x)=+\\infty$ and $\\lim_{x\\to-4^+}f(x)=-\\infty$ with sign reasoning"),
       (1, "(c) Sets $k=\\frac34$ and states $g(4)$ exists, the limit exists, and they are equal"),
       (1, "(d) Finds the limit is 1 and gives $y=1$")],
      "(a) $f(x)=\\frac{(x-4)(x+2)}{(x-4)(x+4)}=\\frac{x+2}{x+4}$ for $x\\neq4$, so $\\lim_{x\\to4}f(x)=\\frac{6}{8}=\\frac34$.\n(b) $f$ is undefined at $x=4$ and $x=-4$. At $x=4$ the factor cancels and the limit is $\\frac34$, so it is removable. At $x=-4$ the denominator tends to 0 and the numerator tends to $-2$: as $x\\to-4^-$, $x+4<0$, so $f\\to\\frac{-2}{0^-}=+\\infty$; as $x\\to-4^+$, $f\\to\\frac{-2}{0^+}=-\\infty$. This is an infinite discontinuity (vertical asymptote $x=-4$).\n(c) Continuity at 4 requires: $g(4)$ is defined, $\\lim_{x\\to4}g(x)$ exists, and the two are equal. The limit is $\\frac34$, so $k=\\frac34$.\n(d) $\\lim_{x\\to\\infty}\\frac{x+2}{x+4}=1$, so the horizontal asymptote is $y=1$.")

# FRQ 5: IVT + one-sided / sign reasoning with a table
B.frq(T_IVT,
      "The function $h$ is continuous on $[0,6]$. Selected values are given in the table.\n\n| $x$ | 0 | 1 | 2 | 4 | 6 |\n|---|---|---|---|---|---|\n| $h(x)$ | $-3$ | $-1$ | $2$ | $1$ | $-2$ |\n\n**(a)** Explain why $h(x)=0$ must have at least two solutions in the interval $(0,6)$.\n\n**(b)** Explain why $h(x)=\\frac32$ must have at least one solution in $(1,4)$, and give a smaller interval of $(1,4)$ in which you can guarantee a solution.\n\n**(c)** Let $p(x)=e^x+x-3$. Use the Intermediate Value Theorem to show that $p(x)=0$ has a solution in $(0,1)$. (You may use $e>2.7$.)\n\n**(d)** A student claims that because $h(1)=-1<0$ and $h(4)=1>0$, $h$ must cross every value between $-1$ and $1$ exactly once in $(1,4)$. Is the claim correct? Explain.",
      [(1, "(a) States $h$ is continuous and finds sign changes on two disjoint intervals, such as $[1,2]$ and $[4,6]$"),
       (1, "(a) Concludes that the IVT gives a zero in each, so at least two zeros"),
       (1, "(b) Uses $h(1)=-1<\\frac32<2=h(2)$ (or $h(4)=1$ and $h(2)=2$) and continuity to guarantee a solution in $(1,2)$"),
       (1, "(c) Shows $p$ is continuous, $p(0)=-2<0$ and $p(1)=e-2>0$, and concludes by the IVT"),
       (1, "(d) Says the claim is incorrect: the IVT guarantees at least one, not exactly one")],
      "(a) $h$ is continuous. Since $h(1)=-1<0<2=h(2)$, the IVT gives a zero in $(1,2)$. Since $h(4)=1>0>-2=h(6)$, the IVT gives a zero in $(4,6)$. These intervals do not overlap, so there are at least two zeros.\n(b) $h(1)=-1<\\frac32<2=h(2)$ and $h$ is continuous on $[1,2]$, so by the IVT there is a $c$ in $(1,2)\\subset(1,4)$ with $h(c)=\\frac32$.\n(c) $p$ is continuous everywhere. $p(0)=1+0-3=-2<0$ and $p(1)=e-2>0.7>0$. By the IVT there is a $c$ in $(0,1)$ with $p(c)=0$.\n(d) The claim is not correct. The IVT guarantees at least one solution for each value between $h(1)$ and $h(4)$, not exactly one. The table gives only a few points, and $h$ could cross a given value several times between them.")

B.save()
B.show()
