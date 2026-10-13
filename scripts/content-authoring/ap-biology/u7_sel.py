"""Unit 7, topics 7.1 Introduction to Natural Selection (8 questions), 7.2 Natural Selection (9) and 7.3 Artificial Selection (6).

Required content (CED 2025-26): 7.1.A natural selection is a major mechanism of evolution; competition for limited resources gives differential survival, and individuals with more favorable phenotypes
survive and produce more offspring, passing those traits on; 7.1.B fitness is measured by reproductive success; biotic and abiotic environments fluctuate and change the rate and direction of evolution, so
different variations are selected in each generation. 7.2.A natural selection acts on phenotypic variation; environments change and apply selective pressures; some phenotypic variations increase or decrease
fitness in particular environments; 7.2.B variation in the number and types of molecules within cells can give a greater ability to survive and reproduce in different environments. 7.3.A through artificial
selection humans affect variation in other species. Suggested skills: 1.B, 2.A, 4.B. Not tested: the names of the types of selection.
"""
from lib import *


def build(B):
    # ------------------------------------------------------------------ 7.1 Introduction to natural selection
    T = 1
    B.mcq(T, "Which statement best summarizes Darwin's theory of natural selection?",
          ch("Competition for limited resources causes differential survival, and individuals with favorable phenotypes produce more offspring and pass on those traits.", "Natural selection results from competition for limited resources, which leads to differential survival and reproduction."),
          [ch("Individuals change their traits during their lives in response to the environment, and they pass on the changed traits to their offspring.", "This describes the inheritance of acquired characteristics. It is not natural selection."),
           ch("All of the individuals in a population have the same chance of surviving, and so the traits of the population stay the same over time.", "Natural selection depends on differences in survival and reproduction between individuals."),
           ch("Individuals with unfavorable phenotypes are changed by the environment so that they have a better chance of surviving and having offspring.", "The environment selects among existing variation. It does not change the phenotypes of individuals into favorable ones.")],
          "Natural selection: competition for limited resources gives differential survival and reproduction of favorable phenotypes.", difficulty="easy")

    rows = [("Beetle 1", "9", "14"), ("Beetle 2", "4", "31"), ("Beetle 3", "11", "6"), ("Beetle 4", "6", "22")]
    best = max(rows, key=lambda r: int(r[2]))
    assert best[0] == "Beetle 2"
    B.mcq(T, "The table shows the lifespan of four beetles of the same species, and the number of their offspring that survived to adulthood. Which beetle has the highest evolutionary fitness?",
          ch("Beetle 2, because it has the most offspring that survived to adulthood, and fitness is measured by reproductive success.", "Evolutionary fitness is measured by reproductive success."),
          [ch("Beetle 3, because it has the longest lifespan, and fitness is measured by how long an individual lives.", "Fitness is not measured by the length of life. Beetle 3 has few surviving offspring."),
           ch("Beetle 1, because it has an intermediate lifespan, and fitness is measured by being average in the population.", "Fitness is not measured by being average."),
           ch("Beetle 4, because it has both a short lifespan and a large number of offspring, and so it has the highest fitness of the four.", "Beetle 4 has fewer surviving offspring than Beetle 2.")],
          "Fitness is measured by reproductive success.",
          diagram=table(["Beetle", "Lifespan (months)", "Offspring that survived to adulthood"], rows, caption="Lifespan and reproductive success of four beetles", row_headers=True), difficulty="easy")

    B.mcq(T, "Which of the following is required for natural selection to change the traits of a population?",
          ch("The individuals in the population differ in heritable traits that affect how many offspring they leave in their environment.", "Natural selection needs heritable variation that affects survival and reproduction."),
          [ch("The individuals in the population are all identical in their traits, so that none of them is favored by the environment.", "If all individuals were identical, there would be nothing for selection to act on."),
           ch("The individuals in the population change their traits during their lives, and these changes are passed on to their offspring.", "Changes that occur during the life of an individual are not inherited by the offspring."),
           ch("The environment of the population stays the same for many generations, so the same traits are selected in every generation.", "A stable environment is not required for natural selection, and the environment often changes.")],
          "Natural selection needs heritable variation that affects fitness.", difficulty="medium")

    B.mcq(T, "A biologist claims that giraffes have long necks because their ancestors stretched their necks to reach leaves and then passed on the longer necks to their offspring. Which statement is the best evaluation of the claim from the point of view of natural selection?",
          ch("It is not supported, because a trait that an individual gains during its life is not inherited, and selection favors existing heritable variation.", "Natural selection acts on heritable variation. Changes acquired by an individual are not passed on."),
          [ch("It is supported, because the individuals that stretch their necks the most are the ones that leave the most offspring in the population.", "Stretching does not change the genes of the gametes, so the longer neck is not inherited."),
           ch("It is supported, because the environment causes the individuals of a population to change in the way that they need to survive.", "The environment selects among existing variants. It does not direct the changes."),
           ch("It is not supported, because giraffes with short necks and giraffes with long necks have the same chance of surviving in all environments.", "Natural selection does depend on differences in survival, and the claim fails for a different reason.")],
          "Acquired characteristics are not inherited; natural selection acts on heritable variation.", difficulty="medium")

    B.mcq(T, "In one year, a drought leaves only large, hard seeds on an island, and finches with deep beaks survive and reproduce more. In the next years there is plenty of rain, and small, soft seeds become common. Which prediction about the finch population is most consistent with natural selection?",
          ch("The favored beak depth can change in the later generations, because the changed environment can select different variations in each generation.", "Biotic and abiotic environments fluctuate, which affects the rate and direction of evolution."),
          [ch("The beak depth stays deep in all of the later generations, because the drought permanently changed the genes of the population.", "The environment does not permanently change the genes. A new environment can select different variants."),
           ch("The beak depth of every finch gets shallower, because the individuals respond to the rain by changing the shape of their beaks.", "Individual birds do not change their beak shape in response to the environment in this way."),
           ch("The beak depth does not change in later generations, because the environment has no effect on which finches survive and reproduce.", "The kind of seeds in the environment does affect survival and reproduction.")],
          "A fluctuating environment changes the direction of selection from one generation to the next.", difficulty="medium")

    B.mcq(T, "Which of the following is an example of a change in the abiotic environment that could change the direction of natural selection in a population?",
          ch("A gradual increase in the average temperature of the habitat over many years, which favors individuals that tolerate heat", "Temperature is an abiotic factor, and a change in it can change which phenotypes are favored."),
          [ch("The arrival of a new predator that hunts the individuals of the population, which favors individuals that can hide well from it", "A predator is a biotic factor and not an abiotic factor."),
           ch("The spread of a parasite among the individuals of the population, which favors individuals that resist its effects", "A parasite is a biotic factor and not an abiotic factor."),
           ch("The increase in the number of competitors that feed on the same food, which favors individuals that use other foods", "Competitors are a biotic factor and not an abiotic factor.")],
          "Biotic and abiotic environments both fluctuate and affect the direction of evolution.", difficulty="medium")

    classes = [6, 7, 8, 9, 10, 11]
    before = [10, 30, 50, 40, 20, 5]
    after = [1, 5, 20, 30, 20, 5]
    mb = sum(c * n for c, n in zip(classes, before)) / sum(before)
    ma = sum(c * n for c, n in zip(classes, after)) / sum(after)
    assert (sum(before), sum(after)) == (155, 81) and (round(mb, 2), round(ma, 2)) == (8.29, 8.96) and round(ma - mb, 1) == 0.7
    graph7 = bars("Beak depth (mm)", "Number of birds", 60, [str(c) for c in classes],
                  [{"values": before, "label": "Before the drought", "color": "blue"}, {"values": after, "label": "After the drought", "color": "red"}],
                  alt="Bar graph of the numbers of birds in beak depth classes of 6 to 11 mm before and after a drought. Before: 10, 30, 50, 40, 20 and 5. After: 1, 5, 20, 30, 20 and 5.")
    B.mcq(T, f"The graph shows the beak depths of a population of finches before a drought and of the survivors after the drought. The mean beak depth is {mb:.2f} mm before the drought. Which statement is best supported by the data?",
          ch(f"The mean beak depth of the survivors is greater by about {ma - mb:.1f} mm, which is consistent with selection for deeper beaks during the drought.", f"The mean of the survivors is {ma:.2f} mm, which is {ma - mb:.1f} mm more than {mb:.2f} mm."),
          [ch("The mean beak depth of the survivors is smaller than before, because the number of birds in every depth class fell during the drought year.", "The numbers fell more in the shallow classes, so the mean beak depth rose."),
           ch("The mean beak depth did not change, because the number of birds in the 10 mm and 11 mm classes is the same before and after.", "The birds in the shallower classes were lost, which changes the mean even though the deepest classes did not change."),
           ch("The drought caused the beaks of the birds to grow deeper, because the survivors have deeper beaks than the whole population had.", "The survivors were selected from birds that already had deeper beaks. The beaks of individuals did not grow deeper.")],
          "Differential survival shifted the population toward deeper beaks.", diagram=graph7, difficulty="hard")

    green_n, green_off, brown_n, brown_off = 40, 120, 60, 120
    fg, fb = green_off / green_n, brown_off / brown_n
    assert (fg, fb, fg / fb) == (3.0, 2.0, 1.5)
    rows = [("Green", str(green_n), str(green_off)), ("Brown", str(brown_n), str(brown_off))]
    B.mcq(T, "A population of beetles has green and brown individuals. The table shows the number of adults of each color and the total number of offspring that they produced. Which statement best compares the evolutionary fitness of the two colors?",
          ch(f"Green beetles have higher fitness, because they produced {fg:.1f} offspring per adult, which is {fg / fb:.1f} times the {fb:.1f} offspring per adult of the brown beetles.", f"{green_off} / {green_n} = {fg:.1f} offspring per green adult, and {brown_off} / {brown_n} = {fb:.1f} per brown adult."),
          [ch(f"Brown beetles have higher fitness, because there are {brown_n} brown adults, which is more than the {green_n} green adults in the population.", "Fitness is measured by reproductive success per individual, not by the number of individuals."),
           ch("The two colors have the same fitness, because the green and the brown beetles produced the same total number of offspring.", "The total is the same, but the green beetles produced it with fewer adults."),
           ch(f"Green beetles have lower fitness, because there are fewer green adults than brown adults in the population that produced the offspring.", "A lower number of adults means the green beetles had more offspring each, not fewer.")],
          "Fitness is measured by reproductive success, such as offspring per individual.",
          diagram=table(["Color", "Number of adults", "Total offspring"], rows, caption="Reproductive success of green and brown beetles", row_headers=True), difficulty="hard")

    # ------------------------------------------------------------------ 7.2 Natural selection
    T = 2
    B.mcq(T, "Natural selection acts directly on which of the following in a population?",
          ch("Phenotypic variation, because the phenotype of an individual affects its survival and reproduction in its environment", "Natural selection acts on phenotypic variation in populations."),
          [ch("The alleles inside the gametes, because the environment can detect an allele before it is expressed in an individual", "Selection acts on phenotypes. Alleles change in frequency as a consequence."),
           ch("The needs of the individuals, because the environment changes the traits that an individual needs in order to survive", "Individuals do not change their traits according to what they need."),
           ch("The traits that individuals gain during their lives, because the environment rewards the individuals that work the hardest", "Traits gained during life are not inherited.")],
          "Natural selection acts on phenotypic variation.", difficulty="easy")

    B.mcq(T, "A population of beetles lives on pale sand. A volcanic eruption covers the sand with dark ash. Some beetles are pale and some are dark, and birds eat the beetles they can see. Which result is most likely in the next generations?",
          ch("The proportion of dark beetles will increase, because the dark beetles are harder for the birds to see on the ash and so they survive more.", "A change in the environment applies a selective pressure, and the phenotype that is favored becomes more common."),
          [ch("The proportion of pale beetles will increase, because the pale beetles were adapted to the sand and so they will adapt to the ash.", "Pale beetles are more visible on the dark ash, so they are eaten more."),
           ch("The pale beetles will turn dark, because the beetles change their color in response to the ash and pass on the new color.", "Individual beetles do not change color in this way, and acquired changes are not inherited."),
           ch("The proportions of pale and dark beetles will stay the same, because the color of a beetle has no effect on its fitness.", "Color affects visibility to predators, so it affects survival.")],
          "Environments change and apply selective pressures to populations.", difficulty="easy")

    B.mcq(T, "Thick fur increases the survival of mammals in a cold climate but decreases the survival of mammals of the same species in a hot climate. Which statement best explains this observation?",
          ch("Whether a phenotypic variation increases or decreases fitness depends on the environment in which the organism lives.", "Some phenotypic variations increase or decrease fitness in particular environments."),
          [ch("A trait that is favorable in one environment is also favorable in all other environments, because fitness is a property of the trait.", "A trait can be favorable in one environment and unfavorable in another."),
           ch("Thick fur is controlled by the environment and not by genes, and so it cannot be affected by natural selection in the population.", "Natural selection acts when the variation in the trait is heritable."),
           ch("The mammals in the hot climate lose the genes for thick fur, because natural selection removes the genes that are not used by the mammals.", "Genes are not lost because they are not used. Individuals with thick fur survive less and leave fewer offspring.")],
          "Some phenotypic variations increase or decrease fitness in particular environments.", difficulty="medium")

    B.mcq(T, "Populations of a fish species live in cold water and in warm water. The fish in the cold water make a form of an enzyme that works well at low temperatures, and the fish in the warm water make a form that works well at high temperatures. Which statement best explains how this variation in molecules can affect the populations?",
          ch("Variation in the types of enzyme molecules gives fish a greater ability to survive and reproduce in the water temperature in which they live.", "Variation in the number and types of molecules in cells can improve survival and reproduction in different environments."),
          [ch("Enzymes in the fish change their shape to suit each new temperature, so all of the fish in a species have the same fitness everywhere.", "The forms of an enzyme are determined by alleles, and fitness differs between environments."),
           ch("Fish in warm water make more mutations in the gene for the enzyme, so the enzyme is able to match the temperature of the water.", "Mutations are random and are not directed by the temperature."),
           ch("The type of enzyme in a fish has no effect on its fitness, because all enzymes work equally well at every temperature.", "Enzyme activity depends on temperature, and so the type of enzyme can affect survival.")],
          "Variation in the molecules in cells can improve survival in different environments.", difficulty="medium")

    gens = [0, 2, 4, 6, 8, 10]
    dark_soil = [0.20, 0.38, 0.60, 0.78, 0.88, 0.93]
    light_sand = [0.20, 0.12, 0.08, 0.05, 0.03, 0.02]
    pts_a = list(zip(gens, dark_soil))
    pts_b = list(zip(gens, light_sand))
    g = graph("Generation", "Frequency of dark-coated mice", 0, 10, 0, 1,
              [line("Dark volcanic soil", pts_a, "red"), line("Light sand", pts_b, "blue")],
              "Frequency of dark-coated mice against generation in two habitats. On dark soil it rises from 0.20 to 0.93 over 10 generations. On light sand it falls from 0.20 to 0.02.")
    B.mcq(T, "Mice in two habitats started with the same frequency of dark-coated mice. The graph shows how the frequency changed over 10 generations. Which conclusion is best supported by the data?",
          ch("Selection favored dark coats on dark soil and light coats on light sand, so the same trait had a different fitness in the two habitats.", "The frequency of dark mice rose in one habitat and fell in the other, so the favored phenotype depends on the environment."),
          [ch("Mice with dark coats have higher fitness in every habitat, because the frequency of dark mice is higher than 0.20 after 10 generations.", "The frequency of dark mice fell on light sand."),
           ch("The coat color of the mice on the dark soil changed because the mice needed to match the soil, and the mice changed their coats to do so.", "The frequency changed because of differential survival and reproduction, not because individuals changed."),
           ch("The two habitats have no effect on the mice, because the frequency of dark mice started at the same value of 0.20 in both populations.", "The frequencies diverged, which shows an effect of the habitat.")],
          "The same phenotype can be favored in one environment and disfavored in another.", diagram=g, difficulty="medium")

    B.mcq(T, "In a population of birds, chicks of intermediate weight survive better than very small chicks or very large chicks. What is the most likely effect of this selection on the variation in chick weight in the population?",
          ch("The variation in chick weight tends to decrease, because chicks at the extremes survive less often and so fewer of them will reproduce.", "When the extremes are selected against, the population has less variation around the favored phenotype."),
          [ch("The variation in chick weight tends to increase, because the chicks at both extremes survive better than the chicks of intermediate weight.", "The chicks at the extremes survive less often in this case."),
           ch("The mean chick weight tends to shift toward a very high weight, because heavier chicks always have a higher fitness than lighter chicks.", "Intermediate chicks are favored here, so the mean does not shift to a very high weight."),
           ch("The variation in chick weight does not change at all, because selection acts only on traits that have a simple pattern of inheritance.", "Selection acts on any heritable variation that affects fitness.")],
          "Selection against extreme phenotypes reduces variation.", difficulty="medium")

    n, p_trait, s_with, s_without = 1000, 0.10, 0.80, 0.50
    with_t = n * p_trait * s_with
    without_t = n * (1 - p_trait) * s_without
    frac = with_t / (with_t + without_t)
    assert (with_t, without_t, round(frac * 100, 1)) == (80.0, 450.0, 15.1)
    B.mcq(T, f"In a population of {n:,} insects, {int(p_trait * 100)}% have a heritable trait. Of the insects with the trait, {int(s_with * 100)}% survive to reproduce, and of the insects without the trait, {int(s_without * 100)}% survive to reproduce. Assuming that all survivors reproduce equally and that the trait is inherited, what percent of the next generation is expected to have the trait?",
          ch(f"About {frac * 100:.0f}%, because {int(with_t)} of the {int(with_t + without_t)} survivors have the trait.", f"{int(with_t)} insects with the trait and {int(without_t)} without it survive, and {int(with_t)} / {int(with_t + without_t)} = {frac * 100:.1f}%.", round(frac * 100, 1)),
          [ch(f"About {int(p_trait * 100)}%, because the percent of insects with the trait does not change when only some of the insects survive.", "The survivors are not a random sample. The insects with the trait survive more often.", p_trait * 100),
           ch(f"About {int(s_with * 100)}%, because that is the percent of the insects with the trait that survive to reproduce in the population.", "80% is the survival rate of the insects with the trait, and not their percent of the survivors.", s_with * 100),
           ch(f"About {int(with_t / (n * p_trait) * 100 - 50)}%, because the survival rates of the two groups differ by this amount and the trait gains that much.", "The difference in survival rates is not the new percent of the population with the trait.", 30.0)],
          "A higher survival rate increases the frequency of a heritable trait in the next generation.", difficulty="hard")

    rows = [("Warm and dry", "72", "38"), ("Cool and wet", "41", "76")]
    ratio_w = 72 / 38
    ratio_c = 76 / 41
    B.mcq(T, "The table shows the percent of seedlings with a hairy-leaf variant and with a smooth-leaf variant that survived in two environments. Which conclusion is best supported by the data?",
          ch("Hairy leaves increase the fitness of seedlings in the warm, dry environment, and smooth leaves increase fitness in the cool, wet environment.", "The variant with the higher survival differs between the two environments."),
          [ch("Hairy leaves increase fitness in both environments, because the percent of hairy seedlings that survived is high in the warm, dry environment.", "In the cool, wet environment, smooth seedlings survived better than hairy seedlings."),
           ch("Smooth leaves increase fitness in both environments, because the percent of smooth seedlings that survived is high in the cool, wet environment.", "In the warm, dry environment, hairy seedlings survived better than smooth seedlings."),
           ch("Leaf type has no effect on fitness in either environment, because some seedlings of both variants survived in both environments.", "The survival percents differ between the variants in each environment, which shows an effect of leaf type.")],
          "Whether a variation is favorable depends on the environment.",
          diagram=table(["Environment", "Hairy leaves: seedlings that survived (%)", "Smooth leaves: seedlings that survived (%)"], rows, caption="Survival of two leaf variants in two environments", row_headers=True), difficulty="medium")

    B.mcq(T, "Individuals in a population of yeast differ in the number of copies of a gene for an enzyme that digests a sugar. Cells with more copies make more of the enzyme. When the sugar is the only food, which prediction is most consistent with natural selection?",
          ch("Cells with more copies of the gene grow faster and reproduce more, so the number of copies per cell tends to increase in the population.", "Variation in the number of molecules in cells can give a greater ability to survive and reproduce."),
          [ch("Cells with fewer copies of the gene grow faster, because making more of an enzyme always wastes energy and lowers fitness.", "When the sugar is the only food, more enzyme allows more growth."),
           ch("The cells add copies of the gene to their DNA because they need them, and then pass these copies on to the cells they produce.", "Genetic changes are not directed by the needs of the cells."),
           ch("The number of copies of the gene has no effect on the growth of the cells, because the amount of an enzyme does not affect its activity.", "The amount of enzyme affects how fast the sugar is digested.")],
          "Variation in the number of molecules in cells can affect fitness.", difficulty="medium")

    # ------------------------------------------------------------------ 7.3 Artificial selection
    T = 3
    B.mcq(T, "Which statement correctly describes artificial selection?",
          ch("Humans choose which individuals of a species reproduce, and so they affect the variation and the traits of the next generation.", "Through artificial selection, humans affect variation in other species."),
          [ch("The environment chooses which individuals of a species reproduce, and so the traits of the population fit the habitat better.", "This describes natural selection."),
           ch("Humans change the genes of individuals during their lives, and the individuals then pass on those new traits to their offspring.", "Artificial selection chooses among existing variation. It does not directly change the genes of individuals."),
           ch("Humans prevent all of the individuals of a species from reproducing, and so the species is not able to evolve in the next generations.", "In artificial selection, some chosen individuals reproduce, and the species can change.")],
          "In artificial selection, humans choose which individuals breed.", difficulty="easy")

    B.mcq(T, "Cabbage, broccoli, kale and cauliflower are all descended from one wild species of mustard plant. Which statement best explains how such different crops arose?",
          ch("Growers chose and bred plants with different favored traits, such as large leaves, flower clusters or buds, over many generations.", "Artificial selection for different traits in the same species produced different crops."),
          [ch("The plants changed their own shapes in response to the way they were grown, and then passed on the new shapes to their seeds.", "Acquired changes are not inherited."),
           ch("Natural selection in the wild favored these shapes without any human involvement, because each shape is better in a different habitat.", "The crops differ because humans chose the traits."),
           ch("The growers introduced new genes into the plants during their lives, and the genes then spread to every plant of the species.", "Selective breeding uses variation that already exists in the species.")],
          "Humans selecting different traits in one species can produce very different forms.", difficulty="medium")

    B.mcq(T, "Which statement correctly compares natural selection and artificial selection?",
          ch("In natural selection the environment determines which individuals reproduce most, and in artificial selection humans determine this.", "The agent of selection is the environment in natural selection and humans in artificial selection."),
          [ch("In natural selection humans determine which individuals reproduce most, and in artificial selection the environment determines this.", "This reverses the agents of the two kinds of selection."),
           ch("In natural selection variation is not needed, and in artificial selection there has to be variation in a trait in the population.", "Both kinds of selection need variation."),
           ch("In natural selection traits are not inherited, and in artificial selection the selected traits are passed on to the next generation.", "Both kinds of selection act on heritable traits.")],
          "Artificial selection is selection by humans; natural selection is selection by the environment.", difficulty="medium")

    gens = [0, 1, 2, 3, 4]
    means = [18.0, 21.5, 25.0, 28.5, 32.0]
    gain = [b - a for a, b in zip(means, means[1:])]
    assert gain == [3.5] * 4
    avg_gain = sum(gain) / len(gain)
    rows = [(str(g_), fix(m_, 1)) for g_, m_ in zip(gens, means)]
    B.mcq(T, f"In an artificial selection experiment, the fruit flies in each generation with the most bristles were used as parents for the next generation. The table shows the mean number of bristles. What was the mean change in bristles per generation?",
          ch(f"{avg_gain:.1f} bristles per generation, because the mean rose from {means[0]:.1f} to {means[-1]:.1f} in {len(gain)} generations.", f"({means[-1]:.1f} - {means[0]:.1f}) / {len(gain)} = {avg_gain:.1f}.", avg_gain),
          [ch(f"{means[-1] - means[0]:.1f} bristles per generation, because the mean rose by that number between the first and the last generation.", f"{means[-1] - means[0]:.1f} is the total rise over {len(gain)} generations and not the rise per generation.", means[-1] - means[0]),
           ch(f"{means[-1] / len(gens):.1f} bristles per generation, because the mean number in the last generation is shared out among the generations.", "The rate is the change in the mean divided by the number of generations over which it changed.", means[-1] / len(gens)),
           ch(f"{(means[-1] - means[0]) / len(gens):.1f} bristles per generation, because the total change is divided by the number of rows in the table.", f"The table has {len(gens)} rows, but only {len(gain)} generations of selection took place between them.", (means[-1] - means[0]) / len(gens))],
          "Rate of change = change in the mean divided by the number of generations.",
          diagram=table(["Generation", "Mean number of bristles"], rows, caption="Artificial selection for bristle number", row_headers=True), difficulty="medium")

    ctrl = [18.0, 18.2, 17.9, 18.1, 18.0]
    g2 = graph("Generation", "Mean number of bristles", 0, 4, 14, 34,
               [line("Selected line", list(zip(gens, means)), "red"), line("Control line (parents chosen at random)", list(zip(gens, ctrl)), "blue")],
               "Mean number of bristles against generation. The selected line rises from 18.0 to 32.0. The control line stays at about 18.")
    B.mcq(T, "The graph shows the mean number of bristles of a selected line of flies and of a control line in which the parents were chosen at random. Why is the control line important to the experiment?",
          ch("It shows that the increase in the selected line is caused by choosing the parents, and not by the conditions in which all of the flies were kept.", "A control that changes little shows that selection, and not another variable, caused the change."),
          [ch("It shows that the bristles of the flies in the control line cannot change, because the flies in this line have no genetic variation.", "The control line has the same kind of variation. Its mean changed little because parents were chosen at random."),
           ch("It shows that artificial selection has no effect on the traits of a population, because both lines are kept in the same laboratory.", "The selected line changed a lot and so selection had an effect."),
           ch("It shows that the flies in the selected line are a different species from the flies in the control line after four generations.", "The data show a change in a trait. They do not show the formation of a new species.")],
          "A control separates the effect of selection from other variables.", diagram=g2, difficulty="medium")

    B.mcq(T, "A farmer breeds only the highest-yielding plants of a crop for many generations, so that almost all of the plants in the field are closely related. What is the most likely long-term risk?",
          ch("The crop has low genetic variation, so a new disease or a change in the climate could harm all of the plants in the field at the same time.", "Artificial selection can reduce variation, and populations with little diversity are at risk."),
          [ch("The crop has high genetic variation, so each plant responds differently to the disease and some plants always survive.", "Breeding closely related plants reduces variation."),
           ch("The crop plants evolve resistance to every disease, because the farmer chose the best plants for many generations in a row.", "Selection for yield does not provide resistance to every disease."),
           ch("The crop plants no longer reproduce, because artificial selection removes the genes that are needed for sexual reproduction.", "The selected plants reproduce. The risk is the loss of variation.")],
          "Artificial selection can reduce genetic variation in a population.", difficulty="medium")
