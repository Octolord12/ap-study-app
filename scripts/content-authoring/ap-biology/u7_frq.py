"""Unit 7: six free-response prompts, one of each kind.

  RESULTS        (9)  7.5   Hardy-Weinberg: genotype counts of a flower population (allele frequencies, the expected heterozygotes, a condition that is not met)
  RESULTS_GRAPH  (9)  7.3   artificial selection for bristle number in four replicate lines (replicate means and standard errors -> graph)
  INVESTIGATION  (4)  7.4   does genetic drift change allele frequencies more in small populations? (a bead model)
  CONCEPT        (4)  7.10  the biological species concept, gene flow and sympatric speciation
  MODEL          (4)  7.9   the vertebrate cladogram (the figure is a real cladogram diagram)
  DATA           (4)  7.6   protein differences against the time since divergence (a molecular clock, line graph)

Part structure follows the CED (see u3_frq.py). Every number is computed here from the raw data, and the sample responses are built from the same variables.
"""
from lib import *
from u7_phylo import vertebrate_tree


def build(B):
    # ------------------------------------------------------------------ RESULTS (9): Hardy-Weinberg
    BB, Bb, bb = 100, 60, 40
    n = BB + Bb + bb
    p = (2 * BB + Bb) / (2 * n)
    q = 1 - p
    exp_Bb = 2 * p * q * n
    exp_BB, exp_bb = p * p * n, q * q * n
    diff = (Bb - exp_Bb) / exp_Bb * 100
    assert (n, round(p, 2), round(q, 2), round(exp_Bb), round(diff)) == (200, 0.65, 0.35, 91, -34)
    rows = [("BB (red flowers)", str(BB)), ("Bb (pink flowers)", str(Bb)), ("bb (white flowers)", str(bb))]
    B.frq(5, "RESULTS",
          "In a species of flower, the alleles for flower color show incomplete dominance: plants with the genotype BB have red flowers, plants with the genotype Bb have pink flowers, and plants with the genotype bb have white flowers. A student counted the flowers of the plants in a meadow with 200 plants. The results are shown in the table. The student will compare the results with the genotype frequencies that are expected if the population is in Hardy-Weinberg equilibrium.\n\n"
          "**(a)** **Describe** two conditions that must be met for a population to be in Hardy-Weinberg equilibrium. (1 point)\n\n"
          "**(b)** (i) **Calculate** the frequency of the allele B (p) in the population. (ii) **Calculate** the frequency of the allele b (q). (iii) **Calculate** the number of pink-flowered plants that is expected if the population is in Hardy-Weinberg equilibrium. Give your answer to the nearest whole number. (3 points)\n\n"
          "**(c)** (i) **Calculate** the percent difference between the observed number of pink-flowered plants and the expected number, relative to the expected number. Give your answer to the nearest whole percent. (ii) **State** a null hypothesis for the comparison of the observed and the expected genotype frequencies. (iii) **Identify** one condition for Hardy-Weinberg equilibrium that the student's results suggest is not met, and justify your answer. (3 points)\n\n"
          "**(d)** **Predict** how the frequency of the allele b will change in the next generation if all of the plants with white flowers are eaten by herbivores before they reproduce, and **justify** your prediction. (2 points)",
          [(1, "(a) Describes two conditions: a large population, no migration (no gene flow), no new mutations, random mating, or no natural selection."),
           (1, "(b)(i) Calculates p = (2 x 100 + 60) / (2 x 200) = 0.65."),
           (1, "(b)(ii) Calculates q = 1 - 0.65 = 0.35."),
           (1, "(b)(iii) Calculates the expected number of pink plants as 2pq x 200 = 2 x 0.65 x 0.35 x 200 = 91."),
           (1, "(c)(i) Calculates (60 - 91) / 91 x 100 = -34 percent (34 percent fewer pink plants than expected)."),
           (1, "(c)(ii) States a null hypothesis: there is no difference between the observed genotype frequencies and the frequencies expected for Hardy-Weinberg equilibrium (any differences are due to chance)."),
           (1, "(c)(iii) Identifies a condition and justifies it: random mating is not met because there are fewer heterozygotes than expected, as when plants mate with similar plants (or no natural selection is not met if the pink plants survive less well)."),
           (1, "(d) Predicts that the frequency of the allele b will decrease."),
           (1, "(d) Justifies the prediction: the plants with the genotype bb do not pass on the allele b, so only the b alleles of the heterozygous plants are passed on, and natural selection reduces the frequency of b in the gene pool.")],
          f"(a) For example, the population must be large, and mating must be random.\n\n"
          f"(b) (i) p = (2 x {BB} + {Bb}) / (2 x {n}) = {2 * BB + Bb} / {2 * n} = {p:.2f}. (ii) q = 1 - {p:.2f} = {q:.2f}. (iii) 2pq x {n} = 2 x {p:.2f} x {q:.2f} x {n} = {exp_Bb:.0f} pink plants.\n\n"
          f"(c) (i) ({Bb} - {exp_Bb:.0f}) / {exp_Bb:.0f} x 100 = {diff:.0f} percent, so there are {-diff:.0f} percent fewer pink plants than expected. (ii) There is no difference between the observed genotype frequencies and the frequencies that are expected for Hardy-Weinberg equilibrium. (iii) Random mating is probably not met. There are many fewer heterozygous plants than expected, and that happens when plants mate more often with plants of the same genotype.\n\n"
          "(d) The frequency of the allele b will decrease. Plants with white flowers (bb) are eaten before they reproduce, so they do not pass on their b alleles. Only the b alleles in the heterozygous plants are passed on, so b is less common in the next generation.",
          diagram=table(["Genotype and flower color", "Number of plants"], rows, caption="Plants in a meadow of 200 plants", row_headers=True))

    # ------------------------------------------------------------------ RESULTS_GRAPH (9): artificial selection
    gens = ["0", "1", "2", "3", "4"]
    raw = {"0": [17.5, 18.4, 18.1, 18.0], "1": [20.9, 22.0, 21.3, 21.8], "2": [24.6, 25.4, 24.8, 25.2], "3": [28.0, 29.1, 28.3, 28.6], "4": [31.5, 32.6, 31.9, 32.0]}
    means = [mean(raw[g_]) for g_ in gens]
    ses = [se(raw[g_]) for g_ in gens]
    assert [round(m_, 1) for m_ in means] == [18.0, 21.5, 25.0, 28.5, 32.0], means
    rate = (means[-1] - means[0]) / (len(gens) - 1)
    assert rate == 3.5
    pct = (means[-1] - means[0]) / means[0] * 100
    assert round(pct) == 78
    rows = [(g_, fix(m_, 1), fix(e_, 2)) for g_, m_, e_ in zip(gens, means, ses)]
    se_text = ", ".join(fix(e_, 2) for e_ in ses[:-1]) + " and " + fix(ses[-1], 2)
    B.frq(3, "RESULTS_GRAPH",
          "Artificial selection is the selection of traits by humans. In an experiment, researchers raised four separate lines of fruit flies. In each generation of each line, they chose the flies with the most bristles on a part of the body as the parents of the next generation. They counted the bristles on the flies of each line in each generation. The means and the standard errors of the means of the four lines are shown in the table.\n\n"
          "**(a)** **Describe** how artificial selection differs from natural selection. (1 point)\n\n"
          "**(b)** **Construct** a graph of the data in the table. Because you are answering in writing, describe the graph you would draw: the type of graph, what is shown on each axis, with units, the scale of each axis, the values you would plot, and how you would show the standard errors. (4 points)\n\n"
          "**(c)** (i) **Calculate** the mean change in the number of bristles per generation from generation 0 to generation 4. (ii) **State** a null hypothesis for this investigation. (2 points)\n\n"
          "**(d)** **Predict** what will happen to the mean number of bristles in each line if the researchers choose the parents at random in the following generations, and **justify** your prediction. (2 points)",
          [(1, "(a) Describes that in artificial selection humans choose which individuals reproduce, but in natural selection the environment determines which individuals survive and reproduce more."),
           (1, "(b) Chooses an appropriate graph type: a line graph (or a bar graph) with the generation on the horizontal axis."),
           (1, "(b) Labels both axes with units: the generation (number) on the horizontal axis and the mean number of bristles per fly on the vertical axis."),
           (1, "(b) Gives an appropriate scale: a vertical axis that starts at 0 (or a broken axis that is marked) and has equal intervals, extending to at least 32 bristles so that all of the means fit."),
           (1, "(b) Plots the data accurately (18.0, 21.5, 25.0, 28.5 and 32.0 bristles) and shows error bars of plus and minus one standard error for each point."),
           (1, "(c)(i) Calculates (32.0 - 18.0) / 4 = 3.5 bristles per generation."),
           (1, "(c)(ii) States a null hypothesis: selecting the flies with the most bristles has no effect on the mean number of bristles (any differences between generations are due to chance)."),
           (1, "(d) Predicts that the mean number of bristles will stop increasing (it will stay about the same or fall slightly)."),
           (1, "(d) Justifies the prediction: without selection for high bristle number, the flies with high and low numbers of bristles reproduce at random, so the alleles for more bristles are no longer favored and the mean stops rising.")],
          "(a) In artificial selection, humans choose which individuals reproduce. In natural selection, the environment determines which individuals survive and reproduce more.\n\n"
          "(b) A line graph. The horizontal axis is labeled \"Generation\" with points at 0, 1, 2, 3 and 4. The vertical axis is labeled \"Mean number of bristles per fly\" and is scaled from 0 to 40 in steps of 10. The points are 18.0, 21.5, 25.0, 28.5 and 32.0, each with an error bar of plus and minus one standard error "
          f"({se_text} bristles, which are small).\n\n"
          f"(c) (i) ({means[-1]:.1f} - {means[0]:.1f}) / 4 = {rate:.1f} bristles per generation. (ii) Selecting the flies with the most bristles has no effect on the mean number of bristles.\n\n"
          "(d) The mean number of bristles will stop rising and stay about the same. When the parents are chosen at random, flies with more bristles are no more likely to reproduce than flies with fewer bristles, so the alleles for more bristles are no longer favored.",
          diagram=table(["Generation", "Mean number of bristles (n = 4 lines)", "Standard error"], rows, caption="Bristles on flies in four lines selected for more bristles", row_headers=True))

    # ------------------------------------------------------------------ INVESTIGATION (4): drift with beads
    B.frq(4, "INVESTIGATION",
          "A student models genetic drift with beads. A bag contains an equal number of red beads and blue beads, which represent two alleles of a gene. To make each new generation, the student draws beads at random from the bag, with each bead put back after it is drawn, until the bag for the next generation has the same number of beads as the first bag. The student does this for 10 generations. The student plans to do the model with a bag of 10 beads and with a bag of 100 beads, with 5 replicate bags of each size.\n\n"
          "**(a)** **Identify** the independent variable in the investigation. (1 point)\n\n"
          "**(b)** **Identify** one variable that must be kept the same in the bags of the two sizes. (1 point)\n\n"
          "**(c)** **Predict** how the frequency of the red beads after 10 generations will vary among the replicate bags of 10 beads, compared with the replicate bags of 100 beads. (1 point)\n\n"
          "**(d)** **Justify** your prediction. (1 point)",
          [(1, "(a) Identifies the independent variable as the size of the bag (the number of beads, which represents the size of the population)."),
           (1, "(b) Identifies a controlled variable, such as the starting proportion of red beads (0.5), the number of generations, or the way that the beads are drawn."),
           (1, "(c) Predicts that the frequency of the red beads after 10 generations will vary much more among the bags of 10 beads (some will be near 0 or 1) than among the bags of 100 beads (which will stay near 0.5)."),
           (1, "(d) Justifies: genetic drift is a change in allele frequencies caused by chance, and chance has a larger effect when a small sample of beads (a small population) is drawn each time.")],
          "(a) The size of the bag, which is the number of beads and represents the size of the population.\n\n"
          "(b) The starting proportion of red beads, which is 0.5 in all of the bags.\n\n"
          "(c) The frequency of the red beads will vary much more among the replicate bags of 10 beads, and some of them may end up with almost all red or almost all blue beads. The bags of 100 beads will stay close to 0.5.\n\n"
          "(d) Drift is a change in allele frequencies that is caused by chance. In each draw, a small sample is more likely to differ from the proportion in the bag than a large sample, so chance has a greater effect in the small populations.")

    # ------------------------------------------------------------------ CONCEPT (4): speciation
    B.frq(10, "CONCEPT",
          "A species of insect lives on a native plant. Some of the insects begin to feed and mate on a different plant that grows in the same area. Insects that feed on the new plant mate only with other insects that feed on the new plant.\n\n"
          "**(a)** **Describe** the biological species concept. (1 point)\n\n"
          "**(b)** **Explain** why gene flow between two populations prevents them from becoming separate species. (1 point)\n\n"
          "**(c)** **Predict** the type of speciation that could occur between the insects on the two plants, if the two groups continue to diverge. (1 point)\n\n"
          "**(d)** **Justify** your prediction. (1 point)",
          [(1, "(a) Describes that a species is a group of organisms that can interbreed and exchange genetic information to produce viable, fertile offspring."),
           (1, "(b) Explains that gene flow moves alleles between populations, which keeps their gene pools similar, so the populations do not diverge."),
           (1, "(c) Predicts sympatric speciation."),
           (1, "(d) Justifies: the two groups live in the same geographic area (they overlap), and become reproductively isolated because they feed and mate on different plants, so they do not exchange alleles.")],
          "(a) A species is a group of organisms that can interbreed and exchange genetic information to produce viable, fertile offspring.\n\n"
          "(b) Gene flow moves alleles between the populations, so the populations stay genetically similar and cannot diverge into separate species.\n\n"
          "(c) Sympatric speciation.\n\n"
          "(d) The two groups live in the same area, with no geographic barrier between them. They become reproductively isolated because they feed and mate on different plants, so they stop exchanging alleles and can diverge.")

    # ------------------------------------------------------------------ MODEL (4): cladogram
    B.frq(9, "MODEL",
          "The cladogram represents the evolutionary relationships among six animals. The traits that are shown on the branches are derived traits that were gained in the lineage that leads to the animals to the right of them. The lamprey is the outgroup. The numbers label the branching points.\n\n"
          "**(a)** **Explain** why the lamprey is used as the outgroup in the cladogram. (1 point)\n\n"
          "**(b)** **Identify** the number of the branching point that represents the most recent common ancestor of the lizard and the mouse. (1 point)\n\n"
          "**(c)** **Explain** how the cladogram shows that the mouse is more closely related to the human than to the shark. (1 point)\n\n"
          "**(d)** **Describe** one limitation of a cladogram such as this one. (1 point)",
          [(1, "(a) Explains that the outgroup is the lineage that is least closely related to the rest of the animals in the cladogram, and it provides a reference for deciding which traits are derived."),
           (1, "(b) Identifies the branching point 3."),
           (1, "(c) Explains that the mouse and the human share a more recent common ancestor (node 4) and share the derived trait hair, but the shark branched off earlier, before the lineage gained four limbs, the amniotic egg and hair."),
           (1, "(d) Describes a limitation: a cladogram does not show the time scale or the amount of evolutionary change (or it is a hypothesis that can be revised with new evidence).")],
          "(a) The lamprey is the lineage that is least closely related to the other five animals, so it is used as a reference to find out which traits are derived (new) in the other lineages.\n\n"
          "(b) Branching point 3.\n\n"
          "(c) The mouse and the human share a recent common ancestor at branching point 4, and they share the derived trait hair. The shark branched off earlier, before four limbs, the amniotic egg and hair appeared, so the mouse has a more recent common ancestor with the human than with the shark.\n\n"
          "(d) A cladogram does not show the time scale or the amount of change, so the lengths of the branches do not show how long ago the groups separated. It is also a hypothesis that can be changed by new evidence.",
          diagram=vertebrate_tree())

    # ------------------------------------------------------------------ DATA (4): molecular clock
    t_div = [10, 25, 50, 90, 140]
    diffs = [5, 12, 26, 44, 70]
    rates = [d_ / t_ for d_, t_ in zip(diffs, t_div)]
    assert [round(r_, 2) for r_ in rates] == [0.5, 0.48, 0.52, 0.49, 0.5]
    pred = 80 * 0.5
    g = graph("Time since the two species diverged (million years)", "Amino acid differences in a protein", 0, 150, 0, 80,
              [line("Pairs of species", list(zip(t_div, diffs)), "blue")],
              "Amino acid differences in a protein against the time since divergence for five pairs of species: 5 at 10, 12 at 25, 26 at 50, 44 at 90 and 70 at 140 million years.")
    B.frq(6, "DATA",
          "Scientists compared the amino acid sequence of the same protein in five pairs of species. For each pair, fossils were used to estimate the time since the two species diverged from a common ancestor. The graph shows the number of amino acid differences in the protein for each pair of species.\n\n"
          "**(a)** **Describe** the relationship between the time since divergence and the number of amino acid differences. (1 point)\n\n"
          "**(b)** **Calculate** the rate of change, in amino acid differences per million years, for the pair that diverged 140 million years ago. (1 point)\n\n"
          "**(c)** A student claims that the protein changes at a constant rate. **Evaluate** the claim using the data. (1 point)\n\n"
          "**(d)** **Predict** the number of amino acid differences for a pair of species that diverged 80 million years ago, and **explain** how such data can be used as a molecular clock. (1 point)",
          [(1, "(a) Describes that the number of amino acid differences increases as the time since divergence increases (a positive, nearly linear relationship)."),
           (1, "(b) Calculates 70 / 140 = 0.5 amino acid differences per million years."),
           (1, "(c) Evaluates the claim as supported, using data: the rate is about the same for all five pairs (0.48 to 0.52 differences per million years), so the changes accumulate at an approximately constant rate."),
           (1, "(d) Predicts about 40 differences (0.5 x 80), and explains that if differences accumulate at a constant rate, the number of differences between two species can be used to estimate the time since they diverged.")],
          "(a) The number of amino acid differences increases as the time since divergence gets longer. The relationship is nearly a straight line.\n\n"
          "(b) 70 / 140 = 0.5 amino acid differences per million years.\n\n"
          f"(c) The data support the claim. The rate for the five pairs is {', '.join(fix(r_, 2) for r_ in rates[:-1])} and {fix(rates[-1], 2)} differences per million years, so it is about the same for all of the pairs, which shows that the changes accumulate at about a constant rate.\n\n"
          "(d) About 40 differences, because 0.5 x 80 = 40. If the differences accumulate at a constant rate, the number of differences between two species can be divided by the rate to estimate how long ago they diverged, so the protein can be used as a molecular clock.",
          diagram=g)
