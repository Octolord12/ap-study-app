"""Unit 7, topics 7.4 Population Genetics (10 questions) and 7.5 Hardy-Weinberg Equilibrium (10).

Required content (CED 2025-26): 7.4.A evolution is driven by random occurrences too: mutation is random and adds variation; genetic drift is a change in allele frequencies from a nonselective process in small
populations; the bottleneck effect and the founder effect are kinds of drift; migration can cause gene flow; 7.4.B mutations give variation for selection, drift can let a small population diverge, gene flow keeps
populations from diverging; 7.4.C changes in allele frequencies are evidence of evolution. 7.5.A the Hardy-Weinberg model describes a non-evolving population (large size, no migration, no new mutations, random
mating, no natural selection), conditions never met but a valuable null hypothesis; allele frequencies can be calculated from genotype frequencies (p + q = 1, p squared + 2pq + q squared = 1). Suggested skills:
3.B, 1.C, 5.A.
"""
from lib import *


def build(B):
    # ------------------------------------------------------------------ 7.4 Population genetics
    T = 4
    B.mcq(T, "Which statement correctly describes the role of mutation in the evolution of a population?",
          ch("Mutation is a random process that adds new genetic variation to a population, on which natural selection can then act.", "Mutations are random and provide new genetic variation."),
          [ch("Mutation is directed by the environment so that it produces the traits that the individuals of a population need in order to survive.", "Mutations are not directed by specific environmental pressures."),
           ch("Mutation removes genetic variation from a population, so that all of the individuals have the same alleles after a few generations.", "Mutation adds variation."),
           ch("Mutation occurs only in populations that are under strong selection, and it stops as soon as the environment becomes stable again.", "Mutations occur in all populations, whether or not there is selection.")],
          "Mutation is a random process that adds new genetic variation.", difficulty="easy")

    B.mcq(T, "Which statement best describes genetic drift?",
          ch("It is a change in allele frequencies that is caused by random chance events, and it has the largest effect in small populations.", "Genetic drift is a change in allele frequencies attributable to a nonselective process in small populations."),
          [ch("It is a change in allele frequencies that is caused by the selection of the best-adapted individuals, and it affects only large populations.", "Genetic drift is not selective and it has the greatest effect in small populations."),
           ch("It is a change in the DNA of one individual that is caused by radiation, and it is passed on to all of the individuals in the population.", "This describes a mutation, which is different from drift."),
           ch("It is the movement of individuals into a population, and it adds new alleles that were not previously in the population at all.", "This describes gene flow caused by migration.")],
          "Genetic drift is a chance change in allele frequencies, most important in small populations.", difficulty="easy")

    B.mcq(T, "A disease reduces a population of 5,000 animals to 20 survivors, and the population then grows again to 5,000. Compared with the original population, which result is most likely?",
          ch("The new population has lower genetic diversity, because the 20 survivors carried only a small sample of the alleles of the original population.", "A bottleneck effect reduces genetic diversity by chance, since only a few individuals pass on their alleles."),
          [ch("The new population has higher genetic diversity, because the large number of new births produces many new alleles in a few generations.", "Births do not create new alleles. The new population only has the alleles of the survivors."),
           ch("The new population has the same genetic diversity, because the survivors were chosen by chance and so they were a perfect copy of the original population.", "A small sample of a population is unlikely to contain all of its alleles."),
           ch("The new population has alleles that are better adapted to the disease, because the survivors were selected for resistance by the disease itself.", "In a bottleneck, survivors may be a chance sample. The effect is not necessarily due to selection.")],
          "A bottleneck is a type of genetic drift that reduces diversity.", difficulty="medium")

    B.mcq(T, "A few birds from a large mainland population are blown to an island and start a new population there. The frequency of a feather-color allele is 0.10 on the mainland and 0.60 on the island. Which process best explains the difference?",
          ch("The founder effect, because the birds that started the island population were a small sample whose allele frequencies differed from the mainland by chance.", "The founder effect is a type of genetic drift in which a separated group has different allele frequencies."),
          [ch("The bottleneck effect, because the mainland population was reduced to a very small size for at least one generation before the move.", "The mainland population was large. The change occurred when a few birds started a new population."),
           ch("Gene flow, because the birds on the island continued to exchange a large number of alleles with the mainland population.", "Gene flow would make the two populations more alike."),
           ch("Mutation, because the island has a different environment that directs the mutations to produce the allele for the new feather color.", "Mutations are random and are not directed by the environment.")],
          "The founder effect is genetic drift in a new, separated population.", difficulty="medium")

    B.mcq(T, "Which statement correctly describes the effect of gene flow between two populations of the same species?",
          ch("It adds alleles to one population and removes them from the other, which makes the populations more alike and prevents them from diverging into separate species.", "Gene flow between two populations prevents them from diverging into separate species."),
          [ch("It adds alleles to both populations by mutation, which makes the populations more different and causes them to diverge into separate species.", "Gene flow is the movement of alleles between populations, and it reduces divergence."),
           ch("It reduces the size of both populations so much that genetic drift is the only process that can change their allele frequencies.", "Gene flow is migration of alleles, and it does not by itself reduce the sizes of populations."),
           ch("It stops all of the random processes in the populations, so the allele frequencies of both populations stay the same over time.", "Gene flow itself changes allele frequencies.")],
          "Gene flow between populations prevents divergence.", difficulty="medium")

    rows = [("10", "0.08 to 0.92"), ("100", "0.34 to 0.66"), ("1,000", "0.46 to 0.54")]
    B.mcq(T, "A simulation started with an allele at a frequency of 0.50 in many populations of three different sizes. After 20 generations of random mating with no selection, the range of the allele frequency in the populations is shown. Which conclusion is best supported by the data?",
          ch("Allele frequencies drifted further from the starting value in smaller populations, so genetic drift has a larger effect in small populations.", "The range of allele frequencies is widest for the populations of 10 individuals."),
          [ch("Allele frequencies drifted further from the starting value in larger populations, so genetic drift has a larger effect in large populations than in small ones.", "The range is narrowest for the largest populations."),
           ch("Allele frequencies did not change in any of the populations, because there was no selection acting during the 20 generations.", "The frequencies changed from 0.50 by chance, in a way that depends on the size of the population."),
           ch("The size of the population has no effect on allele frequencies, because all of the populations started with the same frequency of 0.50.", "The range of frequencies depends on the size of the population.")],
          "Genetic drift is stronger in small populations.",
          diagram=table(["Population size", "Range of the allele frequency after 20 generations"], rows, caption="Genetic drift in simulated populations", row_headers=True), difficulty="medium")

    B.mcq(T, "Which of the following processes changes allele frequencies in a population in a nonrandom way?",
          ch("Natural selection, because individuals with certain phenotypes survive and reproduce more often than the others in the environment", "Natural selection is nonrandom with respect to fitness. Drift and mutation are random."),
          [ch("Genetic drift, because the alleles of the individuals who survive in a small population are chosen by their fitness in the environment", "Genetic drift is a random process and does not depend on fitness."),
           ch("The bottleneck effect, because the survivors of an event are always the individuals with the alleles that are best for the environment", "In a bottleneck, the survivors are a chance sample."),
           ch("Mutation, because the environment determines which alleles will be produced by a mutation in the DNA of the individuals", "Mutation is random and is not directed by the environment.")],
          "Natural selection is nonrandom; mutation, drift and the founder and bottleneck effects are random.", difficulty="medium")

    n1, f1, n2, f2 = 200, 0.50, 50, 0.10
    new_f = (n1 * f1 + n2 * f2) / (n1 + n2)
    assert round(new_f, 2) == 0.42
    B.mcq(T, f"A population of {n1} animals has a frequency of {f1:.2f} for an allele. {n2} migrants with a frequency of {f2:.2f} for the same allele join the population and breed with the residents. What is the new frequency of the allele in the combined population?",
          ch(f"{new_f:.2f}, because the allele copies from all {n1 + n2} animals are averaged: ({n1} x {f1:.2f} + {n2} x {f2:.2f}) / {n1 + n2}.", f"({n1 * f1:.0f} + {n2 * f2:.0f}) / {n1 + n2} = {new_f:.2f}.", round(new_f, 2)),
          [ch(f"{(f1 + f2) / 2:.2f}, because the new frequency is the simple average of the two frequencies, regardless of the sizes of the groups.", "The groups have different sizes, so the frequencies are weighted by the numbers of animals.", round((f1 + f2) / 2, 2)),
           ch(f"{f1:.2f}, because the frequency of an allele in a population cannot be changed by the arrival of animals from outside.", "Migration can change allele frequencies by adding or removing alleles.", f1),
           ch(f"{f1 - f2:.2f}, because the migrants remove their allele frequency from that of the residents in the combined population.", "The migrants add their alleles to the population. They do not subtract them.", round(f1 - f2, 2))],
          "Gene flow changes allele frequencies by adding alleles from the migrants.", difficulty="hard")

    rows = [("1", "0.80", "0.20"), ("2", "0.74", "0.26"), ("3", "0.65", "0.35")]
    assert all(abs(float(r[1]) + float(r[2]) - 1) < 1e-9 for r in rows)
    B.mcq(T, "The table shows the frequencies of two alleles in a population in three consecutive generations. Which statement is best supported by the data?",
          ch("Evolution has occurred in the population, because the frequencies of the alleles changed from one generation to the next.", "Changes in allele frequencies provide evidence for the occurrence of evolution in a population."),
          [ch("Evolution has not occurred in the population, because the sum of the frequencies of the two alleles is 1.00 in each generation.", "The sum is always 1. Evolution is shown by a change in the individual frequencies."),
           ch("Evolution has occurred in the population only if the frequency of allele A fell by more than half during the three generations.", "Any change in allele frequencies over generations is evolution."),
           ch("Evolution has occurred only in the first generation, because evolution requires a change in the number of individuals.", "Evolution is defined by changes in allele frequencies, not in the number of individuals.")],
          "Changes in allele frequencies over generations are evidence of evolution.",
          diagram=table(["Generation", "Frequency of allele A", "Frequency of allele a"], rows, caption="Allele frequencies over three generations", row_headers=True), difficulty="medium")

    B.mcq(T, "Two populations of the same species live on different sides of a river. Occasionally some individuals swim across the river and breed in the other population. Which prediction is most consistent with this?",
          ch("The populations are less likely to diverge into separate species, because the movement of individuals exchanges alleles between them.", "Gene flow between two populations prevents them from diverging into separate species."),
          [ch("The populations are more likely to diverge into separate species, because the individuals that swim are the fittest individuals in each population.", "The exchange of alleles makes the populations more alike."),
           ch("The populations are certain to become two species, because the river is a physical barrier that stops all of the mating between them.", "The river does not stop all gene flow, and gene flow prevents divergence."),
           ch("The populations will each lose all of their genetic variation, because migrating individuals cannot carry any alleles with them.", "Migrants carry alleles, and gene flow can add to the variation.")],
          "Gene flow keeps populations from diverging.", difficulty="medium")

    # ------------------------------------------------------------------ 7.5 Hardy-Weinberg equilibrium
    T = 5
    B.mcq(T, "Which of the following is a condition that must be met for a population to be in Hardy-Weinberg equilibrium?",
          ch("Mating in the population is random with respect to the gene, and the population is large enough that genetic drift is negligible.", "Conditions for Hardy-Weinberg equilibrium: a large population, no migration, no new mutations, random mating and no natural selection."),
          [ch("Individuals with certain genotypes survive and reproduce more than the others, so that selection keeps the allele frequencies steady.", "Natural selection is not allowed in a population in equilibrium."),
           ch("Individuals move into and out of the population freely, so that new alleles are added to the gene pool in every generation.", "There must be no migration."),
           ch("New mutations occur at a high rate in the population, so that the variation in the alleles is renewed in every generation.", "There must be no new mutations.")],
          "Hardy-Weinberg conditions: large population, no migration, no new mutations, random mating, no natural selection.", difficulty="easy")

    B.mcq(T, "In the Hardy-Weinberg equation, $p^2 + 2pq + q^2 = 1$, what does the term $2pq$ represent?",
          ch("The frequency of the heterozygous individuals in the whole population, which have one copy of each of the two alleles", "In the equation, 2pq is the frequency of heterozygotes."),
          [ch("The frequency of the dominant allele in the population, which is found in the homozygous dominant individuals only", "The frequency of an allele is p or q, not 2pq."),
           ch("The frequency of homozygous recessive individuals in the population, which have two copies of the recessive allele", "The frequency of homozygous recessive individuals is q squared."),
           ch("The frequency of all of the alleles in the population, which is the sum of the dominant and the recessive alleles", "The sum of the frequencies of the alleles is p + q = 1.")],
          "p squared and q squared are the homozygotes; 2pq is the heterozygotes.", difficulty="easy")

    q2 = 0.04
    q = q2 ** 0.5
    p = 1 - q
    het = 2 * p * q
    assert (round(q, 2), round(p, 2), round(het, 2)) == (0.2, 0.8, 0.32)
    B.mcq(T, f"In a population that is in Hardy-Weinberg equilibrium, the frequency of homozygous recessive individuals ($q^2$) is {q2:.2f}. What is the frequency of heterozygous individuals?",
          ch(f"{het:.2f}, because q = {q:.1f}, p = {p:.1f}, and 2pq = 2 x {p:.1f} x {q:.1f}.", f"q = the square root of 0.04 = 0.2, p = 0.8, and 2pq = 0.32.", round(het, 2)),
          [ch(f"{q:.2f}, because the square root of {q2:.2f} is the frequency of heterozygous individuals in the population.", "0.20 is the frequency of the recessive allele (q), not the frequency of heterozygotes.", round(q, 2)),
           ch(f"{p ** 2:.2f}, because that is the frequency of the homozygous dominant individuals when p is {p:.1f} in the population.", "p squared is the frequency of the homozygous dominant individuals, not of the heterozygotes.", round(p ** 2, 2)),
           ch(f"{1 - q2:.2f}, because all of the individuals that are not homozygous recessive are heterozygous in the population.", "Individuals that are not homozygous recessive include the homozygous dominant ones.", round(1 - q2, 2))],
          "q squared gives q; then p = 1 - q and the heterozygotes are 2pq.", difficulty="medium")

    N, rec = 1000, 360
    q = (rec / N) ** 0.5
    p = 1 - q
    carriers = 2 * p * q * N
    assert (round(q, 2), round(p, 2), round(carriers)) == (0.6, 0.4, 480)
    B.mcq(T, f"In a population of {N:,} individuals that is in Hardy-Weinberg equilibrium, {rec} individuals have the recessive phenotype for a trait. About how many individuals are heterozygous for the trait?",
          ch(f"{carriers:.0f}, because q = {q:.1f}, p = {p:.1f}, and 2pq x {N:,} = {carriers:.0f}.", f"q squared = {rec} / {N:,} = 0.36, so q = 0.6, p = 0.4, and 2pq = 0.48, which is 480 individuals.", round(carriers)),
          [ch(f"{rec}, because the number of individuals with the recessive phenotype is also the number that are heterozygous.", "The recessive phenotype is shown by the homozygous recessive individuals only. The heterozygotes are another group.", rec),
           ch(f"{(p ** 2) * N:.0f}, because the individuals that are not homozygous recessive are all heterozygous in the population.", "That is the number of homozygous dominant individuals (p squared x N).", round(p ** 2 * N)),
           ch(f"{q * N:.0f}, because the frequency of the recessive allele is the frequency of the heterozygous individuals.", "q is the frequency of the recessive allele and not of the heterozygous individuals.", round(q * N))],
          "q squared = frequency of the recessive phenotype; then 2pq gives the heterozygotes.", difficulty="medium")

    AA, Aa, aa = 50, 40, 10
    tot = AA + Aa + aa
    p = (2 * AA + Aa) / (2 * tot)
    assert (tot, p) == (100, 0.7)
    B.mcq(T, f"A population of {tot} individuals has {AA} with the genotype AA, {Aa} with the genotype Aa, and {aa} with the genotype aa. What is the frequency of the allele A?",
          ch(f"{p:.2f}, because there are {2 * AA + Aa} copies of A among the {2 * tot} alleles in the population.", f"(2 x {AA} + {Aa}) / (2 x {tot}) = {2 * AA + Aa} / {2 * tot} = {p:.2f}.", p),
          [ch(f"{AA / tot:.2f}, because the frequency of the allele is the same as the frequency of the AA genotype.", "Heterozygotes also carry one copy of A.", AA / tot),
           ch(f"{(AA + Aa) / tot:.2f}, because the allele is present in the individuals that have the AA and the Aa genotypes.", "This counts individuals and not alleles, and the Aa individuals have only one copy of A.", (AA + Aa) / tot),
           ch(f"{(2 * AA + Aa) / tot:.2f}, because the number of copies of A is divided by the number of individuals.", "The number of copies must be divided by the number of alleles, which is twice the number of individuals.", (2 * AA + Aa) / tot)],
          "Allele frequency = copies of the allele / total alleles (2N for a diploid).", difficulty="medium")

    p0, q0 = 0.7, 0.3
    exp = (p0 ** 2, 2 * p0 * q0, q0 ** 2)
    assert [round(e, 2) for e in exp] == [0.49, 0.42, 0.09]
    obs = (0.60, 0.20, 0.20)
    assert abs(sum(obs) - 1) < 1e-9
    rows = [("AA", "0.49", "0.60"), ("Aa", "0.42", "0.20"), ("aa", "0.09", "0.20")]
    B.mcq(T, "The allele frequencies in a population are p = 0.7 and q = 0.3. The table shows the genotype frequencies expected under Hardy-Weinberg equilibrium and the frequencies that were observed. Which conclusion is best supported by the data?",
          ch("The population is not in Hardy-Weinberg equilibrium, so one or more of the conditions are not met, for example if mating is not random.", "The observed frequencies differ greatly from the expected ones, so at least one condition for equilibrium is not met."),
          [ch("The population is in Hardy-Weinberg equilibrium, because the observed frequencies add up to 1.00 and so they match the expected values.", "The sum is always 1. What matters is whether each frequency matches the expected value."),
           ch("The population is in Hardy-Weinberg equilibrium, because the observed frequency of the genotype AA is higher than 0.49.", "A difference from the expected value shows that the population is not in equilibrium."),
           ch("The allele frequencies must be wrong, because the observed frequencies of the genotypes cannot differ from the expected ones.", "The observed genotype frequencies can differ from the expected ones when conditions are not met.")],
          "Hardy-Weinberg equilibrium is a null hypothesis; large deviations show that a condition is not met.",
          diagram=table(["Genotype", "Expected frequency", "Observed frequency"], rows, caption="Expected and observed genotype frequencies", row_headers=True), difficulty="hard")

    B.mcq(T, "No real population meets all of the conditions for Hardy-Weinberg equilibrium. Why is the model still useful to biologists?",
          ch("It provides a null hypothesis for a non-evolving population, so a difference from the predicted frequencies suggests that evolution is occurring.", "The conditions are never met, but they provide a valuable null hypothesis."),
          [ch("It shows that real populations never change, so a biologist can use it to predict the allele frequencies of a population in the future.", "The model describes a non-evolving population, and real populations do change."),
           ch("It proves that natural selection is the only process that changes allele frequencies, so the other processes can be ignored.", "Drift, gene flow and mutation also change allele frequencies."),
           ch("It gives the exact genotype frequencies of every real population, so a biologist does not need to count the individuals.", "The model predicts frequencies for an ideal population. Real populations must be sampled.")],
          "The Hardy-Weinberg model is a null hypothesis for a non-evolving population.", difficulty="medium")

    q2 = 1 / 2500
    q = q2 ** 0.5
    p = 1 - q
    het = 2 * p * q
    assert round(q, 2) == 0.02 and round(het, 4) == 0.0392 and round(1 / het) == 26
    B.mcq(T, "A recessive disorder affects 1 in 2,500 people in a population that is in Hardy-Weinberg equilibrium. About what fraction of the people are carriers (heterozygotes)?",
          ch(f"About {het:.3f}, or about 1 in {1 / het:.0f}, because q = 0.02, p = 0.98, and 2pq = 0.039.", "q squared = 1 / 2,500 = 0.0004, so q = 0.02, p = 0.98, and 2pq = 2 x 0.98 x 0.02 = 0.0392.", round(het, 3)),
          [ch(f"About {q:.2f}, or about 1 in {1 / q:.0f}, because the frequency of carriers is the same as the frequency of the recessive allele.", "0.02 is the frequency of the allele (q). Carriers have a frequency of 2pq.", round(q, 3)),
           ch(f"About {q2:.4f}, or about 1 in 2,500, because the carriers are as common as the people who are affected by the disorder.", "0.0004 is q squared, the frequency of the affected people. Carriers are much more common.", round(q2, 4)),
           ch(f"About {p ** 2:.2f}, or about 24 in 25, because most of the people in the population are carriers of the disorder.", "0.96 is the frequency of the homozygous dominant people, who are not carriers.", round(p ** 2, 2))],
          "Carriers (2pq) are much more common than affected people (q squared) for a rare recessive allele.", difficulty="hard")

    q0 = 0.5
    aa_f = q0 ** 2
    Aa_f = 2 * q0 * (1 - q0)
    q1 = (Aa_f / 2) / (1 - aa_f)
    assert round(q1, 3) == 0.333
    B.mcq(T, "In a population in Hardy-Weinberg equilibrium, the frequency of an allele a is 0.50. All of the individuals with the genotype aa die before they reproduce, and the survivors mate at random. What is the frequency of the allele a among the gametes of the survivors?",
          ch("About 0.33, because the survivors are 25% AA and 50% Aa, and a is carried by half of the alleles of the Aa individuals.", "The survivors are 0.25 AA and 0.50 Aa, so a = (0.50 / 2) / 0.75 = 0.33."),
          [ch("0.25, because the individuals with the genotype aa were 25% of the population, and they are the only source of the allele.", "The allele is also carried by the heterozygotes, which survive."),
           ch("0.50, because the frequency of an allele in a population does not change when individuals die before they reproduce.", "Selection against a genotype changes allele frequencies."),
           ch("0.00, because the allele a is removed from the population when all of the individuals with the genotype aa die.", "The heterozygotes still carry the allele a.")],
          "Selection against a genotype changes allele frequencies, so the population is no longer in equilibrium.", difficulty="hard")

    p0 = 0.6
    AAf = p0 ** 2
    assert round(AAf, 2) == 0.36
    B.mcq(T, f"In a population in Hardy-Weinberg equilibrium, the frequency of the dominant allele (p) is {p0:.1f}. What is the expected frequency of the homozygous dominant genotype in the next generation?",
          ch(f"{AAf:.2f}, because the frequency of the genotype is p squared and {p0:.1f} x {p0:.1f} = {AAf:.2f}.", "The frequency of the homozygous dominant genotype is p squared.", round(AAf, 2)),
          [ch(f"{p0:.2f}, because the frequency of the genotype is the same as the frequency of the allele in the population.", "The genotype needs two copies of the allele, so its frequency is p squared.", p0),
           ch(f"{2 * p0 * (1 - p0):.2f}, because the frequency of the genotype is calculated as two times p times q for the population.", "2pq is the frequency of heterozygotes.", round(2 * p0 * (1 - p0), 2)),
           ch(f"{(1 - p0) ** 2:.2f}, because the frequency of the genotype is the square of the frequency of the other allele.", "q squared is the frequency of the homozygous recessive genotype.", round((1 - p0) ** 2, 2))],
          "The frequency of the homozygous dominant genotype is p squared.", difficulty="easy")
