"""Unit 6, BC-only and missing topics: long division / completing the square, integration by parts,
linear partial fractions, improper integrals. Writes content/ap-calc-bc/{questions,frqs}/unit-6-bc.json."""
from lib import *

B = Bank(6, "unit-6-integration-and-accumulation-of-change")
T_LD, T_IBP, T_PF, T_IMP = "long-division-and-completing-the-square", "integration-by-parts", "partial-fractions", "improper-integrals"
LN = lambda e: log(Abs(e))


def check(F, f):
    """F is an antiderivative of f (Abs removed so sympy can differentiate the logs)."""
    Fm = F.replace(Abs, lambda arg: arg)
    assert simplify(diff(Fm, x) - f) == 0, (F, f)


def val(e):
    return simplify(e)


# ---------------------------------------------------------------- long division / completing the square
f1 = (x**2 + 3 * x + 5) / (x + 1)
F1 = x**2 / 2 + 2 * x + 3 * LN(x + 1)
check(F1, f1)
assert simplify(apart(f1, x) - (x + 2 + 3 / (x + 1))) == 0
B.mcq(T_LD, "Which expression is $\\displaystyle\\int\\frac{x^2+3x+5}{x+1}\\,dx$?",
      chCt("\\frac{x^2}{2}+2x+3\\ln|x+1|", "Divide first: $x^2+3x+5=(x+1)(x+2)+3$, so the integrand is $x+2+\\frac{3}{x+1}$. Integrate each term: $\\frac{x^2}{2}+2x+3\\ln|x+1|$.", F1),
      [chCt("\\frac{x^2}{2}+2x+\\frac{3}{x+1}", "After dividing, the remainder term $\\frac{3}{x+1}$ still has to be integrated. Its antiderivative is $3\\ln|x+1|$, not $\\frac{3}{x+1}$.", x**2 / 2 + 2 * x + 3 / (x + 1)),
       chCt("\\frac{x^2}{2}+2x+\\ln|x+1|", "The remainder is $3$, so the last term is $\\int\\frac{3}{x+1}dx=3\\ln|x+1|$. The 3 cannot be dropped.", x**2 / 2 + 2 * x + LN(x + 1)),
       {"text": "$\\dfrac{\\frac{x^3}{3}+\\frac{3x^2}{2}+5x}{\\frac{x^2}{2}+x}+C$", "expl": "An integral of a quotient is not the quotient of the integrals. Integrating top and bottom separately is not a valid rule; divide first, then integrate term by term.", "val": None}],
      "The numerator has higher degree than the denominator, so use long division to rewrite the integrand as a polynomial plus a remainder over $x+1$, then integrate term by term.",
      difficulty="easy")

f2 = 1 / (x**2 + 4 * x + 13)
F2 = atan((x + 2) / 3) / 3
check(F2, f2)
B.mcq(T_LD, "Which expression is $\\displaystyle\\int\\frac{dx}{x^2+4x+13}$?",
      chCt("\\frac13\\arctan\\frac{x+2}{3}", "Complete the square: $x^2+4x+13=(x+2)^2+9$. With $u=x+2$, $\\int\\frac{du}{u^2+9}=\\frac13\\arctan\\frac{u}{3}$.", F2),
      [chCt("\\arctan\\frac{x+2}{3}", "The antiderivative of $\\frac{1}{u^2+a^2}$ is $\\frac1a\\arctan\\frac ua$. The factor $\\frac13$ is missing.", atan((x + 2) / 3)),
       chCt("\\frac13\\arctan(x+2)", "This treats $(x+2)^2+9$ as $(x+2)^2+1$. The 9 means the argument of arctan is $\\frac{x+2}{3}$.", atan(x + 2) / 3),
       chCt("\\ln(x^2+4x+13)", "$\\ln(x^2+4x+13)$ would be the antiderivative of $\\frac{2x+4}{x^2+4x+13}$. The numerator here is 1, not the derivative of the denominator.", log(x**2 + 4 * x + 13))],
      "The denominator has no real roots, so complete the square and use the arctangent form $\\int\\frac{du}{u^2+a^2}=\\frac1a\\arctan\\frac ua+C$.",
      difficulty="medium")

v3 = 1 - pi / 4
assert simplify(integrate(x**2 / (x**2 + 1), (x, 0, 1)) - v3) == 0
B.mcq(T_LD, "What is the value of $\\displaystyle\\int_0^1\\frac{x^2}{x^2+1}\\,dx$?",
      ch(v3, "Divide: $\\frac{x^2}{x^2+1}=1-\\frac{1}{x^2+1}$. Then $\\left[x-\\arctan x\\right]_0^1=1-\\frac\\pi4$."),
      [ch(pi / 4, "This is $\\int_0^1\\frac{dx}{x^2+1}$. The integrand here is $1-\\frac{1}{x^2+1}$, so the 1 contributes too."),
       ch(1 + pi / 4, "The arctangent term is subtracted: $\\frac{x^2}{x^2+1}=1-\\frac{1}{x^2+1}$, not $1+\\frac{1}{x^2+1}$."),
       ch(log(2) / 2, "This is $\\frac12\\ln(x^2+1)$ evaluated from 0 to 1, which would be the integral of $\\frac{x}{x^2+1}$. The numerator here is $x^2$, so divide first.")],
      "The degrees of numerator and denominator are equal, so divide before integrating: $\\frac{x^2}{x^2+1}=1-\\frac{1}{x^2+1}$.",
      difficulty="medium")

