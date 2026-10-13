"""Unit 3, topic 3.5 Cellular Respiration (12 questions).

Required content (CED 2025-26): 3.5.A.1 respiration and fermentation are characteristic of all forms of life; 3.5.A.2-3 ETC, proton gradient across the inner
mitochondrial membrane (high [H+] in the intermembrane space, matrix pH higher), folding of the inner membrane raises surface area and ATP made, oxidative
phosphorylation through ATP synthase, decoupling generates heat, aerobic prokaryotes pump protons across the plasma membrane and anaerobic prokaryotes use
other terminal acceptors; 3.5.B.1-6 glycolysis (ATP, NADH, pyruvate), pyruvate moves to the mitochondrion, Krebs cycle in the matrix (CO2 released, NADH and
FADH2, some ATP), electrons delivered to the ETC, fermentation lets glycolysis proceed without oxygen (alcohol, lactic acid).
Excluded by the CED: memorizing the steps of glycolysis and the Krebs cycle, molecule structures, enzyme names, the names of electron carriers.
Suggested skill 4.A: represent data (graphs with error bars); used here for the table and rate questions.
"""
from lib import *


def build(B):
    B.mcq(5, "Which statement correctly describes glycolysis?",
          ch("It takes place in the cytosol and converts glucose to pyruvate, forming ATP and NADH.", "Glycolysis releases some of the energy in glucose to form ATP (from ADP and inorganic phosphate), NADH (from NAD⁺) and pyruvate."),
          [ch("It takes place in the mitochondrial matrix and requires oxygen to proceed.", "Glycolysis occurs in the cytosol and does not require oxygen."),
           ch("It takes place in the inner mitochondrial membrane and makes most of the ATP in a cell.", "The inner mitochondrial membrane is where the electron transport chain and ATP synthase are found."),
           ch("It takes place in chloroplasts and uses light energy to convert carbon dioxide to glucose.", "This describes photosynthesis, not glycolysis. Glycolysis breaks down glucose.")],
          "Glycolysis occurs in the cytosol, oxidizes glucose to pyruvate and forms ATP and NADH without needing oxygen.", difficulty="easy")

    B.mcq(5, "In aerobic cellular respiration in eukaryotes, which molecule is the final electron acceptor of the electron transport chain?",
          ch("Oxygen, which is reduced to form water", "Oxygen is the terminal electron acceptor in aerobic respiration."),
          [ch("Carbon dioxide, which is reduced to form glucose", "Carbon dioxide is released in the Krebs cycle. It is not an electron acceptor of the chain."),
           ch("Pyruvate, which is reduced to form lactic acid", "Pyruvate is reduced to lactic acid in fermentation. It is not the final electron acceptor of the electron transport chain."),
           ch("NAD⁺, which is reduced to form NADH", "NAD⁺ accepts electrons earlier in respiration, forming NADH, which then delivers electrons to the electron transport chain.")],
          "Oxygen is the terminal electron acceptor in aerobic cellular respiration.", difficulty="easy")

    B.mcq(5, "Which statement correctly describes the Krebs (citric acid) cycle in a eukaryotic cell?",
          ch("It takes place in the mitochondrial matrix, where carbon dioxide is released and NAD⁺ and FAD gain electrons.", "During the Krebs cycle, carbon dioxide is released from organic intermediates, some ATP is made, and electrons are transferred by NAD⁺ and FAD."),
          [ch("It takes place in the cytosol, where glucose is converted to pyruvate and a small amount of ATP is made.", "This describes glycolysis."),
           ch("It takes place on the inner mitochondrial membrane, where oxygen is reduced to water as electrons move along.", "This describes the electron transport chain. The Krebs cycle takes place in the matrix."),
           ch("It takes place in the intermembrane space, where protons accumulate to form a gradient for ATP synthase.", "Protons accumulate in the intermembrane space because of the electron transport chain, not the Krebs cycle.")],
          "The Krebs cycle takes place in the mitochondrial matrix and delivers electrons to the electron transport chain via NADH and FADH₂.", difficulty="medium")

    B.mcq(5, "When the electron transport chain is operating in a mitochondrion, which statement about the two sides of the inner mitochondrial membrane is correct?",
          ch("The intermembrane space has a higher concentration of protons and a lower pH than the matrix.", "Electron transport is accompanied by the movement of protons into the intermembrane space. The pH of the matrix is higher than that of the intermembrane space."),
          [ch("The matrix has a higher concentration of protons and a lower pH than the intermembrane space.", "This reverses the gradient. Protons are pumped out of the matrix."),
           ch("The two sides have the same concentration of protons, because protons move freely across the membrane.", "The membrane is not freely permeable to protons. A gradient forms and is used to make ATP."),
           ch("The intermembrane space has a lower concentration of protons and a higher pH than the matrix.", "This reverses the gradient. It is the intermembrane space that has the higher proton concentration and the lower pH.")],
          "The electron transport chain builds a proton gradient across the inner mitochondrial membrane, high in the intermembrane space and low in the matrix.", difficulty="medium")

    B.mcq(5, "The inner membrane of a mitochondrion is highly folded. Which statement best explains how this feature affects the production of ATP?",
          ch("The folds increase the surface area of the inner membrane, so more ATP synthase and electron transport proteins fit in it.", "Folding of the inner membrane increases surface area, which allows more ATP to be synthesized."),
          [ch("The folds reduce the volume of the matrix, so the Krebs cycle takes place at a slower rate and less ATP is made.", "The folds are not related to slowing down the Krebs cycle. They increase the area available for oxidative phosphorylation."),
           ch("The folds increase the volume of the cytosol available for glycolysis, which makes more ATP.", "The folds are inside the mitochondrion and do not change the volume of the cytosol."),
           ch("The folds prevent protons from moving into the intermembrane space, so that ATP is made more slowly.", "The proton gradient needs protons to move into the intermembrane space. The folds help ATP production by providing more membrane.")],
          "A larger inner membrane area holds more of the proteins needed for oxidative phosphorylation.", difficulty="medium")

    B.mcq(5, "During intense exercise, muscle cells may not receive enough oxygen and may carry out lactic acid fermentation. What is the main benefit to the cell of fermentation?",
          ch("It allows glycolysis to continue to produce ATP when oxygen is not available.", "Fermentation lets glycolysis proceed in the absence of oxygen by regenerating NAD⁺, so some ATP continues to be made."),
          [ch("It produces more ATP from each glucose than aerobic respiration does in the muscle cell.", "Aerobic respiration makes much more ATP per glucose than fermentation."),
           ch("It converts lactic acid back into glucose, which stores the energy for later use.", "Fermentation produces lactic acid from pyruvate. It does not make glucose."),
           ch("It allows the electron transport chain to continue to pump protons without oxygen.", "Fermentation does not supply electrons to the electron transport chain.")],
          "Fermentation allows glycolysis to proceed in the absence of oxygen.", difficulty="medium")

    B.mcq(5, "Cyanide blocks the transfer of electrons from the last carrier of the mitochondrial electron transport chain to oxygen. Which set of effects is most likely in cells exposed to cyanide?",
          ch("Electron transport stops, the proton gradient cannot be maintained, and less ATP is made by oxidative phosphorylation.", "With electron flow blocked, protons are no longer pumped. The proton gradient dissipates and ATP synthase makes less ATP."),
          [ch("Electron transport speeds up, because the electrons that cannot reach oxygen move faster through the chain.", "Blocking the last step stops the chain, because electrons have nowhere to go."),
           ch("The proton gradient increases, because protons can no longer flow back through ATP synthase into the matrix.", "The gradient is made by the electron transport chain. If electron transport stops, the gradient cannot be maintained."),
           ch("Oxygen use increases, because the cell tries to make up for the lack of ATP by using more oxygen.", "Cyanide stops the use of oxygen as a terminal electron acceptor, so oxygen consumption falls.")],
          "Electron transport, the proton gradient and ATP synthesis are linked, so blocking electron transport reduces ATP synthesis.", difficulty="hard")

    B.mcq(5, "A chemical makes the inner mitochondrial membrane permeable to protons, so protons flow back into the matrix without passing through ATP synthase. Which set of effects is most likely in cells treated with the chemical?",
          ch("The rate of oxygen consumption increases, less ATP is made by oxidative phosphorylation, and more energy is released as heat.", "Decoupling oxidative phosphorylation from electron transport generates heat. Electron transport continues, and oxygen is used, but the energy of the gradient is not captured in ATP."),
          [ch("The rate of oxygen consumption decreases and more ATP is made, because the protons enter the matrix more easily.", "Protons that leak across the membrane do not pass through ATP synthase, so less ATP is made."),
           ch("The rate of oxygen consumption is unchanged and the cell releases less heat, because the gradient is then easier for the cell to maintain.", "The leak makes it harder to maintain the gradient, so the chain works faster. More heat is released."),
           ch("Electron transport stops, because the protons that are needed to pump electrons are no longer available.", "Electron transport does not stop. Without the gradient to oppose it, it continues.")],
          "Uncoupling lets the energy of the gradient escape as heat instead of being used to make ATP.", difficulty="hard")

    s_pct = [0, 2, 4, 6, 8, 10]
    co2 = [0.3, 4.5, 8.7, 11.8, 12.0, 12.1]
    minutes = 30
    rate4 = co2[2] / minutes
    assert round(rate4, 2) == 0.29 and round(co2[2] / 60, 3) == 0.145
    B.mcq(5, f"A student measures the volume of carbon dioxide produced by yeast in anaerobic conditions in {minutes} minutes at different sucrose concentrations. What is the rate of carbon dioxide production, in mL per minute, in the 4 percent sucrose treatment?",
          ch("0.29 mL/min", "Rate = volume / time = 8.7 mL / 30 min = 0.29 mL/min.", rate4),
          [ch("8.7 mL/min", "This is the total volume produced in 30 minutes. A rate is the volume divided by the time.", 8.7),
           ch("0.15 mL/min", "This divides by 60 minutes instead of the 30 minutes of the experiment.", co2[2] / 60),
           ch("261 mL/min", "This multiplies the volume by the time (8.7 x 30) instead of dividing.", co2[2] * minutes)],
          "Rate = amount produced / time.",
          diagram=table(["Sucrose concentration (%)", f"Volume of CO₂ produced in {minutes} min (mL)"], [(s_, fix(c_)) for s_, c_ in zip(s_pct, co2)], caption="Fermentation by yeast"), difficulty="medium")

    B.mcq(5, "Which statement about cellular respiration is correct?",
          ch("Plants, animals and most other organisms carry out cellular respiration, because all cells need ATP.", "Respiration and fermentation are characteristic of all forms of life. Plants carry out photosynthesis and cellular respiration."),
          [ch("Only animals carry out cellular respiration, and plants carry out photosynthesis instead.", "This is a common misconception. Plants have mitochondria and carry out cellular respiration, including in the dark."),
           ch("Only organisms with mitochondria can obtain usable energy from glucose and other molecules.", "Prokaryotes lack mitochondria and still obtain energy from glucose by glycolysis, fermentation or respiration."),
           ch("Cellular respiration in plants takes place only at night, when photosynthesis has stopped for the day.", "Plant cells carry out cellular respiration all the time. Photosynthesis may produce more oxygen than respiration uses in the light.")],
          "All forms of life use respiration or fermentation to obtain usable energy from molecules.", difficulty="easy")

    t = [0, 5, 10, 15, 20]
    peas = [0.0, 0.9, 2.0, 3.1, 4.2]
    beads = [0.0, 0.1, 0.1, 0.2, 0.2]
    net = peas[-1] - beads[-1]
    r_net = net / t[-1]
    assert round(r_net, 2) == 0.20 and round(peas[-1] / t[-1], 2) == 0.21 and round(net / 5, 2) == 0.80
    B.mcq(5, "In a respirometer experiment, the volume of oxygen consumed by germinating peas is measured, with glass beads of the same volume as a control for changes in temperature and pressure. What is the rate of oxygen consumption by the germinating peas over 20 minutes, corrected using the control?",
          ch("0.20 mL/min", "The corrected volume is 4.2 - 0.2 = 4.0 mL. The rate is 4.0 mL / 20 min = 0.20 mL/min.", r_net),
          [ch("0.21 mL/min", "This divides the uncorrected volume (4.2 mL) by 20 minutes. The control shows that 0.2 mL of the change was not due to the peas.", peas[-1] / t[-1]),
           ch("4.0 mL/min", "This is the corrected volume. A rate is the volume divided by the time.", net),
           ch("0.80 mL/min", "This divides the corrected volume by 5 minutes, the length of one interval, instead of the 20 minutes over which the volume was measured.", net / 5)],
          "Subtract the control, then divide by the time over which the change was measured.",
          diagram=table(["Time (min)", "Germinating peas: cumulative O₂ consumed (mL)", "Glass beads: cumulative change (mL)"], [(t_, fix(p_), fix(b_)) for t_, p_, b_ in zip(t, peas, beads)], caption="Respirometer data"), difficulty="hard")

    B.mcq(5, "Many aerobic prokaryotes have no mitochondria but still carry out electron transport coupled to the synthesis of ATP. Where are protons moved by the electron transport chain in these cells?",
          ch("Across the plasma membrane, so a proton gradient forms there and drives ATP synthesis as protons flow back.", "In prokaryotes, the passage of electrons is accompanied by the movement of protons across the plasma membrane."),
          [ch("Across the membrane of a nucleus, which holds the proton gradient used by ATP synthase to make ATP.", "Prokaryotes do not have a nucleus. Their electron transport chains are in the plasma membrane."),
           ch("Into small mitochondria that are present in the cytoplasm of every aerobic prokaryote cell.", "Prokaryotes do not have mitochondria."),
           ch("Nowhere, because only cells that contain mitochondria are able to build a proton gradient.", "Electron transport chains occur in chloroplasts, in mitochondria and across prokaryotic plasma membranes.")],
          "Electron transport chains occur in chloroplasts, in mitochondria, and across the plasma membranes of prokaryotes.", difficulty="medium")
