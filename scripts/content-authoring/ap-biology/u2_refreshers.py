"""Writes content/ap-biology/refreshers/unit-2.json (ten refreshers, one per topic). Layout: ### The idea, ### Key facts, ### Watch out for, ### Worked example.
Facts are the CED's required content for each topic; every number in a worked example is asserted. Avoid a lone dollar sign, single-asterisk italics and
em dashes. Edit this script, not the JSON. Run: python3 u2_refreshers.py"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import refreshers_lib

# worked-example numbers
assert (6 * 3**2) / 3**3 == 2.0
assert round(-1.0 * 0.20 * 0.0831 * (27 + 273), 2) == -4.99
assert 2.0 + (-6.5) == -4.5

ENTRIES = [
("cell-structure-and-function", r"""
### The idea
Each part of a cell has a structure that suits its function. Ribosomes build proteins. The endomembrane system, a group of membrane-bound structures that work together, modifies, packages and moves proteins, lipids and polysaccharides. Mitochondria release energy for the cell, and in plants and algae chloroplasts capture it.

### Key facts
- **Ribosomes** are made of rRNA and protein, have no membrane, and make proteins according to messenger RNA. They are found in all forms of life, which reflects common ancestry.
- **The endomembrane system** includes the endoplasmic reticulum (ER), the Golgi complex, lysosomes, vacuoles and transport vesicles, the nuclear envelope and the plasma membrane.
- **Rough ER** has ribosomes attached and helps carry out protein synthesis. **Smooth ER** detoxifies cells and makes lipids.
- **Golgi complex:** flattened sacs that fold and chemically modify new products and package proteins for trafficking.
- **Mitochondria** have a double membrane, and the folded inner membrane lets ATP be made more efficiently. **Chloroplasts** also have a double membrane and carry out photosynthesis.
- **Lysosomes** hold hydrolytic enzymes that digest material and take part in programmed cell death. A large plant vacuole stores water and nutrients and maintains turgor pressure.

### Watch out for
Giving ribosomes a membrane, or placing mitochondria in the endomembrane system. Neither is correct: ribosomes are not membrane-bound, and mitochondria and chloroplasts are not part of the endomembrane system.

### Worked example
Prompt: "Describe the path of a protein that is secreted from a cell."

The protein is made by ribosomes on the rough ER and enters the ER. A transport vesicle carries it to the Golgi complex, which modifies and packages it. A secretory vesicle then carries it to the plasma membrane, where the vesicle fuses with the membrane and releases the protein from the cell.
"""),
("cell-size", r"""
### The idea
A cell takes in nutrients and gets rid of waste across its plasma membrane, so the amount of membrane compared with the volume of the cell matters. This is the surface area-to-volume ratio. As a cell grows, its volume increases faster than its surface area, so the ratio falls and the cell finds it harder to exchange materials. This limits the size of cells.

### Key facts
- **Smaller cells** typically have a higher surface area-to-volume ratio and a more efficient exchange of materials with the environment.
- If a sphere's radius doubles, its surface area becomes four times larger and its volume eight times larger, so the ratio falls to one half.
- Folds and projections of the membrane, such as microvilli, increase the surface area without adding much volume.
- The same idea applies to organisms: smaller organisms lose heat faster for their mass and typically have a higher metabolic rate per unit of body mass.
- The equations are on the AP sheet: surface area of a cube 6s² and volume s³; surface area of a sphere 4πr² and volume 4/3 πr³.

### Watch out for
Inverting the ratio. It is surface area divided by volume, so for a cube it is 6 divided by the side length, and it gets smaller as the cube gets bigger. Remember the units: per micrometer, or per centimeter.

### Worked example
Prompt: "What is the surface area-to-volume ratio of a cube-shaped cell with sides of 3 µm?"

Surface area = 6 x 3² = 54 µm² and volume = 3³ = 27 µm³. The ratio is 54 / 27 = 2.0 per µm. A cube with sides of 6 µm would have a ratio of only 1.0 per µm, so it would be less efficient at exchanging materials.
"""),
("plasma-membrane", r"""
### The idea
The plasma membrane is a bilayer of phospholipids with proteins and other molecules embedded in it. Because each phospholipid has a hydrophilic region and a hydrophobic region, the molecules arrange themselves so that the hydrophilic regions face the watery surroundings and the hydrophobic regions face each other inside. The fluid mosaic model describes the membrane as a flexible structure whose parts can move.

### Key facts
- **Phospholipids:** the polar, hydrophilic phosphate regions face the watery environment inside and outside the cell. The nonpolar, hydrophobic fatty acid tails face each other in the interior.
- **Embedded proteins** can be hydrophilic, hydrophobic or both. Their hydrophobic regions interact with the fatty acid tails, and their hydrophilic regions are inside the protein or exposed to the cytosol.
- **Fluid mosaic model:** a framework of phospholipids embedded with proteins, steroids such as cholesterol in vertebrates, glycoproteins and glycolipids. All of these can move around within the membrane.
- Temperature affects fluidity: at a lower temperature, components of the membrane move more slowly.

