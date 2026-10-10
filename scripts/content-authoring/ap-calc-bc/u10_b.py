"""Unit 10, ratio test and absolute convergence, Taylor polynomials, Lagrange error bound, radius and interval of convergence."""
from lib import *
import math

R = Rational
n_ = symbols("n_", integer=True, positive=True)
T_RT, T_TP, T_LB, T_RI = "ratio-test-and-absolute-convergence", "taylor-polynomials", "lagrange-error-bound", "radius-and-interval-of-convergence"
SUM = "\\sum_{n=1}^{\\infty}"
SUM0 = "\\sum_{n=0}^{\\infty}"


def ratio_limit(a):
    return limit(Abs(a.subs(n_, n_ + 1) / a), n_, oo)


def add(B):
    # ------------------------------------------------------------ ratio test and absolute convergence
    L_ = ratio_limit(2**n_ / factorial(n_))
    assert L_ == 0
    B.mcq(T_RT, f"What does the Ratio Test say about the series ${SUM}\\dfrac{{2^n}}{{n!}}$?",
          ch("It converges, because $\\lim\\left|\\frac{a_{n+1}}{a_n}\\right|=0<1$", "$\\frac{a_{n+1}}{a_n}=\\frac{2^{n+1}/(n+1)!}{2^n/n!}=\\frac{2}{n+1}\\to0$. Since the limit is less than 1, the series converges absolutely."),
          [ch("It diverges, because $\\lim\\left|\\frac{a_{n+1}}{a_n}\\right|=2$", "The ratio is $\\frac{2}{n+1}$, because $\\frac{n!}{(n+1)!}=\\frac1{n+1}$. It does not approach 2."),
           ch("The test is inconclusive, because the limit is 1", "The limit is 0, not 1."),
           ch("It diverges, because $\\lim\\left|\\frac{a_{n+1}}{a_n}\\right|=0$", "A limit less than 1 means convergence, not divergence.")],
          "Compute $\\left|\\frac{a_{n+1}}{a_n}\\right|$ and take the limit. Less than 1: converges absolutely; more than 1: diverges; equal to 1: no information.", difficulty="easy")

    L_ = ratio_limit(factorial(n_) / 3**n_)
    assert L_ == oo
    B.mcq(T_RT, f"What does the Ratio Test say about the series ${SUM}\\dfrac{{n!}}{{3^n}}$?",
          ch("It diverges, because $\\lim\\left|\\frac{a_{n+1}}{a_n}\\right|=\\infty>1$", "$\\frac{a_{n+1}}{a_n}=\\frac{(n+1)!/3^{n+1}}{n!/3^n}=\\frac{n+1}{3}\\to\\infty$."),
          [ch("It converges, because $\\lim\\left|\\frac{a_{n+1}}{a_n}\\right|=\\frac13$", "The factor $n+1$ from the factorial remains in the ratio, so the limit is not $\\frac13$."),
           ch("It converges, because the factorial is in the numerator", "A large factorial in the numerator makes the terms grow, not shrink."),
           ch("The test is inconclusive", "The limit is infinite, which is greater than 1, so the test does decide: the series diverges.")],
          "Factorials simplify in the ratio: $\\frac{(n+1)!}{n!}=n+1$.", difficulty="medium")

    L_ = ratio_limit(n_ / 2**n_)
    assert L_ == R(1, 2)
    B.mcq(T_RT, f"For the series ${SUM}\\dfrac{{n}}{{2^n}}$, what is $\\displaystyle\\lim_{{n\\to\\infty}}\\left|\\frac{{a_{{n+1}}}}{{a_n}}\\right|$?",
          ch(R(1, 2), "$\\frac{a_{n+1}}{a_n}=\\frac{(n+1)/2^{n+1}}{n/2^n}=\\frac{n+1}{2n}\\to\\frac12$."),
          [ch(1, "$\\frac{n+1}{n}\\to1$, but the powers of 2 also contribute a factor $\\frac12$."),
           ch(2, "The powers of 2 give $\\frac{2^n}{2^{n+1}}=\\frac12$, not 2."),
           ch(0, "The factor $\\frac{n+1}{n}$ does not go to 0.")],
          "Simplify $\\frac{a_{n+1}}{a_n}$ into pieces whose limits are easy to see.", difficulty="medium")

    B.mcq(T_RT, f"Which statement about the series ${SUM}\\dfrac{{(-1)^nn}}{{n^2+1}}$ is correct?",
          ch("It converges conditionally", "Alternating Series Test: $\\frac{n}{n^2+1}$ is eventually decreasing and approaches 0, so the series converges. But $\\sum\\frac{n}{n^2+1}$ diverges by limit comparison with $\\sum\\frac1n$, so the convergence is not absolute."),
          [ch("It converges absolutely", "$\\sum\\left|\\frac{(-1)^nn}{n^2+1}\\right|=\\sum\\frac{n}{n^2+1}$ behaves like the harmonic series and diverges."),
           ch("It diverges, by the $n$th-Term Test", "The terms approach 0, so the $n$th-Term Test says nothing, and the series does converge."),
           ch("It diverges, because the Ratio Test gives a limit of 1", "A ratio-test limit of 1 is inconclusive, not a proof of divergence.")],
          "Check absolute convergence first. If $\\sum|a_n|$ diverges, test the alternating series itself.", difficulty="medium")

    B.mcq(T_RT, f"The Ratio Test is applied to ${SUM}\\dfrac{{1}}{{n^2}}$ and to ${SUM}\\dfrac{{1}}{{n}}$. What does it show?",
          ch("In both cases the limit of the ratio is 1, so the test is inconclusive for both", "$\\frac{n^2}{(n+1)^2}\\to1$ and $\\frac{n}{n+1}\\to1$. The Ratio Test gives no information when the limit is 1."),
          [ch("Both converge, because the limit is not greater than 1", "A limit equal to 1 is inconclusive. And $\\sum\\frac1n$ diverges."),
           ch("Both diverge, because the limit of the ratio is 1, not less than 1", "A limit of 1 does not imply divergence. And $\\sum\\frac1{n^2}$ converges."),
           ch("$\\sum\\frac{1}{n^2}$ converges and $\\sum\\frac1n$ diverges, as the Ratio Test shows", "The Ratio Test cannot tell them apart. Another test (the $p$-series test) does.")],
          "When the Ratio Test's limit equals 1, use a different test.", difficulty="hard")

    L_ = ratio_limit(n_**2 / 2**n_)
    assert L_ == R(1, 2)
    B.mcq(T_RT, f"Which statement about the series ${SUM}\\dfrac{{(-1)^nn^2}}{{2^n}}$ is correct?",
          ch("It converges absolutely", "For $\\sum\\frac{n^2}{2^n}$ the Ratio Test gives $\\frac{(n+1)^2}{2n^2}\\to\\frac12<1$, so the series of absolute values converges."),
          [ch("It converges conditionally, because it alternates", "The series of absolute values also converges (Ratio Test), so the convergence is absolute, which is stronger."),
           ch("It diverges, because $n^2$ grows faster than $2^n$ for small $n$", "Only the long-run behavior matters, and $2^n$ eventually grows faster than $n^2$."),
           ch("The Ratio Test is inconclusive because the signs alternate", "The Ratio Test uses absolute values, so the alternating sign does not matter.")],
          "Apply the Ratio Test to $|a_n|$. If it converges, the original series converges absolutely.", difficulty="hard")

    # ------------------------------------------------------------ Taylor polynomials
    B.mcq(T_TP, "What is the third-degree Taylor polynomial for $f(x)=e^x$ about $x=0$?",
          ch("$1+x+\\dfrac{x^2}{2}+\\dfrac{x^3}{6}$", "Every derivative of $e^x$ at 0 equals 1, so the coefficients are $\\frac{f^{(k)}(0)}{k!}=\\frac1{k!}$."),
          [ch("$1+x+x^2+x^3$", "The coefficients need the factorials $k!$ in the denominators."),
           ch("$x+\\dfrac{x^2}{2}+\\dfrac{x^3}{6}$", "The constant term $f(0)=1$ is missing."),
           ch("$1+x+\\dfrac{x^2}{2}+\\dfrac{x^3}{3}$", "The coefficient of $x^3$ is $\\frac{1}{3!}=\\frac16$, not $\\frac13$.")],
          "$T_n(x)=\\sum_{k=0}^n\\frac{f^{(k)}(a)}{k!}(x-a)^k$.", difficulty="easy")

    B.mcq(T_TP, "What is the third-degree Taylor polynomial for $f(x)=\\sin x$ about $x=0$?",
          ch("$x-\\dfrac{x^3}{6}$", "$f(0)=0$, $f'(0)=1$, $f''(0)=0$, $f'''(0)=-1$, so $T_3(x)=x-\\frac{x^3}{3!}$."),
          [ch("$x+\\dfrac{x^3}{6}$", "The third derivative of $\\sin x$ is $-\\cos x$, which is $-1$ at 0. The sign is negative."),
           ch("$x-\\dfrac{x^3}{3}$", "The coefficient is $\\frac{f'''(0)}{3!}=-\\frac16$, not $-\\frac13$."),
           ch("$1-\\dfrac{x^2}{2}$", "This is the second-degree polynomial for $\\cos x$.")],
          "List $f$ and its first three derivatives at 0, then divide by the factorials.", difficulty="easy")

    f0, f1, f2 = 3, -1, 4
    T2 = f0 + f1 * (x - 2) + R(f2, 2) * (x - 2) ** 2
    assert expand(T2.subs(x, 2)) == 3
    B.mcq(T_TP, "A function $f$ has $f(2)=3$, $f'(2)=-1$ and $f''(2)=4$. What is the second-degree Taylor polynomial for $f$ about $x=2$?",
          ch("$3-(x-2)+2(x-2)^2$", "$T_2(x)=f(2)+f'(2)(x-2)+\\frac{f''(2)}{2!}(x-2)^2=3-(x-2)+\\frac42(x-2)^2$."),
          [ch("$3-(x-2)+4(x-2)^2$", "The coefficient of the quadratic term is $\\frac{f''(2)}{2!}=2$. The factorial is missing."),
           ch("$3-x+2x^2$", "The polynomial is centered at 2, so the powers are of $(x-2)$, not $x$."),
           ch("$3+(x-2)+2(x-2)^2$", "$f'(2)=-1$, so the linear term is $-(x-2)$.")],
          "A Taylor polynomial about $x=a$ is written in powers of $(x-a)$.", difficulty="medium")

    T2 = (x - 1) - (x - 1) ** 2 / 2
    approx = T2.subs(x, R(6, 5))
    assert approx == R(9, 50) and abs(float(approx) - math.log(1.2)) < 0.01
    B.mcq(T_TP, "The second-degree Taylor polynomial for $f(x)=\\ln x$ about $x=1$ is used to approximate $\\ln(1.2)$. What is the approximation?",
          ch("$0.18$", "$T_2(x)=(x-1)-\\frac{(x-1)^2}{2}$. At $x=1.2$: $0.2-\\frac{0.04}{2}=0.18$."),
          [ch("$0.20$", "This is the first-degree polynomial $T_1(1.2)=0.2$. The quadratic term $-0.02$ is missing."),
           ch("$0.22$", "The quadratic coefficient is negative: $f''(1)=-1$."),
           ch("$0.16$", "The quadratic coefficient is $\\frac{f''(1)}{2!}=-\\frac12$. Without the $\\frac12$ the term would be $-0.04$.")],
          "$f(1)=0$, $f'(1)=1$, $f''(1)=-1$, so $T_2(x)=(x-1)-\\frac12(x-1)^2$.", difficulty="medium")

    T3 = 1 + 2 * x - 3 * x**2 + 2 * x**3
    assert T3.subs(x, R(1, 10)) == R(1172, 1000)
    nofact = 1 + 2 * R(1, 10) - 6 * R(1, 100) + 12 * R(1, 1000)
    no3 = 1 + 2 * R(1, 10) - 3 * R(1, 100) + 12 * R(1, 1000)
    assert (nofact, no3) == (R(1152, 1000), R(1182, 1000))
    B.mcq(T_TP, "A function $f$ has $f(0)=1$, $f'(0)=2$, $f''(0)=-6$ and $f'''(0)=12$. What is the value of the third-degree Taylor polynomial $T_3(x)$ for $f$ about $x=0$ at $x=0.1$?",
          ch("$1.172$", "$T_3(x)=1+2x+\\frac{-6}{2!}x^2+\\frac{12}{3!}x^3=1+2x-3x^2+2x^3$. At $x=0.1$: $1+0.2-0.03+0.002=1.172$."),
          [ch("$1.152$", "This leaves out the factorials: $1+2(0.1)-6(0.01)+12(0.001)$. Each coefficient is $\\frac{f^{(k)}(0)}{k!}$."),
           ch("$1.182$", "The quadratic coefficient was divided by $2!$ but the cubic one was not divided by $3!$."),
           ch("$1.200$", "This is the first-degree polynomial value, $1+2(0.1)$.")],
          "Compute each Taylor coefficient as the derivative divided by the factorial, then substitute.", difficulty="hard")

    # ------------------------------------------------------------ Lagrange error bound
    B.mcq(T_LB, "Let $T_n$ be the $n$th-degree Taylor polynomial for $f$ about $x=a$, and suppose $\\left|f^{(n+1)}(t)\\right|\\le M$ for all $t$ between $a$ and $x$. Which is the Lagrange error bound for $|f(x)-T_n(x)|$?",
          ch("$\\dfrac{M}{(n+1)!}|x-a|^{n+1}$", "The error bound uses the next derivative, $f^{(n+1)}$, with the factorial $(n+1)!$ and the power $n+1$."),
          [ch("$\\dfrac{M}{n!}|x-a|^{n}$", "The exponent and the derivative must both be one higher than the degree: $n+1$."),
           ch("$M|x-a|^{n+1}$", "The factorial $(n+1)!$ is missing."),
           ch("$\\dfrac{M}{(n+1)!}|x-a|^{n}$", "The power is $n+1$, matching the first omitted term.")],
          "The bound looks like the first omitted Taylor term, with $f^{(n+1)}(a)$ replaced by its maximum $M$.", difficulty="easy")

    err = 2 * R(1, 2) ** 4 / factorial(4)
    assert err == R(1, 192)
    B.mcq(T_LB, "The third-degree Taylor polynomial $T_3$ for $f(x)=e^x$ about $x=0$ is used to approximate $e^{0.5}$. Using the fact that $\\left|f^{(4)}(t)\\right|\\le2$ for $0\\le t\\le0.5$, which is the Lagrange error bound?",
          ch(R(1, 192), "$\\left|f(0.5)-T_3(0.5)\\right|\\le\\frac{2}{4!}(0.5)^4=\\frac{2}{24\\cdot16}=\\frac1{192}$."),
          [ch(R(1, 24), "This uses the exponent 3 and $3!$: $\\frac{2}{3!}(0.5)^3$. For $T_3$ the bound uses $n+1=4$."),
           ch(R(1, 32), "This uses $4$ in place of $4!$: $\\frac{2}{4}(0.5)^4$."),
           ch(R(1, 384), "This leaves out the bound $M=2$ on the fourth derivative.")],
          "Here $n=3$, so use $\\frac{M}{4!}|x-0|^4$ with $M=2$ and $x=0.5$.", difficulty="medium")

    B.mcq(T_LB, "The fifth-degree Taylor polynomial $T_5$ for $f(x)=\\sin x$ about $x=0$ is used to approximate $\\sin1$. Which is the Lagrange error bound for this approximation, using $\\left|f^{(6)}(t)\\right|\\le1$ for all $t$?",
          ch(R(1, 720), "$\\frac{M}{6!}|x|^6=\\frac{1}{720}\\cdot1^6=\\frac1{720}$."),
          [ch(R(1, 120), "$\\frac1{5!}$ would be the bound for $T_4$ (it uses $f^{(5)}$). For $T_5$ the bound has $6!$."),
           ch(R(1, 5040), "$\\frac1{7!}$ comes from $f^{(7)}$, the bound for a sixth-degree polynomial. With the given bound on $f^{(6)}$, the error bound for $T_5$ is $\\frac1{6!}=\\frac1{720}$."),
           ch(R(1, 6), "This is $\\frac1{3!}$, the size of the first omitted Taylor term of $T_2$. It is not the bound for $T_5$.")],
          "For $T_n$ the bound uses $f^{(n+1)}$, so for $T_5$ it uses the sixth derivative.", difficulty="medium")

    nfound = next(m for m in range(1, 20) if R(3, factorial(m + 1)) < R(1, 1000))
    assert nfound == 6
    B.mcq(T_LB, "The Taylor polynomial $T_n$ for $f(x)=e^x$ about $x=0$ is used to approximate $e$. Using $\\left|f^{(n+1)}(t)\\right|\\le3$ for $0\\le t\\le1$, what is the smallest $n$ for which the Lagrange error bound guarantees an error less than $0.001$?",
          ch(6, "The bound is $\\frac{3}{(n+1)!}$. We need $(n+1)!>3000$. Since $6!=720<3000$ and $7!=5040>3000$, $n+1=7$, so $n=6$."),
          [ch(7, "$n+1=7$, so $n=6$. The index 7 is the factorial's argument, not the degree."),
           ch(5, "For $n=5$ the bound is $\\frac{3}{720}\\approx0.0042$, which is not less than 0.001."),
           ch(3000, "3000 is the threshold for $(n+1)!$, not for $n$.")],
          "Solve $\\frac{M}{(n+1)!}<0.001$ by trying successive factorials.", difficulty="hard")

    err = 2 * R(1, 2) ** 3 / factorial(3)
    assert err == R(1, 24)
    max3 = max(abs(diff(log(x), x, 3).subs(x, 1)), abs(diff(log(x), x, 3).subs(x, R(3, 2))))
    assert max3 == 2
    B.mcq(T_LB, "The second-degree Taylor polynomial $T_2$ for $f(x)=\\ln x$ about $x=1$ is used to approximate $\\ln(1.5)$. Since $f'''(x)=\\frac{2}{x^3}$, what is the Lagrange error bound?",
          ch(R(1, 24), "On $[1,1.5]$ the largest value of $\\left|f'''(t)\\right|=\\frac{2}{t^3}$ is at $t=1$, where it equals 2. So the error is at most $\\frac{2}{3!}(0.5)^3=\\frac{2}{6\\cdot8}=\\frac1{24}$."),
          [ch(R(1, 81), "This uses $M=\\frac{2}{1.5^3}=\\frac{16}{27}$, the value at the right endpoint, which is the smallest value of $|f'''|$ on the interval, not the maximum."),
           ch(R(1, 4), "This leaves out the $3!$: $2(0.5)^3=\\frac14$."),
           ch(R(1, 8), "This divides by $2!$ instead of $3!$: $\\frac{2(0.5)^3}{2}=\\frac18$.")],
          "$M$ must be an upper bound for $|f'''(t)|$ over the whole interval between $a$ and $x$. Find where $\\frac{2}{t^3}$ is largest.", difficulty="hard")

    # ------------------------------------------------------------ radius and interval of convergence
    B.mcq(T_RI, f"What is the radius of convergence of the power series ${SUM0}\\dfrac{{x^n}}{{3^n}}$?",
          ch(3, "It is geometric with ratio $\\frac x3$, which converges for $\\left|\\frac x3\\right|<1$, that is $|x|<3$. The radius is 3."),
          [ch(R(1, 3), "The ratio is $\\frac{x}{3}$, so convergence needs $|x|<3$. The radius is 3, not $\\frac13$."),
           ch(1, "1 would be the radius of $\\sum x^n$. The $3^n$ in the denominator changes it."),
           ch(oo, "The series is geometric and diverges for large $|x|$.")],
          "Apply the Ratio Test to the terms: $\\left|\\frac{x^{n+1}/3^{n+1}}{x^n/3^n}\\right|=\\frac{|x|}{3}$.", difficulty="easy")

    L = ratio_limit(1 / (n_ * 3**n_))
    assert L == R(1, 3)
    B.mcq(T_RI, f"What is the interval of convergence of the power series ${SUM}\\dfrac{{(x-2)^n}}{{n\\cdot3^n}}$?",
          ch("$[-1,5)$", "The Ratio Test gives $\\frac{|x-2|}{3}<1$, so $-1<x<5$. At $x=5$ the series is $\\sum\\frac1n$ (diverges); at $x=-1$ it is $\\sum\\frac{(-1)^n}{n}$ (converges by the AST)."),
          [ch("$(-1,5)$", "At $x=-1$ the series is the alternating harmonic series, which converges, so $-1$ is included."),
           ch("$[-1,5]$", "At $x=5$ the series is the harmonic series, which diverges."),
           ch("$(-1,5]$", "The endpoints are reversed: the harmonic series at $x=5$ diverges and the alternating one at $x=-1$ converges.")],
          "Find the open interval from the Ratio Test, then test each endpoint separately.", difficulty="medium")

    L = ratio_limit(factorial(n_))
    assert L == oo
    B.mcq(T_RI, f"What is the radius of convergence of the power series ${SUM0}n!\\,x^n$?",
          ch(0, "$\\left|\\frac{(n+1)!\\,x^{n+1}}{n!\\,x^n}\\right|=(n+1)|x|\\to\\infty$ for every $x\\ne0$. The series converges only at $x=0$, so the radius is 0."),
          [ch(1, "The factorials do not cancel to 1; the ratio contains the factor $n+1$."),
           ch(oo, "A factorial in the numerator makes the terms grow, so the series fails to converge for $x\\ne0$. Factorials in the denominator give an infinite radius."),
           ch(R(1, 2), "Nothing in the ratio produces $\\frac12$.")],
          "Compare with $\\sum\\frac{x^n}{n!}$, whose radius is infinite: a factorial in the denominator helps convergence, in the numerator it destroys it.", difficulty="medium")

    L = ratio_limit(1 / factorial(n_))
    assert L == 0
    B.mcq(T_RI, f"What is the interval of convergence of the power series ${SUM0}\\dfrac{{x^n}}{{n!}}$?",
          ch("$(-\\infty,\\infty)$", "$\\left|\\frac{x^{n+1}/(n+1)!}{x^n/n!}\\right|=\\frac{|x|}{n+1}\\to0<1$ for every $x$. The series converges for all real $x$."),
          [ch("$(-1,1)$", "That is the interval for $\\sum x^n$. The factorials make the terms shrink much faster."),
           ch("$\\{0\\}$", "That would be the interval for $\\sum n!\\,x^n$."),
           ch("$[0,\\infty)$", "The ratio $\\frac{|x|}{n+1}\\to0$ works for negative $x$ as well.")],
          "When the ratio limit is 0 regardless of $x$, the radius of convergence is infinite.", difficulty="medium")

    L = ratio_limit((2**n_) / sqrt(n_))
    assert L == 2
    B.mcq(T_RI, f"What is the interval of convergence of the power series ${SUM}\\dfrac{{2^n(x+1)^n}}{{\\sqrt n}}$?",
          ch("$\\left[-\\frac32,-\\frac12\\right)$", "The Ratio Test gives $2|x+1|<1$, so $-\\frac32<x<-\\frac12$. At $x=-\\frac12$ the series is $\\sum\\frac1{\\sqrt n}$ (diverges); at $x=-\\frac32$ it is $\\sum\\frac{(-1)^n}{\\sqrt n}$ (converges by the AST)."),
          [ch("$\\left(-\\frac32,-\\frac12\\right)$", "At $x=-\\frac32$ the series converges by the Alternating Series Test, so that endpoint is included."),
           ch("$\\left[-\\frac32,-\\frac12\\right]$", "At $x=-\\frac12$ the series is $\\sum\\frac1{\\sqrt n}$, a divergent $p$-series ($p=\\frac12$)."),
           ch("$(-3,1)$", "This solves $\\left|\\frac{x+1}{2}\\right|<1$. The factor is $2^n$ in the numerator, so the condition is $|2(x+1)|<1$.")],
          "Radius from the Ratio Test: $2|x+1|<1$. Then check each endpoint with a $p$-series or the AST.", difficulty="medium")

    B.mcq(T_RI, f"What is the interval of convergence of the power series ${SUM}\\dfrac{{(x-1)^n}}{{n^2}}$?",
          ch("$[0,2]$", "The Ratio Test gives $|x-1|<1$. At $x=2$ the series is $\\sum\\frac1{n^2}$ (converges) and at $x=0$ it is $\\sum\\frac{(-1)^n}{n^2}$ (converges absolutely). Both endpoints are included."),
          [ch("$(0,2)$", "Both endpoint series converge ($p$-series with $p=2$, and its alternating version), so the endpoints are included."),
           ch("$[0,2)$", "At $x=2$ the series is $\\sum\\frac{1}{n^2}$, which converges."),
           ch("$(-1,1)$", "This is the interval for $\\sum\\frac{x^n}{n^2}$. The center here is 1, not 0.")],
          "After finding the open interval, test both endpoints; with $n^2$ in the denominator both converge.", difficulty="hard")

    B.mcq(T_RI, f"What is the interval of convergence of the power series ${SUM}\\dfrac{{(3x-2)^n}}{{n}}$?",
          ch("$\\left[\\frac13,1\\right)$", "The series converges when $|3x-2|<1$, so $\\frac13<x<1$. At $x=1$ it is $\\sum\\frac1n$ (diverges); at $x=\\frac13$ it is $\\sum\\frac{(-1)^n}{n}$ (converges). The radius of convergence in $x$ is $\\frac13$."),
          [ch("$\\left(\\frac13,1\\right]$", "The endpoints are reversed: the harmonic series at $x=1$ diverges."),
           ch("$(-1,1)$", "The condition is $|3x-2|<1$, not $|x|<1$."),
           ch("$\\left[\\frac13,1\\right]$", "At $x=1$ the series is the harmonic series, which diverges.")],
          "The series is geometric-like in $3x-2$: solve $|3x-2|<1$, then test both endpoints in the original series.", difficulty="hard")
