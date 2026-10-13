"""Writes content/ap-biology/refreshers/unit-1.json (seven refreshers, one per topic). Layout: ### The idea, ### Key facts, ### Watch out for, ### Worked example.
Facts are the CED's required content for each topic; every number in a worked example is asserted. Avoid a lone dollar sign, single-asterisk italics and
em dashes. Edit this script, not the JSON. Run: python3 u1_refreshers.py"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import refreshers_lib

# worked-example numbers
assert (36.0 - 20.0) / (28.0 - 20.0) == 2.0
assert 100 - 1 == 99 and 180 + 180 - 342 == 18
assert 249 + 1 == 250
assert 120 - 1 == 119
_c = {"A": "T", "T": "A", "G": "C", "C": "G"}
assert "".join(_c[b] for b in "ATGCCATG")[::-1] == "CATGGCAT"

ENTRIES = [
("structure-of-water-and-hydrogen-bonding", r"""
### The idea
A water molecule is polar. Oxygen pulls the shared electrons in the two O-H bonds closer to itself, so the oxygen end is slightly negative and the hydrogen ends are slightly positive. The slightly positive hydrogen of one water molecule is attracted to the slightly negative oxygen of another. This attraction is a hydrogen bond, and it is weak on its own, but many hydrogen bonds together give water the properties that living things depend on.

### Key facts
- **Cohesion** is the attraction between water molecules. It produces surface tension, which lets a water strider stand on a pond.
- **Adhesion** is the attraction between water and other polar surfaces. Cohesion and adhesion together pull water up narrow tubes, such as those in plants.
- **High specific heat capacity.** Water absorbs a large amount of energy for each degree its temperature rises, partly because the energy breaks hydrogen bonds. This keeps lakes, oceans and the bodies of organisms at stable temperatures.
- **High heat of vaporization.** A large amount of energy is needed to turn liquid water into gas, so evaporating water, such as sweat, cools a surface.
- Hydrogen bonds also form between and within other biological molecules, such as the strands of DNA.

### Watch out for
Mixing up the bonds. The O-H bonds inside a water molecule are covalent. A hydrogen bond is the weaker attraction between two molecules. Also, cohesion is water to water and adhesion is water to something else.

### Worked example
Prompt: "Equal masses of water and oil receive the same heat. The water warms from 20.0 to 28.0 degrees Celsius and the oil from 20.0 to 36.0. What does this show?"

The oil's temperature rose 16.0 degrees and the water's rose 8.0 degrees for the same energy, a ratio of 2. So water has a higher specific heat capacity (about twice that of the oil in this experiment), because it takes more energy to raise its temperature by one degree.
"""),
("elements-of-life", r"""
### The idea
Living things build their molecules from atoms they take in from the environment. Carbon, hydrogen and oxygen are the most prevalent elements in the four main classes of biological molecules: carbohydrates, lipids, proteins and nucleic acids. A few other elements are used in particular molecules, and which elements a molecule contains tells you what kind of molecule it is.

### Key facts
- **Carbon, hydrogen and oxygen** make up most of carbohydrates, lipids, proteins and nucleic acids. A carbohydrate such as starch contains only these three.
- **Sulfur** is used in building proteins. It is found in the side chains of some amino acids.
- **Phosphorus** is used in building nucleic acids (in the phosphate groups of the backbone) and phospholipids, the lipids of membranes.
- **Nitrogen** is used in building nucleic acids (in the bases) and in proteins.
- Radioactive isotopes of phosphorus and sulfur can be used as labels to find out which macromolecules a cell builds.

### Watch out for
Assuming that every element appears in every macromolecule. If a sample has no nitrogen, it is not a protein or a nucleic acid. Also note the confusing pair, phosphorus and sulfur: P for nucleic acids and phospholipids, S for proteins.

### Worked example
Prompt: "Bacteria are grown with radioactive phosphorus. In which macromolecules will the label appear?"

Phosphorus is used in the phosphate groups of nucleic acids and in phospholipids, so the label will appear in the DNA and RNA and in the membranes. It will not appear in proteins, which use sulfur, or in carbohydrates, which contain only carbon, hydrogen and oxygen.
"""),
("introduction-to-macromolecules", r"""
### The idea
Cells build large molecules, the polymers, by joining many small molecules, the monomers, and they break polymers down again when they need the monomers. Two reactions do this. Dehydration synthesis builds polymers, and hydrolysis breaks them down. Water is the key to both: it is lost when a bond forms and it is used when a bond breaks.

### Key facts
- **Dehydration synthesis** joins two monomers by a covalent bond. A hydrogen from one monomer and a hydroxyl group from the other are removed, which is the loss of the equivalent of a water molecule. Joining many monomers is polymerization.
- **Hydrolysis** breaks a covalent bond between monomers by adding a water molecule. The hydrogen goes to one monomer and the hydroxyl group to the other.
- A linear polymer of n monomers has n - 1 bonds, so building it releases n - 1 water molecules and breaking it down completely uses n - 1.
- Digestion of food is hydrolysis: enzymes use water to break polymers into monomers.

### Watch out for
Reversing the two reactions. A helpful check: dehydration means "removing water", so it builds polymers. Also, count the bonds, not the monomers: 100 monomers make 99 bonds.

### Worked example
Prompt: "Sucrose (342 g) is completely hydrolyzed to 180 g of glucose and 180 g of fructose. What mass of water is used? How many water molecules are released when a polymer of 100 monomers is built?"