### Watch out for
Drawing the bilayer with the tails facing the water, or treating the membrane as a fixed, rigid layer. The heads face the water, and the parts move.

### Worked example
Prompt: "Explain why phospholipids in water form a bilayer."

The fatty acid tails are hydrophobic, so they cluster together away from the water, while the polar phosphate heads are hydrophilic and face the water on both sides. This arrangement shields the tails from water and produces a bilayer with a hydrophobic interior.
"""),
("membrane-permeability", r"""
### The idea
The plasma membrane separates the inside of the cell from the outside and lets only some substances cross, which makes it selectively permeable. The reason is its hydrophobic interior, formed by the nonpolar tails of the phospholipids. Small nonpolar molecules slip through, but ions and large polar molecules need help from proteins.

### Key facts
- **Cross freely:** small nonpolar molecules such as N₂, O₂ and CO₂.
- **Cross in small amounts:** small polar molecules with no charge, such as H₂O and NH₃.
- **Need channel or transport proteins:** ions and large polar molecules such as glucose.
- The nonpolar hydrocarbon tails of the phospholipids prevent ions and polar molecules from moving across.
- **Cell walls** of bacteria, archaea, fungi and plants give a structural boundary and a permeability barrier for some substances, and they protect the cell from osmotic lysis.

### Watch out for
Explaining selective permeability by size alone. Charge and polarity matter as much as size. Also, a cell wall is not the same as a plasma membrane: the wall gives structure and the membrane controls what crosses.

### Worked example
Prompt: "Why can oxygen cross the plasma membrane easily but sodium ions cannot?"

Oxygen is a small nonpolar molecule, so it can pass through the hydrophobic interior of the bilayer. Sodium ions are charged, so the nonpolar fatty acid tails block them, and they can cross only through channel or transport proteins.
"""),
("membrane-transport", r"""
### The idea
Because the membrane is selectively permeable, a cell can have different concentrations of a substance inside and outside, which is a concentration gradient. Substances move across the membrane in different ways, depending on whether they move down or against the gradient, and on whether the cell must spend energy.

### Key facts
- **Passive transport** is the net movement of molecules from a region of high concentration to a region of low concentration without a direct input of metabolic energy.
- **Active transport** needs a direct input of energy, and it can move molecules from a region of low concentration to a region of high concentration.
- **Endocytosis** takes in large molecules or particles when the plasma membrane folds in on itself and forms vesicles around the material.
- **Exocytosis** releases material when vesicles fuse with the plasma membrane and secrete their contents.
- Endocytosis and exocytosis need energy.

### Watch out for
Deciding between active and passive transport from the size of the molecule. Look at the direction compared with the gradient and whether energy is needed. Net movement against a gradient means active transport.

### Worked example
Prompt: "Substance R has a concentration of 3 mM outside a cell and 30 mM inside, and it moves into the cell. Is this passive or active transport?"

The substance moves from a lower concentration (3 mM) to a higher concentration (30 mM), which is against its gradient. This needs a direct input of energy, so it is active transport.
"""),
("facilitated-diffusion", r"""
### The idea
Facilitated diffusion lets substances that cannot cross the hydrophobic interior of the membrane move down their concentration gradient with the help of proteins. It is passive, so it needs no energy. Charged ions such as sodium and potassium use channel proteins, and large polar molecules use transport proteins.

### Key facts
- Facilitated diffusion needs **transport or channel proteins**, and the movement is down the concentration gradient with no energy input.
- Charged ions, including Na⁺ and K⁺, need channel proteins to cross the membrane.
- The movement of ions across a membrane can make the membrane polarized, with a difference in electrical charge between the two sides.
- **Aquaporins** transport large quantities of water across membranes.
- The rate of facilitated diffusion levels off at high concentration because the number of proteins is limited (they become saturated), whereas simple diffusion keeps increasing.

### Watch out for
Calling any protein-assisted movement active transport. If the substance moves down its gradient and no ATP is needed, it is facilitated diffusion, even though a protein is involved.

### Worked example
Prompt: "The rate of uptake of molecule Y rises to 32 µmol/min at 20 mM and only to 36 µmol/min at 40 mM. What does this suggest?"

Doubling the concentration barely increases the rate, so the rate has reached a maximum. This suggests that a limited number of transport proteins are saturated, so molecule Y probably crosses by facilitated diffusion.
"""),
("tonicity-and-osmoregulation", r"""
### The idea
Water moves across a membrane by osmosis, from a region of higher water potential to a region of lower water potential. Compared with a cell, a solution can be hypotonic, hypertonic or isotonic, and the cell gains or loses water accordingly. Organisms use osmoregulation to control their water balance and their internal solute composition.

### Key facts
- **Hypertonic** solution: more solute than the cell, so water leaves the cell. **Hypotonic:** less solute, so water enters. **Isotonic:** equal, so there is no net movement.
- Water moves from low solute concentration to high solute concentration, which is from hypotonic to hypertonic.
- Water potential: Ψ = Ψₚ + Ψₛ, pressure potential plus solute potential. In an open container the pressure potential is zero.
- Solute potential: Ψₛ = -iCRT, where i is the ionization constant (1.0 for sucrose), C is the molar concentration, R = 0.0831 L bar per mol K, and T is the temperature in kelvin (°C + 273).
- A plant cell in a hypotonic solution becomes turgid. In a hypertonic solution it loses water, and the membrane pulls away from the wall. An animal cell in a hypotonic solution may burst.

