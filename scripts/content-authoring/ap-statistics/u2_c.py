"""Unit 2, topics 2.8 to 2.10.

Required content (CED effective Fall 2026): 2.8 a random variable has numerical outcomes from a random phenomenon; a discrete probability distribution (table, graph or function) gives P(x) for every value, the probabilities add to 1,
can be found by the rules of probability or a simulation; a cumulative distribution gives P(X <= x). 2.9 a parameter is a single fixed value; mean (expected value) mu = sum of x P(x), the long-run average; standard deviation
sigma = sqrt(sum of (x - mu)^2 P(x)), the typical deviation from the mean over the long run; variance sigma^2; interpret in context. 2.10 binomial: a count of successes in repeated independent trials with two outcomes and constant p; mean np,
standard deviation sqrt(np(1 - p)); P(X = x) = C(n, x) p^x (1 - p)^(n - x); estimate from a simulation; interpret in context. Skills 3.A, 3.C, 3.D, 3.B, 4.B, 4.D.
"""
from fractions import Fraction
from math import comb

from scipy import stats as sps

from lib import *


def p3(v):
    return f"{float(v):.3f}"


def dist_table(values, probs, caption=None, label="x"):
    return table([label] + [str(v) for v in values], [["P(X = x)"] + [f"{p:g}" if p * 100 == int(p * 100) else f"{p:.3f}" for p in probs]], caption=caption, row_headers=True)


