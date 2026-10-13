"""Writes content/ap-biology/refreshers/unit-7.json (twelve refreshers, one per topic). Layout: ### The idea, ### Key facts, ### Watch out for, ### Worked example.
Facts are the CED's required content for each topic; every number in a worked example is asserted. Avoid a lone dollar sign, single-asterisk italics and
em dashes. Edit this script, not the JSON. Run: python3 u7_refreshers.py"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import refreshers_lib

# worked-example numbers
assert (40 * 3.0, 60 * 2.0) == (120.0, 120.0) and 120 / 40 == 3.0 and 120 / 60 == 2.0  # offspring per adult: 3.0 against 2.0
assert round(80 / (80 + 450) * 100, 1) == 15.1  # 1,000 insects, 10% with the trait, survival 80% against 50%
assert (32.0 - 18.0) / 4 == 3.5
assert round((200 * 0.5 + 50 * 0.1) / 250, 2) == 0.42
p = 0.7
assert (round(p * p, 2), round(2 * p * 0.3, 2), round(0.3 * 0.3, 2)) == (0.49, 0.42, 0.09)
assert 0.5 ** 2 == 0.25 and 2 * 5730 == 11460
assert 30 / (12 / 24) == 60
assert round((4.6 - 3.9) , 1) == 0.7 and round((3.9 - 3.5) * 1000) == 400
assert round(0.02 * 0.02 , 4) == 0.0004
q = (1 / 2500) ** 0.5
assert round(q, 2) == 0.02 and round(2 * (1 - q) * q, 3) == 0.039

ENTRIES = [
("introduction-to-natural-selection", r"""
### The idea
Natural selection is a major mechanism of evolution. Organisms produce more offspring than the environment can support, so individuals compete for limited resources, and the ones with more favorable traits tend to leave more offspring.

### Key facts
- **Differential survival:** competition for limited resources means that individuals with more favorable phenotypes are more likely to survive and produce more offspring, passing on those traits.
- **Fitness is reproductive success,** meaning how many offspring an individual leaves that survive to reproduce, and not strength or length of life.
- **Environments fluctuate.** Biotic factors (predators, parasites, competitors) and abiotic factors (temperature, rainfall) change the rate and direction of evolution, and different variations can be selected in each generation.
- Selection needs **heritable variation** that affects survival or reproduction.

### Watch out for
The idea that individuals change to meet their needs. Traits acquired during a life are not inherited, and the environment selects among variation that already exists. Also, fitness is about offspring, not about living the longest.

### Worked example
Prompt: "40 green beetles produce 120 offspring, and 60 brown beetles produce 120 offspring. Which color has the higher fitness?"

Offspring per adult: green 120 / 40 = 3.0 and brown 120 / 60 = 2.0. Green beetles have the higher fitness, because they have more offspring each, even though the totals are equal.
"""),
("natural-selection", r"""
### The idea
Natural selection acts on the phenotypes of individuals. Whether a phenotype helps or hurts depends on the environment, so a change in the environment applies a new selective pressure to the population.

### Key facts
- Natural selection acts on **phenotypic variation** in populations.
- **Environments change** and apply selective pressures. A phenotype can increase fitness in one environment and decrease it in another (thick fur in the cold and in the heat, for example).
- **Variation in molecules** (the number and types of enzymes, pigments or other molecules in cells) can give a population a greater ability to survive and reproduce in different environments.
- Selection against extreme phenotypes reduces variation, and selection that favors one extreme shifts the mean of the population.

### Watch out for
Reading a graph of a trait over generations as proof that individuals changed. The population changed because individuals with some phenotypes left more offspring. Also, selection is not "survival of the strongest." A phenotype is favored if it helps in that environment.

### Worked example
Prompt: "A population has 1,000 insects, and 10% have a heritable trait. 80% of the insects with the trait survive, and 50% of the others survive. What percent of the survivors have the trait?"

