"""Unit 10 free-response prompts (9 points each, in the style of the AP exam)."""
from lib import *
import math

R = Rational
n_ = symbols("n_", integer=True, positive=True)
T_GS, T_RT, T_TP, T_LB, T_RI, T_TM, T_PS, T_AS = (
    "convergent-and-geometric-series", "ratio-test-and-absolute-convergence", "taylor-polynomials", "lagrange-error-bound",
    "radius-and-interval-of-convergence", "taylor-and-maclaurin-series", "power-series-representations", "alternating-series-and-error-bound",
)


def add(B):
    # 1. Taylor polynomial and Lagrange error bound for ln x about 1
    T3 = (x - 1) - (x - 1) ** 2 / 2 + (x - 1) ** 3 / 3
    f = log(x)
    assert all(simplify(T3.diff(x, k).subs(x, 1) - f.diff(x, k).subs(x, 1)) == 0 for k in range(4))
    a3 = T3.subs(x, R(6, 5))
    assert a3 == R(137, 750)
    assert diff(f, x, 4) == -6 / x**4 and max(abs(diff(f, x, 4).subs(x, c_)) for c_ in (1, R(6, 5))) == 6
    bound = R(6, 24) * R(1, 5) ** 4
    assert bound == R(1, 2500)
    assert abs(math.log(1.2) - float(a3)) < float(bound)
    B.frq(T_LB,
          "Let $f(x)=\\ln x$.\n\n**(a)** Find the third-degree Taylor polynomial $P(x)$ for $f$ about $x=1$.\n\n**(b)** Use $P(x)$ to approximate $\\ln(1.2)$.\n\n**(c)** It can be shown that $f^{(4)}(x)=-\\dfrac{6}{x^4}$. Use the Lagrange error bound to show that the error in your approximation from part (b) is less than $0.0005$.",
          [(1, "(a) $f(1)=0$, $f'(1)=1$, $f''(1)=-1$, $f'''(1)=2$"),
           (1, "(a) Coefficients $0,\\,1,\\,-\\frac12,\\,\\frac13$ (dividing by $k!$)"),
           (1, "(a) $P(x)=(x-1)-\\frac{(x-1)^2}{2}+\\frac{(x-1)^3}{3}$"),
           (1, "(b) Substitutes $x=1.2$: $0.2-\\frac{0.04}{2}+\\frac{0.008}{3}$"),
           (1, "(b) $\\approx0.1827$"),
           (1, "(c) Uses the error bound $\\frac{M}{4!}|1.2-1|^4$"),
           (1, "(c) Justifies $M=6$: $\\left|f^{(4)}(t)\\right|=\\frac{6}{t^4}\\le6$ for $1\\le t\\le1.2$"),
           (1, "(c) Computes $\\frac{6}{24}(0.2)^4=0.0004$"),
           (1, "(c) Concludes $0.0004<0.0005$")],
          "(a) $f'(x)=\\frac1x$, $f''(x)=-\\frac1{x^2}$, $f'''(x)=\\frac{2}{x^3}$, so $f(1)=0$, $f'(1)=1$, $f''(1)=-1$, $f'''(1)=2$. Then $P(x)=(x-1)-\\frac{(x-1)^2}{2!}+\\frac{2(x-1)^3}{3!}=(x-1)-\\frac{(x-1)^2}{2}+\\frac{(x-1)^3}{3}$.\n(b) $P(1.2)=0.2-0.02+\\frac{0.008}{3}\\approx0.18267$, so $\\ln(1.2)\\approx0.1827$.\n(c) For $1\\le t\\le1.2$, $\\left|f^{(4)}(t)\\right|=\\frac{6}{t^4}\\le6$. The error is at most $\\frac{6}{4!}(1.2-1)^4=\\frac14(0.0016)=0.0004<0.0005$.")

    # 2. power series, interval, derivative, closed form
    a = (x - 2) ** n_ / (n_ * 3**n_)
    for xv, nv in ((R(7, 2), 5), (R(-1, 2), 9), (R(5, 2), 20)):  # the ratio is n/(n+1) * (x-2)/3
        assert a.subs({x: xv, n_: nv + 1}) / a.subs({x: xv, n_: nv}) == R(nv, nv + 1) * (xv - 2) / 3
    fprime = 1 / (5 - x)
    xv = R(7, 2)  # partial sums of the derivative series approach 1/(5 - x) inside the interval
    assert abs(float(sum((xv - 2) ** (k_ - 1) / R(3) ** k_ for k_ in range(1, 80))) - float(fprime.subs(x, xv))) < 1e-12
    F = log(3) - log(5 - x)
    assert simplify(diff(F, x) - fprime) == 0 and F.subs(x, 2) == 0 and simplify(F.subs(x, -1) + log(2)) == 0
    B.frq(T_RI,
          "Let $f$ be the function defined by the power series $f(x)=\\displaystyle\\sum_{n=1}^{\\infty}\\frac{(x-2)^n}{n\\cdot3^n}$.\n\n**(a)** Find the interval of convergence of the power series. Show the work that leads to your answer.\n\n**(b)** Write the first three nonzero terms and the general term of the power series for $f'(x)$, and find the sum of that series as a function of $x$ on the interval where it converges.\n\n**(c)** Use your answer to part (b), together with $f(2)=0$, to find a closed-form expression for $f(x)$.",
          [(1, "(a) Ratio Test: $\\lim\\left|\\frac{a_{n+1}}{a_n}\\right|=\\frac{|x-2|}{3}$"),
           (1, "(a) Radius of convergence 3, open interval $(-1,5)$"),
           (1, "(a) At $x=5$: $\\sum\\frac1n$, diverges (harmonic series)"),
           (1, "(a) At $x=-1$: $\\sum\\frac{(-1)^n}{n}$, converges (Alternating Series Test)"),
           (1, "(a) Interval of convergence $[-1,5)$"),
           (1, "(b) $f'(x)=\\frac13+\\frac{x-2}{9}+\\frac{(x-2)^2}{27}+\\cdots+\\frac{(x-2)^{n-1}}{3^n}+\\cdots$"),
           (1, "(b) Recognizes a geometric series with first term $\\frac13$ and ratio $\\frac{x-2}{3}$; sum $\\frac{1/3}{1-(x-2)/3}=\\frac{1}{5-x}$"),
           (1, "(c) Antidifferentiates: $f(x)=-\\ln(5-x)+C$"),
           (1, "(c) Uses $f(2)=0$ to get $C=\\ln3$: $f(x)=\\ln3-\\ln(5-x)=\\ln\\frac{3}{5-x}$")],
          "(a) $\\left|\\frac{a_{n+1}}{a_n}\\right|=\\frac{|x-2|^{n+1}}{(n+1)3^{n+1}}\\cdot\\frac{n\\,3^n}{|x-2|^n}=\\frac{n}{n+1}\\cdot\\frac{|x-2|}{3}\\to\\frac{|x-2|}{3}$. This is less than 1 for $-1<x<5$. At $x=5$ the series is $\\sum\\frac1n$ (divergent). At $x=-1$ it is $\\sum\\frac{(-1)^n}{n}$ (convergent by the AST). The interval is $[-1,5)$.\n(b) $f'(x)=\\sum_{n=1}^\\infty\\frac{(x-2)^{n-1}}{3^n}=\\frac13+\\frac{x-2}{9}+\\frac{(x-2)^2}{27}+\\cdots$. This is geometric with first term $\\frac13$ and ratio $\\frac{x-2}{3}$, so for $|x-2|<3$ it sums to $\\frac{1/3}{1-\\frac{x-2}{3}}=\\frac{1}{3-(x-2)}=\\frac{1}{5-x}$.\n(c) $f(x)=\\int\\frac{dx}{5-x}=-\\ln(5-x)+C$. Since $f(2)=0$: $-\\ln3+C=0$, so $C=\\ln3$ and $f(x)=\\ln3-\\ln(5-x)=\\ln\\frac{3}{5-x}$.")

    # 3. convergence of three series
    assert limit(((n_ + 1) / (n_**3 + 1)) / (1 / n_**2), n_, oo) == 1
    assert limit(3 ** (n_ + 1) / factorial(n_ + 1) / (3**n_ / factorial(n_)), n_, oo) == 0
    B.frq(T_RT,
          "For each of the following series, determine whether it converges absolutely, converges conditionally, or diverges. Justify each answer with a convergence test.\n\n**(a)** $\\displaystyle\\sum_{n=1}^{\\infty}\\frac{(-1)^n}{\\sqrt n}$\n\n**(b)** $\\displaystyle\\sum_{n=1}^{\\infty}\\frac{n+1}{n^3+1}$\n\n**(c)** $\\displaystyle\\sum_{n=1}^{\\infty}\\frac{3^n}{n!}$",
          [(1, "(a) Alternating Series Test: $\\frac1{\\sqrt n}$ is decreasing and approaches 0, so the series converges"),
           (1, "(a) The series of absolute values $\\sum\\frac1{\\sqrt n}$ is a $p$-series with $p=\\frac12\\le1$, so it diverges"),
           (1, "(a) Conclusion: converges conditionally"),
           (1, "(b) Chooses a valid test (Limit Comparison with $\\sum\\frac1{n^2}$)"),
           (1, "(b) $\\lim\\frac{(n+1)/(n^3+1)}{1/n^2}=1$, finite and positive"),
           (1, "(b) $\\sum\\frac1{n^2}$ converges ($p$-series, $p=2$), so the series converges (absolutely, since its terms are positive)"),
           (1, "(c) Ratio Test: $\\left|\\frac{a_{n+1}}{a_n}\\right|=\\frac{3}{n+1}$"),
           (1, "(c) The limit is $0<1$"),
           (1, "(c) Conclusion: converges absolutely")],
          "(a) The terms $a_n=\\frac{1}{\\sqrt n}$ are positive, decreasing and tend to 0, so the series converges by the Alternating Series Test. But $\\sum\\left|\\frac{(-1)^n}{\\sqrt n}\\right|=\\sum\\frac1{n^{1/2}}$ diverges ($p=\\frac12\\le1$). It converges conditionally.\n(b) Compare with $\\sum\\frac1{n^2}$: $\\lim_{n\\to\\infty}\\frac{(n+1)/(n^3+1)}{1/n^2}=\\lim\\frac{n^3+n^2}{n^3+1}=1$. Since $\\sum\\frac{1}{n^2}$ converges, so does the series (and, having positive terms, it converges absolutely).\n(c) $\\left|\\frac{a_{n+1}}{a_n}\\right|=\\frac{3^{n+1}/(n+1)!}{3^n/n!}=\\frac{3}{n+1}\\to0<1$. By the Ratio Test the series converges absolutely.")

    # 4. e^{-x^2}: series, integral approximation, alternating error bound
    ser = series(exp(-(x**2)), x, 0, 9).removeO()
    assert [ser.coeff(x, k) for k in (0, 2, 4, 6)] == [1, -1, R(1, 2), R(-1, 6)]
    approx = integrate(1 - x**2 + x**4 / 2, (x, 0, R(1, 2)))
    assert approx == R(443, 960)
    nxt = R(1, 2) ** 7 / 42
    assert nxt == R(1, 5376) and R(1, 2) ** 7 / 42 < R(1, 320) / 1
    true = integrate(exp(-(x**2)), (x, 0, R(1, 2))).evalf()
    assert abs(float(true) - float(approx)) < float(nxt)
    B.frq(T_TM,
          "Let $g(x)=e^{-x^2}$.\n\n**(a)** Write the first four nonzero terms of the Maclaurin series for $g(x)$.\n\n**(b)** Write the general term of the series.\n\n**(c)** Use the first three nonzero terms of the series for $g$ to approximate $\\displaystyle\\int_0^{1/2}e^{-x^2}\\,dx$.\n\n**(d)** The series you obtain for the integral in part (c) is alternating, with terms that decrease in absolute value. Use the Alternating Series Error Bound to give an upper bound on the error in your approximation.",
          [(1, "(a) Substitutes $-x^2$ into the series for $e^u$"),
           (1, "(a) $1-x^2+\\frac{x^4}{2}-\\frac{x^6}{6}$"),
           (1, "(b) General term $\\frac{(-1)^nx^{2n}}{n!}$"),
           (1, "(b) Includes the index range $n\\ge0$ (equivalent forms accepted)"),
           (1, "(c) Integrates the first three terms: $\\int_0^{1/2}\\left(1-x^2+\\frac{x^4}{2}\\right)dx=\\left[x-\\frac{x^3}{3}+\\frac{x^5}{10}\\right]_0^{1/2}$"),
           (1, "(c) Evaluates at $\\frac12$: $\\frac12-\\frac1{24}+\\frac1{320}$"),
           (1, "(c) $\\frac{443}{960}\\approx0.4615$"),
           (1, "(d) The first omitted term of the integrated series is $\\frac{x^7}{42}$ at $x=\\frac12$, that is, $\\frac{(1/2)^7}{7\\cdot3!}$"),
           (1, "(d) Error $\\le\\frac{1}{5376}\\approx0.00019$")],
          "(a) $e^u=1+u+\\frac{u^2}{2!}+\\frac{u^3}{3!}+\\cdots$ with $u=-x^2$: $1-x^2+\\frac{x^4}{2}-\\frac{x^6}{6}+\\cdots$.\n(b) $\\sum_{n=0}^\\infty\\frac{(-1)^nx^{2n}}{n!}$.\n(c) $\\int_0^{1/2}\\left(1-x^2+\\frac{x^4}{2}\\right)dx=\\left[x-\\frac{x^3}{3}+\\frac{x^5}{10}\\right]_0^{1/2}=\\frac12-\\frac1{24}+\\frac1{320}=\\frac{443}{960}\\approx0.4615$.\n(d) Integrating the series term by term gives $\\sum_{n=0}^\\infty\\frac{(-1)^n(1/2)^{2n+1}}{n!\\,(2n+1)}=\\frac12-\\frac1{24}+\\frac1{320}-\\frac{1}{5376}+\\cdots$, which alternates with decreasing terms. The error is at most the first omitted term, $\\frac{1}{5376}\\approx0.00019$.")

    # 5. arctan series and pi
    N = next(k_ for k_ in range(1, 1000) if R(4, 2 * k_ + 1) < R(1, 100))
    assert N == 200
    assert R(4, 2 * 199 + 1) > R(1, 100)
    B.frq(T_PS,
          "**(a)** Write the first four nonzero terms and the general term of the Maclaurin series for $\\dfrac{1}{1+x^2}$, and state its radius of convergence.\n\n**(b)** Use your answer to part (a) to find the first four nonzero terms and the general term of the Maclaurin series for $\\arctan x$.\n\n**(c)** The series for $\\arctan x$ converges at $x=1$. Use this to write $\\pi$ as an infinite series. If you add the first $N$ terms of the series for $\\frac\\pi4$ and multiply by 4 to approximate $\\pi$, what is the least $N$ for which the Alternating Series Error Bound guarantees an error less than $0.01$?",
          [(1, "(a) Substitutes $-x^2$ into $\\frac1{1-u}=\\sum u^n$"),
           (1, "(a) $1-x^2+x^4-x^6+\\cdots=\\sum(-1)^nx^{2n}$"),
           (1, "(a) Radius of convergence 1 (from $|x^2|<1$)"),
           (1, "(b) Integrates term by term"),
           (1, "(b) $x-\\frac{x^3}{3}+\\frac{x^5}{5}-\\frac{x^7}{7}+\\cdots$ with constant 0 (from $\\arctan0=0$)"),
           (1, "(b) General term $\\frac{(-1)^nx^{2n+1}}{2n+1}$"),
           (1, "(c) $\\pi=4\\left(1-\\frac13+\\frac15-\\cdots\\right)=4\\sum\\frac{(-1)^n}{2n+1}$, since $\\arctan1=\\frac\\pi4$"),
           (1, "(c) Error after $N$ terms is at most $4\\cdot\\frac{1}{2N+1}$"),
           (1, "(c) Solves $\\frac{4}{2N+1}<0.01$ to get $N=200$")],
          "(a) $\\frac{1}{1+x^2}=\\sum_{n=0}^\\infty(-x^2)^n=1-x^2+x^4-x^6+\\cdots$, valid for $|x^2|<1$, so the radius of convergence is 1.\n(b) $\\arctan x=\\int_0^x\\frac{dt}{1+t^2}=x-\\frac{x^3}{3}+\\frac{x^5}{5}-\\frac{x^7}{7}+\\cdots=\\sum_{n=0}^\\infty\\frac{(-1)^nx^{2n+1}}{2n+1}$ (the constant is 0 because $\\arctan0=0$).\n(c) At $x=1$: $\\frac\\pi4=1-\\frac13+\\frac15-\\cdots$, so $\\pi=4\\sum_{n=0}^\\infty\\frac{(-1)^n}{2n+1}$. After $N$ terms the error in the series for $\\frac\\pi4$ is at most the first omitted term $\\frac{1}{2N+1}$, so after multiplying by 4 it is at most $\\frac{4}{2N+1}$. We need $\\frac{4}{2N+1}<0.01$, so $2N+1>400$ and $N\\ge200$. (With $N=199$ the bound is $\\frac{4}{399}>0.01$.)")
