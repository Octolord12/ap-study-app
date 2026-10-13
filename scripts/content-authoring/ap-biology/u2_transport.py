"""Unit 2, topics 2.6 Facilitated Diffusion (7 questions), 2.7 Tonicity and Osmoregulation (12) and 2.8 Mechanisms of Transport (6).

Required content (CED 2025-26): 2.6.A facilitated diffusion needs transport or channel proteins; charged ions (Na+, K+) need channel proteins and their movement can polarize the membrane;
large polar molecules move down their gradient with no energy input; aquaporins carry large quantities of water. 2.7.A external environments can be hypotonic, hypertonic or isotonic to cells;
water moves by osmosis from high to low water potential (psi = psi_P + psi_S); 2.7.B osmoregulation keeps water balance and solute composition, water moves from low to high solute concentration;
solute potential psi_S = -iCRT with R = 0.0831 L bar / (mol K) and T in kelvin (C + 273). 2.8.A active transport needs metabolic energy (ATP) and membrane proteins to move ions and molecules
and to establish and maintain electrochemical gradients; the Na+/K+ pump (ATPase) helps maintain the membrane potential. Suggested skills: 6.E, 4.A, 1.B.
"""
from lib import *

R_GAS = 0.0831  # L bar / (mol K), as on the AP equation sheet


def solute_potential(i, molar, celsius):
    return -i * molar * R_GAS * (celsius + 273)


