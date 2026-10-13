"""Unit 2, topics 2.3 Plasma Membrane (8 questions), 2.4 Membrane Permeability (8) and 2.5 Membrane Transport (8).

Required content (CED 2025-26): 2.3.A phospholipids have hydrophilic phosphate regions facing the aqueous inside and outside and hydrophobic fatty acid regions facing each other in the
interior; embedded proteins can be hydrophilic, hydrophobic or both (hydrophobic regions contact the fatty acids); 2.3.B the fluid mosaic model: phospholipids embedded with proteins,
steroids such as cholesterol, glycoproteins and glycolipids, all able to move within the membrane. 2.4.A selective permeability results from the hydrophobic interior; small nonpolar molecules
(N2, O2, CO2) pass freely, hydrophilic substances (large polar molecules, ions) need channels and transport proteins, small polar uncharged molecules (H2O, NH3) cross in small amounts;
2.4.B cell walls of Bacteria, Archaea, Fungi and plants are a structural boundary, a permeability barrier and protect from osmotic lysis. 2.5.A concentration gradients form because of
selective permeability; passive transport is net movement from high to low concentration without direct metabolic energy; active transport needs direct energy and can move molecules from low to
high; 2.5.B endocytosis (the membrane folds in and forms vesicles) and exocytosis (vesicles fuse with the plasma membrane) need energy. Suggested skills: 2.A, 5.D (evaluate a hypothesis), 3.D.
"""
from lib import *


