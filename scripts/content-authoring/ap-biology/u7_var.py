"""Unit 7, topics 7.11 Variations in Populations (7 questions) and 7.12 Origins of Life on Earth (7).

Required content (CED 2025-26): 7.11.A the level of variation in a population affects its dynamics: populations and species with little genetic diversity are at risk of decline or extinction; genetically diverse
populations are more resilient to environmental perturbation because they are more likely to contain individuals that can withstand the pressure; alleles adaptive in one environment may be deleterious in another.
7.12.A the origin of life is supported by geological evidence: Earth formed about 4.6 billion years ago (bya), was too hostile for life until about 3.9 bya, and the earliest fossil evidence of life dates to 3.5 bya;
the RNA world hypothesis proposes RNA as the earliest genetic material, assuming replication of RNA, base-pairing for replication, and no genetically encoded proteins as catalysts. Suggested skills: 6.C, 3.B.
"""
from lib import *


def build(B):
    # ------------------------------------------------------------------ 7.11 Variations in populations
    T = 11
    B.mcq(T, "Why is a population with high genetic diversity better able to survive a change in its environment than a population with little genetic diversity?",
          ch("It is more likely to contain some individuals with alleles that allow them to survive and reproduce under the new conditions.", "Genetically diverse populations are more resilient because they are more likely to contain individuals that can withstand the environmental pressure."),
          [ch("Each individual in a diverse population can change its alleles when the environment changes, so that all of them survive.", "Individuals do not change their alleles in response to the environment."),
           ch("A diverse population has more individuals than a population with little diversity, so the environment affects fewer of them at one time.", "Diversity refers to the variation in alleles and not to the size of the population."),
           ch("A diverse population produces mutations in response to the new conditions, so the mutations always give the needed alleles.", "Mutations are random and are not produced in response to the conditions.")],
          "Genetic diversity increases the chance that some individuals can withstand a change.", difficulty="easy")

    B.mcq(T, "A new fungal disease spreads through a population of trees. In a population with high genetic diversity, some trees survive, but in a population of genetically identical trees, all of the trees die. Which statement best explains the difference?",
          ch("The diverse population contained trees with alleles for resistance, but the identical trees all lacked these alleles and were all equally susceptible.", "Not all of the individuals in a diverse population are susceptible to a disease outbreak."),
          [ch("The trees in the diverse population were exposed to less of the fungus, because diverse trees repel the fungus from their leaves.", "Diversity does not reduce the exposure of the trees to the fungus."),
           ch("The trees in the identical population chose not to resist the fungus, because they had no differences from each other to choose from.", "Trees do not choose whether to resist a disease."),
           ch("The diverse population made new alleles for resistance after it was exposed to the fungus, which the identical trees were not able to do.", "Alleles for resistance must already be present, because mutations are random.")],
          "Not all individuals in a diverse population are susceptible to the same threat.", difficulty="medium")

    B.mcq(T, "An allele makes the fur of mice thicker. Thicker fur helps mice to survive in a cold climate but makes them overheat in a hot climate. Which statement best describes the allele?",
          ch("It is adaptive in the cold climate and deleterious in the hot climate, because the selective pressures on the mice differ between the climates.", "Alleles that are adaptive in one environment may be deleterious in another because of different selective pressures."),
          [ch("It is adaptive in both climates, because an allele that is useful in one environment has to be useful in every environment.", "An allele can be useful in one environment and harmful in another."),
           ch("It is deleterious in both climates, because every allele that changes the fur of an animal reduces the fitness of the animal.", "The allele is favored in the cold climate."),
           ch("It is neutral in both climates, because the thickness of the fur has no effect on how well the mice are able to survive.", "The thickness of the fur does affect survival in each climate.")],
          "Alleles that are adaptive in one environment may be deleterious in another.", difficulty="medium")

    B.mcq(T, "Population X has 12 different alleles of an immune gene, and population Y has 2 alleles of the same gene. A new pathogen appears in both populations. Which prediction is the most reasonable?",
          ch("Population X is more likely to contain individuals that resist the pathogen, so it is less likely to decline or become extinct.", "Species and populations with little genetic diversity are at risk of decline or extinction."),
          [ch("Population Y is more likely to contain individuals that resist the pathogen, because it has fewer alleles to be affected by it.", "Fewer alleles mean a lower chance that one of them gives resistance."),
           ch("Both populations are equally likely to resist the pathogen, because the number of alleles of a gene does not affect resistance.", "Diversity increases the chance of some resistance."),
           ch("Neither population can be affected by the pathogen, because pathogens do not attack the individuals that have an immune gene.", "Pathogens can affect individuals that have immune genes.")],
          "Low genetic diversity puts a population at risk.", difficulty="medium")

    rows = [("One variety (genetically uniform)", "4"), ("Five varieties (genetically diverse)", "61")]
    B.mcq(T, "A fungus attacks fields of a crop. The table shows the percent of the plants that survived in fields planted with one variety and in fields planted with five varieties. Which conclusion is best supported by the data?",
          ch("Fields with higher genetic diversity were more resilient to the disease, because they were more likely to contain plants that withstood it.", "Genetically diverse populations are more resilient to environmental perturbation."),
          [ch("Fields with a single variety were more resilient to the disease, because all of the plants in them had the same alleles and so were protected.", "The uniform fields had a much lower survival."),
           ch("The number of varieties had no effect on the survival of the plants, because some plants survived in both kinds of fields.", "The survival was much higher in the diverse fields."),
           ch("The diverse fields had fewer plants infected by the fungus, because the fungus cannot infect plants of different varieties.", "The data show survival and not infection, and a fungus can infect several varieties.")],
          "Genetic diversity increases resilience to a threat.",
          diagram=table(["Planting", "Plants that survived (%)"], rows, caption="Survival of a crop after a fungal attack", row_headers=True), difficulty="medium")

    N, frac = 50000, 0.01
    surv = N * frac
    assert surv == 500
    B.mcq(T, f"A population of {N:,} genetically diverse plants includes {int(frac * 100)}% with an allele for resistance to a disease. All of the plants without the allele die, and a population of {N:,} genetically identical plants without the allele is exposed to the same disease. How many plants are expected to survive in each population?",
          ch(f"About {int(surv)} in the diverse population and none in the identical population, because only the diverse population contains the resistance allele.", f"{N:,} x {frac} = {int(surv)} plants have the allele, and the identical plants all lack it.", int(surv)),
          [ch(f"About {int(surv)} in each population, because the same number of plants are exposed to the disease in each of the two populations.", "The identical population does not contain the allele, so no plant in it survives.", int(surv) + 1),
           ch(f"About {int(N * (1 - frac)):,} in the diverse population and none in the identical population, because most plants lack the allele.", f"Only the plants with the allele survive, and that is {int(frac * 100)}% of the plants.", int(N * (1 - frac))),
           ch(f"None in either population, because a disease that kills all of the plants without the allele will also kill the plants with it.", "The plants with the resistance allele are not killed by the disease.", 0)],
          "Diversity can preserve alleles that allow some individuals to survive.", difficulty="hard")

    B.mcq(T, "A small population of an endangered species has very low genetic diversity. Conservation biologists move a few individuals from another population into it. Which statement best explains the likely benefit?",
          ch("The new individuals add alleles to the population, which increases its diversity and its ability to respond to environmental changes.", "Gene flow adds alleles and increases genetic diversity."),
          [ch("The new individuals remove the alleles that the population already has, so that the whole population is made of the best alleles.", "Moving individuals in adds alleles. It does not remove the existing ones."),
           ch("The new individuals increase the mutation rate of the population, so that the population can change quickly in response to a new threat.", "Adding individuals does not raise the mutation rate."),
           ch("The new individuals reduce the genetic diversity of the population, which reduces the chance that all of the individuals are lost.", "Reduced diversity increases the risk of loss.")],
          "Gene flow can increase genetic diversity and resilience.", difficulty="medium")

    # ------------------------------------------------------------------ 7.12 Origins of life on Earth
    T = 12
    B.mcq(T, "Earth formed about 4.6 billion years ago (bya), the environment was too hostile for life until about 3.9 bya, and the earliest fossil evidence of life is 3.5 billion years old. Which statement is best supported by this evidence?",
          ch("Life probably originated between about 3.9 and 3.5 bya, because it could not exist before the environment cooled and it had left fossils by 3.5 bya.", "Together, the evidence gives a plausible range of dates for the origin of life."),
          [ch("Life originated at the same time as Earth, about 4.6 bya, because life must have been present when the planet was formed.", "The environment was too hostile for life until about 3.9 bya."),
           ch("Life originated about 1 billion years ago, because the oldest fossils must be younger than the age of the oldest rocks.", "The earliest fossil is 3.5 billion years old, which is much older than 1 billion years."),
           ch("Life cannot have originated on Earth, because the environment was hostile for the first 700 million years of its existence.", "The environment became suitable after about 3.9 bya.")],
          "Geological evidence gives a plausible range of dates for the origin of life.", difficulty="easy")

    hostile, fossil = 3.9, 3.5
    gap = round((hostile - fossil) * 1000)
    assert gap == 400
    B.mcq(T, f"The environment of Earth was too hostile for life until about {hostile} bya, and the earliest fossil evidence of life is {fossil} billion years old. What is the longest possible time, in years, between the end of the hostile period and the earliest fossils?",
          ch(f"About {gap} million years, because {hostile} - {fossil} = 0.4 billion years.", f"({hostile} - {fossil}) billion years = {gap} million years.", gap),
          [ch(f"About {int(round((4.6 - hostile) * 1000)):,} million years, because that is the time from the formation of Earth to the end of the hostile period.", "This is the length of the hostile period. The question asks about the time after it.", int(round((4.6 - hostile) * 1000))),
           ch(f"About {int(round(fossil * 1000)):,} million years, because the earliest fossils are {fossil} billion years old and so that is the time.", "3.5 billion years is the age of the fossils and not the time between the two events.", int(round(fossil * 1000))),
           ch(f"About {int(round((hostile + fossil) * 1000)):,} million years, because the two dates are added to find the total time for life to arise.", "The time between two dates is found by subtracting one from the other.", int(round((hostile + fossil) * 1000)))],
          "The time between two dates is the difference between them.", difficulty="medium")

    B.mcq(T, "Which statement describes the RNA world hypothesis?",
          ch("RNA could have been the earliest genetic material, and it may have been able to replicate and to catalyze reactions before DNA and proteins were present.", "The RNA world hypothesis proposes that RNA could have been the earliest genetic material."),
          [ch("DNA was the earliest genetic material, and RNA appeared later as a copy of the DNA that was used to make the first proteins.", "The hypothesis proposes that RNA came first."),
           ch("Proteins were the earliest genetic material, and they stored the information that was later copied into RNA and then into DNA.", "Proteins do not store hereditary information that can be copied by base pairing."),
           ch("RNA was produced by the first cells from DNA, and the cells then used the RNA to build the other molecules that they needed.", "The hypothesis describes a time before cells, in which RNA was the genetic material.")],
          "The RNA world hypothesis proposes that RNA was the earliest genetic material.", difficulty="medium")

    B.mcq(T, "Which of the following is an assumption of the RNA world hypothesis?",
          ch("At some time genetic continuity was assured by the replication of RNA, and base pairing was necessary for that replication.", "The hypothesis assumes that RNA replication assured genetic continuity and that base pairing is necessary for replication."),
          [ch("Genetically encoded proteins were the catalysts of the first reactions, and they were needed to copy the first genetic molecules.", "The hypothesis assumes that genetically encoded proteins were not involved as catalysts."),
           ch("DNA was present at the start and carried the information that was used to make the first RNA molecules of the first cells.", "The hypothesis considers a time before DNA was the genetic material."),
           ch("Replication of the genetic material did not need the pairing of bases, because it was done by the random joining of nucleotides.", "Base pairing is assumed to be necessary for replication.")],
          "Assumptions: RNA replication, base pairing, and no genetically encoded protein catalysts.", difficulty="medium")

    B.mcq(T, "A scientist wants to test a prediction of the RNA world hypothesis in the laboratory. Which result would best support the hypothesis?",
          ch("A short RNA molecule is found that can catalyze the joining of nucleotides to copy other RNA molecules, in the absence of any protein.", "If RNA can catalyze its own replication without protein, then genetically encoded proteins were not needed as catalysts."),
          [ch("A short DNA molecule is found that can catalyze the joining of amino acids into proteins, in the absence of any RNA.", "This would not show that RNA alone can replicate."),
           ch("A protein is found that can catalyze the joining of nucleotides to copy RNA molecules, but only when there is DNA present.", "The hypothesis assumes that proteins were not involved as catalysts."),
           ch("A short RNA molecule is found that cannot be copied or change in any way, and that stays unchanged for many years.", "An RNA that cannot replicate does not support the hypothesis.")],
          "Evidence that RNA can catalyze and replicate supports the RNA world hypothesis.", difficulty="hard")

    B.mcq(T, "Fossils of ancient mats of microorganisms that are 3.5 billion years old were found in rocks. What does this observation indicate about when life originated?",
          ch("Life originated no later than about 3.5 bya, because organisms were already present and left fossil evidence by that time.", "The earliest fossil evidence sets the latest date for the origin of life."),
          [ch("Life originated exactly 3.5 bya, because the age of the oldest fossils found is always the age at which life began.", "Life could have begun earlier than the oldest known fossils."),
           ch("Life originated after 3.5 bya, because fossils are found only in the rocks that are younger than the time of the origin of life.", "A fossil that is 3.5 billion years old shows that life already existed then."),
           ch("Life did not originate on Earth at all, because organisms that are as old as 3.5 billion years could not have left fossils.", "Fossils from 3.5 bya are evidence that life existed on Earth by then.")],
          "The earliest fossils give an upper limit for the date of the origin of life.", difficulty="medium")

    earth, fossil = 4.6, 3.5
    pct = (earth - fossil) / earth * 100
    assert round(pct) == 24
    B.mcq(T, f"Earth formed about {earth} bya, and the earliest fossil evidence of life is {fossil} billion years old. About what percent of the history of Earth had passed before the time of the earliest fossils?",
          ch(f"About {pct:.0f}%, because {earth} - {fossil} = {earth - fossil:.1f} billion years, and {earth - fossil:.1f} / {earth} is about 0.24.", f"({earth} - {fossil}) / {earth} x 100 = {pct:.1f}%.", round(pct)),
          [ch(f"About {fossil / earth * 100:.0f}%, because {fossil} / {earth} is the fraction of the history of Earth that had passed.", "3.5 / 4.6 is the fraction of the history that came after the earliest fossils were formed.", round(fossil / earth * 100)),
           ch(f"About {(earth - fossil) * 100:.0f}%, because the difference of {earth - fossil:.1f} billion years is multiplied by 100.", "The difference must be divided by the age of Earth to give a fraction.", round((earth - fossil) * 100)),
           ch(f"About {fossil / (earth - fossil) * 100:.0f}%, because the age of the fossils is divided by the time before they formed.", "That ratio is not a percent of the history of Earth.", round(fossil / (earth - fossil) * 100))],
          "Percent = part / whole x 100.", difficulty="hard")
