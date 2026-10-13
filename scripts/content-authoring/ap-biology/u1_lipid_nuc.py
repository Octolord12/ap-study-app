"""Unit 1, topics 1.5 Lipids (8 questions) and 1.6 Nucleic Acids (8).

Required content (CED 2025-26): 1.5.A.1 lipids are typically nonpolar and hydrophobic; saturated fatty acids have only single C-C bonds, unsaturated ones at least one
double bond that kinks the chain; the more unsaturated, the more liquid at room temperature; 1.5.A.2 fats (energy storage, insulation), steroids (hormones), cholesterol
(structural stability of animal cell membranes), phospholipids (the bilayer of plasma and cell membranes); 1.6.A.1-4 nucleotides (five-carbon sugar, phosphate, base;
A, T, G, C, U), 3' hydroxyl and 5' phosphate ends and addition to the 3' end, DNA an antiparallel double helix with A-T and C-G hydrogen bonds (A-U in RNA), DNA has
deoxyribose and thymine and is typically double stranded, RNA has ribose and uracil and is typically single stranded. Excluded: the molecular structure of specific
lipids and nucleotides. Suggested skills 6.E (predict effects of a change) and 2.A (describe visual representations).
"""
from lib import *

COMP = {"A": "T", "T": "A", "G": "C", "C": "G"}


def complement(seq):
    """The complementary strand, written 3' to 5' under the 5' to 3' input."""
    return "".join(COMP[b] for b in seq)


