"""Unit 6, topics 6.1 DNA and RNA Structure (8 questions) and 6.2 DNA Replication (9).

Required content (CED 2025-26): 6.1.A genetic information is stored in DNA (and in some cases RNA); prokaryotes typically have circular chromosomes, eukaryotes multiple linear chromosomes condensed
with histones and associated proteins; plasmids are extra-chromosomal circular DNA in prokaryotes and eukaryotes; 6.1.B base pairing is specific and conserved: purines (A, G) have two rings,
pyrimidines (C, T, U) one; purines pair with pyrimidines (A with T or U, G with C). 6.2.A DNA is synthesized 5' to 3'; replication is semiconservative; helicase unwinds, topoisomerase relaxes
supercoiling ahead of the fork, DNA polymerase needs RNA primers, makes the leading strand continuously and the lagging strand discontinuously, ligase joins the lagging-strand fragments. Excluded: names of
other enzymes and steps. Suggested skills: 1.C, 2.B.
"""
from lib import *
from u6_common import reverse_complement, complement_dna


def build(B):
    # ------------------------------------------------------------------ 6.1 DNA and RNA structure
    T = 1
    B.mcq(T, "Which statement correctly compares the chromosomes of a typical prokaryotic cell with those of a typical eukaryotic cell?",
          ch("A prokaryote typically has a circular chromosome, and a eukaryote typically has several linear chromosomes that are condensed with histones and other proteins.", "Prokaryotes typically have a circular chromosome, and eukaryotes typically have multiple linear chromosomes that are condensed with histones and associated proteins."),
          [ch("A prokaryote typically has several linear chromosomes, and a eukaryote typically has a single circular chromosome that is packaged with histones.", "This reverses the typical chromosomes of the two kinds of cells."),
           ch("A prokaryote typically has a chromosome that is made of RNA, and a eukaryote typically has chromosomes that are made of DNA only.", "The chromosomes of both prokaryotes and eukaryotes are made of DNA."),
           ch("A prokaryote and a eukaryote typically both have a single circular chromosome, and both of them condense it with histones.", "Eukaryotic chromosomes are typically linear and are multiple, and prokaryotic chromosomes are typically circular.")],
          "Prokaryotes typically have circular chromosomes; eukaryotes typically have multiple linear chromosomes condensed with histones.", difficulty="easy")

    B.mcq(T, "Which of the following describes a plasmid?",
          ch("An extra-chromosomal, circular molecule of DNA that can be present in prokaryotes and in some eukaryotes", "Plasmids are extra-chromosomal circular molecules of DNA in prokaryotes and eukaryotes."),
          [ch("A linear chromosome made of DNA and histones that is found in the nucleus of every eukaryotic cell of an organism", "This describes a eukaryotic chromosome and not a plasmid."),
           ch("A small circular molecule of RNA that is found inside the ribosomes of bacteria and that is used to make proteins", "Plasmids are made of DNA and are not part of ribosomes."),
           ch("A protein that unwinds the main chromosome of a bacterium at the start of its replication and that is made by the cell", "A plasmid is a molecule of DNA and is not a protein.")],
          "Plasmids are extra-chromosomal circular DNA molecules.", difficulty="easy")

    B.mcq(T, "Which pair of nitrogenous bases are both purines, with a double ring structure?",
          ch("Adenine and guanine, which each have a double ring structure and which pair with pyrimidines", "Adenine and guanine are the purines."),
          [ch("Cytosine and uracil, which each have a double ring structure and which pair with other pyrimidines", "Cytosine and uracil are pyrimidines, and they have a single ring."),
           ch("Adenine and thymine, which each have a single ring structure and which pair with each other in DNA", "Adenine is a purine (double ring), and thymine is a pyrimidine (single ring)."),
           ch("Thymine and cytosine, which each have a double ring structure and which pair with the other purines", "Thymine and cytosine are pyrimidines with a single ring.")],
          "Purines (adenine and guanine) have a double ring structure; pyrimidines (cytosine, thymine and uracil) have a single ring.", difficulty="medium")

    a_pct = 20
    t_pct = a_pct
    g_pct = c_pct = (100 - a_pct - t_pct) // 2
    assert (t_pct, g_pct, c_pct) == (20, 30, 30) and a_pct + t_pct + g_pct + c_pct == 100
    B.mcq(T, f"In a sample of double-stranded DNA, {a_pct}% of the bases are adenine. What percent of the bases in the sample are cytosine?",
          ch(f"{c_pct}%, because adenine pairs with thymine ({t_pct}%), and the remaining {g_pct + c_pct}% is guanine and cytosine in equal amounts", "A = T = 20%, so G + C = 60%, and G = C = 30%.", c_pct),
          [ch(f"{a_pct}%, because cytosine is present in the same amount as adenine in a molecule of double-stranded DNA", "Cytosine pairs with guanine, so it is equal to guanine and not to adenine.", a_pct),
           ch(f"{100 - a_pct - t_pct}%, because the bases other than adenine and thymine are all cytosine in the double-stranded DNA", "The remaining 60% is shared by guanine and cytosine in equal amounts, which is 30% each.", 100 - a_pct - t_pct),
           ch(f"{100 - a_pct}%, because the bases other than adenine are all cytosine in the molecule of double-stranded DNA", "Thymine is also present in a double-stranded DNA and is equal to adenine.", 100 - a_pct)],
          "In double-stranded DNA, A = T and G = C.", difficulty="medium")

    B.mcq(T, "In a DNA double helix, a purine always pairs with a pyrimidine. Which statement best explains why this is important to the structure of DNA?",
          ch("A double-ring base paired with a single-ring base keeps the width of the double helix the same along its entire length.", "Pairing a purine with a pyrimidine gives a consistent width to the helix."),
          [ch("Two double-ring bases paired together would be too narrow to fit between the sugar-phosphate backbones of the DNA double helix.", "Two purines paired together would be too wide, not too narrow."),
           ch("A purine and a pyrimidine are joined by covalent bonds, which are stronger than the bonds that could join two purines together.", "Base pairs are held together by hydrogen bonds, which are weaker than covalent bonds."),
           ch("A purine and a pyrimidine are the only two bases that are found in both DNA and RNA, and so they have to pair with each other.", "Adenine, guanine and cytosine are found in both DNA and RNA.")],
          "Purines pair with pyrimidines, which gives the DNA double helix a constant width.", difficulty="medium")

    B.mcq(T, "During transcription, an RNA molecule is made from a DNA template strand. Which base in the RNA pairs with an adenine in the template strand?",
          ch("Uracil, because RNA has uracil in place of thymine and uracil pairs with adenine", "In RNA, adenine pairs with uracil."),
          [ch("Thymine, because thymine pairs with adenine in every kind of nucleic acid, including the RNA that is made in transcription", "Thymine is found in DNA. RNA has uracil in its place."),
           ch("Cytosine, because cytosine is a pyrimidine and so it can pair with adenine, which is a purine, in any nucleic acid", "Cytosine pairs with guanine."),
           ch("Adenine, because identical bases pair with each other when the RNA is made on the template strand of the DNA molecule", "Adenine is a purine and pairs with a pyrimidine. It does not pair with another purine.")],
          "In RNA, adenine pairs with uracil.", difficulty="easy")

    rows = [("Sample 1", "30", "30 (T)", "20", "20"), ("Sample 2", "23", "27 (U)", "31", "19"), ("Sample 3", "28", "22 (T)", "26", "24")]
    assert all(sum(int(c.split()[0]) for c in r[1:]) == 100 for r in rows)
    B.mcq(T, "The table shows the percent of each base in three samples of nucleic acid. Which sample is most likely to be double-stranded DNA?",
          ch("Sample 1, because it contains thymine and the amount of adenine equals the amount of thymine, and the amount of guanine equals the amount of cytosine", "Base pairing in double-stranded DNA requires A = T and G = C."),
          [ch("Sample 2, because it has a high percent of guanine, which makes the double helix more stable than the other samples would be", "Sample 2 contains uracil and not thymine, so it is RNA."),
           ch("Sample 3, because it contains thymine, and every nucleic acid that contains thymine has to be double-stranded DNA", "The amounts of adenine and thymine are not equal in Sample 3, so it is probably single-stranded DNA."),
           ch("All of the samples, because all three have base percents that add up to 100% and so all of them can form a double helix", "The base percents of every sample add up to 100%, but that does not show that the sample is double-stranded.")],
          "Double-stranded DNA contains thymine, with A = T and G = C.",
          diagram=table(["Sample", "Adenine (%)", "Thymine or uracil (%)", "Guanine (%)", "Cytosine (%)"], rows, caption="Base composition of three samples of nucleic acid", row_headers=True), difficulty="hard")

    strand = "ATGCCGAT"
    comp = reverse_complement(strand)
    assert comp == "ATCGGCAT" and complement_dna(strand) == "TACGGCTA"
    B.mcq(T, f"One strand of a DNA molecule has the sequence 5'-{strand}-3'. What is the sequence of the complementary strand?",
          ch(f"5'-{comp}-3', because the complementary strand is antiparallel and pairs A with T and G with C", "The strand that pairs with 5'-ATGCCGAT-3' is 3'-TACGGCTA-5', which is written 5'-ATCGGCAT-3'."),
          [ch(f"5'-{complement_dna(strand)}-3', because each base is replaced by its partner and the order stays the same as in the first strand", "This has the correct partners but the wrong direction. The complementary strand is antiparallel."),
           ch(f"5'-{strand}-3', because the two strands of a DNA double helix have the same sequence when they are read in the same direction", "The strands are complementary and they do not have the same sequence."),
           ch(f"5'-{complement_dna(strand).replace('T', 'U')}-3', because the complementary strand is made of RNA bases and has uracil", "DNA has thymine, and the complementary strand of a DNA molecule is DNA.")],
          "The two strands of DNA are complementary and antiparallel.", difficulty="medium")

    # ------------------------------------------------------------------ 6.2 DNA replication
    T = 2
    B.mcq(T, "DNA replication is described as semiconservative. What does this mean?",
          ch("Each new DNA molecule consists of one original strand and one newly synthesized strand.", "In semiconservative replication, one strand of DNA serves as the template for a new, complementary strand."),
          [ch("Each new DNA molecule consists of two newly synthesized strands, while the original molecule stays unchanged.", "This describes conservative replication, which does not happen."),
           ch("Each new DNA molecule consists of short pieces of the original DNA that are mixed with short pieces of new DNA.", "This describes dispersive replication, which does not happen."),
           ch("Each new DNA molecule consists of half of the original chromosome, and the other half of the chromosome is lost.", "The whole genome is copied in replication.")],
          "In semiconservative replication, each new DNA molecule has one old strand and one new strand.", difficulty="easy")

    B.mcq(T, "In which direction does DNA polymerase add nucleotides to a growing strand of DNA?",
          ch("It adds nucleotides to the 3' end of the new strand, so the new strand is synthesized in the 5' to 3' direction.", "DNA is synthesized in the 5' to 3' direction."),
          [ch("It adds nucleotides to the 5' end of the new strand, so the new strand is synthesized in the 3' to 5' direction.", "DNA polymerase cannot add nucleotides to the 5' end."),
           ch("It adds nucleotides to either end of the new strand, depending on which strand of the DNA is used as the template.", "DNA polymerase adds nucleotides only to the 3' end of the new strand."),
           ch("It adds nucleotides to the 3' end of the template strand, so the template strand becomes longer as replication goes on.", "The template strand is not extended. The new strand is made.")],
          "DNA polymerase synthesizes DNA in the 5' to 3' direction.", difficulty="easy")

    B.mcq(T, "A researcher uses a drug that inhibits helicase in dividing cells. Which result is most likely?",
          ch("The two strands of the parental DNA are not separated, so the replication fork cannot move forward and replication stops.", "Helicase unwinds the DNA strands at the replication fork."),
          [ch("The newly made strands are not joined together, so many short fragments of DNA collect on the lagging strand.", "The joining of fragments on the lagging strand is done by ligase."),
           ch("The DNA ahead of the replication fork becomes overly coiled, so the fork stalls because of the stress on the helix of the DNA.", "Relaxing the supercoiling ahead of the fork is done by topoisomerase."),
           ch("The RNA primers are not made, so DNA polymerase cannot start the synthesis of new strands of DNA on either strand.", "The primers are not made by helicase.")],
          "Helicase unwinds the DNA strands.", difficulty="medium")

    B.mcq(T, "As helicase unwinds the DNA at a replication fork, the DNA ahead of the fork becomes more tightly twisted. Which enzyme relaxes this supercoiling?",
          ch("Topoisomerase, which relaxes the supercoiling of the DNA in front of the replication fork", "Topoisomerase relaxes supercoiling in front of the replication fork."),
          [ch("Ligase, which relaxes the supercoiling by joining the strands of the DNA in front of the replication fork", "Ligase joins fragments on the lagging strand."),
           ch("DNA polymerase, which relaxes the supercoiling as it moves along the strand that is used as the template", "DNA polymerase synthesizes new strands."),
           ch("RNA polymerase, which relaxes the supercoiling by making the primers in front of the replication fork", "RNA polymerase makes RNA. Relaxing supercoiling is the function of topoisomerase.")],
          "Topoisomerase relaxes supercoiling in front of the replication fork.", difficulty="medium")

    B.mcq(T, "DNA polymerase cannot start a new strand of DNA on its own. Which statement explains how synthesis is started?",
          ch("An RNA primer is made that is paired with the template, and DNA polymerase adds nucleotides to the end of the primer.", "DNA polymerase requires RNA primers to initiate DNA synthesis."),
          [ch("A DNA primer is made by ligase on the template strand, and DNA polymerase then adds nucleotides to its 5' end.", "The primers are RNA, and DNA polymerase adds nucleotides to the 3' end of the primer."),
           ch("Helicase adds the first nucleotides to the template strand, and DNA polymerase then adds the other nucleotides to it.", "Helicase unwinds the DNA and does not synthesize nucleotides."),
           ch("The two parental strands pair with each other again, and DNA polymerase then adds nucleotides to this double helix.", "The new strand is made on a template strand and needs a primer.")],
          "DNA polymerase requires an RNA primer to start synthesis.", difficulty="medium")

    B.mcq(T, "At a replication fork, one new strand is made continuously and the other new strand is made in short pieces. Which statement best explains why one strand is made in short pieces?",
          ch("DNA polymerase adds nucleotides only in the 5' to 3' direction, so the strand that must grow away from the fork is made as a series of fragments.", "The lagging strand is synthesized discontinuously because DNA is synthesized only in the 5' to 3' direction."),
          [ch("Helicase can unwind only a few base pairs at a time, so the strand is made in short pieces that match the length of the unwound DNA.", "Helicase unwinds the DNA continuously, and the fragments are due to the direction of synthesis."),
           ch("Ligase cuts the new strand into short pieces after it has been made, so that the pieces can then be used as primers for other strands.", "Ligase joins fragments. It does not cut the new strand."),
           ch("One of the parental strands cannot be used as a template, so the new strand has to be copied from fragments of the other new strand.", "Both parental strands are used as templates in replication.")],
          "The lagging strand is made discontinuously because DNA polymerase synthesizes only in the 5' to 3' direction.", difficulty="medium")

    B.mcq(T, "A mutation in a cell prevents ligase from working. Which result is most likely during replication in this cell?",
          ch("The fragments on the lagging strand are not joined together, so the new lagging strand is in pieces and not continuous.", "Ligase joins the fragments on the lagging strand."),
          [ch("The leading strand is not made at all, because ligase is necessary to start the synthesis of this strand at the origin.", "The leading strand is made continuously by DNA polymerase and does not need ligase."),
           ch("The two parental strands cannot be separated, because ligase is the enzyme that breaks the hydrogen bonds between the bases.", "Helicase separates the parental strands."),
           ch("The RNA primers cannot be made, because ligase is the enzyme that adds nucleotides to the 3' end of the primer.", "Primers are made by an RNA polymerase, and DNA polymerase adds nucleotides to them.")],
          "Ligase joins the fragments on the lagging strand.", difficulty="medium")

    rows = [("0 (before the shift)", "100", "0", "0"), ("1", "0", "100", "0"), ("2", "0", "50", "50")]
    assert all(sum(int(x) for x in r[1:]) == 100 for r in rows)
    B.mcq(T, "Bacteria were grown for many generations in a medium that contained heavy nitrogen (15N) and were then moved to a medium that contained light nitrogen (14N). The table shows the DNA that was found after each generation of growth in the new medium. Which conclusion is best supported by the data?",
          ch("Replication is semiconservative, because the DNA after one generation is all of intermediate density, and a light DNA appears after two generations.", "One generation of all intermediate DNA rules out conservative replication, and the light DNA at generation 2 rules out dispersive replication."),
          [ch("Replication is conservative, because the DNA after one generation is of intermediate density, which means that it is a mixture of old and new DNA in each molecule.", "Conservative replication predicts heavy and light DNA after the first generation, with no intermediate DNA."),
           ch("Replication is dispersive, because the DNA after two generations contains some DNA that is of intermediate density.", "Dispersive replication predicts that all of the DNA stays intermediate, with no light DNA at generation 2."),
           ch("Replication cannot be described by any model, because the percent of the heavy DNA falls to zero after one generation.", "The data fit the semiconservative model.")],
          "The results of Meselson and Stahl showed that DNA replication is semiconservative.",
          diagram=table(["Generation in the 14N medium", "Heavy DNA (15N/15N) (%)", "Intermediate DNA (15N/14N) (%)", "Light DNA (14N/14N) (%)"], rows, caption="Density of the DNA of bacteria after growth in a 14N medium", row_headers=True), difficulty="hard")

    gens = 3
    total = 2 ** gens
    heavy_strands = 2
    assert (total, heavy_strands) == (8, 2)
    B.mcq(T, f"Both strands of a DNA molecule contain 15N. The molecule is replicated {gens} times in a medium that contains only 14N. How many of the resulting DNA molecules contain 15N in one of their strands?",
          ch(f"{heavy_strands}, because replication is semiconservative and the two original strands each end up in a different molecule of the {total} molecules", f"After {gens} rounds there are {total} molecules, and the 2 original strands are in 2 different molecules.", heavy_strands),
          [ch(f"{total}, because every new molecule of DNA contains an original strand that was made with 15N", f"Only two molecules contain an original strand. The other {total - heavy_strands} are made of new strands only.", total),
           ch(f"{total // 2}, because half of the DNA molecules contain an original strand after each round of replication", "The fraction of molecules with an original strand is halved in each round, and it is 2 of 8 after three rounds.", total // 2),
           ch(f"{heavy_strands // 2}, because the original molecule is the only molecule that contains 15N after the replication has taken place", "The two original strands are separated and each one ends up in a different molecule.", heavy_strands // 2)],
          "In semiconservative replication, the original strands are never destroyed; each one pairs with a new strand.", difficulty="hard")