With the trait: 100 x 0.80 = 80 survive. Without it: 900 x 0.50 = 450 survive. The survivors number 530, and 80 / 530 = 15.1% have the trait, an increase from 10%.
"""),
("artificial-selection", r"""
### The idea
In artificial selection, humans decide which individuals of a species breed. The method is the same as in natural selection, in that the traits of the next generation depend on the parents, but the selecting agent is human choice.

### Key facts
- Through artificial selection, humans affect the **variation** in other species (crops, farm animals, pets).
- Wild mustard gave rise to cabbage, kale, broccoli and cauliflower by selection for different parts of the plant.
- It needs **heritable variation** in the trait. A **control** (parents chosen at random) shows that the change came from selection.
- Selecting for a few traits can **reduce genetic diversity,** which makes a crop or breed more at risk from a disease or a change in conditions.

### Watch out for
Saying that artificial selection creates new alleles. It chooses among variation that already exists (new alleles come from mutation). Also, calculate a rate of change using the number of generations of selection, not the number of rows in a table.

### Worked example
Prompt: "The mean number of bristles is 18.0 in generation 0 and 32.0 in generation 4. What is the mean change per generation?"

The change is 32.0 - 18.0 = 14.0 bristles over 4 generations, so the rate is 14.0 / 4 = 3.5 bristles per generation.
"""),
("population-genetics", r"""
### The idea
Evolution is driven by random events as well as by selection. Mutation, genetic drift and gene flow change the genetic makeup of a population, and a change in allele frequencies over time is evidence that evolution has occurred.

### Key facts
- **Mutation** is random and adds new variation, on which selection can act.
- **Genetic drift** is a change in allele frequencies from a nonselective process (chance), and it matters most in **small** populations.
- The **bottleneck effect** is drift after a population is reduced to a few individuals. The **founder effect** is drift when a small group separates and starts a new population.
- **Migration** can cause **gene flow** (alleles added or removed). Gene flow between populations prevents them from diverging into separate species, and drift can let a small population diverge.

### Watch out for
Treating drift as selection. Drift is random and has nothing to do with fitness. Also, when migrants join a population, weight the allele frequencies by the numbers of individuals, and do not average the two frequencies.

### Worked example
Prompt: "200 animals have a frequency of 0.50 for an allele, and 50 migrants with a frequency of 0.10 join them. What is the new frequency?"

The allele frequency is weighted by the numbers: (200 x 0.50 + 50 x 0.10) / 250 = (100 + 5) / 250 = 0.42.
"""),
("hardy-weinberg-equilibrium", r"""
### The idea
The Hardy-Weinberg model describes the allele and genotype frequencies of a population that is not evolving. Because real populations always break at least one of its conditions, it is used as a null hypothesis.

### Key facts
- **Conditions:** a large population, no migration, no new mutations, random mating, and no natural selection.
- **Equations:** $p + q = 1$ for the alleles, and $p^2 + 2pq + q^2 = 1$ for the genotypes. $p^2$ and $q^2$ are the homozygotes, and $2pq$ is the heterozygotes.
- You can find allele frequencies from genotype counts: allele copies divided by twice the number of individuals.
- Start with **$q^2$** (the recessive phenotype), take the square root to get $q$, and then find $p = 1 - q$.
- Observed frequencies that differ from the expected ones suggest that a condition is not met.

### Watch out for
Using $q^2$ as if it were $q$. The frequency of the recessive phenotype is $q^2$. Also, carriers are $2pq$, which is much more common than affected people when the allele is rare.

### Worked example
Prompt: "1 in 2,500 people has a recessive disorder. What fraction are carriers?"

$q^2 = 1 / 2{,}500 = 0.0004$, so $q = 0.02$ and $p = 0.98$. Carriers are $2pq = 2 \times 0.98 \times 0.02 = 0.039$, or about 1 in 26.
"""),
("evidence-of-evolution", r"""
### The idea
Evolution is supported by many independent kinds of evidence. When fossils, anatomy and molecules all give the same picture, the evidence for descent with change is strong.

