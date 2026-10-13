"""Unit 1, topic 1.7 Proteins (8 questions).

Required content (CED 2025-26): 1.7.A.1 linear chains of amino acids joined by covalent peptide bonds (carboxyl group of one, amine group of the next);
1.7.A.2 an amino acid has a central carbon with H, carboxyl, amine and a variable R group, and R groups are hydrophobic/nonpolar, hydrophilic/polar or ionic,
their interactions determine structure and function; 1.7.A.3 the sequence is the primary structure and determines overall shape; 1.7.A.4 secondary structure
(alpha helices, beta-pleated sheets) from hydrogen bonding of the backbone; 1.7.A.5 tertiary structure from hydrogen bonds, hydrophobic and ionic interactions or
disulfide bridges; 1.7.A.6 quaternary structure from interactions between multiple polypeptides, and all four levels determine function. Excluded: the molecular
structure of amino acids. Suggested skill 6.E: predict the effects of a change.
"""
from lib import *


def build(B):
    B.mcq(7, "How are the amino acids in a polypeptide joined to one another?",
          ch("By covalent peptide bonds between the carboxyl group of one amino acid and the amine group of the next.", "Peptide bonds are covalent bonds, and they form a growing chain of amino acids."),
          [ch("By hydrogen bonds, each formed between the R group of one amino acid and the R group of the next.", "Hydrogen bonds between R groups contribute to the folding of the protein. They do not join the amino acids in the chain."),
           ch("By ionic bonds, each formed between the positively charged and negatively charged ends of two amino acids.", "The amino acids in the chain are joined by covalent bonds, not ionic bonds."),
           ch("By glycosidic bonds, each formed between the hydroxyl groups of the amino acid and the next amino acid.", "Glycosidic bonds join monosaccharides in carbohydrates and do not join amino acids.")],
          "Amino acids are joined by covalent peptide bonds.", difficulty="easy")

    B.mcq(7, "What determines the primary structure of a protein?",
          ch("The specific sequence of amino acids in the polypeptide chain", "The primary structure is the order of amino acids, and it determines the overall shape of the protein."),
          [ch("The folding of the polypeptide backbone into alpha helices and beta-pleated sheets", "This describes the secondary structure."),
           ch("The three-dimensional shape that results from interactions between the R groups of amino acids", "This describes the tertiary structure."),
           ch("The association of two or more separate polypeptide chains into a single functional protein", "This describes the quaternary structure.")],
          "Primary structure is the amino acid sequence.", difficulty="easy")

    n = 120
    assert n - 1 == 119
    B.mcq(7, f"A polypeptide is made of {n} amino acids in a single linear chain. How many peptide bonds does it contain?",
          ch("119", "A chain of 120 amino acids has 119 bonds between them, one for each pair of neighboring amino acids.", 119),
          [ch("120", "This assumes one peptide bond for each amino acid. A chain has one fewer bond than the number of amino acids.", 120),
           ch("118", "This subtracts two from the number of amino acids. A linear chain of n amino acids has n - 1 bonds.", 118),
           ch("240", "This assumes two peptide bonds for each amino acid. Each amino acid is joined to its neighbors, so each bond is shared by two.", 240)],
          "A linear chain of n amino acids has n - 1 peptide bonds.", difficulty="medium")

    B.mcq(7, "Alpha helices and beta-pleated sheets are examples of the secondary structure of a protein. What forms these shapes?",
          ch("Hydrogen bonding between atoms of the polypeptide backbone, in local regions of the chain", "Secondary structure comes from hydrogen bonds between backbone atoms."),
          [ch("Disulfide bridges between the R groups of amino acids that are far apart in the chain", "Disulfide bridges contribute to the tertiary structure."),
           ch("Ionic interactions between R groups of two different polypeptide chains in the protein", "Interactions between different chains belong to the quaternary structure."),
           ch("Covalent bonds between the carboxyl group of one amino acid and the amine group of the next", "These are the peptide bonds that make the primary structure.")],
          "Secondary structure is formed by hydrogen bonding in the polypeptide backbone.", difficulty="medium")

    B.mcq(7, "Which interactions between the R groups of amino acids determine the three-dimensional shape of the tertiary structure of a protein?",
          ch("Hydrogen bonds, hydrophobic interactions, ionic interactions and disulfide bridges", "These interactions between R groups fold the polypeptide into its tertiary structure."),
          [ch("Only the peptide bonds that join each amino acid to the next one in the polypeptide chain", "Peptide bonds join the amino acids and make the primary structure. They do not fold the chain."),
           ch("Only the hydrogen bonds between the atoms of the polypeptide backbone in the helices and sheets", "This describes the secondary structure and leaves out the interactions between R groups."),
           ch("Only the interactions between separate polypeptide chains that make up a multi-chain protein", "This describes the quaternary structure, which exists only in proteins that have more than one polypeptide.")],
          "R-group interactions fold a polypeptide into its tertiary structure.", difficulty="medium")

    prot_rows = [("Hemoglobin", "4"), ("Myoglobin", "1"), ("Collagen", "3"), ("Lysozyme", "1")]
    B.mcq(7, "The table shows the number of polypeptide chains in four proteins. Which proteins have a quaternary structure?",
          ch("Hemoglobin and collagen, because each is made of more than one polypeptide chain.", "Quaternary structure arises from interactions between multiple polypeptides."),
          [ch("Myoglobin and lysozyme, because each is made of a single chain with a tertiary structure.", "A single polypeptide has no quaternary structure, because there are no other chains to interact with."),
           ch("Hemoglobin only, because it is the protein with the highest number of polypeptide chains.", "Collagen also has more than one chain. A quaternary structure does not require four chains."),
           ch("All four of the proteins, because each has a primary, secondary and tertiary structure.", "All proteins have the first three levels. Quaternary structure exists only if more than one polypeptide is present.")],
          "Quaternary structure requires more than one polypeptide.",
          diagram=table(["Protein", "Number of polypeptide chains"], prot_rows, caption="Four proteins", row_headers=True), difficulty="medium")

    B.mcq(7, "In a water-soluble protein, a polar amino acid on the outer surface of the protein is replaced by a nonpolar amino acid because of a mutation. Which outcome is most likely?",
          ch("The new nonpolar R group may interact differently with water, which could change the folding or make the proteins clump together.", "R groups can be hydrophobic or hydrophilic, and their interactions determine structure and function. A hydrophobic group on a surface in water may cause aggregation."),
          [ch("The protein would be unchanged, because a change in a single amino acid cannot affect the shape of a protein at all.", "The sequence determines the shape. A single change can alter folding and function."),
           ch("The peptide bonds of the protein would break, because nonpolar R groups cannot be joined by peptide bonds to the other amino acids in the chain.", "A peptide bond joins the backbone of amino acids and does not depend on whether the R group is polar or nonpolar."),
           ch("The protein would become more soluble in water, because the nonpolar R group forms more hydrogen bonds with water.", "Nonpolar R groups do not form hydrogen bonds with water, so the change would not increase solubility.")],
          "The properties of R groups determine how a protein folds and functions.", difficulty="hard")

    B.mcq(7, "A chemical disrupts hydrogen bonds and ionic interactions in a protein but does not break any covalent bonds. Which level of protein structure would remain intact?",
          ch("The primary structure, because the peptide bonds that join the amino acids are covalent bonds.", "The sequence of amino acids is held together by covalent peptide bonds, which this chemical does not break."),
          [ch("The secondary structure, because the helices and sheets depend mainly on covalent bonds in the backbone.", "Secondary structure depends on hydrogen bonds, which the chemical disrupts."),
           ch("The tertiary structure, because the folding depends on ionic interactions that are covalent bonds.", "Ionic interactions are not covalent bonds, and the chemical disrupts them."),
           ch("The quaternary structure, because the chains of a multi-chain protein are always held by covalent bonds.", "Chains are usually held by weaker interactions such as hydrogen bonds and ionic interactions.")],
          "Only the primary structure depends on covalent peptide bonds alone.", difficulty="hard")
