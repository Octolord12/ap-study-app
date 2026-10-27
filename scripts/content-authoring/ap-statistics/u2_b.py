"""Unit 2, topics 2.4 to 2.7.

Required content (CED effective Fall 2026): 2.4 sample space (nonoverlapping outcomes, probability 1), theoretical probability of an event with equally likely outcomes (outcomes in the event / outcomes in the sample space), a probability
is between 0 and 1, the complement rule P(E') = 1 - P(E). 2.5 joint probability P(A and B); mutually exclusive (disjoint) events cannot occur together, P(A and B) = 0. 2.6 conditional probability P(A|B) = P(A and B) / P(B), the general
multiplication rule P(A and B) = P(A) P(B|A). 2.7 independence (knowing A does not change the probability of B: P(B|A) = P(B), P(A and B) = P(A) P(B)), the union P(A or B) = P(A) + P(B) - P(A and B). Skills 3.C, 4.B.
"""
from fractions import Fraction

from lib import *


def p3(v):
    return f"{float(v):.3f}"


def p2(v):
    return f"{float(v):.2f}"


def build(B):
    # ------------------------------------------------------------------------------------------------------------ 2.4
    T = 4
    B.mcq(T, "Two fair six-sided dice are rolled, one red and one green, and the number on each die is recorded. How many outcomes are in the sample space?",
          ch("36", "Each of the 6 outcomes of the red die can be paired with each of the 6 outcomes of the green die: 6 x 6 = 36."),
          [ch("12", "This is 6 + 6. The outcomes are pairs of numbers, so the counts are multiplied."),
           ch("21", "This counts the pairs without regard to which die has which number, but the red and the green die are different."),
           ch("11", "This is the number of possible sums, 2 through 12, not the number of outcomes.")],
          "The sample space has 6 x 6 = 36 equally likely outcomes.", difficulty="medium")

    bag = (5, 3, 2)
    assert sum(bag) == 10
    B.mcq(T, "A bag has 5 red marbles, 3 blue marbles and 2 green marbles. One marble is selected at random. What is the probability that the marble is blue?",
          ch("0.30", "The outcomes are equally likely, so the probability is the number of favorable outcomes divided by the total: 3 / 10."),
          [ch("0.60", "This is 3 / 5, which compares the blue marbles with only the red marbles."),
           ch("0.43", "This is 3 / 7, which compares the blue marbles with the 7 marbles that are not blue instead of with all 10 marbles."),
           ch("0.70", "This is the probability that the marble is not blue: 7 / 10.")],
          "P(blue) = 3 / 10 = 0.30.", difficulty="easy")

    B.mcq(T, "The probability that it rains on a given day in a city is 0.35. What is the probability that it does not rain on that day?",
          ch("0.65", "The probability of the complement of an event is 1 minus the probability of the event: 1 - 0.35."),
          [ch("0.35", "This is the probability that it rains, the event itself."),
           ch("1.35", "This adds 1 and 0.35. A probability cannot be greater than 1."),
           ch("0.54", "This is 0.35 / 0.65, a ratio of the two probabilities instead of the probability.")],
          "P(no rain) = 1 - 0.35 = 0.65.", difficulty="easy")

    B.mcq(T, "Which of the following could NOT be the probability of an event?",
          ch("1.25", "A probability is a number between 0 and 1, inclusive."),
          [ch("0", "A probability of 0 is possible: it is the probability of an event that cannot happen."),
           ch("1", "A probability of 1 is possible: it is the probability of an event that is certain."),
           ch("0.999", "This is between 0 and 1, so it can be a probability.")],
          "The probability of an event is a number between 0 and 1, inclusive, so 1.25 is not possible.", difficulty="easy")

    x = 1 - (0.20 + 0.35 + 0.10)
    assert abs(x - 0.35) < 1e-9
    B.mcq(T, "A random process has four possible outcomes that do not overlap, with probabilities 0.20, 0.35, 0.10 and x. What is the value of x?",
          ch("0.35", "The probabilities of all of the outcomes in the sample space add to 1: 1 - (0.20 + 0.35 + 0.10) = 0.35."),
          [ch("0.65", "This is the sum of the other three probabilities, 0.20 + 0.35 + 0.10, and not what remains."),
           ch("0.25", "This is 1 divided by 4, which assumes that the four outcomes are equally likely. They are not."),
           ch("0.45", "This is 1 - 0.55, which leaves out a probability. The three given probabilities add to 0.65.")],
          "The probability of the sample space is 1: x = 1 - 0.65 = 0.35.", difficulty="medium")

    B.mcq(T, "A fair coin is flipped 3 times. What is the probability of getting at least one head?",
          ch("0.875", "Use the complement: the only way to get no heads is 3 tails, with probability (1/2)(1/2)(1/2) = 1/8, so P(at least one head) = 1 - 1/8 = 7/8."),
          [ch("0.125", "This is the probability of 3 tails, the complement of the event."),
           ch("0.375", "This is the probability of exactly 1 head, which is only one of the ways to get at least one."),
           ch("0.500", "This is the probability of a head on any single flip, not on three flips.")],
          "P(at least one head) = 1 - P(no heads) = 1 - 1/8 = 0.875.", difficulty="medium")

    sev = 6 / 36
    B.mcq(T, "Two fair six-sided dice are rolled. What is the probability that the sum of the two numbers is 7?",
          ch("0.167", "Six of the 36 equally likely outcomes have a sum of 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1). 6 / 36 is about 0.167."),
          [ch("0.083", "This is 3 / 36. It counts the pairs without regard to the order, but the outcomes (1,6) and (6,1) are different."),
           ch("0.194", "This is 7 / 36, which uses the sum 7 as the number of favorable outcomes."),
           ch("0.091", "This is 1 / 11, which treats the 11 possible sums as equally likely. They are not.")],
          "P(sum of 7) = 6 / 36, about 0.167.", difficulty="medium")

    B.mcq(T, "A standard deck of 52 cards has 12 face cards (jacks, queens and kings). One card is selected at random. What is the probability that the card is not a face card?",
          ch("0.769", "The complement of a face card has 52 - 12 = 40 outcomes: 40 / 52, about 0.769."),
          [ch("0.231", "This is the probability that the card is a face card, 12 / 52."),
           ch("0.300", "This is 12 / 40, which compares the face cards with the cards that are not face cards."),
           ch("0.500", "This assumes that a card is a face card or not with equal probability, but the two are not equally likely.")],
          "P(not a face card) = 1 - 12 / 52 = 40 / 52, about 0.769.", difficulty="medium")

    B.mcq(T, "A six-sided die is not fair. The probability of rolling a 6 is 0.25, and each of the other five numbers is equally likely. What is the probability of rolling a 2?",
          ch("0.15", "The probabilities add to 1, so the other five numbers share 1 - 0.25 = 0.75. Each has 0.75 / 5 = 0.15."),
          [ch("0.167", "This is 1 / 6, which assumes that all of the six numbers are equally likely. The die is not fair."),
           ch("0.25", "This is the probability of rolling a 6, not a 2."),
           ch("0.125", "This is 0.75 / 6, which shares the remaining probability among six numbers instead of five.")],
          "P(2) = (1 - 0.25) / 5 = 0.15.", difficulty="hard")

    # ------------------------------------------------------------------------------------------------------------ 2.5
    T = 5
    B.mcq(T, "A single card is selected at random from a standard deck of 52 cards. Which of the following pairs of events is mutually exclusive?",
          ch("The card is a heart, and the card is a spade", "No card is both a heart and a spade, so the events cannot occur at the same time."),
          [ch("The card is a heart, and the card is a king", "The king of hearts is both, so the events can occur together."),
           ch("The card is a face card, and the card is red", "A red jack, queen or king is both a face card and red."),
           ch("The card is an ace, and the card is a spade", "The ace of spades is both an ace and a spade.")],
          "Mutually exclusive events cannot occur at the same time: P(heart and spade) = 0.", difficulty="easy")

    B.mcq(T, "For events A and B, P(A) = 0.30, P(B) = 0.40 and P(A and B) = 0.12. Which of the following is correct?",
          ch("A and B are not mutually exclusive, because P(A and B) is not 0", "Events are mutually exclusive only if the joint probability is 0. Here it is 0.12."),
          [ch("A and B are mutually exclusive, because 0.30 + 0.40 is less than 1", "The sum of two probabilities being less than 1 does not show anything about the joint probability."),
           ch("A and B are mutually exclusive, because P(A and B) is less than both P(A) and P(B)", "A joint probability is always less than or equal to each probability, so this does not show that the events are exclusive."),
           ch("A and B are mutually exclusive, because 0.12 is the product of 0.30 and 0.40", "A product that equals the joint probability shows independence, not that the events are mutually exclusive.")],
          "Since P(A and B) = 0.12 is not 0, the events can occur together.", difficulty="medium")

    B.mcq(T, "In a school, 40% of the students take Spanish, 25% take French, and no student takes both languages. Which of the following is the best justification that taking Spanish and taking French are mutually exclusive events?",
          ch("The joint probability is 0: P(Spanish and French) = 0", "Events are mutually exclusive if the probability that both occur is 0."),
          [ch("The sum of the probabilities is less than 1: 0.40 + 0.25 = 0.65", "Mutually exclusive events can have any sum. What matters is the probability that both happen."),
           ch("The joint probability is the product of the probabilities: 0.40 x 0.25 = 0.10", "A product would be the joint probability of independent events, and here no student takes both."),
           ch("The probability of Spanish is greater than the probability of French: 0.40 is greater than 0.25", "Comparing the two probabilities does not tell whether both can occur.")],
          "P(Spanish and French) = 0, so the events cannot occur together.", difficulty="medium")

    B.mcq(T, "A fair six-sided die is rolled once. Let A be the event that the number is even and let B be the event that the number is greater than 4. Which of the following is correct?",
          ch("A and B are not mutually exclusive, because rolling a 6 is in both events and P(A and B) = 1/6", "The outcome 6 is even and greater than 4, so the events can occur at the same time."),
          [ch("A and B are mutually exclusive, because the numbers 5 and 6 that are greater than 4 are not all even", "Events are exclusive only if no outcome is in both, and the number 6 is in both."),
           ch("A and B are mutually exclusive, because P(A) = 1/2 and P(B) = 1/3 are not equal", "Unequal probabilities do not make events mutually exclusive."),
           ch("A and B are not mutually exclusive, because P(A and B) = 1/2 + 1/3 = 5/6", "The joint probability is not the sum of the two probabilities. Only the outcome 6 is in both, so it is 1/6.")],
          "A = {2, 4, 6}, B = {5, 6}. The outcome 6 is in both, so P(A and B) = 1/6, which is not 0.", difficulty="medium")

    B.mcq(T, "For two events A and B that are mutually exclusive, with P(A) > 0 and P(B) > 0, which of the following must be true?",
          ch("A and B are not independent, because P(A and B) = 0 is not equal to P(A) x P(B)", "Independent events have P(A and B) = P(A) P(B), which is greater than 0 here."),
          [ch("A and B are independent, because the occurrence of one does not change anything about the other", "If A occurs, B cannot occur, so knowing A does change the probability of B."),
           ch("A and B are independent, because P(A and B) = 0 is less than both P(A) and P(B)", "Independence requires that the joint probability equal the product of the probabilities."),
           ch("A and B are independent only when P(A) + P(B) = 1, which is the case for complements", "Independence depends on the joint probability, not on whether the probabilities add to 1.")],
          "Mutually exclusive events with positive probabilities cannot be independent: knowing that A occurred makes P(B) become 0.", difficulty="hard")

    B.mcq(T, "In probability, what does P(A and B), the joint probability of events A and B, represent?",
          ch("The probability that both event A and event B occur", "The joint probability is the probability of the intersection of A and B."),
          [ch("The probability that event A occurs or event B occurs, or both", "That is the probability of the union."),
           ch("The probability that event A occurs, given that event B has occurred", "That is a conditional probability."),
           ch("The probability that neither event A nor event B occurs", "That is the probability of the complement of the union.")],
          "P(A and B) is the probability of the intersection: both occur.", difficulty="easy")

    ageT = twoway("Age group", ["Online", "Television", "Print"], ["Under 40", "40 or over"], [[120, 50, 30], [60, 80, 60]], caption="Main way of getting news, for 400 adults")
    B.mcq(T, "The table shows the main way of getting news of 400 adults. One adult is selected at random. Which of the following pairs of events is mutually exclusive?",
          ch("The adult is under 40, and the adult is 40 or over", "No adult is in both age groups."),
          [ch("The adult is under 40, and the adult gets news mainly online", "There are 120 adults who are under 40 and get news mainly online."),
           ch("The adult is under 40, and the adult gets news mainly from television", "There are 50 adults who are under 40 and get news mainly from television."),
           ch("The adult is 40 or over, and the adult gets news mainly from print", "There are 60 adults who are 40 or over and get news mainly from print.")],
          "The two age groups do not overlap, so P(under 40 and 40 or over) = 0.", diagram=ageT, difficulty="medium")

    # ------------------------------------------------------------------------------------------------------------ 2.6
    T = 6
    B.mcq(T, "For events A and B, P(B) = 0.40 and P(A and B) = 0.10. What is P(A | B), the probability of A given that B has occurred?",
          ch("0.25", "P(A | B) = P(A and B) / P(B) = 0.10 / 0.40."),
          [ch("0.04", "This is the product 0.10 x 0.40, instead of the quotient."),
           ch("0.10", "This is the joint probability, P(A and B), which has not been divided by P(B)."),
           ch("4.00", "This is 0.40 / 0.10, the quotient in the wrong order. A probability cannot be greater than 1.")],
          "P(A | B) = 0.10 / 0.40 = 0.25.", difficulty="easy")

    lunch = [[48, 32], [30, 90]]
    lt = twoway("Grade", ["Cafeteria lunch", "Packed lunch"], ["Grade 9", "Grade 10"], lunch, caption="Preferred lunch of 200 students, by grade level")
    packed = lunch[0][1] + lunch[1][1]
    B.mcq(T, "The table shows the preferred lunch of 200 students. One student is selected at random. Given that the student prefers a packed lunch, what is the probability that the student is in Grade 10?",
          ch(p3(lunch[1][1] / packed), f"Restrict to the {packed} students who prefer a packed lunch: {lunch[1][1]} / {packed}."),
          [ch(p3(lunch[1][1] / 200), "This divides by all 200 students, so it is the probability of being in Grade 10 and preferring a packed lunch."),
           ch(p3(lunch[1][1] / sum(lunch[1])), "This is the probability of preferring a packed lunch given Grade 10, the conditional probability in the other direction: 90 / 120."),
           ch(p3(sum(lunch[1]) / 200), "This is the probability of being in Grade 10, which ignores the given information: 120 / 200.")],
          f"P(Grade 10 | packed) = {lunch[1][1]} / {packed} = {p3(lunch[1][1] / packed)}.", diagram=lt, difficulty="medium")

    B.mcq(T, "For events A and B, P(A) = 0.60 and P(B | A) = 0.30. What is P(A and B)?",
          ch("0.18", "By the general multiplication rule, P(A and B) = P(A) P(B | A) = 0.60 x 0.30."),
          [ch("0.90", "This adds the two numbers. The joint probability is found by multiplying."),
           ch("0.50", "This is 0.30 / 0.60, which divides the conditional probability by P(A)."),
           ch("0.30", "This is the conditional probability P(B | A), not the joint probability.")],
          "P(A and B) = 0.60 x 0.30 = 0.18.", difficulty="easy")

    aces = Fraction(4, 52) * Fraction(3, 51)
    B.mcq(T, "Two cards are dealt, one after the other and without replacement, from a standard deck of 52 cards that has 4 aces. What is the probability that both cards are aces?",
          ch(f"{float(aces):.4f}", "P(first ace) = 4/52, and P(second ace | first ace) = 3/51, so P(both) = (4/52)(3/51) = 12/2,652."),
          [ch(f"{(4 / 52) ** 2:.4f}", "This is (4/52)(4/52), which treats the second draw as having the same probability as the first. The deck has one fewer ace and one fewer card."),
           ch(f"{4 / 52 + 3 / 51:.4f}", "This adds the two probabilities. Both cards must be aces, so the probabilities are multiplied."),
           ch(f"{8 / 52 * 3 / 51:.4f}", "This uses 8 aces instead of 4 on the first card, which is more than the number of aces in the deck.")],
          "P(both aces) = (4/52)(3/51), about 0.0045.", difficulty="medium")

    B.mcq(T, "A bag has 6 red marbles and 4 blue marbles. Two marbles are selected at random, one after the other and without replacement. Given that the first marble is blue, what is the probability that the second marble is blue?",
          ch("0.333", "After a blue marble is removed, the bag has 9 marbles and 3 of them are blue: 3 / 9."),
          [ch("0.400", "This is 4 / 10, the probability of blue on the first draw. The second draw is from a bag with one fewer marble."),
           ch("0.300", "This is 3 / 10, which removes the blue marble from the number of blue marbles but not from the total."),
           ch("0.444", "This is 4 / 9, which removes a marble from the total but not from the number of blue marbles.")],
          "P(second blue | first blue) = 3 / 9, about 0.333.", difficulty="medium")

    p_bus, p_late_bus, p_late_no = 0.30, 0.10, 0.05
    both = p_bus * p_late_bus
    p_late = both + (1 - p_bus) * p_late_no
    assert abs(both - 0.03) < 1e-9 and abs(p_late - 0.065) < 1e-9
    B.mcq(T, "Of the students at a school, 30% take the bus to school. A student who takes the bus is late with probability 0.10, and a student who does not take the bus is late with probability 0.05. What is the probability that a randomly selected student takes the bus and is late?",
          ch("0.030", "P(bus and late) = P(bus) P(late | bus) = 0.30 x 0.10."),
          [ch("0.065", "This is the probability that a student is late, 0.30(0.10) + 0.70(0.05). It includes the students who do not take the bus."),
           ch("0.100", "This is P(late | bus), the conditional probability, not the joint probability."),
           ch("0.400", "This adds 0.30 and 0.10. The joint probability is the product.")],
          "P(bus and late) = (0.30)(0.10) = 0.030.", difficulty="medium")

    B.mcq(T, "The probability that a student passes an exam, given that the student studied, is 0.90. Which of the following is a correct interpretation?",
          ch("Among the students who studied, the probability that a randomly selected student passes is 0.90", "A conditional probability restricts to the students who satisfy the condition, here those who studied."),
          [ch("Among the students who passed, the probability that a randomly selected student studied is 0.90", "That would be P(studied | passed), the conditional probability in the other direction."),
           ch("Of all of the students, 90% studied and passed the exam", "That would be a joint probability, the proportion of all students who both studied and passed."),
           ch("A student who studies is certain to pass the exam, because 0.90 is close to 1", "A probability of 0.90 is not certainty.")],
          "P(pass | studied) describes the students who studied.", difficulty="medium")

    B.mcq(T, "The table shows the preferred lunch of 200 students. One student is selected at random. Given that the student is in Grade 9, what is the probability that the student prefers a packed lunch?",
          ch("0.400", "Restrict to the 80 students in Grade 9: 32 / 80."),
          [ch("0.160", "This divides by all 200 students: 32 / 200."),
           ch("0.262", "This divides by the 122 students who prefer a packed lunch: 32 / 122. It is the probability of Grade 9 given a packed lunch."),
           ch("0.610", "This is the probability of preferring a packed lunch, 122 / 200, which ignores the grade.")],
          "P(packed | Grade 9) = 32 / 80 = 0.400.", diagram=lt, difficulty="medium")

    cond_t = table(["", "Has the condition", "Does not have the condition", "Total"],
                   [["Test positive", "90", "81", "171"], ["Test negative", "10", "819", "829"], ["Total", "100", "900", "1000"]],
                   caption="Test results for 1,000 people", row_headers=True)
    B.mcq(T, "The table shows the results of a medical test for 1,000 people. One person is selected at random. Given that the person tests positive, what is the probability that the person has the condition?",
          ch("0.526", "Restrict to the 171 people who test positive: 90 / 171."),
          [ch("0.900", "This is 90 / 100, the probability of testing positive given the condition. It is the conditional probability in the other direction."),
           ch("0.090", "This is 90 / 1,000, the probability of having the condition and testing positive."),
           ch("0.100", "This is the probability of having the condition, 100 / 1,000, which ignores the test result.")],
          "P(condition | positive) = 90 / 171, about 0.526.", diagram=cond_t, difficulty="hard")

    B.mcq(T, "Which of the following is a correct statement of the general multiplication rule for events A and B?",
          ch("P(A and B) = P(A) x P(B | A)", "The probability that both occur is the probability of A times the probability of B given that A has occurred."),
          [ch("P(A and B) = P(A) + P(B | A)", "The probabilities are multiplied, not added."),
           ch("P(A and B) = P(A) x P(B), always", "This holds only for independent events. The general rule uses the conditional probability."),
           ch("P(A and B) = P(A | B) / P(B)", "The conditional probability P(A | B) is P(A and B) / P(B), so this expression is not the joint probability.")],
          "General multiplication rule: P(A and B) = P(A) P(B | A).", difficulty="easy")

    # ------------------------------------------------------------------------------------------------------------ 2.7
    T = 7
    B.mcq(T, "Events A and B are independent, with P(A) = 0.50 and P(B) = 0.30. What is P(A and B)?",
          ch("0.15", "For independent events, P(A and B) = P(A) P(B) = 0.50 x 0.30."),
          [ch("0.80", "This is the sum of the two probabilities. The joint probability of independent events is the product."),
           ch("0.65", "This is P(A or B) = 0.50 + 0.30 - 0.15, the probability of the union."),
           ch("0.00", "This would be the joint probability of mutually exclusive events, not of independent events.")],
          "P(A and B) = 0.50 x 0.30 = 0.15.", difficulty="easy")

    ind = Fraction(120, 200) * Fraction(122, 200)
    joint = Fraction(90, 200)
    assert float(ind) != float(joint)
    B.mcq(T, "The table shows the preferred lunch of 200 students. One student is selected at random. Are the events \"the student is in Grade 10\" and \"the student prefers a packed lunch\" independent?",
          ch("No, because P(Grade 10 and packed) = 0.450 is not equal to P(Grade 10) P(packed) = 0.60(0.61) = 0.366", "Independent events have a joint probability equal to the product of the probabilities."),
          [ch("Yes, because P(Grade 10) and P(packed) are both greater than 0.50", "Independence does not depend on whether the probabilities are greater than 0.50. It depends on the joint probability."),
           ch("Yes, because the student can be in Grade 10 and prefer a packed lunch at the same time, which means that the two events are independent of each other", "Being possible together shows that the events are not mutually exclusive, not that they are independent."),
           ch("No, because the events are mutually exclusive, with P(Grade 10 and packed) = 0", "The joint probability is 90 / 200 = 0.45, so the events are not mutually exclusive.")],
          "The joint probability 0.450 is not the product 0.366, so the events are not independent.", diagram=lt, difficulty="medium")

    B.mcq(T, "Events A and B are independent. Which of the following must be true?",
          ch("P(B | A) = P(B)", "Knowing that A has occurred does not change the probability that B occurs."),
          [ch("P(A and B) = 0", "This is true for mutually exclusive events. Independent events with positive probabilities can occur together."),
           ch("P(A or B) = P(A) + P(B)", "This holds only when P(A and B) = 0. Independent events with positive probabilities have P(A and B) > 0."),
           ch("P(B | A) = 1 - P(B)", "That would mean that the occurrence of A strongly changes the probability of B.")],
          "For independent events, P(B | A) = P(B).", difficulty="easy")

    u1 = 0.40 + 0.35 - 0.15
    B.mcq(T, "For events A and B, P(A) = 0.40, P(B) = 0.35 and P(A and B) = 0.15. What is P(A or B)?",
          ch("0.60", "P(A or B) = P(A) + P(B) - P(A and B) = 0.40 + 0.35 - 0.15."),
          [ch("0.75", "This is P(A) + P(B), which counts the outcomes that are in both events twice."),
           ch("0.90", "This is 0.40 + 0.35 + 0.15, which adds the joint probability instead of subtracting it."),
           ch("0.15", "This is the probability of the intersection, P(A and B), not of the union.")],
          "P(A or B) = 0.40 + 0.35 - 0.15 = 0.60.", difficulty="easy")

    pu = 0.3 + 0.5 - 0.3 * 0.5
    assert abs(pu - 0.65) < 1e-9
    B.mcq(T, "Events A and B are independent, with P(A) = 0.30 and P(B) = 0.50. What is P(A or B)?",
          ch("0.65", "P(A and B) = 0.30 x 0.50 = 0.15, so P(A or B) = 0.30 + 0.50 - 0.15."),
          [ch("0.80", "This is P(A) + P(B), which counts P(A and B) twice."),
           ch("0.15", "This is P(A and B), the probability of the intersection."),
           ch("0.35", "This is 0.50 - 0.15, which does not include the outcomes in only A.")],
          "P(A or B) = 0.30 + 0.50 - (0.30)(0.50) = 0.65.", difficulty="medium")

    u2 = Fraction(13, 52) + Fraction(12, 52) - Fraction(3, 52)
    B.mcq(T, "A single card is selected at random from a standard deck of 52 cards. The deck has 13 hearts, 12 face cards, and 3 cards that are both hearts and face cards. What is the probability that the card is a heart or a face card?",
          ch(f"{float(u2):.3f}", "P(heart or face) = 13/52 + 12/52 - 3/52 = 22/52."),
          [ch(f"{25 / 52:.3f}", "This is 13/52 + 12/52, which counts the 3 face cards that are hearts twice."),
           ch(f"{3 / 52:.3f}", "This is the probability that the card is both a heart and a face card."),
           ch(f"{0.5:.3f}", "This treats the two events as if they were halves of the deck, which they are not.")],
          "P(heart or face card) = 22 / 52, about 0.423.", difficulty="medium")

    atl = 1 - 0.4 ** 2
    B.mcq(T, "A basketball player makes each free throw with probability 0.60, and the shots are independent. The player attempts two free throws. What is the probability that the player makes at least one of them?",
          ch("0.84", "Use the complement: P(miss both) = 0.40 x 0.40 = 0.16, so P(at least one) = 1 - 0.16."),
          [ch("0.36", "This is 0.60 x 0.60, the probability of making both free throws."),
           ch("0.60", "This is the probability of making a single free throw, which ignores the second attempt."),
           ch("1.20", "This adds 0.60 and 0.60. A probability cannot be greater than 1.")],
          "P(at least one) = 1 - (0.40)(0.40) = 0.84.", difficulty="medium")

    B.mcq(T, "A fair six-sided die is rolled twice. Let A be the event that the first roll is a 4, and let B be the event that the sum of the two rolls is 7. Which of the following is correct?",
          ch("A and B are independent, because P(B | A) = 1/6 is equal to P(B) = 6/36", "If the first roll is 4, the sum is 7 only when the second roll is 3, with probability 1/6. The probability of a sum of 7 is 6/36 = 1/6 whatever the first roll is."),
          [ch("A and B are not independent, because the sum depends on the number on the first roll", "The sum does depend on the first roll, but the probability that the sum is 7 stays the same, 1/6, whatever the first roll is."),
           ch("A and B are not independent, because the first roll is part of the outcomes for which the sum is 7", "Being related in this way does not make events dependent. Check whether P(B | A) = P(B)."),
           ch("A and B are not independent, because P(B | A) = 1/36 is not equal to P(B) = 1/6", "Given that the first roll is 4, the sum is 7 when the second roll is 3, which has probability 1/6.")],
          "P(B | A) = 1/6 = P(B), so the events are independent.", difficulty="hard")

    B.mcq(T, "For events A and B, P(A) = 0.40, P(B) = 0.50 and P(A or B) = 0.90. Which of the following is correct?",
          ch("A and B are mutually exclusive but not independent, because P(A and B) = 0.40 + 0.50 - 0.90 = 0 is not equal to (0.40)(0.50)", "A joint probability of 0 means that the events are mutually exclusive, and 0 is not the product 0.20."),
          [ch("A and B are independent but not mutually exclusive, because P(A and B) = 0.20 is the product of the probabilities", "Here P(A and B) = 0.40 + 0.50 - 0.90 = 0, not 0.20."),
           ch("A and B are both mutually exclusive and independent, because P(A and B) = 0", "Independence needs P(A and B) = P(A) P(B) = 0.20, which is not 0."),
           ch("A and B are neither mutually exclusive nor independent, because P(A or B) is not equal to 1", "The union does not need to be 1. The joint probability is 0, so the events are mutually exclusive.")],
          "P(A and B) = 0.40 + 0.50 - 0.90 = 0: mutually exclusive, and not independent since 0 is not 0.20.", difficulty="hard")

    pg = Fraction(80, 200) + Fraction(122, 200) - Fraction(32, 200)
    B.mcq(T, "The table shows the preferred lunch of 200 students. One student is selected at random. What is the probability that the student is in Grade 9 or prefers a packed lunch?",
          ch("0.850", "P(Grade 9 or packed) = 80/200 + 122/200 - 32/200 = 170/200."),
          [ch("1.010", "This is 80/200 + 122/200, which counts the 32 students who are in Grade 9 and prefer a packed lunch twice. It is greater than 1."),
           ch("0.160", "This is the probability of being in Grade 9 and preferring a packed lunch, 32/200."),
           ch("0.610", "This is the probability of preferring a packed lunch, which ignores the students in Grade 9 who prefer a cafeteria lunch.")],
          "P(Grade 9 or packed) = 170 / 200 = 0.850.", diagram=lt, difficulty="medium")
