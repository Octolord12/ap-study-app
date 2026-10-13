"""Unit 5, topic 5.3 Mendelian Genetics (12 questions).

Required content (CED 2025-26): 5.3.A the rules of probability (multiplication for independent events, addition for mutually exclusive events) apply to inheritance; 5.3.B Mendel's model of
dominant and recessive alleles, Punnett squares, monohybrid and dihybrid crosses, test crosses (a cross of an individual of unknown genotype with a homozygous recessive), pedigrees; independent
assortment of genes on different chromosomes; 5.3.C chi-square tests compare observed and expected counts: chi-square = sum of (o - e)^2 / e, degrees of freedom = number of categories - 1, a value below
the critical value at p = 0.05 means the difference could be due to chance (fail to reject the null hypothesis). Suggested skills: 5.A, 5.C, 6.D.
"""
from fractions import Fraction as F

from lib import *

# AP equation sheet: critical values at p = 0.05, degrees of freedom 1 to 8.
CRIT_05 = {1: 3.84, 2: 5.99, 3: 7.81, 4: 9.49, 5: 11.07, 6: 12.59, 7: 14.07, 8: 15.51}


def chi_square(observed, expected):
    return sum((o - e) ** 2 / e for o, e in zip(observed, expected))


def frac(x):
    return f"{x.numerator}/{x.denominator}"


