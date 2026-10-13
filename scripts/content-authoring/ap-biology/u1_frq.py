"""Unit 1: six free-response prompts, one of each kind.

  RESULTS        (9)  1.2  radioactive phosphorus and sulfur in the nucleic acid and protein fractions of bacteria (table)
  RESULTS_GRAPH  (9)  1.1  surface tension: drops of four liquids on a penny (table of means and standard errors -> bar graph with error bars)
  INVESTIGATION  (4)  1.3  hydrolysis of sucrose by acid (variables, a control, a prediction)
  CONCEPT        (4)  1.7  a mutation that puts a polar amino acid in a protein's interior
  MODEL          (4)  1.6  a DNA double-strand segment (a table is the "figure")
  DATA           (4)  1.5  melting point against the number of double bonds in a fatty acid (graph)

Part structure follows the CED (see u3_frq.py). Every number is computed here from the raw data.
"""
from lib import *


def build(B):
    # ------------------------------------------------------------------ RESULTS (9): isotope labelling
    cpm = {"³²P": (9800, 400), "³⁵S": (300, 8600)}  # (nucleic acid fraction, protein fraction)
    p32_share = cpm["³²P"][0] / sum(cpm["³²P"]) * 100
    s35_ratio = cpm["³⁵S"][1] / cpm["³⁵S"][0]
    assert round(p32_share) == 96 and round(s35_ratio) == 29, (p32_share, s35_ratio)
    rows = [(k, f"{a:,}", f"{p:,}") for k, (a, p) in cpm.items()]
    B.frq(2, "RESULTS",
          "Researchers wanted to find out which macromolecules in bacteria are built using phosphorus and which are built using sulfur. One culture of bacteria was grown in a medium that contained radioactive phosphorus (³²P), and a second culture was grown in a medium that contained radioactive sulfur (³⁵S). After several generations, the cells of each culture were broken open and separated into a nucleic acid fraction and a protein fraction. The researchers measured the radioactivity of each fraction, in counts per minute (cpm), using the same amount of material for each measurement. The results are shown in the table.\n\n"
          "**(a)** **Describe** the role of phosphorus in the structure of a nucleic acid. (1 point)\n\n"
          "**(b)** (i) **Identify** the dependent variable in the investigation. (ii) **Identify** one variable that the researchers controlled (kept the same) for the two cultures. (iii) **Describe** the pattern in the data for the culture grown with ³²P. (3 points)\n\n"
          "**(c)** (i) **Calculate** the percent of the total ³²P radioactivity that was found in the nucleic acid fraction. Give your answer to the nearest whole percent. (ii) **Calculate** how many times greater the radioactivity of the protein fraction was than the radioactivity of the nucleic acid fraction in the culture grown with ³⁵S. Give your answer to the nearest whole number. (iii) **Use** the data to support the claim that sulfur is used to build proteins but not nucleic acids. (3 points)\n\n"
          "**(d)** The researchers also separated the membranes from the cells grown with ³²P. **Predict** whether radioactivity will be found in the membrane fraction, and **justify** your prediction. (2 points)",
          [(1, "(a) Describes that phosphorus is part of the phosphate group of each nucleotide, which forms the sugar-phosphate backbone that links the nucleotides."),
           (1, "(b)(i) Identifies the dependent variable as the radioactivity (in cpm) of each fraction."),
           (1, "(b)(ii) Identifies a controlled variable, such as the amount of cell material measured, the growth time or number of generations, the growth temperature, or the instrument used."),
           (1, "(b)(iii) Describes that in the ³²P culture most of the radioactivity was in the nucleic acid fraction (9,800 cpm) and very little was in the protein fraction (400 cpm)."),
           (1, "(c)(i) Calculates 9,800 / (9,800 + 400) x 100 = 96 percent."),
           (1, "(c)(ii) Calculates 8,600 / 300 = 29 (accept 28.7)."),
           (1, "(c)(iii) Uses the data: in the ³⁵S culture the protein fraction had much more radioactivity (8,600 cpm) than the nucleic acid fraction (300 cpm), so the sulfur was incorporated into proteins."),
           (1, "(d) Predicts that radioactivity will be found in the membrane fraction."),
           (1, "(d) Justifies the prediction: phosphorus is used to build phospholipids (in their phosphate groups), which form the lipid bilayer of the membranes.")],
          "(a) Phosphorus is part of the phosphate group of each nucleotide. The phosphate groups join the sugars of neighboring nucleotides, which forms the backbone of the nucleic acid.\n\n"
          "(b) (i) The dependent variable is the radioactivity of each fraction in counts per minute. (ii) The same amount of material was used for each measurement. (iii) In the culture grown with ³²P, the nucleic acid fraction had far more radioactivity (9,800 cpm) than the protein fraction (400 cpm).\n\n"
          "(c) (i) 9,800 / (9,800 + 400) x 100 = 96 percent. (ii) 8,600 / 300 = 29 times greater. (iii) In the ³⁵S culture almost all of the radioactivity was in the protein fraction (8,600 cpm) and very little was in the nucleic acid fraction (300 cpm), so sulfur was used to build proteins and not nucleic acids.\n\n"
          "(d) Radioactivity will be found in the membrane fraction. Phosphorus is used to build phospholipids, which form the lipid bilayer of the membranes, so the ³²P will be taken up into them.",
          diagram=table(["Radioactive element in the medium", "Nucleic acid fraction (cpm)", "Protein fraction (cpm)"], rows, caption="Radioactivity of two fractions of bacterial cells", row_headers=True))

    # ------------------------------------------------------------------ RESULTS_GRAPH (9): surface tension
    liquids = ["Water", "1 M salt solution", "Dish detergent solution", "Ethanol"]
    raw = {
        "Water": [31, 30, 32, 31, 31],
        "1 M salt solution": [33, 34, 32, 33, 33],
        "Dish detergent solution": [13, 15, 14, 14, 14],
        "Ethanol": [11, 12, 10, 11, 11],
    }
    means = [mean(raw[k]) for k in liquids]
    ses = [se(raw[k]) for k in liquids]
    assert means == [31.0, 33.0, 14.0, 11.0], means
    assert all(abs(e_ - 0.316) < 0.001 for e_ in ses), ses  # the sample response quotes this value
    pct_dec = (means[0] - means[2]) / means[0] * 100
    assert round(pct_dec) == 55, pct_dec
    rows = [(k, fix(m_), fix(e_, 2)) for k, m_, e_ in zip(liquids, means, ses)]
    B.frq(1, "RESULTS_GRAPH",
          "Hydrogen bonds between water molecules cause the molecules to stick together. A student investigated how different substances affect the surface tension of water. For each of four liquids, the student used a dropper to place drops of the liquid on a penny, one at a time, until the liquid spilled over the edge, and counted the drops. A liquid with a higher surface tension holds more drops. The student repeated the procedure for five trials of each liquid. The means and the standard errors of the means are shown in the table.\n\n"
          "**(a)** **Describe** how hydrogen bonds between water molecules cause water to have a high surface tension. (1 point)\n\n"
          "**(b)** **Construct** a graph of the data in the table. Because you are answering in writing, describe the graph you would draw: the type of graph, what is shown on each axis, with units, the scale of each axis, the values you would plot, and how you would show the standard errors. (4 points)\n\n"
          "**(c)** (i) **Calculate** the percent decrease in the mean number of drops from water to the dish detergent solution. Give your answer to the nearest whole percent. (ii) **State** a null hypothesis for this investigation. (2 points)\n\n"
          "**(d)** The student repeats the procedure with water that has been heated to 60 °C. **Predict** how the number of drops of the heated water will compare with the number for water at room temperature, and **justify** your prediction. (2 points)",
          [(1, "(a) Describes that the polar water molecules at the surface form hydrogen bonds with the molecules beside and below them, so they cohere strongly and form a surface that resists being broken."),
           (1, "(b) Chooses an appropriate graph type: a bar graph, because the independent variable (the liquid) is categorical."),
           (1, "(b) Labels both axes with units: the liquid on the horizontal axis and the mean number of drops on a penny on the vertical axis."),
           (1, "(b) Gives an appropriate scale: a vertical axis that starts at 0 and has equal intervals, extending to at least 35 so that all of the means fit."),
           (1, "(b) Plots the data accurately (bar heights close to 31, 33, 14 and 11 drops) and shows error bars of plus and minus one standard error for each bar."),
           (1, "(c)(i) Calculates (31 - 14) / 31 x 100 = 55 percent decrease."),
           (1, "(c)(ii) States a null hypothesis: the type of liquid has no effect on the number of drops that fit on the penny (any differences are due to chance)."),
           (1, "(d) Predicts that fewer drops of the heated water will fit on the penny than drops of the water at room temperature."),
           (1, "(d) Justifies the prediction: at a higher temperature the molecules move faster and more hydrogen bonds are broken, so the cohesion between the water molecules and the surface tension are lower.")],
          "(a) Water molecules are polar, so they form hydrogen bonds with one another. The molecules at the surface are held together by hydrogen bonds with the molecules next to them and beneath them, which gives the surface a high surface tension.\n\n"
          "(b) A bar graph, because the liquids are categories. The horizontal axis is labeled \"Liquid\" and has one bar for each of the four liquids. The vertical axis is labeled \"Mean number of drops on a penny\" and is scaled from 0 to 40 in steps of 10. The bars are about 31 (water), 33 (salt solution), 14 (detergent solution) and 11 (ethanol), each with an error bar of plus and minus one standard error (0.32 drops for every liquid, from the table).\n\n"
          "(c) (i) (31 - 14) / 31 x 100 = 55 percent decrease. (ii) The type of liquid has no effect on the number of drops that fit on the penny.\n\n"
          "(d) Fewer drops will fit. At 60 °C the water molecules move faster and more of the hydrogen bonds between them are broken, so the cohesion and the surface tension are lower.",
          diagram=table(["Liquid", "Mean number of drops on a penny (n = 5)", "Standard error"], rows, caption="Drops on a penny", row_headers=True))

    # ------------------------------------------------------------------ INVESTIGATION (4): hydrolysis of sucrose
    B.frq(3, "INVESTIGATION",
          "Sucrose is a disaccharide made of the monosaccharides glucose and fructose. A student wants to investigate whether an acid can break the bond between the monomers of sucrose. The student has a sucrose solution, a dilute hydrochloric acid solution, distilled water, a hot water bath, a solution to neutralize the acid, and test strips that detect glucose. The student plans to mix equal volumes of the sucrose solution with either the acid or water, heat the mixtures for 10 minutes, neutralize the acid, and test each mixture with a glucose test strip.\n\n"
          "**(a)** **Describe** what happens to the bond between the monomers in the hydrolysis of sucrose. (1 point)\n\n"
          "**(b)** **Identify** an appropriate negative control for the investigation. (1 point)\n\n"
          "**(c)** **Predict** the results of the glucose test for the mixture with acid and for the control. (1 point)\n\n"
          "**(d)** **Justify** your prediction. (1 point)",
          [(1, "(a) Describes that in hydrolysis a water molecule is added to the bond between the monomers, which breaks the covalent bond (the hydrogen is added to one monomer and the hydroxyl group to the other)."),
           (1, "(b) Identifies a negative control: sucrose solution mixed with distilled water instead of the acid, and treated in the same way (heated, neutralized and tested)."),
           (1, "(c) Predicts that the glucose test will be positive for the mixture with acid and negative for the control with water."),
           (1, "(d) Justifies: the acid catalyzes the hydrolysis of sucrose, which breaks it into glucose and fructose by adding water, so glucose is present only in the mixture with the acid.")],
          "(a) In hydrolysis a water molecule is added to the covalent bond between the glucose and the fructose. The hydrogen of the water goes to one monomer and the hydroxyl group goes to the other, and the bond is broken.\n\n"
          "(b) A mixture of the sucrose solution and distilled water, heated, neutralized and tested in the same way as the mixture with acid.\n\n"
          "(c) The glucose test will be positive for the mixture with the acid and negative for the control.\n\n"
          "(d) The acid speeds up the hydrolysis of sucrose, which splits it into glucose and fructose. Without the acid, little sucrose is broken down in 10 minutes, so there is no glucose to detect.")

    # ------------------------------------------------------------------ CONCEPT (4): protein mutation
    B.frq(7, "CONCEPT",
          "A protein found in the cytoplasm of human cells is made of one polypeptide of 250 amino acids. When the protein folds, nonpolar (hydrophobic) amino acids are found mostly in the interior of the protein, and polar (hydrophilic) amino acids are found mostly on its surface. A mutation changes the amino acid at position 87, which is in the interior of the folded protein, from a nonpolar amino acid to a polar one.\n\n"
          "**(a)** **Describe** how the sequence of amino acids in a polypeptide determines the three-dimensional shape of the protein. (1 point)\n\n"
          "**(b)** **Explain** how the interactions between the R groups of the amino acids produce the tertiary structure of a protein. (1 point)\n\n"
          "**(c)** **Predict** the effect of the mutation on the structure and the function of the protein. (1 point)\n\n"
          "**(d)** **Justify** your prediction. (1 point)",
          [(1, "(a) Describes that the sequence of amino acids (the primary structure) determines which R groups are present and where, so it determines how the chain folds into its secondary, tertiary and overall shape."),
           (1, "(b) Explains that interactions between R groups, such as hydrogen bonds, hydrophobic interactions, ionic interactions and disulfide bridges, fold the chain into its tertiary structure (for example, hydrophobic R groups cluster together in the interior)."),
           (1, "(c) Predicts that the mutation changes (disrupts) the folding or the stability of the protein, so the protein's function is reduced or lost."),
           (1, "(d) Justifies: a polar R group in the nonpolar interior cannot form the hydrophobic interactions that held the interior together, so the tertiary structure changes and the protein cannot function as before.")],
          "(a) The sequence of amino acids is the primary structure. Because each amino acid has its own R group, the sequence determines which R groups can interact and where, and so it determines how the chain folds into its final shape.\n\n"
          "(b) R groups interact by hydrogen bonds, hydrophobic interactions, ionic interactions and disulfide bridges. Hydrophobic R groups cluster together away from water in the interior, and these interactions fold the chain into the tertiary structure.\n\n"
          "(c) The mutation will disrupt the folding of the protein, so the protein will be less stable and will function poorly or not at all.\n\n"
          "(d) A polar amino acid in the interior cannot form hydrophobic interactions with the other nonpolar R groups there. Without those interactions the tertiary structure changes, and a protein with a changed shape cannot perform its function.")

    # ------------------------------------------------------------------ MODEL (4): DNA segment
    s1 = "ATGCCA"
    s2 = complement_ = "".join({"A": "T", "T": "A", "G": "C", "C": "G"}[b] for b in s1)
    assert s2 == "TACGGT"
    rna = "".join({"A": "U", "T": "A", "G": "C", "C": "G"}[b] for b in s1)
    assert rna == "UACGGU"
    model_rows = [("Strand 1 (5' to 3')",) + tuple(s1), ("Strand 2 (3' to 5')",) + tuple(s2)]
    B.frq(6, "MODEL",
          "The model represents a short segment of a DNA molecule. The table shows the nitrogenous bases at six positions in each of the two strands. Strand 1 is written from its 5' end to its 3' end, and strand 2 is written from its 3' end to its 5' end, directly beneath strand 1.\n\n"
          "**(a)** **Describe** the relationship between the directions of strand 1 and strand 2 shown in the model. (1 point)\n\n"
          "**(b)** **Explain** how the structure of DNA results in the base at position 4 of strand 2 being guanine (G). (1 point)\n\n"
          "**(c)** A molecule of RNA is made that pairs with strand 1 at these six positions. **Identify** the sequence of the bases of the RNA, from position 1 to position 6, and **identify** the base in RNA that takes the place of thymine. (1 point)\n\n"
          "**(d)** **Explain** how the structure of DNA allows it to store information. (1 point)",
          [(1, "(a) Describes that the strands are antiparallel: they run in opposite directions (strand 1 from its 5' end to its 3' end, strand 2 from its 3' end to its 5' end)."),
           (1, "(b) Explains that bases on the two strands pair by complementary base pairing, hydrogen bonds forming between cytosine (C) and guanine (G), and the base opposite the cytosine at position 4 of strand 1 is therefore guanine."),
           (1, "(c) Identifies the RNA bases as U A C G G U (from position 1 to 6) and identifies uracil (U) as the base that takes the place of thymine."),
           (1, "(d) Explains that information is encoded in the sequence of the nucleotides (the order of the bases), and that complementary base pairing allows the sequence to be copied accurately.")],
          "(a) The two strands are antiparallel. They run in opposite directions: strand 1 runs from 5' to 3' and strand 2 runs from 3' to 5'.\n\n"
          "(b) The bases of the two strands pair by complementary base pairing, held together by hydrogen bonds. At position 4, strand 1 has cytosine (C), and cytosine pairs with guanine (G), so strand 2 has G at that position.\n\n"
          "(c) The RNA bases are U, A, C, G, G, U. Uracil (U) takes the place of thymine, and it pairs with adenine.\n\n"
          "(d) The information in DNA is encoded in the sequence of the nucleotides, the order of the bases. Because each base pairs with only one other base, the sequence of one strand determines the sequence of the other, so the information can be copied accurately.",
          diagram=table(["Strand", "Position 1", "Position 2", "Position 3", "Position 4", "Position 5", "Position 6"], model_rows, caption="Bases in a segment of DNA", row_headers=True))

    # ------------------------------------------------------------------ DATA (4): melting points
    pts = [(0, 70), (1, 13), (2, -5), (3, -11)]
    g = graph("Number of double bonds in the fatty acid", "Melting point (°C)", 0, 4, -20, 100,
              [line("Fatty acids with 18 carbons", pts, "blue")],
              "Melting point against the number of double bonds for four fatty acids of 18 carbons: 70 degrees Celsius for no double bonds, 13 for one, minus 5 for two and minus 11 for three.")
    drop = pts[0][1] - pts[1][1]
    assert drop == 57
    B.frq(5, "DATA",
          "Fatty acids are components of many lipids. The graph shows the melting points of four fatty acids that each have a chain of 18 carbon atoms but different numbers of carbon-carbon double bonds.\n\n"
          "**(a)** **Describe** the relationship between the number of double bonds in these fatty acids and their melting points. (1 point)\n\n"
          "**(b)** **Describe** the difference between the melting point of the fatty acid with no double bonds and the melting point of the fatty acid with one double bond. (1 point)\n\n"
          "**(c)** A student claims that all of the fatty acids that have at least one double bond are liquids at the body temperature of 37 °C. **Evaluate** the claim using the data in the graph. (1 point)\n\n"
          "**(d)** **Explain** how the number of double bonds in a fatty acid is related to its melting point. (1 point)",
          [(1, "(a) Describes that as the number of double bonds increases, the melting point decreases (an inverse relationship)."),
           (1, "(b) Describes that the fatty acid with no double bonds melts at about 70 °C and the fatty acid with one double bond melts at about 13 °C, a decrease of about 57 °C."),
           (1, "(c) Evaluates the claim as supported, using data: the fatty acids with one, two and three double bonds all melt at 13 °C or below, which is lower than 37 °C, so they are liquids at 37 °C."),
           (1, "(d) Explains that double bonds put kinks in the fatty acid tails, so the molecules pack less closely and need less energy to separate, which lowers the melting point.")],
          "(a) As the number of double bonds increases, the melting point decreases.\n\n"
          "(b) The fatty acid with no double bonds melts at about 70 °C and the fatty acid with one double bond melts at about 13 °C, so its melting point is about 57 °C lower.\n\n"
          "(c) The data support the claim. The fatty acids with one, two and three double bonds have melting points of 13 °C, -5 °C and -11 °C, all of which are below 37 °C, so they are liquid at body temperature.\n\n"
          "(d) Each double bond puts a kink in the tail of the fatty acid. Kinked tails cannot pack closely together, so less energy is needed to separate the molecules, and the melting point is lower.",
          diagram=g)
