"""Unit 1, topics 1.3 Introduction to Macromolecules (8 questions) and 1.4 Carbohydrates (7).

Required content (CED 2025-26): 1.3.A.1 hydrolysis cleaves covalent bonds by adding water (the H goes to one monomer, the OH to the other); 1.3.A.2 dehydration
synthesis joins monomers by removing the equivalent of a water molecule, and joining many monomers is polymerization; 1.4.A.1 monosaccharides are the monomers
of polysaccharides (complex carbohydrates), which may be linear or branched (examples: cellulose, starch, glycogen). Excluded: the molecular structure of
specific carbohydrate polymers. Suggested skills 2.A (visual representations) and 1.A (describe concepts).
"""
from lib import *


def build(B):
    # ------------------------------------------------------------------ 1.3 Introduction to macromolecules
    B.mcq(3, "Two monosaccharides are joined to form a disaccharide. Which statement correctly describes the reaction?",
          ch("A hydrogen from one monomer and a hydroxyl group from the other are removed as water, and a covalent bond forms between the monomers.",
             "This is dehydration synthesis. The equivalent of a water molecule is lost and the two monomers are connected by a covalent bond."),
          [ch("A water molecule is added to the two monomers, and the covalent bond that held them together is broken in the process.",
              "This describes hydrolysis, which breaks a polymer into smaller molecules. Here a bond is being formed, not broken."),
           ch("A hydrogen ion moves from one monomer to the other, and an ionic bond forms between the two monomers without water.",
              "The monomers are connected by a covalent bond, and water is lost in the process. No ionic bond is formed."),
           ch("A molecule of carbon dioxide is released from each monomer, and the monomers are then held together by hydrogen bonds.",
              "Carbon dioxide is not released when monomers join. The monomers are connected by a covalent bond and water is removed.")],
          "Dehydration synthesis joins monomers by removing the equivalent of a water molecule.", difficulty="easy")

    B.mcq(3, "The bond between two monomers of a polymer is broken by hydrolysis. Which statement correctly describes what happens?",
          ch("A water molecule is added to the bond, with its hydrogen added to one monomer and its hydroxyl group added to the other monomer.",
             "Hydrolysis uses a water molecule to break a covalent bond between monomers. The H and OH of the water complete the two monomers."),
          [ch("A water molecule is removed from the two monomers, and a new covalent bond forms between them in its place.",
              "This describes dehydration synthesis, which builds polymers. Hydrolysis adds water and breaks a bond."),
           ch("Energy is released when the bond breaks, and no water is needed because the bond splits on its own into two parts.",
              "Hydrolysis requires water. The water molecule is split and its parts are added to the monomers."),
           ch("The two monomers each lose a hydroxyl group and a hydrogen ion, and these combine to form a new water molecule.",
              "That is the reverse of hydrolysis. In hydrolysis the water is a reactant that is added to the bond.")],
          "Hydrolysis breaks a bond between monomers by adding a water molecule.", difficulty="easy")

    B.mcq(3, "Which statement correctly pairs each reaction with its effect on a polymer?",
          ch("Dehydration synthesis joins monomers and releases water, and hydrolysis breaks the bonds between monomers by adding water.",
             "Dehydration synthesis builds polymers and produces water. Hydrolysis breaks polymers down and uses water."),
          [ch("Dehydration synthesis breaks the bonds between monomers and uses water, and hydrolysis joins monomers and releases water.",
              "This reverses the two reactions."),
           ch("Dehydration synthesis and hydrolysis both join monomers into polymers, but they differ in the type of monomer that is used.",
              "Hydrolysis breaks polymers into monomers. The two reactions are different in what they do, not in the monomers they use."),
           ch("Dehydration synthesis and hydrolysis both release a water molecule, but they differ in the type of bond that they form.",
              "Hydrolysis uses a water molecule instead of releasing one.")],
          "Dehydration synthesis builds polymers and releases water; hydrolysis breaks polymers and uses water.", difficulty="medium")

    n = 100
    assert n - 1 == 99
    B.mcq(3, f"A polymer is built from {n} monomers by dehydration synthesis. How many water molecules are released when it is made?",
          ch("99", "Joining 100 monomers in a chain makes 99 bonds, and each bond forms by the loss of one water molecule.", 99),
          [ch("100", "This assumes one water molecule for each monomer. A chain of 100 monomers has 99 bonds between them.", 100),
           ch("101", "This adds one to the number of monomers. The number of bonds is one less than the number of monomers.", 101),
           ch("50", "This assumes that monomers join in pairs. In a polymer every monomer is bonded to the next one in the chain.", 50)],
          "A chain of n monomers has n - 1 bonds, and each is formed by the loss of one water molecule.", difficulty="medium")

    m = 25
    assert m - 1 == 24
    B.mcq(3, f"A polymer made of {m} monomers is completely broken down into monomers by hydrolysis. How many water molecules are used in the process?",
          ch("24", "A chain of 25 monomers has 24 bonds, and each bond is broken by the addition of one water molecule.", 24),
          [ch("25", "This assumes one water molecule for each monomer. There are only 24 bonds in a chain of 25 monomers.", 25),
           ch("12", "This assumes that each water molecule breaks two bonds. Each hydrolysis reaction breaks one bond and uses one water molecule.", 12),
           ch("26", "This adds one to the number of monomers. The number of bonds is one fewer than the number of monomers.", 26)],
          "Complete hydrolysis of a chain of n monomers uses n - 1 water molecules.", difficulty="medium")

    sucrose, glucose, fructose = 342, 180, 180
    water = glucose + fructose - sucrose
    assert water == 18
    B.mcq(3, "In an experiment, 342 g of the disaccharide sucrose is completely broken down by hydrolysis into 180 g of glucose and 180 g of fructose. What mass of water is used in the reaction?",
          ch("18 g", "Mass is conserved, so the mass of water used is the mass of the products minus the mass of the sucrose: (180 + 180) - 342 = 18 g.", 18),
          [ch("36 g", "This assumes that two water molecules are used. Breaking the single bond in sucrose uses one water molecule.", 36),
           ch("9 g", "This divides the water between the two products. All of the water is added to the sucrose.", 9),
           ch("360 g", "This is the combined mass of the products. The mass of water is the difference between the products and the sucrose.", 360)],
          "The products have the mass of the sucrose plus the mass of the water that was added.", difficulty="medium")

    B.mcq(3, "In the digestive system, enzymes break down the large polymers in food into monomers. Which type of reaction is this, and what does each reaction require?",
          ch("Hydrolysis, which requires a molecule of water for each bond that is broken in the polymer.", "Digestion breaks bonds between monomers by adding water, which is hydrolysis."),
          [ch("Dehydration synthesis, which requires a molecule of water for each bond that is broken.", "Dehydration synthesis forms bonds and releases water. It does not break down polymers."),
           ch("Hydrolysis, which releases a molecule of water for each bond that is broken in the polymer.", "Hydrolysis uses water. It does not release it."),
           ch("Dehydration synthesis, which releases a molecule of water for each monomer that is released.", "Dehydration synthesis builds polymers, and it is the reverse of what digestion does.")],
          "Digestion of polymers into monomers is hydrolysis, which uses water.", difficulty="easy")

    B.mcq(3, "An enzyme that catalyzes the hydrolysis of a polymer into its monomers is inhibited in a cell. Which prediction is most consistent with the effect of this change?",
          ch("The polymer would accumulate, and fewer monomers would be available to the cell for building other molecules.", "Hydrolysis breaks polymers into monomers. If it is inhibited, less polymer is broken down and fewer monomers are produced."),
          [ch("The monomers would accumulate, and the polymer would be broken down more quickly by another reaction.", "Inhibiting the breakdown of the polymer would make fewer monomers, not more."),
           ch("The cell would have the same amount of polymer, because dehydration synthesis would also be stopped by the inhibitor.", "The inhibitor acts on an enzyme for hydrolysis. Dehydration synthesis would not be stopped by it."),
           ch("Water would accumulate in the cell, because it is no longer needed to join monomers into a polymer.", "Hydrolysis uses water to break the polymer, and the inhibition does not change the joining of monomers.")],
          "Blocking hydrolysis blocks the release of monomers from polymers.", difficulty="hard")

    # ------------------------------------------------------------------ 1.4 Carbohydrates
    B.mcq(4, "What are the monomers of polysaccharides such as starch and cellulose?",
          ch("Monosaccharides, which are simple sugars joined by covalent bonds into chains", "Polysaccharides, or complex carbohydrates, are polymers of monosaccharides."),
          [ch("Amino acids, which are joined by covalent bonds called peptide bonds", "Amino acids are the monomers of proteins, not of carbohydrates."),
           ch("Nucleotides, which are joined by covalent bonds in a long sugar-phosphate chain of many units", "Nucleotides are the monomers of nucleic acids, not of carbohydrates."),
           ch("Fatty acids, which are joined by covalent bonds in long branched chains", "Fatty acids are parts of many lipids. Lipids are not polymers of fatty acids, and carbohydrates are not made of them.")],
          "The monomers of polysaccharides are monosaccharides (simple sugars).", difficulty="easy")

    B.mcq(4, "Which of the following are examples of polysaccharides?",
          ch("Starch, glycogen and cellulose, which are all polymers of sugar monomers", "These three are complex carbohydrates made from monosaccharides."),
          [ch("Glucose, fructose and sucrose, which are all small sugar molecules", "Glucose and fructose are monosaccharides, and sucrose is a disaccharide. None is a polysaccharide."),
           ch("Starch, DNA and cholesterol, which are all large molecules in cells", "DNA is a nucleic acid and cholesterol is a steroid. Only starch is a polysaccharide."),
           ch("Glycogen, hemoglobin and cellulose, which are all found in living organisms", "Hemoglobin is a protein, so it is not a polysaccharide.")],
          "Starch, glycogen and cellulose are polysaccharides.", difficulty="easy")

    B.mcq(4, "Which statement correctly pairs a polysaccharide with its function?",
          ch("Glycogen, which stores energy in the cells of animals such as humans", "Animals store glucose as glycogen, and plants store it as starch."),
          [ch("Cellulose, which stores energy in the liver cells of animals", "Cellulose is a structural molecule in plant cell walls, not an energy store in animals."),
           ch("Starch, which provides structural support in the cell walls of plants", "Starch stores energy in plants. The structural polysaccharide of plants is cellulose."),
           ch("Cellulose, which carries the genetic information in plant cells", "Genetic information is carried by nucleic acids, not by polysaccharides.")],
          "Starch and glycogen store energy, and cellulose provides structural support in plant cell walls.", difficulty="medium")

    B.mcq(4, "Which statement about the structure of polysaccharides is correct?",
          ch("They may be linear or branched polymers of monosaccharides that are connected by covalent bonds.", "Complex carbohydrates are made of sugar monomers joined by covalent bonds, in chains that may be linear or branched."),
          [ch("They are always linear chains, because each monosaccharide can form a covalent bond with only two others.", "Some polysaccharides are branched, so the chains do not have to be linear."),
           ch("They are held together by hydrogen bonds, which form between the monosaccharides in the polymer chain.", "The bonds between the monomers are covalent. Hydrogen bonds are weaker interactions."),
           ch("They are polymers of amino acids that have been modified by the addition of one or more sugar groups.", "Polysaccharides are polymers of monosaccharides, not of amino acids.")],
          "Polysaccharides are linear or branched polymers of monosaccharides.", difficulty="medium")

    poly_rows = [("Starch", "Plants", "Stores energy"), ("Glycogen", "Animals", "Stores energy"), ("Cellulose", "Plants", "Gives structural support in cell walls")]
    B.mcq(4, "The table gives information about three polysaccharides. Which statement is best supported by the table?",
          ch("Starch and glycogen both store energy, but they are made by different groups of living organisms.", "Both are energy stores. Starch is found in plants and glycogen in animals."),
          [ch("Cellulose and glycogen both store energy, but they are made by different groups of organisms.", "The table shows that cellulose provides structural support. It is not described as an energy store."),
           ch("Starch and cellulose are made by plants, so they must have the same structure and the same function in plants.", "They are both made by plants, but their functions differ. The table shows different functions."),
           ch("Glycogen and cellulose are made by different organisms, so only one of them can be a polymer of sugars.", "All three are polysaccharides, so all three are polymers of sugars.")],
          "The table compares the source and function of starch, glycogen and cellulose.",
          diagram=table(["Polysaccharide", "Made by", "Function"], poly_rows, caption="Three polysaccharides", row_headers=True), difficulty="medium")

    water_released = 249
    assert water_released + 1 == 250
    B.mcq(4, f"A linear polysaccharide is built from glucose monomers by dehydration synthesis, and {water_released} water molecules are released. How many glucose monomers does the polysaccharide contain?",
          ch("250", "A linear chain of n monomers has n - 1 bonds, so the release of 249 water molecules means that 250 monomers were joined.", 250),
          [ch("249", "This takes the number of water molecules as the number of monomers. There is one more monomer than there are bonds.", 249),
           ch("248", "This subtracts one from the number of water molecules. The number of monomers is one more than the number of bonds.", 248),
           ch("500", "This doubles the number of monomers. Each water molecule is released when one bond forms between two monomers.", 500)],
          "A chain of n monomers has n - 1 bonds, so the number of monomers is the number of water molecules plus one.", difficulty="medium")

    B.mcq(4, "A mutation prevents a plant from making cellulose. Which effect is most likely in the cells of the plant?",
          ch("The cell walls would be weaker, so the cells of the plant would have less structural support to hold them upright.", "Cellulose is the structural polysaccharide of plant cell walls, so without it the walls are weaker."),
          [ch("The plant would be unable to store energy, because cellulose is the main energy storage polysaccharide in plant cells.", "Plants store energy mainly as starch. Cellulose has a structural role."),
           ch("The plant would be unable to make glucose, because glucose is the monomer that is built from cellulose.", "Glucose is the monomer from which cellulose is built, not the other way around."),
           ch("The plant would store genetic information in a different way, because cellulose is part of the plant's DNA.", "Cellulose is not part of DNA. Genetic information is stored in nucleic acids.")],
          "Cellulose provides structural support in plant cell walls.", difficulty="hard")