def build(B):
    # ------------------------------------------------------------------ 1.5 Lipids
    B.mcq(5, "Which statement describes a general property of lipids?",
          ch("They are typically nonpolar and hydrophobic, so they do not dissolve readily in water or mix with it.", "Lipids are nonpolar, which is why they do not mix well with water."),
          [ch("They are typically polar and hydrophilic, so they dissolve readily in water and form hydrogen bonds with it.", "Lipids are nonpolar and hydrophobic. It is polar molecules that dissolve in water."),
           ch("They are polymers of amino acids that fold into specific shapes, which determines their function.", "Amino acids are the monomers of proteins, not lipids."),
           ch("They are ionic compounds that break apart into charged particles when they are mixed with water.", "Lipids are nonpolar molecules and are not ionic compounds.")],
          "Lipids are typically nonpolar and hydrophobic.", difficulty="easy")

    B.mcq(5, "Which statement correctly describes an unsaturated fatty acid?",
          ch("It has at least one double bond between carbon atoms in its tail, which causes the carbon chain to kink.", "Double bonds between carbons in the hydrocarbon tail put a bend in the chain."),
          [ch("It has only single bonds between the carbon atoms in its tail, which keeps the carbon chain straight.", "This describes a saturated fatty acid, which is saturated with hydrogen atoms."),
           ch("It has a phosphate group in its tail, which makes the fatty acid polar and gives it a kink.", "A phosphate group is part of a phospholipid. Unsaturated fatty acids are described by double bonds in the tail."),
           ch("It has a carbon atom that is joined to more hydrogen atoms than in any other fatty acid in the tail.", "Unsaturated fatty acids have fewer hydrogen atoms because of the double bonds in the tail.")],
          "Unsaturated fatty acids contain at least one carbon-carbon double bond, which kinks the chain.", difficulty="medium")

    B.mcq(5, "Olive oil is liquid at room temperature, but butter is solid at the same temperature. Which statement best explains the difference?",
          ch("Olive oil has more unsaturated fatty acids, whose kinked tails prevent the molecules from packing closely together.", "The more unsaturated a lipid is, the more liquid it is at room temperature, because kinks in the tails keep the molecules apart."),
          [ch("Olive oil has more saturated fatty acids, whose straight tails keep the molecules too far apart to form a solid at all.", "Straight tails of saturated fatty acids pack closely together, which makes a lipid more solid."),
           ch("Butter contains more water than olive oil, and the water holds the lipid molecules together as a solid.", "Water is not the reason that butter is solid. Both are made mostly of lipids."),
           ch("Olive oil is made of proteins, which are always liquids at room temperature, and butter is made of fats.", "Olive oil is a lipid and not a protein, and proteins are not liquids because of their type.")],
          "More double bonds means more kinks, less tight packing and a more liquid lipid at room temperature.", difficulty="medium")

    fat_rows = [("Fat P", "0.3", "Solid"), ("Fat Q", "1.1", "Liquid"), ("Fat R", "1.9", "Liquid"), ("Fat S", "0.1", "Solid")]
    B.mcq(5, "A student measures the average number of carbon-carbon double bonds per fatty acid in four fats and records whether each fat is solid or liquid at 20 °C. Which conclusion is best supported by the data?",
          ch("Fats with more double bonds per fatty acid are more likely to be liquid at 20 °C than fats with fewer double bonds.", "The two fats with fewer than half a double bond per fatty acid are solid, and the two with more than one are liquid."),
          [ch("Fats with fewer double bonds per fatty acid are more likely to be liquid at 20 °C than fats with more double bonds.", "This reverses the pattern in the data. Fats with fewer double bonds are the solids."),
           ch("Whether a fat is solid or liquid at 20 °C does not depend on its fatty acids, because all four are fats.", "The four fats differ in their state and in their number of double bonds, which suggests that the two are related."),
           ch("Double bonds make the tails of fatty acids straighter, which explains why these fats are liquid at 20 °C.", "Double bonds put kinks in the tails. Kinked tails pack less closely, which explains the liquid fats.")],
          "The data show that fats with more double bonds per fatty acid tend to be liquid at room temperature.",
          diagram=table(["Fat", "Average number of C=C double bonds per fatty acid", "State at 20 °C"], fat_rows, caption="Four fats", row_headers=True), difficulty="hard")

    B.mcq(5, "Which type of lipid groups together to form the lipid bilayers of plasma membranes and other cell membranes?",
          ch("Phospholipids, which group together to form a bilayer in the plasma membrane", "Phospholipids form the lipid bilayer found in plasma and cell membranes."),
          [ch("Steroids, which are hormones that support growth and development in the body", "Steroids are lipids that act as hormones. They do not form the bilayer."),
           ch("Fats, which store energy and can provide insulation in some mammals", "Fats store energy and insulate. The bilayer is formed by phospholipids."),
           ch("Cholesterol, which forms the entire bilayer of the plasma membrane by itself", "Cholesterol is found in animal cell membranes and stabilizes them, but phospholipids form the bilayer.")],
          "Phospholipids form the lipid bilayer of cell membranes.", difficulty="easy")

    B.mcq(5, "Which statement about steroids is correct?",
          ch("Steroids include hormones that support physiological functions such as growth and development, energy metabolism and homeostasis.", "Steroid hormones act as chemical signals that support many functions of the body."),
          [ch("Steroids are the main energy storage lipids, which are stored in cells and used for insulation in mammals.", "This describes fats. Steroids are mainly known as hormones."),
           ch("Steroids are polymers of nucleotides, which store the genetic information that is passed on from parent to offspring.", "Nucleotides are the monomers of nucleic acids, which store genetic information."),
           ch("Steroids are the lipids that form the lipid bilayer, with a hydrophilic head and two hydrophobic tails.", "This describes phospholipids, not steroids.")],
          "Steroids are lipids that function as hormones.", difficulty="medium")

    B.mcq(5, "Which statement describes a function of cholesterol in animal cells?",
          ch("It provides structural stability to the plasma membrane of the cell.", "Cholesterol is found in animal cell membranes, where it provides structural stability."),
          [ch("It stores energy for the cell in the form of a long polymer of sugar molecules.", "Cholesterol is a lipid, not a polysaccharide, and it is not mainly an energy store."),
           ch("It carries amino acids to the ribosome so that they can be joined into a protein.", "Transfer of amino acids is not a function of cholesterol."),
           ch("It stores the genetic information of the cell in the order of its subcomponents.", "Genetic information is stored in nucleic acids, not in cholesterol.")],
          "Cholesterol provides structural stability to animal cell membranes.", difficulty="medium")

    B.mcq(5, "A manufacturer converts a liquid vegetable oil into a solid margarine by adding hydrogen atoms to the double bonds in its fatty acid tails. Which explanation best accounts for the margarine being solid?",
          ch("The tails become saturated and straight, so the lipid molecules pack closely together and the lipid is solid at room temperature.", "Removing the double bonds removes the kinks. Straight tails pack closely, which makes the lipid more solid."),
          [ch("The tails become more kinked, so the lipid molecules pack more closely together and the lipid is solid at room temperature.", "Adding hydrogen to the double bonds removes the kinks. It does not add more."),
           ch("The tails become polar and hydrophilic, so the lipid molecules form hydrogen bonds with one another and with the water.", "The tails remain nonpolar hydrocarbon chains after the hydrogen is added."),
           ch("The tails gain double bonds, so the fatty acids become more unsaturated and the lipid molecules form a solid at room temperature.", "Adding hydrogen to double bonds reduces the number of double bonds, so the fatty acids become more saturated.")],
          "More saturated tails are straighter, pack more closely and make a lipid more solid.", difficulty="hard")

    # ------------------------------------------------------------------ 1.6 Nucleic acids
    B.mcq(6, "Which choice lists the three structural components of a nucleotide?",
          ch("A five-carbon sugar, a phosphate group and a nitrogenous base", "Each nucleotide of DNA or RNA has these three components."),
          [ch("An amino group, a carboxyl group and a variable R group on a central carbon", "These are the parts of an amino acid, the monomer of proteins."),
           ch("A fatty acid tail, a glycerol molecule and a phosphate group in a membrane", "These are parts of lipids such as phospholipids, not of nucleotides."),
           ch("A monosaccharide, a hydroxyl group and a peptide bond between two molecules", "A nucleotide does not contain a peptide bond. Peptide bonds join amino acids.")],
          "A nucleotide has a five-carbon sugar, a phosphate and a nitrogenous base.", difficulty="easy")

    B.mcq(6, "Which choice correctly identifies two structural differences between DNA and RNA?",
          ch("DNA contains the sugar deoxyribose and the base thymine, whereas RNA contains the sugar ribose and the base uracil.", "These are the structural differences in the sugar and in one of the bases."),
          [ch("DNA contains the sugar ribose and the base uracil, whereas RNA contains the sugar deoxyribose and the base thymine.", "This reverses the sugars and bases of the two molecules."),
           ch("DNA contains the base uracil and is typically single stranded, whereas RNA contains thymine and is typically double stranded.", "DNA contains thymine and is typically double stranded. RNA contains uracil and is typically single stranded."),
           ch("DNA and RNA contain the same sugar and bases, but DNA is found only in the nucleus and RNA only in the cytoplasm.", "The sugar and one base differ. The locations are not what distinguishes the structures.")],
          "DNA has deoxyribose and thymine; RNA has ribose and uracil.", difficulty="easy")

    strand = "ATGCCATG"
    comp_35 = complement(strand)
    comp_53 = comp_35[::-1]
    assert (comp_35, comp_53) == ("TACGGTAC", "CATGGCAT")
    B.mcq(6, f"One strand of a DNA molecule has the sequence 5'-{strand}-3'. What is the sequence of the complementary strand, written in the 5' to 3' direction?",
          ch(f"5'-{comp_53}-3'", "Complementary bases pair A with T and C with G, and the strands are antiparallel. The complement reads 3'-TACGGTAC-5', which is 5'-CATGGCAT-3' when written from the 5' end."),
          [ch(f"5'-{comp_35}-3'", "These are the complementary bases, but they are written in the 3' to 5' direction. The strand must be reversed to give the 5' to 3' sequence."),
           ch(f"5'-{strand}-3'", "This is the original sequence. The complementary strand has the complementary base at each position."),
           ch(f"5'-{strand[::-1]}-3'", "This is the original strand written backward. It has the same bases and not the complementary ones.")],
          "Pair A with T and C with G, then write the new strand 5' to 3', because the strands run in opposite directions.", difficulty="medium")

    B.mcq(6, "In a DNA double helix, one strand runs in the 5' to 3' direction from left to right. In which direction does the other strand run?",
          ch("In the opposite direction, so it runs 5' to 3' from right to left, which makes the strands antiparallel.", "DNA is an antiparallel double helix, with two strands running in opposite 5' to 3' orientations."),
          [ch("In the same direction, so it also runs 5' to 3' from left to right, which makes the strands parallel.", "The strands of DNA are antiparallel, not parallel."),
           ch("It has no particular direction, because only one strand of DNA is made of nucleotides that have a 5' end.", "Both strands are made of nucleotides, and each strand has a 5' end and a 3' end."),
           ch("It runs 3' to 5' from left to right, because the second strand must follow the same path as the first.", "A strand that runs 3' to 5' from left to right runs the same way as the first strand. The antiparallel strand runs the opposite way.")],
          "The two strands of DNA are antiparallel.", difficulty="medium")

    B.mcq(6, "During the synthesis of a strand of nucleic acid, where on the growing strand are new nucleotides added?",
          ch("To the 3' end, forming a covalent bond with the hydroxyl group of the sugar at that end of the strand.", "New nucleotides are added to the 3' end of the growing strand."),
          [ch("To the 5' end, forming a covalent bond with the phosphate group of the sugar at that end of the strand.", "Nucleotides are added to the 3' end, not the 5' end."),
           ch("To either end, because both ends of the strand have a hydroxyl group that can form a covalent bond.", "Only one end is used. The 5' end has a phosphate and the 3' end a hydroxyl group."),
           ch("To the middle of the strand, by breaking a hydrogen bond between two of the nucleotides in the strand.", "Nucleotides are added at the end of the strand, forming a covalent bond.")],
          "Nucleotides are added to the 3' end of a growing strand.", difficulty="medium")

    s1 = {"A": 30, "T": 30, "G": 20, "C": 20}
    s2 = {"A": 18, "U": 29, "G": 32, "C": 21}
    assert sum(s1.values()) == 100 and sum(s2.values()) == 100
    comp_rows = [("Sample 1", "30", "30", "0", "20", "20"), ("Sample 2", "18", "0", "29", "32", "21")]
    B.mcq(6, "A researcher analyzes the nitrogenous bases in two purified samples of nucleic acid. The table shows the percentage of each base. Which conclusion is best supported by the data?",
          ch("Sample 1 is probably double-stranded DNA, because it has thymine and equal amounts of A and T and of G and C, and sample 2 is probably RNA.", "DNA has thymine, and in a double helix A pairs with T and G with C. RNA contains uracil in place of thymine."),
          [ch("Sample 1 is probably RNA, because it has equal amounts of A and T, and sample 2 is probably DNA, because it contains uracil in addition to the other bases.", "Thymine is found in DNA and uracil is found in RNA, so the identification is reversed."),
           ch("Both samples are probably DNA, because both contain the bases adenine, guanine and cytosine, although in different amounts in each.", "Sample 2 contains uracil and no thymine, so it is not DNA."),
           ch("Both samples are probably RNA, because they contain different amounts of the four bases and neither one shows equal amounts of paired bases.", "Sample 1 contains thymine and not uracil, so it is not RNA, and its equal pairs fit a double helix.")],
          "Thymine indicates DNA, uracil indicates RNA, and equal A and T and equal G and C fit a double helix.",
          diagram=table(["Sample", "Adenine (%)", "Thymine (%)", "Uracil (%)", "Guanine (%)", "Cytosine (%)"], comp_rows, caption="Base composition of two nucleic acid samples", row_headers=True), difficulty="hard")

    B.mcq(6, "Which type of interaction holds the two strands of a DNA double helix together?",
          ch("Hydrogen bonds between the complementary bases A and T and between C and G of the strands", "Complementary bases on the two strands pair through hydrogen bonds."),
          [ch("Covalent bonds between the sugar of one strand and the phosphate of the opposite strand", "Covalent bonds join the nucleotides within each strand. They do not hold the two strands together."),
           ch("Ionic bonds between the positively charged and negatively charged bases of the two strands", "The bases are held together by hydrogen bonds, not by ionic bonds."),
           ch("Peptide bonds between the nitrogenous bases of the two strands of the double helix", "Peptide bonds join amino acids in proteins and do not occur in DNA.")],
          "The two strands are held together by hydrogen bonds between complementary bases.", difficulty="easy")

    B.mcq(6, "A mutation changes one nucleotide in a gene from G to A. Which statement best explains how this change could alter the information carried by the gene?",
          ch("Biological information is encoded in the sequence of nucleotides, so a change in the sequence can change the information.", "In nucleic acids the information is in the order of the nucleotide monomers, and a change in that order can change it."),
          [ch("The information is stored in the sugar-phosphate backbone, so a change in a base cannot change it in any way.", "The backbone is the same along the strand. The information is carried in the order of the bases."),
           ch("The information is stored in the number of strands in the molecule, so one base change has no effect on it.", "The number of strands does not carry the information. The sequence of nucleotides does."),
           ch("The information is stored in the hydrogen bonds between strands, so the change would only affect the strength of the bonds.", "The hydrogen bonds hold the strands together. The information is in the sequence of the bases.")],
          "In DNA and RNA, information is encoded in the sequence of nucleotides.", difficulty="hard")
