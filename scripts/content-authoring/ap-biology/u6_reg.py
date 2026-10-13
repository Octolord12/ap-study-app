"""Unit 6, topics 6.5 Regulation of Gene Expression (9 questions) and 6.6 Gene Expression and Cell Specialization (8).

Required content (CED 2025-26): 6.5.A regulatory sequences are stretches of DNA that interact with regulatory proteins to control transcription; some genes are constitutively expressed and others inducible;
epigenetic changes (reversible modifications of DNA or histones) affect expression; the phenotype depends on which genes are expressed and at what levels (differentiation from tissue-specific proteins; induction
of transcription factors gives sequential expression). 6.5.B groups of genes are coordinately regulated: prokaryotes use inducible or repressible operons, eukaryotes use shared transcription factors.
6.6.A RNA polymerase and transcription factors bind promoter or enhancer sequences, upstream or downstream of the start site; negative regulators bind DNA and block transcription. 6.6.B differential gene
expression gives different cell products and functions; small RNA molecules regulate expression. Suggested skills: 6.A, 6.B.
"""
from lib import *


def build(B):
    # ------------------------------------------------------------------ 6.5 Regulation of gene expression
    T = 5
    B.mcq(T, "Some genes are constitutively expressed and other genes are inducible. Which statement correctly describes the difference?",
          ch("A constitutive gene is expressed all of the time, and an inducible gene is expressed only when a signal or a condition turns it on.", "Constitutive genes are expressed continuously, and inducible genes are expressed in response to a condition."),
          [ch("A constitutive gene is expressed only in response to a signal, and an inducible gene is expressed all of the time in the cells of the organism.", "This reverses the two terms."),
           ch("A constitutive gene is found only in prokaryotes, and an inducible gene is found only in the cells of eukaryotes.", "Both kinds of regulation are found in prokaryotes and in eukaryotes."),
           ch("A constitutive gene has a mutation that stops it, and an inducible gene is a normal gene that works in all conditions.", "Constitutive expression is a normal feature of some genes and is not caused by a mutation.")],
          "Constitutive genes are always expressed; inducible genes are expressed in response to a signal.", difficulty="easy")

    B.mcq(T, "Which statement correctly describes regulatory sequences?",
          ch("They are stretches of DNA that interact with regulatory proteins to control the transcription of genes.", "Regulatory sequences are stretches of DNA that interact with regulatory proteins to control transcription."),
          [ch("They are stretches of mRNA that bind the ribosome to control the speed at which proteins are made in the cell.", "Regulatory sequences are DNA, and they control transcription."),
           ch("They are proteins that bind to the DNA polymerase to control the replication of the genes of the cell.", "Regulatory sequences are not proteins, and they control transcription and not replication."),
           ch("They are the codons of the genes that code for the amino acids of the regulatory proteins of the cell.", "Regulatory sequences do not code for amino acids. They bind regulatory proteins.")],
          "Regulatory sequences are DNA sequences that interact with regulatory proteins.", difficulty="medium")

    B.mcq(T, "In the lac operon of E. coli, there is no lactose in the environment of the bacteria. Which statement describes what happens?",
          ch("The repressor protein binds to the operator, and this blocks RNA polymerase, so the genes for the use of lactose are not transcribed.", "Without lactose, the active repressor binds the operator and prevents transcription."),
          [ch("The repressor protein is removed from the operator, and RNA polymerase transcribes the genes for the use of lactose.", "This happens when lactose is present."),
           ch("The repressor protein binds to the promoter, and this helps RNA polymerase to transcribe the genes for the use of lactose.", "The repressor blocks transcription."),
           ch("The repressor protein is not made, and RNA polymerase transcribes the genes for the use of lactose at a high rate.", "The repressor is made all of the time. It is active when lactose is absent.")],
          "In an inducible operon such as the lac operon, the repressor blocks transcription until the inducer is present.", difficulty="medium")

    B.mcq(T, "Lactose is added to the environment of E. coli cells that were grown without lactose. Which statement best describes how the lac operon is turned on?",
          ch("A molecule that is made from lactose binds to the repressor, the repressor can no longer bind to the operator, and the genes are transcribed.", "The inducer binds the repressor and changes its shape, so it is released from the operator and transcription takes place."),
          [ch("Lactose binds to RNA polymerase, the polymerase can then change into a repressor, and the genes are not transcribed.", "Lactose acts on the repressor and not on RNA polymerase."),
           ch("Lactose binds to the operator, the operator can no longer bind to the repressor, and the genes are not transcribed.", "The repressor binds to the operator, and the operator is a sequence of DNA."),
           ch("Lactose changes the sequence of the promoter, the promoter can then bind the repressor, and the genes are transcribed.", "Lactose does not change the DNA sequence.")],
          "In an inducible operon, the inducer inactivates the repressor so that the genes can be transcribed.", difficulty="medium")

    B.mcq(T, "The trp operon is a repressible operon. When tryptophan is abundant in the cell, tryptophan binds to the repressor. Which result is most likely?",
          ch("The repressor becomes active and binds to the operator, so the genes for making tryptophan are not transcribed.", "In a repressible operon, the end product activates the repressor, which turns off the synthesis of the product when it is not needed."),
          [ch("The repressor becomes inactive and leaves the operator, so the genes for making tryptophan are transcribed at a higher rate.", "This is the pattern of an inducible operon, and tryptophan makes the repressor active."),
           ch("The repressor is broken down by the cell, so the genes for making tryptophan are transcribed at a higher rate.", "Tryptophan does not cause the destruction of the repressor."),
           ch("The repressor binds to the tryptophan that is in the cell, so the amount of tryptophan in the cell is made lower.", "The tryptophan activates the repressor and is not removed by it.")],
          "In a repressible operon, the end product activates the repressor and turns off transcription.", difficulty="medium")

    rows = [("Wild type", "Low", "High"), ("Strain 1", "High", "High"), ("Strain 2", "Low", "Low"), ("Strain 3", "Low", "High")]
    B.mcq(T, "The table shows the activity of the enzyme that breaks down lactose in a wild-type strain of E. coli and in three mutant strains, grown with and without lactose. Strain 1 has a mutation in the lac operon. Which mutation is most consistent with the data for Strain 1?",
          ch("A mutation in the operator so that the repressor can no longer bind to it, which allows transcription to take place all of the time", "A repressor that cannot bind to the operator allows the genes to be transcribed whether or not lactose is present."),
          [ch("A mutation in the promoter so that RNA polymerase can no longer bind to it, which prevents transcription in all conditions", "This would give low activity, with or without lactose, as in Strain 2."),
           ch("A mutation in the gene for the enzyme so that the enzyme is made inactive, which lowers the activity of the enzyme in all conditions", "This would give low activity with and without lactose, not high activity."),
           ch("A mutation in the cell membrane so that lactose can no longer enter the cell, which lowers the activity of the enzyme with lactose", "This would give low activity with lactose and not high activity without it.")],
          "A mutation that stops the repressor from binding the operator makes the operon constitutive.",
          diagram=table(["Strain", "Enzyme activity without lactose", "Enzyme activity with lactose"], rows, caption="Activity of the enzyme that breaks down lactose", row_headers=True), difficulty="hard")

    B.mcq(T, "Epigenetic changes can affect gene expression. Which statement correctly describes an epigenetic change?",
          ch("A reversible modification of the DNA or of the histones changes how much a gene is expressed, without a change in the DNA sequence.", "Epigenetic changes affect gene expression through reversible modifications of DNA or histones."),
          [ch("A permanent change in the order of the bases of a gene changes the amino acid sequence of the protein that the gene codes for.", "This describes a mutation."),
           ch("A change in the number of chromosomes in a cell changes how much of each gene is expressed in the cells of the organism.", "This describes a change in the chromosome number, which is not an epigenetic change."),
           ch("A change in the sequence of the mRNA after it has been made changes the protein that is made and also the gene that was copied by the cell.", "Epigenetic changes affect the DNA or the histones and not the mRNA, and they do not change the gene.")],
          "Epigenetic changes are reversible modifications of DNA or histones that affect gene expression.", difficulty="medium")

    B.mcq(T, "In bacteria, the genes for the enzymes of one pathway are often next to each other and are controlled by a single operator. What is an advantage of this arrangement?",
          ch("The genes can be coordinately regulated, so all of the enzymes of the pathway are made together when they are needed.", "Groups of genes in prokaryotes are coordinately regulated in operons."),
          [ch("The genes can be transcribed from different promoters, so each enzyme is made at a different time from the others.", "A single operator controls the whole group, so the genes are made together."),
           ch("The genes can be translated by different kinds of ribosomes, so each enzyme is made at a different rate from the others.", "The arrangement of the genes on the DNA is related to transcription and not to the kind of ribosome."),
           ch("The genes can be spliced in different ways, so each gene can code for several versions of an enzyme in the pathway.", "Bacterial operons are not spliced in this way.")],
          "Operons allow groups of genes to be coordinately regulated.", difficulty="medium")

    gp = [(0, 2), (10, 2), (20, 45), (30, 90), (40, 100), (50, 62), (60, 26), (70, 10)]
    g = graph("Time (min)", "Activity of the enzyme that breaks down lactose (arbitrary units)", 0, 70, 0, 120,
              [line("Enzyme activity", gp, "green")],
              "Enzyme activity against time. It stays at 2 until 10 minutes, rises to 100 at 40 minutes, and then falls to 62 at 50 minutes, 26 at 60 minutes and 10 at 70 minutes.")
    B.mcq(T, "Lactose is added to a culture of E. coli at 10 minutes and is removed from the culture at 40 minutes. The graph shows the activity of the enzyme that breaks down lactose. Which conclusion is best supported by the data?",
          ch("The gene for the enzyme is inducible, because the activity increases when lactose is added and decreases after the lactose is removed.", "Expression of an inducible gene increases in the presence of the inducer and decreases when the inducer is removed."),
          [ch("The gene for the enzyme is constitutively expressed, because the activity of the enzyme is not zero at any time during the experiment.", "The activity is low at first and rises after lactose is added, which is a response to a signal and not constitutive expression."),
           ch("Lactose permanently changes the sequence of the gene, because the activity of the enzyme is higher after the lactose has been added.", "The activity decreases after the lactose is removed, so the change is reversible and is not a change in the DNA sequence."),
           ch("The enzyme is made only after the lactose has been removed, because the activity is highest at the time that the lactose is removed.", "The activity starts to rise soon after the lactose is added.")],
          "An inducible gene is turned on by a signal and turns off again when the signal is removed.", diagram=g, difficulty="hard")

    # ------------------------------------------------------------------ 6.6 Gene expression and cell specialization
    T = 6
    B.mcq(T, "A muscle cell and a nerve cell from the same person have different structures and functions. Which statement best explains this difference?",
          ch("The two cells have the same genes, but different genes are expressed in each cell, so the cells make different proteins.", "Gene regulation results in differential gene expression, which influences cell products and functions."),
          [ch("The two cells have different genes, because the cells lost the genes that they do not use when they became specialized.", "The cells of an organism have the same genes."),
           ch("The two cells have the same genes, and the same genes are expressed in each cell, so the difference is due to the environment.", "The cells express different sets of genes."),
           ch("The two cells have different numbers of chromosomes, because the nerve cell is formed by meiosis and the muscle cell by mitosis.", "Both kinds of cell are body cells that are formed by mitosis and have the same chromosomes.")],
          "Differential gene expression gives different cell types the same genes but different proteins.", difficulty="easy")

    B.mcq(T, "Which statement correctly describes how transcription is initiated in a eukaryotic cell?",
          ch("RNA polymerase and transcription factors bind to promoter or enhancer sequences of the DNA, which can be upstream or downstream of the start site.", "RNA polymerase and transcription factors bind promoter or enhancer DNA sequences to initiate transcription."),
          [ch("Transcription factors bind to the mRNA, and this allows RNA polymerase to copy the mRNA into a new strand of DNA.", "Transcription factors bind to DNA sequences, and transcription makes RNA from DNA."),
           ch("RNA polymerase binds to the ribosome, and transcription factors bring the amino acids to the site of transcription.", "RNA polymerase is not bound to the ribosome in transcription."),
           ch("Enhancer sequences can work only when they are next to the start site and on the upstream side of the promoter.", "Enhancers can be upstream or downstream of the transcription start site.")],
          "Transcription factors and RNA polymerase bind promoter and enhancer sequences.", difficulty="medium")

    B.mcq(T, "A negative regulatory molecule inhibits the expression of a gene. Which statement describes how this happens?",
          ch("It binds to the DNA of the gene and blocks transcription, so less mRNA is made from the gene.", "Negative regulatory molecules inhibit gene expression by binding to DNA and blocking transcription."),
          [ch("It binds to the ribosome and blocks translation, so the tRNAs cannot bring the amino acids to the mRNA.", "Negative regulators of transcription act on the DNA, not on the ribosome."),
           ch("It binds to the DNA polymerase and blocks replication, so the gene cannot be copied before the cell divides.", "The molecule controls transcription and not replication."),
           ch("It binds to the protein that the gene codes for and breaks it down, so the cell has less of the protein.", "A negative regulator of transcription acts before the protein is made.")],
          "Negative regulators bind DNA and block transcription.", difficulty="medium")

    B.mcq(T, "Certain small RNA molecules have roles in regulating gene expression. Which statement best describes one way in which a small RNA can reduce the expression of a gene?",
          ch("It base pairs with a complementary mRNA, so the mRNA is broken down or cannot be translated into protein.", "Small RNAs can pair with mRNA molecules and prevent their translation or cause their degradation."),
          [ch("It base pairs with the amino acids of the protein, so the protein cannot fold into its correct shape in the cell.", "RNA base pairs with nucleic acids and not with amino acids."),
           ch("It changes the sequence of the gene in the DNA, so the gene codes for a protein that does not work.", "Regulatory small RNAs do not change the DNA sequence."),
           ch("It adds a poly-A tail to the mRNA, so the mRNA is more stable and is translated more often.", "This would increase the expression of the gene and not reduce it.")],
          "Small RNAs regulate gene expression, for example by pairing with mRNA.", difficulty="medium")

    rows = [("Gene 1", "96", "1", "2"), ("Gene 2", "2", "94", "1"), ("Gene 3", "51", "49", "50")]
    B.mcq(T, "The table shows the relative amounts of the mRNA of three genes in three types of cell from the same organism. Which conclusion is best supported by the data?",
          ch("Gene 3 is expressed at similar levels in all three types of cell, but genes 1 and 2 are each expressed at high levels in only one type of cell.", "Gene 3 has similar amounts of mRNA in all three types, and genes 1 and 2 are expressed in a single type each."),
          [ch("Genes 1 and 2 are present only in one type of cell each, and so the other two types of cell have lost them.", "The cells of one organism have the same genes. The data show differences in expression and not in the presence of the genes."),
           ch("Gene 3 is not expressed in any of the three types of cell, because the amounts of mRNA are about the same in all of them.", "Gene 3 is expressed at a similar, substantial level in all three types."),
           ch("All three genes are expressed in the same way in all of the cells, because the three cell types came from the same organism.", "Genes 1 and 2 are expressed very differently in the three types of cell.")],
          "Cell types differ in which genes are expressed, even though they have the same genes.",
          diagram=table(["Gene", "Cell type A", "Cell type B", "Cell type C"], rows, caption="Relative amount of mRNA in three cell types", row_headers=True), difficulty="hard")

    B.mcq(T, "A transcription factor that is needed to turn on a muscle gene is not made in liver cells of the same person. Which prediction is most consistent with this?",
          ch("The muscle gene is present in the liver cells but is not transcribed, so the muscle protein is not made in them.", "Without the transcription factor, the gene is not expressed, though it is still present."),
          [ch("The muscle gene is absent from the DNA of the liver cells, because they have lost the genes that they do not use.", "Both kinds of cell have the same genes."),
           ch("The muscle gene is transcribed at a high rate in the liver cells, but the mRNA is not translated into protein.", "Without the transcription factor, the gene is not transcribed."),
           ch("The muscle gene is replicated more often in the liver cells, so that more copies of the gene are available for use.", "The lack of a transcription factor does not change how often the gene is replicated.")],
          "Transcription factors bind to regulatory sequences and are needed to turn on genes.", difficulty="medium")

    B.mcq(T, "During the development of an embryo, a transcription factor is made in a group of cells. This transcription factor turns on genes for other transcription factors, which turn on other genes. What does this process produce?",
          ch("Sequential gene expression, in which each set of genes that is turned on leads to the expression of the next set, as the tissues develop.", "Induction of transcription factors during development results in sequential gene expression."),
          [ch("Simultaneous expression of all genes in all cells, because each cell makes all of the transcription factors at the same time.", "The expression of genes is in a sequence, and different cells express different genes."),
           ch("Permanent loss of the genes that are not used, because the cells remove them from the DNA as the tissues develop.", "Cells do not lose the genes that they do not use."),
           ch("Replication of the DNA in each of the cells, because transcription factors are the enzymes that copy the DNA.", "Transcription factors regulate transcription and do not copy the DNA.")],
          "Induction of transcription factors during development results in sequential gene expression.", difficulty="medium")

    rows = [("1", "Promoter and enhancer, with the enhancer upstream of the promoter", "100"), ("2", "Promoter only (the enhancer is deleted)", "6"),
            ("3", "Enhancer only (the promoter is deleted)", "0"), ("4", "Promoter and enhancer, with the enhancer moved downstream of the gene", "94")]
    B.mcq(T, "Researchers made four versions of a gene and measured the amount of mRNA that each version produced in cells. Which conclusion is best supported by the data in the table?",
          ch("Both a promoter and an enhancer are needed for a high level of transcription, and the enhancer works from either side of the gene.", "Removing either sequence greatly reduces transcription, and the enhancer still works when it is moved downstream."),
          [ch("The enhancer alone is enough for a high level of transcription, because the enhancer increases transcription when it is present.", "With the promoter deleted, the amount of mRNA is zero."),
           ch("The promoter alone is enough for a high level of transcription, because RNA polymerase binds to the promoter.", "With the enhancer deleted, the amount of mRNA is very low."),
           ch("The enhancer works only when it is upstream of the promoter, because it is a part of the promoter of the gene that is transcribed.", "The enhancer still works when it is moved downstream of the gene.")],
          "Promoters and enhancers both regulate transcription; enhancers can be upstream or downstream of the start site.",
          diagram=table(["Version of the gene", "Description", "Relative amount of mRNA"], rows, caption="Effect of regulatory sequences on transcription", row_headers=True), difficulty="hard")