### Key facts
- **Kinds of data:** geographical, geological, physical, biochemical and mathematical.
- **Fossils** are dated by the age of the rock layers, by the decay of isotopes such as carbon-14, and by geographical data.
- **Morphological homologies,** including vestigial structures, show common ancestry.
- **DNA and protein sequences** can be compared. Fewer differences suggest a more recent common ancestor, and differences that build up at a steady rate act as a molecular clock.
- Molecular data are typically more reliable than morphology.

### Watch out for
Treating any similarity as evidence of common ancestry. Similar traits can evolve separately under similar pressures. Also, after n half-lives, (1/2) to the power n of the isotope remains.

### Worked example
Prompt: "Carbon-14 has a half-life of 5,730 years. A wooden tool has 25% of the carbon-14 of a living tree. How old is it?"

25% is 1/2 x 1/2, which is two half-lives, so the tool is 2 x 5,730 = 11,460 years old.
"""),
("common-ancestry", r"""
### The idea
All eukaryotes share structural and functional features that would be unlikely to evolve again and again. They point to a single common ancestor of the eukaryotes.

### Key facts
- **Membrane-bound organelles** such as the nucleus and the mitochondria.
- **Linear chromosomes** that are condensed with proteins.
- **Genes that contain introns.**
- Prokaryotes typically have a circular chromosome, no membrane-bound organelles, and no introns in their genes.
- Shared features are expected if lineages came from a common ancestor, and a feature found in only one lineage is not evidence of common ancestry.

### Watch out for
Listing features that only some eukaryotes have, such as chloroplasts and cell walls. Only features present in all eukaryotes support the claim that they share an ancestor.

### Worked example
Prompt: "A new single-celled organism has a nucleus, linear chromosomes and genes with introns. What do you predict?"

These are features of eukaryotes, so it is a eukaryote and probably shares a common ancestor with plants, fungi and animals.
"""),
("continuing-evolution", r"""
### The idea
Evolution has not stopped. Populations alive today are still changing, and we can see it happen in organisms that reproduce quickly or that are under strong selection.

### Key facts
- **Examples:** genomic changes over time, continuous change in the fossil record, resistance to antibiotics, pesticides, herbicides or chemotherapy drugs, and pathogens that evolve and cause emergent diseases.
- Resistance evolves by selection: a few individuals already have a **random mutation** for resistance, they survive the treatment, and they reproduce.
- The drug or poison does not cause the mutation. It acts as the selective pressure.
- A good test of the hypothesis that resistance preexisted is to expose a **population that has never met the agent** and see whether some survive.

### Watch out for
Saying that the bacteria "learn" or "adapt on purpose." Individuals do not change to resist, and the percent of resistant individuals grows because the others die. Also, a graph that shows resistance rising with use shows a correlation that fits selection, and not proof of cause by itself.

### Worked example
Prompt: "A tumor shrinks with a drug, and then regrows and no longer responds. Why?"

A few tumor cells already had mutations that made them resistant. They survived the drug and divided, so the regrown tumor is made mostly of resistant cells.
"""),
("phylogeny", r"""
### The idea
Phylogenetic trees and cladograms are diagrams of hypothesized evolutionary relationships. You read them by following the branches to the nodes where lineages split from a common ancestor.

### Key facts
- A **node** is the **most recent common ancestor** of the lineages that branch from it.
- The **outgroup** is the lineage that is least closely related to the others.
- **Shared derived characters** (traits gained in a lineage) are informative about grouping. A trait shared by all of the lineages being compared is not.
- A **phylogenetic tree** can show time or the amount of change (calibrated by fossils or a molecular clock). A **cladogram** shows only the branching pattern.
- Trees can be built from morphology or from DNA and protein sequences. **Molecular data** are typically more reliable. Trees are **hypotheses** that are revised with new evidence.

### Watch out for
Reading a tree as a ladder in which one living species is "more advanced." Every tip is a living lineage. Also, closeness of the tips on the page does not mean close relationship. Count the nodes back to the common ancestor.

