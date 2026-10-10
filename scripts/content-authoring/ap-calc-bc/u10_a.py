"""Unit 10, geometric series, divergence / integral / p-series tests, comparison tests, alternating series."""
from lib import *

R = Rational
n_ = symbols("n_", integer=True, positive=True)
T_GS, T_DT, T_CT, T_AS = "convergent-and-geometric-series", "divergence-integral-and-p-series", "comparison-tests", "alternating-series-and-error-bound"
SUM = "\\sum_{n=1}^{\\infty}"
SUM0 = "\\sum_{n=0}^{\\infty}"


def add(B):
    # ------------------------------------------------------------ geometric series
    s = summation(3 * R(1, 2) ** n_, (n_, 0, oo))
    assert s == 6
    B.mcq(T_GS, f"What is the sum of the series ${SUM0}3\\left(\\frac12\\right)^n$?",
          ch(6, "A geometric series with first term $a=3$ and ratio $r=\\frac12$ has sum $\\frac{a}{1-r}=\\frac{3}{1/2}=6$."),
          [ch(3, "3 is the first term. The sum includes all the terms."),
           ch(2, "This uses $\\frac{a}{1+r}=\\frac{3}{3/2}$. The formula has $1-r$ in the denominator."),
           ch("The series diverges", "A geometric series converges when $|r|<1$, and here $r=\\frac12$.")],
          "For $|r|<1$, $\\sum_{n=0}^\\infty ar^n=\\frac{a}{1-r}$.", difficulty="easy")

    s = summation(4 * R(-1, 3) ** (n_ - 1), (n_, 1, oo))
    assert s == 3
    B.mcq(T_GS, f"What is the sum of the series ${SUM}4\\left(-\\frac13\\right)^{{n-1}}$?",
          ch(3, "The first term is $a=4$ and the ratio is $r=-\\frac13$. The sum is $\\frac{4}{1-(-1/3)}=\\frac{4}{4/3}=3$."),
          [ch(6, "This uses $\\frac{a}{1-|r|}=\\frac{4}{2/3}$. The ratio is negative, so the denominator is $1-r=1+\\frac13$."),
           ch(4, "4 is the first term, not the sum."),
           ch("The series diverges", "A negative ratio does not cause divergence. The series converges because $|r|=\\frac13<1$.")],
          "Identify the first term and the common ratio (with its sign), and check $|r|<1$.", difficulty="easy")

    s = summation(5 / 3**n_, (n_, 1, oo))
    assert s == R(5, 2)
    B.mcq(T_GS, f"What is the sum of the series ${SUM}\\dfrac{{5}}{{3^n}}$?",
          ch(R(5, 2), "The first term (at $n=1$) is $\\frac53$ and the ratio is $\\frac13$. The sum is $\\frac{5/3}{1-1/3}=\\frac{5/3}{2/3}=\\frac52$."),
          [ch(R(15, 2), "This uses 5 as the first term, which is the value at $n=0$. The series starts at $n=1$, so the first term is $\\frac53$."),
           ch(R(5, 3), "$\\frac53$ is the first term only."),
           ch(R(1, 2), "The first term is $\\frac53$, not $\\frac13$.")],
          "When the series starts at $n=1$, the first term is the value at $n=1$.", difficulty="medium")

    B.mcq(T_GS, "The repeating decimal $0.272727\\ldots$ can be written as the geometric series $\\frac{27}{100}+\\frac{27}{100^2}+\\frac{27}{100^3}+\\cdots$. What fraction is it equal to?",
          ch(R(3, 11), "$a=\\frac{27}{100}$ and $r=\\frac1{100}$, so the sum is $\\frac{27/100}{1-1/100}=\\frac{27}{99}=\\frac{3}{11}$."),
          [ch(R(27, 100), "This is the first term only."),
           ch(R(27, 101), "This uses $1+r$ in the denominator: $\\frac{27/100}{1+1/100}$."),
           ch(R(3, 10), "This uses the ratio $\\frac1{10}$: $\\frac{27/100}{1-1/10}$. The repeating block has two digits, so each term is $\\frac{1}{100}$ of the one before.")],
          "A repeating block of $k$ digits is a geometric series with ratio $10^{-k}$.", difficulty="medium")

    B.mcq(T_GS, f"For which values of $x$ does the series ${SUM0}\\dfrac{{(x-1)^n}}{{2^n}}$ converge?",
          ch("$-1<x<3$", "It is geometric with ratio $\\frac{x-1}{2}$, so it converges exactly when $\\left|\\frac{x-1}{2}\\right|<1$, that is, $|x-1|<2$, which is $-1<x<3$."),
          [ch("$0<x<2$", "This solves $|x-1|<1$. The ratio is $\\frac{x-1}{2}$, so the condition is $|x-1|<2$."),
           ch("$x<3$", "The condition is an absolute value: $-2<x-1<2$. Values below $-1$ also make the series diverge."),
           ch("$-2<x<2$", "This solves $|x|<2$. The ratio involves $x-1$, not $x$.")],
          "A geometric series converges exactly when $|r|<1$.", difficulty="medium")

    s4 = sum(6 * R(1, 3) ** k for k in range(4))
    assert s4 == R(80, 9)
    B.mcq(T_GS, "What is the sum of the first four terms of the geometric series $6+2+\\frac23+\\frac29+\\cdots$?",
          ch(R(80, 9), "$S_4=a\\cdot\\frac{1-r^4}{1-r}=6\\cdot\\frac{1-\\frac1{81}}{\\frac23}=9\\cdot\\frac{80}{81}=\\frac{80}{9}$. (Directly: $6+2+\\frac23+\\frac29=\\frac{54+18+6+2}{9}$.)"),
          [ch(8, "This adds only the first two terms."),
           ch(R(26, 3), "This adds the first three terms, $6+2+\\frac23$."),
           ch(9, "This is the sum of the whole infinite series, $\\frac{6}{1-1/3}$. The question asks for four terms.")],
          "For a finite geometric sum, $S_n=a\\frac{1-r^n}{1-r}$.", difficulty="hard")

    # ------------------------------------------------------------ nth-term, integral and p-series tests
    B.mcq(T_DT, "Which of the following series can be shown to diverge by the $n$th-Term Test for Divergence?",
          ch(f"${SUM}\\dfrac{{n}}{{n+1}}$", "The terms approach $\\lim\\frac{n}{n+1}=1\\ne0$, so the series diverges by the $n$th-Term Test."),
          [ch(f"${SUM}\\dfrac{{1}}{{n}}$", "The terms approach 0, so the test is inconclusive. (This series does diverge, but a different test, such as the integral test, shows it.)"),
           ch(f"${SUM}\\dfrac{{1}}{{n^2}}$", "The terms approach 0, so the test says nothing. The series converges, as a $p$-series with $p=2$."),
           ch(f"${SUM}\\dfrac{{(-1)^n}}{{n}}$", "The terms approach 0, so the test is inconclusive. The series converges by the alternating series test.")],
          "If $\\lim a_n\\ne0$ (or does not exist), then $\\sum a_n$ diverges. If $\\lim a_n=0$, the test gives no information.", difficulty="easy")

    B.mcq(T_DT, "Which of the following series converges?",
          ch(f"${SUM}\\dfrac{{1}}{{n^{{3/2}}}}$", "It is a $p$-series with $p=\\frac32>1$."),
          [ch(f"${SUM}\\dfrac{{1}}{{\\sqrt n}}$", "It is a $p$-series with $p=\\frac12\\le1$, so it diverges."),
           ch(f"${SUM}\\dfrac{{1}}{{n}}$", "This is the harmonic series, the $p$-series with $p=1$, which diverges."),
           ch(f"${SUM}\\dfrac{{1}}{{n^{{0.9}}}}$", "A $p$-series with $p=0.9<1$ diverges.")],
          "The $p$-series $\\sum\\frac1{n^p}$ converges exactly when $p>1$.", difficulty="easy")

    f = 1 / (x * log(x) ** 2)
    iv = integrate(f, (x, 2, oo))
    assert simplify(iv - 1 / log(2)) == 0
    B.mcq(T_DT, f"Consider the series ${SUM}\\dfrac{{1}}{{(n+1)\\left(\\ln(n+1)\\right)^2}}$, whose terms are $f(n+1)$ for the function $f(x)=\\dfrac{{1}}{{x(\\ln x)^2}}$. Which statement is correct?",
          ch("The series converges, because $\\int_2^\\infty\\frac{dx}{x(\\ln x)^2}=\\frac{1}{\\ln2}$ is finite", "$f$ is positive, continuous and decreasing for $x\\ge2$. With $u=\\ln x$: $\\int_2^b\\frac{dx}{x(\\ln x)^2}=\\frac{1}{\\ln2}-\\frac{1}{\\ln b}\\to\\frac1{\\ln2}$. By the Integral Test, the series converges."),
          [ch("The series diverges, because $\\int_2^\\infty\\frac{dx}{x(\\ln x)^2}$ is infinite", "The integral is finite: $\\frac1{\\ln b}\\to0$."),
           ch("The series converges to $\\frac{1}{\\ln2}$", "The Integral Test says the series converges; it does not say the sum equals the integral."),
           ch("The series diverges, because its terms behave like $\\frac1n$", "The factor $(\\ln n)^2$ makes the terms smaller than $\\frac1n$ by more than any constant; the comparison with $\\frac1n$ does not decide convergence.")],
          "The Integral Test: if $f$ is positive, continuous and decreasing, then $\\sum f(n)$ and $\\int f(x)\\,dx$ converge or diverge together.", difficulty="medium")

    f = x * exp(-(x**2))
    assert integrate(f, (x, 1, oo)) == exp(-1) / 2 and diff(f, x).subs(x, 1) < 0
    B.mcq(T_DT, f"Which statement about the series ${SUM}ne^{{-n^2}}$ is correct?",
          ch("It converges: $f(x)=xe^{-x^2}$ is positive and decreasing for $x\\ge1$, and $\\int_1^\\infty xe^{-x^2}dx=\\frac1{2e}$ is finite", "$f'(x)=\\left(1-2x^2\\right)e^{-x^2}<0$ for $x\\ge1$, so the Integral Test applies. With $u=-x^2$: $\\int_1^\\infty xe^{-x^2}dx=\\left[-\\frac12e^{-x^2}\\right]_1^\\infty=\\frac1{2e}$."),
          [ch("It diverges, because $f(x)=xe^{-x^2}$ is not decreasing on all of $[0,\\infty)$, so the Integral Test fails", "The Integral Test only needs $f$ to be decreasing eventually (here for $x\\ge1$). The first terms do not affect convergence."),
           ch("It converges, and its sum is $\\frac{1}{2e}$, the value of the improper integral", "The integral's value is not the sum of the series; the Integral Test only decides whether the series converges."),
           ch("The Integral Test cannot be used, because $e^{-x^2}$ has no elementary antiderivative, so the integral cannot be evaluated", "The function here is $xe^{-x^2}$, not $e^{-x^2}$, and it is easy to integrate by substitution ($u=-x^2$), so the test is a good choice.")],
          "Check the hypotheses (positive, continuous, decreasing), then evaluate the improper integral.", difficulty="medium")

    B.mcq(T_DT, f"Which statement about the series ${SUM}\\dfrac{{1}}{{n+3}}$ is correct?",
          ch("It diverges, because it is the harmonic series with its first few terms removed", "Removing or adding finitely many terms does not change convergence. $\\sum\\frac{1}{n+3}=\\frac14+\\frac15+\\frac16+\\cdots$ diverges like $\\sum\\frac1n$."),
          [ch("It converges, because $\\frac{1}{n+3}\\to0$", "Terms approaching 0 is necessary for convergence, not sufficient (the harmonic series is the standard counterexample)."),
           ch("It converges, because it is a $p$-series with $p=1$", "A $p$-series with $p=1$ diverges, and this series diverges for the same reason."),
           ch("It converges, because the $+3$ makes the terms smaller than those of the harmonic series", "The terms are smaller than $\\frac1n$, but a series smaller than a divergent one proves nothing.")],
          "Compare with $\\sum\\frac1n$: shifting the index does not change the behavior.", difficulty="medium")

    B.mcq(T_DT, "For which values of $p$ does the series $\\displaystyle\\sum_{n=1}^{\\infty}\\frac{1}{n^p}$ converge?",
          ch("$p>1$", "By the Integral Test, $\\int_1^\\infty x^{-p}dx$ is finite exactly when $p>1$."),
          [ch("$p\\ge1$", "At $p=1$ this is the harmonic series, which diverges."),
           ch("$p<1$", "That is where $\\int_0^1x^{-p}dx$ converges, not the series."),
           ch("$p>0$", "For $0<p\\le1$ the terms still go to 0, but the series diverges.")],
          "Remember the borderline: $p=1$ diverges.", difficulty="easy")

    B.mcq(T_DT, "A series $\\sum a_n$ has $\\displaystyle\\lim_{n\\to\\infty}a_n=0$. Which conclusion is justified by that fact alone?",
          ch("No conclusion can be drawn about whether the series converges", "Both $\\sum\\frac1n$ (divergent) and $\\sum\\frac{1}{n^2}$ (convergent) have terms that approach 0."),
          [ch("The series converges, because terms that approach 0 let the partial sums settle down", "The harmonic series is a counterexample: its terms approach 0 but it diverges."),
           ch("The series diverges, because $\\lim a_n=0$ is the condition the test uses to detect divergence", "Divergence follows from $\\lim a_n\\ne0$, not from $\\lim a_n=0$."),
           ch("The series converges absolutely, because the terms are eventually smaller than those of any geometric series", "Terms approaching 0 does not even guarantee ordinary convergence, so absolute convergence is out of reach too.")],
          "The $n$th-Term Test can prove divergence, but never convergence.", difficulty="medium")

    # ------------------------------------------------------------ comparison tests
    B.mcq(T_CT, f"Which statement about the series ${SUM}\\dfrac{{1}}{{n^2+3}}$ is correct?",
          ch("It converges, by direct comparison with $\\sum\\frac{1}{n^2}$", "For every $n$, $0<\\frac{1}{n^2+3}<\\frac{1}{n^2}$, and $\\sum\\frac1{n^2}$ converges, so the smaller series converges too."),
          [ch("It diverges, by direct comparison with $\\sum\\frac1{n^2}$", "Being smaller than a convergent series cannot make a series diverge."),
           ch("It converges, by direct comparison with $\\sum\\frac1n$", "$\\sum\\frac1n$ diverges, so being smaller than it proves nothing."),
           ch("The comparison test is inconclusive", "The inequality $\\frac{1}{n^2+3}<\\frac1{n^2}$ together with convergence of $\\sum\\frac1{n^2}$ settles it.")],
          "Direct Comparison: if $0\\le a_n\\le b_n$ and $\\sum b_n$ converges, then $\\sum a_n$ converges.", difficulty="easy")

    B.mcq(T_CT, f"Which statement about the series $\\displaystyle\\sum_{{n=2}}^{{\\infty}}\\dfrac{{1}}{{\\sqrt n-1}}$ is correct?",
          ch("It diverges, because $\\frac{1}{\\sqrt n-1}>\\frac1{\\sqrt n}$ and $\\sum\\frac1{\\sqrt n}$ diverges", "For $n\\ge2$ the denominator $\\sqrt n-1$ is smaller than $\\sqrt n$, so each term is larger. A series larger than a divergent $p$-series ($p=\\frac12$) diverges."),
          [ch("It converges, because $\\frac1{\\sqrt n-1}\\to0$", "Terms approaching 0 is not enough."),
           ch("It converges, because $\\frac{1}{\\sqrt n-1}<\\frac1{\\sqrt n}$", "The inequality goes the other way: the smaller denominator makes the term larger."),
           ch("It converges, because it is a $p$-series with $p=\\frac12$", "A $p$-series with $p\\le1$ diverges. And this series is not exactly a $p$-series.")],
          "Check the direction of the inequality when comparing denominators: a smaller denominator means a larger term.", difficulty="medium")

    lim = limit(((2 * n_ + 1) / (n_**3 - n_ + 5)) / (1 / n_**2), n_, oo)
    assert lim == 2
    B.mcq(T_CT, f"Which statement about the series ${SUM}\\dfrac{{2n+1}}{{n^3-n+5}}$ is correct?",
          ch("It converges, by the Limit Comparison Test with $\\sum\\frac1{n^2}$", "$\\lim\\frac{(2n+1)/(n^3-n+5)}{1/n^2}=\\lim\\frac{2n^3+n^2}{n^3-n+5}=2$, a finite positive number, and $\\sum\\frac1{n^2}$ converges."),
          [ch("It diverges, by the Limit Comparison Test with $\\sum\\frac1n$", "The terms behave like $\\frac{2n}{n^3}=\\frac{2}{n^2}$, not $\\frac1n$. The limit with $\\frac1n$ is 0, which is not a useful comparison."),
           ch("It diverges, because the limit of the ratio is 2", "With a convergent comparison series and a finite positive limit, the conclusion is convergence."),
           ch("It converges, because the terms approach 0", "Terms approaching 0 is necessary but not sufficient.")],
          "Compare with the series of the dominant terms: $\\frac{2n}{n^3}=\\frac2{n^2}$. If the limit of the ratio is finite and positive, both series do the same thing.", difficulty="medium")

    lim = limit(sin(1 / n_) / (1 / n_), n_, oo)
    assert lim == 1
    B.mcq(T_CT, f"Which statement about the series ${SUM}\\sin\\left(\\dfrac1n\\right)$ is correct?",
          ch("It diverges, by the Limit Comparison Test with $\\sum\\frac1n$", "$\\lim_{n\\to\\infty}\\frac{\\sin(1/n)}{1/n}=1$, a finite positive number, and $\\sum\\frac1n$ diverges. (All terms are positive since $0<\\frac1n\\le1<\\pi$.)"),
          [ch("It converges, because $\\sin\\left(\\frac1n\\right)\\to0$", "Terms approaching 0 is not enough for convergence."),
           ch("It converges, because $\\sin x\\le x$ and the terms are small", "$\\sin\\left(\\frac1n\\right)\\le\\frac1n$ compares the series to a divergent one, which proves nothing."),
           ch("It converges, because $\\left|\\sin\\left(\\frac1n\\right)\\right|\\le1$", "A bound by the constant 1 gives no information about the sum.")],
          "For small $u$, $\\sin u\\approx u$. Use the Limit Comparison Test with $\\sum\\frac1n$.", difficulty="hard")

    lim = limit(((n_**2 + 1) / (n_**3 + 4 * n_)) / (1 / n_), n_, oo)
    assert lim == 1
    B.mcq(T_CT, f"Which statement about the series ${SUM}\\dfrac{{n^2+1}}{{n^3+4n}}$ is correct?",
          ch("It diverges, by the Limit Comparison Test with $\\sum\\frac1n$", "The terms behave like $\\frac{n^2}{n^3}=\\frac1n$: $\\lim\\frac{(n^2+1)/(n^3+4n)}{1/n}=\\lim\\frac{n^3+n}{n^3+4n}=1$, and $\\sum\\frac1n$ diverges."),
          [ch("It converges, by the Limit Comparison Test with $\\sum\\frac1{n^2}$", "With $\\frac{1}{n^2}$ the limit of the ratio is $\\lim\\frac{n^4+n^2}{n^3+4n}=\\infty$, so the test does not apply."),
           ch("It converges, because the degree of the denominator is greater than the degree of the numerator", "The difference in degrees is only 1, so the terms behave like $\\frac1n$. A difference of at least 2 is needed for convergence."),
           ch("It converges, because $\\frac{n^2+1}{n^3+4n}<\\frac1n$", "Being smaller than the divergent harmonic series proves nothing.")],
          "For rational terms, compare with $\\frac1{n^k}$, where $k$ is the difference between the degrees of the denominator and numerator.", difficulty="hard")

    # ------------------------------------------------------------ alternating series
    B.mcq(T_AS, "Which of the following series converges but does not converge absolutely?",
          ch(f"${SUM}\\dfrac{{(-1)^n}}{{n}}$", "It converges by the Alternating Series Test, but $\\sum\\left|\\frac{(-1)^n}{n}\\right|=\\sum\\frac1n$ diverges."),
          [ch(f"${SUM}\\dfrac{{(-1)^n}}{{n^2}}$", "It converges absolutely, since $\\sum\\frac1{n^2}$ converges."),
           ch(f"${SUM}\\dfrac{{(-1)^nn}}{{n+1}}$", "The terms approach $\\pm1$, not 0, so the series diverges."),
           ch(f"${SUM}\\dfrac{{1}}{{n}}$", "This is the harmonic series, which diverges.")],
          "A series is conditionally convergent when it converges but $\\sum|a_n|$ diverges.", difficulty="easy")

    B.mcq(T_AS, f"Why can the Alternating Series Test not be used to show that ${SUM}\\dfrac{{(-1)^nn}}{{n+1}}$ converges?",
          ch("Because $a_n=\\frac{n}{n+1}$ approaches 1, not 0", "The test requires the unsigned terms to approach 0. Here $|a_n|\\to1$, so the series in fact diverges by the $n$th-Term Test."),
          [ch("Because the terms do not alternate in sign", "They do alternate, because of the factor $(-1)^n$."),
           ch("Because $a_n=\\frac{n}{n+1}$ is negative for some $n$", "$\\frac{n}{n+1}>0$ for $n\\ge1$. The sign alternation comes from $(-1)^n$."),
           ch("Because $a_n=\\frac{n}{n+1}$ is unbounded", "$\\frac{n}{n+1}<1$ for all $n$, so it is bounded.")],
          "The test requires (1) alternating signs, (2) unsigned terms decreasing and (3) unsigned terms approaching 0. A series whose terms do not approach 0 diverges outright.", difficulty="easy")

    a5 = R(1, 25)
    B.mcq(T_AS, f"The alternating series ${SUM}\\dfrac{{(-1)^{{n+1}}}}{{n^2}}$ is approximated by the sum $S_4$ of its first four terms. What is the best bound on the error $|S-S_4|$ from the Alternating Series Error Bound?",
          ch(R(1, 25), "The error is at most the magnitude of the first term not used, $a_5=\\frac{1}{5^2}=\\frac1{25}$."),
          [ch(R(1, 16), "This is $a_4$, the last term that was used."),
           ch(R(1, 36), "This is $a_6$. The first omitted term is $a_5$."),
           ch(R(1, 4), "This is $a_2$. The bound uses the next term after the partial sum.")],
          "For an alternating series with decreasing terms, $|S-S_N|\\le a_{N+1}$.", difficulty="medium")

    need = next(Nn for Nn in range(1, 200) if R(1, (Nn + 1) ** 2) < R(1, 1000))
    assert need == 31
    B.mcq(T_AS, f"What is the smallest number of terms of ${SUM}\\dfrac{{(-1)^{{n+1}}}}{{n^2}}$ that guarantees the partial sum is within $0.001$ of the sum of the series, by the Alternating Series Error Bound?",
          ch(31, "We need $a_{N+1}=\\frac{1}{(N+1)^2}<0.001$, so $(N+1)^2>1000$ and $N+1\\ge32$. Hence $N=31$ terms."),
          [ch(32, "$N+1=32$ is the index of the first omitted term. The number of terms used is $N=31$."),
           ch(1000, "This confuses the size of the error with the number of terms. $(N+1)^2>1000$, not $N+1>1000$."),
           ch(500, "$(N+1)^2>1000$ puts $N+1$ near $\\sqrt{1000}\\approx31.6$, nowhere near 500.")],
          "Find the first $N$ with $a_{N+1}<$ the tolerance.", difficulty="medium")

    S3 = 1 - R(1, 6) + R(1, 120)
    assert S3 == R(101, 120) and R(1, factorial(7)) == R(1, 5040)
    B.mcq(T_AS, "The series $\\displaystyle\\sum_{n=0}^{\\infty}\\frac{(-1)^n}{(2n+1)!}=1-\\frac1{3!}+\\frac1{5!}-\\cdots$ is approximated by the sum of its first three terms, $1-\\frac16+\\frac1{120}$. What is the Alternating Series Error Bound for this approximation?",
          ch(R(1, 5040), "The first omitted term is the one with $n=3$, namely $\\frac{1}{7!}=\\frac1{5040}$."),
          [ch(R(1, 120), "$\\frac1{5!}$ is the last term used, not the first omitted."),
           ch(R(1, 720), "$\\frac1{6!}$ is not in this series (it has only odd factorials)."),
           ch(R(1, 40320), "$\\frac{1}{8!}$ skips a term: the omitted terms begin with $\\frac{1}{7!}$.")],
          "List the terms: $\\frac1{1!},\\frac1{3!},\\frac1{5!},\\frac1{7!},\\ldots$ and find the first one that is left out.", difficulty="hard")

    B.mcq(T_AS, "For which values of $p$ does the series $\\displaystyle\\sum_{n=1}^{\\infty}\\frac{(-1)^n}{n^p}$ converge conditionally?",
          ch("$0<p\\le1$", "For $p>0$ the terms decrease to 0, so the series converges by the Alternating Series Test. It converges absolutely when $p>1$, so conditional convergence occurs only for $0<p\\le1$."),
          [ch("$p>1$", "For $p>1$ the series converges absolutely, which is stronger than conditional convergence."),
           ch("$p>0$", "This includes $p>1$, where the convergence is absolute."),
           ch("$0<p<1$", "At $p=1$ the series $\\sum\\frac{(-1)^n}{n}$ converges conditionally, so $p=1$ is included.")],
          "Combine two facts: the AST gives convergence for $p>0$, and the $p$-series test gives absolute convergence for $p>1$.", difficulty="hard")