def build(B):
    # ------------------------------------------------------------------ 2.6 Facilitated diffusion
    B.mcq(6, "Which statement correctly describes facilitated diffusion?",
          ch("Channel proteins or transport proteins allow substances to move down their concentration gradient across the membrane without an input of energy.", "Facilitated diffusion is passive transport that needs membrane proteins but does not use energy."),
          [ch("Transport proteins use energy from ATP to move substances from a region of low concentration to a region of high concentration across the membrane.", "This describes active transport, which needs energy."),
           ch("Substances pass directly through the hydrophobic interior of the phospholipid bilayer, without the help of any protein, down their gradient.", "This describes simple diffusion. Facilitated diffusion needs proteins."),
           ch("The plasma membrane folds in and forms vesicles that take large particles into the cell, using energy that is supplied by the cell.", "This describes endocytosis.")],
          "Facilitated diffusion uses channel or transport proteins and needs no energy.", difficulty="easy")

    B.mcq(6, "Sodium ions and potassium ions need channel proteins to cross the plasma membrane. Which statement best explains why?",
          ch("The ions are charged, so they cannot pass through the hydrophobic interior of the lipid bilayer without a channel.", "Charged ions are blocked by the nonpolar interior of the membrane and cross through channel proteins."),
          [ch("The ions are too large to pass between the phospholipid molecules, which are packed too tightly for the ions to fit.", "The barrier is the charge of the ions and the hydrophobic interior, not only the size of the ions."),
           ch("The ions are nonpolar, so they are repelled by the polar heads of the phospholipids on both sides of the membrane.", "Ions are charged and polar interactions are not what block them. The hydrophobic interior blocks them."),
           ch("The ions are produced inside the membrane by proteins, so they must be moved out through channels to the cytoplasm.", "Ions are not made inside the membrane. They come from the solutions on either side.")],
          "Charged ions require channel proteins to cross the membrane.", difficulty="medium")

    B.mcq(6, "Glucose is a large polar molecule. Cells take glucose in from a region of higher concentration to a region of lower concentration, without using any ATP, through a protein in the membrane. Which process is this?",
          ch("Facilitated diffusion, which moves large polar molecules through membranes down a concentration gradient with no energy input", "Large polar molecules move through transport proteins down the gradient in facilitated diffusion."),
          [ch("Active transport, which moves large polar molecules through membranes down a concentration gradient using energy from ATP", "No ATP is used in this process, so it is not active transport."),
           ch("Simple diffusion, which moves large polar molecules directly through the lipid bilayer down a concentration gradient with no protein", "A protein is involved in this process, and large polar molecules do not cross the bilayer directly."),
           ch("Exocytosis, which moves large polar molecules out of the cell inside vesicles that fuse with the plasma membrane using energy", "In this case the molecule moves into the cell without using energy.")],
          "Facilitated diffusion enables large polar molecules to move down their gradient through a protein with no energy input.", difficulty="medium")

    B.mcq(6, "The cells of the kidney move large quantities of water across their membranes. Which membrane proteins make this rapid movement of water possible?",
          ch("Aquaporins, which transport large quantities of water across the membrane", "Aquaporins are channel proteins that allow large amounts of water to cross membranes."),
          [ch("Sodium-potassium pumps, which use ATP to carry water across the membrane against its concentration gradient", "These pumps move Na⁺ and K⁺, and water moves by osmosis."),
           ch("Phospholipids, which form a pore in the bilayer that lets water pass through in large quantities", "Phospholipids form a barrier, and only a small amount of water crosses the bilayer directly."),
           ch("Glycoproteins, which bind water molecules on the outside of the cell and carry them into the cytoplasm", "Glycoproteins are involved in other functions. Aquaporins transport the water.")],
          "Aquaporins transport large quantities of water across membranes.", difficulty="medium")

    g_x = [(0, 0), (10, 10), (20, 20), (30, 30), (40, 40)]
    g_y = [(0, 0), (10, 22), (20, 32), (30, 35), (40, 36)]
    graph_fd = graph("External concentration (mM)", "Rate of uptake (µmol/min)", 0, 40, 0, 40,
                     [line("Molecule X", g_x, "blue"), line("Molecule Y", g_y, "red")],
                     "Rate of uptake against external concentration. For molecule X the rate rises in a straight line from 0 to 40. For molecule Y the rate rises steeply to about 32 at 20 millimolar and then levels off near 36.")
    B.mcq(6, "The graph shows the rate at which cells take up two molecules, X and Y, at different external concentrations. Which statement best explains why the rate of uptake of molecule Y levels off at high concentrations?",
          ch("The transport proteins that move molecule Y become saturated, so a higher concentration cannot increase the rate.", "A limited number of transport proteins can only carry molecules at a maximum rate, which leads to a plateau."),
          [ch("The membrane runs out of phospholipids at high concentrations, so no more of molecule Y can cross the bilayer.", "The number of phospholipids does not limit the rate. The number of transport proteins does."),
           ch("The cell uses up its ATP at high concentrations, so it can no longer move molecule Y in the direction of the gradient.", "Facilitated diffusion does not use ATP, and the plateau is explained by the limited number of proteins."),
           ch("The molecules of Y are denatured at high concentrations, so they can no longer pass through channels in the membrane.", "A plateau in the rate does not indicate that the molecules are denatured. It shows that the proteins are saturated.")],
          "Facilitated diffusion has a maximum rate, because the number of transport proteins is limited.", diagram=graph_fd, difficulty="medium")

    B.mcq(6, "Based on the graph, which statement about how molecules X and Y cross the membrane is best supported?",
          ch("Molecule X probably crosses by simple diffusion, since its rate increases steadily, and molecule Y probably crosses by facilitated diffusion, since its rate reaches a maximum.", "A rate that keeps increasing with concentration fits simple diffusion, and a rate that reaches a maximum fits a process that depends on a limited number of proteins."),
          [ch("Molecule X probably crosses by facilitated diffusion, since its rate increases steadily, and molecule Y probably crosses by simple diffusion, since its rate reaches a maximum.", "This reverses the interpretation. A maximum rate suggests that proteins are involved."),
           ch("Both molecules probably cross by active transport, since the rates for both of them are higher at higher external concentrations.", "A higher rate at a higher concentration does not show that energy is used."),
           ch("Both molecules probably cross by simple diffusion, since the rates for both of them are above zero at every concentration shown.", "The two graphs differ in shape, and the plateau for molecule Y is not expected for simple diffusion.")],
          "Saturation at high concentration indicates facilitated diffusion.", diagram=graph_fd, difficulty="hard")

    B.mcq(6, "A mutation reduces the number of potassium channel proteins in the plasma membrane of a cell. Which prediction is most consistent with this change?",
          ch("The movement of potassium ions across the membrane would be slower, since the ions need channel proteins to cross the membrane.", "Potassium ions are charged and need channels. Fewer channels means a lower rate of movement."),
          [ch("The movement of potassium ions across the membrane would not change, since the ions can pass directly through the lipid bilayer.", "Charged ions cannot pass directly through the hydrophobic interior of the bilayer."),
           ch("The movement of potassium ions across the membrane would be faster, since the ions have fewer channels that they need to pass through.", "Fewer channels would slow the movement, not speed it up."),
           ch("The movement of water across the membrane would stop, since potassium channels are the only proteins that water can cross through.", "Water moves through the bilayer and through aquaporins, not through potassium channels.")],
          "Ions such as K⁺ require channel proteins for facilitated diffusion.", difficulty="hard")

    B.mcq(6, "The movement of sodium ions and potassium ions through channel proteins can change the electrical charge difference across a membrane. Which statement best explains why?",
          ch("The ions carry electrical charge, so their net movement changes how the charge is distributed on the two sides of the membrane.", "The membrane can become polarized by the movement of charged ions across it."),
          [ch("The ions are nonpolar, so they bring an electrical charge with them only when they combine with the phospholipids of the bilayer.", "Ions are charged, and the charge does not depend on combining with phospholipids."),
           ch("The channel proteins are made of metal, so they conduct electrical current in the same way that a wire conducts it.", "Channel proteins are not metal. They are made of amino acids."),
           ch("The ions are changed into neutral molecules as they cross the membrane, so a charge difference builds up on one side.", "The ions stay charged as they cross. The movement of charge is what changes the difference.")],
          "Membranes may become polarized by the movement of ions across them.", difficulty="medium")

    # ------------------------------------------------------------------ 2.7 Tonicity and osmoregulation
    B.mcq(7, "A red blood cell is placed in a solution that has a higher concentration of solutes than the cytoplasm of the cell. Which statement is correct?",
          ch("The solution is hypertonic to the cell, so water moves out of the cell by osmosis and the cell shrinks.", "In a hypertonic solution the water potential is lower outside, so water leaves the cell."),
          [ch("The solution is hypotonic to the cell, so water moves out of the cell by osmosis and the cell shrinks.", "A hypotonic solution has a lower solute concentration, and water would move into the cell."),
           ch("The solution is hypertonic to the cell, so water moves into the cell by osmosis and the cell swells and bursts.", "Water moves toward the higher solute concentration, which is outside, so the cell loses water."),
           ch("The solution is isotonic to the cell, so water moves out of the cell by osmosis until the cell is completely empty.", "An isotonic solution has the same solute concentration, and there is no net movement of water.")],
          "Water moves from the hypotonic to the hypertonic side.", difficulty="easy")

    B.mcq(7, "Solution A has a water potential of -2.0 bars and solution B has a water potential of -5.0 bars. The two solutions are separated by a membrane that is permeable to water but not to solutes. What is the net movement of water?",
          ch("From solution A to solution B, because solution A has the higher water potential", "Water moves by osmosis from a region of higher water potential to a region of lower water potential. -2.0 is higher than -5.0."),
          [ch("From solution B to solution A, because solution B has the larger number of the two values when the signs are ignored", "Water potential is compared with the sign, and -5.0 is lower than -2.0."),
           ch("There is no net movement, because the membrane does not allow any solutes to cross from one solution to the other", "The difference in water potential drives the movement of water across the membrane."),
           ch("From solution B to solution A, because water moves toward the region that has the lower solute concentration", "Water moves toward the lower water potential, which is the more negative value of solution B.")],
          "Water moves from high water potential to low water potential.", difficulty="medium")

    B.mcq(7, "A plant cell and an animal cell are each placed in distilled water. Which outcome is most likely?",
          ch("The plant cell becomes firm (turgid) because its cell wall resists the water that enters, and the animal cell may burst.", "Water enters both cells by osmosis. The wall of the plant cell protects it from lysis, but the animal cell has no wall."),
          [ch("The plant cell bursts because its cell wall breaks, and the animal cell becomes firm because it has no wall.", "The cell wall protects plant cells from lysis."),
           ch("Both cells shrink because water moves out of them into the distilled water, which has more water than the cells.", "Distilled water is hypotonic to both cells, so water moves into them."),
           ch("Both cells stay the same size because the distilled water is isotonic to the cytoplasm of both of the cells.", "Distilled water contains no solutes, so it is hypotonic to the cells.")],
          "A cell wall protects plant cells from osmotic lysis in hypotonic solutions.", difficulty="medium")

    i_s, C_s, T_c = 1.0, 0.20, 27
    psi_s = solute_potential(i_s, C_s, T_c)
    assert round(psi_s, 2) == -4.99
    B.mcq(7, f"What is the solute potential of a {C_s:.2f} M sucrose solution at {T_c} °C? (Ψₛ = -iCRT, where i = 1.0 for sucrose, and R = 0.0831 L bar / mol K.)",
          ch("-4.99 bars", "T = 27 + 273 = 300 K, so Ψₛ = -(1.0)(0.20)(0.0831)(300) = -4.99 bars.", round(psi_s, 2)),
          [ch("+4.99 bars", "The solute potential of a solution is negative. The equation has a minus sign.", 4.99),
           ch("-0.45 bars", "This uses the temperature in degrees Celsius (27) instead of kelvin (300).", round(solute_potential(1, 0.2, 0) / 273 * 27, 2)),
           ch("-9.97 bars", "This uses i = 2, which is the ionization constant for a substance that separates into two ions, such as sodium chloride. Sucrose does not ionize, so i = 1.", round(solute_potential(2, 0.2, 27), 2))],
          "Solute potential = -iCRT, with the temperature in kelvin.", difficulty="medium")

    psiP, psiS_cell, psiS_sol = 2.0, -6.5, -4.0
    psi_cell, psi_sol = psiP + psiS_cell, 0.0 + psiS_sol
    assert (psi_cell, psi_sol) == (-4.5, -4.0)
    B.mcq(7, "A plant cell has a pressure potential of +2.0 bars and a solute potential of -6.5 bars. It is placed in an open beaker that contains a solution with a solute potential of -4.0 bars. In which direction is there a net movement of water?",
          ch("Into the cell, because the solution has a water potential of -4.0 bars, which is higher than that of the cell (-4.5 bars)", "Water potential = pressure potential + solute potential. The cell is at +2.0 + (-6.5) = -4.5 bars and the solution (pressure potential of zero in an open beaker) is at -4.0 bars."),
          [ch("Out of the cell, because the water potential of the cell, -4.5 bars, is higher than the water potential of the solution, -4.0 bars", "-4.5 is lower than -4.0, so the cell has the lower water potential and water moves into it."),
           ch("There is no net movement, because the pressure potential of the cell balances out the solute potential of the cell", "The cell has a total water potential of -4.5 bars, not zero, and it differs from the solution."),
           ch("Out of the cell, because the positive pressure potential of +2.0 bars pushes water out through the plasma membrane", "Pressure potential is part of the water potential of the cell, and the total is -4.5 bars, which is lower than that of the solution.")],
          "Water moves from the higher total water potential to the lower one.", difficulty="hard")

    conc = [0.0, 0.2, 0.4, 0.6, 0.8]
    pct = [18.0, 9.0, 1.0, -8.0, -15.0]
    iso = conc[2] + (pct[2] - 0.0) / (pct[2] - pct[3]) * (conc[3] - conc[2])
    assert round(iso, 2) == 0.42
    B.mcq(7, "Potato cores of the same initial mass were placed in sucrose solutions of different concentrations for 24 hours, and the percent change in mass of each core was measured, as shown in the table. Which concentration of sucrose is closest to the solute concentration inside the cells of the potato?",
          ch("0.42 M, the concentration at which a straight line through the data points for 0.4 M and 0.6 M shows no change in mass", "The cores neither gained nor lost mass when the solution was isotonic to the cells. Between 0.4 M (+1.0 percent) and 0.6 M (-8.0 percent), the change in mass is zero at about 0.42 M.", round(iso, 2)),
          [ch("0.50 M, the concentration that is halfway between the two concentrations at which the mass changed from a gain to a loss", "The point of no change is closer to 0.4 M, since the gain at 0.4 M (+1.0) is much smaller than the loss at 0.6 M (-8.0).", 0.50),
           ch("0.40 M, the concentration of the tested solution at which the percent change in mass has the smallest absolute value", "This is the nearest tested value, but the line through the data crosses zero a little above 0.4 M, at about 0.42 M.", 0.40),
           ch("0.00 M, the concentration at which the potato cores had the largest change in mass because of the water they took up", "At 0.0 M the cores gained the most water, so that solution was the most hypotonic to the cells.", 0.0)],
          "The solution that is isotonic to the cells is the one in which the mass does not change; interpolate between the data points.",
          diagram=table(["Sucrose concentration (M)", "Percent change in mass"], [(fix(c_, 1), f"{p_:+.1f}") for c_, p_ in zip(conc, pct)], caption="Potato cores in sucrose solutions"), difficulty="hard")

    B.mcq(7, "Freshwater protists that live in ponds have a structure called a contractile vacuole. Which statement best explains why they need it?",
          ch("The cytoplasm of the protist is hypertonic to the pond water, so water enters by osmosis and the contractile vacuole pumps the excess out.", "Osmoregulation lets organisms control their water balance. In fresh water, water moves into the cell by osmosis."),
          [ch("The cytoplasm of the protist is hypotonic to the pond water, so water enters by osmosis and the vacuole pumps the water out.", "If the cytoplasm were hypotonic to the pond water, water would move out of the cell."),
           ch("The pond water is hypertonic to the cytoplasm, so water leaves the cell by osmosis and the vacuole stores the extra water.", "Pond water is dilute, so it is hypotonic to the cytoplasm and water enters the cell."),
           ch("The cytoplasm and the pond water are isotonic, so the vacuole is needed to move water against a gradient that does not exist.", "In an isotonic solution no net movement of water occurs, and no vacuole would be needed.")],
          "A contractile vacuole removes the water that enters a freshwater protist by osmosis.", difficulty="medium")

    B.mcq(7, "A plant cell is placed in a solution that is hypertonic to the cell. Which description of the cell is correct?",
          ch("Water leaves the cell, the plasma membrane pulls away from the cell wall, and the pressure potential of the cell decreases.", "Water leaves a plant cell in a hypertonic solution, so the cell loses turgor pressure and the membrane shrinks away from the wall."),
          [ch("Water enters the cell, the plasma membrane presses against the cell wall, and the pressure potential of the cell increases.", "This describes a plant cell in a hypotonic solution."),
           ch("Water leaves the cell, the plasma membrane presses against the cell wall, and the pressure potential of the cell increases.", "A cell that loses water loses pressure and does not press against the wall."),
           ch("There is no net movement of water, the plasma membrane stays in contact with the cell wall, and the cell stays the same.", "A hypertonic solution causes a net loss of water from the cell.")],
          "In a hypertonic solution a plant cell loses water and turgor pressure.", difficulty="medium")

    B.mcq(7, "A cell is placed in a solution that is isotonic to its cytoplasm. Which statement about the movement of water is correct?",
          ch("Water molecules move across the membrane in both directions at equal rates, so there is no net movement of water.", "In an isotonic solution the water potentials are equal, so water moves into and out of the cell at the same rate."),
          [ch("Water molecules do not cross the membrane at all, because the solute concentrations on both sides of it are equal.", "Water molecules still move across the membrane. There is no net movement."),
           ch("Water molecules move only into the cell, because the cell has a larger number of solutes than the solution has.", "The solute concentrations are equal in an isotonic solution."),
           ch("Water molecules move only out of the cell, because the solution has a higher water potential than the cytoplasm has.", "In an isotonic solution the water potentials are the same.")],
          "In an isotonic solution there is no net movement of water.", difficulty="easy")

    means = [15.2, 3.1, -9.4]
    errs = [1.6, 1.4, 1.8]
    cats = ["0.0 M", "0.3 M", "0.6 M"]
    lo = [m - e for m, e in zip(means, errs)]
    hi = [m + e for m, e in zip(means, errs)]
    assert lo[0] > hi[1] and lo[1] > hi[2]
    B.mcq(7, "The graph shows the mean percent change in mass of beet cores after 24 hours in three sucrose solutions. Each mean is from six cores, and the error bars show plus and minus 2 standard errors of the mean. Which conclusion is best supported by the data?",
          ch("The mean change in mass differs among the three solutions, because none of the error bars overlap, and the cores lost mass in the 0.6 M solution.", "Because the error bars do not overlap, the differences between the means are unlikely to be due to chance. The negative value means a loss of mass."),
          [ch("The mean change in mass is not different between the 0.0 M and 0.3 M solutions, because both of the means are above zero and so must be the same.", "Both means are above zero, but the error bars do not overlap, so the two means differ."),
           ch("The cores lost mass in all three solutions, because the 0.6 M solution has the largest error bar of the three.", "Only the 0.6 M solution shows a loss of mass. The size of an error bar does not tell the direction of a change."),
           ch("The cores took up water in the 0.6 M solution, because the solution contains the largest amount of dissolved sucrose.", "The 0.6 M solution is hypertonic to the cells, so the cores lost water and mass.")],
          "Error bars that do not overlap suggest real differences between the means.",
          diagram=bars("Sucrose concentration", "Mean change in mass (%)", 20, cats, [{"values": means, "errors": errs, "color": "green"}], y_min=-20), difficulty="hard")

    B.mcq(7, "A plant cell that is turgid in distilled water is moved to a 0.5 M sucrose solution. Which prediction is best supported by what is known about osmosis?",
          ch("Water will leave the cell by osmosis, and the pressure potential of the cell will decrease.", "The solution has a lower water potential than the cell, so water leaves and the cell loses turgor pressure."),
          [ch("Water will enter the cell by osmosis, and the pressure potential of the cell will increase.", "Water enters when the solution is hypotonic, and this solution is hypertonic."),
           ch("Water will leave the cell by osmosis, and the pressure potential of the cell will increase.", "A cell that loses water loses pressure, not gains it."),
           ch("Water will not move, because the cell wall prevents water from crossing in either direction.", "The cell wall does not stop water crossing. It resists the swelling of the cell.")],
          "Moving a plant cell to a hypertonic solution makes it lose water and turgor.", difficulty="hard")

    B.mcq(7, "Which statement best describes osmoregulation?",
          ch("It is the set of mechanisms that organisms use to control their water balance and their internal solute concentration.", "Osmoregulation maintains water balance and lets organisms control their internal solute composition and water potential."),
          [ch("It is the movement of solutes into a cell by active transport, which is the only way that water balance can be controlled.", "Osmoregulation involves control of water and solutes, and active transport is not the only mechanism."),
           ch("It is the movement of water out of a cell by osmosis until the solute concentration in the cell is the same as it is outside.", "Osmoregulation is the control of water balance and does not just mean water leaving a cell until the concentrations are equal."),
           ch("It is the production of new cells to replace those that have burst, which keeps the total volume of an organism constant.", "Osmoregulation controls water and solutes in cells. It is not the replacement of cells.")],
          "Osmoregulation maintains water balance and control of solute composition.", difficulty="medium")

    # ------------------------------------------------------------------ 2.8 Mechanisms of transport
    B.mcq(8, "What is needed to move ions across a membrane by active transport?",
          ch("Metabolic energy, such as ATP, and a membrane protein that carries out the transport", "Active transport requires metabolic energy and membrane proteins."),
          [ch("A concentration gradient only, because the ions move across the membrane because of their concentration difference", "Movement driven only by a concentration gradient is passive transport."),
           ch("A lipid bilayer only, because the ions dissolve in the hydrophobic interior and move through it using the energy of the ions", "Ions do not dissolve in the hydrophobic interior, and active transport needs energy and proteins."),
           ch("A cell wall only, because the wall pushes the ions across the membrane by applying pressure to the cell", "A cell wall does not move ions across the membrane.")],
          "Active transport requires metabolic energy and membrane proteins.", difficulty="easy")

    B.mcq(8, "Which statement best describes the function of the sodium-potassium pump (Na⁺/K⁺ ATPase) in an animal cell?",
          ch("It uses energy from ATP to move sodium ions and potassium ions across the membrane against their gradients, which helps maintain the membrane potential.", "The pump is a membrane protein that uses ATP for active transport, and it contributes to the membrane potential."),
          [ch("It allows sodium ions and potassium ions to move down their concentration gradients without using energy, which uses up the membrane potential.", "This describes channel proteins, not the pump, and the pump helps to maintain the membrane potential."),
           ch("It uses energy from ATP to move water across the membrane against its concentration gradient, which maintains the volume of the cell.", "The pump moves ions. Water moves by osmosis."),
           ch("It makes ATP by letting sodium ions and potassium ions move through the membrane, which provides energy for other cell processes.", "The pump uses ATP. It does not make it.")],
          "The Na⁺/K⁺ pump is an ATPase that carries out active transport and maintains the membrane potential.", difficulty="medium")

    B.mcq(8, "A poison stops a nerve cell from making ATP. Which prediction about the concentrations of sodium ions and potassium ions across its membrane is most consistent with what is known about active transport?",
          ch("The concentration gradients of the ions will gradually decrease, because ions move down their gradients through channels and the pumps no longer work.", "Active transport maintains the gradients. Without ATP the pumps stop, and ions move down their gradients."),
          [ch("The concentration gradients of the ions will increase, because the pumps continue to move ions after the ATP has been used up in the cell.", "The pumps need ATP, so they stop working without it."),
           ch("The concentration gradients of the ions will not change, because ions cannot cross the membrane without the action of a pump.", "Ions leak across the membrane through channels, so the gradients decrease without pumping."),
           ch("The concentration gradients of the ions will reverse at once, because the poison turns the pumps into channel proteins.", "The poison stops the production of ATP. It does not change the proteins into channels.")],
          "Active transport requires energy to maintain gradients, so the gradients dissipate when ATP production stops.", difficulty="medium")

    inh_rows = [("Without the inhibitor", "0.10", "5.2"), ("With a chemical that stops ATP production", "0.10", "0.1")]
    B.mcq(8, "Cells were placed in a solution that contained 0.10 mM of a molecule, and the concentration of the molecule inside the cells was measured after 30 minutes, with and without a chemical that stops the production of ATP, as shown in the table. Which conclusion is best supported by the data?",
          ch("The molecule is probably taken into the cells by active transport, because uptake against the concentration gradient required ATP.", "Without the inhibitor the cells accumulated the molecule to a concentration inside that was about 50 times the concentration outside. This did not occur when ATP production was stopped."),
          [ch("The molecule is probably taken into the cells by simple diffusion, because the concentration inside the cells became higher than outside.", "Simple diffusion would move the molecule down its gradient, so it could not raise the concentration inside above the outside concentration."),
           ch("The molecule is probably taken into the cells by facilitated diffusion, because the chemical had no effect on the uptake.", "The chemical greatly reduced the uptake, so energy was needed."),
           ch("The molecule is probably not taken into the cells, because the concentration inside was 0.1 mM when ATP production was stopped.", "The concentration inside was 5.2 mM when ATP was available, so the molecule is taken in.")],
          "Uptake against a gradient that depends on ATP indicates active transport.",
          diagram=table(["Condition", "Concentration outside (mM)", "Concentration inside after 30 min (mM)"], inh_rows, caption="Uptake of a molecule by cells", row_headers=True), difficulty="hard")

    B.mcq(8, "Why must a cell continuously use energy to maintain a sodium ion concentration gradient across its plasma membrane?",
          ch("Sodium ions leak back across the membrane through channels, down their gradient, so the pumps must keep moving them out.", "Ions tend to move down their gradients, so gradients and the electrochemical gradient need constant active transport to be maintained."),
          [ch("Sodium ions are made inside the cell by the pumps, so the pumps must keep supplying the cell with new sodium ions all the time.", "The pumps move ions that already exist and do not make them."),
           ch("Sodium ions become denatured over time, so the pumps must keep replacing the old sodium ions with new ones.", "Ions are not denatured. They move across the membrane."),
           ch("Sodium ions are not able to cross the membrane in either direction, so the gradient would stay the same without energy.", "Ions can cross the membrane through channels, which is why the gradient decays without pumping.")],
          "Metabolic energy is needed to establish and maintain electrochemical gradients.", difficulty="hard")

    B.mcq(8, "A researcher studies a membrane protein that moves a substance across the membrane. Which observation would best indicate that the protein is an ATP-powered pump rather than a channel?",
          ch("The substance moves against its concentration gradient, and the movement stops when the supply of ATP is removed.", "A pump uses ATP to move a substance against its gradient. A channel allows only movement down the gradient."),
          [ch("The substance moves down its concentration gradient, and the movement continues at the same rate when the supply of ATP is removed.", "This is what is expected for a channel or a transport protein for passive transport."),
           ch("The substance moves in both directions at the same rate, and the movement does not depend on the concentration on either side.", "This does not show that the protein uses ATP."),
           ch("The substance moves more quickly when the temperature is lowered, and the movement stops when the membrane is made thinner.", "Neither observation shows that the protein uses ATP to move the substance.")],
          "Active transport needs ATP and can move a substance against its gradient.", difficulty="hard")