v4 = pi / 8
assert simplify(integrate(1 / (x**2 - 4 * x + 8), (x, 0, 2)) - v4) == 0
B.mcq(T_LD, "What is the value of $\\displaystyle\\int_0^2\\frac{dx}{x^2-4x+8}$?",
      ch(v4, "Complete the square: $x^2-4x+8=(x-2)^2+4$. An antiderivative is $\\frac12\\arctan\\frac{x-2}{2}$. At $x=2$ it is 0 and at $x=0$ it is $\\frac12\\arctan(-1)=-\\frac\\pi8$, so the value is $0-\\left(-\\frac\\pi8\\right)=\\frac\\pi8$."),
      [ch(pi / 4, "The factor $\\frac12$ from $\\frac1a$ with $a=2$ is missing."),
       ch(pi / 16, "The coefficient is $\\frac1a=\\frac12$, not $\\frac1{a^2}=\\frac14$."),
       ch(-log(2), "This is $\\ln(x^2-4x+8)$ from 0 to 2, which is $\\ln4-\\ln8$. That is the antiderivative of $\\frac{2x-4}{x^2-4x+8}$, not of $\\frac{1}{x^2-4x+8}$.")],
      "The quadratic has no real roots. Completing the square gives the arctangent form $\\int\\frac{du}{u^2+a^2}=\\frac1a\\arctan\\frac ua$ with $u=x-2$ and $a=2$.",
      difficulty="medium")

f5 = (2 * x + 3) / (x**2 + 4 * x + 8)
F5 = log(x**2 + 4 * x + 8) - atan((x + 2) / 2) / 2
check(F5, f5)
B.mcq(T_LD, "Which expression is $\\displaystyle\\int\\frac{2x+3}{x^2+4x+8}\\,dx$?",
      chCt("\\ln(x^2+4x+8)-\\frac12\\arctan\\frac{x+2}{2}", "Split the numerator as $2x+3=(2x+4)-1$. The first part is the derivative of the denominator, giving $\\ln(x^2+4x+8)$. The rest is $-\\int\\frac{dx}{(x+2)^2+4}=-\\frac12\\arctan\\frac{x+2}{2}$.", F5),
      [chCt("\\ln(x^2+4x+8)+\\frac12\\arctan\\frac{x+2}{2}", "$2x+3=(2x+4)-1$, so the leftover term is $-\\frac{1}{x^2+4x+8}$. It is subtracted, not added.", log(x**2 + 4 * x + 8) + atan((x + 2) / 2) / 2),
       chCt("\\ln(x^2+4x+8)", "Only the part $2x+4$ is the derivative of the denominator. The leftover $-1$ still contributes an arctangent term.", log(x**2 + 4 * x + 8)),
       chCt("\\ln(x^2+4x+8)-\\arctan\\frac{x+2}{2}", "The arctangent term should carry the factor $\\frac1a=\\frac12$.", log(x**2 + 4 * x + 8) - atan((x + 2) / 2))],
      "Rewrite the numerator as a multiple of the denominator's derivative plus a constant. The first piece gives a logarithm, the second (after completing the square) an arctangent.",
      difficulty="hard")

# ---------------------------------------------------------------- integration by parts
F = x * exp(x) - exp(x)
check(F, x * exp(x))
B.mcq(T_IBP, "Which expression is $\\displaystyle\\int xe^x\\,dx$?",
      chC(F, "Let $u=x$ and $dv=e^x\\,dx$, so $du=dx$ and $v=e^x$. Then $\\int xe^x\\,dx=xe^x-\\int e^x\\,dx=xe^x-e^x$."),
      [chC(x * exp(x) + exp(x), "The formula is $uv-\\int v\\,du$. The second integral is subtracted."),
       chC(x**2 * exp(x) / 2, "Integrating each factor separately does not work: the integral of a product is not the product of the integrals. Differentiating $\\frac{x^2}{2}e^x$ gives $xe^x+\\frac{x^2}{2}e^x$."),
       chC(x * exp(x), "This is $uv$ alone. The formula also subtracts $\\int v\\,du=\\int e^x\\,dx$.")],
      "A product of a polynomial and an exponential is a case for integration by parts: choose $u$ as the factor that gets simpler when differentiated.",
      difficulty="easy")

B.mcq(T_IBP, "Which choice of $u$ and $dv$ is most useful for $\\displaystyle\\int x\\ln x\\,dx$?",
      ch("$u=\\ln x$ and $dv=x\\,dx$", "Differentiating $\\ln x$ gives the simpler $\\frac1x$, and $v=\\frac{x^2}{2}$ is easy. The new integral is $\\int\\frac{x}{2}\\,dx$."),
      [ch("$u=x$ and $dv=\\ln x\\,dx$", "This is legitimate in principle, but then $v=\\int\\ln x\\,dx$ is itself a parts problem, so it makes the work longer, not shorter."),
       ch("$u=x\\ln x$ and $dv=dx$", "Then $du=(\\ln x+1)\\,dx$ and $v=x$, which gives $\\int x(\\ln x+1)\\,dx$, a harder integral than the one we started with."),
       ch("$u=1$ and $dv=x\\ln x\\,dx$", "This chooses $dv$ to be the whole integrand, so $v$ is the very integral we are trying to find.")],
      "Choose $u$ so that differentiating it simplifies the integral, and $dv$ so that it can be integrated directly. A logarithm is usually $u$ because its derivative is algebraic.",
      difficulty="easy")

