"""Unit 8: six free-response prompts, one of each kind.

  RESULTS        (9)  8.1  woodlice in a light and dark choice chamber (a chi-square test of a behavioral response)
  RESULTS_GRAPH  (9)  8.4  yeast in a flask of medium (replicate means and standard errors -> graph, growth rate, carrying capacity)
  INVESTIGATION  (4)  8.7  does phosphate cause an algal bloom? (pond water in jars)
  CONCEPT        (4)  8.6  a keystone sea star on a rocky shore
  MODEL          (4)  8.2  energy at four trophic levels (a table is the "figure")
  DATA           (4)  8.5  Simpson's diversity index for two forest plots

Part structure follows the CED (see u3_frq.py). Every number is computed here from the raw data, and the sample responses are built from the same variables.
"""
from lib import *


def build(B):
    # ------------------------------------------------------------------ RESULTS (9): woodlice, chi-square
    n, dark, light = 60, 41, 19
    exp = n / 2
    chi = (dark - exp) ** 2 / exp + (light - exp) ** 2 / exp
    crit = 3.84
    assert (dark + light, exp, round(chi, 2)) == (60, 30.0, 8.07) and chi > crit
    rows = [("Dark side", str(dark)), ("Light side", str(light))]
    B.frq(1, "RESULTS",
          "Woodlice (small land crustaceans) lose water easily and are eaten by many predators. A student put 60 woodlice into a chamber that had one dark half and one light half. The two halves were at the same temperature and the same humidity. After 10 minutes, the student counted the woodlice on each half. The results are shown in the table. The student will use a chi-square test to analyze the results.\n\n"
          "**(a)** **Describe** one way in which a behavioral response to light could increase the fitness of woodlice. (1 point)\n\n"
          "**(b)** (i) **Identify** the independent variable in the investigation. (ii) **State** the null hypothesis for the chi-square test. (iii) **Calculate** the number of woodlice that is expected on each half if the null hypothesis is correct. (3 points)\n\n"
          "**(c)** (i) **Calculate** the chi-square value for the data. Give your answer to the nearest 0.01. (ii) **Use** the critical value of 3.84 (p = 0.05, 1 degree of freedom) to determine whether the null hypothesis should be rejected. (iii) **State** a conclusion about the response of the woodlice to light. (3 points)\n\n"
          "**(d)** A classmate claims that the woodlice are responding to humidity and not to light. **Describe** a change to the procedure that would test this claim, and **predict** the result if the claim is correct. (2 points)",
          [(1, "(a) Describes that moving away from light (to a dark place) helps woodlice to avoid predators that find them by sight, or to lose less water, so they are more likely to survive and reproduce."),
           (1, "(b)(i) Identifies the independent variable as the amount of light (light or dark) in each half of the chamber."),
           (1, "(b)(ii) States a null hypothesis: the woodlice have no preference for the dark or the light half (they are distributed equally, and any difference is due to chance)."),
           (1, "(b)(iii) Calculates the expected number as 30 woodlice on each half (60 / 2)."),
           (1, "(c)(i) Calculates chi-square = (41 - 30)²/30 + (19 - 30)²/30 = 8.07."),
           (1, "(c)(ii) Determines that the null hypothesis is rejected, because 8.07 is greater than the critical value of 3.84."),
           (1, "(c)(iii) States that the woodlice respond to light by moving to the dark half (the difference from an equal distribution is unlikely to be due to chance)."),
           (1, "(d) Describes a change that separates humidity from light, such as making one half moist and the other half dry while the light is the same in both halves (or making both halves of the same humidity but different in light)."),
           (1, "(d) Predicts that, if the claim is correct, most of the woodlice will move to the moist half, whichever half is lit.")],
          "(a) Woodlice that move into the dark are harder for predators that hunt by sight to find, and they lose less water, so they are more likely to survive and reproduce.\n\n"
          "(b) (i) The independent variable is the amount of light in each half of the chamber (light or dark). (ii) The woodlice have no preference for either half, and any difference from an equal distribution is due to chance. (iii) 60 / 2 = 30 woodlice are expected on each half.\n\n"
          f"(c) (i) Chi-square = ({dark} - {exp:.0f})²/{exp:.0f} + ({light} - {exp:.0f})²/{exp:.0f} = {121 / 30:.3f} + {121 / 30:.3f} = {chi:.2f}. (ii) {chi:.2f} is greater than 3.84, so the null hypothesis is rejected. (iii) The woodlice respond to light by moving to the dark half, and the difference from an equal distribution is unlikely to be due to chance.\n\n"
          "(d) Make one half moist and the other half dry, and keep the light the same in both halves. If the woodlice are responding to humidity, most of them will move to the moist half, whichever half is lit.",
          diagram=table(["Half of the chamber", "Number of woodlice after 10 minutes"], rows, caption="Woodlice in a chamber with a dark half and a light half", row_headers=True))

    # ------------------------------------------------------------------ RESULTS_GRAPH (9): yeast logistic growth
    days = ["0", "2", "4", "6", "8", "10"]
    raw = {"0": [18, 21, 19, 22], "2": [66, 73, 69, 72], "4": [221, 238, 229, 232], "6": [505, 534, 516, 525], "8": [688, 714, 696, 702], "10": [731, 748, 736, 745]}
    means = [mean(raw[d_]) for d_ in days]
    ses = [se(raw[d_]) for d_ in days]
    assert means == [20.0, 70.0, 230.0, 520.0, 700.0, 740.0], means
    rate = (means[3] - means[2]) / (int(days[3]) - int(days[2]))
    assert rate == 145.0
    rows = [(d_, fix(m_, 0), fix(e_, 2)) for d_, m_, e_ in zip(days, means, ses)]
    se_text = ", ".join(fix(e_, 1) for e_ in ses[:-1]) + " and " + fix(ses[-1], 1)
    B.frq(4, "RESULTS_GRAPH",
          "A student put a small number of yeast cells into each of four flasks that contained the same volume of a medium with a limited amount of sugar. The student counted the yeast cells in each flask every two days. The means and the standard errors of the means of the four flasks are shown in the table.\n\n"
          "**(a)** **Identify** one density-dependent factor that could limit the growth of the yeast population in a flask. (1 point)\n\n"
          "**(b)** **Construct** a graph of the data in the table. Because you are answering in writing, describe the graph you would draw: the type of graph, what is shown on each axis, with units, the scale of each axis, the values you would plot, and how you would show the standard errors. (4 points)\n\n"
          "**(c)** (i) **Calculate** the average rate of growth of the population, in thousands of cells per milliliter per day, between day 4 and day 6. (ii) **Estimate** the carrying capacity of the flask from the data. (2 points)\n\n"
          "**(d)** **Predict** how the carrying capacity would change if the volume of the medium in each flask were doubled, with the same concentration of sugar, and **justify** your prediction. (2 points)",
          [(1, "(a) Identifies a density-dependent factor, such as the shortage of sugar (competition for resources), the build-up of waste products such as ethanol, or the spread of disease or a lack of space."),
           (1, "(b) Chooses an appropriate graph type: a line graph (or a scatter plot with a line) with time on the horizontal axis."),
           (1, "(b) Labels both axes with units: time (days) on the horizontal axis and the mean number of yeast cells (thousands per milliliter) on the vertical axis."),
           (1, "(b) Gives an appropriate scale: a vertical axis that starts at 0 and has equal intervals, extending to at least 750 so that all of the means fit, and a horizontal axis from 0 to 10 days."),
           (1, "(b) Plots the data accurately (20, 70, 230, 520, 700 and 740) and shows error bars of plus and minus one standard error for each point."),
           (1, "(c)(i) Calculates (520 - 230) / (6 - 4) = 145 thousand cells per milliliter per day."),
           (1, "(c)(ii) Estimates a carrying capacity of about 740 thousand cells per milliliter (the value at which the population levels off, 700 to 750)."),
           (1, "(d) Predicts that the carrying capacity would increase (to about double, or about 1,500 thousand cells per milliliter in total, if the concentration of cells is unchanged)."),
           (1, "(d) Justifies the prediction: the carrying capacity is set by the available resources, and doubling the volume of the medium doubles the total amount of sugar, which can support more yeast cells.")],
          "(a) The shortage of sugar, because the cells compete for it more as their density rises (or the build-up of waste products).\n\n"
          "(b) A line graph. The horizontal axis is labeled \"Time (days)\" and is scaled from 0 to 10 in steps of 2. The vertical axis is labeled \"Mean number of yeast cells (thousands per milliliter)\" and is scaled from 0 to 800 in steps of 100. The points are 20, 70, 230, 520, 700 and 740, each with an error bar of plus and minus one standard error "
          f"({se_text} thousand cells per milliliter, which are small). The curve rises slowly, then steeply, and then levels off.\n\n"
          f"(c) (i) ({means[3]:.0f} - {means[2]:.0f}) / (6 - 4) = {rate:.0f} thousand cells per milliliter per day. (ii) The population levels off at about 740 thousand cells per milliliter, so the carrying capacity is about 740.\n\n"
          "(d) The carrying capacity would increase. The carrying capacity is the number of cells that the available resources can support, and doubling the volume of the medium doubles the amount of sugar that is available, so more yeast cells can be supported.",
          diagram=table(["Time (days)", "Mean number of yeast cells (thousands per milliliter, n = 4)", "Standard error"], rows, caption="Yeast in flasks with a limited amount of sugar", row_headers=True))

    # ------------------------------------------------------------------ INVESTIGATION (4): phosphate and algae
    B.frq(7, "INVESTIGATION",
          "Runoff from farm fields can carry the nutrient phosphate into ponds. A student hypothesizes that adding phosphate to pond water causes the growth of algae to increase. The student fills eight clear jars with the same volume of water from a pond, adds phosphate to four of the jars, and adds nothing to the other four jars. The jars are kept in the same place in the light for 10 days, and the student then measures the amount of chlorophyll in the water of each jar as a measure of the amount of algae.\n\n"
          "**(a)** **Identify** the dependent variable in the investigation. (1 point)\n\n"
          "**(b)** **Identify** the negative control in the investigation. (1 point)\n\n"
          "**(c)** **Predict** the results for the jars with phosphate compared with the control jars. (1 point)\n\n"
          "**(d)** **Justify** your prediction. (1 point)",
          [(1, "(a) Identifies the dependent variable as the amount of chlorophyll in the water (the amount of algae)."),
           (1, "(b) Identifies the negative control as the jars that have the same pond water, with no phosphate added."),
           (1, "(c) Predicts that the jars with phosphate will contain more chlorophyll (more algae) than the control jars."),
           (1, "(d) Justifies: phosphate is a nutrient that limits the growth of producers, so adding it allows the algae to grow and reproduce more, which increases the amount of algae (an algal bloom).")],
          "(a) The dependent variable is the amount of chlorophyll in the water of each jar, which measures the amount of algae.\n\n"
          "(b) The negative control is the four jars of pond water to which no phosphate was added.\n\n"
          "(c) The jars with phosphate will have more chlorophyll than the control jars.\n\n"
          "(d) Phosphate is a nutrient that limits the growth of algae. When it is added, the algae can grow and reproduce more, so there are more algae, and so more chlorophyll, in the jars with phosphate.")

    # ------------------------------------------------------------------ CONCEPT (4): keystone sea star
    B.frq(6, "CONCEPT",
          "On a rocky shore, mussels compete with many other species for space on the rocks. A sea star eats the mussels, and the shore has 15 species. Researchers remove the sea star from part of the shore, and after a year the number of species there is 8.\n\n"
          "**(a)** **Describe** what is meant by a keystone species. (1 point)\n\n"
          "**(b)** **Explain** why an ecosystem that has more species is usually more resilient to a disturbance than an ecosystem that has fewer species. (1 point)\n\n"
          "**(c)** **Predict** how the abundance of the mussels will change in the part of the shore from which the sea star was removed. (1 point)\n\n"
          "**(d)** **Justify** your prediction, and use it to explain the decrease in the number of species. (1 point)",
          [(1, "(a) Describes that a keystone species is a species that has an effect on its ecosystem that is much greater than its abundance would suggest, so its removal often changes or collapses the ecosystem."),
           (1, "(b) Explains that an ecosystem with more species and more variety among its parts is more likely to contain species or populations that can withstand a disturbance, and the loss of one part is less damaging (an ecosystem with few, similar parts is less resilient)."),
           (1, "(c) Predicts that the abundance of the mussels will increase."),
           (1, "(d) Justifies: without the predator the mussels are no longer eaten, so they multiply and outcompete other species for space on the rocks, which drives out those species and reduces the number of species.")],
          "(a) A keystone species is a species whose effect on its ecosystem is much greater than its abundance would suggest. When it is removed, the ecosystem often changes a great deal or collapses.\n\n"
          "(b) An ecosystem with more species has more varied parts, so it is more likely to contain species that can withstand a disturbance. The loss of one species then does less harm to the whole ecosystem.\n\n"
          "(c) The abundance of the mussels will increase.\n\n"
          "(d) The sea star ate the mussels. Without it, the mussels are not eaten, so they increase in number and take over the space on the rocks. They outcompete the other species for space, so those species disappear and the number of species falls from 15 to 8.")

    # ------------------------------------------------------------------ MODEL (4): energy pyramid
    levels = [("Producers", 20000), ("Primary consumers", 2000), ("Secondary consumers", 200), ("Tertiary consumers", 20)]
    pct = levels[2][1] / levels[1][1] * 100
    assert pct == 10.0
    half = levels[3][1] * 0.5
    assert half == 10.0
    rows = [(a_, f"{b_:,}") for a_, b_ in levels]
    B.frq(2, "MODEL",
          "The table is a model of the energy that is available in each trophic level of a grassland ecosystem in one year. The energy that is stored in the tissues of the organisms of each level is shown in kilojoules (kJ) per square meter.\n\n"
          "**(a)** **Explain** why the producers have the greatest amount of energy in the model. (1 point)\n\n"
          "**(b)** **Calculate** the percent of the energy of the primary consumers that is available to the secondary consumers. (1 point)\n\n"
          "**(c)** **Explain** why the energy decreases from one trophic level to the next, although matter is recycled in the ecosystem. (1 point)\n\n"
          "**(d)** A drought reduces the energy that is captured by the producers to half of the value in the model. **Predict** the energy that will be available to the tertiary consumers, if the percent of the energy that is passed on at each transfer is the same, and **justify** your prediction. (1 point)",
          [(1, "(a) Explains that producers (autotrophs) capture the energy from sunlight (or from inorganic molecules), so all of the energy of the other trophic levels comes from them."),
           (1, "(b) Calculates 200 / 2,000 x 100 = 10 percent."),
           (1, "(c) Explains that at each transfer a large part of the energy is lost as heat (through cellular respiration and the activities of the organisms) or is not eaten, and energy flows through the ecosystem and is not recycled, but matter and nutrients cycle."),
           (1, "(d) Predicts 10 kJ per square meter, and justifies it: the energy of each level depends on the energy of the level below it, so if the producers capture half as much, every level has half as much (20 x 0.5 = 10 kJ).")],
          "(a) The producers capture the energy from sunlight and make organic compounds. All of the energy that the other trophic levels have comes from the producers, so the producers have the most.\n\n"
          "(b) 200 / 2,000 x 100 = 10 percent.\n\n"
          "(c) At each transfer, most of the energy is lost as heat from cellular respiration or is not consumed, and energy flows through the ecosystem and cannot be reused, so less is left at each level. Matter and nutrients are recycled by decomposers, so matter is not lost in the same way.\n\n"
          "(d) The tertiary consumers will have about 10 kJ per square meter. The energy at each level depends on the energy of the level below it, so if the producers capture half as much energy, each level has half as much, and 20 x 0.5 = 10 kJ.",
          diagram=table(["Trophic level", "Energy stored (kJ per square meter per year)"], rows, caption="Energy at four trophic levels of a grassland", row_headers=True))

    # ------------------------------------------------------------------ DATA (4): Simpson's index
    p1 = [40, 30, 15, 10, 5]
    p2 = [70, 10, 10, 5, 5]

    def simpson(counts):
        t = sum(counts)
        return 1 - sum((c / t) ** 2 for c in counts)
    d1, d2 = simpson(p1), simpson(p2)
    assert (round(d1, 3), round(d2, 3)) == (0.715, 0.485)
    rows = [(f"Species {i + 1}", str(a_), str(b_)) for i, (a_, b_) in enumerate(zip(p1, p2))] + [("Total", str(sum(p1)), str(sum(p2)))]
    B.frq(5, "DATA",
          "Researchers counted the trees of five species in two plots of a forest. Simpson's diversity index is 1 minus the sum of (n / N) squared for all of the species, where n is the number of individuals of one species and N is the total number of individuals of all species. The table shows the counts.\n\n"
          "**(a)** **Describe** one difference between the two plots in the way that the individuals are distributed among the species. (1 point)\n\n"
          "**(b)** **Calculate** Simpson's diversity index for plot 1. Give your answer to the nearest 0.01. (1 point)\n\n"
          "**(c)** A student claims that the diversity of plot 2 is higher than the diversity of plot 1, because plot 2 has a species with the most individuals. **Evaluate** the claim using the index of plot 2, which is 0.49. (1 point)\n\n"
          "**(d)** **Predict** how the index of plot 1 would change if an invasive species spread until it made up most of the individuals in the plot, and **explain** your prediction. (1 point)",
          [(1, "(a) Describes that in plot 1 the individuals are spread more evenly among the species, but in plot 2 one species has most of the individuals (70 of 100)."),
           (1, "(b) Calculates 1 - (0.40² + 0.30² + 0.15² + 0.10² + 0.05²) = 1 - 0.285 = 0.72 (accept 0.71 to 0.72)."),
           (1, "(c) Evaluates the claim as not supported, using data: the index of plot 2 (0.49) is lower than the index of plot 1 (0.72), so plot 2 is less diverse, because one species dominates."),
           (1, "(d) Predicts that the index would decrease, and explains that when one species makes up most of the individuals, the sum of (n / N) squared rises, so the index falls (the community is less even).")],
          "(a) In plot 1 the individuals are spread more evenly among the five species. In plot 2 one species has most of the individuals: 70 of the 100.\n\n"
          f"(b) 1 - (0.40² + 0.30² + 0.15² + 0.10² + 0.05²) = 1 - 0.285 = {d1:.3f}, which is about 0.72.\n\n"
          f"(c) The claim is not supported. The index of plot 2 is {d2:.2f}, which is lower than the index of plot 1 ({d1:.2f}), so plot 2 is less diverse. One species with most of the individuals makes the community less even and so less diverse.\n\n"
          "(d) The index of plot 1 would decrease. If an invasive species makes up most of the individuals, then its (n / N) squared becomes large, so the sum of the squares rises and the index falls, which means that the plot is less diverse.",
          diagram=table(["Species", "Plot 1: number of trees", "Plot 2: number of trees"], rows, caption="Trees of five species in two plots", row_headers=True))