def build(B):
    # ------------------------------------------------------------------------------------------------------------ 2.8
    T = 8
    B.mcq(T, "Which of the following is a discrete random variable?",
          ch("The number of heads in 10 flips of a fair coin", "The values are countable: 0, 1, 2, ..., 10."),
          [ch("The time, in seconds, that a runner takes to run 100 meters", "Time can be any value in an interval, so it is continuous."),
           ch("The height, in inches, of a randomly selected student", "Height can be any value in an interval, so it is continuous."),
           ch("The weight, in pounds, of a randomly selected package", "Weight can be any value in an interval, so it is continuous.")],
          "A discrete random variable takes countable values.", difficulty="easy")

    vals = [0, 1, 2, 3]
    pr = [0.10, 0.30, None, 0.25]
    x2 = round(1 - 0.10 - 0.30 - 0.25, 10)
    assert abs(x2 - 0.35) < 1e-9
    tb = table(["x", "0", "1", "2", "3"], [["P(X = x)", "0.10", "0.30", "?", "0.25"]], caption="Probability distribution of a random variable X", row_headers=True)
    B.mcq(T, "The table shows the probability distribution of a discrete random variable X, with one probability missing. What is P(X = 2)?",
          ch("0.35", "The probabilities of all of the possible values add to 1: 1 - (0.10 + 0.30 + 0.25) = 0.35."),
          [ch("0.65", "This is the sum of the other three probabilities, 0.10 + 0.30 + 0.25, and not the probability that remains."),
           ch("0.25", "This is 1 divided by 4, which assumes that the four values are equally likely. They are not."),
           ch("0.45", "This is 1 - 0.55, which leaves out one of the given probabilities.")],
          "The probabilities add to 1: P(X = 2) = 1 - 0.65 = 0.35.", diagram=tb, difficulty="easy")

    B.mcq(T, "Which of the following tables is a valid probability distribution for a discrete random variable X with the possible values 1, 2, 3 and 4?",
          ch("P(X = x) = 0.15, 0.35, 0.30, 0.20", "Each probability is between 0 and 1, and they add to 1."),
          [ch("P(X = x) = 0.20, 0.35, 0.30, 0.20", "The probabilities add to 1.05, which is more than 1."),
           ch("P(X = x) = 0.40, 0.30, 0.20, 0.00", "This adds to 0.90, so the probabilities do not add to 1."),
           ch("P(X = x) = 0.50, 0.40, 0.30, -0.20", "This adds to 1, but a probability cannot be negative.")],
          "A probability distribution has probabilities between 0 and 1 that add to 1.", difficulty="medium")

    pcum = [0.10, 0.30, 0.35, 0.25]
    tb4 = table(["x", "0", "1", "2", "3"], [["P(X = x)", "0.10", "0.30", "0.35", "0.25"]], caption="Probability distribution of a random variable X", row_headers=True)
    B.mcq(T, "The table shows the probability distribution of a discrete random variable X. What is the cumulative probability P(X ≤ 2)?",
          ch("0.75", "P(X ≤ 2) = P(0) + P(1) + P(2) = 0.10 + 0.30 + 0.35."),
          [ch("0.35", "This is P(X = 2), only one of the values that are less than or equal to 2."),
           ch("0.40", "This is P(X ≤ 1), which leaves out the value 2."),
           ch("0.60", "This is P(X ≥ 2) = 0.35 + 0.25, the probability of being at least 2 instead of at most 2.")],
          "P(X ≤ 2) = 0.10 + 0.30 + 0.35 = 0.75.", diagram=tb4, difficulty="medium")

    B.mcq(T, "The table shows the probability distribution of a discrete random variable X. What is P(X > 1)?",
          ch("0.60", "X > 1 means X = 2 or X = 3: 0.35 + 0.25."),
          [ch("0.90", "This is P(X ≥ 1), which includes the value 1."),
           ch("0.40", "This is P(X ≤ 1) = 0.10 + 0.30, the probability of the complement."),
           ch("0.35", "This is P(X = 2), which leaves out the value 3.")],
          "P(X > 1) = P(2) + P(3) = 0.35 + 0.25 = 0.60.", diagram=tb4, difficulty="medium")

    B.mcq(T, "Two fair coins are flipped. Let X be the number of heads. Which of the following is the probability distribution of X?",
          ch("P(0) = 0.25, P(1) = 0.50, P(2) = 0.25", "The outcomes TT, HT, TH and HH are equally likely, so one head has two ways out of four."),
          [ch("P(0) = 1/3, P(1) = 1/3, P(2) = 1/3", "This assumes that 0, 1 and 2 heads are equally likely. One head can happen in two ways."),
           ch("P(0) = 0.50, P(1) = 0.50, P(2) = 0.00", "Two heads is possible, with probability 0.25."),
           ch("P(0) = 0.25, P(1) = 0.25, P(2) = 0.50", "Two heads is one of four equally likely outcomes, so its probability is 0.25, not 0.50.")],
          "The sample space {TT, HT, TH, HH} gives P(0) = 1/4, P(1) = 2/4, P(2) = 1/4.", difficulty="medium")

    bg = bars(["0", "1", "2", "3", "4"], [0.05, 0.20, 0.40, 0.25, 0.10], "Number of pets, x", "Probability, P(X = x)", y_max=0.5,
              alt="Bar graph of the probability distribution of the number of pets: 0 is 0.05, 1 is 0.20, 2 is 0.40, 3 is 0.25 and 4 is 0.10.")
    B.mcq(T, "The bar graph shows the probability distribution of the number of pets, X, of a randomly selected family. What is the probability that a family has at least 3 pets?",
          ch("0.35", "At least 3 pets means 3 or 4 pets: 0.25 + 0.10."),
          [ch("0.25", "This is the probability of exactly 3 pets, which leaves out the families with 4 pets."),
           ch("0.65", "This is the probability of at most 2 pets, 0.05 + 0.20 + 0.40, the complement."),
           ch("0.10", "This is the probability of 4 pets, the tallest value on the right, only one of the values.")],
          "P(X ≥ 3) = 0.25 + 0.10 = 0.35.", diagram=bg, difficulty="medium")

    counts = [18, 62, 81, 39]
    assert sum(counts) == 200
    sim = table(["Number of heads", "0", "1", "2", "3"], [["Number of trials", *[str(v) for v in counts]]], caption="Results of 200 simulated trials", row_headers=True)
    B.mcq(T, "A simulation of 200 trials is used to estimate the probability distribution of a random variable X, the number of heads in 3 flips of a coin that may not be fair. Based on the simulation, what is the estimated probability that X is 2?",
          ch(p3(81 / 200), "The relative frequency of the trials with X = 2 is 81 / 200."),
          [ch(p3(81 / 161), "This divides by 161, the number of trials with at most 2 heads, instead of by all 200 trials."),
           ch("81", "This is the number of trials with X = 2, not a probability."),
           ch(p3(62 / 200), "This is the relative frequency of the trials with X = 1.")],
          f"Estimated P(X = 2) = 81 / 200 = {p3(81 / 200)}.", diagram=sim, difficulty="medium")

    # ------------------------------------------------------------------------------------------------------------ 2.9
    T = 9
    xs, ps = [0, 1, 2, 3], [0.10, 0.30, 0.35, 0.25]
    mu = sum(x * p for x, p in zip(xs, ps))
    var = sum((x - mu) ** 2 * p for x, p in zip(xs, ps))
    sg = var ** 0.5
    ex2 = sum(x * x * p for x, p in zip(xs, ps))
    assert abs(mu - 1.75) < 1e-9 and abs(var - 0.8875) < 1e-9
    tbm = table(["x", "0", "1", "2", "3"], [["P(X = x)", "0.10", "0.30", "0.35", "0.25"]], caption="Probability distribution of the number of goals, X, in a game", row_headers=True)
    B.mcq(T, "The table shows the probability distribution of X, the number of goals that a team scores in a game. What is the mean (expected value) of X?",
          ch("1.75", "μ = Σ x P(x) = 0(0.10) + 1(0.30) + 2(0.35) + 3(0.25) = 1.75."),
          [ch("1.50", "This is the mean of the four values 0, 1, 2 and 3, which ignores their probabilities."),
           ch("0.25", "This is the mean of the four probabilities, which has no meaning here."),
           ch("2.00", "This is the most likely value of X, since P(X = 2) = 0.35 is the greatest probability. The mean is not necessarily the most likely value.")],
          "μ = 1.75 goals.", diagram=tbm, difficulty="easy")

    B.mcq(T, "The table shows the probability distribution of X, the number of goals that a team scores in a game. The mean of X is 1.75. What is the standard deviation of X?",
          ch(f"{sg:.2f}", f"σ = √Σ (x - μ)² P(x) = √0.8875, about {sg:.2f}."),
          [ch(f"{var:.2f}", "This is the variance, σ², the value before taking the square root."),
           ch(f"{ex2 ** 0.5:.2f}", f"This is √Σ x² P(x) = √{ex2:.4f}. The deviations from the mean were not used."),
           ch("1.29", "This is the standard deviation of the four values 0, 1, 2 and 3 by themselves, which ignores their probabilities.")],
          f"σ = √0.8875, about {sg:.2f} goals.", diagram=tbm, difficulty="medium")

    B.mcq(T, "The mean of the number of goals, X, that a team scores in a game is 1.75. Which of the following is the correct interpretation?",
          ch("Over a very large number of games, the mean number of goals per game for the team will be about 1.75", "The expected value is the long-run average outcome of the random variable."),
          [ch("In each game that the team plays, the team scores exactly 1.75 goals, because 1.75 is the mean number of goals", "The number of goals is a whole number. The mean is a long-run average."),
           ch("In the next 4 games that the team plays, the team will score a total of exactly 7 goals, since 4(1.75) = 7", "A mean describes the long run and does not decide the total in a short run."),
           ch("The most likely number of goals for the team in a single game is 1.75 goals, because that is the mean", "The mean need not be a possible value, and it is not the most likely value.")],
          "The expected value is interpreted as the long-run average of the random variable.", difficulty="medium")

    B.mcq(T, "The number of goals, X, that a team scores in a game has a mean of 1.75 goals and a standard deviation of 0.94 goals. Which of the following is the correct interpretation of the standard deviation?",
          ch("Over a very large number of games, the number of goals in a game typically differs from the mean of 1.75 goals by about 0.94 goals", "The standard deviation is the typical deviation of the values from the mean over the long run."),
          [ch("In every game, the team scores between 0.81 and 2.69 goals, which is 1.75 plus or minus 0.94", "Many games are outside this interval, and a standard deviation does not set limits on the values."),
           ch("The team scores 0.94 goals in the typical game over the long run", "The typical value is described by the mean or the median, not by the standard deviation."),
           ch("About 94% of the games of the team have the mean number of goals, which is 1.75 goals", "A standard deviation is not a percent of the games.")],
          "The standard deviation is the typical distance of the values of the random variable from the mean over the long run.", difficulty="medium")

    gain = [7, 1, -3]
    gp = [0.2, 0.3, 0.5]
    eg = sum(g * p for g, p in zip(gain, gp))
    assert abs(eg - 0.2) < 1e-9
    B.mcq(T, "In a game, a player pays 3 points to play. The player then wins 10 points with probability 0.2, wins 4 points with probability 0.3, and wins 0 points with probability 0.5. What is the expected net gain of the player per game?",
          ch("0.2 points", "The net gains are 7, 1 and -3: 7(0.2) + 1(0.3) + (-3)(0.5) = 0.2."),
          [ch("3.2 points", "This is the expected number of points won, 10(0.2) + 4(0.3), which does not subtract the 3 points paid."),
           ch("1.67 points", "This is the mean of the three prizes minus 3, (10 + 4 + 0) / 3 - 3, which ignores the probabilities."),
           ch("-1.5 points", "This is only the contribution of the outcome in which the player wins nothing, (-3)(0.5).")],
          "Expected net gain = 7(0.2) + 1(0.3) + (-3)(0.5) = 0.2 points.", difficulty="hard")

    B.mcq(T, "Which of the following statements about the mean μ of a probability distribution of a random variable X is correct?",
          ch("It is a parameter, a single fixed value that describes the distribution", "A parameter is a numerical value measuring a characteristic of a probability distribution, and its value is fixed."),
          [ch("It is a statistic, because it is calculated from the values of a sample", "The mean of a probability distribution is calculated from the probabilities, not from a sample."),
           ch("It changes from one sample of values to another sample of values", "That describes a sample mean. The mean of the distribution is a fixed value."),
           ch("It must be one of the possible values of X", "The mean need not be a possible value of X, such as 1.75 goals.")],
          "The expected value is a parameter with a single, fixed value.", difficulty="medium")

    B.mcq(T, "A random variable X has a standard deviation of 1.2. What is the variance of X?",
          ch("1.44", "The variance is the square of the standard deviation: 1.2 squared."),
          [ch("1.10", "This is the square root of 1.2. The variance is found by squaring."),
           ch("2.40", "This doubles the standard deviation instead of squaring it."),
           ch("0.83", "This is 1 / 1.2, the reciprocal of the standard deviation, which has no meaning here.")],
          "Variance = (1.2)² = 1.44.", difficulty="easy")

    B.mcq(T, "Two games each have a mean net gain of 2 points per game. In Game 1 the standard deviation of the net gain is 0.5 points, and in Game 2 the standard deviation is 4 points. Which of the following is correct?",
          ch("In the long run the players of the two games have the same average net gain, but the net gains in Game 2 are more variable", "The means are equal, and the larger standard deviation means more variability."),
          [ch("In the long run the players of Game 1 have the greater average net gain, because the net gain in Game 1 has less variability", "Variability does not change the mean, which is 2 points for both games."),
           ch("In the long run the players of Game 2 have the greater average net gain, because the standard deviation is greater", "A greater standard deviation does not mean a greater mean."),
           ch("In every game the net gain in Game 2 is greater than the net gain in Game 1, because 4 is greater than 0.5", "The standard deviations do not give the net gains of the individual games.")],
          "Equal means: the same long-run average. The standard deviation measures the variability.", difficulty="medium")

    p_ = Fraction(1, 6)
    emean = (1 * 1 + 2 * 2 + 3 * 3) * p_
    assert emean == Fraction(7, 3)
    B.mcq(T, "A random variable X takes the values 1, 2 and 3 with probabilities p, 2p and 3p. What is the mean of X?",
          ch("2.33", "The probabilities add to 1: 6p = 1, so p = 1/6. Then μ = 1(1/6) + 2(2/6) + 3(3/6) = 14/6, about 2.33."),
          [ch("2.00", "This is the mean of the values 1, 2 and 3, which ignores the probabilities."),
           ch("1.17", "This is 14 / 12, which divides by 12 instead of by 6."),
           ch("0.33", "This is the probability of the value 2, 2p = 2/6, not the mean.")],
          "Solve 6p = 1, then μ = 14/6, about 2.33.", difficulty="hard")

    # ------------------------------------------------------------------------------------------------------------ 2.10
    T = 10
    B.mcq(T, "Which of the following random variables is a binomial random variable?",
          ch("The number of free throws that a player makes in 12 attempts, when each attempt is independent and has probability 0.70 of success",
             "There is a fixed number of trials, two outcomes for each (made or missed), independent trials and a constant probability of success."),
          [ch("The number of hearts in a 5-card hand dealt from a standard deck of 52 cards, without replacement",
              "The trials are not independent. The probability of a heart changes as the cards are dealt."),
           ch("The number of rolls of a fair die that are needed to get a 6 for the first time during the game",
              "The number of trials is not fixed. The count is the number of trials, not the number of successes."),
           ch("The total number of points that a player scores in a game, when each shot is worth 1, 2 or 3 points",
              "Each trial has more than two possible outcomes, and the variable adds points instead of counting successes.")],
          "A binomial random variable counts the successes in a fixed number of independent trials with two outcomes and the same probability of success.", difficulty="medium")

    B.mcq(T, "A box has 10 marbles, 4 of which are red. Three marbles are selected at random without replacement. Let X be the number of red marbles selected. Is X a binomial random variable?",
          ch("No, because the trials are not independent: the probability that a marble is red changes after each marble is selected and not replaced",
             "The probability that the second marble is red depends on the color of the first one."),
          [ch("Yes, because each marble is either red or not red, which are the two outcomes of a trial",
              "Two outcomes are not enough. The trials must also be independent with a constant probability of success."),
           ch("Yes, because the number of marbles that are selected is fixed at 3 for the process",
              "A fixed number of trials is needed, but it is not enough. The trials must be independent."),
           ch("No, because the number of red marbles in the box, 4, is not equal to the number of marbles that are selected from the box, 3, so X is not binomial",
              "The two numbers do not need to be equal. The problem is the dependence among the trials.")],
          "Sampling without replacement from a small box makes the trials dependent, so X is not binomial.", difficulty="hard")

    pm = sps.binom.pmf(3, 8, 0.4)
    cd = sps.binom.cdf(3, 8, 0.4)
    nocomb = 0.4 ** 3 * 0.6 ** 5
    sf = sps.binom.sf(2, 8, 0.4)
    assert len({round(v, 3) for v in (pm, cd, nocomb, sf)}) == 4
    B.mcq(T, "A random variable X is binomial with n = 8 trials and probability of success p = 0.4. What is P(X = 3)?",
          ch(p3(pm), "P(X = 3) = C(8, 3) (0.4)³ (0.6)⁵ = 56(0.064)(0.07776)."),
          [ch(p3(cd), "This is P(X ≤ 3), the probability of 3 or fewer successes."),
           ch(p3(sf), "This is P(X ≥ 3), the probability of 3 or more successes."),
           ch(p3(nocomb), "This is (0.4)³ (0.6)⁵, which leaves out the number of ways to choose which 3 of the 8 trials are successes.")],
          f"P(X = 3) = C(8, 3)(0.4)³(0.6)⁵, about {p3(pm)}.", difficulty="medium")

    a = sps.binom.sf(1, 10, 0.1)
    b2 = sps.binom.pmf(2, 10, 0.1)
    c2 = sps.binom.cdf(1, 10, 0.1)
    d2 = 1 - sps.binom.pmf(2, 10, 0.1)
    assert len({round(v, 3) for v in (a, b2, c2, d2)}) == 4
    B.mcq(T, "A random variable X is binomial with n = 10 and p = 0.1. What is P(X ≥ 2)?",
          ch(p3(a), "P(X ≥ 2) = 1 - P(X ≤ 1) = 1 - [P(0) + P(1)] = 1 - (0.349 + 0.387)."),
          [ch(p3(b2), "This is P(X = 2), the probability of exactly 2 successes."),
           ch(p3(c2), "This is P(X ≤ 1), the probability of the complement."),
           ch(p3(d2), "This is 1 - P(X = 2), which leaves out only the outcome of exactly 2 successes instead of every outcome less than 2.")],
          f"P(X ≥ 2) = 1 - P(X ≤ 1), about {p3(a)}.", difficulty="hard")

    mu_b, sd_b = 50 * 0.2, (50 * 0.2 * 0.8) ** 0.5
    B.mcq(T, "A random variable X is binomial with n = 50 and p = 0.2. What are the mean and the standard deviation of X?",
          ch(f"The mean is 10 and the standard deviation is {sd_b:.2f}", "μ = np = 50(0.2) = 10 and σ = √(np(1 - p)) = √(50(0.2)(0.8)) = √8."),
          [ch("The mean is 10 and the standard deviation is 8", "The value 8 is np(1 - p), the variance. The standard deviation is its square root."),
           ch(f"The mean is 0.2 and the standard deviation is {(0.2 * 0.8) ** 0.5:.2f}", "These are for one trial, with p = 0.2. For n trials, multiply the mean by n."),
           ch(f"The mean is 40 and the standard deviation is {sd_b:.2f}", "The 40 is n(1 - p), the expected number of failures, not the expected number of successes.")],
          f"μ = 10 and σ = √8, about {sd_b:.2f}.", difficulty="medium")

    B.mcq(T, "In a large school, 20% of the students walk to school. A random sample of 50 students is selected, and X is the number of the students in the sample who walk to school. The mean of X is 10. Which of the following is the correct interpretation of the mean?",
          ch("Over many random samples of 50 students, the mean number of students who walk to school is about 10", "The mean of a binomial random variable is the long-run average number of successes."),
          [ch("In each random sample of 50 students, exactly 10 of the students walk to school", "The count varies from one sample to another. The mean is a long-run average."),
           ch("In a random sample of 50 students, the number of students who walk to school is never more than 10", "Samples with more than 10 students who walk to school are common."),
           ch("The probability that a student in the sample walks to school is 10", "A probability cannot be greater than 1. The probability is 0.20.")],
          "The mean is interpreted in context as the long-run average number of students who walk.", difficulty="medium")

    guess = sps.binom.sf(5, 12, 0.25)
    assert abs(guess - 0.0544) < 5e-4, guess
    B.mcq(T, "A student guesses on all 12 questions of a multiple-choice quiz, and each question has 4 choices. Let X be the number of questions that the student gets correct. The probability that X is at least 6 is about 0.054. Which of the following is the correct interpretation of this probability?",
          ch("If a student guesses on all 12 questions, there is about a 5.4% chance of getting 6 or more of the questions correct", "The probability is interpreted in context, as the chance of the event for this student."),
          [ch("If a student guesses on all 12 questions, the student will get exactly 5.4% of the questions correct", "The probability is not the percent of the questions that are correct."),
           ch("If a student guesses on all 12 questions, about 5.4% of the questions will be answered correctly in every quiz", "A probability does not guarantee a percent in each quiz."),
           ch("A student who gets 6 or more of the questions correct was not guessing with probability 0.054", "A probability of the event does not give the probability that the student guessed.")],
          "P(X ≥ 6) ≈ 0.054 means about a 5.4% chance of 6 or more correct answers when guessing on all 12 questions.", difficulty="medium")

    rng = np.random.default_rng(5)
    sims = sorted(int(v) for v in rng.binomial(10, 0.5, 50))
    le3 = sum(1 for v in sims if v <= 3)
    assert 3 <= le3 <= 12 and le3 != sims.count(3), (le3, sims)
    dpb = dotplot(sims, "Number of heads in 10 flips", axis=(0, 10, 1), alt="Dotplot of the number of heads in 10 flips of a fair coin, in each of 50 simulated trials.")
    B.mcq(T, "The dotplot shows the number of heads in 10 flips of a fair coin, in each of 50 simulated trials. Based on the simulation, what is the estimated probability of 3 or fewer heads in 10 flips?",
          ch(p3(le3 / 50), f"{le3} of the 50 trials had 3 or fewer heads: {le3} / 50."),
          [ch(p3(sims.count(3) / 50), f"This counts only the trials with exactly 3 heads: {sims.count(3)} / 50."),
           ch(f"{le3}", "This is the number of trials with 3 or fewer heads, not a probability."),
           ch(p3((50 - le3) / 50), f"This is the relative frequency of the trials with more than 3 heads: {50 - le3} / 50.")],
          f"Estimated probability = {le3} / 50 = {p3(le3 / 50)}.", diagram=dpb, difficulty="medium")

    B.mcq(T, "A random variable X is binomial with n = 6 and p = 0.3. Which of the following expressions gives P(X = 2)?",
          ch("C(6, 2)(0.3)²(0.7)⁴", "There are C(6, 2) ways to place 2 successes among 6 trials, each with probability (0.3)²(0.7)⁴."),
          [ch("C(6, 2)(0.3)⁴(0.7)²", "The exponents are reversed. There are 2 successes (probability 0.3) and 4 failures (probability 0.7)."),
           ch("C(6, 4)(0.3)²(0.7)²", "The exponents must add to the number of trials, 6, and here they add to 4."),
           ch("(0.3)²(0.7)⁴", "This leaves out C(6, 2), the number of ways to choose which 2 trials are successes.")],
          "P(X = 2) = C(6, 2)(0.3)²(0.7)⁴.", difficulty="medium")

    atmost = sps.binom.cdf(8, 10, 0.8)
    assert abs(atmost - 0.6242) < 1e-3
    B.mcq(T, "A basketball player makes each free throw with probability 0.80, and the attempts are independent. In 10 attempts, what is the probability that the player makes at most 8 free throws?",
          ch(p3(atmost), "P(X ≤ 8) = 1 - [P(9) + P(10)] = 1 - (0.268 + 0.107)."),
          [ch(p3(sps.binom.pmf(8, 10, 0.8)), "This is P(X = 8), the probability of exactly 8 made free throws."),
           ch(p3(sps.binom.sf(8, 10, 0.8)), "This is P(X ≥ 9), the probability of the complement: 0.268 + 0.107."),
           ch(p3(sps.binom.cdf(7, 10, 0.8)), "This is P(X ≤ 7), which leaves out the outcome of exactly 8 made free throws.")],
          f"P(X ≤ 8) = 1 - P(X ≥ 9), about {p3(atmost)}.", difficulty="hard")

    B.mcq(T, "A student guesses on every question of a 15-question quiz. Each question has 5 choices, and X is the number of questions that the student gets correct. Which of the following identifies the values of n and p for the binomial distribution of X?",
          ch("n = 15 and p = 0.20", "There are 15 trials (questions), and a guess is correct with probability 1 / 5 = 0.20."),
          [ch("n = 5 and p = 0.20", "The number of trials is the number of questions, 15, and not the number of choices."),
           ch("n = 15 and p = 0.80", "The probability of success is the probability of a correct answer, 0.20. The 0.80 is the probability of a wrong answer."),
           ch("n = 15 and p = 5", "A probability cannot be greater than 1. The probability of a correct guess is 1 / 5.")],
          "n = 15 questions and p = 1/5 = 0.20.", difficulty="easy")

    B.mcq(T, "A random variable X is binomial with n = 20 and p = 0.1. Which of the following best describes the shape of the probability distribution of X?",
          ch("Skewed to the right, because the probability of success is small and the most likely values of X are near 0", "With a small p, the probabilities are largest at small values and trail off to the right."),
          [ch("Approximately symmetric, because every binomial distribution is symmetric about its mean", "A binomial distribution is symmetric only when p is 0.5 or when n is large enough."),
           ch("Skewed to the left, because the probability of success is small and the most likely values of X are near 20", "With a small p, the most likely values are small, not near 20."),
           ch("Approximately uniform, because each of the values from 0 to 20 has about the same probability", "The values near 2 are much more likely than the values near 20.")],
          "For n = 20 and p = 0.1, the mean is 2, and the distribution is skewed right.", difficulty="medium")