v3 = (exp(2) + 1) / 4
assert simplify(integrate(x * exp(2 * x), (x, 0, 1)) - v3) == 0
B.mcq(T_IBP, "What is the value of $\\displaystyle\\int_0^1xe^{2x}\\,dx$?",
      chv("\\frac{e^2+1}{4}", "With $u=x$ and $dv=e^{2x}dx$: $\\int xe^{2x}dx=\\frac{x}{2}e^{2x}-\\frac14e^{2x}$. At 1 this is $\\frac{e^2}{2}-\\frac{e^2}{4}=\\frac{e^2}{4}$; at 0 it is $-\\frac14$. The value is $\\frac{e^2}{4}+\\frac14$.", v3),
      [chv("\\frac{e^2-1}{4}", "The lower limit contributes $-\\left(-\\frac14\\right)=+\\frac14$, not $-\\frac14$.", (exp(2) - 1) / 4),
       chv("\\frac{e^2}{4}", "This leaves out the value of the antiderivative at the lower limit, which is $-\\frac14$ and not 0.", exp(2) / 4),
       chv("\\frac{e^2}{2}", "This evaluates only $\\frac{x}{2}e^{2x}$ at 1 and forgets both the second term of the antiderivative and the lower limit.", exp(2) / 2)],
      "Use parts with $u=x$, $dv=e^{2x}dx$, then evaluate the antiderivative at both limits. Remember $v=\\frac12e^{2x}$, not $e^{2x}$.",
      difficulty="medium")

assert simplify(integrate(log(x), (x, 1, E)) - 1) == 0
B.mcq(T_IBP, "What is the value of $\\displaystyle\\int_1^e\\ln x\\,dx$?",
      ch(1, "Let $u=\\ln x$ and $dv=dx$, so $du=\\frac{dx}{x}$ and $v=x$. Then $\\int\\ln x\\,dx=x\\ln x-\\int dx=x\\ln x-x$. From 1 to $e$: $(e-e)-(0-1)=1$."),
      [ch(E, "This evaluates only $x\\ln x$ and drops the $-x$ term: $\\int dx$ still has to be subtracted."),
       ch(2 * E - 1, "The second integral is subtracted: $x\\ln x-x$, not $x\\ln x+x$."),
       ch(Rational(1, 2), "This takes $\\frac{(\\ln x)^2}{2}$ as the antiderivative of $\\ln x$. Differentiating it gives $\\frac{\\ln x}{x}$.")],
      "There is no basic antiderivative for $\\ln x$, but parts with $dv=dx$ produces one: $\\int\\ln x\\,dx=x\\ln x-x+C$.",
      difficulty="medium")

F5b = exp(x) * (x**2 - 2 * x + 2)
check(F5b, x**2 * exp(x))
B.mcq(T_IBP, "Which expression is $\\displaystyle\\int x^2e^x\\,dx$?",
      chC(F5b, "Parts twice. First $u=x^2$, $dv=e^xdx$ gives $x^2e^x-2\\int xe^xdx$. Then $\\int xe^xdx=xe^x-e^x$, so the result is $x^2e^x-2xe^x+2e^x=e^x(x^2-2x+2)$."),
      [chC(exp(x) * (x**2 - 2 * x - 2), "The last term is $-2\\cdot(-e^x)=+2e^x$. The minus sign in front of the second integral multiplies the minus sign inside it."),
       chC(exp(x) * (x**2 + 2 * x + 2), "The first parts step subtracts: $x^2e^x-2\\int xe^x\\,dx$, so the middle term is $-2xe^x$."),
       chC(exp(x) * (x**2 - 2 * x), "The second parts step produces both $-2xe^x$ and $+2e^x$. Stopping at $-2xe^x$ leaves out the constant term $2e^x$.")],
      "When the polynomial has degree 2, parts is applied twice, each time lowering the degree by one.",
      difficulty="medium")

v6 = (exp(pi) + 1) / 2
assert simplify(integrate(exp(x) * sin(x), (x, 0, pi)) - v6) == 0
B.mcq(T_IBP, "What is the value of $\\displaystyle\\int_0^\\pi e^x\\sin x\\,dx$?",
      chv("\\frac{e^{\\pi}+1}{2}", "Two rounds of parts bring back the original integral: $I=e^x\\sin x-e^x\\cos x-I$, so $I=\\frac{e^x}{2}(\\sin x-\\cos x)$. At $\\pi$: $\\frac{e^\\pi}{2}$. At 0: $-\\frac12$. The value is $\\frac{e^\\pi}{2}+\\frac12$.", v6),
      [chv("\\frac{e^{\\pi}-1}{2}", "The antiderivative at 0 is $-\\frac12$, and subtracting it adds $\\frac12$.", (exp(pi) - 1) / 2),
       chv("e^{\\pi}+1", "Solving $I=\\ldots-I$ gives $2I=\\ldots$, so the antiderivative has a factor $\\frac12$.", exp(pi) + 1),
       chv("\\frac{e^{\\pi}}{2}", "This omits the value at the lower limit: $\\frac{e^0}{2}(\\sin0-\\cos0)=-\\frac12$, not 0.", exp(pi) / 2)],
      "Neither factor gets simpler under repeated differentiation, so apply parts twice. The original integral reappears, and you solve for it algebraically.",
      difficulty="hard")

