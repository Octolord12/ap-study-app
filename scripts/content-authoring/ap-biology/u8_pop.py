"""Unit 8, topics 8.3 Population Ecology (9 questions) and 8.4 Effect of Density on Populations (8).

Required content (CED 2025-26): 8.3.A populations are individuals of the same species that interact with one another and with the environment; many adaptations relate to obtaining and using energy and matter in a
particular environment; growth dynamics depend on birth rate, death rate and population size, dN/dt = B - D; reproduction without constraints gives exponential growth, dN/dt = rmax N. 8.4.A carrying capacity is the
sustainable abundance of a species that the available resources can support; density-dependent and density-independent limits give logistic growth, dN/dt = rmax N (K - N) / K. Suggested skills: 4.A, 5.A.
"""
from lib import *


def build(B):
    # ------------------------------------------------------------------ 8.3 Population ecology
    T = 3
    B.mcq(T, "Which description correctly defines a population in ecology?",
          ch("A group of individuals of the same species that live in the same area and that interact with each other and with their environment", "Populations comprise individual organisms of the same species that interact with one another and with the environment."),
          [ch("A group of individuals of different species that live in the same area and that interact with each other and with their environment", "This describes a community."),
           ch("All of the living and nonliving things in an area, including the soil, the water, and the organisms that live in the area", "This describes an ecosystem."),
           ch("A group of individuals of the same species that live in different areas and that never interact with each other at all", "A population is a group of individuals that interact.")],
          "A population is a group of individuals of one species that interact in an area.", difficulty="easy")

    B_, D_ = 120, 80
    dn = B_ - D_
    assert dn == 40
    B.mcq(T, f"In one year, {B_} individuals are born into a population and {D_} individuals die. Ignoring migration, what is the change in the size of the population (dN) in that year?",
          ch(f"An increase of {dn} individuals, because dN = B - D = {B_} - {D_}.", f"The change in population size equals births minus deaths: {B_} - {D_} = {dn}.", dn),
          [ch(f"An increase of {B_ + D_} individuals, because the births and the deaths are both added to the size of the population.", "Deaths reduce the size of the population, so they are subtracted.", B_ + D_),
           ch(f"A decrease of {dn} individuals, because dN = D - B = {D_} - {B_} in a year in which the population is changing.", "The births exceed the deaths, so the population grows.", -dn),
           ch(f"An increase of {B_} individuals, because the change in the size of a population is equal to the number of births.", "Deaths must be subtracted from the births.", B_)],
          "dN/dt = B - D.", difficulty="medium")

    N, b, d = 500, 60, 20
    r = (b - d) / N
    assert r == 0.08
    B.mcq(T, f"A population of {N} mice has {b} births and {d} deaths in one year, and there is no migration. What is the per capita growth rate of the population per year?",
          ch(f"{r:.2f}, because the change in the size of the population ({b} - {d} = {b - d}) is divided by the number of mice ({N}).", f"({b} - {d}) / {N} = {r:.2f}.", r),
          [ch(f"{b - d}, because the per capita growth rate is the difference between the number of births and the number of deaths.", "That is the change in the size of the population. The per capita rate is divided by the size of the population.", float(b - d)),
           ch(f"{b / N:.2f}, because the per capita growth rate is the number of births divided by the size of the population.", "The deaths must be subtracted from the births before the rate is found.", round(b / N, 2)),
           ch(f"{(b + d) / N:.2f}, because the per capita growth rate is the sum of the births and the deaths divided by the size of the population.", "Deaths are subtracted from births and not added to them.", round((b + d) / N, 2))],
          "Per capita growth rate = (B - D) / N.", difficulty="medium")

    B.mcq(T, "A few bacteria are placed in a flask with plenty of nutrients, at a constant temperature, and the number of bacteria doubles every 20 minutes. Which model describes the growth of the population over the first few hours?",
          ch("Exponential growth, because reproduction without constraints makes the population increase by a constant fraction in each interval.", "Reproduction without constraints results in the exponential growth of a population."),
          [ch("Logistic growth, because the population is limited by the carrying capacity from the first minute of the experiment.", "The nutrients are plentiful at first, so the carrying capacity has no effect yet."),
           ch("Linear growth, because the same number of new bacteria is added in each interval of 20 minutes from the start to the end of the experiment.", "The number added grows, since each bacterium divides."),
           ch("No growth, because the number of births is equal to the number of deaths in the population at all times.", "The number doubles, so the births exceed the deaths.")],
          "Reproduction without constraints results in exponential growth.", difficulty="medium")

    N0, rmax = 200, 0.5
    rate = rmax * N0
    assert rate == 100
    B.mcq(T, f"A population of {N0} insects grows exponentially, with a maximum per capita growth rate (r max) of {rmax} per day. What is the rate of growth of the population (dN/dt) at this size?",
          ch(f"{rate:.0f} insects per day, because dN/dt = r max x N = {rmax} x {N0}.", f"dN/dt = {rmax} x {N0} = {rate:.0f}.", rate),
          [ch(f"{N0 + rmax:.1f} insects per day, because r max is added to the size of the population to find the rate of growth.", "The rate is the product of r max and N, not their sum.", N0 + rmax),
           ch(f"{N0 / rmax:.0f} insects per day, because the size of the population is divided by r max to find the rate of growth.", "The rate is the product of r max and N, not their ratio.", N0 / rmax),
           ch(f"{rmax:.1f} insects per day, because the rate of growth is equal to r max and does not depend on the size of the population.", "In exponential growth the rate depends on the size of the population.", rmax)],
          "Exponential growth: dN/dt = rmax N.", difficulty="medium")

    start, double_min, total_min = 100, 20, 120
    doublings = total_min // double_min
    final = start * 2 ** doublings
    assert (doublings, final) == (6, 6400)
    B.mcq(T, f"A culture starts with {start} bacteria, and the population doubles every {double_min} minutes without any limit. How many bacteria are in the culture after {total_min // 60} hours?",
          ch(f"{final:,}, because the population doubles {doublings} times in {total_min} minutes and {start} x 2⁶ = {final:,}.", f"{total_min} / {double_min} = {doublings} doublings, and {start} x 64 = {final:,}.", final),
          [ch(f"{start * doublings * 2:,}, because {start} bacteria are added in each interval of {double_min} minutes, which makes the growth linear.", "Each doubling adds more bacteria than the one before.", start * doublings * 2),
           ch(f"{start * 2 ** (doublings - 1):,}, because the population doubles only {doublings - 1} times, as the first interval is used to start the growth.", "The population doubles in each of the 6 intervals.", start * 2 ** (doublings - 1)),
           ch(f"{start * total_min:,}, because the number of bacteria is multiplied by the number of minutes that have passed.", "Doubling is repeated multiplication by 2, and not multiplication by the number of minutes.", start * total_min)],
          "Exponential growth: N = N0 x 2^(number of doublings).", difficulty="hard")

    B.mcq(T, "Desert plants called cacti have thick stems that store water and shallow roots that spread out widely. Which statement best describes these traits?",
          ch("They are adaptations to obtaining and using matter in a particular environment, because they let the plants take in and keep scarce water.", "Many adaptations in organisms are related to obtaining and using energy and matter in a particular environment."),
          [ch("They are traits that the cacti gained during their lives, because the cacti needed water, and they pass the new traits on to the seeds that they make.", "Traits gained during a life are not inherited."),
           ch("They are traits that have no relation to the environment, because cacti would look the same in any habitat.", "The traits match the dry environment."),
           ch("They are traits that reduce the survival of the cacti in the desert, but they are kept because they use less energy.", "The traits increase survival in the desert.")],
          "Adaptations relate to obtaining and using energy and matter in a particular environment.", difficulty="medium")

    rows = [("A", "300", "20", "20"), ("B", "150", "40", "25"), ("C", "250", "30", "45"), ("D", "400", "50", "50")]
    diff = {r_[0]: int(r_[2]) - int(r_[3]) for r_ in rows}
    assert diff == {"A": 0, "B": 15, "C": -15, "D": 0}
    B.mcq(T, "The table shows the number of births and deaths in one year in four populations, with no migration. Which population is expected to be larger next year than it is now?",
          ch("Population B, because its births (40) are greater than its deaths (25), so dN is positive.", "dN = B - D = 40 - 25 = +15, so the population grows."),
          [ch("Population C, because it is larger than population B at the start of the year, which gives it the larger growth.", "dN = 30 - 45 = -15. The population falls."),
           ch("Population A, because its birth rate and its death rate are equal, which gives a population that grows at a steady rate.", "Equal births and deaths mean that dN = 0, so the size of the population does not change."),
           ch("Population D, because it has the most births in the year, which makes it the fastest growing of the four populations.", "D has equal births and deaths (50 and 50), so it is stable.")],
          "A population grows when births exceed deaths.",
          diagram=table(["Population", "Size now", "Births in a year", "Deaths in a year"], rows, caption="Births and deaths in four populations", row_headers=True), difficulty="hard")

    days = [0, 1, 2, 3, 4]
    sizes = [100, 200, 400, 800, 1600]
    g = graph("Time (days)", "Number of individuals", 0, 4, 0, 1800,
              [line("Population size", list(zip(days, sizes)), "blue")],
              "Population size against time. It is 100 at day 0, 200 at day 1, 400 at day 2, 800 at day 3 and 1,600 at day 4.")
    avg = (sizes[4] - sizes[2]) / (days[4] - days[2])
    assert avg == 600
    B.mcq(T, "The graph shows the size of a population over four days. What is the average rate of growth of the population between day 2 and day 4?",
          ch(f"{avg:.0f} individuals per day, because the population changed from {sizes[2]} to {sizes[4]} in the 2 days from day 2 to day 4.", f"({sizes[4]} - {sizes[2]}) / (4 - 2) = {avg:.0f} individuals per day.", avg),
          [ch(f"{sizes[4] - sizes[2]:,} individuals per day, because that is the difference between the sizes of the population at the two times.", "That is the total change over 2 days. The rate is the change divided by the time.", sizes[4] - sizes[2]),
           ch(f"{(sizes[4] - sizes[0]) / 4:.0f} individuals per day, because the rate is found for the whole period from day 0 to day 4.", "The question asks for the rate between day 2 and day 4 only.", (sizes[4] - sizes[0]) / 4),
           ch(f"{sizes[4] / 4:.0f} individuals per day, because the size of the population at day 4 is divided by the number of days.", "The rate is found from the change in the size and not from the size at one time.", sizes[4] / 4)],
          "Rate = change in N divided by the change in time.", diagram=g, difficulty="hard")

    # ------------------------------------------------------------------ 8.4 Effect of density on populations
    T = 4
    B.mcq(T, "What is the carrying capacity (K) of a population in an ecosystem?",
          ch("The sustainable number of individuals of a species that the available resources of the ecosystem can support", "Carrying capacity is the sustainable abundance of a species that can be supported by the total available resources of the ecosystem."),
          [ch("The largest number of individuals that the species has ever reached in the ecosystem, even if only for a short time", "Carrying capacity is a sustainable number and not the largest number ever reached."),
           ch("The number of offspring that each female of the species can produce in a lifetime under the best conditions", "This describes the reproductive potential of an individual."),
           ch("The number of individuals that are born in each year in the population when there are no limits to its growth", "That describes births in exponential growth, and not the carrying capacity.")],
          "Carrying capacity is the sustainable abundance that the resources can support.", difficulty="easy")

    B.mcq(T, "When limits to growth are imposed by density-dependent and density-independent factors, which pattern of growth typically results?",
          ch("Logistic growth, in which the population grows quickly at first and then levels off as it approaches the carrying capacity.", "As limits to growth are imposed, a logistic growth model typically ensues."),
          [ch("Exponential growth, in which the population keeps growing by a constant fraction in each interval without ever leveling off.", "Exponential growth happens when there are no constraints."),
           ch("Linear growth, in which the population increases by the same number of individuals in each interval from the very start.", "Logistic growth is not linear."),
           ch("Steady decline, in which the population falls by a constant fraction in each interval until the species is extinct.", "Limits to growth lead to leveling off and not to a steady decline.")],
          "Limits to growth give logistic growth.", difficulty="medium")

    B.mcq(T, "Which of the following is a density-independent factor that limits the size of a population?",
          ch("A wildfire that burns an area and kills organisms regardless of how many of them there are", "A density-independent factor affects a population regardless of its density, such as a fire or a storm."),
          [ch("The spread of a disease that passes more easily between individuals when they are crowded together in the population", "The spread of a disease depends on density."),
           ch("Competition between individuals for a limited supply of food that becomes scarcer as the population gets larger", "Competition for resources depends on density."),
           ch("The build-up of waste products in the habitat as the number of individuals in the population increases over time", "The build-up of waste depends on density.")],
          "Density-independent factors act regardless of population density.", difficulty="medium")

    r_, N_, K_ = 0.4, 500, 1000
    rate = r_ * N_ * (K_ - N_) / K_
    assert rate == 100
    B.mcq(T, f"A population has a maximum per capita growth rate (r max) of {r_} per year and a carrying capacity (K) of {K_:,}. What is the rate of growth (dN/dt) of the population when N = {N_}?",
          ch(f"{rate:.0f} individuals per year, because the rate dN/dt = r max x N x (K - N) / K = {r_} x {N_} x {K_ - N_} / {K_:,}.", f"{r_} x {N_} x ({K_} - {N_}) / {K_} = {rate:.0f}.", rate),
          [ch(f"{r_ * N_:.0f} individuals per year, because the rate is the product of r max and N, as in exponential growth.", "This ignores the term (K - N) / K that slows the growth near the carrying capacity.", r_ * N_),
           ch(f"{r_ * N_ * K_ / (K_ - N_):.0f} individuals per year, because the term for the carrying capacity multiplies the rate of growth.", "The term is (K - N) / K, which is less than 1. It reduces the rate.", r_ * N_ * K_ / (K_ - N_)),
           ch(f"0 individuals per year, because the population is at half of its carrying capacity and so it stops growing.", "The growth stops at the carrying capacity (N = K) and not at half of it.", 0.0)],
          "Logistic growth: dN/dt = rmax N (K - N) / K.", difficulty="medium")

    K2 = 800
    B.mcq(T, f"A population shows logistic growth with a carrying capacity of {K2}. At what population size is the rate of growth (dN/dt) the highest?",
          ch(f"At {K2 // 2}, which is half of the carrying capacity, because the term N (K - N) / K is at its maximum at that size.", f"N (K - N) / K is largest at N = K / 2 = {K2 // 2}.", K2 // 2),
          [ch(f"At {K2}, which is the carrying capacity, because the population has the largest number of individuals that produce offspring.", "At N = K the growth rate is zero.", K2),
           ch("At a size close to 0, which is the start of the growth, because the population has the most resources for each individual.", "The rate is small when the population is small, as there are few individuals that reproduce.", 10),
           ch(f"At {K2 * 3 // 4}, which is three quarters of the carrying capacity, because the population grows by a constant fraction at that size.", "The rate is greatest at half of the carrying capacity.", K2 * 3 // 4)],
          "In logistic growth the rate of growth is highest at K / 2.", difficulty="hard")

    days = [0, 2, 4, 6, 8, 10, 12, 14]
    sizes = [20, 55, 150, 330, 560, 700, 740, 750]
    g = graph("Time (days)", "Number of yeast cells (in thousands)", 0, 14, 0, 900,
              [line("Yeast cells", list(zip(days, sizes)), "green")],
              "Number of yeast cells (in thousands) against time. It rises from 20 at day 0 to 330 at day 6, 700 at day 10, and then levels off at about 750 by day 14.")
    B.mcq(T, "The graph shows the growth of a yeast population in a flask with a fixed amount of sugar. Which statement is best supported by the graph?",
          ch("The growth is logistic, and the carrying capacity of the flask is about 750 thousand cells, where the growth levels off.", "The population grows quickly and then levels off, which shows a logistic pattern with a carrying capacity near 750."),
          [ch("The growth is exponential, and the population will keep growing at the same rate for as long as the flask is kept.", "The growth levels off after day 10, so it is not exponential."),
           ch("The growth is linear, because the number of cells that are added in each interval of two days is constant.", "The numbers added per interval change a lot over time."),
           ch("The population has no carrying capacity, because the number of cells at day 14 is greater than the number of cells at day 0.", "The leveling off shows a carrying capacity.")],
          "Logistic growth levels off at the carrying capacity.", diagram=g, difficulty="medium")

    B.mcq(T, "The yeast population in the flask levels off at its carrying capacity. Which factor most likely explains why the population stops growing?",
          ch("The sugar is used up and waste products build up as the density rises, which are density-dependent limits on the growth.", "As the density rises, resources decline and wastes build up, which limits the growth."),
          [ch("The yeast cells lose the ability to reproduce at a fixed time, which is independent of how crowded the flask is.", "The limit depends on the density of the cells and on the resources."),
           ch("The flask has too much sugar for the yeast cells, which makes them stop dividing at the same time in the culture.", "Too little sugar, not too much, limits the growth."),
           ch("The yeast cells change their genes in order to stop reproducing, because they know that the sugar will soon run out in the flask.", "Cells do not change their genes in response to a future shortage.")],
          "Density-dependent factors limit population growth.", difficulty="medium")

    B.mcq(T, "A drought reduces the food supply in the habitat of a population, so that the carrying capacity falls from 1,000 to 600 individuals. The population is at 900 individuals when the drought starts. Which prediction is the most reasonable?",
          ch("The population will decline toward the new carrying capacity, because the available resources can support fewer individuals.", "Carrying capacity is the abundance that the resources can support, so when it falls, the population falls."),
          [ch("The population will keep growing above 900 individuals, because the old carrying capacity of 1,000 stays in effect for the species.", "The carrying capacity depends on the present resources."),
           ch("The population will stay at 900 individuals, because the size of a population is not affected by the supply of food.", "The food supply sets the carrying capacity."),
           ch("The population will rise to 1,200 individuals, because the individuals that are left will have less competition for food.", "The food supply is smaller, so the population cannot rise above the carrying capacity.")],
          "When resources fall, carrying capacity falls and the population declines.", difficulty="medium")
