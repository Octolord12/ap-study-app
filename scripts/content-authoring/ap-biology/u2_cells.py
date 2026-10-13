"""Unit 2, topics 2.1 Cell Structure and Function (12 questions) and 2.2 Cell Size (8).

Required content (CED 2025-26): 2.1.A.1 ribosomes (rRNA and protein, no membrane, in all forms of life, common ancestry) make proteins from mRNA; 2.1.A.2 the endomembrane
system (ER, Golgi, lysosomes, vacuoles and vesicles, nuclear envelope, plasma membrane) modifies, packages and transports polysaccharides, lipids and proteins; 2.1.A.3 rough ER
(bound ribosomes, protein synthesis), smooth ER (detoxification, lipid synthesis); 2.1.A.4 Golgi folds and modifies products and packages proteins; 2.1.A.5 mitochondria have a
double membrane, the inner one folded; 2.1.A.6 lysosomes (hydrolytic enzymes, apoptosis); 2.1.A.7 vacuoles (a plant's large vacuole holds nutrients and water and maintains turgor);
2.1.A.8 chloroplasts (double membrane, photosynthesis, in plants and photosynthetic algae). 2.2.A.1-2 surface area-to-volume ratio limits exchange of materials and heat: smaller
cells have a higher ratio, the ratio falls as volume rises, membrane folds help, smaller organisms lose heat faster and have a higher metabolic rate per unit mass. Equations given:
sphere and cube volume and surface area. Excluded: specific smooth ER functions in specialized cells and the Golgi's role in specific phospholipids or lysosomal enzymes.
"""
import math

from lib import *