v7 = pi / 4 - log(2) / 2
assert simplify(integrate(atan(x), (x, 0, 1)) - v7) == 0
B.mcq(T_IBP, "What is the value of $\\displaystyle\\int_0^1\\arctan x\\,dx$?",
      chv("\\frac\\pi4-\\frac{\\ln2}{2}", "Let $u=\\arctan x$, $dv=dx$. Then $\\int\\arctan x\\,dx=x\\arctan x-\\int\\frac{x}{1+x^2}dx=x\\arctan x-\\frac12\\ln(1+x^2)$. From 0 to 1: $\\frac\\pi4-\\frac12\\ln2$.", v7),
      [chv("\\frac\\pi4+\\frac{\\ln2}{2}", "The second integral is subtracted: $uv-\\int v\\,du$.", pi / 4 + log(2) / 2),
       chv("\\frac\\pi4", "This keeps only $x\\arctan x$ and drops $-\\int\\frac{x}{1+x^2}dx$.", pi / 4),
       chv("\\frac\\pi4-\\ln2", "$\\int\\frac{x}{1+x^2}dx=\\frac12\\ln(1+x^2)$. The factor $\\frac12$ comes from $u=1+x^2$, $du=2x\\,dx$.", pi / 4 - log(2))],
      "An inverse trigonometric function has no basic antiderivative, but taking $dv=dx$ turns the integral into one with a rational integrand.",
      difficulty="hard")

B.mcq(T_IBP, "A function $f$ has $f(2)=5$ and $\\displaystyle\\int_0^2f(x)\\,dx=7$. What is $\\displaystyle\\int_0^2xf'(x)\\,dx$?",
      ch(3, "Let $u=x$, $dv=f'(x)dx$. Then $\\int_0^2xf'(x)dx=\\big[xf(x)\\big]_0^2-\\int_0^2f(x)dx=2(5)-0-7=3$."),
      [ch(17, "The second integral is subtracted: $[xf(x)]_0^2-\\int_0^2f(x)\\,dx$."),
       ch(-3, "This subtracts in the wrong order: $\\int_0^2f-[xf]_0^2$. The formula is $uv-\\int v\\,du$."),
       ch(10, "This is $[xf(x)]_0^2$ alone. The integral of $f$ over the interval still has to be subtracted.")],
      "Parts with $u=x$ and $dv=f'(x)\\,dx$ (so $v=f(x)$) trades an integral of $xf'$ for one of $f$, which is given.",
      difficulty="medium")

# ---------------------------------------------------------------- linear partial fractions
B.mcq(T_PF, "The expression $\\dfrac{1}{(x-1)(x+2)}$ is written as $\\dfrac{A}{x-1}+\\dfrac{B}{x+2}$. What are $A$ and $B$?",
      ch("$A=\\frac13$ and $B=-\\frac13$", "Multiply through: $1=A(x+2)+B(x-1)$. At $x=1$: $1=3A$, so $A=\\frac13$. At $x=-2$: $1=-3B$, so $B=-\\frac13$."),
      [ch("$A=1$ and $B=-1$", "Each coefficient comes from $3A=1$ and $-3B=1$. The 3 cannot be dropped."),
       ch("$A=-\\frac13$ and $B=\\frac13$", "The values are swapped. Substituting $x=1$ kills the $B$ term and leaves $1=3A$."),
       ch("$A=\\frac13$ and $B=\\frac13$", "Substituting $x=-2$ gives $1=B(-2-1)=-3B$, so $B$ is negative.")],
      "Clear denominators to get $1=A(x+2)+B(x-1)$ and substitute the roots $x=1$ and $x=-2$ to isolate each constant.",
      difficulty="easy")

f2 = 1 / ((x - 1) * (x + 2))
F2 = (LN(x - 1) - LN(x + 2)) / 3
check(F2, f2)
B.mcq(T_PF, "Which expression is $\\displaystyle\\int\\frac{dx}{(x-1)(x+2)}$?",
      {"text": "$\\frac13\\ln\\left|\\frac{x-1}{x+2}\\right|+C$", "expl": "$\\frac{1}{(x-1)(x+2)}=\\frac13\\left(\\frac{1}{x-1}-\\frac{1}{x+2}\\right)$, so the integral is $\\frac13\\big(\\ln|x-1|-\\ln|x+2|\\big)+C$.", "val": F2},
      [{"text": "$\\frac13\\ln|(x-1)(x+2)|+C$", "expl": "The two logarithms have opposite signs, so they combine as a quotient. A product would come from adding them.", "val": (LN(x - 1) + LN(x + 2)) / 3},
       {"text": "$\\ln\\left|\\frac{x-1}{x+2}\\right|+C$", "expl": "The coefficients are $\\pm\\frac13$, not $\\pm1$.", "val": LN(x - 1) - LN(x + 2)},
       {"text": "$\\frac13\\ln\\left|\\frac{x+2}{x-1}\\right|+C$", "expl": "The $x-1$ term is the one with the positive coefficient $\\frac13$, so it goes in the numerator.", "val": (LN(x + 2) - LN(x - 1)) / 3}],
      "The denominator factors into distinct linear factors, so decompose into partial fractions and integrate each term as a logarithm.",
      difficulty="medium")

