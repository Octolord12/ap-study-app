"""Unit 2 free response: one COLLECT_DATA prompt, five ANALYZE_DATA prompts and two MULTI_FOCUS prompts, 10 points each (one point per rubric line, in the order of the parts).

  C1 2.3 design a simulation with random digits, estimate and compare with the exact probability       A1 2.2 a two-way table: joint, marginal and conditional relative frequencies, and association
  A2 2.9 a probability distribution with a missing value: mean, standard deviation, interpretation       A3 2.11 a normal distribution: z-score, areas, a percentile, an unusual value
  A4 2.7 probabilities from percents: union, complement, conditional, independence                       A5 2.10 a guessing quiz: dotplot of a simulation, the binomial probability, mean and standard deviation
  M1 2.10 a binomial count of defective items plus the reason for a random sample                        M2 2.12 a simulated sampling distribution of a mean, the central limit theorem, and a random sample
Every number is computed here from the data that is shown or described.
"""
from fractions import Fraction

from scipy import stats as sps

from lib import *


def L(*lines):
    return [(1, t) for t in lines]


def fx(v, p=2):
    return f"{v:.{p}f}"


def build(B):
    # ----------------------------------------------------------------------------------------------------------- C1: simulation design
    p_c = 0.20
    exact = 1 - (1 - p_c) ** 4
    rng = np.random.default_rng(21)
    trials = 100
    sims = [int(np.any(rng.random(4) < p_c)) for _ in range(trials)]
    k = sum(sims)
    est = k / trials
    assert abs(est - exact) < 0.12 and k != round(exact * trials), (k, exact)
    setup = ("A restaurant puts a coupon for a free dessert in 1 of every 5 of its children's meals, chosen at random, so each meal has a coupon with probability 0.20, independently of the other meals. "
             "A family buys 4 children's meals. The restaurant owner wants to estimate the probability that at least one of the 4 meals has a coupon. A student plans to use a table of random digits, in which each of the digits 0 through 9 is equally likely, to simulate the process.")
    parts = [("A", "Describe how the student can use the random digits to simulate whether one meal has a coupon."),
             ("B", "Describe one trial of the simulation. Say what the student does and what the student records."),
             ("C", f"The student carries out {trials} trials of the simulation. In {k} of the trials, at least one of the 4 meals has a coupon. Calculate an estimate of the probability that at least one of the 4 meals has a coupon."),
             ("D", "Calculate the exact probability that at least one of the 4 meals has a coupon. Show your work."),
             ("E", "Explain why the estimate in part C is not equal to the exact probability in part D, and describe how the student could get an estimate that is likely to be closer to the exact probability.")]
    ans = [("A", "Let the digits 0 and 1 represent a meal with a coupon and the digits 2 through 9 represent a meal without a coupon. Two of the ten equally likely digits give a probability of 0.20 for a coupon."),
           ("B", "One trial reads 4 digits from the table, one for each of the meals. The student records whether at least one of the 4 digits is a 0 or a 1 (a coupon)."),
           ("C", f"The estimated probability is the relative frequency of the trials with at least one coupon: {k} / {trials} = {fx(est)}."),
           ("D", f"The probability that a meal has no coupon is 0.80, and the meals are independent, so P(no coupon in 4 meals) = (0.80)⁴ = {fx(0.8 ** 4, 4)}. P(at least one coupon) = 1 - {fx(0.8 ** 4, 4)} = {fx(exact, 4)}."),
           ("E", f"An estimate from a simulation is a relative frequency of a number of trials that is not large, so it varies by chance and is not usually equal to the exact probability ({fx(est)} compared with {fx(exact, 4)}). The student could run many more trials, since by the law of large numbers the relative frequency gets closer to the probability as the number of trials increases.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(3, "COLLECT_DATA", prompt,
          L("A: Assigns digits to a coupon with a total probability of 0.20 (for example, 0 and 1 represent a coupon).",
            "A: Assigns the remaining digits (2 through 9) to a meal without a coupon.",
            "B: Describes one trial as reading 4 digits, one for each of the 4 meals.",
            "B: States that the student records whether at least one of the 4 digits is a coupon digit.",
            f"C: Calculates the estimate as the relative frequency {k} / {trials} = {fx(est)}.",
            "D: Uses the complement: P(at least one coupon) = 1 - P(no coupon in the 4 meals).",
            f"D: Calculates P(no coupon in the 4 meals) = (0.80)⁴ = {fx(0.8 ** 4, 4)} (using independence).",
            f"D: Calculates the exact probability {fx(exact, 4)}.",
            "E: Explains that the estimate is based on a limited number of trials, so it varies by chance from the exact probability.",
            "E: States that more trials are likely to give an estimate that is closer to the exact probability (the law of large numbers)."),
          sample)

    # ----------------------------------------------------------------------------------------------------------- A1: two-way table
    grid = [[60, 110, 130], [100, 40, 60]]
    tb = twoway("Region", ["Dog", "Cat", "No pet"], ["Urban", "Rural"], grid, caption="Pets owned by 500 adults, by region")
    n = 500
    assert sum(map(sum, grid)) == n
    joint = grid[1][0] / n
    marg = (grid[0][1] + grid[1][1]) / n
    cu, cr = grid[0][1] / 300, grid[1][1] / 200
    dog_rural = grid[1][0] / (grid[0][0] + grid[1][0])
    du, dr = grid[0][0] / 300, grid[1][0] / 200
    setup = "A researcher surveyed 500 adults, 300 who live in an urban area and 200 who live in a rural area, about the kind of pet that they own. The table shows the results."
    parts = [("A", "Calculate the joint relative frequency of the adults who live in a rural area and own a dog. Interpret this value in context."),
             ("B", "Calculate the marginal relative frequency of the adults who own a cat."),
             ("C", "Among the adults who live in an urban area, what proportion own a cat? Among the adults who live in a rural area, what proportion own a cat?"),
             ("D", "Given that an adult owns a dog, what is the proportion who live in a rural area?"),
             ("E", "The researcher claims that there is an association between the region where an adult lives and the kind of pet that the adult owns. Use the relative frequencies of the dog owners in each region to justify the claim.")]
    ans = [("A", f"The joint relative frequency is {grid[1][0]} / {n} = {fx(joint)}. About {joint * 100:.0f}% of all of the 500 adults surveyed live in a rural area and own a dog."),
           ("B", f"{grid[0][1] + grid[1][1]} adults own a cat, so the marginal relative frequency is {grid[0][1] + grid[1][1]} / {n} = {fx(marg)}."),
           ("C", f"Urban: {grid[0][1]} / 300 = {fx(cu, 3)}. Rural: {grid[1][1]} / 200 = {fx(cr, 3)}."),
           ("D", f"There are {grid[0][0] + grid[1][0]} dog owners and {grid[1][0]} of them live in a rural area: {grid[1][0]} / {grid[0][0] + grid[1][0]} = {fx(dog_rural, 3)}."),
           ("E", f"The conditional relative frequency of owning a dog is {grid[0][0]} / 300 = {fx(du)} for the adults in an urban area and {grid[1][0]} / 200 = {fx(dr)} for the adults in a rural area. The proportions are very different, so the distribution of the kind of pet is not the same in the two regions, which is evidence of an association between region and kind of pet.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(2, "ANALYZE_DATA", prompt,
          L(f"A: Calculates the joint relative frequency {grid[1][0]} / {n} = {fx(joint)}.",
            f"A: Interprets the value in context: about {joint * 100:.0f}% of all of the adults in the survey live in a rural area and own a dog.",
            f"B: Identifies the number of cat owners ({grid[0][1] + grid[1][1]}) and divides by the total 500.",
            f"B: Gives the marginal relative frequency {fx(marg)}.",
            f"C: Calculates the proportion of the urban adults who own a cat: {grid[0][1]} / 300 = {fx(cu, 3)}.",
            f"C: Calculates the proportion of the rural adults who own a cat: {grid[1][1]} / 200 = {fx(cr, 3)}.",
            f"D: Restricts to the {grid[0][0] + grid[1][0]} adults who own a dog.",
            f"D: Gives the conditional relative frequency {grid[1][0]} / {grid[0][0] + grid[1][0]} = {fx(dog_rural, 3)}.",
            f"E: Compares the proportions of dog owners in each region ({fx(du)} for urban and {fx(dr)} for rural).",
            "E: Concludes that the proportions are different, so the variables appear to be associated."),
          sample, diagram=tb)

    # ----------------------------------------------------------------------------------------------------------- A2: probability distribution
    xs = [0, 1, 2, 3, 4]
    ps = [0.15, 0.30, 0.25, None, 0.10]
    p3_ = round(1 - 0.15 - 0.30 - 0.25 - 0.10, 10)
    full = [0.15, 0.30, 0.25, p3_, 0.10]
    assert abs(p3_ - 0.20) < 1e-9
    mu = sum(x * p for x, p in zip(xs, full))
    var = sum((x - mu) ** 2 * p for x, p in zip(xs, full))
    sg = var ** 0.5
    p_ge2 = sum(p for x, p in zip(xs, full) if x >= 2)
    tb = table(["Number of customers, x", "0", "1", "2", "3", "4"], [["P(X = x)", "0.15", "0.30", "0.25", "?", "0.10"]], caption="Probability distribution of the number of customers who arrive in a 10-minute interval", row_headers=True)
    setup = "The random variable X is the number of customers who arrive at a coffee counter during a randomly selected 10-minute interval. The table shows the probability distribution of X, with one probability missing."
    parts = [("A", "Find the missing probability, P(X = 3)."),
             ("B", "What is the probability that at least 2 customers arrive in a 10-minute interval? Show your work."),
             ("C", "Calculate the mean (expected value) of X. Show your work."),
             ("D", "Calculate the standard deviation of X. Show your work."),
             ("E", "Interpret the mean from part C and the standard deviation from part D in context, and use the table to say whether it would be unusual for 4 customers to arrive in a 10-minute interval.")]
    ans = [("A", f"The probabilities add to 1, so P(X = 3) = 1 - (0.15 + 0.30 + 0.25 + 0.10) = {fx(p3_)}."),
           ("B", f"P(X ≥ 2) = P(2) + P(3) + P(4) = 0.25 + {fx(p3_)} + 0.10 = {fx(p_ge2)}."),
           ("C", f"μ = 0(0.15) + 1(0.30) + 2(0.25) + 3({fx(p3_)}) + 4(0.10) = {fx(mu)} customers."),
           ("D", f"σ = √[(0 - {fx(mu)})²(0.15) + (1 - {fx(mu)})²(0.30) + (2 - {fx(mu)})²(0.25) + (3 - {fx(mu)})²({fx(p3_)}) + (4 - {fx(mu)})²(0.10)] = √{fx(var, 4)} = {fx(sg)} customers."),
           ("E", f"Over a very large number of 10-minute intervals, the mean number of customers who arrive per interval is about {fx(mu)} customers. The number of customers in an interval typically differs from the mean of {fx(mu)} by about {fx(sg)} customers. P(X = 4) = 0.10, so 4 customers arrive in 10% of the intervals, which is not very unusual.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(9, "ANALYZE_DATA", prompt,
          L(f"A: Uses the fact that the probabilities add to 1 and finds P(X = 3) = {fx(p3_)}.",
            "B: Identifies the values X = 2, 3 and 4 (at least 2).",
            f"B: Adds the probabilities to get {fx(p_ge2)}.",
            "C: Uses the expected value formula, the sum of x P(x).",
            f"C: Calculates the mean {fx(mu)}.",
            "D: Uses the standard deviation formula with the deviations from the mean.",
            f"D: Calculates the standard deviation {fx(sg)}.",
            f"E: Interprets the mean in context: the long-run average number of customers per 10-minute interval is about {fx(mu)}.",
            f"E: Interprets the standard deviation in context: the number of customers typically differs from the mean by about {fx(sg)} customers.",
            "E: Uses P(X = 4) = 0.10 to say whether 4 customers is unusual (it happens 10% of the time, so it is not very unusual)."),
          sample, diagram=tb)

    # ----------------------------------------------------------------------------------------------------------- A3: normal
    mu_b, sd_b = 40, 5
    z33 = (33 - mu_b) / sd_b
    p_lt33 = sps.norm.cdf(z33)
    p_btw = sps.norm.cdf((48 - mu_b) / sd_b) - sps.norm.cdf((35 - mu_b) / sd_b)
    q90 = mu_b + sps.norm.ppf(0.90) * sd_b
    z28 = (28 - mu_b) / sd_b
    p_lt28 = sps.norm.cdf(z28)
    d = density(mu_b, sd_b, [(25, "25"), (30, "30"), (35, "35"), (40, "40"), (45, "45"), (50, "50"), (55, "55")], x_label="Battery life (hours)",
                alt="Normal curve of the battery life, in hours, with mean 40 and standard deviation 5.", span=3.0)
    setup = "The battery life of a certain brand of phone battery is approximately normally distributed with a mean of 40 hours and a standard deviation of 5 hours. The graph shows the distribution."
    parts = [("A", "Calculate the z-score for a battery that lasts 33 hours, and interpret the z-score in context."),
             ("B", "What is the probability that a randomly selected battery lasts less than 33 hours? Sketch a normal curve, shade the region, and show your work."),
             ("C", "What is the probability that a randomly selected battery lasts between 35 hours and 48 hours? Show your work."),
             ("D", "Find the battery life that is at the 90th percentile of the distribution. Show your work."),
             ("E", f"A battery lasts 28 hours. Calculate the z-score, and use it to say whether a battery life of 28 hours is unusual.")]
    ans = [("A", f"z = (33 - 40) / 5 = {fx(z33, 1)}. A battery that lasts 33 hours has a life that is 1.4 standard deviations below the mean battery life."),
           ("B", f"P(X < 33) = P(Z < {fx(z33, 1)}) = {fx(p_lt33, 4)}. (The sketch is a normal curve with the mean 40 marked, the region to the left of 33 shaded, and 33 labeled.)"),
           ("C", f"z = (35 - 40) / 5 = -1.0 and z = (48 - 40) / 5 = 1.6. P(35 < X < 48) = P(-1.0 < Z < 1.6) = {fx(sps.norm.cdf(1.6), 4)} - {fx(sps.norm.cdf(-1.0), 4)} = {fx(p_btw, 4)}."),
           ("D", f"The 90th percentile has z = {fx(sps.norm.ppf(0.90), 3)}, so x = 40 + {fx(sps.norm.ppf(0.90), 3)}(5) = {fx(q90, 1)} hours."),
           ("E", f"z = (28 - 40) / 5 = {fx(z28, 1)}. The battery life is 2.4 standard deviations below the mean, and P(X < 28) = {fx(p_lt28, 4)}, so only about {p_lt28 * 100:.1f}% of the batteries last less than 28 hours. A battery life of 28 hours is unusual.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(11, "ANALYZE_DATA", prompt,
          L(f"A: Calculates z = (33 - 40) / 5 = {fx(z33, 1)}.",
            "A: Interprets the z-score in context: the battery life is 1.4 standard deviations below the mean battery life.",
            "B: Draws a normal curve, labels the mean, and shades the region to the left of 33.",
            f"B: Calculates the probability {fx(p_lt33, 4)}.",
            "C: Calculates both z-scores (-1.0 and 1.6) or identifies the boundaries 35 and 48.",
            f"C: Calculates the probability {fx(p_btw, 4)} (the area between the boundaries).",
            f"D: Uses the z-score for the 90th percentile ({fx(sps.norm.ppf(0.90), 2)}).",
            f"D: Calculates the battery life {fx(q90, 1)} hours.",
            f"E: Calculates z = (28 - 40) / 5 = {fx(z28, 1)}.",
            f"E: Concludes that 28 hours is unusual, with a justification (2.4 standard deviations below the mean, or a probability of {fx(p_lt28, 4)})."),
          sample, diagram=d)

    # ----------------------------------------------------------------------------------------------------------- A4: probability rules
    pS, pB, pSB = 0.60, 0.40, 0.30
    p_union = pS + pB - pSB
    p_neither = 1 - p_union
    p_b_given_s = pSB / pS
    assert abs(p_union - 0.70) < 1e-9 and abs(p_neither - 0.30) < 1e-9 and abs(p_b_given_s - 0.50) < 1e-9
    setup = ("At a high school, 60% of the students play a sport, 40% of the students are in the band, and 30% of the students both play a sport and are in the band. "
             "One student is selected at random from the school.")
    parts = [("A", "What is the probability that the student plays a sport or is in the band? Show your work."),
             ("B", "What is the probability that the student neither plays a sport nor is in the band?"),
             ("C", "Given that the student plays a sport, what is the probability that the student is in the band? Show your work."),
             ("D", "Are the events \"plays a sport\" and \"is in the band\" independent? Justify your answer with probabilities."),
             ("E", "Are the events \"plays a sport\" and \"is in the band\" mutually exclusive? Justify your answer.")]
    ans = [("A", f"P(sport or band) = P(sport) + P(band) - P(sport and band) = 0.60 + 0.40 - 0.30 = {fx(p_union)}."),
           ("B", f"The event is the complement of \"sport or band\": 1 - {fx(p_union)} = {fx(p_neither)}."),
           ("C", f"P(band | sport) = P(band and sport) / P(sport) = 0.30 / 0.60 = {fx(p_b_given_s)}."),
           ("D", f"If the events were independent, P(band | sport) would equal P(band), or P(sport and band) would equal P(sport) P(band) = 0.60(0.40) = 0.24. But P(band | sport) = {fx(p_b_given_s)} is not equal to P(band) = 0.40 (and 0.30 is not 0.24), so the events are not independent."),
           ("E", "The events are not mutually exclusive, because P(sport and band) = 0.30, which is not 0. Some students both play a sport and are in the band.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(7, "ANALYZE_DATA", prompt,
          L("A: Uses P(A or B) = P(A) + P(B) - P(A and B), with the given probabilities substituted.",
            f"A: Calculates the probability {fx(p_union)}.",
            "B: Recognizes the event as the complement of \"sport or band\" (or uses 1 - the union).",
            f"B: Calculates the probability {fx(p_neither)}.",
            "C: Uses the conditional probability formula P(band and sport) / P(sport).",
            f"C: Calculates the probability {fx(p_b_given_s)}.",
            "D: Compares P(band | sport) with P(band), or P(sport and band) with P(sport) P(band) = 0.24.",
            "D: Concludes that the events are not independent, with the justification that the probabilities are not equal.",
            "E: Uses the joint probability P(sport and band) = 0.30, which is not 0.",
            "E: Concludes that the events are not mutually exclusive."),
          sample)

    # ----------------------------------------------------------------------------------------------------------- A5: guessing, simulation and binomial
    rng = np.random.default_rng(2)
    sims = sorted(int(v) for v in rng.binomial(10, 0.25, 50))
    ge4 = sum(1 for v in sims if v >= 4)
    ex = sps.binom.sf(3, 10, 0.25)
    mu_g, sd_g = 10 * 0.25, (10 * 0.25 * 0.75) ** 0.5
    assert 6 <= ge4 <= 16 and abs(ge4 / 50 - ex) > 0.025 and max(sims) <= 8, (ge4, ex, sims)
    dp = dotplot(sims, "Number of correct answers", axis=(0, 10, 1), alt="Dotplot of the number of correct answers out of 10, in each of 50 simulated trials of guessing on a quiz.")
    setup = ("A quiz has 10 multiple-choice questions, and each question has 4 choices. A student guesses the answer to every question. Let X be the number of questions that the student answers correctly. "
             "The dotplot shows the value of X in each of 50 simulated trials of this situation.")
    parts = [("A", "Describe the shape of the distribution of the simulated results."),
             ("B", "Use the dotplot to estimate the probability that the student answers at least 4 questions correctly."),
             ("C", "X is a binomial random variable. Identify n and p, and calculate the exact probability that the student answers at least 4 questions correctly. Show your work."),
             ("D", "Compare the estimate in part B with the exact probability in part C. Describe one way to improve the simulation."),
             ("E", "Calculate the mean and the standard deviation of X, and interpret the mean in context.")]
    ans = [("A", "The distribution is unimodal and skewed to the right. The most common values are 1, 2 and 3 correct answers, and there are a few trials with a large number of correct answers."),
           ("B", f"{ge4} of the 50 trials have 4 or more correct answers, so the estimate is {ge4} / 50 = {fx(ge4 / 50)}."),
           ("C", f"n = 10 and p = 1/4 = 0.25. P(X ≥ 4) = 1 - P(X ≤ 3) = 1 - [P(0) + P(1) + P(2) + P(3)] = 1 - {fx(sps.binom.cdf(3, 10, 0.25), 4)} = {fx(ex, 4)}."),
           ("D", f"The estimate {fx(ge4 / 50)} is {'close to' if abs(ge4 / 50 - ex) < 0.05 else 'different from'} the exact probability {fx(ex, 4)}; they differ because the simulation used only 50 trials. The simulation can be improved by using many more trials."),
           ("E", f"μ = np = 10(0.25) = {fx(mu_g, 1)} and σ = √(np(1 - p)) = √(10(0.25)(0.75)) = {fx(sd_g)}. Over a very large number of quizzes on which the student guesses, the mean number of correct answers is about {fx(mu_g, 1)} per quiz.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(10, "ANALYZE_DATA", prompt,
          L("A: Describes the shape as skewed to the right (and unimodal).",
            f"B: Counts the trials with 4 or more correct answers ({ge4}).",
            f"B: Divides by 50 to get the estimate {fx(ge4 / 50)}.",
            "C: Identifies n = 10 and p = 0.25.",
            f"C: Calculates the probability {fx(ex, 4)} (for example by the complement, 1 - P(X ≤ 3)).",
            "D: Compares the estimate with the exact probability.",
            "D: Describes a valid improvement (many more trials).",
            f"E: Calculates the mean {fx(mu_g, 1)} and the standard deviation {fx(sd_g)}.",
            "E: Interprets the mean as the long-run average number of correct answers per quiz.",
            "E: Uses the formulas for a binomial random variable, np and the square root of np(1 - p), with the values substituted."),
          sample, diagram=dp)

    # ----------------------------------------------------------------------------------------------------------- M1: binomial and a random sample
    n_i, p_d = 10, 0.04
    p1 = sps.binom.pmf(1, n_i, p_d)
    p_ge1 = sps.binom.sf(0, n_i, p_d)
    mu_d, sd_d = n_i * p_d, (n_i * p_d * (1 - p_d)) ** 0.5
    setup = ("A factory makes light bulbs, and 4% of the bulbs that it makes are defective. A quality inspector examines a random sample of 10 bulbs from one day's production, which is a very large number of bulbs. "
             "Let X be the number of defective bulbs in the sample of 10.")
    parts = [("A", "Explain why X can be modeled with a binomial distribution. Identify n and p."),
             ("B", "What is the probability that exactly 1 of the 10 bulbs is defective? Show your work."),
             ("C", "What is the probability that at least 1 of the 10 bulbs is defective? Show your work."),
             ("D", "Calculate the mean of X, and interpret the mean in context."),
             ("E", "The inspector could examine the first 10 bulbs made that day instead of a random sample. Explain why a random sample is better for estimating the proportion of defective bulbs made that day.")]
    ans = [("A", "There is a fixed number of trials (10 bulbs), each bulb is either defective (success) or not defective (failure), the bulbs are independent (a random sample from a very large number of bulbs), and the probability that a bulb is defective is the same, 0.04, for every bulb. So n = 10 and p = 0.04."),
           ("B", f"P(X = 1) = C(10, 1)(0.04)¹(0.96)⁹ = {fx(p1, 4)}."),
           ("C", f"P(X ≥ 1) = 1 - P(X = 0) = 1 - (0.96)¹⁰ = 1 - {fx(sps.binom.pmf(0, n_i, p_d), 4)} = {fx(p_ge1, 4)}."),
           ("D", f"μ = np = 10(0.04) = {fx(mu_d)}. Over many random samples of 10 bulbs, the mean number of defective bulbs per sample is about {fx(mu_d)}."),
           ("E", "The first 10 bulbs made may not be representative of the whole day: machines can behave differently when they start, so those bulbs might have a higher or lower rate of defects. A random sample gives every bulb made that day a chance of being selected, so the sample proportion can be used to estimate the proportion for the whole day without a systematic bias.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(10, "MULTI_FOCUS", prompt,
          L("A: Justifies the binomial model: a fixed number of trials, two outcomes, independent, and the same probability of success.",
            "A: Identifies n = 10 and p = 0.04.",
            "B: Uses the binomial probability formula with n = 10, p = 0.04 and x = 1.",
            f"B: Calculates the probability {fx(p1, 4)}.",
            "C: Uses the complement, 1 - P(X = 0), or adds the probabilities for 1 through 10.",
            f"C: Calculates the probability {fx(p_ge1, 4)}.",
            f"D: Calculates the mean np = {fx(mu_d)}.",
            f"D: Interprets the mean in context: the long-run average number of defective bulbs in a sample of 10 is about {fx(mu_d)}.",
            "E: Explains that the first 10 bulbs may not be representative of the whole day (a possible bias).",
            "E: Explains that random selection gives every bulb a chance, so the sample can be used to generalize to the day's production."),
          sample)

    # ----------------------------------------------------------------------------------------------------------- M2: sampling distribution and a random sample
    rng2 = np.random.default_rng(3)
    means = [float(np.mean(rng2.exponential(20, 40))) for _ in range(200)]
    edges = [10 + 2 * k_ for k_ in range(0, 14)]
    gt24 = sum(1 for v in means if v > 24)
    mm, ss = mean(means), sd(means)
    assert min(means) > 10 and max(means) < 36 and 3 <= gt24 <= 30 and abs(mm - 20) < 1, (min(means), max(means), gt24, mm)
    hist = histogram(means, edges, "Sample mean (minutes)", alt="Histogram of the means of 200 simulated random samples of 40 waiting times from a right-skewed population with mean 20 minutes.")
    setup = ("The waiting times at a clinic have a distribution that is strongly skewed to the right, with a mean of 20 minutes. A researcher simulates random samples of 40 waiting times from this population, calculates the mean of each sample, "
             "and repeats the process 200 times. The histogram shows the 200 sample means.")
    parts = [("A", "Describe the shape and the center of the distribution of the 200 sample means."),
             ("B", "Explain why the distribution of the sample means has the shape that you described in part A, even though the population is skewed to the right."),
             ("C", "Use the histogram to estimate the probability that a random sample of 40 waiting times has a mean greater than 24 minutes. Show your work."),
             ("D", "The researcher repeats the simulation with random samples of size 10 instead of size 40. Describe how the shape of the distribution of the sample means is likely to change, and explain why."),
             ("E", "The clinic has a list of 2,000 waiting times. Describe how the researcher can select a simple random sample of 40 of the waiting times from the list.")]
    ans = [("A", f"The distribution of the sample means is approximately normal (unimodal and approximately symmetric), and it is centered near the population mean of 20 minutes (the mean of the 200 sample means is about {fx(mm, 1)} minutes)."),
           ("B", "By the central limit theorem, the sampling distribution of the mean of a random sample has a shape that can be approximated by a normal distribution, and the larger the sample the better the approximation. A sample of size 40 is large enough for the distribution of the sample means to be approximately normal even though the population is skewed."),
           ("C", f"{gt24} of the 200 sample means are greater than 24, so the estimated probability is {gt24} / 200 = {fx(gt24 / 200, 3)}."),
           ("D", "The distribution of the sample means for samples of size 10 is likely to be more skewed to the right (less close to normal) than for samples of size 40, because the normal approximation of the central limit theorem is better for larger samples."),
           ("E", "Number the waiting times from 1 to 2,000. Use a random number generator to select 40 different numbers between 1 and 2,000 (ignoring repeats), and use the waiting times with those numbers.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(12, "MULTI_FOCUS", prompt,
          L("A: Describes the shape as approximately normal (unimodal and symmetric).",
            "A: Describes the center as near 20 minutes (the population mean).",
            "B: Cites the central limit theorem (the sampling distribution of a mean is approximately normal).",
            "B: States that this is because the sample size is large (and the approximation improves as the sample gets larger).",
            f"C: Counts the sample means greater than 24 ({gt24}).",
            f"C: Divides by 200 to get the estimate {fx(gt24 / 200, 3)}.",
            "D: States that the distribution of the means of samples of size 10 is likely to be more skewed to the right (less normal).",
            "D: Explains that a smaller sample gives a poorer normal approximation (central limit theorem).",
            "E: Describes numbering the 2,000 values and using a random mechanism, such as a random number generator, to choose numbers.",
            "E: States that 40 different numbers are selected (without replacement) and the corresponding waiting times are the sample."),
          sample, diagram=hist)
