"""Unit 10, Taylor and Maclaurin series, and power-series representations of functions."""
from lib import *

R = Rational
n_ = symbols("n_", integer=True, nonnegative=True)
T_TM, T_PS = "taylor-and-maclaurin-series", "power-series-representations"
SUM0 = "\\sum_{n=0}^{\\infty}"


def add(B):
    # ------------------------------------------------------------ Taylor and Maclaurin series
    assert series(cos(x), x, 0, 8).removeO().coeff(x, 4) == R(1, 24)
    B.mcq(T_TM, "What is the coefficient of $x^4$ in the Maclaurin series for $\\cos x$?",
          ch(R(1, 24), "$\\cos x=1-\\frac{x^2}{2!}+\\frac{x^4}{4!}-\\cdots$, so the coefficient of $x^4$ is $\\frac1{4!}=\\frac1{24}$."),
          [ch(R(1, 4), "The coefficient is $\\frac{f^{(4)}(0)}{4!}$, divided by the factorial $4!=24$, not by 4."),
           ch(R(-1, 24), "The signs alternate $+,-,+$ starting with the constant term 1, so the $x^4$ term is positive."),
           ch(R(1, 6), "$\\frac1{3!}=\\frac16$ is the size of the $x^3$ coefficient in $\\sin x$. For $x^4$ in $\\cos x$ it is $\\frac1{4!}$.")],
          "Know the Maclaurin series for $e^x$, $\\sin x$ and $\\cos x$.", difficulty="easy")

    assert series(exp(-(x**2)), x, 0, 8).removeO().coeff(x, 4) == R(1, 2)
    B.mcq(T_TM, "What is the coefficient of $x^4$ in the Maclaurin series for $f(x)=e^{-x^2}$?",
          ch(R(1, 2), "Substitute $-x^2$ into $e^u=1+u+\\frac{u^2}{2!}+\\cdots$: $1-x^2+\\frac{x^4}{2}-\\frac{x^6}{6}+\\cdots$. The coefficient of $x^4$ is $\\frac12$."),
          [ch(R(1, 24), "$\\frac{1}{4!}$ is the coefficient of $u^4$, but here $u=-x^2$, so $x^4$ comes from $\\frac{u^2}{2!}$."),
           ch(R(-1, 2), "$u^2=(-x^2)^2=x^4$ is positive, so the term is $+\\frac{x^4}{2}$."),
           ch(1, "The term is $\\frac{u^2}{2!}$, so the coefficient is $\\frac12$.")],
          "Substituting into a known series is quicker than taking derivatives.", difficulty="easy")

    ser = series(x**2 * sin(x), x, 0, 10).removeO()
    assert [ser.coeff(x, k) for k in (3, 5, 7)] == [1, R(-1, 6), R(1, 120)]
    B.mcq(T_TM, "What are the first three nonzero terms of the Maclaurin series for $f(x)=x^2\\sin x$?",
          ch("$x^3-\\dfrac{x^5}{6}+\\dfrac{x^7}{120}$", "Multiply the series $\\sin x=x-\\frac{x^3}{3!}+\\frac{x^5}{5!}-\\cdots$ by $x^2$ term by term."),
          [ch("$x-\\dfrac{x^3}{6}+\\dfrac{x^5}{120}$", "This is the series for $\\sin x$; the factor $x^2$ raises each power by 2."),
           ch("$x^3+\\dfrac{x^5}{6}+\\dfrac{x^7}{120}$", "The signs of $\\sin x$'s series alternate."),
           ch("$x^3-\\dfrac{x^5}{3}+\\dfrac{x^7}{5}$", "The denominators are factorials: $3!=6$ and $5!=120$, not 3 and 5.")],
          "Multiplying a series by $x^2$ shifts every exponent up by 2.", difficulty="medium")

    ser = series(sin(x**2), x, 0, 10).removeO()
    assert ser.coeff(x, 6) == R(-1, 6) and ser.coeff(x, 6) * factorial(6) == -120
    B.mcq(T_TM, "The function $f(x)=\\sin\\left(x^2\\right)$ has the Maclaurin series $x^2-\\dfrac{x^6}{6}+\\dfrac{x^{10}}{120}-\\cdots$. What is $f^{(6)}(0)$?",
          ch(-120, "The coefficient of $x^6$ is $\\frac{f^{(6)}(0)}{6!}=-\\frac16$, so $f^{(6)}(0)=-\\frac{720}{6}=-120$."),
          [ch(R(-1, 6), "$-\\frac16$ is the coefficient of $x^6$, not the sixth derivative. Multiply by $6!$."),
           ch(-720, "$-720$ would be $-6!$. The coefficient of $x^6$ is $-\\frac16$, so multiply $-\\frac16$ by $720$."),
           ch(120, "The coefficient is negative, so the derivative is negative.")],
          "The coefficient of $x^k$ equals $\\frac{f^{(k)}(0)}{k!}$, so $f^{(k)}(0)=k!\\times$ coefficient.", difficulty="medium")

    ser = series(sin(x), x, pi, 6).removeO()
    u = x - pi
    assert expand(ser - (-u + u**3 / 6 - u**5 / 120)) == 0
    B.mcq(T_TM, "What are the first two nonzero terms of the Taylor series for $f(x)=\\sin x$ about $x=\\pi$?",
          ch("$-(x-\\pi)+\\dfrac{(x-\\pi)^3}{6}$", "$f(\\pi)=0$, $f'(\\pi)=\\cos\\pi=-1$, $f''(\\pi)=0$, $f'''(\\pi)=-\\cos\\pi=1$. So the terms are $-(x-\\pi)+\\frac{1}{3!}(x-\\pi)^3$."),
          [ch("$(x-\\pi)-\\dfrac{(x-\\pi)^3}{6}$", "This is the Maclaurin pattern. At $x=\\pi$ the derivatives are $\\cos\\pi=-1$ and $-\\cos\\pi=1$, which flips both signs."),
           ch("$-(x-\\pi)-\\dfrac{(x-\\pi)^3}{6}$", "$f'''(\\pi)=-\\cos\\pi=+1$, so the cubic term is positive."),
           ch("$1-\\dfrac{(x-\\pi)^2}{2}$", "$f(\\pi)=\\sin\\pi=0$, so there is no constant term.")],
          "Evaluate $f$ and its derivatives at $\\pi$ instead of 0. Alternatively, use $\\sin x=-\\sin(x-\\pi)$.", difficulty="hard")

    assert limit((sin(x) - x) / x**3, x, 0) == R(-1, 6)
    B.mcq(T_TM, "What is $\\displaystyle\\lim_{x\\to0}\\frac{\\sin x-x}{x^3}$?",
          ch(R(-1, 6), "Using $\\sin x=x-\\frac{x^3}{6}+\\frac{x^5}{120}-\\cdots$: $\\frac{\\sin x-x}{x^3}=-\\frac16+\\frac{x^2}{120}-\\cdots\\to-\\frac16$."),
          [ch(0, "This replaces $\\sin x$ by $x$. The next term of the series, $-\\frac{x^3}{6}$, is of the same order as the denominator."),
           ch(R(1, 6), "The $x^3$ term of the sine series is negative."),
           ch(R(-1, 2), "$\\frac{1}{3!}=\\frac16$, not $\\frac12$.")],
          "Replace $\\sin x$ by its Maclaurin series and cancel the lowest-order terms.", difficulty="hard")

    # ------------------------------------------------------------ power series representations
    B.mcq(T_PS, "Which power series represents $\\dfrac{1}{1+x^2}$ for $|x|<1$?",
          ch(f"${SUM0}(-1)^nx^{{2n}}$", "Substitute $-x^2$ into $\\frac{1}{1-u}=\\sum u^n$: $\\sum(-x^2)^n=\\sum(-1)^nx^{2n}=1-x^2+x^4-\\cdots$."),
          [ch(f"${SUM0}x^{{2n}}$", "That is the series for $\\frac{1}{1-x^2}$. The sign in $1+x^2$ makes the terms alternate."),
           ch(f"${SUM0}(-1)^nx^n$", "That is the series for $\\frac{1}{1+x}$. The exponents here are $2n$."),
           ch(f"${SUM0}(-1)^nx^{{2n+1}}$", "That is the series for $\\frac{x}{1+x^2}$, with an extra factor of $x$.")],
          "Start from the geometric series $\\frac1{1-u}=\\sum u^n$ and substitute $u=-x^2$.", difficulty="easy")

    assert series(1 / (1 - 3 * x), x, 0, 6).removeO().coeff(x, 3) == 27
    B.mcq(T_PS, "What is the coefficient of $x^3$ in the Maclaurin series for $\\dfrac{1}{1-3x}$?",
          ch(27, "$\\frac{1}{1-3x}=\\sum(3x)^n=1+3x+9x^2+27x^3+\\cdots$."),
          [ch(3, "3 is the coefficient of $x$. For $x^3$ the ratio is cubed: $3^3=27$."),
           ch(9, "9 is the coefficient of $x^2$."),
           ch(R(1, 27), "The ratio is $3x$, not $\\frac{x}{3}$.")],
          "Substitute $u=3x$ into the geometric series.", difficulty="easy")

    assert series(1 / (1 - x) ** 2, x, 0, 6).removeO().coeff(x, 3) == 4
    B.mcq(T_PS, "Which is the Maclaurin series for $\\dfrac{1}{(1-x)^2}$?",
          ch("$1+2x+3x^2+4x^3+\\cdots$", "Differentiate $\\frac{1}{1-x}=1+x+x^2+x^3+\\cdots$ term by term: $\\frac{1}{(1-x)^2}=1+2x+3x^2+4x^3+\\cdots$."),
          [ch("$1+x+x^2+x^3+\\cdots$", "That is the series for $\\frac{1}{1-x}$."),
           ch("$1+4x+9x^2+16x^3+\\cdots$", "Squaring the coefficients of $\\frac1{1-x}$ is not the same as squaring the function."),
           ch("$x+2x^2+3x^3+\\cdots$", "That is $\\frac{x}{(1-x)^2}$, which has an extra factor of $x$.")],
          "Termwise differentiation of a power series is allowed inside its interval of convergence.", difficulty="medium")

    assert series(log(1 + x), x, 0, 6).removeO().coeff(x, 3) == R(1, 3)
    B.mcq(T_PS, "Integrating the series for $\\dfrac{1}{1+x}=1-x+x^2-x^3+\\cdots$ term by term gives a series for $\\ln(1+x)$. What is the coefficient of $x^3$ in that series?",
          ch(R(1, 3), "$\\int\\left(1-x+x^2-\\cdots\\right)dx=x-\\frac{x^2}{2}+\\frac{x^3}{3}-\\cdots$ (the constant is 0 because $\\ln1=0$). The coefficient of $x^3$ is $\\frac13$."),
          [ch(R(-1, 3), "The $x^2$ term of the integrand is $+x^2$, and its integral is $+\\frac{x^3}{3}$."),
           ch(R(1, 6), "There is no factorial here: integrating $x^2$ gives $\\frac{x^3}{3}$."),
           ch(3, "Integration divides by the new exponent: $\\int x^2dx=\\frac{x^3}{3}$.")],
          "Integrate each term, and use a known value (here $\\ln1=0$) to find the constant.", difficulty="medium")

    B.mcq(T_PS, f"What is the sum of the series ${SUM0}\\dfrac{{(-1)^n}}{{2n+1}}=1-\\dfrac13+\\dfrac15-\\cdots$?",
          ch(pi / 4, "Integrating $\\frac{1}{1+x^2}=\\sum(-1)^nx^{2n}$ gives $\\arctan x=\\sum\\frac{(-1)^nx^{2n+1}}{2n+1}$, which converges at $x=1$. So the sum is $\\arctan1=\\frac\\pi4$."),
          [ch(pi / 2, "$\\arctan1=\\frac\\pi4$. The value $\\frac\\pi2$ is $\\lim_{x\\to\\infty}\\arctan x$."),
           ch(1, "1 is only the first term."),
           ch(log(2), "$\\ln2$ is the sum of $\\sum\\frac{(-1)^{n+1}}{n}$, which comes from the series for $\\ln(1+x)$ at $x=1$.")],
          "Recognize the series for $\\arctan x$ at $x=1$.", difficulty="medium")

    v = integrate(series(exp(-(x**2)), x, 0, 5).removeO(), (x, 0, 1))
    assert v == R(23, 30)
    B.mcq(T_PS, "Using the first three nonzero terms of the Maclaurin series for $e^{-x^2}$, which is $1-x^2+\\frac{x^4}{2}-\\cdots$, what is the approximation of $\\displaystyle\\int_0^1e^{-x^2}\\,dx$?",
          ch(R(23, 30), "Integrate term by term: $\\int_0^1\\left(1-x^2+\\frac{x^4}{2}\\right)dx=1-\\frac13+\\frac1{10}=\\frac{23}{30}$."),
          [ch(R(1, 2), "This adds the coefficients, $1-1+\\frac12$, which evaluates the integrand at $x=1$ rather than integrating."),
           ch(R(13, 15), "$\\int_0^1\\frac{x^4}2dx=\\frac1{10}$. Leaving out the $\\frac12$ gives $\\frac15$ and the sum $\\frac{13}{15}$."),
           ch(R(2, 3), "This uses the series for $e^{-x}$, $1-x+\\frac{x^2}{2}$, instead of $e^{-x^2}$.")],
          "Integrating a power series term by term turns each $x^k$ into $\\frac{x^{k+1}}{k+1}$.", difficulty="hard")

    s = summation(n_ / 2**n_, (n_, 1, oo))
    assert s == 2
    B.mcq(T_PS, f"What is the sum of the series $\\displaystyle\\sum_{{n=1}}^{{\\infty}}\\dfrac{{n}}{{2^n}}$?",
          ch(2, "From $\\frac{1}{1-x}=\\sum x^n$, differentiate and multiply by $x$: $\\sum nx^n=\\frac{x}{(1-x)^2}$ for $|x|<1$. At $x=\\frac12$: $\\frac{1/2}{1/4}=2$."),
          [ch(1, "$\\sum\\frac{1}{2^n}=1$ is the geometric series without the factor $n$."),
           ch(4, "$\\frac{1}{(1-x)^2}$ at $x=\\frac12$ is 4 and is the sum of $\\sum nx^{n-1}$. The series here has $nx^n$, which has one more factor of $x$."),
           ch(R(1, 2), "$\\frac12$ is the first term only.")],
          "Start with a known geometric series, differentiate, and adjust by a power of $x$.", difficulty="hard")
