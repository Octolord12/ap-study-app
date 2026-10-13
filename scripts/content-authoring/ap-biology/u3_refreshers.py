"""Writes content/ap-biology/refreshers/unit-3.json (five refreshers, one per topic). Layout of every refresher: ### The idea, ### Key facts,
### Watch out for, ### Worked example. Facts are the CED's required content for the topic; every number in a worked example is asserted below.
Avoid a lone dollar sign, single-asterisk italics and em dashes. Edit this script, not the JSON. Run: python3 u3_refreshers.py"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import refreshers_lib

# worked-example numbers
assert 120 - 30 == 90 and 60 - 30 == 30 and 90 - 30 == 60
assert (8.0 - 6.0) / (8 - 4) == 0.5 and 6.0 / 4 == 1.5
assert 1000 - 400 == 600
assert 10 ** (8.0 - 5.0) == 1000
assert abs((4.2 - 0.2) - 4.0) < 1e-9 and abs((4.2 - 0.2) / 20 - 0.20) < 1e-9

ENTRIES = [
("enzymes", r"""
### The idea
Enzymes are protein catalysts. They speed up the chemical reactions of a cell by lowering the activation energy, the energy barrier the reactants must cross before they can form products. Each enzyme has an active site whose shape and charge fit its substrate, so an enzyme acts on only one or a few kinds of molecule. The substrate binds at the active site to form a temporary enzyme-substrate complex, the reaction takes place, and the products are released. The enzyme is unchanged and can be used again.

### Key facts
- An enzyme lowers the activation energy. It does not supply energy, and it does not change the energy of the reactants or of the products.
- An enzyme is not used up. One enzyme molecule can catalyze the same reaction many times.
- The substrate must be compatible with the active site in shape and charge. Changing one active-site amino acid can change how well the substrate binds.
- A good enzyme experiment names the independent variable (what is changed), the dependent variable (what is measured, such as product formed per minute) and the controlled variables (what is kept the same). A negative control has no enzyme, or enzyme that has been boiled.

### Watch out for
Saying that an enzyme "gives energy" to a reaction or "is used up". Both are wrong. On a free-energy graph, an enzyme lowers the peak (the activation energy), but the starting and ending levels stay the same.

### Worked example
Prompt: "A graph shows a reaction's free energy rising from 30 to 120 kJ/mol and then falling to 0 without an enzyme, and rising only to 60 kJ/mol with an enzyme. By how much does the enzyme lower the activation energy?"

Without the enzyme the activation energy is 120 - 30 = 90 kJ/mol. With it, the activation energy is 60 - 30 = 30 kJ/mol. The enzyme lowers it by 90 - 30 = 60 kJ/mol, and the energy released by the reaction (30 kJ/mol) is the same either way.
"""),
("environmental-impacts-on-enzyme-function", r"""
### The idea
An enzyme works only while its three-dimensional shape is intact. Temperature, pH and the chemical environment can change that shape (denaturation) or change how often enzyme and substrate meet, so they change the rate of the reaction. Every enzyme has an optimum, such as pH 2 for pepsin, and its activity falls on either side of it.

### Key facts
- **Temperature.** Up to the optimum, higher temperature makes molecules move faster and collide more often, so the rate rises. Above the optimum, hydrogen bonds are disrupted, the enzyme is denatured and the rate drops sharply.
- **pH.** A pH far from the optimum changes the charges and bonds that hold the enzyme's shape, so activity falls.
- **Denaturation** is sometimes reversible: a mildly disrupted enzyme can refold and regain activity when conditions return to normal. Severe disruption is not reversible.
- **Substrate concentration.** The rate rises with substrate until the enzyme is saturated and then levels off. A reaction slows over time as substrate is used up and product builds up.
- **Inhibitors.** A competitive inhibitor binds the active site reversibly, and extra substrate can overcome it. A noncompetitive inhibitor binds an allosteric site and changes the enzyme's activity, and extra substrate cannot overcome it.

### Watch out for
Reading a lower rate at high temperature as only "slower": it is usually denaturation. On an inhibitor graph, check what happens at high substrate. If the maximum rate comes back, think competitive. If it does not, think noncompetitive.

### Worked example
Prompt: "Product concentration is 6.0 mM at 4 min and 8.0 mM at 8 min. What is the average rate between 4 and 8 min?"

Rate = change in product / change in time = (8.0 - 6.0) mM / (8 - 4) min = 0.50 mM/min. This is lower than the rate over the first 4 minutes (6.0 / 4 = 1.5 mM/min) because substrate has been used up and product has built up.
"""),
("cellular-energy", r"""
### The idea
Living cells are highly ordered, and keeping that order takes a constant input of energy. Cells do not break the laws of thermodynamics. Energy is conserved (the first law), and the order inside a cell is paid for by energy input and by the heat the cell releases, which increases the disorder of its surroundings (the second law).

