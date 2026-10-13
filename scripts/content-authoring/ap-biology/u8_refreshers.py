"""Writes content/ap-biology/refreshers/unit-8.json (seven refreshers, one per topic). Layout: ### The idea, ### Key facts, ### Watch out for, ### Worked example.
Facts are the CED's required content for each topic; every number in a worked example is asserted. Avoid a lone dollar sign, single-asterisk italics and
em dashes. Edit this script, not the JSON. Run: python3 u8_refreshers.py"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import refreshers_lib

# worked-example numbers
n, exp = 60, 30
assert round(2 * (41 - exp) ** 2 / exp, 2) == 8.07
assert 10000 * 0.1 * 0.1 == 100.0
assert 120 - 80 == 40 and round((60 - 20) / 500, 2) == 0.08
assert 100 * 2 ** 6 == 6400
assert 0.4 * 500 * (1000 - 500) / 1000 == 100
assert round(1 - (0.2 ** 2) * 5, 2) == 0.80 and round(1 - (0.8 ** 2 + 4 * 0.05 ** 2), 2) == 0.35
assert round((8 - 15) / 15 * 100, 1) == -46.7
assert 25 / 0.04 == 625

ENTRIES = [
("responses-to-the-environment", r"""
### The idea
Organisms detect changes in their surroundings and in their own bodies, and they respond. Responses and signals that improve survival and reproduction are favored by natural selection.

### Key facts
- Organisms respond to the environment through **behavioral and physiological mechanisms** (a plant bending toward light, a plant closing its leaf openings in a drought, an animal moving to a moist place). You do not have to know the specific mechanisms.
- Organisms **exchange information** with signals that can be visual, audible, tactile, electrical or chemical. Animals use signals to show dominance, to find food, to claim territory and to find mates.
- **Fitness favors** innate and learned behaviors that increase survival and reproductive success. **Cooperative behavior** tends to raise the fitness of the individual and the survival of the population.
- In a **choice chamber** experiment, the independent variable is the condition (for example light or dark), the dependent variable is where the organisms are, and the control keeps the two sides the same.

### Watch out for
Saying that animals change their behavior "in order to" evolve. Individuals respond, and populations change by selection. Also, a response does not need every organism to move, so compare the counts with the numbers that you would expect by chance.

### Worked example
Prompt: "60 woodlice are in a chamber with a dark half and a light half, and 41 are on the dark half. Is this different from chance?"

The expected number on each half is 30. Chi-square = (41 - 30)^2 / 30 + (19 - 30)^2 / 30 = 4.03 + 4.03 = 8.07, which is greater than the critical value of 3.84 (1 degree of freedom, p = 0.05), so the null hypothesis of no preference is rejected.
"""),
("energy-flow-through-ecosystems", r"""
### The idea
Energy flows through an ecosystem in one direction, from the sun or from inorganic molecules to autotrophs, then to heterotrophs, and it is lost as heat. Matter does not flow away. It cycles between organisms and the environment.

### Key facts
- **Endotherms** use heat from their metabolism to keep a steady body temperature. **Ectotherms** rely on behavior, such as moving into sun or shade. A **net gain** of energy lets an organism store energy, grow and reproduce more, and a **net loss** leads to a loss of mass and eventually death.
- **Levels of organization:** population, community, ecosystem, biome.
- **Cycles:** the **water** cycle (evaporation, condensation, precipitation, transpiration), the **carbon** cycle (photosynthesis, cellular respiration, decomposition, combustion), the **nitrogen** cycle (fixation, assimilation, ammonification, nitrification, denitrification, performed by microorganisms in the soil) and the **phosphorus** cycle (weathering of rocks releases phosphate, producers take it up, decomposition returns it).
- **Autotrophs** capture energy from sunlight (photosynthesis) or from inorganic molecules (chemosynthesis, possible without oxygen). **Heterotrophs** metabolize carbohydrates, lipids and proteins from the organisms that they eat.
- Less energy reaches each higher **trophic level**, so a change in producers changes the number and size of the other levels.

### Watch out for
Saying that energy cycles. Energy is not recycled. It is lost as heat at each transfer, and the sun must supply it again. Also, nitrogen gas is the largest reservoir of nitrogen, but most organisms cannot use it until it is fixed.

### Worked example
Prompt: "Producers capture 10,000 kJ, and 10% of the energy passes to the next trophic level at each transfer. How much reaches the secondary consumers?"

There are two transfers: 10,000 x 0.10 = 1,000 kJ for the primary consumers, and 1,000 x 0.10 = 100 kJ for the secondary consumers.
"""),
("population-ecology", r"""
### The idea
A population is a group of individuals of one species that interact with each other and with the environment. Its size changes with births and deaths, and with no limits it grows exponentially.

### Key facts
- **Population growth:** $\frac{dN}{dt} = B - D$, where B is the birth rate, D is the death rate and N is the population size.
- **Exponential growth** (reproduction without constraints): $\frac{dN}{dt} = r_{max} N$, where $r_{max}$ is the maximum per capita growth rate. The curve is J-shaped, and the population doubles at regular intervals.
- The **per capita growth rate** is (B - D) / N.
- Many adaptations help organisms to obtain and use energy and matter in a particular environment (deep roots, water storage in desert plants).
- A **rate** from a graph is the change in N divided by the change in time.

