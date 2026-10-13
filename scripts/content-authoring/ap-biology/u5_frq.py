"""Unit 5: six free-response prompts, one of each kind.

  RESULTS        (9)  5.3  a chi-square test of a dihybrid cross (observed counts, the 9:3:3:1 expectation, the critical value)
  RESULTS_GRAPH  (9)  5.5  clones of a plant grown with four amounts of nitrogen (replicate means and standard errors -> graph)
  INVESTIGATION  (4)  5.4  reciprocal crosses to test whether a body-color gene is on the X chromosome
  CONCEPT        (4)  5.2  crossing over, independent assortment and nondisjunction in a cell with 2n = 6
  MODEL          (4)  5.1  a table of cells, chromosomes and DNA at four stages of meiosis
  DATA           (4)  5.4  offspring of a test cross of two linked genes (a bar graph of counts)

Part structure follows the CED (see u3_frq.py). Every number is computed here from the raw data.
"""
from lib import *


def build(B):
    # ------------------------------------------------------------------ RESULTS (9): chi-square of a dihybrid cross
    obs = [171, 68, 58, 23]
    ratio = [9, 3, 3, 1]
    total = sum(obs)
    exp = [total * r / 16 for r in ratio]
    assert total == 320 and exp == [180.0, 60.0, 60.0, 20.0]
    chi = sum((o - e) ** 2 / e for o, e in zip(obs, exp))
    crit = 7.81  # AP equation sheet, p = 0.05, 3 degrees of freedom
    assert round(chi, 2) == 2.03 and chi < crit
    terms = [(o - e) ** 2 / e for o, e in zip(obs, exp)]
    assert [round(t, 3) for t in terms] == [0.45, 1.067, 0.067, 0.45]  # the sample response quotes these
    assert round(sum(round(t, 3) for t in terms), 2) == 2.03
    phenos = ["Round, yellow", "Round, green", "Wrinkled, yellow", "Wrinkled, green"]
    rows = [(p, str(o)) for p, o in zip(phenos, obs)]
    B.frq(3, "RESULTS",
          "In pea plants, the allele for round seeds (R) is dominant to the allele for wrinkled seeds (r), and the allele for yellow seeds (Y) is dominant to the allele for green seeds (y). The genes for the two traits are on different chromosomes. A student crossed two plants that were each heterozygous for both genes (RrYy x RrYy) and counted the seeds of the 320 offspring. The results are shown in the table. The student will use a chi-square test to compare the results with the results that are expected for independent assortment.\n\n"
          "**(a)** **Describe** how the behavior of the chromosomes in meiosis allows a plant with the genotype RrYy to make four kinds of gametes. (1 point)\n\n"
          "**(b)** (i) **State** the null hypothesis for the test. (ii) **Calculate** the number of round, yellow seeds that is expected if the null hypothesis is correct. (iii) **Identify** the number of degrees of freedom for the test. (3 points)\n\n"
          "**(c)** (i) **Calculate** the chi-square value for the data. Give your answer to the nearest 0.01. (ii) **Use** the critical value of 7.81 (p = 0.05, 3 degrees of freedom) to determine whether the null hypothesis should be rejected. (iii) **Explain** what the result of the test shows about the inheritance of the two traits. (3 points)\n\n"
          "**(d)** A second student crosses plants with two other genes and finds many more offspring with the parental combinations of traits than the number that is expected for independent assortment. **Identify** a possible explanation for the second student's result and **justify** the explanation. (2 points)",
          [(1, "(a) Describes that the pairs of homologous chromosomes line up at random at the equator in metaphase I, so the alleles of the two genes (on different chromosomes) are sorted independently into gametes (RY, Ry, rY and ry)."),
           (1, "(b)(i) States a null hypothesis: there is no significant difference between the observed numbers of offspring and the numbers expected for a 9:3:3:1 ratio (the two genes assort independently), and any difference is due to chance."),
           (1, "(b)(ii) Calculates 9/16 x 320 = 180 round, yellow seeds."),
           (1, "(b)(iii) Identifies 3 degrees of freedom (four categories minus one)."),
           (1, "(c)(i) Calculates chi-square = (171 - 180)²/180 + (68 - 60)²/60 + (58 - 60)²/60 + (23 - 20)²/20 = 2.03."),
           (1, "(c)(ii) Determines that the null hypothesis should not be rejected, because 2.03 is less than the critical value of 7.81."),
           (1, "(c)(iii) Explains that the observed numbers do not differ significantly from the numbers expected for a 9:3:3:1 ratio, so the data are consistent with independent assortment of the two genes (the difference can be due to chance)."),
           (1, "(d) Identifies the explanation that the two genes are linked (close together on the same chromosome)."),
           (1, "(d) Justifies: linked genes are usually passed on together, so the parental combinations occur more often than expected, and only the crossing over between the genes makes the recombinant combinations, which are rarer.")],
          "(a) In metaphase I the homologous pairs line up at the equator at random. The pair with R and r and the pair with Y and y are on different chromosomes, so each pair is oriented independently, and a gamete can receive any combination of one allele of each gene: RY, Ry, rY or ry.\n\n"
          "(b) (i) The null hypothesis is that there is no significant difference between the observed numbers and the numbers expected for a 9:3:3:1 ratio (the genes assort independently); any difference is due to chance. (ii) 9/16 x 320 = 180. (iii) There are four categories, so 4 - 1 = 3 degrees of freedom.\n\n"
          "(c) (i) The expected numbers are 180, 60, 60 and 20. Chi-square = (171 - 180)²/180 + (68 - 60)²/60 + (58 - 60)²/60 + (23 - 20)²/20 = 0.450 + 1.067 + 0.067 + 0.450 = 2.03. (ii) 2.03 is less than 7.81, so the null hypothesis is not rejected. (iii) The observed numbers do not differ significantly from the numbers expected for independent assortment, so the data are consistent with the two genes being inherited independently.\n\n"
          "(d) The two genes could be linked, close together on one chromosome. Linked genes tend to be inherited together, so the parental combinations are common, and only crossing over between the genes makes the recombinant combinations, which are therefore less common than 9:3:3:1 predicts.",
          diagram=table(["Phenotype of the seeds", "Observed number of offspring"], rows, caption="Seeds of the offspring of the cross RrYy x RrYy", row_headers=True))

    # ------------------------------------------------------------------ RESULTS_GRAPH (9): nitrogen and plant height
    doses = ["0", "2", "4", "8"]
    raw = {"0": [10.2, 11.0, 9.8, 10.6, 10.4], "2": [15.1, 16.0, 15.6, 14.8, 15.5], "4": [21.0, 22.4, 21.7, 20.9, 22.0], "8": [22.8, 23.9, 23.1, 23.5, 23.2]}
    means = [mean(raw[d_]) for d_ in doses]
    ses = [se(raw[d_]) for d_ in doses]
    assert [round(m_, 1) for m_ in means] == [10.4, 15.4, 21.6, 23.3], means
    assert [round(e_, 2) for e_ in ses] == [0.20, 0.21, 0.29, 0.19], ses  # the sample response quotes these
    inc = pct_change(means[0], means[3])
    assert round(inc) == 124, inc
    rows = [(d_, fix(m_, 1), fix(e_, 2)) for d_, m_, e_ in zip(doses, means, ses)]
    B.frq(5, "RESULTS_GRAPH",
          "The phenotype of an organism depends on its genotype and on its environment. Researchers took cuttings from a single plant, so that all of the new plants were genetically identical, and grew them in pots. Each plant received the same amount of water and light and one of four amounts of nitrogen fertilizer. After six weeks, the researchers measured the height of each plant. Each amount of fertilizer was given to five plants. The means and the standard errors of the means are shown in the table.\n\n"
          "**(a)** **Describe** how the environment can influence the phenotype of an organism. (1 point)\n\n"
          "**(b)** **Construct** a graph of the data in the table. Because you are answering in writing, describe the graph you would draw: the type of graph, what is shown on each axis, with units, the scale of each axis, the values you would plot, and how you would show the standard errors. (4 points)\n\n"
          "**(c)** (i) **Calculate** the percent increase in the mean height between the plants that received no fertilizer and the plants that received 8 g of fertilizer. Give your answer to the nearest whole percent. (ii) **State** a null hypothesis for this investigation. (2 points)\n\n"
          "**(d)** **Predict** whether the difference in the mean heights of the plants that received no fertilizer and the plants that received 8 g of fertilizer is caused by a difference in their genotypes, and **justify** your prediction. (2 points)",
          [(1, "(a) Describes that environmental factors (such as nutrients, temperature or light) can affect how the genes of an organism are expressed, so that the same genotype can produce different phenotypes in different environments."),
           (1, "(b) Chooses an appropriate graph type: a bar graph (or a line graph) with the amount of fertilizer on the horizontal axis."),
           (1, "(b) Labels both axes with units: the amount of nitrogen fertilizer (g) on the horizontal axis and the mean height of the plants (cm) on the vertical axis."),
           (1, "(b) Gives an appropriate scale: a vertical axis that starts at 0 and has equal intervals, extending to at least 25 cm so that all of the means fit."),
           (1, "(b) Plots the data accurately (about 10.4, 15.4, 21.6 and 23.3 cm) and shows error bars of plus and minus one standard error for each point."),
           (1, "(c)(i) Calculates (23.3 - 10.4) / 10.4 x 100 = 124 percent increase."),
           (1, "(c)(ii) States a null hypothesis: the amount of nitrogen fertilizer has no effect on the mean height of the plants (any differences are due to chance)."),
           (1, "(d) Predicts that the difference is not caused by a difference in genotype."),
           (1, "(d) Justifies the prediction: all of the plants came from cuttings of one plant, so they have the same genotype, and the amount of fertilizer was the only variable that was different, so it is the environment that caused the different phenotypes.")],
          "(a) The environment can change how genes are expressed, so one genotype can produce different phenotypes. For example, the nutrients that are available to a plant can affect how tall it grows.\n\n"
          "(b) A bar graph. The horizontal axis is labeled \"Amount of nitrogen fertilizer (g)\" with bars at 0, 2, 4 and 8. The vertical axis is labeled \"Mean height of the plants (cm)\" and is scaled from 0 to 30 in steps of 5. The bars are about 10.4, 15.4, 21.6 and 23.3, each with an error bar of plus and minus one standard error (about 0.20, 0.21, 0.29 and 0.19 cm, which are small).\n\n"
          "(c) (i) (23.3 - 10.4) / 10.4 x 100 = 124 percent. (ii) The amount of nitrogen fertilizer has no effect on the mean height of the plants.\n\n"
          "(d) No, the difference is not caused by a difference in genotype. All of the plants were grown from cuttings of one plant, so they have the same genotype. The amount of fertilizer was the only thing that was different, so the difference in the heights was caused by the environment.",
          diagram=table(["Amount of nitrogen fertilizer (g)", "Mean height of the plants (cm) (n = 5)", "Standard error"], rows, caption="Effect of nitrogen on the height of genetically identical plants", row_headers=True))

    # ------------------------------------------------------------------ INVESTIGATION (4): reciprocal crosses
    B.frq(4, "INVESTIGATION",
          "In a species of fly, the body can be gray or yellow. A student hypothesizes that the allele for yellow bodies is recessive and is on the X chromosome. The student plans two crosses of true-breeding flies. In cross 1, a yellow female is crossed with a gray male. In cross 2, a gray female is crossed with a yellow male. The student will record the sex and the body color of each of the offspring in both crosses.\n\n"
          "**(a)** **Identify** the dependent variable in the investigation. (1 point)\n\n"
          "**(b)** **Predict** the body colors of the daughters and of the sons in cross 1 if the hypothesis is correct. (1 point)\n\n"
          "**(c)** **Predict** the body colors of the daughters and of the sons in cross 2 if the hypothesis is correct. (1 point)\n\n"
          "**(d)** **Justify** your predictions for cross 1 and cross 2. (1 point)",
          [(1, "(a) Identifies the dependent variable as the body color (and sex) of the offspring (the numbers of gray and yellow daughters and sons)."),
           (1, "(b) Predicts that, in cross 1, all of the daughters are gray and all of the sons are yellow."),
           (1, "(c) Predicts that, in cross 2, all of the offspring (daughters and sons) are gray."),
           (1, "(d) Justifies: a son receives his X chromosome from his mother and his Y chromosome from his father, so the sons show the trait of the mother; a daughter receives an X chromosome from each parent, so in cross 1 she receives the dominant allele from her father, and in cross 2 she receives the dominant allele from her mother.")],
          "(a) The dependent variable is the body color of the offspring, recorded for the daughters and the sons separately.\n\n"
          "(b) In cross 1 (yellow female x gray male), all of the daughters are gray and all of the sons are yellow.\n\n"
          "(c) In cross 2 (gray female x yellow male), all of the offspring are gray.\n\n"
          "(d) A son gets his X chromosome from his mother and his Y chromosome from his father. In cross 1 the mother has only the recessive allele, so the sons are yellow, and the daughters get the dominant allele on the X chromosome from their father, so they are gray. In cross 2 the mother has only the dominant allele, so every son and every daughter receives it from her, and all of the offspring are gray.")

    # ------------------------------------------------------------------ CONCEPT (4): meiosis, 2n = 6
    n_pairs = 3
    combos = 2 ** n_pairs
    assert combos == 8
    B.frq(2, "CONCEPT",
          "A species of insect has six chromosomes in its body cells (2n = 6). Sexual reproduction in this species increases the genetic variation of the offspring.\n\n"
          "**(a)** **Describe** how crossing over in meiosis increases the genetic variation of the gametes. (1 point)\n\n"
          "**(b)** **Calculate** the number of different combinations of maternal and paternal chromosomes that can be present in the gametes of one insect as a result of the independent assortment of the chromosomes. Ignore crossing over. (1 point)\n\n"
          "**(c)** In one cell, the sister chromatids of one chromosome fail to separate in meiosis II. **Predict** the number of chromosomes in each of the four gametes that are produced from the original cell before meiosis I. (1 point)\n\n"
          "**(d)** **Justify** your prediction. (1 point)",
          [(1, "(a) Describes that, in prophase I, non-sister chromatids of homologous chromosomes exchange segments of DNA, which makes chromatids with new combinations of alleles."),
           (1, "(b) Calculates 2³ = 8 combinations (three pairs of homologous chromosomes, each of which can line up in two ways)."),
           (1, "(c) Predicts that two of the gametes have 3 chromosomes, one has 4 chromosomes and one has 2 chromosomes."),
           (1, "(d) Justifies: meiosis I is normal, so both cells have 3 chromosomes, and in meiosis II the normal cell makes two gametes with 3 chromosomes, but the cell with the nondisjunction gives one gamete both copies of the chromosome (4 chromosomes) and the other gamete none of them (2 chromosomes).")],
          "(a) In prophase I, the homologous chromosomes pair up and non-sister chromatids exchange segments of DNA. This makes chromatids with combinations of alleles that were not present on either of the original chromosomes, so the gametes are more varied.\n\n"
          "(b) There are three pairs of chromosomes, and each pair can line up in two ways, so there are 2³ = 8 combinations.\n\n"
          "(c) Two gametes have 3 chromosomes, one gamete has 4 chromosomes and one gamete has 2 chromosomes.\n\n"
          "(d) Meiosis I was normal, so both cells that it made have 3 chromosomes. The normal cell separates its sister chromatids in meiosis II and makes two gametes with 3 chromosomes. In the other cell, both chromatids of one chromosome go to the same gamete, so that gamete has 4 chromosomes and the other has 2.")

    # ------------------------------------------------------------------ MODEL (4): meiosis table
    stages = [("Beginning of interphase (G1)", "1", "4", "2"), ("Before meiosis I (after S phase)", "1", "4", "4"), ("End of meiosis I", "2", "2", "2"), ("End of meiosis II", "4", "2", "1")]
    assert [int(s[1]) * int(s[3]) for s in stages] == [2, 4, 4, 4]  # the total amount of DNA is conserved until the last division
    B.frq(1, "MODEL",
          "The table is a model of the changes in the number of cells, the number of chromosomes per cell and the amount of DNA per cell (in arbitrary units) as a diploid cell with four chromosomes (2n = 4) goes through meiosis.\n\n"
          "**(a)** **Identify** the stage in the model in which the cells become haploid, and **describe** what separates at this stage. (1 point)\n\n"
          "**(b)** **Explain** why the model shows a decrease in the amount of DNA per cell from 4 units to 2 units at the end of meiosis I and from 2 units to 1 unit at the end of meiosis II, although the number of chromosomes per cell is the same at the end of meiosis II as it is at the end of meiosis I. (1 point)\n\n"
          "**(c)** **Describe** one way in which the values in the model would be different if the cell had divided once by mitosis instead of meiosis. (1 point)\n\n"
          "**(d)** **Describe** one limitation of the model for explaining how meiosis produces genetic variation. (1 point)",
          [(1, "(a) Identifies the end of meiosis I (the number of chromosomes per cell changes from 4 to 2), and describes that the homologous chromosomes separate."),
           (1, "(b) Explains that, in meiosis I, the homologous chromosomes separate and each cell receives half of the chromosomes (each with two chromatids), and in meiosis II the sister chromatids separate, so each cell has the same number of chromosomes but each chromosome has only one chromatid, which halves the DNA again."),
           (1, "(c) Describes a difference: mitosis would produce 2 cells (not 4), each with 4 chromosomes (not 2) and 2 units of DNA (not 1)."),
           (1, "(d) Describes a limitation: the model does not show crossing over or the random alignment of the homologous pairs, so it does not show that the four cells are genetically different (it shows only the numbers).")],
          "(a) The cells become haploid at the end of meiosis I, when the number of chromosomes per cell changes from 4 to 2. The homologous chromosomes separate at this stage.\n\n"
          "(b) In meiosis I the homologous chromosomes separate, so each cell has half of the chromosomes, and each chromosome still has two sister chromatids, so the DNA per cell is halved from 4 to 2. In meiosis II the sister chromatids separate, so each chromosome has one chromatid, and the DNA per cell is halved again to 1, but the number of chromosomes stays at 2.\n\n"
          "(c) Mitosis would make only 2 cells at the end, each with 4 chromosomes and 2 units of DNA, and not 4 cells with 2 chromosomes and 1 unit.\n\n"
          "(d) The model shows only the numbers of cells, chromosomes and the amount of DNA. It does not show crossing over or the random alignment of the homologous pairs, so it cannot show that the four cells have different combinations of alleles.",
          diagram=table(["Stage", "Number of cells", "Chromosomes per cell", "DNA per cell (arbitrary units)"], stages, caption="Model of the changes during meiosis in a cell with 2n = 4", row_headers=True))

    # ------------------------------------------------------------------ DATA (4): linked genes, counts of a test cross
    cats = ["Gray body, normal wings", "Black body, vestigial wings", "Gray body, vestigial wings", "Black body, normal wings"]
    counts = [425, 405, 80, 90]
    tot = sum(counts)
    rf = (counts[2] + counts[3]) / tot * 100
    assert tot == 1000 and rf == 17.0
    exp_each = tot / 4
    assert exp_each == 250
    chart = bars("Phenotype of the offspring", "Number of offspring", 500, ["Gray, normal", "Black, vestigial", "Gray, vestigial", "Black, normal"],
                 [{"values": counts, "color": "blue"}],
                 alt="Bar graph of the numbers of offspring: gray with normal wings 425, black with vestigial wings 405, gray with vestigial wings 80, black with normal wings 90.")
    B.frq(4, "DATA",
          "In fruit flies, the genes for body color (gray or black) and wing shape (normal or vestigial) are on the same chromosome. Female flies that are heterozygous for both genes, with the alleles for gray body and normal wings on one chromosome and the alleles for black body and vestigial wings on the homologous chromosome, were crossed with male flies that have black bodies and vestigial wings (homozygous recessive for both genes). The graph shows the numbers of the 1,000 offspring of each phenotype.\n\n"
          "**(a)** **Describe** the pattern in the numbers of the four phenotypes of the offspring. (1 point)\n\n"
          "**(b)** **Calculate** the percent of the offspring that are recombinants (the recombination frequency). (1 point)\n\n"
          "**(c)** A student claims that the genes for body color and wing shape are on different chromosomes. **Evaluate** the claim using the data. (1 point)\n\n"
          "**(d)** **Explain** how the recombinant offspring were produced. (1 point)",
          [(1, "(a) Describes that the offspring with the parental combinations (gray body with normal wings, and black body with vestigial wings) are much more numerous (425 and 405) than the offspring with the new combinations (80 and 90)."),
           (1, "(b) Calculates (80 + 90) / 1,000 x 100 = 17 percent."),
           (1, "(c) Evaluates the claim as not supported, using data: for genes on different chromosomes about 25 percent of the offspring (about 250) would be expected in each phenotype class, but the observed numbers are very different from 250, so the genes are linked."),
           (1, "(d) Explains that crossing over between the two genes in prophase I of meiosis in the heterozygous female exchanged segments between non-sister chromatids of the homologous chromosomes and made gametes with new combinations of alleles.")],
          "(a) Most of the offspring have the parental combinations: 425 are gray with normal wings and 405 are black with vestigial wings. Only a few have new combinations: 80 are gray with vestigial wings and 90 are black with normal wings.\n\n"
          "(b) (80 + 90) / 1,000 x 100 = 17 percent.\n\n"
          "(c) The data do not support the claim. If the genes were on different chromosomes, they would assort independently and each of the four phenotypes would make up about 25 percent (about 250) of the offspring. The observed numbers are very different from 250 and the parental types are much more common, so the genes are linked.\n\n"
          "(d) In prophase I of meiosis in the heterozygous female, crossing over between the two genes exchanged segments between non-sister chromatids of the homologous chromosomes. This made some gametes with new combinations of alleles (gray with vestigial and black with normal), which gave the recombinant offspring.",
          diagram=chart)