v3 = log(Rational(3, 2)) / 2
assert simplify(integrate(1 / (x**2 - 1), (x, 2, 3)) - v3) == 0
B.mcq(T_PF, "What is the value of $\\displaystyle\\int_2^3\\frac{dx}{x^2-1}$?",
      chv("\\frac12\\ln\\frac32", "$\\frac{1}{x^2-1}=\\frac12\\left(\\frac{1}{x-1}-\\frac{1}{x+1}\\right)$, so the integral is $\\frac12\\ln\\frac{x-1}{x+1}$ from 2 to 3: $\\frac12\\left(\\ln\\frac12-\\ln\\frac13\\right)=\\frac12\\ln\\frac32$.", v3),
      [chv("\\ln\\frac32", "The coefficient $\\frac12$ is missing.", log(Rational(3, 2))),
       chv("\\frac12\\ln\\frac23", "The upper limit minus the lower limit is $\\ln\\frac12-\\ln\\frac13=\\ln\\frac32$. This has them reversed.", log(Rational(2, 3)) / 2),
       chv("\\frac12\\ln\\frac83", "This is $\\frac12\\ln(x^2-1)$ from 2 to 3. That antiderivative would need the numerator $x$ (so that $du=2x\\,dx$); here the numerator is 1.", log(Rational(8, 3)) / 2)],
      "Factor $x^2-1=(x-1)(x+1)$, decompose, integrate, and evaluate the combined logarithm at the limits.",
      difficulty="medium")

f4 = (3 * x + 5) / ((x + 1) * (x + 3))
F4 = LN(x + 1) + 2 * LN(x + 3)
check(F4, f4)
B.mcq(T_PF, "Which expression is $\\displaystyle\\int\\frac{3x+5}{(x+1)(x+3)}\\,dx$?",
      chCt("\\ln|x+1|+2\\ln|x+3|", "Write $\\frac{3x+5}{(x+1)(x+3)}=\\frac{A}{x+1}+\\frac{B}{x+3}$. At $x=-1$: $2=2A$, so $A=1$. At $x=-3$: $-4=-2B$, so $B=2$.", F4),
      [chCt("2\\ln|x+1|+\\ln|x+3|", "The constants are swapped. $A$ (over $x+1$) comes from substituting $x=-1$, which gives $3(-1)+5=2$ divided by $(-1+3)=2$.", 2 * LN(x + 1) + LN(x + 3)),
       chCt("\\ln|x+1|-2\\ln|x+3|", "At $x=-3$: $3(-3)+5=-4$ and $(x+1)=-2$, so $B=\\frac{-4}{-2}=+2$.", LN(x + 1) - 2 * LN(x + 3)),
       chCt("3\\ln|x+1|+5\\ln|x+3|", "The coefficients of the numerator are not the partial-fraction constants. Find $A$ and $B$ by substituting the roots.", 3 * LN(x + 1) + 5 * LN(x + 3))],
      "Use $3x+5=A(x+3)+B(x+1)$ and substitute $x=-1$ and $x=-3$.",
      difficulty="medium")

f5 = 1 / (x * (100 - x))
F5 = (LN(x) - LN(100 - x)) / 100
check(F5, f5)
B.mcq(T_PF, "Which expression is $\\displaystyle\\int\\frac{dP}{P(100-P)}$? (Treat $0<P<100$.)",
      {"text": "$\\frac{1}{100}\\ln\\left|\\frac{P}{100-P}\\right|+C$", "expl": "$\\frac{1}{P(100-P)}=\\frac{1}{100}\\left(\\frac1P+\\frac{1}{100-P}\\right)$. Since $\\int\\frac{dP}{100-P}=-\\ln|100-P|$, the result is $\\frac{1}{100}\\big(\\ln|P|-\\ln|100-P|\\big)$.", "val": F5},
      [{"text": "$\\frac{1}{100}\\ln|P(100-P)|+C$", "expl": "The antiderivative of $\\frac{1}{100-P}$ is $-\\ln|100-P|$ because of the inner function $100-P$. The two logarithms subtract.", "val": (LN(x) + LN(100 - x)) / 100},
       {"text": "$\\ln\\left|\\frac{P}{100-P}\\right|+C$", "expl": "The partial-fraction constants are $\\frac1{100}$, not 1.", "val": LN(x) - LN(100 - x)},
       {"text": "$\\frac{1}{100}\\ln\\left|\\frac{100-P}{P}\\right|+C$", "expl": "The $\\frac1P$ term has the positive coefficient, so $P$ is in the numerator.", "val": (LN(100 - x) - LN(x)) / 100}],
      "This is the integral that appears when solving the logistic equation $\\frac{dP}{dt}=kP(1-\\frac{P}{100})$ by separation of variables. It needs partial fractions, with care for the $100-P$ factor.",
      difficulty="hard")