def build(B):
    # ------------------------------------------------------------------ 2.3 Plasma membrane
    B.mcq(3, "In a phospholipid bilayer, how are the phospholipid molecules arranged?",
          ch("The hydrophilic phosphate regions face the watery environments inside and outside the cell, and the fatty acid tails face each other in the interior.", "The polar heads are oriented toward the aqueous surroundings and the nonpolar tails are shielded from water in the middle of the bilayer."),
          [ch("The hydrophobic fatty acid tails face the watery environments inside and outside the cell, and the hydrophilic phosphate regions face each other.", "This reverses the arrangement. Hydrophobic tails face away from water."),
           ch("All of the phospholipid molecules lie flat with their heads and tails mixed together in a single layer on the surface of the cell.", "A bilayer has two layers, with the tails of the two layers facing each other."),
           ch("The phospholipids are arranged in a single layer with their hydrophilic heads pointing toward the cytoplasm and their tails toward the outside.", "The membrane is a double layer, and the heads of one layer face the outside of the cell.")],
          "Hydrophilic heads face the aqueous environments and hydrophobic tails face each other inside the membrane.", difficulty="easy")

    B.mcq(3, "Which statement best explains why phospholipids in water form a bilayer?",
          ch("The nonpolar fatty acid tails are hydrophobic and cluster together away from water, while the polar phosphate heads interact with water.", "The two regions of a phospholipid behave differently in water, which produces the bilayer arrangement."),
          [ch("The polar phosphate heads are hydrophobic and cluster together away from water, while the nonpolar fatty acid tails interact with water.", "The phosphate heads are the hydrophilic part and the fatty acid tails are the hydrophobic part."),
           ch("The phospholipids are held together by covalent bonds that join the tails of one molecule to the heads of the next molecule.", "A bilayer is held together by weaker interactions. Phospholipids are not joined by covalent bonds to each other."),
           ch("The phospholipids are attracted to the proteins in the membrane, and these proteins form a fixed frame that holds the layers in place.", "The bilayer forms because of the hydrophilic and hydrophobic regions of the phospholipids.")],
          "Phospholipids have both hydrophilic and hydrophobic regions, which determines their arrangement in water.", difficulty="medium")

    B.mcq(3, "Which regions of a protein embedded in a plasma membrane interact with the fatty acid tails in the interior of the membrane?",
          ch("Hydrophobic regions, which have nonpolar side groups and make up the surface of the protein within the membrane interior", "The hydrophobic regions of an embedded protein interact with the fatty acid tails of the phospholipids."),
          [ch("Hydrophilic regions, which have charged and polar side groups and make up the surface of the protein within the membrane interior", "Hydrophilic regions are inside the protein or exposed to the cytosol, not in contact with the fatty acid tails."),
           ch("Regions made only of ionic side groups, which form strong bonds with the fatty acid tails in the interior of the membrane", "Ionic groups are hydrophilic and do not interact with the nonpolar tails."),
           ch("Regions made of phosphate groups, which are covalently bonded to the fatty acid tails in the interior of the membrane", "Phosphate groups are part of the phospholipid heads and are not found in proteins in this way.")],
          "The hydrophobic regions of membrane proteins face the fatty acid tails.", difficulty="medium")

    B.mcq(3, "Which statement best describes the fluid mosaic model of the plasma membrane?",
          ch("The membrane is a framework of phospholipids embedded with proteins and other molecules that can move around within it.", "The model describes a flexible structure in which the components can move, like pieces in a mosaic that is fluid."),
          [ch("The membrane is a rigid sheet of protein that is coated with phospholipids, and none of its parts can move from place to place.", "In the fluid mosaic model, the phospholipids and proteins are not fixed in place."),
           ch("The membrane is a layer of phospholipids that is surrounded on both sides by a continuous layer of protein that does not move.", "The proteins are embedded in the phospholipids, and the components can move."),
           ch("The membrane is a single layer of phospholipids with a few proteins attached to the outside, which can move only along one axis.", "The membrane is a bilayer, with proteins embedded in it, and the components can move across its surface.")],
          "In the fluid mosaic model the components of the membrane can move within it.", difficulty="medium")

    B.mcq(3, "Which choice lists components that are found in the plasma membranes of animal cells?",
          ch("Phospholipids, proteins, cholesterol, glycoproteins and glycolipids", "Plasma membranes have a framework of phospholipids embedded with proteins, steroids such as cholesterol, glycoproteins and glycolipids."),
          [ch("Phospholipids, proteins, starch, glycogen, cellulose and nucleotides", "Starch, glycogen and cellulose are polysaccharides that are not part of the plasma membrane."),
           ch("Proteins, DNA, cholesterol, glycoproteins and ribosomes", "DNA and ribosomes are not components of the plasma membrane."),
           ch("Phospholipids, fatty acids, nucleotides, cellulose and glycolipids", "Nucleotides and cellulose are not components of the plasma membrane.")],
          "Plasma membranes contain phospholipids, proteins, cholesterol, glycoproteins and glycolipids.", difficulty="easy")

    mix_rows = [("37 °C", "0", "42", "100"), ("15 °C", "0", "4", "21")]
    B.mcq(3, "Researchers labeled the membrane proteins of two different cells with two different fluorescent dyes, fused the cells, and then measured the percent of cells in which the two dyes had mixed. The table shows the results at two temperatures. Which conclusion is best supported by the data?",
          ch("Membrane proteins can move within the plasma membrane, and they move more slowly at the lower temperature, consistent with the fluid mosaic model.", "The dyes mixed over time, so the proteins moved in the membrane. Mixing was much slower at 15 °C."),
          [ch("Membrane proteins are fixed in place in the plasma membrane, because the dyes mixed in only some of the cells after 10 minutes.", "The dyes mixed in all of the cells at 37 °C, which shows that proteins can move."),
           ch("Membrane proteins move at the same rate at both temperatures, because the dyes eventually mixed in some of the cells at each temperature.", "The rates differ a great deal: 100 percent mixing at 37 °C after 40 minutes and 21 percent at 15 °C."),
           ch("Membrane proteins move faster at the lower temperature, because the dyes mixed in fewer cells at 15 °C than they did at 37 °C.", "Fewer mixed cells at 15 °C means slower movement, not faster.")],
          "Mixing of the labels shows that membrane proteins move, and the temperature affects the fluidity of the membrane.",
          diagram=table(["Temperature", "Time 0 min (% mixed)", "Time 10 min (% mixed)", "Time 40 min (% mixed)"], mix_rows, caption="Percent of fused cells in which the two dyes had mixed", row_headers=True), difficulty="hard")

    B.mcq(3, "A mutation changes several nonpolar amino acids in the part of a membrane protein that lies within the membrane to polar amino acids. Which prediction is best supported by what is known about membrane proteins?",
          ch("The protein would be less likely to stay embedded, because the altered region would interact poorly with the nonpolar fatty acid tails.", "The region within the membrane is hydrophobic so that it can interact with the fatty acid tails. Polar amino acids there would interact poorly with the interior."),
          [ch("The protein would be more likely to stay embedded, because polar amino acids form stronger bonds with the fatty acid tails.", "Polar amino acids do not interact well with the nonpolar tails."),
           ch("The protein would be unchanged, because the amino acids inside the membrane do not affect how the protein is positioned.", "The properties of the amino acids determine how the protein interacts with its surroundings."),
           ch("The protein would move out of the membrane and into the cell wall, because polar amino acids are always found in cell walls.", "Animal cells have no cell wall, and polar amino acids are not limited to cell walls.")],
          "The hydrophobic regions of membrane proteins interact with the hydrophobic interior of the membrane.", difficulty="hard")

    B.mcq(3, "Which part of a phospholipid molecule is hydrophilic?",
          ch("The polar phosphate region, which is oriented toward the watery environment", "The phosphate region of a phospholipid is polar and hydrophilic."),
          [ch("The long fatty acid tails, which are made of chains of carbon and hydrogen atoms", "The fatty acid tails are nonpolar and hydrophobic."),
           ch("The covalent bonds between the carbon atoms in each of the fatty acid tails", "These bonds are part of the hydrophobic tails."),
           ch("The center of the bilayer, where the two layers of phospholipids meet each other", "The interior of the bilayer is hydrophobic.")],
          "The phosphate head of a phospholipid is hydrophilic; the fatty acid tails are hydrophobic.", difficulty="easy")

    # ------------------------------------------------------------------ 2.4 Membrane permeability
    B.mcq(4, "Which molecules can pass freely across the plasma membrane without the help of proteins?",
          ch("Small nonpolar molecules, such as oxygen, carbon dioxide and nitrogen", "Small nonpolar molecules freely pass across the hydrophobic interior of the membrane."),
          [ch("Charged ions, such as sodium and potassium ions, because they are small", "Ions are charged and cannot cross the hydrophobic interior without channel or transport proteins."),
           ch("Large polar molecules, such as glucose, because they dissolve in water", "Large polar molecules need transport proteins to cross the membrane."),
           ch("Every molecule that is smaller than a protein, because the membrane is full of holes", "The bilayer has no holes. Its hydrophobic interior blocks many small molecules, such as ions.")],
          "Small nonpolar molecules, such as N₂, O₂ and CO₂, pass freely through the membrane.", difficulty="easy")

    B.mcq(4, "Which molecules cross the plasma membrane through embedded channel proteins and transport proteins?",
          ch("Hydrophilic substances, such as ions and large polar molecules", "Hydrophilic substances cannot cross the hydrophobic interior directly, so they move through channels and transport proteins."),
          [ch("Small nonpolar molecules, such as oxygen and carbon dioxide", "These pass freely through the membrane without help."),
           ch("Only the phospholipids that make up the membrane, as they move from one cell to another", "Phospholipids are a part of the membrane and are not transported across it by channel proteins."),
           ch("Only the fatty acids that make up the tails of the phospholipids in the bilayer", "Fatty acids are a part of the membrane lipids. They are not moved by channel proteins.")],
          "Ions and large polar molecules need channels and transport proteins.", difficulty="easy")

    B.mcq(4, "Which statement best explains why ions such as Na⁺ cannot pass directly through the lipid bilayer of the plasma membrane?",
          ch("The nonpolar hydrocarbon tails in the interior of the membrane prevent charged particles and polar molecules from crossing.", "The hydrophobic interior is the barrier that makes the membrane selectively permeable."),
          [ch("The polar phosphate heads of the phospholipids attract ions so strongly that they hold them at the surface of the membrane.", "Heads on the surface can interact with ions, but the main barrier is the hydrophobic interior."),
           ch("The ions are too large to fit between the phospholipids, which are packed tightly with no spaces between the heads.", "The barrier is not size alone. The charged ions are blocked by the nonpolar interior."),
           ch("The cell makes enzymes that break down all ions at the surface of the membrane before they have a chance to enter.", "Ions are not broken down by enzymes at the membrane. They are blocked by the hydrophobic interior.")],
          "The nonpolar hydrocarbon tails prevent ions and polar molecules from crossing the membrane.", difficulty="medium")

    perm = [("Oxygen (O₂)", "100"), ("Carbon dioxide (CO₂)", "85"), ("Water (H₂O)", "4"), ("Glucose", "0.1"), ("Sodium ion (Na⁺)", "0.001")]
    B.mcq(4, "The table shows how quickly different substances cross an artificial lipid bilayer that contains no proteins, in arbitrary units. Which conclusion is best supported by the data?",
          ch("Small nonpolar molecules cross the bilayer much faster than polar molecules and ions, consistent with the hydrophobic interior.", "Oxygen and carbon dioxide cross fastest. Water crosses slowly, and glucose and sodium ions cross very slowly."),
          [ch("Small nonpolar molecules cross the bilayer more slowly than polar molecules and ions, because they are repelled by the hydrophilic heads.", "The data show the opposite: oxygen and carbon dioxide have the highest values."),
           ch("All of the substances cross the bilayer at about the same rate, because the bilayer does not have any selective properties.", "The rates range from 100 to 0.001, so the bilayer discriminates among substances."),
           ch("Water cannot cross the bilayer at all, because the rate for water is lower than the rates for the gases in the table.", "The rate for water is not zero. A small amount of water crosses the bilayer.")],
          "A bilayer is selectively permeable, with small nonpolar molecules crossing most easily.",
          diagram=table(["Substance", "Relative rate of crossing the bilayer"], perm, caption="Crossing an artificial bilayer", row_headers=True), difficulty="medium")

    B.mcq(4, "Bacteria, archaea, fungi and plants all have cell walls. Which statement describes a role of the cell wall?",
          ch("It provides a structural boundary and a permeability barrier, and it protects the cell from bursting when water enters.", "Cell walls give structure, act as a barrier for some substances, and protect cells from osmotic lysis."),
          [ch("It makes the plasma membrane selectively permeable, because the cell wall has a hydrophobic interior that blocks ions.", "The hydrophobic interior of the plasma membrane makes it selectively permeable. The cell wall does not do this."),
           ch("It provides the energy that the cell needs, because the cell wall is where the ATP of the cell is made.", "ATP is made in mitochondria or across the plasma membrane. It is not made in the cell wall."),
           ch("It stores the genetic information of the cell, because the cell wall contains the DNA in a protected compartment.", "DNA is not stored in the cell wall.")],
          "Cell walls provide a structural boundary, a permeability barrier and protection from osmotic lysis.", difficulty="medium")

    B.mcq(4, "A bacterium whose cell wall has been removed bursts when it is placed in pure water, but a bacterium with an intact cell wall does not. Which statement best explains the difference?",
          ch("The cell wall gives structure and protects the cell from osmotic lysis, so the intact cell resists the water that enters.", "Water enters the cell by osmosis, and the cell wall prevents the cell from swelling until it bursts."),
          [ch("The cell wall keeps water out of the cell completely, so no water can enter the intact bacterium in pure water.", "Water can cross the cell wall and enter. The wall resists the swelling and bursting of the cell."),
           ch("The cell wall makes the plasma membrane thicker, so the intact bacterium loses water by osmosis instead of gaining it.", "The cell wall does not thicken the plasma membrane, and water moves into the cell in pure water."),
           ch("The cell wall provides the cell with an extra supply of ATP, so the intact bacterium can pump out all of the water.", "The cell wall does not supply ATP.")],
          "The cell wall protects against osmotic lysis.", difficulty="hard")

    B.mcq(4, "A researcher hypothesizes that the hydrophobic interior of the membrane prevents the movement of sodium ions unless a channel protein is present. Which result would best support this hypothesis?",
          ch("An artificial bilayer without proteins is almost impermeable to sodium ions, but the permeability increases greatly when channel proteins for sodium are added.", "This result shows that the lipid bilayer alone blocks the ions and that the channel proteins allow them across."),
          [ch("An artificial bilayer without proteins is highly permeable to sodium ions, and adding channel proteins for sodium has no effect on its permeability.", "This would show that the bilayer does not block the ions."),
           ch("An artificial bilayer without proteins is permeable to sodium ions only when the temperature is raised, and channel proteins make no difference.", "This does not test the role of the interior or of the proteins."),
           ch("An artificial bilayer with channel proteins is less permeable to sodium ions than a bilayer without proteins, since proteins block the ions.", "This would contradict the hypothesis that the channel proteins allow ions through.")],
          "Evidence for a hypothesis comes from a comparison in which only the factor being tested is changed.", difficulty="hard")

    B.mcq(4, "Water is a polar molecule, yet a small amount of water crosses the lipid bilayer of a plasma membrane without the help of any protein. Which statement best explains this?",
          ch("Water is a small polar molecule with no charge, and small polar uncharged molecules can pass through the membrane in small amounts.", "Small, uncharged polar molecules, such as water and ammonia, can slip through the bilayer, although only in small amounts."),
          [ch("Water is a nonpolar molecule when it is in contact with a membrane, so it passes through the hydrophobic interior as easily as oxygen does.", "Water remains polar. It crosses the bilayer far more slowly than small nonpolar molecules do."),
           ch("Water is a charged ion that is attracted to the phosphate heads, so it is carried through the interior of the membrane by the heads.", "Water molecules are not charged, and the interior of the membrane is not crossed by being carried by the heads."),
           ch("Water is too large to enter any channel, so the only way it can cross the membrane is by active transport using energy from ATP.", "Water can cross by passive transport, and aquaporins can carry water in large quantities without direct input of energy.")],
          "Small polar uncharged molecules, such as H\u2082O and NH\u2083, cross the membrane in small amounts.", difficulty="medium")

    # ------------------------------------------------------------------ 2.5 Membrane transport
    B.mcq(5, "Which statement correctly describes passive transport?",
          ch("It is the net movement of molecules from a region of high concentration to one of low concentration without direct input of energy.", "Passive transport moves molecules down their concentration gradient and does not need direct input of energy."),
          [ch("It is the net movement of molecules from a region of low concentration to a region of high concentration using energy from ATP.", "This describes active transport."),
           ch("It is the movement of large particles into the cell by the folding of the plasma membrane to make a vesicle around them.", "This describes endocytosis, which requires energy."),
           ch("It is the movement of molecules in which each molecule must be moved by a protein that is powered directly by the hydrolysis of ATP.", "Passive transport does not directly use the energy of ATP.")],
          "Passive transport is movement down a concentration gradient with no direct input of metabolic energy.", difficulty="easy")

    B.mcq(5, "Which statement correctly describes active transport?",
          ch("It requires a direct input of energy and, in some cases, moves molecules from low concentration to high concentration.", "Active transport uses energy to move molecules, including against their concentration gradients."),
          [ch("It requires no input of energy and always moves molecules from a region of low concentration to a region of high concentration.", "Active transport requires energy, and the direction is not always against the gradient in this way."),
           ch("It requires a direct input of energy and always moves molecules from a region of high concentration to a region of low concentration.", "Active transport can move molecules against a gradient, from low to high concentration."),
           ch("It requires no input of energy and moves molecules only through the phospholipid bilayer and never through proteins.", "Active transport requires energy and it needs membrane proteins.")],
          "Active transport requires a direct input of energy.", difficulty="easy")

    B.mcq(5, "Which feature of the plasma membrane allows concentration gradients of solutes to form across it?",
          ch("The membrane is selectively permeable, so some substances cross it more easily than others.", "Selective permeability allows different concentrations of solutes to be established on the two sides of the membrane."),
          [ch("The membrane is completely permeable, so every substance crosses it at the same rate in both directions.", "If the membrane were completely permeable, gradients could not be maintained."),
           ch("The membrane is completely impermeable, so no substances are able to cross it in either direction at any time.", "A membrane that nothing could cross would not allow the cell to take in nutrients."),
           ch("The membrane is made of a single type of protein, so all of the substances cross it through the same channel.", "The membrane has a phospholipid bilayer with different proteins in it.")],
          "Selective permeability allows concentration gradients to form.", difficulty="medium")

    B.mcq(5, "Which statement correctly describes endocytosis?",
          ch("The cell takes in large molecules or particles by folding the plasma membrane in on itself and forming vesicles that engulf the material.", "In endocytosis, new small vesicles form from the plasma membrane and enclose material from outside the cell."),
          [ch("The cell releases large molecules by fusing vesicles with the plasma membrane so that their contents are secreted to the outside.", "This describes exocytosis."),
           ch("The cell takes in small nonpolar molecules by letting them pass directly through the hydrophobic interior of the membrane.", "Small nonpolar molecules move directly across the membrane by passive transport, and this is not endocytosis."),
           ch("The cell takes in ions by opening channel proteins so that the ions can move down their concentration gradient.", "This describes facilitated diffusion through channel proteins.")],
          "Endocytosis takes material into the cell in vesicles formed from the plasma membrane.", difficulty="medium")

    B.mcq(5, "Cells of the pancreas release the protein hormone insulin into the blood. Which process moves this large molecule out of the cell?",
          ch("Exocytosis, in which vesicles that contain the insulin fuse with the plasma membrane and release their contents", "Exocytosis secretes large molecules by fusion of vesicles with the plasma membrane. It requires energy."),
          [ch("Endocytosis, in which the plasma membrane folds in and forms vesicles that carry the insulin out of the cell", "Endocytosis takes material into the cell."),
           ch("Passive diffusion, in which the insulin passes directly through the hydrophobic interior of the plasma membrane", "Insulin is a large molecule that cannot cross the hydrophobic interior of the membrane by itself."),
           ch("Facilitated diffusion, in which the insulin moves down its gradient through a channel protein in the plasma membrane", "Large molecules such as proteins are too large to pass through channel proteins.")],
          "Exocytosis moves large molecules out of the cell.", difficulty="medium")

    sub_rows = [("Substance P", "2", "20", "Out of the cell"), ("Substance Q", "50", "5", "Into the cell"), ("Substance R", "3", "30", "Into the cell")]
    B.mcq(5, "A researcher measures the concentration of three substances inside and outside a cell and determines the direction of the net movement of each substance across the plasma membrane, as shown in the table. Which substance is most likely moved by active transport?",
          ch("Substance R, because it moves from the lower concentration outside the cell to the higher concentration inside the cell", "Net movement against the concentration gradient requires a direct input of energy."),
          [ch("Substance Q, because it moves from the higher concentration outside the cell to the lower concentration inside the cell", "This is movement down the concentration gradient, which is consistent with passive transport."),
           ch("Substance P, because it moves from the higher concentration inside the cell to the lower concentration outside the cell", "This is also movement down the concentration gradient, which is consistent with passive transport."),
           ch("None of the substances, because the concentrations differ across the membrane for all three substances in the table", "A concentration difference is expected across the membrane and does not rule out active transport.")],
          "Active transport can move a substance against its concentration gradient.",
          diagram=table(["Substance", "Concentration outside (mM)", "Concentration inside (mM)", "Direction of net movement"], sub_rows, caption="Movement of three substances", row_headers=True), difficulty="hard")

    B.mcq(5, "Which of the following processes require a direct input of metabolic energy?",
          ch("Active transport across the membrane, endocytosis and exocytosis", "Active transport, endocytosis and exocytosis require energy."),
          [ch("Facilitated diffusion, osmosis and endocytosis", "Facilitated diffusion and osmosis are passive. Only endocytosis in this list requires energy."),
           ch("The diffusion of oxygen, the diffusion of carbon dioxide and exocytosis", "Diffusion of gases is passive."),
           ch("Osmosis, the diffusion of oxygen and the movement of ions through channels", "All three of these are passive and need no direct input of energy.")],
          "Active transport, endocytosis and exocytosis require energy.", difficulty="medium")

    B.mcq(5, "A researcher wants to test whether a molecule enters cells by active transport. Which investigation would best test this?",
          ch("Measure the uptake of the molecule by cells with and without a chemical that stops ATP production, and see whether uptake against the gradient falls.", "If the uptake against the gradient depends on energy, a metabolic inhibitor will reduce it."),
          [ch("Measure the uptake of the molecule by cells in solutions with different concentrations of salt, and see whether the cells change in size.", "This tests the effects of osmosis on cells, not the role of energy in the movement of the molecule."),
           ch("Measure the uptake of the molecule by two different samples of cells without any treatment, and see whether the uptake is the same.", "Without changing the supply of energy, this cannot show whether the uptake needs energy."),
           ch("Measure the size of the molecule with a microscope, and see whether it is smaller than the largest channel in the membrane.", "The size of the molecule does not show whether it is moved by active transport.")],
          "To test whether transport needs energy, compare uptake with and without a block on energy supply.", difficulty="hard")