Mass is conserved, so the water used is (180 + 180) - 342 = 18 g. A polymer of 100 monomers has 99 bonds, and each is made by the loss of one water molecule, so 99 water molecules are released.
"""),
("carbohydrates", r"""
### The idea
Carbohydrates are made of sugar monomers, called monosaccharides. When many monosaccharides are joined by covalent bonds, the product is a polysaccharide, or complex carbohydrate. Polysaccharides can be linear or branched, and different ones do different jobs, such as storing energy or giving structural support.

### Key facts
- **Monosaccharides** (simple sugars) are the monomers. They are joined by covalent bonds made by dehydration synthesis.
- **Starch** stores energy in plants.
- **Glycogen** stores energy in animals.
- **Cellulose** is a structural polysaccharide that makes up the cell walls of plants.
- Polysaccharides may be linear or branched. The detailed molecular structure of specific carbohydrates is not tested.
- Carbohydrates contain only carbon, hydrogen and oxygen.

### Watch out for
Mixing up the plant and animal storage molecules (starch in plants, glycogen in animals) and forgetting that cellulose is a structural molecule, not an energy store. Also remember that all three are polymers of sugars, not of amino acids.

### Worked example
Prompt: "A linear polysaccharide is built from glucose by dehydration synthesis, and 249 water molecules are released. How many glucose monomers does it contain?"

A linear chain of n monomers has n - 1 bonds, and each bond forms by the loss of one water molecule. So the chain has 249 + 1 = 250 monomers.
"""),
("lipids", r"""
### The idea
Lipids are typically nonpolar and hydrophobic, so they do not dissolve in water. Their structure and function come from how their subcomponents are assembled. Fats store energy, steroids act as hormones, cholesterol stabilizes animal cell membranes, and phospholipids form the bilayers of cell membranes.

### Key facts
- **Saturated fatty acids** have only single bonds between carbon atoms, so the tail is straight.
- **Unsaturated fatty acids** have at least one double bond between carbons, which kinks the tail. The more double bonds, the more unsaturated the lipid.
- Straight tails pack closely together and kinked tails do not, so the more unsaturated a lipid is, the more liquid it is at room temperature.
- **Fats** provide energy storage and, in some mammals, insulation.
- **Steroids** include hormones that support growth and development, energy metabolism and homeostasis.
- **Cholesterol** gives structural stability to animal cell membranes.
- **Phospholipids** group together to form the lipid bilayer of plasma membranes and other cell membranes.

### Watch out for
Mixing up which kind of fatty acid is liquid. Think about the shape: kinks mean loose packing, so unsaturated fats such as oils are liquid. The molecular structure of specific lipids is not tested.

### Worked example
Prompt: "Explain why olive oil is liquid at room temperature but butter is solid."

Olive oil has more unsaturated fatty acids. Each double bond kinks the tail, so the molecules cannot pack closely together and the oil stays liquid. Butter has more saturated fatty acids, whose straight tails pack tightly and form a solid.
"""),
("nucleic-acids", r"""
### The idea
Nucleic acids, DNA and RNA, store and transmit biological information. They are polymers of nucleotides, and the information is encoded in the order of the nucleotides. Each nucleotide has a five-carbon sugar, a phosphate group and a nitrogenous base.

### Key facts
- **Bases:** adenine (A), thymine (T), guanine (G), cytosine (C) and uracil (U).
- **DNA** has the sugar deoxyribose and the bases A, T, G and C. It is typically double stranded. **RNA** has the sugar ribose and the bases A, U, G and C, and is typically single stranded.
- A strand has a 5' end (a phosphate) and a 3' end (a hydroxyl group). New nucleotides are added to the 3' end, forming covalent bonds.
- DNA is an antiparallel double helix: the two strands run in opposite directions. The strands are held together by hydrogen bonds between complementary bases: A with T, and C with G. In RNA, A pairs with U.
- The molecular structure of specific nucleotides is not tested.

### Watch out for
Writing a complementary strand in the wrong direction. Because the strands are antiparallel, the complement of a strand written 5' to 3' is written 3' to 5' unless you reverse it.

### Worked example
Prompt: "One strand of DNA is 5'-ATGCCATG-3'. What is the complementary strand, written 5' to 3'?"

Pair each base (A with T, C with G) to get 3'-TACGGTAC-5'. To write it from the 5' end, reverse it: 5'-CATGGCAT-3'.
"""),
("proteins", r"""
### The idea
Proteins are linear chains of amino acids. Their shape determines their function, and the shape depends on the sequence of the amino acids and on interactions between their R groups. Each amino acid has a central carbon with a hydrogen atom, a carboxyl group, an amine group and a variable R group.

### Key facts
- **Peptide bonds** are covalent bonds between the carboxyl group of one amino acid and the amine group of the next.
- R groups can be hydrophobic (nonpolar), hydrophilic (polar) or ionic, and their interactions determine the structure of that region.
- **Primary structure** is the sequence of amino acids.
- **Secondary structure** is local folding, such as alpha helices and beta-pleated sheets, due to hydrogen bonds between atoms of the backbone.
- **Tertiary structure** is the three-dimensional shape that results from hydrogen bonds, hydrophobic interactions, ionic interactions or disulfide bridges between R groups.
- **Quaternary structure** arises from interactions between multiple polypeptides. All four levels determine function.
- The molecular structure of amino acids is not tested.

### Watch out for
Using "protein" and "proton" as if they were the same, which costs points on the exam, and attributing quaternary structure to a protein with a single chain. A change of one amino acid can change the shape.

### Worked example
Prompt: "How many peptide bonds are in a polypeptide of 120 amino acids?"

A linear chain of 120 amino acids has one bond between each neighboring pair, so it has 120 - 1 = 119 peptide bonds.
"""),
]

refreshers_lib.write("ap-biology", 1, ENTRIES)
