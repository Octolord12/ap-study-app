"""Unit 8, topics 8.5 Community Ecology (10 questions), 8.6 Biodiversity (7) and 8.7 Disruptions in Ecosystems (9).

Required content (CED 2025-26): 8.5.A community structure is measured by species composition and diversity (Simpson's index = 1 - sum of (n/N) squared); 8.5.B communities are interacting populations that change over
time; interactions (predator/prey, cooperation, trophic cascades, niche partitioning, competition, predation, parasitism, mutualism, commensalism) have positive and negative effects and drive population dynamics.
8.6.A ecosystems with fewer, less diverse parts are often less resilient; keystone species, producers and essential abiotic and biotic factors maintain diversity; 8.6.B keystone species have disproportionate effects
and the ecosystem often collapses without them. 8.7.A an adaptation is a genetic variation favored by selection; heterozygote advantage; mutations are not directed by environmental pressures; 8.7.B invasive species
exploit a new niche or outcompete natives; 8.7.C human activity accelerates change (biomagnification, eutrophication); 8.7.D geological and meteorological events change habitats and distributions (biogeography).
Suggested skills: 5.B (confidence intervals and error bars), 5.D, 6.E.
"""
from lib import *


def simpson(counts):
    n = sum(counts)
    return 1 - sum((c / n) ** 2 for c in counts)


