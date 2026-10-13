"""Unit 8, topics 8.1 Responses to the Environment (9 questions) and 8.2 Energy Flow Through Ecosystems (14).

Required content (CED 2025-26): 8.1.A organisms respond to changes in the environment through behavioral and physiological mechanisms (specific mechanisms excluded); organisms exchange information in response
to internal changes and external cues; 8.1.B organisms communicate by visual, audible, tactile, electrical or chemical signals that change the behavior of others and affect reproductive success (animals signal
dominance, food, territory, reproduction; specific mechanisms excluded); fitness favors innate and learned behaviors; cooperative behavior tends to raise individual fitness and population survival. 8.2.A organisms
use energy to organize, grow, reproduce and maintain homeostasis (endotherms and ectotherms); net gain and net loss of energy; reproductive strategies and energy availability (alternating asexual and sexual
reproduction); 8.2.B levels of organization (populations, communities, ecosystems, biomes), energy flows and matter cycles (hydrologic, carbon, nitrogen, phosphorus cycles); 8.2.C changes in energy availability
change populations and trophic levels; 8.2.D autotrophs (photosynthetic and chemosynthetic) and heterotrophs. Suggested skills: 3.C, 6.D. Not tested: specific behavioral or physiological mechanisms.
"""
from lib import *


def build(B):
    # ------------------------------------------------------------------ 8.1 Responses to the environment
    T = 1
    B.mcq(T, "A houseplant on a windowsill grows toward the light from the window. Which statement correctly describes this response?",
          ch("It is a physiological response of the plant to an external cue, and it helps the plant to capture more energy from light.", "Organisms respond to changes in their environment through behavioral and physiological mechanisms, such as phototropism."),
          [ch("It is a genetic change in the plant, and it is passed on to the seeds as soon as the stem has bent toward the window in the room.", "A bend in a stem during its life is a response of the individual and does not change the genes."),
           ch("It is a response to an internal cue only, because plants cannot detect anything that is outside of their own cells.", "Plants respond to external cues such as light."),
           ch("It is a random movement of the plant, and it has no effect on the amount of light that the leaves can capture.", "Phototropism is a response to a cue, and it increases the light captured.")],
          "Organisms respond to environmental cues through physiological and behavioral mechanisms.", difficulty="easy")

    B.mcq(T, "Female moths release a chemical that males detect from far away, and the males fly toward the source of the chemical. Which type of signal is this?",
          ch("A chemical signal, because the information passes between the moths in the form of molecules that the receiving moths detect.", "Organisms communicate through visual, audible, tactile, electrical and chemical signals."),
          [ch("A visual signal, because the male moths can see the female moths over a large distance in the dark.", "No light is involved. The signal is a chemical."),
           ch("An audible signal, because the male moths hear the female moths calling to them from a distance.", "No sound is involved. The signal is a chemical."),
           ch("A tactile signal, because the male moths touch the female moths before they begin to fly toward them.", "The male moths respond from a distance, without touching.")],
          "Organisms communicate through chemical signals, among others.", difficulty="easy")

    B.mcq(T, "A male songbird sings from a perch at the edge of its area, and other males that hear the song stay away. Which statement best explains the value of the song to the singing bird?",
          ch("It is a signal that establishes a territory, and it increases the reproductive success of the singer by reducing conflict over resources.", "Animals use signals to indicate dominance, find food, establish territory and ensure reproductive success."),
          [ch("It is a signal that increases the number of competitors in the area, and so it increases the number of mates that are available to the singer.", "The song keeps other males away."),
           ch("It is a random sound that has no effect on the behavior of other birds, and so it does not affect the fitness of the singer.", "The song changes the behavior of the other males."),
           ch("It is a response to an internal cue only, so that it cannot change the behavior of any other bird in the area.", "The song is a signal that causes a change in the behavior of the others.")],
          "Signals produce changes in the behavior of others and can affect reproductive success.", difficulty="medium")

    B.mcq(T, "Which statement best explains why certain innate and learned behaviors are common in a population?",
          ch("Individuals with behaviors that increase survival and reproductive success leave more offspring, so fitness favors those behaviors.", "Fitness favors innate and learned behaviors that increase survival and reproductive success."),
          [ch("Individuals choose behaviors that they need, and the behaviors then change the genes that are passed on to their offspring.", "Behaviors that individuals choose do not change the genes that they pass on."),
           ch("Behaviors have no effect on the number of offspring that an individual leaves, and so they are not affected by natural selection.", "Behaviors affect survival and reproduction, and so selection acts on them."),
           ch("Behaviors that are learned can never be favored by selection, because only innate behaviors can affect the fitness of an individual.", "Both innate and learned behaviors can affect fitness.")],
          "Fitness favors behaviors that increase survival and reproduction.", difficulty="medium")

    B.mcq(T, "Some meerkats in a group act as sentinels that watch for predators while the other meerkats feed. Which statement best explains how this cooperative behavior can be favored?",
          ch("Cooperative behavior tends to increase the fitness of the individual and the survival of the population, because the whole group is warned of danger.", "Cooperative behavior tends to increase the fitness of the individual and the survival of the population."),
          [ch("Cooperative behavior reduces the survival of the group, but it is favored because the sentinels like to be at a high place.", "Cooperative behavior is favored because it increases survival, not because of preference."),
           ch("Cooperative behavior is not inherited in any way, and so it cannot be favored by natural selection in a group of meerkats.", "Behaviors can have a genetic basis and be affected by selection."),
           ch("Cooperative behavior benefits only the sentinels, because the other meerkats do not receive any information from them.", "The other meerkats are warned by the sentinel.")],
          "Cooperative behavior tends to increase fitness and population survival.", difficulty="medium")

    B.mcq(T, "A student wants to test whether pillbugs prefer moist or dry conditions. The student puts pillbugs in a chamber that has a moist side and a dry side, and counts the pillbugs on each side after 10 minutes. Which setup is the most appropriate control?",
          ch("A chamber with both sides dry, so that any preference for one side that is not caused by moisture can be detected.", "A control with the same conditions on both sides shows whether the pillbugs prefer one side for another reason."),
          [ch("A chamber with a moist side and a dry side, with pillbugs that have been left without food for a longer time.", "This changes another variable, and it is not a control for the effect of moisture."),
           ch("A chamber with a moist side and a dry side, with a larger number of pillbugs and a longer time for the test.", "This changes the number of pillbugs and the time, and it does not show the baseline."),
           ch("A chamber that has no pillbugs in it, with a moist side and a dry side, to measure the humidity of each side of the chamber.", "A chamber without animals cannot show how the animals behave.")],
          "A control keeps all conditions the same except the variable that is tested.", difficulty="medium")

    counts = [("0", 10, 10), ("2", 14, 6), ("4", 17, 3), ("6", 18, 2)]
    pct_moist = 18 / 20 * 100
    assert pct_moist == 90.0
    rows = [(t_, str(m_), str(d_)) for t_, m_, d_ in counts]
    B.mcq(T, "A student placed 20 pillbugs in a chamber with a moist side and a dry side, and counted the pillbugs on each side at intervals. The table shows the results. Which statement is best supported by the data?",
          ch(f"The pillbugs responded to the moisture by moving to the moist side, and {pct_moist:.0f}% of them were on that side after 6 minutes.", "18 of 20 pillbugs, which is 90%, were on the moist side at the end of the test."),
          [ch("The pillbugs did not respond to the moisture, because some of them were still on the dry side after 6 minutes.", "The number on the dry side fell steadily. A response does not need all of the pillbugs to move."),
           ch("The pillbugs responded to the moisture by moving to the dry side, because the number of pillbugs on that side increased.", "The number of pillbugs on the dry side decreased."),
           ch("The pillbugs started on the moist side, because 10 of the 20 pillbugs were on each side at the start of the test.", "10 on each side at the start shows that the pillbugs were spread evenly across the two sides.")],
          "A change in the distribution of organisms between two conditions shows a behavioral response.",
          diagram=table(["Time (minutes)", "Pillbugs on the moist side", "Pillbugs on the dry side"], rows, caption="Position of 20 pillbugs in a choice chamber", row_headers=True), difficulty="hard")

    B.mcq(T, "During a drought, a plant closes the small openings in its leaves and loses less water. Which term best describes this response?",
          ch("A physiological response of the organism to a change in its external environment, which helps the organism to survive.", "Organisms respond to changes in the environment through behavioral and physiological mechanisms."),
          [ch("A behavioral response of the plant that was learned from other plants in the same field during earlier seasons.", "Plants do not learn behaviors from other plants."),
           ch("A mutation of the genes of the plant that occurred because the plant needed to lose less water during the drought.", "The response occurs in the individual and is not a mutation."),
           ch("A response that has no effect on the survival of the plant, because the plant loses the same amount of water as before.", "Closing the openings reduces water loss.")],
          "Physiological responses help organisms to cope with changes in the environment.", difficulty="medium")

    n_flies, n_a, n_b = 50, 40, 10
    exp_each = n_flies / 2
    chi = (n_a - exp_each) ** 2 / exp_each + (n_b - exp_each) ** 2 / exp_each
    assert (exp_each, chi) == (25.0, 18.0) and chi > 3.84
    B.mcq(T, f"A scientist places {n_flies} fruit flies in a chamber with an odor A on one side and an odor B on the other side. After 10 minutes, {n_a} flies are on the side of odor A and {n_b} flies are on the side of odor B. If the flies have no preference, 25 flies are expected on each side. The chi-square value is {chi:.1f}, and the critical value for 1 degree of freedom at p = 0.05 is 3.84. Which conclusion is best supported?",
          ch("The null hypothesis of no preference is rejected, because the chi-square value is greater than the critical value, so the flies prefer the odor A.", "A chi-square value greater than the critical value means that the difference from the expected counts is unlikely to be due to chance."),
          [ch("The null hypothesis of no preference cannot be rejected, because the chi-square value is greater than the critical value of 3.84 for 1 degree of freedom.", "A value that is greater than the critical value leads to rejection."),
           ch("The flies prefer the odor B, because there are 10 flies on the side of odor B, which is fewer than the number expected.", "Fewer flies than expected on that side means that the flies avoid it."),
           ch("The flies have no preference, because the expected count on each side is the same and so the result cannot show a preference.", "The expected counts are the counts under the null hypothesis, and the observed counts differ from them.")],
          "Compare chi-square with the critical value to reject or fail to reject the null hypothesis.", difficulty="hard")

    # ------------------------------------------------------------------ 8.2 Energy flow through ecosystems
    T = 2
    B.mcq(T, "Which statement correctly compares endotherms and ectotherms?",
          ch("Endotherms use thermal energy generated by their metabolism to keep a steady body temperature, and ectotherms rely on behaviors such as moving into the sun or shade.", "Endotherms maintain homeostatic body temperatures with thermal energy from metabolism, and ectotherms lack efficient internal mechanisms."),
          [ch("Ectotherms use thermal energy generated by their metabolism to keep a steady body temperature, and endotherms rely on the temperature of their surroundings and on their behavior.", "This reverses the two terms."),
           ch("Endotherms and ectotherms both keep a steady body temperature by using the same amount of energy, which is independent of the environment.", "Endotherms use much more energy to keep their body temperature steady."),
           ch("Endotherms are found only in cold environments, and ectotherms are found only in warm environments, and neither of them uses energy.", "Both kinds of organism use energy, and they live in many environments.")],
          "Endotherms regulate body temperature with metabolic heat; ectotherms do so mostly through behavior.", difficulty="easy")

    B.mcq(T, "An animal takes in more energy in its food than it uses. Which result is most likely?",
          ch("The surplus energy is stored in the body, the animal can grow, and its reproductive output can increase.", "A net gain in energy results in energy storage, growth and increased reproductive output."),
          [ch("The animal loses mass, and its reproductive output decreases, because extra food is always lost as heat.", "A net loss of energy, and not a net gain, causes a loss of mass."),
           ch("The animal stays the same mass, and its reproductive output does not change, because energy is never stored in the body.", "A net gain in energy can be stored and used for growth."),
           ch("The animal dies, because taking in more energy than is used always leads to the death of an organism.", "A net loss of energy can eventually lead to death.")],
          "A net gain in energy results in storage, growth and increased reproduction.", difficulty="easy")

    B.mcq(T, "Some organisms reproduce asexually when food is plentiful and sexually when food is scarce. Which statement best describes this strategy?",
          ch("Organisms use different reproductive strategies in response to the availability of energy, and some alternate between asexual and sexual reproduction.", "Different organisms use various reproductive strategies in response to energy availability."),
          [ch("The organisms choose the type of reproduction by thinking about their future, and then their cells change their genes.", "Organisms do not choose by thinking about the future, and the response is not a change in the genes."),
           ch("The organisms use the same type of reproduction in every environment, because reproduction is not affected by energy.", "Reproduction does respond to the availability of energy."),
           ch("The organisms reproduce sexually when food is plentiful, because asexual reproduction needs much more energy than sexual reproduction does in these organisms.", "The pattern in the question is the opposite.")],
          "Reproductive strategies can respond to the availability of energy.", difficulty="medium")

    B.mcq(T, "Which list arranges the ecological levels of organization from the smallest to the largest?",
          ch("Population, community, ecosystem, biome", "The ecological levels of organization include populations, communities, ecosystems and biomes."),
          [ch("Community, population, biome, ecosystem", "A population is smaller than a community, and an ecosystem is smaller than a biome."),
           ch("Ecosystem, community, population, biome", "An ecosystem includes communities, which include populations."),
           ch("Biome, ecosystem, community, population", "This list is arranged from the largest to the smallest.")],
          "Levels of organization: population, community, ecosystem, biome.", difficulty="easy")

    B.mcq(T, "Which statement correctly describes the movement of energy and matter in an ecosystem?",
          ch("Energy flows through the ecosystem and is lost as heat, but matter and nutrients cycle between organisms and the environment.", "Energy flows through ecosystems, while matter and nutrients cycle between the environment and organisms."),
          [ch("Matter flows through the ecosystem and is lost as heat, but energy and nutrients cycle between organisms and the environment.", "This reverses the roles of energy and matter."),
           ch("Both energy and matter cycle between the organisms and the environment and none of them is lost from the ecosystem.", "Energy is lost as heat and has to be supplied again, for example by the sun."),
           ch("Both energy and matter flow in a single direction through the ecosystem, and neither of them is used again by organisms.", "Matter is recycled by biogeochemical cycles.")],
          "Energy flows; matter cycles.", difficulty="easy")

    B.mcq(T, "Which of the following processes returns carbon from organisms to the atmosphere as carbon dioxide?",
          ch("Cellular respiration, decomposition, and combustion, which release the carbon of organic compounds into the air as CO₂", "At the highest level, the carbon cycle involves photosynthesis, cellular respiration, decomposition and combustion."),
          [ch("Photosynthesis, which takes in CO₂ and releases the carbon in the atmosphere as carbohydrates in the leaves of plants", "Photosynthesis removes CO₂ from the atmosphere."),
           ch("Nitrogen fixation, which converts carbon dioxide into ammonia that the roots of plants are able to take up from the soil", "Nitrogen fixation is part of the nitrogen cycle and not the carbon cycle."),
           ch("Precipitation, which carries carbon dioxide from the atmosphere into the surface water of the oceans and the lakes", "Precipitation is part of the water cycle.")],
          "The carbon cycle: photosynthesis, cellular respiration, decomposition, combustion.", difficulty="medium")

    B.mcq(T, "Which process in the nitrogen cycle converts nitrogen gas (N₂) from the atmosphere into ammonia (NH₃)?",
          ch("Nitrogen fixation, which is performed by microorganisms in the soil, and the ammonia that is formed then ionizes to ammonium.", "In nitrogen fixation, N₂ is fixed into ammonia, which ionizes to ammonium."),
          [ch("Denitrification, which is performed by microorganisms in the soil, and which returns nitrogen to the atmosphere as nitrogen gas.", "Denitrification returns nitrogen gas to the atmosphere."),
           ch("Nitrification, which is performed by microorganisms in the soil, and which converts ammonium into nitrite and then into nitrate.", "Nitrification converts ammonium to nitrates."),
           ch("Assimilation, which is performed by the roots of plants, and which converts the nitrogen gas in the air into amino acids.", "Assimilation is the uptake of nitrogen compounds from the soil by plants.")],
          "Nitrogen fixation converts N₂ to ammonia.", difficulty="medium")

    B.mcq(T, "Which sequence of steps of the nitrogen cycle correctly describes what happens to nitrogen in dead organic matter in the soil?",
          ch("Ammonification of the organic matter produces ammonium, nitrification converts it to nitrate, and plants assimilate the nitrate.", "The nitrogen cycle includes fixation, assimilation, ammonification, nitrification and denitrification, performed by microorganisms in the soil."),
          [ch("Nitrification of the organic matter produces ammonia, ammonification converts it to nitrogen gas, and plants fix the nitrogen gas.", "The steps are not in this order, and plants do not fix nitrogen gas."),
           ch("Denitrification of the organic matter produces nitrate, fixation converts it to ammonium, and plants assimilate the ammonium gas.", "Denitrification returns nitrogen gas to the atmosphere."),
           ch("Assimilation of the organic matter by microorganisms produces nitrogen gas, which is then used directly by animals as food.", "Animals do not use nitrogen gas as food.")],
          "Ammonification releases ammonium, nitrification makes nitrate, and plants assimilate it.", difficulty="medium")

    B.mcq(T, "Which statement correctly describes the phosphorus cycle?",
          ch("Weathering of rocks releases phosphate into the soil, producers take it up, consumers obtain it from producers, and decomposition returns it to the soil.", "In the phosphorus cycle, phosphate from weathered rocks is taken up by producers, passed to consumers, and returned to the soil by decomposition and excretion."),
          [ch("Phosphorus gas in the atmosphere is fixed by bacteria in the soil, and the phosphorus gas is then taken up by the producers.", "The phosphorus cycle does not have a large atmospheric reservoir."),
           ch("Phosphate is made by photosynthesis in the leaves of producers, and then it is released into the air by the cells of consumers.", "Phosphate is not made by photosynthesis."),
           ch("Phosphate is removed from the biosphere by the cells of decomposers, which keep it in their tissues and never release it.", "Decomposers return phosphate to the soil.")],
          "The phosphorus cycle moves phosphate from rocks to soil, producers, consumers, and back to the soil.", difficulty="medium")

    B.mcq(T, "Which list contains only processes of the hydrologic (water) cycle?",
          ch("Evaporation, condensation, precipitation, and transpiration", "The processes of the water cycle include evaporation, condensation, precipitation and transpiration."),
          [ch("Evaporation, nitrification, precipitation, and combustion", "Nitrification and combustion are not processes of the water cycle."),
           ch("Condensation, photosynthesis, denitrification, and transpiration", "Photosynthesis and denitrification are not processes of the water cycle."),
           ch("Precipitation, weathering of rocks, ammonification, and cellular respiration", "Ammonification and cellular respiration are not processes of the water cycle.")],
          "Water cycle processes: evaporation, condensation, precipitation, transpiration.", difficulty="medium")

    prod, eff = 10000, 0.10
    levels = [prod * eff ** i for i in range(4)]
    assert levels == [10000, 1000.0, 100.0, 10.0] or [round(x, 6) for x in levels] == [10000, 1000, 100, 10]
    secondary = prod * eff * eff
    assert round(secondary) == 100
    B.mcq(T, f"Producers in an ecosystem capture {prod:,} kJ of energy. Assume that {int(eff * 100)}% of the energy of each trophic level is transferred to the next level. How much energy is available to the secondary consumers?",
          ch(f"About {secondary:,.0f} kJ, because {prod:,} kJ is reduced to 10% twice, first for the primary consumers and then for the secondary consumers.", f"{prod:,} x 0.10 x 0.10 = {secondary:,.0f} kJ.", round(secondary)),
          [ch(f"About {prod * eff:,.0f} kJ, because {int(eff * 100)}% of the energy of the producers is available to the secondary consumers.", "1,000 kJ reaches the primary consumers. The secondary consumers receive 10% of that.", round(prod * eff)),
           ch(f"About {prod * eff ** 3:,.0f} kJ, because the energy is reduced to 10% three times before it reaches the secondary consumers.", "There are only two transfers from the producers to the secondary consumers.", round(prod * eff ** 3)),
           ch(f"About {prod * (1 - eff) ** 2:,.0f} kJ, because 90% of the energy is kept at each transfer between the trophic levels.", "Only 10% of the energy is transferred, and 90% is not kept.", round(prod * (1 - eff) ** 2))],
          "Energy decreases at each transfer between trophic levels.", difficulty="medium")

    B.mcq(T, "A drought reduces the biomass of the producers in a grassland by 40%. Which prediction about the other trophic levels is the most reasonable?",
          ch("The number and size of the primary consumers and of the higher trophic levels will probably decrease, because less energy is available to them.", "A change in the biomass of producers affects the number and size of the other trophic levels."),
          [ch("The primary consumers will increase in number, because the producers are fewer and so they are easier to find and eat.", "Fewer producers means less food for the primary consumers."),
           ch("The higher trophic levels will not be affected, because the energy they use does not come from the producers at all.", "The energy in the higher trophic levels comes from the producers."),
           ch("The decomposers will disappear, because they depend on the sunlight that the producers capture in their cells.", "Decomposers feed on dead organic matter and do not capture sunlight.")],
          "A change in the biomass of producers affects the other trophic levels.", difficulty="hard")

    B.mcq(T, "Bacteria near a deep-sea hydrothermal vent make organic compounds from hydrogen sulfide, without using light or oxygen. Which term describes these organisms?",
          ch("Chemosynthetic autotrophs, because they capture energy from small inorganic molecules found in their environment.", "Chemosynthetic organisms capture energy from small inorganic molecules and can do so in the absence of oxygen."),
          [ch("Photosynthetic autotrophs, because they capture the energy that is present in sunlight and so they contribute to primary productivity.", "No light reaches the vents, so the energy is not from sunlight."),
           ch("Heterotrophs, because they obtain their energy by consuming organic matter that is derived from other organisms.", "These bacteria make their own organic compounds."),
           ch("Decomposers, because they obtain energy from dead organisms and so they return nutrients to the soil of the ocean floor.", "These bacteria obtain energy from inorganic molecules.")],
          "Chemosynthetic organisms capture energy from inorganic molecules.", difficulty="medium")

    B.mcq(T, "Which statement correctly describes how heterotrophs obtain energy?",
          ch("They consume organic matter derived from autotrophs and metabolize its carbohydrates, lipids and proteins as sources of energy.", "Heterotrophs capture the energy present in carbon compounds by consuming organic matter."),
          [ch("They capture the energy from sunlight or from inorganic molecules, and use it to make their own organic compounds from CO₂.", "This describes autotrophs."),
           ch("They make carbohydrates from carbon dioxide and water, and they release oxygen as a product of the reactions that they carry out.", "This describes photosynthesis in autotrophs."),
           ch("They take in energy from the soil as heat, and they store the heat in their tissues as a source of energy for their cells.", "Heterotrophs obtain the chemical energy of organic compounds and not heat.")],
          "Heterotrophs metabolize the organic matter that they consume.", difficulty="medium")
