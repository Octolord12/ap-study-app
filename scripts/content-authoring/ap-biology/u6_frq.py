"""Unit 6: six free-response prompts, one of each kind.

  RESULTS        (9)  6.5  the lac operon: enzyme activity of a wild-type strain and two mutants with and without lactose
  RESULTS_GRAPH  (9)  6.8  bacterial transformation: colonies against the amount of plasmid DNA (replicate means and standard errors -> graph)
  INVESTIGATION  (4)  6.7  does ultraviolet light cause mutations that stop bacteria from making histidine?
  CONCEPT        (4)  6.4  a mutation that changes a codon into a stop codon in a gene for a 200 amino acid polypeptide
  MODEL          (4)  6.3  a table that labels the parts of a model of transcription and RNA processing
  DATA           (4)  6.2  the density of the DNA of bacteria over four generations (the experiment of Meselson and Stahl; a bar graph)

Part structure follows the CED (see u3_frq.py). Every number is computed here from the raw data.
"""
from lib import *


def build(B):
    # ------------------------------------------------------------------ RESULTS (9): lac operon
    act = {"Wild type": (3, 150), "Strain 1": (145, 152), "Strain 2": (2, 3)}
    fold = act["Wild type"][1] / act["Wild type"][0]
    assert fold == 50
    rows = [(k, str(a), str(b)) for k, (a, b) in act.items()]
    B.frq(5, "RESULTS",
          "In E. coli, the genes that code for the enzymes that use lactose are part of the lac operon. In the wild-type strain, the genes are expressed at a low level when there is no lactose in the medium and at a high level when there is lactose. A student compared the wild-type strain with two mutant strains. Strain 1 has a mutation in the lac operon. Strain 2 has a mutation in the promoter of the lac operon. Each strain was grown in a medium without lactose and in a medium with lactose, and the activity of one of the enzymes that uses lactose was measured. The results are shown in the table.\n\n"
          "**(a)** **Describe** how the repressor of the lac operon controls the expression of the genes in a medium without lactose. (1 point)\n\n"
          "**(b)** (i) **Identify** the dependent variable in the investigation. (ii) **Identify** one variable that the student should keep the same for all of the cultures. (iii) **Describe** the effect of lactose on the enzyme activity in the wild-type strain. (3 points)\n\n"
          "**(c)** (i) **Calculate** how many times greater the enzyme activity of the wild-type strain is with lactose than without lactose. (ii) **Use** the data to support the claim that the genes of the lac operon are expressed all of the time in Strain 1. (iii) **Identify** one location in the lac operon where a mutation could account for the results for Strain 1. (3 points)\n\n"
          "**(d)** **Predict** how the enzyme activity of Strain 2 would change if the concentration of lactose in the medium was increased a great deal, and **justify** your prediction. (2 points)",
          [(1, "(a) Describes that, without lactose, the repressor binds to the operator, which blocks RNA polymerase, so the genes are not transcribed (or are transcribed at a very low level)."),
           (1, "(b)(i) Identifies the dependent variable as the activity of the enzyme."),
           (1, "(b)(ii) Identifies a controlled variable, such as the temperature, the time of growth, the number of cells, the type of medium (other than lactose), or the method used to measure the enzyme."),
           (1, "(b)(iii) Describes that lactose increases the enzyme activity of the wild-type strain (from 3 to 150)."),
           (1, "(c)(i) Calculates 150 / 3 = 50 times greater."),
           (1, "(c)(ii) Uses the data: Strain 1 has a high activity (145) without lactose and a high activity (152) with lactose, so its genes are expressed whether or not lactose is present."),
           (1, "(c)(iii) Identifies a possible location of the mutation: the operator (so that the repressor cannot bind) or the gene for the repressor (so that the repressor does not work)."),
           (1, "(d) Predicts that the activity of Strain 2 will not change (it will stay low)."),
           (1, "(d) Justifies the prediction: the mutation in the promoter prevents RNA polymerase from binding, so the genes cannot be transcribed whether or not the repressor has been released.")],
          "(a) Without lactose, the repressor protein binds to the operator. This blocks RNA polymerase, so the genes of the operon are not transcribed.\n\n"
          "(b) (i) The dependent variable is the activity of the enzyme. (ii) The temperature (or the time of growth, or the number of cells). (iii) Lactose increases the enzyme activity of the wild-type strain from 3 to 150.\n\n"
          "(c) (i) 150 / 3 = 50 times greater. (ii) Strain 1 has a high enzyme activity both without lactose (145) and with lactose (152), so its genes are expressed whether or not lactose is present. (iii) The mutation could be in the operator, so that the repressor cannot bind to it, or in the gene for the repressor, so that the repressor does not work.\n\n"
          "(d) The activity of Strain 2 would not change and would stay low. The mutation is in the promoter, so RNA polymerase cannot bind to it and start transcription, even if the repressor has been released by the lactose.",
          diagram=table(["Strain", "Enzyme activity without lactose", "Enzyme activity with lactose"], rows, caption="Activity of an enzyme that uses lactose (arbitrary units)", row_headers=True))

    # ------------------------------------------------------------------ RESULTS_GRAPH (9): transformation
    doses = ["0.05", "0.10", "0.20", "0.40"]
    raw = {"0.05": [22, 27, 25, 26], "0.10": [49, 53, 51, 55], "0.20": [98, 104, 101, 105], "0.40": [160, 171, 166, 163]}
    means = [mean(raw[d_]) for d_ in doses]
    ses = [se(raw[d_]) for d_ in doses]
    assert means == [25.0, 52.0, 102.0, 165.0], means
    assert [round(e_, 2) for e_ in ses] == [1.08, 1.29, 1.58, 2.35], ses  # the sample response quotes these
    inc = pct_change(means[1], means[3])
    assert round(inc) == 217, inc
    rows = [(d_, fix(m_, 0), fix(e_, 2)) for d_, m_, e_ in zip(doses, means, ses)]
    B.frq(8, "RESULTS_GRAPH",
          "Bacterial transformation introduces foreign DNA into bacteria. A student mixed E. coli that are sensitive to the antibiotic ampicillin with a plasmid that contains a gene for resistance to ampicillin. The student used four different amounts of plasmid DNA, with four plates for each amount. After the bacteria were treated so that they could take up the plasmid, they were spread on agar plates that contained ampicillin, and the colonies on each plate were counted after 24 hours. The means and the standard errors of the means are shown in the table.\n\n"
          "**(a)** **Describe** what happens to a bacterial cell in a bacterial transformation. (1 point)\n\n"
          "**(b)** **Construct** a graph of the data in the table. Because you are answering in writing, describe the graph you would draw: the type of graph, what is shown on each axis, with units, the scale of each axis, the values you would plot, and how you would show the standard errors. (4 points)\n\n"
          "**(c)** (i) **Calculate** the percent increase in the mean number of colonies between the plates that received 0.10 µg of plasmid DNA and the plates that received 0.40 µg. Give your answer to the nearest whole percent. (ii) **State** a null hypothesis for this investigation. (2 points)\n\n"
          "**(d)** The student also spreads bacteria that were treated with the plasmid on plates that do not contain ampicillin. **Predict** how the growth on these plates will compare with the growth on the plates with ampicillin, and **justify** your prediction. (2 points)",
          [(1, "(a) Describes that the cell takes up foreign DNA (the plasmid) from its surroundings, and that the cell can then express the genes on the plasmid, which changes its phenotype (for example, it becomes resistant to ampicillin)."),
           (1, "(b) Chooses an appropriate graph type: a bar graph (or a line graph) with the amount of plasmid DNA on the horizontal axis."),
           (1, "(b) Labels both axes with units: the amount of plasmid DNA (µg) on the horizontal axis and the mean number of colonies per plate on the vertical axis."),
           (1, "(b) Gives an appropriate scale: a vertical axis that starts at 0 and has equal intervals, extending to at least 170 so that all of the means fit."),
           (1, "(b) Plots the data accurately (25, 52, 102 and 165 colonies) and shows error bars of plus and minus one standard error for each point."),
           (1, "(c)(i) Calculates (165 - 52) / 52 x 100 = 217 percent increase."),
           (1, "(c)(ii) States a null hypothesis: the amount of plasmid DNA has no effect on the mean number of colonies (any differences are due to chance)."),
           (1, "(d) Predicts that there will be much more growth (a lawn of bacteria, or many more colonies) on the plates without ampicillin."),
           (1, "(d) Justifies: without ampicillin, the bacteria that did not take up the plasmid are not killed, so they also grow, but with ampicillin only the transformed bacteria (with the resistance gene) can grow.")],
          "(a) The bacterial cell takes up the foreign DNA, the plasmid, from the medium around it. The cell can then make the proteins that the genes of the plasmid code for, which changes its phenotype. Here the cell becomes resistant to ampicillin.\n\n"
          "(b) A bar graph. The horizontal axis is labeled \"Amount of plasmid DNA (µg)\" with bars at 0.05, 0.10, 0.20 and 0.40. The vertical axis is labeled \"Mean number of colonies per plate\" and is scaled from 0 to 200 in steps of 50. The bars are 25, 52, 102 and 165, each with an error bar of plus and minus one standard error (about 1.08, 1.29, 1.58 and 2.35 colonies, which are small).\n\n"
          "(c) (i) (165 - 52) / 52 x 100 = 217 percent. (ii) The amount of plasmid DNA has no effect on the mean number of colonies.\n\n"
          "(d) There will be much more growth on the plates without ampicillin, probably a lawn of bacteria. Without ampicillin, the bacteria that did not take up the plasmid are not killed, so they grow too. With ampicillin, only the transformed bacteria, which have the gene for resistance, can grow.",
          diagram=table(["Amount of plasmid DNA (µg)", "Mean number of colonies per plate (n = 4)", "Standard error"], rows, caption="Colonies of E. coli on plates that contain ampicillin", row_headers=True))

    # ------------------------------------------------------------------ INVESTIGATION (4): UV and histidine
    B.frq(7, "INVESTIGATION",
          "Ultraviolet (UV) light is radiation that can damage DNA. A student hypothesizes that exposure to UV light causes mutations in bacteria that stop them from making the amino acid histidine. The student exposes samples of a bacterium that can make its own histidine to UV light for 0, 30 or 60 seconds. The student then spreads each sample on two agar plates, one with histidine and one without histidine, and counts the colonies on each plate after 24 hours.\n\n"
          "**(a)** **Identify** the dependent variable in the investigation. (1 point)\n\n"
          "**(b)** **Identify** an appropriate negative control for the investigation. (1 point)\n\n"
          "**(c)** **Predict** how the number of colonies on the plates without histidine will compare with the number of colonies on the plates with histidine as the time of exposure to UV light increases. (1 point)\n\n"
          "**(d)** **Justify** your prediction. (1 point)",
          [(1, "(a) Identifies the dependent variable as the number of colonies on the plates (with and without histidine)."),
           (1, "(b) Identifies a negative control: the sample that is not exposed to UV light (0 seconds), which is plated on both kinds of agar."),
           (1, "(c) Predicts that, as the time of exposure increases, the number of colonies on the plates without histidine will fall further below the number of colonies on the plates with histidine (the plates with histidine will have similar numbers of colonies, or somewhat fewer)."),
           (1, "(d) Justifies: UV light damages DNA and causes random mutations; a mutation in a gene that is needed for the synthesis of histidine stops the cell from making it, so those cells grow only on the plates that contain histidine.")],
          "(a) The dependent variable is the number of colonies on the plates with and without histidine.\n\n"
          "(b) The sample that is exposed to UV light for 0 seconds, plated on agar with histidine and on agar without histidine.\n\n"
          "(c) As the exposure to UV light gets longer, the number of colonies on the plates without histidine will be lower and lower compared with the number of colonies on the plates with histidine.\n\n"
          "(d) UV light damages DNA and causes random mutations. Some of the mutations will be in the genes for the enzymes that make histidine, and the cells with such mutations cannot make it. They can grow only on the plates that contain histidine, so a longer exposure gives more of these cells.")

    # ------------------------------------------------------------------ CONCEPT (4): premature stop codon
    n_aa, stop_at = 200, 50
    made = stop_at - 1
    assert made == 49
    B.frq(4, "CONCEPT",
          f"A gene codes for a polypeptide that has {n_aa} amino acids. A point mutation in the gene changes the mRNA codon for amino acid {stop_at} into the stop codon UAG.\n\n"
          "**(a)** **Describe** the role of transfer RNA (tRNA) in translation. (1 point)\n\n"
          "**(b)** **Explain** why a point mutation that changes the third nucleotide of a codon often does not change the amino acid that the codon codes for. (1 point)\n\n"
          "**(c)** **Predict** the number of amino acids in the polypeptide that is made from the mutated gene. (1 point)\n\n"
          "**(d)** **Justify** your prediction. (1 point)",
          [(1, "(a) Describes that each tRNA binds a specific amino acid and has an anticodon that base pairs with a codon of the mRNA, so it brings the correct amino acid to the ribosome in the order that the mRNA specifies."),
           (1, "(b) Explains that the genetic code is redundant: many amino acids are encoded by more than one codon, so the new codon can code for the same amino acid (a silent mutation)."),
           (1, f"(c) Predicts that the polypeptide has {made} amino acids."),
           (1, f"(d) Justifies: translation ends when the ribosome reaches the stop codon, which does not code for an amino acid, so only the codons before it (amino acids 1 to {made}) are translated, and the polypeptide is released.")],
          "(a) Each tRNA carries a specific amino acid and has an anticodon that base pairs with a codon of the mRNA. In this way it brings the correct amino acid to the ribosome in the order that the mRNA specifies.\n\n"
          "(b) The genetic code is redundant, which means that many amino acids are coded for by more than one codon. A change in the third nucleotide often gives another codon for the same amino acid, so the protein does not change.\n\n"
          f"(c) The polypeptide has {made} amino acids.\n\n"
          f"(d) Translation stops when the ribosome reaches a stop codon. The stop codon does not code for an amino acid, so only the {made} codons before it are translated, and then the polypeptide is released from the ribosome.")

    # ------------------------------------------------------------------ MODEL (4): transcription and RNA processing
    model_rows = [("1", "The template strand of the DNA (3' to 5')"), ("2", "The enzyme that moves along the template strand and builds the RNA"),
                  ("3", "The RNA transcript, which has exons and introns"), ("4", "The mature mRNA, with a GTP cap at one end and a poly-A tail at the other end"),
                  ("5", "A ribosome in the cytoplasm that reads the mRNA")]
    B.frq(3, "MODEL",
          "The model represents the way in which genetic information flows from a gene to a protein in a eukaryotic cell. The table is the key to the model. In the model, the enzyme (2) moves along the template strand (1) and makes the transcript (3). The transcript is processed into the mature mRNA (4), which is read by the ribosome (5).\n\n"
          "**(a)** **Identify** the enzyme (2) in the model, and **describe** the direction in which it synthesizes the RNA. (1 point)\n\n"
          "**(b)** **Explain** how the cap and the tail on the mature mRNA (4) help the cell to make a protein. (1 point)\n\n"
          "**(c)** **Explain** how the processing of the transcript (3) could produce two different mature mRNAs from the same gene. (1 point)\n\n"
          "**(d)** **Describe** one limitation of the model for explaining how the amount of protein that a cell makes is controlled. (1 point)",
          [(1, "(a) Identifies the enzyme as RNA polymerase, and describes that it synthesizes the RNA in the 5' to 3' direction (by reading the template strand from 3' to 5')."),
           (1, "(b) Explains that the GTP cap helps the ribosome to recognize the mRNA, and the poly-A tail makes the mRNA more stable, so it lasts longer and can be translated more times."),
           (1, "(c) Explains that alternative splicing removes the introns and can keep different combinations of exons, so that different mature mRNAs (and different proteins) are made from the same gene."),
           (1, "(d) Describes a limitation: the model does not show the regulatory sequences or the transcription factors that control whether, and how often, the gene is transcribed (or the factors that control how long the mRNA lasts).")],
          "(a) The enzyme is RNA polymerase. It synthesizes the RNA in the 5' to 3' direction, while it reads the template strand in the 3' to 5' direction.\n\n"
          "(b) The GTP cap helps the ribosome to recognize the mRNA, and the poly-A tail makes the mRNA more stable, so the mRNA lasts longer and can be translated more times.\n\n"
          "(c) The introns are removed from the transcript, and the exons are spliced together. If different exons are kept or left out, the mature mRNAs are different, and so the proteins that are made from them are different.\n\n"
          "(d) The model does not show the regulatory sequences, such as the promoter and the enhancers, or the transcription factors that bind to them. These control whether the gene is transcribed and how often, so the model cannot explain how the amount of the protein is controlled.",
          diagram=table(["Label", "Part of the model"], model_rows, caption="Key to the model of the flow of information from a gene to a protein", row_headers=True))

    # ------------------------------------------------------------------ DATA (4): Meselson and Stahl
    gens = [0, 1, 2, 3]
    inter = [0, 100, 50, 25]
    assert inter[1:] == [100 / 2 ** (g - 1) for g in gens[1:]]  # the fraction of intermediate DNA halves each generation
    light = [0, 0, 50, 75]
    heavy = [100, 0, 0, 0]
    assert [i + l + h for i, l, h in zip(inter, light, heavy)] == [100, 100, 100, 100]
    g4_inter = 100 / 2 ** 3
    g4_light = 100 - g4_inter
    assert (g4_inter, g4_light) == (12.5, 87.5)
    chart = bars("Generation in the 14N medium", "DNA in the sample (%)", 100, ["0", "1", "2", "3"],
                 [{"values": heavy, "label": "Heavy (15N/15N)", "color": "red"}, {"values": inter, "label": "Intermediate (15N/14N)", "color": "green"}, {"values": light, "label": "Light (14N/14N)", "color": "blue"}],
                 alt="Bar graph of the percent of heavy, intermediate and light DNA. Generation 0: 100 heavy. Generation 1: 100 intermediate. Generation 2: 50 intermediate and 50 light. Generation 3: 25 intermediate and 75 light.")
    B.frq(2, "DATA",
          "Researchers grew bacteria for many generations in a medium that contained heavy nitrogen (15N), and then moved the bacteria to a medium that contained light nitrogen (14N). They separated the DNA of the bacteria by its density after each generation of growth in the new medium. The graph shows the percent of the DNA that was heavy (both strands with 15N), intermediate (one strand with 15N and one with 14N) or light (both strands with 14N).\n\n"
          "**(a)** **Describe** the change in the percent of the DNA that was of intermediate density from generation 1 to generation 3. (1 point)\n\n"
          "**(b)** **Predict** the percent of the DNA that will be light in generation 4 if the pattern continues. (1 point)\n\n"
          "**(c)** A student claims that DNA replication is conservative, which means that the original DNA stays together and an entirely new DNA molecule is made. **Evaluate** the claim using the data from generation 1. (1 point)\n\n"
          "**(d)** **Explain** how the data from generation 2 are consistent with semiconservative replication. (1 point)",
          [(1, "(a) Describes that the percent of intermediate DNA decreases from 100 percent in generation 1 to 50 percent in generation 2 and to 25 percent in generation 3 (it halves in each generation)."),
           (1, "(b) Predicts 87.5 percent light DNA in generation 4 (12.5 percent intermediate)."),
           (1, "(c) Evaluates the claim as not supported, using data: conservative replication predicts heavy DNA and light DNA, with no intermediate DNA, but all of the DNA in generation 1 was of intermediate density."),
           (1, "(d) Explains that, in semiconservative replication, each of the two heavy strands stays in a different molecule, paired with a new light strand, so half of the DNA is intermediate and the other half, made of two new light strands, is light.")],
          "(a) The percent of the DNA that is of intermediate density falls from 100 percent in generation 1 to 50 percent in generation 2 and to 25 percent in generation 3, so it is halved in each generation.\n\n"
          "(b) In generation 4, the intermediate DNA would be 12.5 percent, so the light DNA would be 100 - 12.5 = 87.5 percent.\n\n"
          "(c) The data do not support the claim. If replication were conservative, the DNA in generation 1 would be a mixture of heavy DNA (the original) and light DNA (the new copy). There would be no DNA of intermediate density. In fact all of the DNA in generation 1 was intermediate.\n\n"
          "(d) In semiconservative replication, each molecule of the DNA has one old strand and one new strand. In generation 2, the two original heavy strands are each in a different molecule, paired with a light strand, which gives 50 percent intermediate DNA. The other molecules have two new light strands, which gives 50 percent light DNA.",
          diagram=chart)
