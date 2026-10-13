"""Unit 2, topics 2.9 Cell Compartmentalization (6 questions) and 2.10 Origins of Cell Compartmentalization (5).

Required content (CED 2025-26): 2.9.A membranes and membrane-bound organelles compartmentalize intracellular metabolic processes and specific enzymatic reactions in eukaryotic cells;
2.9.B internal membranes minimize competing interactions and increase the surface area where reactions occur; 2.10.A.1 mitochondria and chloroplasts evolved from once free-living prokaryotic
cells by endosymbiosis; 2.10.A.2 prokaryotes typically lack internal membrane-bound organelles but have internal regions with specialized structures and functions; 2.10.A.3 eukaryotic cells
maintain internal membranes that partition the cell into specialized regions. Suggested skills: 6.E (predict) and 6.B (support a claim with evidence).
"""
from lib import *


def build(B):
    # ------------------------------------------------------------------ 2.9 Cell compartmentalization
    B.mcq(9, "Which statement best describes how membranes and membrane-bound organelles compartmentalize a eukaryotic cell?",
          ch("They separate metabolic processes and specific enzymatic reactions into different regions of the cell, so each takes place in its own environment.", "Compartmentalization keeps different reactions in separate regions of the cell."),
          [ch("They combine all of the metabolic processes of the cell into a single region, so that every enzyme can reach every substrate in the cell.", "Compartmentalization separates processes. It does not combine them into one region."),
           ch("They prevent any molecules from moving between regions of the cell, so each organelle must make everything that it needs.", "Molecules are moved between compartments, for example in vesicles and through membrane proteins."),
           ch("They store the genetic information of the cell in each organelle, so that every compartment can make its own proteins.", "Compartmentalization is about separating reactions and processes. DNA is not stored in every organelle.")],
          "Membranes compartmentalize intracellular metabolic processes and specific enzymatic reactions.", difficulty="easy")

    B.mcq(9, "Lysosomes keep their hydrolytic enzymes inside a membrane. Which statement best explains why this is important to the cell?",
          ch("The membrane separates the enzymes from the cytoplasm, which minimizes competing interactions and keeps them from digesting the cell's own components.", "Internal membranes minimize competing interactions by keeping some reactions away from other parts of the cell."),
          [ch("The membrane makes the enzymes work more quickly, because the enzymes can digest material only when they are surrounded by a membrane first.", "Enclosure is not what speeds up the enzymes. It separates their activity from the cytoplasm."),
           ch("The membrane gives the enzymes their energy, because ATP is stored in the membrane of the lysosome until the enzymes need it.", "Membranes do not supply energy to enzymes in this way."),
           ch("The membrane makes the lysosomes larger, which increases the surface area of the cell and so allows it to exchange more materials.", "The lysosome membrane does not increase the surface area of the plasma membrane of the cell.")],
          "Internal membranes minimize competing interactions and protect the rest of the cell from enzymes.", difficulty="medium")

    B.mcq(9, "The inner membrane of a mitochondrion has many folds. Which statement best explains how this feature contributes to the compartmentalization of reactions in the cell?",
          ch("The folds increase the surface area of membrane on which the reactions of the electron transport chain can take place.", "Internal membranes increase the surface area where reactions can occur."),
          [ch("The folds decrease the surface area of the membrane, so the reactions are concentrated into a very small part of the organelle.", "Folds increase the surface area and do not decrease it."),
           ch("The folds separate the organelle from the cytoplasm, so no molecules can move into or out of the mitochondrion.", "The outer membrane and the folds do not stop all movement of molecules across the membranes."),
           ch("The folds make a second nucleus inside the organelle, which controls the reactions that take place within the mitochondrion.", "Mitochondria do not contain a second nucleus. The folds are part of the inner membrane.")],
          "Internal membranes increase the surface area where reactions can occur.", difficulty="medium")

    B.mcq(9, "A drug damages the membranes of lysosomes so that they leak. Which prediction is most consistent with the role of lysosomes and of compartmentalization?",
          ch("The hydrolytic enzymes would escape into the cytoplasm and could digest components of the cell, which could lead to cell death.", "Without the membrane, the enzymes are no longer separated from the rest of the cell, and lysosomes also play a role in cell death."),
          [ch("The cell would make more proteins than before, because the enzymes that escape from the lysosomes would increase protein synthesis.", "The enzymes are hydrolytic, so they break molecules down."),
           ch("The cell would not be affected, because the enzymes work only inside the lysosome and are inactive anywhere else in the cell.", "The enzymes would be able to act on components in the cytoplasm if they escape."),
           ch("The cell would produce more ATP than before, because the lysosome enzymes would supply energy to the mitochondria of the cell.", "Hydrolytic enzymes break down molecules and do not supply ATP to the mitochondria.")],
          "Compartmentalization protects the cell from its own digestive enzymes.", difficulty="hard")

    B.mcq(9, "Which choice lists only membrane-bound structures of a eukaryotic cell?",
          ch("The nucleus, mitochondria, endoplasmic reticulum, Golgi complex and lysosomes", "All of these are surrounded by membranes."),
          [ch("The nucleus, ribosomes, mitochondria, endoplasmic reticulum, lysosomes and vacuoles", "Ribosomes have no membrane."),
           ch("Mitochondria, ribosomes, the Golgi complex, vacuoles and the cell wall", "Ribosomes have no membrane, and the cell wall is not a membrane-bound structure."),
           ch("The nucleus, the cytoskeleton, the Golgi complex, lysosomes and ribosomes", "The cytoskeleton and ribosomes have no membrane.")],
          "The nucleus, mitochondria, ER, Golgi complex and lysosomes are membrane-bound.", difficulty="medium")

    B.mcq(9, "A eukaryotic cell builds fatty acids in one compartment and breaks fatty acids down in another compartment. Which statement best explains the advantage of this arrangement?",
          ch("The enzymes of the two opposing pathways are kept apart, so the pathways do not interfere and can be regulated separately.", "Internal membranes minimize competing interactions between processes."),
          [ch("The two pathways are always active at the same time in the same place, which makes the cell produce more energy at the same time.", "Separating the pathways keeps them from running together in the same place."),
           ch("The enzymes of the two pathways move between the compartments, which lets each enzyme catalyze the reaction of the other pathway.", "Enzymes are specific to their reactions and are kept in their own compartments."),
           ch("The membranes between the compartments provide the energy for both pathways, so that the cell does not have to make ATP.", "Membranes do not provide energy for the pathways.")],
          "Compartmentalization minimizes competing interactions between processes.", difficulty="hard")

    # ------------------------------------------------------------------ 2.10 Origins of cell compartmentalization
    B.mcq(10, "According to the theory of endosymbiosis, from what did mitochondria and chloroplasts evolve?",
          ch("Free-living prokaryotic cells that were taken in by an ancestor of eukaryotic cells and became organelles inside it", "Mitochondria and chloroplasts evolved from once free-living prokaryotes by endosymbiosis."),
          [ch("Pieces of the nucleus that grew their own membranes and moved into the cytoplasm of the ancestral eukaryotic cell long ago", "The theory states that they came from free-living prokaryotes, not from the nucleus."),
           ch("Vesicles of the endomembrane system that gained DNA from the nucleus and then took over the production of ATP", "The theory involves once free-living prokaryotes."),
           ch("Viruses that infected the ancestral eukaryotic cell and replaced its metabolic enzymes with enzymes that make ATP", "Mitochondria and chloroplasts are thought to have come from prokaryotic cells and not from viruses.")],
          "Mitochondria and chloroplasts evolved from free-living prokaryotes by endosymbiosis.", difficulty="easy")

    B.mcq(10, "Which observation provides the best support for the claim that mitochondria evolved from free-living bacteria?",
          ch("Mitochondria have their own circular DNA and ribosomes like those of bacteria, and they are surrounded by a double membrane.", "These features of mitochondria are similar to those of prokaryotes, which supports an ancestral relationship."),
          [ch("Mitochondria are found in the cells of animals, plants and fungi, and they are the site of the production of most of the cell's ATP.", "Being found in many organisms does not show that they came from bacteria."),
           ch("Mitochondria are the largest organelles in most cells, and they are easier to see than other organelles with a light microscope.", "The size of an organelle says nothing about its origin."),
           ch("Mitochondria use oxygen in cellular respiration, and the oxygen they use is released by the chloroplasts in plant cells.", "The use of oxygen does not show that mitochondria evolved from bacteria.")],
          "Features shared with bacteria support the claim that mitochondria evolved from free-living bacteria.", difficulty="medium")

    B.mcq(10, "Which statement correctly compares the compartmentalization of prokaryotic and eukaryotic cells?",
          ch("Prokaryotic cells typically lack internal membrane-bound organelles, whereas eukaryotic cells have internal membranes that partition the cell.", "Prokaryotes have specialized regions without membrane-bound organelles, and eukaryotes have internal membranes."),
          [ch("Prokaryotic cells have more internal membrane-bound organelles than eukaryotic cells have, and eukaryotic cells have no specialized regions of any kind.", "This reverses the comparison. Eukaryotic cells have internal membranes."),
           ch("Prokaryotic cells and eukaryotic cells both have a nucleus, mitochondria and an endomembrane system that divide the cell into parts.", "Prokaryotes typically lack these membrane-bound organelles."),
           ch("Prokaryotic cells have no specialized structures of any kind inside, and eukaryotic cells have only one internal membrane around the DNA.", "Prokaryotes have internal regions with specialized structures, and eukaryotic cells have many internal membranes.")],
          "Eukaryotic cells have internal membranes that partition the cell; prokaryotes typically do not have membrane-bound organelles.", difficulty="medium")

    B.mcq(10, "A newly discovered single-celled organism has a plasma membrane, a cell wall, ribosomes and DNA, but no nucleus and no mitochondria. Which statement about the organism is best supported by what is known about cell structure?",
          ch("It is a prokaryote, because it typically lacks internal membrane-bound organelles, although it may have specialized regions.", "The absence of membrane-bound organelles such as a nucleus and mitochondria is typical of a prokaryotic cell."),
          [ch("It is a eukaryote, because it has ribosomes and DNA, which are found only in cells that have a nucleus and mitochondria.", "Ribosomes and DNA are found in all forms of life, including prokaryotes."),
           ch("It is a eukaryote, because it has a cell wall, which is a membrane-bound organelle that is found only in eukaryotes.", "A cell wall is not a membrane-bound organelle, and prokaryotes also have cell walls."),
           ch("It cannot be a living cell, because every living cell must have a nucleus that contains its genetic information.", "Prokaryotic cells are alive and do not have a nucleus.")],
          "Prokaryotes typically lack internal membrane-bound organelles.", difficulty="medium")

    feat = [("Shape of the main DNA molecule", "Circular", "Circular", "Linear"), ("Division of the structure", "By a process similar to binary fission", "Binary fission", "Mitosis of the whole cell"),
            ("Ribosomes are most similar to", "Bacterial ribosomes", "Bacterial ribosomes", "Eukaryotic ribosomes")]
    B.mcq(10, "The table compares features of mitochondria, bacteria and the nuclear genome of a eukaryotic cell. Which claim is best supported by the data?",
          ch("Mitochondria share several features with bacteria that they do not share with the nucleus of a eukaryotic cell, supporting the claim that mitochondria evolved from bacteria.", "The shape of the DNA, the type of division and the type of ribosomes all match those of bacteria."),
          [ch("Mitochondria share several features with the nucleus of a eukaryotic cell that they do not share with bacteria, which shows that they evolved from the nucleus of the cell.", "The table shows that mitochondria match bacteria in each feature."),
           ch("Mitochondria are different from bacteria in all of the features shown in the table, which shows that they cannot be related to them.", "The table shows that mitochondria are similar to bacteria in every feature listed."),
           ch("Bacteria and the eukaryotic nucleus are the same in all of the features shown in the table, so they must have a common origin.", "The table shows that bacteria and the nucleus differ in each feature.")],
          "Shared features support an evolutionary relationship.",
          diagram=table(["Feature", "Mitochondrion", "Bacterium", "Eukaryotic nucleus"], feat, caption="Comparison of features", row_headers=True), difficulty="hard")