### Worked example
Prompt: "In a cladogram, mouse and human share the trait hair, and the lizard branches off earlier. Which two are more closely related?"

The mouse and the human share a more recent common ancestor (the node where hair was gained) than either shares with the lizard, so they are more closely related to each other.
"""),
("speciation", r"""
### The idea
A new species arises when two populations become reproductively isolated, so that they stop exchanging genes and diverge. How fast and where this happens depends on the ecological conditions.

### Key facts
- **Biological species concept:** a group that can interbreed and exchange genes to produce **viable, fertile** offspring.
- **Allopatric** speciation: the populations are geographically isolated. **Sympatric** speciation: the populations overlap geographically.
- **Pre-zygotic** mechanisms prevent the formation of a zygote (different mating times, songs or habitats). **Post-zygotic** mechanisms act after it (hybrids that do not survive or are sterile).
- **Punctuated equilibrium:** rapid change after a long stasis. **Gradualism:** slow change over a long time.
- **Divergent evolution** and **adaptive radiation** (rapid speciation when new habitats open) give many species from one ancestor. **Convergent evolution** gives similar traits in unrelated lineages under similar pressures.

### Watch out for
Mixing up the two zygote terms. If no zygote forms, the barrier is pre-zygotic. Also, a mule is evidence that a horse and a donkey are separate species, because the offspring are sterile.

### Worked example
Prompt: "A river splits a population of mice. After many generations the two groups can no longer produce fertile offspring. What type of speciation?"

The groups were geographically separated, so it is allopatric speciation. They are now reproductively isolated, so they are separate species.
"""),
("variations-in-populations", r"""
### The idea
The more genetic variation a population has, the better its chances when conditions change. A population with little diversity can be wiped out by a single new threat.

### Key facts
- **Genetic diversity** affects how a population responds to changes in the environment. Species and populations with little diversity are at risk of decline or extinction.
- A diverse population is more **resilient** because it is more likely to contain individuals that can withstand the pressure (a disease outbreak, for example).
- An allele that is **adaptive** in one environment may be **deleterious** in another, because the selective pressures differ.
- Conservation can add alleles by **gene flow,** by moving individuals between populations.

### Watch out for
Saying that individuals in a diverse population adapt to the threat. The resistant alleles must already be in the population, because mutations are random. Also, diversity refers to the variety of alleles, and not to the number of individuals.

### Worked example
Prompt: "A disease kills all plants without a resistance allele. 1% of 50,000 diverse plants have it, and none of the 50,000 identical plants do. How many survive?"

In the diverse population 50,000 x 0.01 = 500 plants survive. In the identical population no plant has the allele, so none survive.
"""),
("origins-of-life-on-earth", r"""
### The idea
Geological evidence gives a window of time for the origin of life, and the RNA world hypothesis is a model of what the first genetic material may have been.

### Key facts
- **Dates:** Earth formed about 4.6 billion years ago (bya). The environment was too hostile for life until about 3.9 bya. The earliest fossil evidence of life dates to 3.5 bya. Together these give a plausible range for the origin of life.
- The **RNA world hypothesis** proposes that RNA could have been the earliest genetic material.
- Its three assumptions: genetic continuity was assured by **RNA replication,** **base pairing** is necessary for replication, and genetically encoded **proteins were not involved as catalysts.**
- Evidence that RNA can catalyze reactions and copy itself without proteins supports the hypothesis.

### Watch out for
Taking the age of the oldest fossil as the date at which life began. It is the latest date by which life existed, and life could have begun earlier. Also, subtract dates to find an interval, and do not add them.

### Worked example
Prompt: "The environment became suitable at 3.9 bya, and the earliest fossils are 3.5 billion years old. What is the longest time between the two?"

3.9 - 3.5 = 0.4 billion years, which is 400 million years.
"""),
]

refreshers_lib.write("ap-biology", 7, ENTRIES)
