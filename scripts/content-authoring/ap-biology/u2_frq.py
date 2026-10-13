"""Unit 2: six free-response prompts, one of each kind.

  RESULTS        (9)  2.7  potato cores in sucrose solutions (masses -> percent change, solute potential, isotonic point)
  RESULTS_GRAPH  (9)  2.2  agar cubes of three sizes (replicate means and standard errors -> bar graph with error bars; surface area-to-volume ratio)
  INVESTIGATION  (4)  2.4  beet pigment leaking at different temperatures (membrane structure, a control, a prediction)
  CONCEPT        (4)  2.8  a drug that blocks the sodium-potassium pump
  MODEL          (4)  2.1  the secretion pathway through the endomembrane system (a table is the "figure")
  DATA           (4)  2.6  uptake of glucose with and without a transport-protein inhibitor (graph)

Part structure follows the CED (see u3_frq.py). Every number is computed here from the raw data.
"""
from lib import *

R_GAS = 0.0831


def build(B):
    # ------------------------------------------------------------------ RESULTS (9): potato cores
    conc = [0.0, 0.2, 0.4, 0.6, 0.8]
    init = 2.50
    final = [2.95, 2.73, 2.53, 2.30, 2.13]
    pct = [(f - init) / init * 100 for f in final]
    assert [round(p, 1) for p in pct] == [18.0, 9.2, 1.2, -8.0, -14.8], pct
    iso = conc[2] + pct[2] / (pct[2] - pct[3]) * (conc[3] - conc[2])
    assert round(iso, 2) == 0.43, iso
    psi_06 = -1 * 0.6 * R_GAS * (22 + 273)
    assert round(psi_06, 1) == -14.7, psi_06
    rows = [(fix(c_, 1), fix(init, 2), fix(f_, 2)) for c_, f_ in zip(conc, final)]
    B.frq(7, "RESULTS",
          "Water moves across the plasma membrane of a cell by osmosis. A student investigated the movement of water into and out of potato cells. The student prepared five sucrose solutions of different molar concentrations and placed five potato cores of equal initial mass in each solution at 22 °C for 24 hours. The mean initial mass and the mean final mass of the cores in each solution are shown in the table.\n\n"
          "**(a)** **Describe** how water potential determines the direction in which water moves by osmosis. (1 point)\n\n"
          "**(b)** (i) **Identify** the dependent variable in the investigation. (ii) **Identify** one variable that the student controlled (kept the same). (iii) **Describe** the relationship between the concentration of sucrose in the solution and the change in the mass of the potato cores. (3 points)\n\n"
          "**(c)** (i) **Calculate** the percent change in the mass of the cores in the 0.6 M solution. Give your answer to the nearest 0.1 percent. (ii) **Calculate** the solute potential of the 0.6 M sucrose solution at 22 °C. Use Ψₛ = -iCRT, with i = 1.0 for sucrose and R = 0.0831 L bar per mol K, and give your answer to the nearest 0.1 bar. (iii) **Estimate** the concentration of sucrose that would be isotonic to the potato cells, by using the percent changes in the mass of the cores in the 0.4 M and the 0.6 M solutions. (3 points)\n\n"
          "**(d)** A chemical that blocks the aquaporins in the plasma membrane is added to a second group of potato cores, which are placed in the 0.0 M solution for 24 hours. **Predict** how the percent change in the mass of these cores will compare with the percent change in the cores in 0.0 M solution without the chemical, and **justify** your prediction. (2 points)",
          [(1, "(a) Describes that water moves from a region of higher water potential to a region of lower water potential."),
           (1, "(b)(i) Identifies the dependent variable as the change in mass (or the final mass, or the percent change in mass) of the potato cores."),
           (1, "(b)(ii) Identifies a controlled variable, such as the initial mass of the cores, the volume of solution, the temperature, the time in the solution, the number of cores, or the type of potato."),
           (1, "(b)(iii) Describes that as the sucrose concentration increases, the percent change in mass decreases, from a gain in mass at the low concentrations to a loss in mass at the high concentrations."),
           (1, "(c)(i) Calculates (2.30 - 2.50) / 2.50 x 100 = -8.0 percent."),
           (1, "(c)(ii) Calculates -(1.0)(0.6)(0.0831)(22 + 273) = -14.7 bars."),
           (1, "(c)(iii) Estimates the isotonic concentration as about 0.43 M (accept 0.40 to 0.45 M), the point between 0.4 M and 0.6 M at which the change in mass would be zero."),
           (1, "(d) Predicts that the cores with the chemical will gain less mass (a smaller percent increase) than the cores without it."),
           (1, "(d) Justifies the prediction: aquaporins transport large quantities of water across the membrane, so blocking them slows the movement of water into the cells by osmosis.")],
          "(a) Water moves by osmosis from a region of higher water potential to a region of lower water potential.\n\n"
          "(b) (i) The dependent variable is the change in the mass of the potato cores. (ii) The initial mass of the cores (2.50 g) was the same in every solution. (iii) As the concentration of sucrose increases, the percent change in mass decreases. The cores gained mass in the solutions with the lowest concentrations and lost mass in the solutions with the highest concentrations.\n\n"
          "(c) (i) Percent change = (2.30 - 2.50) / 2.50 x 100 = -8.0 percent. (ii) Solute potential = -iCRT = -(1.0)(0.6)(0.0831)(295) = -14.7 bars. (iii) The percent change is +1.2 percent in 0.4 M and -8.0 percent in 0.6 M, so the change is zero at about 0.4 + (1.2 / 9.2)(0.2) = 0.43 M.\n\n"
          "(d) The cores with the chemical will gain less mass. Aquaporins carry large quantities of water across the membrane, so if they are blocked, water enters the cells by osmosis more slowly, and less water enters in 24 hours.",
          diagram=table(["Sucrose concentration (M)", "Mean initial mass of cores (g)", "Mean final mass of cores (g)"], rows, caption="Mass of potato cores after 24 hours", row_headers=True))

    # ------------------------------------------------------------------ RESULTS_GRAPH (9): agar cubes
    sides = [1, 2, 3]
    raw = {1: [77.9, 78.6, 79.0, 78.1], 2: [48.0, 49.5, 48.9, 48.8], 3: [34.0, 35.6, 35.1, 34.9]}
    means = [mean(raw[s_]) for s_ in sides]
    ses = [se(raw[s_]) for s_ in sides]
    assert [round(m_, 1) for m_ in means] == [78.4, 48.8, 34.9], means
    assert [round(e_, 2) for e_ in ses] == [0.25, 0.31, 0.33], ses  # the sample response quotes these
    sa_v_2 = (6 * 2**2) / (2**3)
    assert sa_v_2 == 3.0
    sav = [(6 * s_**2) / s_**3 for s_ in sides]
    assert sav == [6.0, 3.0, 2.0]
    rows = [(str(s_), fix(m_, 1), fix(e_, 2)) for s_, m_, e_ in zip(sides, means, ses)]
    B.frq(2, "RESULTS_GRAPH",
          "Cells exchange materials with their environment across the plasma membrane. A student modeled this with cubes of agar that contain a dye, which changes color when acid diffuses in. For each of three sizes of cube, the student placed four cubes in a solution of acid for 10 minutes, cut each cube in half, and measured how much of the volume of the cube had changed color. The means and the standard errors of the means are shown in the table.\n\n"
          "**(a)** **Describe** how the surface area-to-volume ratio of a cell affects the exchange of materials between the cell and its environment. (1 point)\n\n"
          "**(b)** **Construct** a graph of the data in the table. Because you are answering in writing, describe the graph you would draw: the type of graph, what is shown on each axis, with units, the scale of each axis, the values you would plot, and how you would show the standard errors. (4 points)\n\n"
          "**(c)** (i) **Calculate** the surface area-to-volume ratio of the cube that has sides of 2 cm. (The surface area of a cube is 6s² and the volume of a cube is s³, where s is the length of a side.) (ii) **State** a null hypothesis for this investigation. (2 points)\n\n"
          "**(d)** The student also tests a cube that has sides of 6 cm. **Predict** how the percent of the volume that changed color in this cube will compare with the percent in the cube that has sides of 3 cm, and **justify** your prediction. (2 points)",
          [(1, "(a) Describes that a higher surface area-to-volume ratio gives a larger membrane surface for each unit of volume, so materials are exchanged more efficiently (and a lower ratio makes exchange less efficient)."),
           (1, "(b) Chooses an appropriate graph type: a bar graph with one bar for each size of cube (or a line graph with the side length on the horizontal axis)."),
           (1, "(b) Labels both axes with units: the side length of the cube (cm) and the mean percent of the volume that changed color (percent)."),
           (1, "(b) Gives an appropriate scale: a vertical axis that starts at 0 and has equal intervals, extending to at least 80 percent so all of the means fit."),
           (1, "(b) Plots the data accurately (about 78.4, 48.8 and 34.9 percent) and shows error bars of plus and minus one standard error for each point."),
           (1, "(c)(i) Calculates 6(2)² / (2)³ = 24 / 8 = 3.0 per cm (3.0 cm⁻¹)."),
           (1, "(c)(ii) States a null hypothesis: the size of the cube has no effect on the percent of its volume that changes color in 10 minutes (any differences are due to chance)."),
           (1, "(d) Predicts that a smaller percent of the volume of the 6 cm cube will change color than of the 3 cm cube (less than 34.9 percent)."),
           (1, "(d) Justifies the prediction: the surface area-to-volume ratio decreases as the cube gets larger (2.0 per cm for 3 cm and 1.0 per cm for 6 cm), so the acid reaches less of the volume in the same time.")],
          "(a) A cell with a higher surface area-to-volume ratio has more plasma membrane for each unit of volume, so it can exchange materials with its environment more efficiently. A cell with a lower ratio is less efficient.\n\n"
          "(b) A bar graph. The horizontal axis is labeled \"Side length of the cube (cm)\" with bars at 1, 2 and 3. The vertical axis is labeled \"Mean percent of volume that changed color\" and is scaled from 0 to 100 in steps of 20. The bars are about 78.4, 48.8 and 34.9, each with an error bar of plus and minus one standard error (about 0.25, 0.31 and 0.33 percent, which are small).\n\n"
          "(c) (i) SA:V = 6(2)² / (2)³ = 24 cm² / 8 cm³ = 3.0 per cm. (ii) The size of the cube has no effect on the percent of its volume that changes color.\n\n"
          "(d) A smaller percent of the volume of the 6 cm cube will change color. The surface area-to-volume ratio of the 6 cm cube (1.0 per cm) is lower than that of the 3 cm cube (2.0 per cm), so in the same 10 minutes the acid reaches a smaller part of the volume.",
          diagram=table(["Side length of the cube (cm)", "Mean percent of volume that changed color (n = 4)", "Standard error"], rows, caption="Diffusion into agar cubes in 10 minutes", row_headers=True))

    # ------------------------------------------------------------------ INVESTIGATION (4): beet pigment
    B.frq(4, "INVESTIGATION",
          "The cells of a beet root contain a red pigment inside their vacuoles. The pigment stays inside undamaged cells, but it leaks into the surrounding water if the membranes of the cells are damaged. A student wants to investigate how temperature affects the permeability of the membranes of beet cells. The student has beet root cut into equal pieces, test tubes of distilled water, water baths at 20 °C, 40 °C, 60 °C and 80 °C, and a colorimeter that measures the amount of pigment in water. The student plans to place one piece of beet in a tube of water in each water bath for 10 minutes, remove the pieces, and measure the amount of pigment in the water in each tube.\n\n"
          "**(a)** **Describe** how the structure of the plasma membrane normally prevents the pigment molecules from leaving the cell. (1 point)\n\n"
          "**(b)** **Identify** an appropriate control for the investigation. (1 point)\n\n"
          "**(c)** **Predict** how the amount of pigment in the water will change as the temperature of the water bath increases. (1 point)\n\n"
          "**(d)** **Justify** your prediction. (1 point)",
          [(1, "(a) Describes that the membrane has a hydrophobic (nonpolar) interior formed by the fatty acid tails of the phospholipid bilayer, which prevents large polar molecules and ions, such as the pigment, from crossing (selective permeability)."),
           (1, "(b) Identifies a control: a piece of beet kept in water at room temperature (or at 20 °C) and not heated, or a tube of water with no beet piece to show the baseline reading of the colorimeter."),
           (1, "(c) Predicts that the amount of pigment in the water will increase as the temperature increases (especially at the higher temperatures)."),
           (1, "(d) Justifies: heat disrupts the structure of the membrane (it makes the phospholipids more fluid and denatures the membrane proteins), so the membrane becomes more permeable and the pigment leaks out.")],
          "(a) The plasma membrane has a hydrophobic interior made of the fatty acid tails of the phospholipids. It blocks large polar molecules and ions, so the pigment cannot pass through the bilayer.\n\n"
          "(b) A piece of beet that is kept in water at 20 °C and is not heated, treated the same in every other way.\n\n"
          "(c) The amount of pigment in the water will increase as the temperature of the water bath increases.\n\n"
          "(d) Heat damages the membrane. It makes the phospholipids more fluid and denatures the proteins in the membrane, so the membrane is more permeable and more pigment leaks out into the water.")

    # ------------------------------------------------------------------ CONCEPT (4): sodium-potassium pump
    B.frq(8, "CONCEPT",
          "Nerve cells keep a high concentration of potassium ions (K⁺) inside the cell and a high concentration of sodium ions (Na⁺) outside the cell. They do this using the sodium-potassium pump, a membrane protein that uses ATP. A drug is developed that blocks the sodium-potassium pump in the plasma membranes of nerve cells.\n\n"
          "**(a)** **Describe** one way in which active transport differs from passive transport. (1 point)\n\n"
          "**(b)** **Explain** how the sodium-potassium pump helps to maintain the membrane potential of a nerve cell. (1 point)\n\n"
          "**(c)** **Predict** how the concentration of Na⁺ inside a nerve cell will change over time after the drug is added. (1 point)\n\n"
          "**(d)** **Justify** your prediction. (1 point)",
          [(1, "(a) Describes a difference: active transport requires a direct input of energy (such as ATP) and can move substances against their concentration gradients, but passive transport does not require energy and moves substances down their gradients."),
           (1, "(b) Explains that the pump uses ATP to move Na⁺ out and K⁺ into the cell against their concentration gradients, which maintains the difference in the concentration of the ions, and so the electrical charge difference, across the membrane."),
           (1, "(c) Predicts that the concentration of Na⁺ inside the cell will increase."),
           (1, "(d) Justifies: without the pump, Na⁺ moves down its concentration gradient into the cell through channels, and nothing moves it back out, so the gradient gradually disappears.")],
          "(a) Active transport requires energy from ATP and can move a substance from a low concentration to a high concentration, against its gradient. Passive transport needs no energy and moves a substance down its gradient.\n\n"
          "(b) The pump uses the energy of ATP to move Na⁺ out of the cell and K⁺ into the cell, against their gradients. This maintains the different concentrations of the ions on the two sides of the membrane, which maintains the membrane potential.\n\n"
          "(c) The concentration of Na⁺ inside the cell will increase.\n\n"
          "(d) When the pump is blocked, Na⁺ moves into the cell down its concentration gradient through channel proteins, and it is no longer pumped back out, so the concentration of Na⁺ inside the cell rises until the gradient is gone.")

    # ------------------------------------------------------------------ MODEL (4): the secretion pathway
    model_rows = [("1", "Ribosomes attached to the endoplasmic reticulum, where a protein is made"), ("2", "A transport vesicle that buds off the endoplasmic reticulum"),
                  ("3", "A stack of flattened membrane sacs that receives the vesicle"), ("4", "A vesicle that buds off the stack of sacs"), ("5", "The plasma membrane at the surface of the cell")]
    B.frq(1, "MODEL",
          "The model represents the path of a protein that is made in a gland cell and secreted from the cell. The table is the key to the model. In the model, a protein is made by ribosomes on the endoplasmic reticulum (1) and enters the endoplasmic reticulum. A transport vesicle (2) carries the protein from the endoplasmic reticulum to a stack of flattened membrane sacs (3), where the protein is modified. A vesicle (4) then carries the protein from the stack of sacs to the plasma membrane (5), and the protein is released from the cell.\n\n"
          "**(a)** **Describe** the role of the ribosomes on the endoplasmic reticulum (1) in the model. (1 point)\n\n"
          "**(b)** **Explain** why the model shows the protein being carried between the structures in vesicles. (1 point)\n\n"
          "**(c)** **Identify** the structure represented by the stack of flattened membrane sacs (3), and **identify** one function of this structure. (1 point)\n\n"
          "**(d)** **Explain** how the protein is released from the cell when the vesicle (4) reaches the plasma membrane (5). (1 point)",
          [(1, "(a) Describes that the ribosomes make (synthesize) the protein according to the sequence of messenger RNA, and the ER helps to carry out protein synthesis (the ribosomes attached to the rough ER make the protein that enters the ER)."),
           (1, "(b) Explains that the structures are separated by membranes (the endomembrane system is compartmentalized), so a vesicle that buds from one membrane and fuses with the next membrane carries the protein between compartments without it crossing a membrane."),
           (1, "(c) Identifies structure 3 as the Golgi complex and identifies a function: it chemically modifies and folds newly made products, or it packages proteins for trafficking."),
           (1, "(d) Explains that the vesicle fuses with the plasma membrane (exocytosis), which releases its contents (the protein) to the outside of the cell, and that this process requires energy.")],
          "(a) The ribosomes make the protein by joining amino acids according to the sequence of the messenger RNA. Because they are attached to the endoplasmic reticulum, the protein enters the endoplasmic reticulum as it is made.\n\n"
          "(b) Each structure is surrounded by its own membrane, so the cell is divided into compartments. A vesicle buds from the membrane of one structure and fuses with the membrane of the next, which carries the protein from one compartment to the next.\n\n"
          "(c) Structure 3 is the Golgi complex. It modifies and correctly folds newly made products and packages proteins for transport.\n\n"
          "(d) The vesicle fuses with the plasma membrane. This is exocytosis, and it requires energy. The fusion opens the vesicle to the outside of the cell, which releases the protein.",
          diagram=table(["Label", "Part of the model"], model_rows, caption="Key to the model of the path of a secreted protein", row_headers=True))

    # ------------------------------------------------------------------ DATA (4): facilitated diffusion
    g = graph("External glucose concentration (mM)", "Rate of glucose uptake (µmol/min)", 0, 20, 0, 100,
              [line("No inhibitor", [(0, 0), (2, 40), (5, 70), (10, 90), (20, 100)], "blue"),
               line("With an inhibitor of the glucose transport protein", [(0, 0), (2, 20), (5, 35), (10, 45), (20, 50)], "red")],
              "Rate of glucose uptake against external glucose concentration. With no inhibitor the rate rises steeply and reaches 100 at 20 millimolar. With the inhibitor the rate rises more slowly and reaches 50 at 20 millimolar.")
    B.frq(6, "DATA",
          "Glucose is a large polar molecule that enters red blood cells through a transport protein in the plasma membrane. A researcher measured the rate of uptake of glucose by red blood cells at different external concentrations of glucose, with and without a chemical that inhibits the transport protein. The results are shown in the graph.\n\n"
          "**(a)** **Describe** how the rate of glucose uptake changes as the external glucose concentration increases from 0 mM to 20 mM when there is no inhibitor. (1 point)\n\n"
          "**(b)** **Describe** the effect of the inhibitor on the rate of glucose uptake at an external glucose concentration of 20 mM. (1 point)\n\n"
          "**(c)** A student claims that glucose enters red blood cells by simple diffusion directly through the phospholipid bilayer. **Evaluate** the claim using the data in the graph. (1 point)\n\n"
          "**(d)** **Explain** why the rate of glucose uptake without the inhibitor levels off at high external glucose concentrations. (1 point)",
          [(1, "(a) Describes that the rate increases steeply at low concentrations and then levels off at about 100 µmol/min at the higher concentrations (it does not keep increasing)."),
           (1, "(b) Describes that the inhibitor decreases the rate of uptake at 20 mM from about 100 µmol/min to about 50 µmol/min, which is a decrease of about half."),
           (1, "(c) Evaluates the claim as not supported, using data: the rate reaches a maximum rather than increasing steadily, and an inhibitor of a protein reduces the rate, which shows that a transport protein is involved."),
           (1, "(d) Explains that the number of transport proteins is limited, so at high concentrations all of them are being used (they are saturated) and the rate cannot increase any more.")],
          "(a) Without the inhibitor, the rate of uptake rises quickly at low glucose concentrations (to about 70 µmol/min at 5 mM) and then levels off at about 100 µmol/min.\n\n"
          "(b) At 20 mM the inhibitor lowers the rate of uptake from about 100 µmol/min to about 50 µmol/min, a decrease of about one half.\n\n"
          "(c) The data do not support the claim. In simple diffusion the rate would keep increasing as the concentration increases, but here it levels off. An inhibitor of a transport protein also lowers the rate, which shows that a protein is needed for glucose to enter.\n\n"
          "(d) There is a limited number of transport proteins in the membrane. At high glucose concentrations all of them are working at their maximum rate, so they are saturated, and more glucose cannot increase the rate.",
          diagram=g)