f6 = 1 / (x**2 - x - 6)
F6 = (LN(x - 3) - LN(x + 2)) / 5
check(F6, f6)
B.mcq(T_PF, "Which expression is $\\displaystyle\\int\\frac{dx}{x^2-x-6}$?",
      {"text": "$\\frac15\\ln\\left|\\frac{x-3}{x+2}\\right|+C$", "expl": "$x^2-x-6=(x-3)(x+2)$ and $\\frac{1}{(x-3)(x+2)}=\\frac15\\left(\\frac{1}{x-3}-\\frac{1}{x+2}\\right)$.", "val": F6},
      [{"text": "$\\frac15\\ln\\left|\\frac{x+2}{x-3}\\right|+C$", "expl": "The $\\frac{1}{x-3}$ term has the positive coefficient $\\frac15$, so $x-3$ is in the numerator.", "val": (LN(x + 2) - LN(x - 3)) / 5},
       {"text": "$\\frac15\\ln|(x-3)(x+2)|+C$", "expl": "The partial-fraction terms have opposite signs, so the logarithms subtract and combine as a quotient.", "val": (LN(x - 3) + LN(x + 2)) / 5},
       {"text": "$\\frac{1}{2x-1}\\ln|x^2-x-6|+C$", "expl": "$\\int\\frac{dx}{u}=\\ln|u|$ only works when the numerator is $du$. Here the numerator is 1, and $du=(2x-1)\\,dx$.", "val": log(x**2 - x - 6) / (2 * x - 1)}],
      "Factor the quadratic first, then decompose. The constants are $A=\\frac{1}{3+2}$ and $B=\\frac{1}{-2-3}$.",
      difficulty="hard")

# ---------------------------------------------------------------- improper integrals
B.mcq(T_IMP, "What is the value of $\\displaystyle\\int_1^\\infty\\frac{dx}{x^2}$?",
      ch(1, "$\\int_1^b\\frac{dx}{x^2}=1-\\frac1b$, and $\\lim_{b\\to\\infty}\\left(1-\\frac1b\\right)=1$."),
      [ch(0, "This keeps the antiderivative's value at infinity and forgets to subtract its value at the lower limit: $\\left[-\\frac1x\\right]_1^\\infty=0-(-1)=1$."),
       ch(-1, "This adds the lower-limit value instead of subtracting it: it is $F(\\infty)-F(1)=0-(-1)=1$, not $0+(-1)$."),
       ch("The integral diverges", "An infinite interval does not make an integral diverge by itself. The integrand decays fast enough: $\\frac{1}{x^p}$ converges on $[1,\\infty)$ when $p>1$.")],
      "Replace the infinite limit by a variable $b$, integrate, and take the limit as $b\\to\\infty$.",
      difficulty="easy")

B.mcq(T_IMP, "Which statement about $\\displaystyle\\int_1^\\infty\\frac{dx}{x}$ is true?",
      ch("It diverges, because $\\ln b\\to\\infty$ as $b\\to\\infty$", "$\\int_1^b\\frac{dx}{x}=\\ln b$, which grows without bound."),
      [ch("It converges to 0, because $\\frac1x\\to0$", "The integrand approaching 0 does not make the integral converge. It has to approach 0 fast enough, and $\\frac1x$ does not."),
       ch("It converges to 1", "The integral of $\\frac1x$ over $[1,b]$ is $\\ln b$, not a number that settles near 1."),
       ch("It converges to $e$", "$\\ln b=1$ only at $b=e$, not as $b\\to\\infty$. The limit of $\\ln b$ is $\\infty$.")],
      "Compare with $\\int_1^\\infty\\frac{dx}{x^p}$: it converges exactly when $p>1$. Here $p=1$, the borderline case, which diverges.",
      difficulty="easy")

B.mcq(T_IMP, "What is the value of $\\displaystyle\\int_0^\\infty e^{-2x}\\,dx$?",
      ch(Rational(1, 2), "$\\int_0^be^{-2x}dx=\\frac12\\left(1-e^{-2b}\\right)\\to\\frac12$."),
      [ch(2, "The antiderivative of $e^{-2x}$ is $-\\frac12e^{-2x}$, not $-2e^{-2x}$. Dividing by the inner coefficient gives $\\frac12$."),
       ch(0, "The integrand tends to 0, but the area from 0 up to any $b$ is positive and tends to $\\frac12$."),
       ch("The integral diverges", "The interval is infinite, but $e^{-2x}$ decays exponentially, so the area is finite.")],
      "Take $\\lim_{b\\to\\infty}\\int_0^be^{-2x}dx$.",
      difficulty="medium")

B.mcq(T_IMP, "What is the value of $\\displaystyle\\int_0^1\\frac{dx}{\\sqrt x}$?",
      ch(2, "The integrand is unbounded at $x=0$, so this is improper: $\\lim_{a\\to0^+}\\int_a^1x^{-1/2}dx=\\lim\\left(2-2\\sqrt a\\right)=2$."),
      [ch("The integral diverges", "An unbounded integrand does not guarantee divergence. $\\frac{1}{x^p}$ near 0 converges when $p<1$, and here $p=\\frac12$."),
       ch(1, "The antiderivative of $x^{-1/2}$ is $2x^{1/2}$. Evaluating at 1 gives 2, not 1."),
       ch(Rational(1, 2), "This divides by 2 instead of by $\\frac12$ in the power rule: $\\int x^{-1/2}dx=\\frac{x^{1/2}}{1/2}=2x^{1/2}$.")],
      "The discontinuity is at the lower limit, so replace 0 by $a$ and take $a\\to0^+$.",
      difficulty="medium")