def build(B):
    # ------------------------------------------------------------------ 2.1 Cell structure and function
    B.mcq(1, "Which statement correctly describes ribosomes?",
          ch("They are made of rRNA and protein, have no surrounding membrane, and make proteins from the sequence of messenger RNA.",
             "Ribosomes are non-membrane subcellular structures made of rRNA and protein. They synthesize proteins using the sequence of mRNA."),
          [ch("They are membrane-bound organelles made mostly of lipid, and they package finished proteins for transport out of the cell.",
              "Ribosomes have no membrane and are not made of lipid. Packaging of proteins is a function of the Golgi complex."),
           ch("They are made of DNA and protein, are found only in eukaryotic cells, and copy the genetic information of the nucleus.",
              "Ribosomes are made of rRNA and protein and are found in cells of all forms of life, including prokaryotes."),
           ch("They are double-membrane organelles that contain their own DNA, and they make most of the ATP that the cell uses.",
              "This describes mitochondria. Ribosomes have no membrane and do not make ATP.")],
          "Ribosomes are non-membrane structures of rRNA and protein that synthesize proteins from mRNA.", difficulty="easy")

    B.mcq(1, "Which observation about cells is best evidence that all known forms of life share a common ancestor?",
          ch("Cells of all known forms of life contain ribosomes that make proteins according to messenger RNA sequences.",
             "A structure found in the cells of every form of life is best explained by inheritance from a common ancestor."),
          [ch("Cells of all known forms of life contain mitochondria that make ATP by aerobic cellular respiration in the cell.",
              "Many prokaryotes have no mitochondria, so mitochondria are not found in all forms of life."),
           ch("Cells of all known forms of life are surrounded by a cell wall that gives the cell its shape and its structure.",
              "Animal cells have no cell wall, so cell walls are not found in all forms of life."),
           ch("Cells of all known forms of life contain chloroplasts that capture light energy and store it as chemical energy.",
              "Chloroplasts occur only in plants and photosynthetic algae, so they are not found in all forms of life.")],
          "Ribosomes occur in all forms of life, which reflects common ancestry.", difficulty="easy")

    B.mcq(1, "Which choice lists only structures that are part of the endomembrane system of a eukaryotic cell?",
          ch("Endoplasmic reticulum, Golgi complex, lysosomes, transport vesicles and the plasma membrane", "These membrane-bound structures work together to modify, package and transport proteins, lipids and polysaccharides."),
          [ch("Ribosomes, mitochondria, chloroplasts, lysosomes, the Golgi complex and the cell wall", "Ribosomes have no membrane, and mitochondria and chloroplasts are not part of the endomembrane system."),
           ch("Endoplasmic reticulum, ribosomes, mitochondria, vacuoles and the nuclear envelope", "Ribosomes and mitochondria are not part of the endomembrane system."),
           ch("Golgi complex, chloroplasts, transport vesicles, the cell wall and the plasma membrane", "Chloroplasts and the cell wall are not part of the endomembrane system.")],
          "The endomembrane system includes the ER, Golgi complex, lysosomes, vacuoles and vesicles, the nuclear envelope and the plasma membrane.", difficulty="medium")

    B.mcq(1, "A gland cell makes large amounts of a protein that is secreted from the cell. Which structure is most likely to be abundant in this cell?",
          ch("Rough endoplasmic reticulum, which has ribosomes bound to its membrane and helps to carry out protein synthesis", "Rough ER is associated with membrane-bound ribosomes, and it helps with synthesizing proteins."),
          [ch("Smooth endoplasmic reticulum, which has ribosomes bound to its membrane and makes most of the cell's proteins", "Smooth ER does not have bound ribosomes. It functions in lipid synthesis and detoxification."),
           ch("Lysosomes, which contain ribosomes in their interior and make proteins for the digestion of material in the cell", "Lysosomes contain hydrolytic enzymes that digest material. They are not the site of protein synthesis."),
           ch("Chloroplasts, which contain ribosomes on their outer membrane and make the proteins that are secreted from the cell", "Chloroplasts are the site of photosynthesis in plants and algae and are not in animal gland cells.")],
          "Rough ER has bound ribosomes and is involved in protein synthesis.", difficulty="medium")

    B.mcq(1, "Liver cells detoxify drugs and make lipids. Which organelle would be expected to be especially abundant in a liver cell?",
          ch("Smooth endoplasmic reticulum, because its functions include detoxification and the synthesis of lipids", "Smooth ER is associated with detoxifying cells and with lipid synthesis."),
          [ch("Rough endoplasmic reticulum, because its bound ribosomes carry out detoxification and the synthesis of lipids", "Rough ER is associated with protein synthesis, not with detoxification and lipid synthesis."),
           ch("The nuclear envelope, because it separates the cell's DNA from the toxins that are present in the cytoplasm", "The nuclear envelope encloses the nucleus. It does not detoxify drugs or make lipids."),
           ch("Chloroplasts, because they use light energy to break down drugs and to build lipids from carbon dioxide", "Chloroplasts are found in plants and algae. They are not the site of detoxification in the liver.")],
          "Smooth ER functions in detoxification and in lipid synthesis.", difficulty="medium")

    B.mcq(1, "Which choice correctly describes functions of the Golgi complex?",
          ch("It chemically modifies and correctly folds newly made cellular products, and it packages proteins for trafficking.", "The Golgi complex is a series of flattened membrane sacs that modifies new products and packages proteins for transport."),
          [ch("It reads messenger RNA and joins amino acids into proteins, and then it packages the proteins into vesicles.", "Joining amino acids into proteins according to mRNA is the function of ribosomes."),
           ch("It makes most of the ATP of the cell, and it also stores the proteins that it makes until they are needed.", "ATP is made mainly by mitochondria. The Golgi complex modifies and packages products."),
           ch("It digests worn-out organelles with hydrolytic enzymes, and it releases the products into the cytoplasm for reuse.", "Digestion with hydrolytic enzymes is a function of lysosomes.")],
          "The Golgi complex modifies, folds and packages cellular products.", difficulty="medium")

    B.mcq(1, "Mitochondria have a double membrane, and the inner membrane is highly folded. Which statement best explains how these features help the mitochondrion?",
          ch("The two membranes provide separate compartments for different metabolic reactions, and the inner folds allow more efficient ATP synthesis.", "A double membrane provides compartments for reactions of aerobic respiration, and the folds increase the surface area for ATP synthesis."),
          [ch("The two membranes allow light energy to be captured, and the folds of the inner membrane store the glucose that is made there.", "Light is captured in chloroplasts. Mitochondria use energy stored in molecules to make ATP."),
           ch("The two membranes make a barrier that no molecules can cross, and the folds of the inner membrane keep the DNA protected inside the organelle.", "Molecules do cross the mitochondrial membranes through proteins. The folds increase membrane surface area."),
           ch("The two membranes help the mitochondrion to make proteins, and the folds of the inner membrane carry the ribosomes.", "The main role of the folds is to increase the surface area for ATP synthesis, not to carry ribosomes.")],
          "The double membrane compartmentalizes respiration, and the folded inner membrane increases the surface area for making ATP.", difficulty="medium")

    B.mcq(1, "A white blood cell takes in a bacterium by forming a vesicle around it. Which organelle most likely fuses with this vesicle to digest the bacterium?",
          ch("A lysosome, which contains hydrolytic enzymes that digest material", "Lysosomes are membrane-enclosed sacs of hydrolytic enzymes that digest material taken in by the cell."),
          [ch("A chloroplast, which contains pigments that break down bacteria with light energy captured from the surroundings", "Chloroplasts are found in plants and algae and capture light energy for photosynthesis."),
           ch("A ribosome, which contains enzymes that break down the proteins of the bacterium into individual amino acids", "Ribosomes build proteins and do not digest material."),
           ch("A large central vacuole, which is surrounded by water that dissolves the bacterium and stores the material", "A large central vacuole is a feature of plant cells and its main role is storage of nutrients and water.")],
          "Lysosomes digest material with hydrolytic enzymes.", difficulty="medium")

    B.mcq(1, "A houseplant wilts when it is not watered. Which structure of its cells is most directly involved in maintaining the turgor pressure that keeps the plant upright?",
          ch("The large central vacuole, which stores water and nutrients and so maintains the turgor pressure of the cell", "In plant cells, a specialized large vacuole maintains turgor pressure through nutrient and water storage."),
          [ch("The mitochondrion, which stores the water of the cell in the matrix and so keeps its cytoplasm full", "Mitochondria are the site of aerobic respiration. They are not the main water store."),
           ch("The Golgi complex, which stores water in its flattened sacs and pumps it out to the cell wall as needed", "The Golgi complex modifies and packages products. It is not the main store of water."),
           ch("The nucleus, which stores water in the nuclear envelope and releases it to the cytoplasm when the plant is dry", "The nucleus holds the DNA of the cell and is not the main store of water.")],
          "A large vacuole in plant cells maintains turgor pressure by storing water and nutrients.", difficulty="medium")

    B.mcq(1, "Which pair of organelles is surrounded by a double membrane?",
          ch("Mitochondria and chloroplasts", "Both mitochondria and chloroplasts have a double membrane."),
          [ch("Lysosomes and vacuoles", "Lysosomes and vacuoles are surrounded by a single membrane."),
           ch("The Golgi complex and ribosomes", "The Golgi complex has a single membrane, and ribosomes have no membrane."),
           ch("Transport vesicles and the rough ER", "Vesicles and the endoplasmic reticulum are bounded by a single membrane.")],
          "Mitochondria and chloroplasts have double membranes.", difficulty="easy")

    cell_rows = [("Cell 1", "High", "Low", "Low", "Low"), ("Cell 2", "Low", "High", "Low", "Low"), ("Cell 3", "Low", "Low", "High", "Low"), ("Cell 4", "Low", "Low", "Low", "High")]
    B.mcq(1, "The table shows the relative abundance of four structures in four types of cell. One of the cells makes and secretes large amounts of a protein hormone. Which cell is it most likely to be?",
          ch("Cell 1, because it has a high abundance of rough ER, where proteins are made", "Rough ER has bound ribosomes that help with protein synthesis, which a protein-secreting cell needs in large amounts."),
          [ch("Cell 2, because it has a high abundance of smooth ER, where proteins are made", "Smooth ER is associated with lipid synthesis and detoxification, not with protein synthesis."),
           ch("Cell 3, because it has a high abundance of mitochondria, where proteins are made", "Mitochondria make ATP. They are not the main site of protein synthesis for secretion."),
           ch("Cell 4, because it has a high abundance of lysosomes, where proteins are made", "Lysosomes digest material and are not the site where proteins are made.")],
          "A cell that secretes a protein needs a lot of rough ER.",
          diagram=table(["Cell", "Rough ER", "Smooth ER", "Mitochondria", "Lysosomes"], cell_rows, caption="Relative abundance of four structures", row_headers=True), difficulty="medium")

    B.mcq(1, "A protein that will be secreted from a cell is made on a ribosome. Which sequence best describes the path of the protein through the cell?",
          ch("Rough ER, transport vesicle, Golgi complex, secretory vesicle, plasma membrane", "The protein is made at the rough ER, moves in vesicles to the Golgi complex for modification, and is then packaged in vesicles that fuse with the plasma membrane."),
          [ch("Golgi complex, rough ER, lysosome, transport vesicle, nuclear envelope, plasma membrane", "The protein is made at the rough ER before it reaches the Golgi complex, and it is not taken to a lysosome for secretion."),
           ch("Nucleus, mitochondrion, rough ER, secretory vesicle, plasma membrane", "Proteins are not made in the nucleus and do not pass through the mitochondrion on the way out of the cell."),
           ch("Rough ER, lysosome, Golgi complex, nuclear envelope, plasma membrane", "A lysosome digests material and is not part of the secretion pathway, and the nuclear envelope is not on the path.")],
          "Secreted proteins pass from rough ER to the Golgi complex in vesicles and then to the plasma membrane.", difficulty="hard")

    # ------------------------------------------------------------------ 2.2 Cell size
    B.mcq(2, "Which of the following cells has the highest surface area-to-volume ratio?",
          ch("A small cell, because its surface area is large compared with its volume", "A smaller cell has a higher surface area-to-volume ratio, so it can exchange materials efficiently."),
          [ch("A large cell, because its large volume means that it has more membrane through which to exchange material", "Volume increases faster than surface area as a cell grows, so a large cell has a lower ratio."),
           ch("A cell of any size, because the surface area-to-volume ratio depends on the type of cell and not on its size", "The ratio depends on the size and shape of the cell. Smaller cells have higher ratios."),
           ch("A cell with the most organelles, because its organelles increase the surface area of the plasma membrane", "Organelles inside the cell do not change the surface area of the plasma membrane.")],
          "Smaller cells typically have a higher surface area-to-volume ratio.", difficulty="easy")

    side = 3.0
    sa, vol = 6 * side**2, side**3
    assert (sa, vol, sa / vol) == (54.0, 27.0, 2.0)
    B.mcq(2, f"A cube-shaped cell has sides of length {side:.0f} µm. What is its surface area-to-volume ratio? (Surface area of a cube = 6s²; volume of a cube = s³.)",
          ch("2.0 µm⁻¹", "Surface area = 6 x 3² = 54 µm² and volume = 3³ = 27 µm³, so the ratio is 54 / 27 = 2.0 per µm.", 2.0),
          [ch("54 µm⁻¹", "This is the surface area. The ratio is the surface area divided by the volume.", 54.0),
           ch("0.5 µm⁻¹", "This is the volume divided by the surface area, which is the inverse of the ratio that was asked for.", 0.5),
           ch("18 µm⁻¹", "This divides the surface area by the side length (54 / 3). The ratio is the surface area divided by the volume.", 18.0)],
          "Surface area-to-volume ratio = surface area / volume = 6s² / s³ = 6 / s.", difficulty="medium")

    r = 5.0
    sa_s, v_s = 4 * math.pi * r**2, 4 / 3 * math.pi * r**3
    assert round(sa_s / v_s, 2) == 0.60
    B.mcq(2, f"A spherical cell has a radius of {r:.0f} µm. What is its surface area-to-volume ratio? (Surface area of a sphere = 4πr²; volume of a sphere = 4/3 πr³.)",
          ch("0.60 µm⁻¹", "Surface area = 4π(5)² = 314 µm² and volume = 4/3 π(5)³ = 524 µm³, so the ratio is 314 / 524 = 0.60 per µm.", round(sa_s / v_s, 2)),
          [ch("1.7 µm⁻¹", "This is the inverse of the ratio (524 / 314), the volume divided by the surface area.", round(v_s / sa_s, 2)),
           ch("3.0 µm⁻¹", "This leaves out the division by the radius. For a sphere the ratio is 3 / r, which is 0.60 when r is 5 µm.", 3.0),
           ch("0.30 µm⁻¹", "This is the ratio for a sphere with a radius of 10 µm (3 / 10). For a radius of 5 µm the ratio is 3 / 5 = 0.60.", 0.30)],
          "For a sphere the ratio simplifies to 3 / r.", difficulty="medium")

    B.mcq(2, "The radius of a spherical cell doubles as the cell grows. What happens to the surface area-to-volume ratio of the cell?",
          ch("It falls to one half of its original value, because volume increases eightfold and surface area fourfold.", "Doubling the radius multiplies the surface area by 2² = 4 and the volume by 2³ = 8, so the ratio is multiplied by 4 / 8 = 1/2."),
          [ch("It doubles, because the surface area and the volume both double when the radius of the cell doubles.", "Surface area increases fourfold and volume eightfold, not twofold."),
           ch("It does not change, because the surface area and the volume of the cell increase by the same factor.", "Volume increases by a larger factor than surface area, so the ratio changes."),
           ch("It decreases to one quarter of its original value, because the surface area of the cell increases fourfold.", "The volume increases eightfold as well, so the ratio falls to one half, not one quarter.")],
          "As a cell grows, its volume increases faster than its surface area, so the ratio decreases.", difficulty="medium")

    B.mcq(2, "Which statement best explains why most cells are small?",
          ch("As a cell grows, its volume increases faster than its surface area, so the plasma membrane may not exchange materials fast enough for the cell.", "A decreasing surface area-to-volume ratio limits the exchange of nutrients and waste, which restricts cell size."),
          [ch("As a cell grows, its surface area increases faster than its volume, so the cell has too much membrane for the amount of cytoplasm.", "The opposite is true: volume increases faster than surface area as a cell grows."),
           ch("As a cell grows, its DNA is divided among more organelles, so the cell cannot make the proteins that it requires.", "This does not describe the limit set by the surface area-to-volume ratio."),
           ch("As a cell grows, its plasma membrane becomes thicker, so materials can no longer pass through it at all.", "The thickness of the membrane does not increase as a cell grows. The limit is the ratio of surface area to volume.")],
          "The surface area-to-volume ratio restricts cell size.", difficulty="medium")

    cells = [("Cell A", 6.0, 8.0), ("Cell B", 24.0, 16.0), ("Cell C", 54.0, 27.0)]  # surface area, volume
    ratios = [sa_ / v_ for _, sa_, v_ in cells]
    assert ratios == [0.75, 1.5, 2.0]
    B.mcq(2, "The table shows the surface area and the volume of three cells. Which cell is best able to exchange materials with its environment, and why?",
          ch("Cell C, because it has the highest surface area-to-volume ratio of the three cells", "The ratios are 0.75 for cell A, 1.5 for cell B and 2.0 for cell C. A higher ratio allows more efficient exchange."),
          [ch("Cell A, because it has the lowest surface area-to-volume ratio of the three cells", "A lower ratio means less surface for each unit of volume, which makes exchange less efficient."),
           ch("Cell C, because it has the highest volume of the three cells and so holds the most materials", "A larger volume increases the demand for materials. What matters is the ratio of surface area to volume."),
           ch("Cell B, because it has a surface area that falls between the surface areas of the other two cells", "A value between the other two is not an advantage. The ratio of surface area to volume determines exchange.")],
          "A higher surface area-to-volume ratio allows more efficient exchange.",
          diagram=table(["Cell", "Surface area (µm²)", "Volume (µm³)"], [(n_, fix(s_), fix(v_)) for n_, s_, v_ in cells], caption="Three cells", row_headers=True), difficulty="hard")

    B.mcq(2, "Cells that line the small intestine have many tiny projections called microvilli on their surface. Which statement best explains how this feature helps the cells?",
          ch("The projections increase the surface area of the membrane without greatly increasing cell volume, which allows more absorption.", "Membrane folds and projections increase surface area, which improves the exchange of materials with the environment."),
          [ch("The projections decrease the surface area of the plasma membrane, which keeps the nutrients inside the cell for longer.", "Projections increase the surface area. They do not decrease it."),
           ch("The projections increase the volume of the cell without changing its surface area, which allows more nutrients to be stored.", "Microvilli increase the surface area. Their effect on the volume is small."),
           ch("The projections make the cell larger, which gives it a lower surface area-to-volume ratio and a faster rate of absorption.", "A lower ratio would make exchange less efficient. The projections raise the ratio.")],
          "More complex membrane structures, such as folds, allow more exchange with the environment.", difficulty="medium")

    B.mcq(2, "A shrew is a very small mammal and an elephant is a very large mammal. Which statement about the two animals is best supported by what is known about surface area-to-volume ratios?",
          ch("The shrew loses heat to the environment faster for each gram of body mass and has a higher metabolic rate per unit of body mass.", "Smaller organisms have a higher surface area-to-volume ratio, exchange more heat for their mass, and typically have a higher metabolic rate per unit of body mass."),
          [ch("The elephant loses heat to the environment faster for each gram of body mass and has a higher metabolic rate per unit of body mass.", "Larger organisms have a lower surface area-to-volume ratio, so they lose less heat for each gram of mass."),
           ch("The shrew and the elephant lose heat at the same rate for each gram of body mass, because both are mammals.", "Heat loss for each gram of body mass depends on the surface area-to-volume ratio, which differs with size."),
           ch("The shrew loses heat to the environment more slowly for each gram of body mass and has a lower metabolic rate per unit of body mass.", "The shrew's higher surface area-to-volume ratio makes it lose heat faster, not more slowly.")],
          "Smaller organisms have higher surface area-to-volume ratios and higher metabolic rates per unit of mass.", difficulty="hard")
