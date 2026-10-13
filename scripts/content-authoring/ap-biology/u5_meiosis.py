"""Unit 5, topics 5.1 Meiosis (10 questions) and 5.2 Meiosis and Genetic Diversity (9).

Required content (CED 2025-26): 5.1.A meiosis forms haploid gametes in sexually reproducing diploid organisms; meiosis I (prophase I: homologous chromosomes pair, condense, synapsis, chiasmata may form;
metaphase I: homologous pairs align at the equator; anaphase I: homologs separate while sister chromatids stay attached; telophase I: two haploid cells) and meiosis II (sister chromatids separate;
four haploid cells, each with unduplicated chromatids); 5.1.B mitosis and meiosis both use a spindle but differ in the number of cells and their genetic content; 5.2.A correct separation of homologs
in meiosis I and sister chromatids in meiosis II gives haploid gametes with a mix of maternal and paternal chromosomes, incorrect separation (nondisjunction) gives gametes that are not haploid, crossing
over between non-sister chromatids in prophase I, random assortment and fertilization increase variation. Suggested skills: 1.B, 3.A. Excluded: details of sexual reproduction cycles of specific organisms.
"""
from lib import *


def build(B):
    # ------------------------------------------------------------------ 5.1 Meiosis
    B.mcq(1, "What is the result of meiosis in a diploid organism that reproduces sexually?",
          ch("Haploid gametes, each of which has one set of chromosomes", "Meiosis forms haploid gamete cells from diploid cells."),
          [ch("Diploid body cells, each of which has two sets of chromosomes", "Diploid body cells are made by mitosis, not by meiosis."),
           ch("Haploid body cells, each of which has one set of chromosomes", "Meiosis makes gametes. Body cells are not haploid in a diploid organism."),
           ch("Diploid gametes, each of which has two sets of chromosomes", "Gametes are haploid, so that fertilization restores the diploid number.")],
          "Meiosis forms haploid gametes in sexually reproducing diploid organisms.", difficulty="easy")

    B.mcq(1, "Which statement correctly compares the products of mitosis and meiosis in an animal?",
          ch("Mitosis makes two genetically identical diploid cells, and meiosis makes four genetically different haploid cells.", "Mitosis and meiosis differ in the number of cells produced and in the genetic content of the daughter cells."),
          [ch("Mitosis makes four genetically different haploid cells, and meiosis makes two genetically identical diploid cells.", "This reverses the products of the two processes."),
           ch("Mitosis and meiosis both make four genetically identical cells, and they differ only in the use of a spindle.", "Both processes use a spindle, and they differ in the number of cells and the genetic content."),
           ch("Mitosis makes two haploid cells, and meiosis makes two diploid cells, and both of them use a spindle.", "Mitosis makes diploid cells and meiosis makes haploid cells.")],
          "Mitosis and meiosis both use a spindle but differ in the number of cells produced and in their genetic content.", difficulty="easy")

    B.mcq(1, "Which of the following events occurs in prophase I of meiosis but not in prophase of mitosis?",
          ch("Homologous chromosomes pair up in synapsis, and chiasmata may form between them", "In prophase I the homologous chromosomes pair and condense, and chiasmata may form."),
          [ch("The sister chromatids condense and the mitotic spindle starts to form between the centrosomes", "This happens in prophase of mitosis and also in prophase I."),
           ch("The nuclear envelope breaks down and the centrosomes move to the opposite poles of the cell", "This happens in prophase of mitosis as well."),
           ch("The sister chromatids separate and are pulled to the opposite poles by the spindle fibers", "Sister chromatids separate in anaphase of mitosis and in anaphase II.")],
          "Synapsis of homologous chromosomes is a feature of prophase I.", difficulty="medium")

    B.mcq(1, "How does the arrangement of chromosomes at the equator of the cell in metaphase I of meiosis differ from the arrangement in metaphase of mitosis?",
          ch("In metaphase I the homologous pairs line up at the equator, but in mitosis individual chromosomes line up.", "Meiotic spindle fibers align homologous pairs along the equator in metaphase I."),
          [ch("In metaphase I the individual chromosomes line up at the equator, but in mitosis the homologous pairs line up.", "This reverses the arrangements."),
           ch("In metaphase I the chromosomes do not line up at the equator, but in mitosis they do line up there.", "Chromosomes line up at the equator in metaphase I."),
           ch("In metaphase I all of the sister chromatids line up in a single row, but in mitosis they scatter in the cell.", "In mitosis the chromosomes line up at the equator as well.")],
          "Homologous pairs align at the metaphase plate in metaphase I.", difficulty="medium")

    B.mcq(1, "What separates during anaphase I of meiosis?",
          ch("The homologous chromosomes, while the sister chromatids of each chromosome remain attached", "In anaphase I homologous chromosomes separate and are pulled toward the poles."),
          [ch("The sister chromatids of each chromosome, while the homologous chromosomes stay paired together", "Sister chromatids separate in anaphase II."),
           ch("The two daughter cells, while the chromosomes in each stay together in a pair", "The cells separate at cytokinesis after telophase."),
           ch("The nuclear envelope and the spindle, while the chromosomes stay at the equator of the cell", "The chromosomes move to the poles in anaphase I.")],
          "Homologs separate in anaphase I; sister chromatids separate in anaphase II.", difficulty="medium")

    B.mcq(1, "Which event distinguishes anaphase II from anaphase I?",
          ch("In anaphase II the sister chromatids are pulled apart toward opposite poles, as the centromeres separate.", "In anaphase II the centromeres separate, and the sister chromatids are pulled to opposite poles."),
          [ch("In anaphase II the homologous chromosomes are pulled apart toward opposite poles, as the pairs break down.", "Homologous chromosomes separate in anaphase I."),
           ch("In anaphase II the chromosomes line up in pairs on the equator, as the chiasmata hold them together.", "This describes metaphase I."),
           ch("In anaphase II the DNA is replicated again, as the sister chromatids are pulled apart toward the poles.", "DNA is not replicated between meiosis I and meiosis II.")],
          "Sister chromatids separate in anaphase II.", difficulty="medium")

    n = 4  # haploid number of a diploid cell with 2n = 8
    two_n = 2 * n
    assert (two_n, n, 2 * n) == (8, 4, 8)
    B.mcq(1, f"A diploid cell has {two_n} chromosomes (2n = {two_n}). How many chromosomes does each cell have at the end of meiosis I, and how many at the end of meiosis II?",
          ch(f"{n} chromosomes at the end of meiosis I, and {n} chromosomes at the end of meiosis II", "Meiosis I separates the homologous chromosomes, so each cell has the haploid number (4). Meiosis II separates sister chromatids, and each cell still has 4 chromosomes."),
          [ch(f"{two_n} chromosomes at the end of meiosis I, and {n} chromosomes at the end of meiosis II", "The number of chromosomes is halved in meiosis I, because the homologous chromosomes separate."),
           ch(f"{n} chromosomes at the end of meiosis I, and {n // 2} chromosomes at the end of meiosis II", "Meiosis II separates the sister chromatids. It does not halve the number of chromosomes again."),
           ch(f"{two_n} chromosomes at the end of meiosis I, and {two_n} chromosomes at the end of meiosis II", "The cells that result from meiosis are haploid and so they have 4 chromosomes.")],
          "Meiosis I halves the number of chromosomes; meiosis II separates sister chromatids and does not change the number.", difficulty="medium")

    B.mcq(1, "Which choice lists a similarity between mitosis and meiosis, and a difference between them?",
          ch("Both use a spindle apparatus to move chromosomes, but meiosis makes four cells and mitosis makes two.", "Mitosis and meiosis are similar in the use of a spindle and they differ in the number of cells and their genetic content."),
          [ch("Both start with the replication of DNA, but only mitosis makes cells that have different combinations of alleles.", "Meiosis makes cells that differ genetically. Mitosis makes identical cells."),
           ch("Both make daughter cells with half of the chromosomes, but only meiosis uses a spindle to move them.", "Mitosis does not make cells with half of the chromosomes, and both processes use a spindle."),
           ch("Both make two daughter cells, but only mitosis happens in the cells that form the gametes of an animal.", "Meiosis happens in the cells that form gametes, and it makes four cells.")],
          "Mitosis and meiosis both use a spindle; they differ in the number of cells and in their genetic content.", difficulty="medium")

    cmp_rows = [("Process 1", "1", "2", "Diploid", "Identical to the parent cell"), ("Process 2", "2", "4", "Haploid", "Different from each other and from the parent cell")]
    B.mcq(1, "The table compares two processes of cell division in a diploid organism. Which statement is best supported by the table?",
          ch("Process 2 is meiosis, because it has two divisions and makes four haploid cells that are genetically different from each other.", "Meiosis has two divisions and produces four genetically different haploid cells."),
          [ch("Process 1 is meiosis, because it has one division and makes two diploid cells that are identical to the parent cell.", "Process 1 matches mitosis, which makes two identical diploid cells."),
           ch("Process 2 is mitosis, because it makes four cells and so it is able to supply a larger number of cells for growth.", "Mitosis makes two cells. The four haploid cells indicate meiosis."),
           ch("Both processes are mitosis, because both of them have a diploid parent cell and make daughter cells with chromosomes.", "The two processes differ in the number of divisions and in the cells they make.")],
          "Meiosis has two divisions and makes four genetically different haploid cells.",
          diagram=table(["Process", "Number of divisions", "Cells produced", "Chromosome number of the cells", "Genetic content of the cells"], cmp_rows, caption="Two processes of cell division", row_headers=True), difficulty="hard")

    B.mcq(1, "At the end of meiosis I, each cell is haploid, although each of its chromosomes still consists of two sister chromatids. Which statement best explains why the cell is described as haploid?",
          ch("The homologous chromosomes have separated, so each cell has one chromosome (one set) from each homologous pair.", "The chromosome number is counted by the number of centromeres, and each cell now has only one chromosome of each homologous pair."),
          [ch("The sister chromatids have separated, so each cell has only one chromatid of each of its chromosomes.", "The sister chromatids separate in meiosis II, and they are still attached at the end of meiosis I."),
           ch("Each chromosome has been cut in half, so each cell has half of the DNA of every one of its chromosomes.", "Chromosomes are not cut in half in meiosis I. Each chromosome still consists of two sister chromatids."),
           ch("The cell has not replicated its DNA, so it has half of the chromosomes that were present in the parent cell.", "DNA was replicated before meiosis I, so the cell has duplicated chromosomes.")],
          "Ploidy is counted by chromosomes (centromeres), not by chromatids.", difficulty="hard")

    # ------------------------------------------------------------------ 5.2 Meiosis and genetic diversity
    B.mcq(2, "Which statement correctly describes crossing over?",
          ch("In prophase I, non-sister chromatids of homologous chromosomes exchange genetic material, which increases genetic diversity among the gametes.", "Crossing over (recombination) happens in prophase I and produces new combinations of alleles."),
          [ch("In prophase II, sister chromatids of the same chromosome exchange genetic material, which keeps the genetic content of the gametes the same.", "Crossing over occurs in prophase I and between non-sister chromatids."),
           ch("In metaphase I, the two homologous chromosomes fuse into one chromosome, which doubles the number of chromosomes in the gametes.", "Homologous chromosomes do not fuse. They exchange segments."),
           ch("In anaphase I, the chromosomes break and join at random, which makes the gametes diploid and genetically identical.", "Gametes are haploid and are not genetically identical.")],
          "Crossing over between non-sister chromatids increases genetic diversity.", difficulty="easy")

    n2 = 4
    combos = 2**n2
    assert combos == 16
    B.mcq(2, f"An organism has {2 * n2} chromosomes in its body cells (2n = {2 * n2}). Ignoring crossing over, how many different combinations of maternal and paternal chromosomes are possible in its gametes?",
          ch("16", "Each of the 4 homologous pairs can line up in 2 ways at metaphase I, so the number of combinations is 2⁴ = 16.", 16),
          [ch("8", "This is 2 x 4. Each pair of chromosomes assorts independently, so the number of combinations is 2 raised to the power of 4.", 8),
           ch("4", "This is the number of chromosomes in a gamete (the haploid number), not the number of possible combinations.", 4),
           ch("256", "This is 16 x 16, the number of ways in which a gamete from each of two such parents could combine at fertilization, not the number of kinds of gamete.", 256)],
          "With n homologous pairs, independent assortment gives 2ⁿ possible combinations in the gametes.", difficulty="medium")

    B.mcq(2, "Which of the following is a source of genetic variation among the offspring of sexually reproducing parents?",
          ch("Random assortment of homologous chromosomes during meiosis and random fertilization of the gametes", "Crossing over, random assortment and fertilization all increase genetic variation."),
          [ch("Replication of the DNA before meiosis, which makes identical copies of every chromosome in the parent cell", "Replication makes copies and does not by itself create new combinations."),
           ch("Division of the somatic cells of the parent by mitosis, which makes genetically identical cells in its body", "Mitosis makes genetically identical cells, so it does not add variation to the gametes."),
           ch("Production of the gametes of both parents at the same time, which makes the gametes have the same alleles", "Gametes differ in their alleles, which is a source of variation.")],
          "Crossing over, random assortment and fertilization increase genetic variation.", difficulty="medium")

    B.mcq(2, "Nondisjunction of one pair of homologous chromosomes occurs during meiosis I in a cell with 2n = 4. What are the chromosome numbers of the four gametes that result?",
          ch("Two gametes with 3 chromosomes and two gametes with 1 chromosome, because one pair moves to the same pole", "Both homologs of one pair move to the same pole, so two gametes have an extra chromosome (n + 1 = 3) and two lack one (n - 1 = 1)."),
          [ch("Four gametes with 2 chromosomes each, because nondisjunction does not change the number of chromosomes", "Nondisjunction changes the number of chromosomes in the gametes."),
           ch("Two gametes with 2 chromosomes, one gamete with 3 chromosomes and one gamete with 1 chromosome", "This pattern results from nondisjunction in meiosis II. In meiosis I all four gametes are abnormal."),
           ch("Two gametes with 4 chromosomes and two gametes with 0 chromosomes, because both pairs fail to separate", "Only one pair fails to separate, so two gametes have 3 chromosomes and two have 1.")],
          "Nondisjunction in meiosis I makes all four gametes abnormal: two with n + 1 and two with n - 1.", difficulty="medium")

    B.mcq(2, "Nondisjunction occurs for one chromosome during meiosis II. How many of the four gametes are expected to have the normal haploid number of chromosomes?",
          ch("Two, because only the cell in which the sister chromatids failed to separate makes two abnormal gametes", "Only one of the two meiosis II divisions goes wrong, so two gametes are normal, one is n + 1 and one is n - 1."),
          [ch("None, because the failure of one chromosome to separate affects all four of the gametes that are made", "This is what happens in nondisjunction in meiosis I."),
           ch("Four, because meiosis II does not separate the chromosomes and so an error cannot change the number", "Meiosis II separates sister chromatids, and an error can change the number."),
           ch("One, because nondisjunction affects three of the gametes and leaves a single gamete with the normal number", "Nondisjunction in one cell in meiosis II affects two gametes and leaves two normal.")],
          "Nondisjunction in meiosis II affects only the two gametes that come from one of the two cells.", difficulty="medium")

    B.mcq(2, "A chromosome from the father carries alleles A and B. The homologous chromosome from the mother carries alleles a and b. Which statement correctly describes how crossing over could change the gametes?",
          ch("A crossover between the two genes could produce a chromatid with alleles A and b, a combination that was not in either parent's chromosome.", "Crossing over exchanges segments between non-sister chromatids, which can make new combinations of alleles."),
          [ch("A crossover between the two genes could change the allele A into the allele a, so that it is the same as the maternal allele.", "Crossing over exchanges alleles between chromatids. It does not change one allele into another."),
           ch("A crossover between the two genes would make all of the gametes carry A and B, as in the chromosome of the father.", "Crossing over produces new combinations in some gametes. It does not make all gametes alike."),
           ch("A crossover between the two genes could take place only in the cells of the mother, because only her chromosomes have the b allele.", "Crossing over occurs in meiosis in both parents.")],
          "Crossing over can combine alleles from the two homologs on one chromatid.", difficulty="hard")

    B.mcq(2, "A person has trisomy 21 because they received two copies of chromosome 21 from one parent. Which statement best explains how this could have happened?",
          ch("Nondisjunction occurred during meiosis in the parent, so a gamete had two copies of chromosome 21 and fused with a normal gamete.", "Incorrect separation of homologous chromosomes or sister chromatids makes gametes that are not haploid."),
          [ch("Mitosis occurred twice in the zygote after fertilization, so the cells have two copies of chromosome 21 that came from the same parent.", "The extra chromosome comes from a gamete that was not haploid."),
           ch("Crossing over occurred in prophase I, so the gamete had received a second copy of chromosome 21 from the same parent.", "Crossing over exchanges segments and does not add whole chromosomes."),
           ch("Replication occurred twice in S phase, so the gamete had received four copies of every chromosome from the parent.", "Double replication would affect all of the chromosomes and not only chromosome 21.")],
          "Nondisjunction produces gametes that are no longer haploid.", difficulty="hard")

    B.mcq(2, "Meiosis I is sometimes called a reduction division. Which statement best explains this name?",
          ch("It reduces the number of chromosomes in each cell from diploid to haploid, because the homologous chromosomes separate.", "The separation of homologs in meiosis I reduces the chromosome number by half."),
          [ch("It reduces the amount of DNA in each chromosome by half, because the chromatids of each chromosome are separated.", "The chromatids of each chromosome separate in meiosis II."),
           ch("It reduces the number of cells from four to two, because the first division combines the cells that were made earlier.", "Meiosis I produces two cells from one. It does not combine cells."),
           ch("It reduces the genetic variation of the gametes, because the cells make identical copies of the chromosomes of the parent.", "Meiosis increases genetic variation. It does not reduce it.")],
          "Meiosis I reduces the chromosome number from diploid to haploid.", difficulty="medium")

    n_h = 23
    gam = 2 ** n_h
    zyg = gam * gam
    assert gam == 8_388_608 and zyg == 70_368_744_177_664
    B.mcq(2, f"Humans have {n_h} pairs of chromosomes. Ignoring crossing over, one person can make {gam:,} genetically different gametes. About how many genetically different zygotes could two unrelated people produce when a gamete from each of them fuses?",
          ch(f"About 70 trillion, because each of the {gam:,} kinds of gamete from one parent can combine with each kind from the other", f"Random fertilization multiplies the numbers: {gam:,} x {gam:,} = {zyg:,}, which is about 70 trillion.", zyg),
          [ch(f"About 17 million, because the {gam:,} kinds of gamete from one parent are added to the {gam:,} kinds from the other parent", f"{gam:,} + {gam:,} = {2 * gam:,}. The kinds of gamete combine with each other, so the numbers are multiplied and not added.", 2 * gam),
           ch(f"About 8.4 million, because the zygote has the same number of kinds of chromosome combinations as one of the gametes", f"Each parent supplies one of {gam:,} kinds of gamete, so the number of kinds of zygote is much greater than {gam:,}.", gam),
           ch(f"46, because a zygote has {2 * n_h} chromosomes and so there are {2 * n_h} different kinds of zygote", "The number of chromosomes in a zygote is not the number of combinations of chromosomes that are possible.", 2 * n_h)],
          "Random fertilization of genetically different gametes greatly increases the number of possible genotypes.", difficulty="hard")