def build(B):
    # ------------------------------------------------------------------ 8.5 Community ecology
    T = 5
    B.mcq(T, "How is the structure of a community measured and described?",
          ch("By its species composition, which is the species that are present, and by its species diversity", "The structure of a community is measured and described in terms of species composition and species diversity."),
          [ch("By the number of individuals of the most common species only, and by the total mass of the nonliving matter in the area", "Community structure includes all of the species and their diversity."),
           ch("By the genetic variation within one species, and by the number of chromosomes in the cells of the members of the species", "That describes a population and not a community."),
           ch("By the amount of sunlight that reaches the area, and by the temperature and the rainfall that are recorded each year", "Those are abiotic factors of the environment and not the structure of the community.")],
          "Community structure: species composition and species diversity.", difficulty="easy")

    c1 = [20, 20, 20, 20, 20]
    c2 = [80, 5, 5, 5, 5]
    d1, d2 = simpson(c1), simpson(c2)
    s2 = 1 - d2
    assert (round(d1, 2), round(d2, 2), round(s2, 2)) == (0.80, 0.35, 0.65)
    rows = [("Species 1", "20", "80"), ("Species 2", "20", "5"), ("Species 3", "20", "5"), ("Species 4", "20", "5"), ("Species 5", "20", "5"), ("Total", "100", "100")]
    B.mcq(T, "The table shows the number of individuals of five species in two communities. Simpson's diversity index is 1 minus the sum of (n / N) squared for each species. What is the value of the index for community 2, and which community is more diverse?",
          ch(f"{d2:.2f}, and community 1 is more diverse, because its individuals are spread evenly among the species and its index is {d1:.2f}.", f"For community 2, the sum of (n / N) squared is {s2:.2f}, so the index is 1 - {s2:.2f} = {d2:.2f}. Community 1 has a higher index ({d1:.2f}).", round(d2, 2)),
          [ch(f"{s2:.2f}, and community 2 is more diverse, because the sum of the squares is greater than the sum of the squares for community 1.", "The sum of the squares must be subtracted from 1 to find the index, and community 1 has the higher index.", round(s2, 2)),
           ch(f"{d1:.2f}, and community 2 is more diverse, because it has one species with a very large number of individuals.", "0.80 is the index of community 1, and a community dominated by one species has a lower index.", round(d1, 2)),
           ch(f"{d2:.2f}, and community 2 is more diverse, because both communities have the same total number of individuals.", "The same number of species and individuals does not make the diversity equal. Evenness matters too.", 0.351)],
          "Simpson's diversity index = 1 - sum of (n / N) squared; a higher value means more diversity.",
          diagram=table(["Species", "Community 1: individuals", "Community 2: individuals"], rows, caption="Individuals of five species in two communities", row_headers=True), difficulty="hard")

    B.mcq(T, "An orchid grows on the branch of a tree. The orchid receives more light than it would on the ground, and the tree is not helped or harmed. Which term describes the interaction?",
          ch("Commensalism, because one species benefits and the other species is not affected.", "Commensalism is a relationship in which one species benefits and the other is neither helped nor harmed."),
          [ch("Mutualism, because both of the species receive a benefit from living together in the same place in the forest.", "The tree receives no benefit."),
           ch("Parasitism, because one species benefits and the other species is harmed by the relationship between them.", "The tree is not harmed."),
           ch("Competition, because both of the species are harmed by the use of the same resources in the same part of the forest.", "Neither species is harmed.")],
          "Commensalism: one species benefits and the other is not affected.", difficulty="medium")

    years = [0, 2, 4, 6, 8, 10, 12, 14]
    hare = [20, 45, 60, 35, 15, 30, 55, 40]
    lynx = [5, 8, 14, 22, 12, 7, 14, 24]
    g = graph("Time (years)", "Number of animals (in thousands)", 0, 14, 0, 70,
              [line("Prey (hares)", list(zip(years, hare)), "green"), line("Predator (lynx)", list(zip(years, lynx)), "red")],
              "Numbers of hares and lynx over 14 years. The hares peak at 60 at year 4, and the lynx peak at 22 at year 6. The hares peak again at 55 at year 12, and the lynx at 24 at year 14.")
    B.mcq(T, "The graph shows the numbers of a prey species and of its predator over time. Which statement is best supported by the graph?",
          ch("The numbers of the predator rise and fall after the numbers of the prey do, which is consistent with a predator-prey interaction that drives the dynamics.", "Predator-prey interactions can drive population dynamics, with the predator peaking after the prey."),
          [ch("The numbers of the predator rise before the numbers of the prey rise, so the prey depend on the predator for their food.", "The peak of the predator comes after the peak of the prey."),
           ch("The numbers of the two species change in unrelated ways, so there is no interaction between the two species.", "The patterns are linked, with a delay."),
           ch("The numbers of the prey stay constant, while the numbers of the predator change from year to year in the community.", "The prey numbers change a lot from year to year.")],
          "Predator and prey populations can oscillate, with the predator lagging behind.", diagram=g, difficulty="medium")

    B.mcq(T, "When wolves were reintroduced to a park, the number of elk fell, and willow trees along the streams grew taller and more numerous. Which term describes this chain of effects?",
          ch("A trophic cascade, in which a change in a predator affects the lower trophic levels through the interactions among the populations.", "Trophic cascades are interactions among populations that spread through the trophic levels."),
          [ch("Niche partitioning, in which species with similar needs divide a resource so that they do not compete with each other for the resource.", "Niche partitioning divides resources among competing species. It does not describe a chain of effects."),
           ch("Commensalism, in which one species benefits from a second species that is not helped or harmed by the interaction.", "The wolves and the elk are in a predator-prey interaction."),
           ch("Genetic drift, in which the frequencies of alleles change because of chance in the small population of willow trees.", "The change is in the numbers of the populations and not in the allele frequencies.")],
          "A trophic cascade is a chain of effects through trophic levels.", difficulty="medium")

    B.mcq(T, "Several species of warblers feed on insects in the same spruce tree. Each species feeds mainly in a different part of the tree. Which statement best explains how this allows the species to live together?",
          ch("Niche partitioning reduces the competition between the species, because each species uses a different part of the shared resource.", "Niche partitioning allows species with similar needs to coexist."),
          [ch("Mutualism helps the species, because each species provides insects for the other species and receives food in return for that help.", "The warblers are not exchanging benefits."),
           ch("Parasitism helps the species, because each species lives on the body of another and takes food from it.", "The warblers are not parasites of each other."),
           ch("Competition is stronger between the species, because they use the same part of the tree and so eat the same insects.", "Each species feeds mainly in a different part, which lowers the competition.")],
          "Niche partitioning allows similar species to coexist.", difficulty="medium")

    sites = ["Site A", "Site B", "Site C"]
    means = [0.52, 0.58, 0.81]
    errs = [0.03, 0.04, 0.03]
    rng = [(m - e, m + e) for m, e in zip(means, errs)]
    overlap_ab = rng[0][1] >= rng[1][0]
    overlap_bc = rng[1][1] >= rng[2][0]
    assert overlap_ab and not overlap_bc
    chart = bars("Site", "Simpson's diversity index", 1.0, sites, [{"values": means, "errors": errs, "color": "green"}],
                 alt="Bar graph of the mean Simpson's diversity index with standard error bars: site A 0.52 plus or minus 0.03, site B 0.58 plus or minus 0.04, site C 0.81 plus or minus 0.03.")
    B.mcq(T, "The bars show the mean Simpson's diversity index of three sites, and the error bars show plus and minus one standard error. Which conclusion is best supported by the graph?",
          ch("Site C probably differs from site B, because their error bars do not overlap, but sites A and B may not differ, because their error bars overlap.", "Error bars that do not overlap suggest that the means are different. Overlapping error bars suggest that the difference may not be significant."),
          [ch("Site B has a significantly higher diversity than site A, because the mean of site B is greater than the mean of site A.", "The error bars overlap, so the difference may be due to chance."),
           ch("Sites A and C are the same, because the heights of the bars of all three sites are shown on the same axis.", "Site C has a much higher mean, and its error bar does not overlap with that of site A."),
           ch("The error bars show that the sites are the same, because a graph with error bars cannot be used to compare means.", "Error bars are used to estimate whether sample means are different.")],
          "Use error bars to estimate whether sample means are statistically different.", diagram=chart, difficulty="hard")

    rows = [("Alone", "400", "300"), ("Together", "380", "20")]
    B.mcq(T, "Two species of Paramecium that eat the same food were grown alone and together in separate flasks. The table shows the number of cells per milliliter at the end. Which conclusion is best supported by the data?",
          ch("The two species compete, and species 1 outcompetes species 2, because the numbers of species 2 fall greatly when it is grown together with species 1.", "Competition has negative effects on the species, and one species can drive the other to a lower population."),
          [ch("The two species have a mutualistic relationship, because both of the species grow better when they are in the same flask.", "Species 2 grows much worse when it is together with species 1."),
           ch("The two species do not interact, because the number of cells of species 1 is about the same alone and together.", "Species 2 is strongly affected when the species are together, which shows an interaction."),
           ch("Species 2 outcompetes species 1, because species 2 has the smaller number of cells when the species are together.", "The species with the larger number of cells is the better competitor.")],
          "Competition for the same resources can reduce one population.",
          diagram=table(["Culture", "Species 1 (cells/mL)", "Species 2 (cells/mL)"], rows, caption="Growth of two species of Paramecium", row_headers=True), difficulty="medium")

    rows = [("Interaction 1", "+", "+"), ("Interaction 2", "+", "-"), ("Interaction 3", "+", "0"), ("Interaction 4", "-", "-")]
    B.mcq(T, "The table shows the effect of four interactions on each of two species (+ is a benefit, - is harm, 0 is no effect). Which interaction is an example of mutualism?",
          ch("Interaction 1, because both species benefit from the interaction.", "In mutualism both species receive a benefit."),
          [ch("Interaction 2, because one species benefits and the other species is harmed by the interaction.", "This pattern describes predation or parasitism."),
           ch("Interaction 3, because one species benefits and the other species is not affected by the interaction.", "This pattern describes commensalism."),
           ch("Interaction 4, because both species are harmed by the interaction between them in the community.", "This pattern describes competition.")],
          "Mutualism: + for both species.",
          diagram=table(["Interaction", "Effect on species 1", "Effect on species 2"], rows, caption="Effects of four interactions", row_headers=True), difficulty="medium")

    B.mcq(T, "A new predator is introduced into a community, and it feeds mostly on the most common herbivore. Which change in the community is the most likely?",
          ch("The number of the herbivore falls, and the plants it eats and the other herbivores that use the same plants may increase in number.", "Interactions among populations change community structure over time."),
          [ch("The number of the herbivore rises, because predators remove the sick individuals and so the herbivore has more food to eat for each individual.", "A predator that feeds mostly on the herbivore lowers its numbers."),
           ch("The community stays the same, because the interactions between the populations do not change the structure of a community.", "Interactions determine how a community changes."),
           ch("The number of plants falls to zero, because the predator also eats the plants that the herbivore would normally eat.", "The predator feeds on the herbivore, not on plants.")],
          "Interactions among populations change community structure over time.", difficulty="medium")

    # ------------------------------------------------------------------ 8.6 Biodiversity
    T = 6
    B.mcq(T, "Which statement correctly compares a species-rich prairie with a lawn that has a single species of grass?",
          ch("The prairie is often more resilient to changes in the environment, because ecosystems with more diverse parts are less likely to be harmed by a single event.", "Ecosystems with fewer component parts and little diversity are often less resilient to changes."),
          [ch("The lawn is more resilient to changes in the environment, because a single species of grass is affected in the same way by every event.", "Less diversity makes the lawn less resilient."),
           ch("The prairie and the lawn are equally resilient, because both are ecosystems that have plants that capture energy from sunlight.", "Diversity affects resilience."),
           ch("The prairie is less resilient to changes in the environment, because a larger number of species increases the chance of a disruption.", "More diversity makes an ecosystem more resilient, not less.")],
          "Ecosystems with little diversity are often less resilient.", difficulty="easy")

    B.mcq(T, "Which description best defines a keystone species?",
          ch("A species whose effect on its ecosystem is much greater than its abundance would suggest, and whose removal often leads to a collapse of the ecosystem.", "The effects of keystone species on the ecosystem are disproportionate relative to their abundance."),
          [ch("The species with the largest number of individuals in an ecosystem, whose removal would have no effect on the other species.", "A keystone species is defined by its effect and not by being the most abundant."),
           ch("The species that is at the highest trophic level of an ecosystem, and which is the largest animal that lives in it.", "Keystone species are not necessarily top predators or the largest animals."),
           ch("The species that was the first to live in an ecosystem, and which stays there while the other species come and go.", "A keystone species is defined by its large effect, not by its age in the ecosystem.")],
          "Keystone species have disproportionate effects relative to their abundance.", difficulty="easy")

    rows = [("Species P", "55", "1"), ("Species Q", "30", "2"), ("Species R", "3", "14"), ("Species S", "12", "0")]
    B.mcq(T, "The table shows, for four species in a community, the percent of the total biomass and the number of other species that disappeared when the species was removed. Which species is most likely a keystone species?",
          ch("Species R, because it has a very small share of the biomass but its removal was followed by the loss of the greatest number of species.", "A keystone species has an effect that is disproportionate to its abundance."),
          [ch("Species P, because it has the largest share of the total biomass, which means that its removal has the largest effect.", "Species P is the most abundant, and its removal affected only one species."),
           ch("Species S, because it has a moderate share of the biomass, which means that it must be the most important species in the whole community.", "The removal of species S had no effect on the other species."),
           ch("Species Q, because it has the second largest share of the biomass, which gives it the second largest effect on the community.", "The effect of species Q is small, and abundance does not decide the effect.")],
          "A keystone species has a disproportionate effect compared with its biomass.",
          diagram=table(["Species", "Share of total biomass (%)", "Other species lost when it was removed"], rows, caption="Biomass of four species and the effect of removing each", row_headers=True), difficulty="hard")

    B.mcq(T, "Sea otters eat sea urchins, and sea urchins eat kelp. When sea otters are removed from a coastal ecosystem, the kelp forest often disappears. Which statement best explains this?",
          ch("The urchins increase in number without the otters and overgraze the kelp, so the loss of a keystone species causes the ecosystem to collapse.", "The effects of keystone species are disproportionate, and their removal often causes the ecosystem to collapse."),
          [ch("The kelp depends directly on the sea otters for its energy, so it cannot live if the otters are removed from the ecosystem.", "Kelp is a producer that captures its own energy from sunlight."),
           ch("The urchins decrease in number without the otters, so the kelp has no more competitors and so it should increase.", "Without the otters, the urchins increase in number."),
           ch("The otters are the most abundant species in the ecosystem, and so their removal removes most of the energy from it.", "The effect of the otters is larger than their abundance would suggest.")],
          "Removal of a keystone species can collapse an ecosystem through a trophic cascade.", difficulty="medium")

    B.mcq(T, "Why are producers important for maintaining the diversity of an ecosystem?",
          ch("They capture energy from sunlight or from inorganic molecules and make organic matter, which supports the other trophic levels of the ecosystem.", "Producers and essential biotic and abiotic factors contribute to maintaining the diversity of an ecosystem."),
          [ch("They obtain energy by consuming other organisms, and so they keep the numbers of the consumers from becoming too large.", "Producers are autotrophs and do not consume other organisms."),
           ch("They are always the least abundant organisms of an ecosystem, and so they have no influence on the other organisms.", "Producers are usually abundant, and the others depend on them."),
           ch("They return the carbon in dead organisms to the atmosphere, which is the main role of the producers in an ecosystem.", "That describes decomposers.")],
          "Producers supply the energy base for the ecosystem.", difficulty="medium")

    ctrl, rem = 15, 8
    pc = (rem - ctrl) / ctrl * 100
    assert round(pc, 1) == -46.7
    rows = [("Control plots (predator present)", str(ctrl)), ("Plots with the predator removed", str(rem))]
    B.mcq(T, f"Researchers removed a predator from some plots of a rocky shore. After a year, control plots had {ctrl} species and the plots without the predator had {rem} species. What was the percent change in the number of species after the removal of the predator?",
          ch(f"A decrease of about {abs(pc):.0f}%, because ({rem} - {ctrl}) / {ctrl} x 100 = {pc:.1f}%.", f"({rem} - {ctrl}) / {ctrl} x 100 = {pc:.1f}%.", round(pc, 1)),
          [ch(f"A decrease of about {(ctrl - rem) / rem * 100:.0f}%, because the difference is divided by the number of species in the plots without the predator.", "The percent change is calculated relative to the control value, which is the starting point.", round((ctrl - rem) / rem * 100, 1)),
           ch(f"A decrease of about {ctrl - rem}%, because the difference in the number of species is the percent change.", "A difference in numbers is not a percent. It must be divided by the control value.", float(ctrl - rem)),
           ch(f"An increase of about {abs(pc):.0f}%, because the plots without the predator have fewer species and so they are more diverse.", "The number of species fell, so the change is a decrease.", abs(round(pc, 1)))],
          "Percent change = (new - old) / old x 100.",
          diagram=table(["Plots", "Number of species"], rows, caption="Species on a rocky shore after one year", row_headers=True), difficulty="hard")

    B.mcq(T, "A keystone predator is removed from a grassland. Which prediction about the short-term and long-term effects is the most reasonable?",
          ch("In the short term the numbers of the herbivores that it ate rise, and in the long term the overgrazed plants decline and the ecosystem loses species.", "The addition or removal of a component of an ecosystem affects its short-term and long-term structure."),
          [ch("In the short term the numbers of the herbivores fall, and in the long term the plants decline because there are fewer herbivores.", "Without the predator, the herbivores would increase."),
           ch("In the short term nothing changes in the grassland, and in the long term the herbivores become the keystone species of the whole ecosystem of the grassland.", "The removal of a keystone species has effects soon."),
           ch("In the short term the numbers of the plants fall, and in the long term the predator returns by itself from the soil of the grassland.", "A removed predator does not return from the soil.")],
          "Removing a keystone species changes the ecosystem in the short term and the long term.", difficulty="medium")

    # ------------------------------------------------------------------ 8.7 Disruptions in ecosystems
    T = 7
    B.mcq(T, "Which statement best defines an adaptation?",
          ch("A genetic variation that is favored by selection and that appears as a trait that gives an advantage to an organism in a particular environment.", "An adaptation is a genetic variation favored by selection, manifested as a trait that provides an advantage in a particular environment."),
          [ch("A change that an individual makes to its own body during its life in order to cope with a change in the environment.", "A change during the life of an individual is not an inherited adaptation."),
           ch("A mutation that appears in an organism because the environment of the organism requires the organism to have it.", "Mutations are not directed by environmental pressures."),
           ch("A trait that is found in every member of a species, regardless of the environment in which the members live.", "An adaptation is advantageous in a particular environment, and not necessarily universal.")],
          "An adaptation is a heritable variation favored by selection in an environment.", difficulty="easy")

    rows = [("HbA HbA (normal hemoglobin)", "0.90"), ("HbA HbS (carrier)", "1.00"), ("HbS HbS (sickle cell disease)", "0.20")]
    B.mcq(T, "In a region with malaria, the relative fitness of people with each genotype of a hemoglobin gene is shown in the table. Which statement best explains why the allele HbS stays in the population?",
          ch("The heterozygous genotype has a higher relative fitness than either homozygous genotype, so selection keeps both alleles in the population.", "Heterozygote advantage is when the heterozygous genotype has a higher relative fitness than either homozygous genotype."),
          [ch("The homozygous genotype HbS HbS has the highest fitness of the three genotypes, so the allele HbS is increasing in the population of the region.", "HbS HbS has the lowest fitness in the table."),
           ch("The allele HbS is lost from the population at once, because the genotype HbS HbS has a very low relative fitness.", "Heterozygotes have the highest fitness, and they carry the allele."),
           ch("The allele HbS is kept in the population because malaria causes the HbA allele to mutate to the allele HbS.", "Mutations are not directed by the environment.")],
          "Heterozygote advantage maintains two alleles in a population.",
          diagram=table(["Genotype", "Relative fitness in a region with malaria"], rows, caption="Relative fitness of hemoglobin genotypes", row_headers=True), difficulty="medium")

    B.mcq(T, "Which statement correctly describes the relationship between mutations and environmental pressures?",
          ch("Mutations are not directed by specific environmental pressures, but selection by the environment acts on the variation that mutations provide.", "Mutations are not directed by specific environmental pressures."),
          [ch("Mutations are directed by specific environmental pressures, so that an organism makes the mutations that it needs in order to survive in that environment.", "Mutations occur at random."),
           ch("Mutations are caused by the needs of the organism, and the changes are passed on to the offspring as soon as the need appears.", "Needs do not cause mutations."),
           ch("Mutations occur only when the environment changes, and they stop when the environment becomes stable again for several years.", "Mutations occur all of the time, whether or not the environment changes.")],
          "Mutations are random; selection acts on the resulting variation.", difficulty="medium")

    B.mcq(T, "An invasive species is introduced into a lake. Which of the following best explains why it can spread and harm the native species?",
          ch("It may exploit a new niche that is free of predators or competitors, or outcompete the native species for resources.", "The introduction of an invasive species can allow it to exploit a new niche free of predators or competitors, or to outcompete native species."),
          [ch("It has a higher mutation rate than the native species, which gives it the alleles that it needs for the lake.", "The success of an invasive species is not due to a mutation rate."),
           ch("It is a native species of the lake that has recently changed its genes in response to the presence of other species.", "An invasive species is a species that is introduced from outside."),
           ch("It is a keystone species in its original habitat, and so it must also be a keystone species in the lake.", "Being a keystone species elsewhere does not explain its spread.")],
          "Invasive species exploit a new niche or outcompete natives.", difficulty="medium")

    conc = [("Plankton", 0.04), ("Small fish", 0.5), ("Large fish", 2.0), ("Fish-eating bird", 25.0)]
    fold = conc[-1][1] / conc[0][1]
    assert fold == 625
    rows = [(n_, f"{c_:g}") for n_, c_ in conc]
    B.mcq(T, "The table shows the concentration of a pesticide in the tissues of organisms in a food chain in a lake. Which conclusion is best supported by the data, and what is the increase from the plankton to the bird?",
          ch(f"The pesticide shows biomagnification, because its concentration rises at each trophic level, and it is {fold:.0f} times higher in the bird than in the plankton.", f"25 / 0.04 = {fold:.0f}. Biomagnification is the increase in the concentration of a substance at higher trophic levels.", fold),
          [ch(f"The pesticide is broken down by the organisms, because its concentration is {fold:.0f} times lower in the bird than in the plankton.", "The concentration is higher in the bird, not lower.", 1 / fold),
           ch("The pesticide is distributed equally in the food chain, because every organism takes it in from the water of the lake.", "The concentrations differ greatly among the organisms.", 1.0),
           ch(f"The pesticide shows biomagnification, because its concentration is {conc[-1][1] - conc[0][1]:g} times higher in the bird than in the plankton.", "The ratio of the concentrations is found by division, and not by subtraction.", conc[-1][1] - conc[0][1])],
          "Biomagnification: concentration increases at higher trophic levels.",
          diagram=table(["Organism", "Pesticide in tissues (parts per million)"], rows, caption="Concentration of a pesticide in a lake food chain", row_headers=True), difficulty="hard")

    B.mcq(T, "Fertilizer from fields runs into a lake. Soon after, algae cover the surface, and later many fish in the lake die. Which sequence of events best explains the death of the fish?",
          ch("Nutrients cause an algal bloom, the algae die and are decomposed by microorganisms that use up the oxygen, and the fish suffocate (eutrophication).", "Eutrophication is the enrichment of water with nutrients, which leads to oxygen depletion."),
          [ch("Nutrients cause the fish to grow larger and use up the oxygen, the algae die from a lack of food, and the fish starve.", "The algae increase because of the nutrients, and the oxygen is used up by decomposers."),
           ch("Nutrients cause a bloom of algae that releases large amounts of oxygen, and the extra oxygen poisons the fish in the lake.", "The decay of the algae uses up the oxygen and does not add it."),
           ch("Nutrients cause the temperature of the lake to fall, and the fish die because the algae block the sunlight from them.", "The death of the fish is due to a lack of oxygen and not to a lack of sunlight.")],
          "Eutrophication: nutrient enrichment, algal bloom, decomposition, oxygen depletion.", difficulty="medium")

    before, after = 120, 30
    pc = (after - before) / before * 100
    assert pc == -75.0
    rows = [("Before the introduction", str(before)), ("Five years after the introduction", str(after))]
    B.mcq(T, f"The table shows the density of a native mussel in a lake before and after an invasive mussel was introduced. What was the percent change in the density of the native mussel?",
          ch(f"A decrease of {abs(pc):.0f}%, because ({after} - {before}) / {before} x 100 = {pc:.0f}%.", f"({after} - {before}) / {before} x 100 = {pc:.0f}%.", pc),
          [ch(f"A decrease of {(before - after) / after * 100:.0f}%, because the loss of {before - after} is divided by the density after the introduction.", "The change is divided by the original density and not by the final density.", -(before - after) / after * 100),
           ch(f"A decrease of {before - after}%, because the loss of {before - after} individuals per square meter is a percent.", "A loss in individuals is not a percent until it is divided by the original density.", float(-(before - after))),
           ch(f"A decrease of {after / before * 100:.0f}%, because the final density is the percent change in the density.", "25% is the fraction that remained and not the percent change.", -25.0)],
          "Percent change = (new - old) / old x 100.",
          diagram=table(["Time", "Native mussels (individuals per square meter)"], rows, caption="Density of a native mussel", row_headers=True), difficulty="hard")

    B.mcq(T, "A volcano forms a new island, and a hurricane later blows seeds and birds to it from a nearby coast. Which statement best describes the role of such events?",
          ch("Geological and meteorological events change habitats and the distribution of ecosystems, and biogeographical studies show these changes.", "Geological and meteorological events affect habitat change and ecosystem distribution, and biogeographical studies illustrate these changes."),
          [ch("Geological and meteorological events have no effect on the distribution of species, because species stay in their original habitats for ever.", "These events can create new habitats and move species."),
           ch("Geological and meteorological events cause mutations that give the colonists the alleles that they need on the new island.", "Mutations are not directed by such events."),
           ch("Geological and meteorological events matter only to humans, because other species are not affected by changes in their habitats.", "Species are affected by changes in their habitats.")],
          "Geological and meteorological events change habitats and species distributions.", difficulty="medium")

    ctrl_m, ctrl_e, rem_m, rem_e = 4.2, 0.4, 7.8, 0.5
    assert (ctrl_m + ctrl_e) < (rem_m - rem_e)
    chart = bars("Plots", "Native plant species per plot", 10, ["Invasive plant present", "Invasive plant removed"],
                 [{"values": [ctrl_m, rem_m], "errors": [ctrl_e, rem_e], "color": "green"}],
                 alt="Bar graph of the mean number of native plant species per plot with standard error bars: invasive plant present 4.2 plus or minus 0.4, invasive plant removed 7.8 plus or minus 0.5.")
    B.mcq(T, "Researchers removed an invasive plant from some plots and left it in others. The bars show the mean number of native plant species per plot, and the error bars show plus and minus one standard error. Which conclusion is best supported?",
          ch("The plots without the invasive plant probably have more native species, because the error bars of the two means do not overlap, so the null hypothesis may be rejected.", "Error bars that do not overlap suggest that the means are different, which is evidence against the null hypothesis."),
          [ch("The invasive plant has no effect on the native species, because there are native species in the plots in which it is present.", "The mean number of native species is much lower where the invasive plant is present."),
           ch("The two means are the same, because both bars are within the range of the axis and so they are not different.", "The error bars do not overlap, which suggests that the means differ."),
           ch("The removal of the invasive plant reduced the number of native species, because the bar of the plots with removal is taller.", "The taller bar means that there are more native species.")],
          "Use error bars to evaluate a hypothesis about a difference.", diagram=chart, difficulty="hard")