B.mcq(T_IMP, "For which values of $p$ does $\\displaystyle\\int_0^1\\frac{dx}{x^p}$ converge?",
      ch("$p<1$", "Near 0, $\\int_a^1x^{-p}dx=\\frac{1-a^{1-p}}{1-p}$ has a finite limit as $a\\to0^+$ exactly when $1-p>0$. At $p=1$ it is $-\\ln a\\to\\infty$."),
      [ch("$p>1$", "This is the condition for convergence on $[1,\\infty)$. Near 0 the condition reverses."),
       ch("$p\\le1$", "At $p=1$ the integral is $\\int_a^1\\frac{dx}{x}=-\\ln a$, which diverges as $a\\to0^+$."),
       ch("$p\\ne1$", "For $p>1$ the integrand blows up faster than $\\frac1x$ near 0, and the integral diverges.")],
      "Compute $\\int_a^1x^{-p}dx$ and look at its limit as $a\\to0^+$. Notice how this differs from $\\int_1^\\infty$.",
      difficulty="medium")

assert simplify(integrate(x * exp(-x), (x, 0, oo)) - 1) == 0
B.mcq(T_IMP, "What is the value of $\\displaystyle\\int_0^\\infty xe^{-x}\\,dx$?",
      ch(1, "Parts gives the antiderivative $-xe^{-x}-e^{-x}$. As $b\\to\\infty$ it tends to 0 (since $be^{-b}\\to0$), and at 0 it equals $-1$. So the value is $0-(-1)=1$."),
      [ch(0, "$xe^{-x}\\to0$ at infinity, but that says nothing about the area. The antiderivative at the lower limit is $-1$."),
       ch(-1, "This comes from the antiderivative $-xe^{-x}+e^{-x}$, which has a sign error: its derivative is $xe^{-x}-2e^{-x}$. The correct one is $-xe^{-x}-e^{-x}$."),
       ch("The integral diverges", "The factor $x$ grows, but $e^{-x}$ decays faster, so $be^{-b}\\to0$.")],
      "Integrate by parts first, then take the limit as the upper bound goes to infinity. $\\lim_{b\\to\\infty}be^{-b}=0$.",
      difficulty="hard")

v7 = log(3) / 2
assert simplify(integrate(1 / (x**2 - 1), (x, 2, oo)) - v7) == 0
B.mcq(T_IMP, "What is the value of $\\displaystyle\\int_2^\\infty\\frac{dx}{x^2-1}$?",
      ch(v7, "$\\frac{1}{x^2-1}=\\frac12\\left(\\frac{1}{x-1}-\\frac{1}{x+1}\\right)$, so $\\int_2^b=\\frac12\\ln\\frac{x-1}{x+1}\\Big|_2^b=\\frac12\\ln\\frac{b-1}{b+1}-\\frac12\\ln\\frac13$. As $b\\to\\infty$ the first term goes to $0$, leaving $\\frac12\\ln3$."),
      [ch(-log(3) / 2, "The lower limit contributes $-\\frac12\\ln\\frac13=+\\frac12\\ln3$."),
       ch(log(3), "The partial-fraction coefficient $\\frac12$ is missing."),
       ch("The integral diverges", "Each partial-fraction piece diverges separately, but together they cancel at infinity. The integrand behaves like $\\frac{1}{x^2}$ for large $x$, so the integral converges.")],
      "Decompose into partial fractions, combine the logarithms before taking the limit, and the infinite parts cancel.",
      difficulty="hard")

B.mcq(T_IMP, "Which statement is true about $\\displaystyle\\int_0^2\\frac{dx}{(x-1)^2}$?",
      ch("It diverges, because the integrand is unbounded inside the interval at $x=1$", "The discontinuity at $x=1$ lies in the middle, so split the integral there. $\\int_0^1\\frac{dx}{(x-1)^2}$ diverges, so the whole integral diverges."),
      [ch("It equals $-2$, found by the Fundamental Theorem of Calculus", "Applying the Fundamental Theorem across $x=1$ with the antiderivative $-\\frac{1}{x-1}$ gives $-1-1=-2$. But the FTC requires a function continuous on the whole interval, and this one is not."),
       ch("It equals 2, the absolute value of the result from the Fundamental Theorem", "This takes the absolute value of the invalid $-2$ because the integrand is positive. The $-2$ is itself the result of applying the FTC where it does not apply, and the area is actually infinite."),
       ch("It equals 0, because the areas on the two sides of $x=1$ cancel", "Symmetry about $x=1$ does not make the two halves cancel: the integrand is positive on both sides, so their areas add.")],
      "Check the interval for points where the integrand is undefined. An interior discontinuity forces you to split the integral and treat each half as an improper integral.",
      difficulty="hard")

