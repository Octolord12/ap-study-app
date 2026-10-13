"""Unit 1, topics 1.1 Structure of Water and Hydrogen Bonding (9 questions) and 1.2 Elements of Life (6).

Required content (CED 2025-26): 1.1.A water is polar (polar covalent O-H bonds), which gives hydrogen bonding between and within biological molecules; high
specific heat capacity (homeostatic body temperature); high heat of vaporization (evaporative cooling); hydrogen bonds between water molecules give cohesion,
adhesion and surface tension. 1.2.A carbon, hydrogen and oxygen are the most prevalent elements in carbohydrates, proteins, lipids and nucleic acids;
sulfur is used in proteins, phosphorus in phospholipids and nucleic acids, nitrogen in nucleic acids. Suggested skill 2.A: describe visual representations.
Drafted with every wrong choice about as long as the right one (see length_stats.py).
"""
from lib import *


def build(B):
    # ------------------------------------------------------------------ 1.1 Structure of water
    B.mcq(1, "Why is a water molecule described as polar?",
          ch("Oxygen pulls the shared electrons closer than hydrogen does, so oxygen is slightly negative and each hydrogen slightly positive.",
             "The O-H bonds are polar covalent bonds. Unequal sharing of the electrons gives the oxygen end a partial negative charge and the hydrogen ends partial positive charges."),
          [ch("Each hydrogen atom transfers its electron completely to oxygen, so the molecule has a full negative end and a full positive end.",
              "Electrons in water are shared, not transferred. The charges are partial, not full, and the bonds are covalent rather than ionic."),
           ch("The oxygen and hydrogen atoms share their electrons equally, so the charge is spread evenly over the whole of the molecule.",
              "Equal sharing would make the molecule nonpolar. In water, oxygen attracts the shared electrons more strongly."),
           ch("The two hydrogen atoms are bonded to each other, which moves all of the negative charge of the molecule to the other side.",
              "The hydrogen atoms in water are bonded to oxygen, not to each other. The polarity comes from the unequal sharing in those O-H bonds.")],
          "Water is polar because its polar covalent O-H bonds share electrons unequally.", difficulty="easy")

    B.mcq(1, "A water strider walks across the surface of a pond without sinking. Which property of water best explains this observation?",
          ch("Surface tension, which results from hydrogen bonds that hold the water molecules at the surface together.",
             "Hydrogen bonds between water molecules produce cohesion, and cohesion at the surface gives water a high surface tension."),
          [ch("High specific heat capacity, which keeps the water at a constant temperature while the insect walks on it.",
              "Specific heat capacity describes how much energy is needed to change the temperature of water. It does not explain why an insect can stay on the surface."),
           ch("High heat of vaporization, which stops the surface water from evaporating under the weight of the insect.",
              "Heat of vaporization is about the energy needed for water to evaporate. It does not support the insect's weight."),
           ch("Adhesion between the water and the legs of the insect, which pulls the legs down below the surface.",
              "Adhesion is attraction between water and other substances. The insect stays on top because of the cohesion of the water molecules, not because of adhesion.")],
          "Surface tension comes from cohesion: hydrogen bonds hold surface water molecules together.", difficulty="easy")

    B.mcq(1, "Water moves upward through very narrow tubes in a plant, against the pull of gravity. Which properties of water best explain this movement?",
          ch("Adhesion of water molecules to the walls of the tubes, and cohesion of water molecules to one another.",
             "Hydrogen bonds make water molecules stick to each other (cohesion) and to the polar walls of the tubes (adhesion), so water can be pulled up in a continuous column."),
          [ch("High specific heat capacity of water, together with the high heat of vaporization of water.",
              "These properties affect temperature and evaporation. They do not hold water in a continuous column against gravity."),
           ch("The nonpolar nature of water molecules, together with their attraction to the nonpolar walls of the tubes.",
              "Water molecules are polar, not nonpolar. The attraction to the walls is a result of this polarity."),
           ch("The covalent bonds between separate water molecules, together with the loss of heat as the water evaporates.",
              "Separate water molecules are attracted by hydrogen bonds, not by covalent bonds. Evaporation cools the plant but does not explain the column of water.")],
          "Cohesion and adhesion, both due to hydrogen bonding, allow water to move up narrow tubes.", difficulty="medium")

    B.mcq(1, "The temperature of a large lake changes much more slowly than the temperature of the air above it. Which property of water best explains this difference?",
          ch("Water has a high specific heat capacity, so it absorbs or releases a large amount of energy for each degree that its temperature changes.",
             "Energy absorbed by water goes into breaking hydrogen bonds as well as raising the temperature, so the temperature changes slowly."),
          [ch("Water has a low specific heat capacity, so it holds on to heat energy and does not release any of it into the air.",
              "A low specific heat capacity would make the temperature change quickly. Water has a high specific heat capacity."),
           ch("Water has a high surface tension, which traps heat energy beneath the surface of the lake and keeps it there.",
              "Surface tension is about the attraction between surface molecules. It does not control how fast the temperature changes."),
           ch("Water molecules are nonpolar, so they do not take up the energy that is carried to the lake by the sun's light.",
              "Water molecules are polar. Water absorbs energy and the temperature changes slowly because of its high specific heat capacity.")],
          "A high specific heat capacity helps water, and the organisms in it, to maintain a stable temperature.", difficulty="medium")

    B.mcq(1, "Sweating helps cool the body of a mammal on a hot day. Which property of water is most directly responsible for the cooling?",
          ch("High heat of vaporization, because the evaporation of sweat removes a large amount of heat energy from the surface of the body.",
             "Water needs a large input of energy to change from liquid to gas. When sweat evaporates, that energy comes from the body, which cools it."),
          [ch("High specific heat capacity, because the water in sweat absorbs heat energy without increasing the body's temperature at all.",
              "Specific heat capacity helps keep body temperature stable, but the cooling effect of sweating depends on evaporation."),
           ch("Cohesion, because the drops of sweat stick together and fall from the skin, carrying their heat energy away with them.",
              "Falling drops are not the main cooling effect. The cooling occurs when the water evaporates from the skin."),
           ch("Adhesion, because sweat sticks to the skin and traps the heat energy against the body so that it spreads evenly.",
              "Trapping heat against the body would warm it, not cool it. Cooling occurs when sweat evaporates.")],
          "Evaporative cooling depends on water's high heat of vaporization.", difficulty="medium")

    water_t0, water_t1, oil_t1 = 20.0, 28.0, 36.0
    assert (water_t1 - water_t0, oil_t1 - water_t0) == (8.0, 16.0)
    B.mcq(1, "A student heats 100 g of water and 100 g of vegetable oil under the same conditions for 5 minutes, using the same heat source for both, and measures the temperatures shown. Which conclusion is best supported by the data?",
          ch("Water has a higher specific heat capacity than the oil, because it absorbed the same amount of heat energy but its temperature rose by less.",
             "The water's temperature rose by 8.0 degrees and the oil's by 16.0 degrees for the same energy input, so more energy is needed to raise the temperature of water by one degree."),
          [ch("Water has a lower specific heat capacity than the oil, because the temperature of the water rose by less than that of the oil.",
              "This reverses the reasoning. A smaller rise in temperature for the same energy means a higher specific heat capacity."),
           ch("The oil has stronger hydrogen bonds than the water, because the temperature of the oil rose by more than that of the water.",
              "Hydrogen bonding is characteristic of water and is what lets water absorb energy before its temperature rises. The data do not show hydrogen bonds in the oil."),
           ch("Both liquids have the same specific heat capacity, because both were heated for the same amount of time with the same source.",
              "The same heating time gives the same energy input, but the temperature changes were different, so the specific heat capacities differ.")],
          "For the same energy input, a smaller temperature change means a higher specific heat capacity.",
          diagram=table(["Liquid (100 g)", "Starting temperature (°C)", "Temperature after 5 min (°C)"], [("Water", fix(water_t0), fix(water_t1)), ("Vegetable oil", fix(water_t0), fix(oil_t1))], caption="Heating water and oil", row_headers=True), difficulty="medium")

    cap = [("0.5", 30), ("1.0", 15), ("1.5", 10), ("3.0", 5)]
    assert all(abs(d * h - 15) < 1e-9 for (d, h) in [(float(a), b) for a, b in cap])
    B.mcq(1, "A student places the lower end of each of four narrow glass tubes in a dish of water and measures how high the water rises in each tube. The table shows the results. Which conclusion is best supported by the data?",
          ch("Water rises higher in narrower tubes, which is consistent with water molecules adhering to the walls of the tube and cohering to one another.",
             "Adhesion to the glass pulls water up the wall, and cohesion pulls the neighboring water molecules after it. In a narrower tube there is more wall for the volume of water, so the water rises higher."),
          [ch("Water rises higher in wider tubes, because a greater volume of water is able to adhere to the glass of the tube walls.",
              "The data show the opposite: the narrowest tube had the highest rise, 30 mm, and the widest tube had the lowest, 5 mm."),
           ch("The diameter of the tube has no effect on the height of the water, because the same water was used in every tube.",
              "The heights differ from 5 mm to 30 mm, so the diameter of the tube does affect the rise in the water."),
           ch("Water rises in the tubes because of its high specific heat capacity, which also makes the narrow tubes warmer than the wide tubes.",
              "Specific heat capacity describes how water absorbs heat energy. The data do not involve temperature, and they are explained by adhesion and cohesion.")],
          "Capillary action, in which water rises in a narrow tube, depends on adhesion and cohesion, both of which result from hydrogen bonding.",
          diagram=table(["Inside diameter of tube (mm)", "Height of water in tube (mm)"], [(d_, h_) for d_, h_ in cap], caption="Water rising in narrow glass tubes"), difficulty="hard")

    B.mcq(1, "Which statement correctly describes the hydrogen bonds between water molecules?",
          ch("Each one is a weak attraction between a slightly positive hydrogen of one molecule and a slightly negative oxygen of another.",
             "Hydrogen bonds form because of the polarity of water. Each is weak, but many of them together give water its unusual properties."),
          [ch("Each one is a strong covalent bond that forms when two water molecules share a pair of electrons with each other.",
              "Hydrogen bonds are weak attractions, not covalent bonds. The covalent bonds in water are the O-H bonds inside each molecule."),
           ch("Each one is an attraction between the two hydrogen atoms that are part of the same water molecule.",
              "Hydrogen bonds form between different water molecules, between a hydrogen of one and an oxygen of another."),
           ch("Each one is an ionic bond that forms when one water molecule gains an electron from a neighboring molecule.",
              "No electrons are transferred between water molecules. The attraction is between partial charges.")],
          "Hydrogen bonds are weak attractions between the partial charges of polar molecules such as water.", difficulty="easy")

    B.mcq(1, "A scientist proposes a hypothetical liquid whose molecules are nonpolar and cannot form hydrogen bonds. If this liquid replaced the water in cells, which prediction is best supported by what is known about water?",
          ch("The liquid would show weaker cohesion and a lower specific heat capacity than water, so it would resist temperature changes less well.",
             "Cohesion and a high specific heat capacity both result from hydrogen bonding between polar water molecules. Without hydrogen bonds, both would be lower."),
          [ch("The liquid would show a stronger surface tension and a higher heat of vaporization than water, because its molecules would be more stable.",
              "Surface tension and heat of vaporization depend on hydrogen bonds. A liquid that cannot form them would be lower in both."),
           ch("The liquid would behave in the same way as water, because the properties of water result only from the small size of its molecules.",
              "Water's properties depend on its polarity and hydrogen bonding, not on its size alone."),
           ch("The liquid would have a higher specific heat capacity than water, because nonpolar molecules are able to store more energy.",
              "A high specific heat capacity depends on the energy absorbed by breaking hydrogen bonds. A liquid without them would have a lower value.")],
          "Polarity and hydrogen bonding explain water's cohesion, specific heat capacity and heat of vaporization.", difficulty="hard")

    # ------------------------------------------------------------------ 1.2 Elements of life
    B.mcq(2, "Which three elements are the most prevalent in carbohydrates, lipids, proteins and nucleic acids?",
          ch("Carbon, hydrogen and oxygen", "These three elements are the most prevalent in all of the major biological molecules."),
          [ch("Carbon, nitrogen and phosphorus", "Nitrogen and phosphorus are used in some of these molecules, but hydrogen and oxygen are more prevalent in all of them."),
           ch("Hydrogen, sulfur and phosphorus", "Sulfur and phosphorus are found only in some of these molecules, and carbon is the element that is in all of them."),
           ch("Oxygen, nitrogen and calcium", "Calcium is not a main component of these molecules, and carbon and hydrogen are more prevalent than nitrogen.")],
          "Carbon, hydrogen and oxygen make up most of the biological molecules.", difficulty="easy")

    B.mcq(2, "Which element is used in building both the phospholipids of membranes and nucleic acids?",
          ch("Phosphorus, which is found in the phosphate groups of these molecules.", "Phosphorus is used in phospholipids and in nucleic acids, where phosphate groups are part of the sugar-phosphate backbone."),
          [ch("Sulfur, which is found in the side chains of some of the amino acids.", "Sulfur is used in building proteins, not phospholipids or nucleic acids."),
           ch("Calcium, which is found as ions in the bones of many animals.", "Calcium is not one of the elements used to build phospholipids or nucleic acids."),
           ch("Iron, which is found in the oxygen-carrying proteins of the blood.", "Iron is a component of some proteins. It is not used to build phospholipids or nucleic acids.")],
          "Phosphorus is used in phospholipids and nucleic acids; sulfur is used in proteins.", difficulty="medium")

    B.mcq(2, "A culture of bacteria is grown in a medium that contains radioactive phosphorus (³²P) and radioactive sulfur (³⁵S). After several hours, which macromolecules are most likely to contain the radioactive atoms?",
          ch("³²P in nucleic acids, and ³⁵S in proteins", "Phosphorus is used in building nucleic acids, and sulfur is used in building proteins."),
          [ch("³²P in proteins, and ³⁵S in nucleic acids", "This swaps the elements. Sulfur is used in proteins and phosphorus in nucleic acids."),
           ch("³²P in carbohydrates, and ³⁵S in lipids", "Carbohydrates are made of carbon, hydrogen and oxygen. Neither phosphorus nor sulfur is used in building them."),
           ch("³²P and ³⁵S in carbohydrates, but neither in nucleic acids", "Carbohydrates do not contain these elements, and nucleic acids do contain phosphorus.")],
          "Phosphorus labels nucleic acids (and phospholipids), and sulfur labels proteins.", difficulty="hard")

    el_rows = [("Sample 1", "Yes", "Yes", "Yes", "No", "No", "No"), ("Sample 2", "Yes", "Yes", "Yes", "Yes", "No", "Yes"), ("Sample 3", "Yes", "Yes", "Yes", "Yes", "Yes", "No")]
    B.mcq(2, "A student analyzes three purified samples of macromolecules, each of which is a carbohydrate, a protein or a nucleic acid. The table shows which elements were detected. Which identification is most consistent with the data?",
          ch("Sample 1 is a carbohydrate, sample 2 is a protein, and sample 3 is a nucleic acid.", "Carbohydrates contain only carbon, hydrogen and oxygen. Proteins use sulfur, and nucleic acids use phosphorus (and nitrogen)."),
          [ch("Sample 1 is a protein, sample 2 is a nucleic acid, and sample 3 is a carbohydrate.", "Sample 1 contains only carbon, hydrogen and oxygen, which fits a carbohydrate, not a protein."),
           ch("Sample 1 is a nucleic acid, sample 2 is a carbohydrate, and sample 3 is a protein.", "Sample 1 lacks phosphorus, so it cannot be a nucleic acid, and sample 3 has phosphorus but no sulfur."),
           ch("Samples 2 and 3 are both proteins, and sample 1 is a nucleic acid.", "Only sample 2 contains sulfur, which is used in proteins, and sample 3 contains phosphorus.")],
          "The elements in a molecule indicate the type of macromolecule.",
          diagram=table(["Sample", "Carbon", "Hydrogen", "Oxygen", "Nitrogen", "Phosphorus", "Sulfur"], el_rows, caption="Elements detected in three samples", row_headers=True), difficulty="medium")

    B.mcq(2, "A strain of bacteria loses the ability to take up phosphorus from its environment. Which of the following processes would be most directly impaired in the bacteria?",
          ch("The making of DNA and RNA, and the building of the phospholipids of the cell membrane", "Phosphorus is used in phospholipids and in nucleic acids. Without it these molecules cannot be built."),
          [ch("The making of the glucose monomers of carbohydrates, which each contain a phosphorus atom", "Glucose is made of carbon, hydrogen and oxygen. It does not contain phosphorus."),
           ch("The making of proteins, because every amino acid in a protein contains a phosphorus atom", "Sulfur is used in some amino acids, but amino acids do not contain phosphorus."),
           ch("The making of cellulose for the cell wall, because cellulose is a polymer of phosphorus", "Cellulose is a carbohydrate made of glucose monomers and does not contain phosphorus.")],
          "Phosphorus is needed for nucleic acids and phospholipids.", difficulty="medium")

    B.mcq(2, "Which of the following molecules is made of only carbon, hydrogen and oxygen?",
          ch("A carbohydrate, such as starch", "Carbohydrates contain only carbon, hydrogen and oxygen."),
          [ch("A protein, such as an enzyme", "Proteins also contain nitrogen, and some contain sulfur."),
           ch("A nucleic acid, such as DNA", "Nucleic acids also contain nitrogen and phosphorus."),
           ch("A phospholipid, such as in a cell membrane", "Phospholipids also contain phosphorus.")],
          "Carbohydrates are made of carbon, hydrogen and oxygen only.", difficulty="easy")