def build(B):
    T = 3

    # Aa x Aa: probability of aa
    p_aa = F(1, 2) * F(1, 2)
    assert p_aa == F(1, 4)
    B.mcq(T, "A heterozygous pea plant (Aa) is crossed with another heterozygous plant (Aa). What is the probability that an offspring is homozygous recessive (aa)?",
          ch(f"{frac(p_aa)}, because the probability that each parent passes on the a allele is 1/2 and the two events are independent", "The probabilities of independent events are multiplied: 1/2 x 1/2 = 1/4.", 0.25),
          [ch("1/2, because half of the alleles that each parent has are recessive alleles and so half of the offspring are recessive", "The offspring needs the recessive allele from both parents, so the two probabilities are multiplied.", 0.5),
           ch("3/4, because three of the four possible offspring show the recessive phenotype in the Punnett square of this cross", "Three fourths of the offspring show the dominant phenotype. One fourth are aa.", 0.75),
           ch("0, because a heterozygous parent shows the dominant phenotype and so cannot pass on the recessive allele to its offspring", "A heterozygous parent can pass on either allele, each with a probability of 1/2.", 0.0)],
          "The rule of multiplication gives the probability of two independent events: 1/2 x 1/2 = 1/4.", difficulty="easy")

    # Test cross
    B.mcq(T, "A test cross is performed with a pea plant that shows a dominant phenotype and has an unknown genotype. Half of the offspring show the dominant phenotype and half show the recessive phenotype. What is the genotype of the unknown plant?",
          ch("Heterozygous, because a plant that is homozygous dominant would have produced only offspring that show the dominant phenotype", "A test cross is a cross with a homozygous recessive. Half and half indicates that the unknown parent makes two kinds of gametes."),
          [ch("Homozygous dominant, because the plant shows the dominant phenotype and so both of its alleles must be dominant alleles", "A homozygous dominant plant would have only offspring with the dominant phenotype in a test cross."),
           ch("Homozygous recessive, because the offspring show the recessive phenotype and so the parent must have two recessive alleles", "The parent shows the dominant phenotype, so it has at least one dominant allele."),
           ch("It cannot be determined, because the cross used only one parent that has an unknown genotype and so the ratio is not useful", "The ratio of the phenotypes of the offspring shows the genotype of the unknown parent.")],
          "A test cross with a homozygous recessive reveals the genotype of the individual with the dominant phenotype.", difficulty="easy")

    # Dihybrid 9:3:3:1
    p_dom = F(3, 4)
    p_both = p_dom * p_dom
    p_neither = F(1, 4) * F(1, 4)
    assert p_both == F(9, 16) and p_neither == F(1, 16)
    B.mcq(T, "Two pea plants that are heterozygous for two genes on different chromosomes (AaBb) are crossed. What fraction of the offspring is expected to show the dominant phenotype for both traits?",
          ch(f"{frac(p_both)}, because 3/4 of the offspring show the dominant phenotype for each trait and the genes assort independently", "Independent probabilities are multiplied: 3/4 x 3/4 = 9/16.", float(p_both)),
          [ch("3/16, because three of the sixteen boxes in the Punnett square show the dominant phenotype for both of the traits", "3/16 is the fraction that shows one dominant and one recessive phenotype, such as A_ bb.", 3 / 16),
           ch("1/16, because only one of the sixteen boxes in the Punnett square shows the dominant phenotype for both of the traits", f"1/16 is the fraction that is homozygous recessive for both genes (aabb).", 1 / 16),
           ch("3/4, because each plant has the dominant phenotype and so three fourths of the offspring show it for both of the traits", "3/4 is the fraction that shows the dominant phenotype for a single trait.", 0.75)],
          "In a dihybrid cross AaBb x AaBb the phenotypes are in the ratio 9:3:3:1.", difficulty="medium")

    # Three children all dominant
    p3 = F(3, 4) ** 3
    assert p3 == F(27, 64)
    B.mcq(T, "Two parents are both heterozygous (Aa) for a gene. The dominant allele A produces the dominant phenotype. What is the probability that three children of these parents all show the dominant phenotype?",
          ch(f"{frac(p3)}, because each child has a probability of 3/4 of showing the dominant phenotype and the births are independent events", "The probability of three independent events is the product: 3/4 x 3/4 x 3/4 = 27/64.", float(p3)),
          [ch("9/16, because the probability of the dominant phenotype in each child is 3/4 and this is multiplied by the same probability twice", "This is (3/4)², the probability for two children and not for three.", 9 / 16),
           ch("3/4, because the genotypes of the parents do not change and so the probability is the same as that for each child", "The probability that all three children show the dominant phenotype is lower than the probability for one child.", 0.75),
           ch("9/4, because the probability of 3/4 for each child is added for each of the three children in the family", "Probabilities of independent events are multiplied. A probability cannot be greater than 1.", 9 / 4)],
          "The rule of multiplication gives the probability that independent events all occur.", difficulty="medium")

    # Rule of addition: heterozygous offspring
    p_het = F(1, 4) + F(1, 4)
    assert p_het == F(1, 2)
    B.mcq(T, "Two heterozygous parents (Aa x Aa) have an offspring. The offspring can be heterozygous because it receives A from the first parent and a from the second parent, or because it receives a from the first parent and A from the second parent. What is the probability that the offspring is heterozygous?",
          ch(f"{frac(p_het)}, because the probabilities of the two mutually exclusive ways to be heterozygous (1/4 each) are added", "The rule of addition applies to mutually exclusive events: 1/4 + 1/4 = 1/2.", 0.5),
          [ch("1/4, because each of the two ways to be heterozygous has a probability of 1/4 and so the answer is the same", "There are two different ways to be heterozygous, and their probabilities are added.", 0.25),
           ch("1/16, because the probabilities of 1/4 for the two ways to be heterozygous are multiplied by each other", "The two ways are mutually exclusive, so the probabilities are added and not multiplied.", 1 / 16),
           ch("3/4, because three of the four possible genotypes of the offspring are different from the genotype of the parents", "Only the genotype Aa is heterozygous. Of the four boxes in the Punnett square two are Aa.", 0.75)],
          "The rule of addition gives the probability that one of several mutually exclusive events occurs.", difficulty="medium")

    # Crosses table: dominance deduction
    rows = [("1", "Purple x purple", "Some offspring white"), ("2", "White x white", "All offspring white"), ("3", "Purple x white", "All offspring purple")]
    B.mcq(T, "A student crosses pea plants and records the results in the table. Which statement is best supported by the data?",
          ch("Purple is dominant, because two purple parents in cross 1 had some white offspring, so the purple parents carried a hidden allele for white.", "Two parents that show the same phenotype and have some offspring with a different phenotype means that the trait of the parents is dominant and that the parents were heterozygous."),
          [ch("White is dominant, because two white parents in cross 2 had only white offspring and so white was transmitted to every offspring.", "A recessive trait also breeds true. All white offspring from two white parents is expected when white is recessive."),
           ch("Purple is recessive, because two purple parents in cross 1 had some offspring with a different color from the color of the parents.", "If purple was recessive, two purple parents would have only purple offspring."),
           ch("Neither allele is dominant, because the offspring of cross 3 do not show the white phenotype of one of their two parents.", "When one phenotype appears in the offspring and the other is hidden, the phenotype that appears is dominant.")],
          "Two parents with the same phenotype that have offspring with a different phenotype are both heterozygous for a dominant trait.",
          diagram=table(["Cross", "Parent phenotypes", "Offspring"], rows, caption="Results of three crosses of pea plants", row_headers=True), difficulty="medium")

    # Independent assortment explanation
    B.mcq(T, "Mendel observed that two genes that are on different chromosomes are inherited independently of each other. Which statement best explains this observation?",
          ch("The homologous pairs of chromosomes line up at random at the equator in metaphase I, so the alleles of one gene do not affect the alleles of the other in a gamete.", "The orientation of each homologous pair at metaphase I is random, so genes on different chromosomes assort independently."),
          [ch("Each gene is replicated at a different time in the S phase, so the alleles of one gene are not passed on together with the alleles of another gene.", "The time of replication does not determine which alleles end up in a gamete."),
           ch("The alleles of different genes cross over in prophase II, so the alleles of one gene are always exchanged with the alleles of another gene.", "Crossing over happens between homologous chromosomes in prophase I and it does not explain the independence of genes on different chromosomes."),
           ch("The sister chromatids of every chromosome separate in meiosis I, so the alleles of the two genes are separated from each other in this division.", "Homologous chromosomes separate in meiosis I. Sister chromatids separate in meiosis II.")],
          "Independent assortment of genes on different chromosomes results from the random alignment of homologous pairs in metaphase I.", difficulty="medium")

    # Chi-square 1: fail to reject
    obs = [140, 60]
    exp = [150, 50]
    assert sum(obs) == sum(exp) == 200
    chi = chi_square(obs, exp)
    assert round(chi, 2) == 2.67 and chi < CRIT_05[1]
    B.mcq(T, f"A monohybrid cross is expected to give a 3:1 ratio of phenotypes. Among 200 offspring, the student observes {obs[0]} with the dominant phenotype and {obs[1]} with the recessive phenotype. The chi-square value is {fix(chi, 2)}. The critical value at p = 0.05 with 1 degree of freedom is {CRIT_05[1]}. Which conclusion is best supported?",
          ch("The null hypothesis cannot be rejected, because the chi-square value is lower than the critical value, so the difference could be due to chance.", "A chi-square value that is lower than the critical value means that there is no significant difference between the observed and the expected counts."),
          [ch("The null hypothesis is rejected, because the observed counts are not exactly the same as the expected counts of 150 and 50.", "Some difference from the expected counts is expected because of chance. The test compares the chi-square value with the critical value."),
           ch("The null hypothesis is proved true, because the chi-square value is lower than the critical value, and so the ratio of 3:1 is shown to be correct for the cross.", "A chi-square test can fail to reject the null hypothesis. It cannot prove it."),
           ch("The null hypothesis is rejected, because the chi-square value is greater than zero, which means that the counts are different.", "A value greater than zero is expected from chance. The value is compared with the critical value.")],
          "If chi-square is lower than the critical value, the null hypothesis is not rejected.", difficulty="medium")

    # Chi-square 2: reject
    obs2 = [130, 70]
    chi2 = chi_square(obs2, exp)
    assert round(chi2, 2) == 10.67 and chi2 > CRIT_05[1]
    B.mcq(T, f"In a second experiment, the student observes {obs2[0]} offspring with the dominant phenotype and {obs2[1]} with the recessive phenotype, and the expected counts are {exp[0]} and {exp[1]}. The chi-square value is {fix(chi2, 2)}. The critical value at p = 0.05 with 1 degree of freedom is {CRIT_05[1]}. Which conclusion is best supported?",
          ch("The null hypothesis is rejected, because the chi-square value is greater than the critical value, so the difference is unlikely to be due to chance alone.", "A chi-square value that is greater than the critical value means that the null hypothesis is rejected."),
          [ch("The null hypothesis cannot be rejected, because the chi-square value is greater than the critical value, and so the difference between the counts must be due to chance alone.", "A value that is greater than the critical value leads to rejection of the null hypothesis."),
           ch("The null hypothesis cannot be rejected, because the observed counts of 130 and 70 are close to the expected counts of 150 and 50.", "The conclusion depends on the chi-square value and the critical value and not on how close the counts look."),
           ch("The experiment is invalid, because the chi-square value is greater than the chi-square value that was found in the first experiment.", "A chi-square test can reject a null hypothesis in one experiment and not in another.")],
          "If chi-square is greater than the critical value, the null hypothesis is rejected.", difficulty="medium")

    # Degrees of freedom
    B.mcq(T, "A student uses a chi-square test to compare the observed numbers of offspring of a dihybrid cross in four phenotype categories with the numbers that are expected. How many degrees of freedom should the student use to find the critical value?",
          ch("3, because the degrees of freedom are the number of phenotype categories minus one, and 4 - 1 = 3", "The degrees of freedom for a chi-square test are the number of categories minus 1: 4 - 1 = 3.", 3),
          [ch("4, because there are four phenotype categories and each category adds one degree of freedom to the test", "One is subtracted from the number of categories.", 4),
           ch("1, because the null hypothesis is a single hypothesis about the ratio of the phenotypes of the offspring", "The degrees of freedom depend on the number of categories and not on the number of hypotheses.", 1),
           ch("16, because the Punnett square of a dihybrid cross has sixteen boxes and each box is a degree of freedom", "The categories are the phenotypes, not the boxes of the Punnett square.", 16)],
          "Degrees of freedom = number of categories - 1.", difficulty="easy")

    # Multi-gene probability
    p_abc = F(1, 4) * F(3, 4) * F(1, 4)
    assert p_abc == F(3, 64)
    B.mcq(T, "Two parents are both heterozygous for three genes on different chromosomes (AaBbCc x AaBbCc). What is the probability that an offspring has the genotype aa, shows the dominant phenotype for the second gene (B_), and has the genotype cc?",
          ch(f"{frac(p_abc)}, because the probability for each gene is found separately (1/4, 3/4 and 1/4) and the three probabilities are multiplied", "The genes assort independently, so the probabilities are multiplied: 1/4 x 3/4 x 1/4 = 3/64.", float(p_abc)),
          [ch("1/64, because the probability of the recessive genotype of each of the three genes is 1/4 and the probabilities are multiplied", "The second gene is required to show the dominant phenotype, which has a probability of 3/4 and not of 1/4.", 1 / 64),
           ch("9/64, because two of the three genes have to show a recessive genotype and the other gene has to be dominant", "The dominant requirement applies to one gene (B_) and two genes need the recessive genotype: 1/4 x 3/4 x 1/4.", 9 / 64),
           ch("5/4, because the probabilities of 1/4, 3/4 and 1/4 for the three genes are added to give the total for the offspring", "Probabilities for independent events that must all occur are multiplied. A probability cannot be greater than 1.", 5 / 4)],
          "Multiply the probabilities of independent events that must all occur.", difficulty="hard")

    # Cross prediction: ratio for test cross dihybrid
    ratio = F(1, 2) * F(1, 2)
    assert ratio == F(1, 4)
    B.mcq(T, "A plant with the genotype AaBb is crossed with a plant with the genotype aabb. The two genes are on different chromosomes. What fraction of the offspring is expected to have the genotype aabb?",
          ch(f"{frac(ratio)}, because 1/2 of the gametes of the AaBb plant carry a, 1/2 carry b, and the aabb plant gives only a and b gametes", "The probability of an a gamete is 1/2 and the probability of a b gamete is 1/2, so 1/2 x 1/2 = 1/4.", float(ratio)),
          [ch("1/16, because the genotype aabb has a probability of 1/16 when two double heterozygotes are crossed with each other", "1/16 applies to a cross of two double heterozygotes. Here one parent is aabb and makes only ab gametes.", 1 / 16),
           ch("1/2, because the aabb plant gives only gametes that carry recessive alleles and so half of the offspring have its genotype", "Each gamete from the AaBb plant must also carry both recessive alleles, which has a probability of 1/4.", 0.5),
           ch("9/16, because the genes are on different chromosomes and so the offspring show the ratio of 9:3:3:1 in this cross", "The ratio 9:3:3:1 applies to a cross of two double heterozygotes.", 9 / 16)],
          "In a test cross of a dihybrid, each of the four phenotype classes is expected at a frequency of 1/4.", difficulty="hard")