# ---------------------------------------------------------------- free response
a_ = -x * exp(-x) - exp(-x)
check(a_, x * exp(-x))
area = integrate(x * exp(-x), (x, 0, 2))
assert simplify(area - (1 - 3 * exp(-2))) == 0
B.frq(T_IBP,
      "Let $f(x)=xe^{-x}$ for $x\\ge0$.\n\n**(a)** Find $\\displaystyle\\int f(x)\\,dx$.\n\n**(b)** Evaluate $\\displaystyle\\int_0^\\infty f(x)\\,dx$, or show that it diverges.\n\n**(c)** Find the area of the region bounded by the graph of $f$, the $x$-axis and the line $x=2$.",
      [(1, "(a) Chooses $u=x$ and $dv=e^{-x}dx$ (so $du=dx$, $v=-e^{-x}$)"),
       (1, "(a) Applies $\\int u\\,dv=uv-\\int v\\,du$ to get $-xe^{-x}+\\int e^{-x}dx$"),
       (1, "(a) Antiderivative $-xe^{-x}-e^{-x}+C$"),
       (1, "(b) Writes the integral as $\\lim_{b\\to\\infty}\\int_0^bf(x)\\,dx$"),
       (1, "(b) Evaluates the antiderivative at $b$ and at 0"),
       (1, "(b) Shows $be^{-b}\\to0$ and $e^{-b}\\to0$, and concludes the value is 1"),
       (1, "(c) Sets up $\\int_0^2xe^{-x}\\,dx$ (with $f\\ge0$ on the interval)"),
       (1, "(c) Evaluates the antiderivative at 2 and 0"),
       (1, "(c) Area $=1-3e^{-2}\\approx0.594$")],
      "(a) With $u=x$, $dv=e^{-x}dx$: $\\int xe^{-x}dx=-xe^{-x}+\\int e^{-x}dx=-xe^{-x}-e^{-x}+C$.\n(b) $\\int_0^\\infty xe^{-x}dx=\\lim_{b\\to\\infty}\\left[-xe^{-x}-e^{-x}\\right]_0^b=\\lim_{b\\to\\infty}\\left(-be^{-b}-e^{-b}\\right)-(0-1)=0+1=1$, since $be^{-b}\\to0$ and $e^{-b}\\to0$.\n(c) $f(x)\\ge0$ on $[0,2]$, so the area is $\\int_0^2xe^{-x}dx=\\left[-xe^{-x}-e^{-x}\\right]_0^2=-2e^{-2}-e^{-2}+1=1-3e^{-2}\\approx0.594$.")

g = 1 / (x**2 - x - 2)
assert simplify(apart(g, x) - (Rational(1, 3) / (x - 2) - Rational(1, 3) / (x + 1))) == 0
vb = integrate(g, (x, 3, oo))
vc = integrate(g, (x, 0, 1))
assert simplify(vb - 2 * log(2) / 3) == 0 and simplify(vc + 2 * log(2) / 3) == 0
B.frq(T_PF,
      "Let $g(x)=\\dfrac{1}{x^2-x-2}$.\n\n**(a)** Find constants $A$ and $B$ such that $g(x)=\\dfrac{A}{x-2}+\\dfrac{B}{x+1}$.\n\n**(b)** Evaluate $\\displaystyle\\int_3^\\infty g(x)\\,dx$, or show that it diverges.\n\n**(c)** Evaluate $\\displaystyle\\int_0^1g(x)\\,dx$.",
      [(1, "(a) Factors $x^2-x-2=(x-2)(x+1)$ and writes $1=A(x+1)+B(x-2)$"),
       (1, "(a) $A=\\frac13$ and $B=-\\frac13$"),
       (1, "(b) Antiderivative $\\frac13\\ln|x-2|-\\frac13\\ln|x+1|$ (or $\\frac13\\ln\\left|\\frac{x-2}{x+1}\\right|$)"),
       (1, "(b) Writes the integral as $\\lim_{b\\to\\infty}\\int_3^bg(x)\\,dx$"),
       (1, "(b) Evaluates the limit (the term at $b$ tends to 0 after combining the logarithms)"),
       (1, "(b) Value $\\frac13\\ln4=\\frac23\\ln2$"),
       (1, "(c) Uses the same antiderivative with limits 0 and 1 (no discontinuity on $[0,1]$)"),
       (1, "(c) Evaluates $\\frac13\\left(\\ln\\frac12-\\ln2\\right)$"),
       (1, "(c) Value $-\\frac23\\ln2$")],
      "(a) $1=A(x+1)+B(x-2)$. At $x=2$: $A=\\frac13$. At $x=-1$: $B=-\\frac13$.\n(b) $\\int g\\,dx=\\frac13\\ln\\left|\\frac{x-2}{x+1}\\right|+C$. Then $\\int_3^\\infty g\\,dx=\\lim_{b\\to\\infty}\\frac13\\ln\\frac{b-2}{b+1}-\\frac13\\ln\\frac14=0+\\frac13\\ln4=\\frac23\\ln2\\approx0.462$.\n(c) $g$ is continuous on $[0,1]$, so $\\int_0^1g\\,dx=\\frac13\\ln\\left|\\frac{1-2}{1+1}\\right|-\\frac13\\ln\\left|\\frac{0-2}{0+1}\\right|=\\frac13\\ln\\frac12-\\frac13\\ln2=-\\frac23\\ln2\\approx-0.462$.")

B.save()
B.brief()