### Watch out for
Using degrees Celsius in the equation, and forgetting that solute potential is negative. Also compare water potentials with their signs: -2.0 bars is higher than -5.0 bars.

### Worked example
Prompt: "What is the solute potential of a 0.20 M sucrose solution at 27 °C?"

T = 27 + 273 = 300 K, so Ψₛ = -(1.0)(0.20)(0.0831)(300) = -4.99 bars. If a plant cell with a pressure potential of +2.0 bars and a solute potential of -6.5 bars (total -4.5 bars) were placed in this solution in an open beaker, the solution (-4.99 bars) would have the lower water potential, so water would leave the cell.
"""),
("mechanisms-of-transport", r"""
### The idea
Cells use energy to move ions and molecules across membranes against their concentration gradients. This active transport builds and maintains electrochemical gradients, which are differences in concentration and in electrical charge across the membrane. Membrane proteins carry out the work, and ATP usually supplies the energy.

### Key facts
- Active transport needs **metabolic energy**, such as ATP, and **membrane proteins**.
- The **sodium-potassium pump (Na⁺/K⁺ ATPase)** uses ATP to move Na⁺ and K⁺ across the membrane against their gradients, and it helps maintain the membrane potential.
- Gradients are maintained by constant work, because ions leak back across the membrane through channels, down their gradients.
- If ATP production stops, the pumps stop and the gradients gradually disappear.
- Evidence for active transport: a substance accumulates against its gradient, and the accumulation stops when ATP production is blocked.

### Watch out for
Thinking that a gradient, once built, stays in place on its own. It decays unless energy keeps being used. Also, the pump uses ATP and does not make it.

### Worked example
Prompt: "Cells take up a molecule from a 0.10 mM solution and reach 5.2 mM inside. With a chemical that stops ATP production the inside concentration is only 0.1 mM. What does this show?"

The cells moved the molecule from 0.10 mM outside to 5.2 mM inside, which is against the gradient, and this stopped when ATP was not available. This shows that the molecule is taken up by active transport.
"""),
("cell-compartmentalization", r"""
### The idea
Membranes divide a eukaryotic cell into compartments. Each membrane-bound organelle provides its own environment for particular reactions, so the many reactions of the cell can take place at the same time without getting in each other's way.

### Key facts
- Membranes and membrane-bound organelles **compartmentalize** metabolic processes and specific enzymatic reactions in eukaryotic cells.
- Internal membranes **minimize competing interactions**: for example, lysosomes keep their hydrolytic enzymes away from the rest of the cell.
- Internal membranes **increase the surface area** where reactions can occur, as in the folded inner membrane of a mitochondrion.
- Membrane-bound structures include the nucleus, mitochondria, chloroplasts, the endoplasmic reticulum, the Golgi complex, lysosomes and vacuoles. Ribosomes are not membrane-bound.

### Watch out for
Treating compartments as sealed off from one another. Materials move between compartments in vesicles and through membrane proteins.

### Worked example
Prompt: "Explain one advantage of keeping a cell's digestive enzymes inside lysosomes."

The membrane of the lysosome separates the hydrolytic enzymes from the rest of the cell. This minimizes competing interactions, because the enzymes cannot digest the cell's own proteins and other components in the cytoplasm, and they act only on material that is brought to the lysosome.
"""),
("origins-of-cell-compartmentalization", r"""
### The idea
Eukaryotic cells have a complex system of internal membranes, but prokaryotic cells typically do not. Evidence suggests that two of the organelles, mitochondria and chloroplasts, began as free-living prokaryotes that were taken in by a larger cell. This is the theory of endosymbiosis.

### Key facts
- **Endosymbiosis:** mitochondria and chloroplasts evolved from once free-living prokaryotic cells that came to live inside another cell.
- Features that support this claim: mitochondria and chloroplasts have their own circular DNA, ribosomes like those of bacteria, a double membrane, and they divide in a way that is similar to binary fission.
- **Prokaryotes** typically lack internal membrane-bound organelles but have internal regions with specialized structures and functions.
- **Eukaryotic cells** maintain internal membranes that partition the cell into specialized regions.

### Watch out for
Saying that prokaryotes have no structure inside. They have specialized regions, but these are not usually bounded by membranes. Also, a claim needs evidence: say which features match.

### Worked example
Prompt: "Support the claim that mitochondria evolved from free-living bacteria."

Mitochondria have their own circular DNA and ribosomes that are similar to those of bacteria, and they are surrounded by a double membrane. They also divide by a process that resembles the binary fission of bacteria. These features are shared with bacteria and not with the eukaryotic nucleus, which supports an origin from bacteria.
"""),
]

refreshers_lib.write("ap-biology", 2, ENTRIES)
