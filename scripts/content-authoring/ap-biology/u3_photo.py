"""Unit 3, topic 3.4 Photosynthesis (12 questions).

Required content (CED 2025-26): 3.4.A.1 CO2 + H2O + light -> carbohydrates + O2 (first evolved in prokaryotes; cyanobacterial photosynthesis produced an
oxygenated atmosphere); 3.4.A.2 stroma (Calvin cycle) and thylakoids/grana (light reactions); 3.4.A.3 light reactions yield ATP and NADPH; 3.4.B.1-6 ETC,
photosystems I and II, water splits to replace electrons lost from PSII, NADP+ reduced to NADPH at PSI, proton gradient (high inside the thylakoid, low
outside), chemiosmosis through ATP synthase (photophosphorylation), ATP and NADPH power the Calvin cycle in the stroma.
Excluded by the CED: the steps of the Calvin cycle, molecule structures, enzyme names (except ATP synthase), the names of the electron carriers.
Suggested skill 6.B: support a claim with evidence from principles, concepts, processes and data.
"""
from lib import *


def build(B):
    B.mcq(4, "Which choice correctly lists the inputs and the outputs of photosynthesis?",
          ch("Inputs: carbon dioxide, water and light energy. Outputs: carbohydrates and oxygen.", "Photosynthesis uses carbon dioxide, water and light energy to make carbohydrates and oxygen."),
          [ch("Inputs: oxygen and carbohydrates. Outputs: carbon dioxide, water and energy released.", "This reverses the process. It describes the overall inputs and outputs of aerobic cellular respiration."),
           ch("Inputs: carbon dioxide and oxygen. Outputs: water and light energy.", "Light energy is an input to photosynthesis, not an output, and oxygen is an output, not an input."),
           ch("Inputs: water and oxygen. Outputs: carbohydrates and carbon dioxide.", "Carbon dioxide is an input and oxygen is an output of photosynthesis.")],
          "Photosynthesis: CO₂ + H₂O + light energy gives carbohydrates + O₂.", difficulty="easy")

    B.mcq(4, "In a plant cell, where do the light reactions and the Calvin cycle of photosynthesis take place?",
          ch("The light reactions take place in the thylakoid membranes, and the Calvin cycle takes place in the stroma.", "The thylakoid membranes (stacked in grana) contain the photosystems and electron transport chain. The carbon fixation reactions of the Calvin cycle occur in the stroma."),
          [ch("The light reactions take place in the stroma, and the Calvin cycle takes place in the thylakoid membranes.", "This reverses the locations. The photosystems are in the thylakoid membranes."),
           ch("Both take place in the mitochondria, where the ATP is made.", "Photosynthesis takes place in chloroplasts. Mitochondria carry out cellular respiration."),
           ch("The light reactions take place in the cytosol, and the Calvin cycle takes place in the nucleus.", "Neither process takes place in the cytosol or nucleus of a plant cell. Both are in the chloroplast.")],
          "Light reactions: thylakoid membranes. Calvin cycle: stroma.", difficulty="easy")

    B.mcq(4, "A researcher supplies a photosynthesizing plant with water that contains the heavy oxygen isotope ¹⁸O and with carbon dioxide that contains only ordinary oxygen. In which molecule released by the plant would the ¹⁸O first be found?",
          ch("O₂, the oxygen gas", "Water is split in the light reactions, and the oxygen from the water is released as O₂."),
          [ch("CO₂, the carbon dioxide", "Carbon dioxide is an input of photosynthesis. The ¹⁸O in the water would not be released in carbon dioxide."),
           ch("Glucose, the carbohydrate", "Glucose is made from carbon dioxide in the Calvin cycle. The oxygen released as a gas is the oxygen from the water that is split in the light reactions."),
           ch("NADPH, which carries electrons to the Calvin cycle", "NADPH carries hydrogen and electrons, not oxygen atoms.")],
          "Water splitting in photosystem II is the source of the oxygen gas released in photosynthesis.", difficulty="medium")

    B.mcq(4, "In the light reactions, what is the immediate source of the electrons that replace those lost from photosystem II after it absorbs light?",
          ch("Water, which is split", "Water is split, supplying electrons to photosystem II and releasing oxygen as a product."),
          [ch("NADPH, which is produced from the light reactions", "NADPH is a product of the light reactions, not a source of electrons for photosystem II."),
           ch("Carbon dioxide, which enters the stroma", "Carbon dioxide is used in the Calvin cycle. It does not supply electrons to photosystem II."),
           ch("Photosystem I, which passes electrons back to photosystem II", "Electrons move from photosystem II to photosystem I through the electron transport chain, not the other way.")],
          "Water splits to replace the electrons that photosystem II loses when light excites chlorophyll.", difficulty="medium")

    B.mcq(4, "At the end of the electron transport chain of the light reactions, to what are the electrons ultimately transferred?",
          ch("NADP⁺, which is reduced to NADPH for use in the Calvin cycle", "In the light reactions, electrons passing through the thylakoid membrane are picked up and ultimately transferred to NADP⁺, reducing it to NADPH."),
          [ch("Oxygen, which is reduced to form water", "Oxygen is the final electron acceptor in the electron transport chain of cellular respiration, not in the light reactions."),
           ch("Carbon dioxide, which is converted directly to glucose in the thylakoid membrane", "Carbon dioxide is converted to carbohydrates in the Calvin cycle in the stroma, and NADPH is used to power the process."),
           ch("Water, which is re-formed on the inside of the thylakoid", "Water is split to provide electrons in the light reactions. It is not re-formed from them.")],
          "Electrons from the light reactions reduce NADP⁺ to NADPH.", difficulty="medium")

    ph_lumen, ph_stroma = 5.0, 8.0
    ratio = 10 ** (ph_stroma - ph_lumen)
    assert round(ratio) == 1000
    B.mcq(4, f"In illuminated chloroplasts, the pH of the thylakoid lumen is {ph_lumen:.1f} and the pH of the stroma is {ph_stroma:.1f}. Approximately how many times greater is the concentration of hydrogen ions in the lumen than in the stroma?",
          ch("1,000 times", "The pH scale is logarithmic. A difference of 3 pH units means a 10³ = 1,000-fold difference in hydrogen ion concentration.", 1000),
          [ch("3 times", "This is the difference in pH units. Because the pH scale is logarithmic, each unit is a tenfold change in concentration.", 3),
           ch("100 times", "This would be a difference of 2 pH units. The difference here is 3 units.", 100),
           ch("1.6 times", "This divides one pH value by the other (8.0 / 5.0). The pH scale is logarithmic, so the concentrations differ by a power of ten.", 1.6)],
          "Each pH unit is a tenfold change in hydrogen ion concentration. The lumen is the more acidic compartment.", difficulty="hard")

    B.mcq(4, "Which statement correctly describes how ATP is made in the light reactions of photosynthesis?",
          ch("Protons flow from the lumen to the stroma through ATP synthase, which drives the formation of ATP from ADP and phosphate.", "This is chemiosmosis. The movement of protons through ATP synthase drives ATP formation, which in photosynthesis is called photophosphorylation."),
          [ch("Protons are pumped by ATP synthase from the stroma into the thylakoid lumen, using the energy that is stored in ATP.", "This reverses the direction. The electron transport chain pumps protons into the lumen, and ATP synthase makes ATP as they flow back."),
           ch("Light energy is transferred directly to ADP and inorganic phosphate, which combine without any proton gradient being involved.", "ATP is made using the proton gradient formed across the thylakoid membrane."),
           ch("Electrons flow through ATP synthase and phosphorylate ADP as they pass from photosystem II to photosystem I in the membrane.", "Electrons pass through the electron transport chain. ATP synthase is a channel for protons.")],
          "The proton gradient across the thylakoid membrane drives ATP synthesis by ATP synthase.", difficulty="medium")

    B.mcq(4, "A plant that has been in bright light is moved into darkness. After several minutes, which change is most likely in the Calvin cycle taking place in the stroma?",
          ch("The Calvin cycle slows, because the ATP and NADPH it uses are no longer replaced by the light reactions.", "The energy captured in the light reactions and transferred to ATP and NADPH powers the Calvin cycle. Without light, these are used up and not replaced."),
          [ch("The Calvin cycle speeds up, because carbon dioxide no longer has to compete with oxygen at the active site.", "Without ATP and NADPH from the light reactions the Calvin cycle cannot continue at a high rate."),
           ch("The Calvin cycle is unchanged, because it uses light energy directly in the stroma of the chloroplast.", "The Calvin cycle uses ATP and NADPH made in the light reactions. It does not absorb light."),
           ch("The Calvin cycle runs in reverse in the dark, producing carbon dioxide from carbohydrates.", "The Calvin cycle does not run in reverse in the dark. It slows because its energy supply decreases.")],
          "The light reactions supply the ATP and NADPH that power carbon fixation in the Calvin cycle.", difficulty="hard")

    B.mcq(4, "Which evidence would best support the claim that photosynthesis by prokaryotes was responsible for the production of an oxygenated atmosphere on Earth?",
          ch("Fossils of photosynthetic prokaryotes in rocks that are older than the first widespread oxidized minerals.", "Photosynthesis releases oxygen. Evidence that photosynthetic prokaryotes existed before oxygen-dependent minerals formed supports the claim that they were the source."),
          [ch("The observation that modern plants release oxygen when they carry out photosynthesis.", "This shows that photosynthesis releases oxygen today, but it does not show that prokaryotes produced the oxygen in Earth's early atmosphere."),
           ch("The observation that oxygen is the second most abundant gas in the present atmosphere.", "The present amount of oxygen does not identify which organisms produced it."),
           ch("Fossils of animals that needed oxygen for cellular respiration, found in rocks younger than the prokaryote fossils.", "The animals show that oxygen was present later. They do not show where the oxygen came from.")],
          "Evidence that supports a claim must connect the claim to the observation, here the order and the process.", difficulty="medium")

    light = [0, 100, 200, 400, 800, 1600]
    minutes = [None, 24, 12, 6, 5, 5]
    leaf_rows = []
    for L_, m_ in zip(light, minutes):
        leaf_rows.append((str(L_), "Did not float" if m_ is None else str(m_), "0.000" if m_ is None else f"{1 / m_:.3f}"))
    assert leaf_rows[-1][2] == "0.200" and leaf_rows[-2][2] == "0.200" and leaf_rows[3][2] == "0.167"
    B.mcq(4, "In a leaf disk assay, disks float when the oxygen produced by photosynthesis fills their air spaces. A student measures the median time for disks to float at six light intensities. The rate is calculated as 1 divided by the time. Which hypothesis best explains the lack of increase in the rate between 800 and 1,600 µmol photons per square meter per second?",
          ch("Another factor, such as the supply of carbon dioxide, has become the limiting factor.", "The rate was increasing with light and then stopped increasing even though the light intensity doubled. This is expected when a different factor limits the rate."),
          [ch("Light is no longer used by the leaf disks at these intensities.", "The rate is 0.200 at both intensities, which means photosynthesis is still occurring at a high rate."),
           ch("The leaf disks have stopped producing oxygen at these intensities.", "The disks still float, so they are still producing oxygen. The rate has not fallen."),
           ch("The rate and the light intensity have an inverse relationship at high light intensities, so the rate falls.", "An inverse relationship would show a lower rate at 1,600 than at 800. The rate is the same.")],
          "A rate that stops increasing as light increases suggests another factor is now limiting.",
          diagram=table(["Light intensity (µmol photons/m²/s)", "Median time to float (min)", "Rate (1/min)"], leaf_rows, caption="Leaf disk assay"), difficulty="hard")

    spectrum = graph("Wavelength of light (nm)", "Relative rate of photosynthesis (%)", 400, 700, 0, 100,
                     [line("Photosynthetic rate", [(400, 60), (430, 95), (470, 85), (500, 35), (550, 20), (600, 40), (650, 80), (680, 100), (700, 40)], "green")],
                     "Relative rate of photosynthesis against wavelength from 400 to 700 nanometers. The rate is highest near 430 and 680 nanometers and lowest near 550 nanometers.")
    B.mcq(4, "The graph shows the rate of photosynthesis in a plant leaf exposed to different wavelengths of light. Which statement is best supported by the data?",
          ch("The rate is highest in blue and red light and lowest in green light, which suggests chlorophyll absorbs blue and red best.", "The graph shows peaks near 430 nm (blue) and 680 nm (red). A pigment's absorption of a wavelength determines how well that wavelength drives photosynthesis."),
          [ch("The rate is highest in green light, because leaves appear green and so must use green light most.", "The graph shows the lowest rates in the green region. Leaves look green because they absorb green light poorly."),
           ch("The rate does not change with wavelength, because light is the energy source for all wavelengths equally.", "The graph shows that the rate changes a lot with wavelength."),
           ch("The rate is zero for green light, because chlorophyll cannot absorb any green light at all and so green light is useless.", "The rate is low but not zero near 550 nm, so some light in that range is used.")],
          "The rate of photosynthesis depends on how well the wavelengths of light are absorbed by the photosynthetic pigments.", diagram=spectrum, difficulty="medium")

    B.mcq(4, "A herbicide blocks the transfer of electrons from photosystem II to the electron transport chain in chloroplasts. Which set of effects is most likely?",
          ch("Less oxygen is released, a smaller proton gradient forms across the thylakoid membrane, and less ATP and NADPH are made.", "Blocking electron flow from photosystem II reduces the splitting of water that replaces its electrons, reduces the proton pumping that depends on electron flow, and so lowers ATP and NADPH production."),
          [ch("More oxygen is released, because electrons that cannot move on cause water to be split faster at photosystem II.", "Water is split to replace the electrons lost by photosystem II. If electrons cannot be passed on, less water is split."),
           ch("The proton gradient becomes larger because protons cannot be used, so more ATP is made by ATP synthase.", "The proton gradient is formed as electrons pass through the electron transport chain. Blocking that flow reduces the gradient."),
           ch("Only the Calvin cycle is affected, because the light reactions do not depend on the transfer of electrons.", "The light reactions depend on electron transfer. The effect on the Calvin cycle occurs because the light reactions slow.")],
          "Photosystem II, the electron transport chain, the proton gradient and ATP synthesis are linked. Blocking one step reduces the later steps.", difficulty="hard")