### Key facts
- Energy input must exceed energy loss for a cell to keep its order and power its processes. A major loss of order or of energy flow results in death.
- Energy-releasing processes can be coupled to energy-requiring ones. ATP hydrolysis is the usual example: the energy it releases drives processes such as active transport and the building of large molecules.
- Metabolic pathways are made of steps. The product of one step is typically the reactant of the next, which allows a more controlled transfer of energy.
- Core pathways such as glycolysis and oxidative phosphorylation are found in Bacteria, Archaea and Eukarya. A pathway shared by all three domains is evidence of common ancestry.
- The Gibbs free energy equation is not tested.

### Watch out for
Saying that cells "make" energy. Cells transfer energy from food or light to forms such as ATP, and some is always lost as heat. Also, an enzyme lowers the activation energy but supplies no energy, so a reaction that needs energy must be coupled to one that releases it.

### Worked example
Prompt: "A cell takes in 1,000 J of food energy and transfers 400 J of it to ATP. What happens to the rest?"

Energy is conserved, so the other 1,000 - 400 = 600 J is transferred to the surroundings, mostly as heat. The cell keeps its order because its energy input is larger than what it loses, and the heat it gives off increases the disorder of the surroundings, so the second law is not violated.
"""),
("photosynthesis", r"""
### The idea
Photosynthesis uses light energy to build carbohydrates from carbon dioxide and water, and it releases oxygen. In eukaryotes it takes place in chloroplasts in two linked stages. The light reactions, in the thylakoid membranes, capture light energy as ATP and NADPH. The Calvin cycle, in the stroma, uses that ATP and NADPH to make carbohydrates from CO₂.

### Key facts
- The overall inputs are CO₂, H₂O and light, and the outputs are carbohydrates and O₂. The O₂ released comes from water that is split at photosystem II.
- Photosystem II absorbs light, and water splits to replace its electrons. The electrons pass along an electron transport chain to photosystem I and are then transferred to NADP⁺, which is reduced to NADPH.
- As electrons pass along the chain, protons are moved into the thylakoid lumen. The lumen has a high proton concentration (low pH) and the stroma a low one.
- Protons flow back to the stroma through ATP synthase, which makes ATP by chemiosmosis (photophosphorylation).
- Photosynthesis first evolved in prokaryotes, and cyanobacteria added oxygen to the early atmosphere.
- The steps of the Calvin cycle and the names of its enzymes are not tested.

### Watch out for
Thinking the oxygen comes from CO₂, that only plants photosynthesize, or that the Calvin cycle uses light directly. In the dark, the Calvin cycle slows because the ATP and NADPH are not replaced.

### Worked example
Prompt: "In illuminated chloroplasts the pH of the thylakoid lumen is 5.0 and the pH of the stroma is 8.0. How many times greater is the hydrogen ion concentration in the lumen?"

The pH scale is logarithmic, so a difference of 3 pH units is a difference of 10³ = 1,000 times. The lumen has 1,000 times the concentration of H⁺ that the stroma has, which is the gradient that ATP synthase uses.
"""),
("cellular-respiration", r"""
### The idea
Cells release the energy stored in molecules such as glucose and use it to make ATP. All forms of life use respiration or fermentation. In aerobic respiration in a eukaryote, glycolysis in the cytosol is followed by the Krebs cycle in the mitochondrial matrix, and then by the electron transport chain (ETC) and ATP synthase in the inner mitochondrial membrane.

### Key facts
- Glycolysis, in the cytosol, converts glucose to pyruvate and forms ATP and NADH. It does not need oxygen.
- The Krebs cycle, in the matrix, releases CO₂ and transfers electrons to NAD⁺ and FAD, forming NADH and FADH₂ and a little ATP.
- NADH and FADH₂ deliver electrons to the ETC. Oxygen is the final electron acceptor and is reduced to water.
- The ETC moves protons into the intermembrane space, which then has the higher proton concentration (lower pH), while the matrix has the higher pH. Protons flow back through ATP synthase, which makes ATP (oxidative phosphorylation).
- The folded inner membrane has a large surface area, so more ATP can be made. Decoupling the gradient from ATP synthesis releases heat.
- Fermentation lets glycolysis continue without oxygen and forms lactic acid, or ethanol and CO₂. Aerobic prokaryotes pump protons across their plasma membrane.

### Watch out for
The idea that only animals respire. Plants, fungi and prokaryotes do too. In a respirometer or similar experiment, a rate is an amount divided by time, and the control must be subtracted before you divide.

### Worked example
Prompt: "Germinating peas consume 4.2 mL of O₂ in 20 min. Glass beads used as a control change by 0.2 mL. What is the corrected rate?"

Corrected volume = 4.2 - 0.2 = 4.0 mL. Rate = 4.0 mL / 20 min = 0.20 mL/min.
"""),
]

refreshers_lib.write("ap-biology", 3, ENTRIES)
