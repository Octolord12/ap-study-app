"""Unit 6, topics 6.7 Mutations (10 questions) and 6.8 Biotechnology (7).

Required content (CED 2025-26): 6.7.A point mutations (one nucleotide substituted), frameshift (insertions or deletions shift the reading frame), nonsense (premature stop), silent (no change in the amino acid
sequence); beneficial, detrimental or neutral depending on the environment; 6.7.B errors in replication or repair, radiation and reactive chemicals cause random mutations; mutations are a source of variation;
nondisjunction changes chromosome number (aneuploidy), structural changes lead to disorders; 6.7.C genotype changes that affect phenotype are subject to natural selection; horizontal transfer in prokaryotes by
transformation, transduction, conjugation and transposition; related viruses can recombine if they infect the same host cell. 6.8.A gel electrophoresis (size and charge), PCR (denature, anneal primers, extend),
bacterial transformation, DNA sequencing and DNA fingerprints. Excluded: specific mutations and disorders, the details of each technique. Suggested skills: 2.C, 6.D.
"""
from lib import *
from u6_common import amino, translate, codon_table, codons


def build(B):
    # ------------------------------------------------------------------ 6.7 Mutations
    T = 7
    B.mcq(T, "Which statement describes a point mutation?",
          ch("One nucleotide in the DNA is substituted for a different nucleotide.", "Point mutations occur when one nucleotide has been substituted for a different nucleotide."),
          [ch("One or more nucleotides are inserted into the DNA, which shifts the reading frame of the gene.", "This describes a frameshift mutation."),
           ch("A whole chromosome fails to separate from its homologous chromosome during the first division of meiosis.", "This describes nondisjunction, which changes the chromosome number."),
           ch("A short sequence of the DNA is copied into mRNA more often than the other sequences of the gene.", "This describes a change in transcription and is not a mutation.")],
          "A point mutation substitutes one nucleotide for another.", difficulty="easy")

    used = ["GAA", "GAG"]
    assert amino("GAA") == amino("GAG") == "Glu"
    B.mcq(T, "A point mutation in a gene changes one codon in the mRNA from GAA to GAG. Using the table, which type of mutation is this?",
          ch("A silent mutation, because the new codon codes for the same amino acid as the original codon", "GAA and GAG both code for glutamic acid, so the amino acid sequence is unchanged."),
          [ch("A nonsense mutation, because the new codon causes the translation of the mRNA to stop earlier than it did before", "Neither codon is a stop codon."),
           ch("A frameshift mutation, because a nucleotide was added to the sequence and so the reading frame is shifted", "A nucleotide was substituted. None was added, so the reading frame is not shifted."),
           ch("A mutation that changes the protein, because any change in a codon has to change the amino acid that it codes for", "The genetic code is redundant, so more than one codon can code for an amino acid.")],
          "A silent mutation changes the nucleotide sequence but not the amino acid sequence.",
          diagram=codon_table(used), difficulty="medium")

    used = ["UAC", "UAA"]
    assert (amino("UAC"), amino("UAA")) == ("Tyr", "Stop")
    B.mcq(T, "A mutation changes one codon near the middle of an mRNA from UAC to UAA. Using the table, which result is most likely?",
          ch("The polypeptide is shorter than normal, because the new codon is a stop codon that ends the translation early.", "UAA is a stop codon, so the mutation is a nonsense mutation and translation stops at that codon."),
          [ch("The polypeptide is longer than normal, because the new codon adds extra amino acids to the end of the chain.", "A stop codon ends translation. It does not add amino acids."),
           ch("The polypeptide is the same as normal, because the new codon codes for the same amino acid as the original codon.", "UAC codes for tyrosine, and UAA is a stop codon."),
           ch("The polypeptide has every amino acid after the mutation changed, because the reading frame is shifted by the mutation.", "A substitution does not shift the reading frame.")],
          "A nonsense mutation causes a premature stop.",
          diagram=codon_table(used), difficulty="medium")

    mrna = "AUGGAACCUUGGAAAUAA"
    orig = translate(mrna)
    mut = mrna[:3] + mrna[4:]
    after = translate(mut)
    assert orig == ["Met", "Glu", "Pro", "Trp", "Lys"] and after == ["Met", "Asn", "Leu", "Gly", "Asn"]
    skip = ["Met", "Pro", "Trp", "Lys"]
    used = ["AUG", "GAA", "CCU", "UGG", "AAA", "UAA", "AAC", "CUU", "GGA", "AAU"]
    assert [amino(c) for c in codons(mut)[:5]] == ["Met", "Asn", "Leu", "Gly", "Asn"]
    B.mcq(T, f"The mRNA 5'-{mrna}-3' codes for the polypeptide {'-'.join(orig)}. The fourth nucleotide of the mRNA (the first G of the codon GAA) is deleted. Using the table, which statement best describes the new polypeptide?",
          ch(f"It begins {'-'.join(after)}, because the deletion shifts the reading frame and changes every codon after the deletion", "A deletion of one nucleotide is a frameshift. The mRNA is read as AUG AAC CUU GGA AAU AA, so all the codons after the deletion are different."),
          [ch(f"It is {'-'.join(skip)}, because only the codon that lost a nucleotide is removed and the other codons are read as before", "The nucleotides are read in triplets, so the removal of one nucleotide changes the grouping of all of the following nucleotides."),
           ch(f"It is {'-'.join(orig)}, because the genetic code is redundant and so a deletion of one nucleotide does not change the protein", "Redundancy helps with some substitutions, but it does not help when the reading frame is shifted."),
           ch(f"It is Met-Asn-Pro-Trp-Lys, because only the codon that lost the nucleotide is changed and the rest of the mRNA is the same", "The following codons are changed too, because the frame is shifted.")],
          "Insertions or deletions of one or two nucleotides shift the reading frame.",
          diagram=codon_table(used), difficulty="hard")

    B.mcq(T, "A mutation in a bacterium makes the bacterium resistant to an antibiotic. Which statement best describes the effect of this mutation?",
          ch("It is beneficial in an environment that contains the antibiotic, and it may be neutral or harmful in an environment without it.", "Whether a mutation is beneficial, detrimental or neutral depends on the environmental context."),
          [ch("It is beneficial in every environment, because a mutation that gives resistance always increases the survival of the bacterium.", "The effect of a mutation depends on the environment."),
           ch("It is harmful in every environment, because any change to the DNA of a bacterium makes the cell less able to survive.", "Some mutations are beneficial, depending on the environment."),
           ch("It has no effect in any environment, because the mutation changes the DNA and does not change the proteins of the bacterium.", "A mutation can change the protein and the phenotype.")],
          "Whether a mutation is beneficial, detrimental or neutral depends on the environment.", difficulty="medium")

    B.mcq(T, "Which of the following can cause random mutations in DNA?",
          ch("Errors in DNA replication or DNA repair, and exposure to radiation, such as UV light, or to reactive chemicals", "Errors in replication or repair, radiation and reactive chemicals can all cause random mutations."),
          [ch("Transcription of the DNA by RNA polymerase and translation of the mRNA by the ribosomes of the cell", "Transcription and translation do not change the DNA sequence."),
           ch("Normal division of the cell by mitosis, which always changes the sequence of the DNA of the daughter cells", "Mitosis normally gives daughter cells with identical DNA."),
           ch("The needs of the organism, because mutations occur in the genes that an organism requires in its environment", "Mutations are random and do not occur because the organism needs them.")],
          "Mutations are random; they come from errors in replication or repair, and from radiation and reactive chemicals.", difficulty="medium")

    B.mcq(T, "Which process in prokaryotes is the transfer of DNA from one bacterial cell to another by a virus?",
          ch("Transduction, which is the viral transmission of genetic information between bacterial cells", "In transduction, a virus carries DNA from one cell to another."),
          [ch("Transformation, which is the uptake of DNA from the surroundings of the cell by a bacterial cell", "This is the uptake of DNA from the environment."),
           ch("Conjugation, which is the transfer of DNA through direct contact between two bacterial cells", "This is the cell-to-cell transfer of DNA, and no virus is involved."),
           ch("Transposition, which is the movement of segments of DNA within and between DNA molecules in the cell", "This is the movement of DNA segments, and it does not need a virus.")],
          "Horizontal gene transfer in prokaryotes includes transformation, transduction, conjugation and transposition.", difficulty="medium")

    B.mcq(T, "A change in chromosome number often results in a new phenotype. Which event is most likely to cause a change in the number of chromosomes in a gamete?",
          ch("Nondisjunction, in which homologous chromosomes or sister chromatids fail to separate correctly in meiosis", "Errors in meiosis such as nondisjunction change the number of chromosomes."),
          [ch("A point mutation in which one nucleotide of a gene is replaced by a different nucleotide in the DNA", "A point mutation changes a nucleotide and not the number of chromosomes."),
           ch("A silent mutation in which the sequence of the DNA changes but the amino acid sequence stays the same in the protein that is made", "A silent mutation does not change the number of chromosomes."),
           ch("A frameshift mutation in which the deletion of a nucleotide changes the codons of the mRNA of a gene", "A frameshift changes the reading frame and not the number of chromosomes.")],
          "Nondisjunction changes chromosome number (aneuploidy).", difficulty="medium")

    B.mcq(T, "Two related strains of a virus infect the same host cell at the same time. Which result is possible?",
          ch("The two strains recombine their genetic information, so new viruses with a combination of genes from both strains can be made.", "Related viruses can recombine genetic information if they infect the same host cell."),
          [ch("The two strains cannot be copied in the host cell, because a host cell can make only one strain of virus at a time.", "A host cell can make copies of both strains."),
           ch("The host cell divides by meiosis, so the viruses are shared between the haploid cells that are made.", "Viruses do not use meiosis, and the host cell is not changed in this way."),
           ch("The two strains become one species of bacteria, because the viral proteins combine with the proteins of the host.", "Viruses are not bacteria, and the strains do not change into a new kind of cell.")],
          "Related viruses can recombine genetic information if they infect the same host cell.", difficulty="hard")

    rows = [("0", "0.1"), ("1", "4.5"), ("2", "61"), ("3", "96")]
    B.mcq(T, "A population of bacteria is exposed to an antibiotic in each generation. The table shows the percent of the bacteria that are resistant. Which statement best explains the data?",
          ch("Some bacteria already had a mutation for resistance, and they survived and reproduced more than the others, so their frequency rose in the population.", "A mutation that enhances survival and reproduction can be selected for by environmental conditions."),
          [ch("The antibiotic caused each of the bacteria to make a mutation for resistance, so the percent of resistant bacteria increased.", "Mutations are random. The antibiotic selects for bacteria that already have a resistance mutation."),
           ch("The bacteria needed resistance in order to survive, so the cells changed their DNA to make themselves resistant.", "Mutations do not occur because they are needed."),
           ch("The percent of the resistant bacteria increased because the antibiotic made the non-resistant bacteria mutate into resistant ones.", "The antibiotic kills the non-resistant bacteria and does not turn them into resistant ones.")],
          "Natural selection increases the frequency of a mutation that enhances survival and reproduction in an environment.",
          diagram=table(["Generation", "Resistant bacteria (%)"], rows, caption="Bacteria that are resistant to an antibiotic", row_headers=True), difficulty="hard")

    # ------------------------------------------------------------------ 6.8 Biotechnology
    T = 8
    B.mcq(T, "A mixture of DNA fragments that are 500, 1,200, 2,000 and 3,000 base pairs long is loaded into a well of an agarose gel, and an electric current is applied. Which fragment travels the farthest from the well?",
          ch("The 500 base pair fragment, because smaller fragments move through the gel more easily than larger fragments", "Gel electrophoresis separates DNA fragments by size and charge, and smaller fragments travel farther."),
          [ch("The 3,000 base pair fragment, because larger fragments have more DNA and so they are pulled through the gel faster", "Larger fragments are slowed down more by the gel, so they move more slowly."),
           ch("All of the fragments travel the same distance, because the DNA of each fragment has the same negative charge", "Fragments of different sizes travel different distances in the gel."),
           ch("None of the fragments travel, because DNA is a large molecule that cannot move through a gel when a current is applied", "DNA has a negative charge and moves toward the positive electrode.")],
          "In gel electrophoresis, the smallest DNA fragments travel the farthest.", difficulty="easy")

    rows = [("Crime scene", "1,200", "850", "400"), ("Suspect A", "1,200", "850", "400"), ("Suspect B", "1,200", "900", "400"), ("Suspect C", "1,500", "850", "none")]
    B.mcq(T, "A sample of DNA from a crime scene and samples from three suspects were cut with the same enzyme and separated by gel electrophoresis. The table shows the sizes of the fragments. Which conclusion is best supported by the data?",
          ch("The DNA from Suspect A has the same fragments as the DNA from the crime scene, so it may have come from Suspect A, but this is not proof.", "The fragment pattern of Suspect A matches the pattern of the sample from the scene."),
          [ch("The DNA from Suspect B came from the crime scene, because it has fragments of two of the same sizes as the sample from the scene.", "Suspect B has a fragment of 900 base pairs, which is not in the sample from the scene, so the patterns do not match."),
           ch("The DNA from Suspect C came from the crime scene, because it has the 850 base pair fragment that is also in the sample.", "Suspect C has a different pattern, with a 1,500 base pair fragment and without the 400 base pair fragment."),
           ch("The DNA of the suspects is the same as the DNA of the sample, because all of the DNA is cut by the same enzyme.", "The same enzyme cuts different DNA into fragments of different sizes.")],
          "A DNA fingerprint compares the fragment patterns of different samples.",
          diagram=table(["Sample", "Fragment 1 (base pairs)", "Fragment 2 (base pairs)", "Fragment 3 (base pairs)"], rows, caption="Fragments of DNA from a crime scene and from three suspects", row_headers=True), difficulty="hard")

    B.mcq(T, "Polymerase chain reaction (PCR) is used to make many copies of a segment of DNA. Which list gives the three steps of each cycle of PCR in the correct order?",
          ch("Denaturing the DNA, annealing primers to the original strands, and extending the new DNA molecules", "In PCR, DNA is denatured, primers are annealed to the original strands, and the new DNA is extended."),
          [ch("Annealing primers to the DNA, denaturing the DNA, and extending the new DNA molecules", "The strands must be separated before primers can bind to them."),
           ch("Extending the new DNA molecules, annealing primers to the DNA, and denaturing the DNA to end the cycle", "Extension happens after primers are annealed."),
           ch("Denaturing the DNA, extending the new DNA molecules, and annealing primers to the finished strands", "Primers have to be annealed before the new DNA can be extended.")],
          "Each PCR cycle: denature, anneal primers, extend.", difficulty="medium")

    start, cycles = 3, 5
    copies = start * 2 ** cycles
    assert copies == 96
    B.mcq(T, f"A PCR reaction starts with {start} copies of a segment of DNA. Assuming that the number of copies doubles in each cycle, how many copies are there after {cycles} cycles?",
          ch(f"{copies}, because the number of copies doubles {cycles} times, which multiplies the starting number of copies by {2 ** cycles}", f"{start} x 2⁵ = {copies}.", copies),
          [ch(f"{start * cycles}, because the same number of copies is added in each cycle and so the number is multiplied by {cycles}", f"The number of copies doubles in each cycle. It does not increase by the same amount: {start} x 2⁵ = {copies}.", start * cycles),
           ch(f"{2 ** cycles}, because the number of copies doubles {cycles} times, and the starting number is not used in the calculation", f"The starting number of {start} copies is multiplied by {2 ** cycles}.", 2 ** cycles),
           ch(f"{start * 2 ** (cycles - 1)}, because the number of copies doubles only {cycles - 1} times, as the first cycle starts the reaction", f"The number doubles in each of the {cycles} cycles.", start * 2 ** (cycles - 1))],
          "In PCR the number of copies doubles with each cycle.", difficulty="medium")

    B.mcq(T, "A plasmid that has a gene for resistance to the antibiotic ampicillin is mixed with bacteria that are sensitive to ampicillin, and conditions are used that allow the bacteria to take up the plasmid. The bacteria are then spread onto a plate that contains ampicillin. Which result is expected?",
          ch("Only the bacteria that took up the plasmid grow into colonies, because only those bacteria have the gene for resistance to ampicillin.", "Bacterial transformation introduces foreign DNA, and the resistance gene allows the transformed bacteria to grow in the presence of the antibiotic."),
          [ch("All of the bacteria grow into colonies, because the plasmid that is added to the mixture also protects the cells that did not take it up.", "Cells that did not take up the plasmid do not have the resistance gene."),
           ch("None of the bacteria grow into colonies, because a gene for resistance to ampicillin cannot be expressed in a bacterial cell.", "The transformed bacteria express the gene and are able to grow."),
           ch("Only the bacteria that did not take up the plasmid grow into colonies, because the plasmid slows down the growth of bacteria.", "The bacteria without the plasmid are killed by the ampicillin.")],
          "Bacterial transformation introduces foreign DNA into bacterial cells; a resistance gene allows selection.", difficulty="medium")

    rows = [("A", "No plasmid", "No", "Lawn of bacteria"), ("B", "No plasmid", "Yes", "No colonies"), ("C", "Plasmid", "Yes", "148 colonies"), ("D", "Plasmid", "No", "Lawn of bacteria")]
    B.mcq(T, "A student performs a bacterial transformation with a plasmid that has an ampicillin resistance gene. The table shows the results on four plates. Which statement is best supported by the results?",
          ch("The colonies on plate C result from the plasmid, because bacteria without the plasmid did not grow on ampicillin on plate B.", "Plate B shows that the bacteria without the plasmid cannot grow with ampicillin, so growth on plate C requires the plasmid."),
          [ch("The colonies on plate C result from a mutation, because the same number of colonies is found on plate D as on plate C, which received the same amount of plasmid.", "Plate D has a lawn of bacteria, and it does not show the same number of colonies as plate C."),
           ch("The plasmid kills the bacteria on plate D, because a lawn of bacteria grew on plate A, which had no plasmid.", "Plate D has a lawn of bacteria. The plasmid does not kill them."),
           ch("The ampicillin has no effect on bacteria, because bacteria grew on plate C, which contained ampicillin.", "No bacteria grew on plate B, so ampicillin does kill bacteria that lack the plasmid.")],
          "A control without the plasmid shows that growth on ampicillin requires the plasmid.",
          diagram=table(["Plate", "Plasmid added", "Ampicillin in the agar", "Result"], rows, caption="Results of a bacterial transformation", row_headers=True), difficulty="hard")

    rows = [("Species 1", "99.8"), ("Species 2", "92.1"), ("Species 3", "85.0")]
    B.mcq(T, "A scientist amplifies a segment of DNA from an unknown fish by PCR and determines its sequence. The scientist compares the sequence with the sequences from three known species, as shown in the table. Which conclusion is best supported by the data?",
          ch("The unknown fish is most likely to be species 1, because its DNA sequence is the most similar (99.8%) to the sequence from species 1.", "DNA sequence comparison can be used to identify organisms. The highest similarity suggests the closest relationship."),
          [ch("The unknown fish is most likely to be species 3, because its DNA sequence is the least similar to the sequence from species 3.", "A low similarity indicates a more distant relationship."),
           ch("The unknown fish cannot be identified, because none of the sequences of the species is exactly the same as the sequence of the fish.", "A small difference does not prevent identification. The most similar sequence is the best match."),
           ch("The unknown fish is equally related to all three species, because the DNA of all of the species is made of the same four nucleotides.", "The order of the nucleotides is different in the species, and that is what is compared.")],
          "Amplified and sequenced DNA can be used to identify organisms and to perform phylogenetic analysis.",
          diagram=table(["Known species", "Similarity to the sequence of the unknown fish (%)"], rows, caption="Comparison of a DNA sequence from an unknown fish with known species", row_headers=True), difficulty="medium")