### Watch out for
Dividing by the wrong number. A per capita rate is divided by the population size, and an average rate is divided by the time. Also, exponential growth cannot go on for ever, because resources are limited.

### Worked example
Prompt: "A culture starts with 100 bacteria that double every 20 minutes. How many are there after 2 hours?"

2 hours is 120 minutes, which is 6 doublings: 100 x 2^6 = 100 x 64 = 6,400 bacteria.
"""),
("effect-of-density-on-populations", r"""
### The idea
No population can grow without limit. As it gets denser, resources get scarcer, and the growth slows and levels off near the number that the environment can support.

### Key facts
- **Carrying capacity (K)** is the sustainable abundance of a species that the available resources can support.
- **Density-dependent** factors (competition for food, disease, wastes) become stronger as the population gets denser. **Density-independent** factors (a fire, a storm, a drought) act whatever the density.
- With these limits, **logistic growth** typically results, with an S-shaped curve: $\frac{dN}{dt} = r_{max} N \frac{K - N}{K}$.
- The growth rate is **highest at K / 2** and is zero at K. If resources fall, K falls and the population declines.

### Watch out for
Treating K as a fixed number for a species. It depends on the resources of an ecosystem at that time. Also, the term (K - N) / K is less than 1, so it reduces the exponential rate.

### Worked example
Prompt: "r max is 0.4 per year, K is 1,000 and N is 500. What is dN/dt?"

$\frac{dN}{dt} = 0.4 \times 500 \times \frac{1000 - 500}{1000} = 0.4 \times 500 \times 0.5 = 100$ individuals per year. (N is K / 2, where the growth rate is highest.)
"""),
("community-ecology", r"""
### The idea
A community is a group of interacting populations of different species. Its structure depends on which species are present and how evenly the individuals are spread among them, and it changes over time as the populations interact.

### Key facts
- **Community structure** is described by **species composition** and **species diversity.**
- **Simpson's diversity index** = 1 - sum of $(n/N)^2$, where n is the number of individuals of one species and N is the total number. A higher value means more diversity, and a community dominated by one species has a low value.
- **Interactions:** predation, competition (-/-), parasitism (+/-), mutualism (+/+) and commensalism (+/0). They can be modeled, as in predator-prey cycles, **trophic cascades** and **niche partitioning.**
- **Error bars** (for example, one standard error) can be used to estimate whether means differ: error bars that do not overlap suggest that the means are different, but overlapping error bars do not show a difference.

### Watch out for
Subtracting the wrong way in the diversity index. You find the sum of the squares and then take it away from 1. Also, "no overlap" is evidence of a difference, and "overlap" means that you cannot say that there is one.

### Worked example
Prompt: "Community 1 has 5 species with 20 individuals each. Community 2 has 80, 5, 5, 5 and 5. Which has the higher index?"

Community 1: 1 - 5 x (0.20)^2 = 1 - 0.20 = 0.80. Community 2: 1 - (0.80^2 + 4 x 0.05^2) = 1 - 0.65 = 0.35. Community 1 is more diverse, because its individuals are evenly spread.
"""),
("biodiversity", r"""
### The idea
The more species and the more variety an ecosystem has, the better it can absorb a disturbance. Some species have an effect that is much larger than their numbers would suggest.

### Key facts
- Natural and artificial ecosystems with **fewer parts and little diversity** are often **less resilient** to changes in the environment.
- **Keystone species,** producers and essential abiotic and biotic factors help to maintain the diversity of an ecosystem.
- The effects of a **keystone species** are **disproportionate** to its abundance, and when it is removed the ecosystem often collapses (sea otters, urchins and kelp).
- The addition or removal of any component changes the structure of an ecosystem in the short term and in the long term.

### Watch out for
Assuming that the most abundant species is the most important. A keystone species can be rare. Also, calculate a percent change relative to the starting (control) value.

### Worked example
Prompt: "Control plots have 15 species, and plots without a predator have 8. What is the percent change?"

(8 - 15) / 15 x 100 = -46.7%, a decrease of about 47%. The loss is large, which suggests that the predator is a keystone species.
"""),
("disruptions-in-ecosystems", r"""
### The idea
Ecosystems change when a variation is selected, when a new species arrives, when people alter the environment, and when geological or weather events change a habitat.

### Key facts
- An **adaptation** is a genetic variation that is favored by selection and that gives an advantage in a particular environment. **Mutations are not directed** by environmental pressures.
- **Heterozygote advantage:** the heterozygous genotype has a higher relative fitness than either homozygous genotype (the sickle cell allele in places with malaria), which keeps both alleles in the population.
- An **invasive species** may exploit a new niche that is free of predators and competitors, or outcompete native species.
- Human activities speed up change: **biomagnification** (a toxin becomes more concentrated at higher trophic levels) and **eutrophication** (nutrient runoff causes an algal bloom, then decomposition uses up the oxygen).
- **Geological and meteorological events** change habitats and where ecosystems are found, and biogeography shows this.

### Watch out for
Saying that a pollutant "causes" an adaptation. It selects among existing variation. Also, to compare concentrations in a food chain, divide one by the other.

### Worked example
Prompt: "A pesticide is 0.04 ppm in plankton and 25 ppm in a fish-eating bird. How many times higher is it in the bird?"

25 / 0.04 = 625 times higher, which is biomagnification up the food chain.
"""),
]

refreshers_lib.write("ap-biology", 8, ENTRIES)
