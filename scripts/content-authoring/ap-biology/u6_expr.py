"""Unit 6, topics 6.3 Transcription and RNA Processing (9 questions) and 6.4 Translation (10).

Required content (CED 2025-26): 6.3.A mRNA carries information from the nucleus to the ribosome; tRNAs bind specific amino acids and have anticodons that pair with codons; rRNA is a building block of
ribosomes; RNA polymerase uses a single template strand and synthesizes mRNA 5' to 3' by reading the template 3' to 5'; in eukaryotes the transcript gets a GTP cap (ribosome recognition), a poly-A tail
(stability) and loses introns, with exons spliced (alternative splicing gives different mature mRNAs). 6.4.A translation on ribosomes in the cytoplasm and on the rough ER of prokaryotes and eukaryotes;
prokaryotic translation occurs during transcription; initiation at AUG (methionine), codons read in triplets, redundancy, an almost universal code (evidence for common ancestry), tRNA brings the amino acid,
termination at a stop codon; retroviruses use reverse transcriptase. Excluded: names of factors and steps, memorization of the code except AUG. Suggested skills: 2.B, 2.D, 6.E.
"""
from lib import *
from u6_common import amino, translate, transcribe, codon_table, codons


def build(B):
    # ------------------------------------------------------------------ 6.3 Transcription and RNA processing
    T = 3
    B.mcq(T, "Which statement correctly matches a type of RNA with its function?",
          ch("Transfer RNA binds one specific amino acid, and it has an anticodon that base pairs with a codon of the mRNA.", "tRNA molecules bind specific amino acids and have anticodons that pair with codons."),
          [ch("Messenger RNA is a functional building block of the ribosome, and it combines with proteins to form the subunits.", "Ribosomal RNA is the building block of ribosomes. mRNA carries information."),
           ch("Ribosomal RNA carries the information of a gene from the DNA in the nucleus to the ribosome in the cytoplasm.", "mRNA carries the information from the nucleus to the ribosome."),
           ch("Transfer RNA is the molecule that is used as the template for the synthesis of mRNA by RNA polymerase in the nucleus.", "A strand of DNA is the template for transcription.")],
          "mRNA carries information, tRNA brings amino acids, and rRNA is part of the ribosome.", difficulty="easy")

    B.mcq(T, "During transcription of a gene, which molecule is used by RNA polymerase as a template?",
          ch("A single strand of the DNA, which directs the order of the bases in the new RNA molecule", "RNA polymerase uses a single template strand of DNA to direct the inclusion of bases in the new RNA."),
          [ch("Both strands of the DNA at the same time, which each make a separate molecule of mRNA from the same gene", "RNA polymerase uses a single template strand of DNA."),
           ch("A molecule of mRNA, which is copied by RNA polymerase into a new strand of DNA in the nucleus of the cell", "Copying RNA into DNA is done only by reverse transcriptase in retroviruses."),
           ch("A molecule of tRNA, which brings the bases to the DNA so that RNA polymerase can add them to the new RNA", "tRNA carries amino acids in translation and is not the template for RNA polymerase.")],
          "RNA polymerase uses a single template strand of DNA.", difficulty="easy")

    B.mcq(T, "In which direction does RNA polymerase read the template strand of the DNA, and in which direction does it synthesize the mRNA?",
          ch("It reads the template in the 3' to 5' direction and synthesizes the mRNA in the 5' to 3' direction.", "RNA polymerase synthesizes mRNA in the 5' to 3' direction by reading the template DNA in the 3' to 5' direction."),
          [ch("It reads the template in the 5' to 3' direction and synthesizes the mRNA in the 3' to 5' direction.", "This reverses the directions."),
           ch("It reads the template in the 5' to 3' direction and synthesizes the mRNA in the 5' to 3' direction.", "The template is antiparallel to the new strand, so it is read 3' to 5'."),
           ch("It reads the template in the 3' to 5' direction and synthesizes the mRNA in the 3' to 5' direction.", "RNA, like DNA, is synthesized in the 5' to 3' direction.")],
          "RNA polymerase reads the template 3' to 5' and synthesizes RNA 5' to 3'.", difficulty="medium")

    tmpl = "TACGGATCCTGA"
    mrna = transcribe(tmpl)
    assert mrna == "AUGCCUAGGACU" and "UAG" not in [mrna[i:i + 3] for i in range(0, 12, 3)]
    B.mcq(T, f"The template strand of a gene is 3'-{tmpl}-5'. What is the sequence of the mRNA that is made from this template?",
          ch(f"5'-{mrna}-3', because the mRNA is complementary and antiparallel to the template, with uracil in place of thymine", "Each base of the template is paired with its partner: A with U, T with A, G with C and C with G, and the new strand is written 5' to 3'."),
          [ch(f"5'-{tmpl.replace('T', 'U')}-3', because the mRNA has the same sequence as the template strand, with uracil in place of thymine", "The mRNA is complementary to the template and does not have the same sequence."),
           ch(f"5'-{mrna.replace('U', 'T')}-3', because the mRNA is complementary to the template, as it is in DNA, and has thymine", "RNA has uracil in place of thymine."),
           ch(f"5'-{mrna[::-1]}-3', because the complementary bases are read from the 5' end of the template, which reverses their order", "The template is written 3' to 5', so the complementary bases are written in the same left to right order, and the mRNA is 5'-AUGCCUAGGACU-3'.")],
          "The mRNA is complementary and antiparallel to the template strand.", difficulty="medium")

    B.mcq(T, "Which statement correctly describes the processing of a eukaryotic mRNA transcript before it leaves the nucleus?",
          ch("A GTP cap is added, which helps with ribosomal recognition, and a poly-A tail is added, which makes the mRNA more stable.", "The cap helps ribosomes to recognize the mRNA, and the poly-A tail makes it more stable."),
          [ch("A poly-A tail is added, which helps with ribosomal recognition, and a GTP cap is added, which makes the mRNA more stable.", "This reverses the functions of the cap and the tail."),
           ch("The exons are removed and the introns are spliced together, which generates the mature mRNA that is translated.", "Introns are excised, and exons are retained and spliced."),
           ch("A second strand of RNA is added to the transcript, which makes the mRNA double-stranded and more stable.", "Processing does not make the mRNA double-stranded.")],
          "Eukaryotic mRNA gets a GTP cap, a poly-A tail, and splicing.", difficulty="medium")

    B.mcq(T, "Alternative splicing of a single pre-mRNA can produce several different mature mRNAs. Which statement best explains how this happens?",
          ch("Different combinations of exons are kept and the introns are removed, so that one gene can code for several versions of a protein.", "The excision of introns, with the splicing and retention of exons, generates different versions of the mature mRNA."),
          [ch("Different strands of the DNA are used as the template by RNA polymerase, so that one gene can code for several mRNAs.", "RNA polymerase uses a single template strand."),
           ch("Different introns are translated into proteins by the ribosome, so that one gene can code for several versions of a protein.", "Introns are removed and are not translated."),
           ch("Different numbers of the nucleotides are added to the poly-A tail, so that the codons of the mRNA are changed in each version of the mRNA.", "The poly-A tail does not change the codons of the mRNA.")],
          "Alternative splicing generates different mature mRNAs from one gene.", difficulty="medium")

    pre, intron_a, intron_b, tail = 1800, 300, 450, 200
    mature = pre - intron_a - intron_b + tail
    assert mature == 1250
    B.mcq(T, f"A eukaryotic gene is transcribed into a pre-mRNA of {pre:,} nucleotides. The pre-mRNA contains two introns, of {intron_a} and {intron_b} nucleotides. After splicing, a poly-A tail of {tail} nucleotides is added. Ignoring the cap, how many nucleotides are in the mature mRNA?",
          ch(f"{mature:,}, because the {intron_a + intron_b} nucleotides of the introns are removed and then the {tail} nucleotides of the tail are added", f"{pre:,} - {intron_a} - {intron_b} + {tail} = {mature:,}.", mature),
          [ch(f"{mature - tail:,}, because the introns are removed but the poly-A tail is not counted as a part of the mature mRNA", f"The tail is part of the mature mRNA: {mature - tail:,} + {tail} = {mature:,}.", mature - tail),
           ch(f"{pre + tail:,}, because the poly-A tail is added to the whole transcript and the introns are kept in the mature mRNA that leaves the nucleus", "Introns are removed during splicing.", pre + tail),
           ch(f"{pre:,}, because the mature mRNA has the same number of nucleotides as the pre-mRNA from which it was made", "Splicing removes the introns and the tail is added, so the length changes.", pre)],
          "The mature mRNA is the pre-mRNA minus the introns, plus the poly-A tail.", difficulty="hard")

    B.mcq(T, "A mutation in a eukaryotic cell prevents the addition of a poly-A tail to the mRNA of a gene. Which result is most likely?",
          ch("The mRNA is less stable and is broken down sooner, so less of the protein is made from the mRNA in the cell.", "The poly-A tail makes mRNA more stable."),
          [ch("The mRNA is not recognized by RNA polymerase, so the gene is not transcribed in the nucleus of the cell.", "The tail is added to the transcript after transcription has taken place."),
           ch("The introns are not removed from the mRNA, so the protein that is made has the extra amino acids from the introns.", "The tail does not control the removal of introns."),
           ch("The mRNA cannot leave the cell, so the protein is made in the nucleus instead of on the ribosomes in the cytoplasm.", "mRNA does not leave the cell. The tail affects stability.")],
          "The poly-A tail makes mRNA more stable.", difficulty="hard")

    B.mcq(T, "Which sequence of events correctly describes the flow of information for a protein-coding gene in a eukaryotic cell?",
          ch("DNA is transcribed in the nucleus, the RNA is processed, the mRNA moves to the cytoplasm, and the mRNA is translated by a ribosome.", "Information flows from DNA to mRNA to protein: transcription and RNA processing in the nucleus, and translation in the cytoplasm."),
          [ch("DNA is translated in the cytoplasm, the polypeptide is processed, the mRNA moves to the nucleus, and then the mRNA is transcribed there.", "Transcription and translation are in the opposite order in this answer."),
           ch("DNA is replicated in the nucleus, the DNA moves to the cytoplasm, and the DNA is translated directly into a protein.", "DNA is not translated directly. It is transcribed into RNA first."),
           ch("A protein is used as a template in the cytoplasm, the protein is transcribed into mRNA, and the mRNA is copied into DNA.", "The flow of information from protein to RNA does not occur.")],
          "DNA is transcribed to RNA, and RNA is translated to protein.", difficulty="easy")

    # ------------------------------------------------------------------ 6.4 Translation
    T = 4
    B.mcq(T, "Where does translation take place in a eukaryotic cell?",
          ch("On ribosomes in the cytoplasm, and on ribosomes on the cytoplasmic surface of the rough ER of the cell", "Translation occurs on ribosomes in the cytoplasm and on the cytoplasmic surface of the rough ER."),
          [ch("Only on the ribosomes that are bound to the chromosomes inside the nucleus, where the mRNA is made", "Translation occurs in the cytoplasm and on the rough ER and not inside the nucleus."),
           ch("Only on the inner surface of the nuclear envelope, because the mRNA remains in the nucleus until it is translated", "mRNA leaves the nucleus to be translated in the cytoplasm."),
           ch("Inside the Golgi apparatus, where the ribosomes join the amino acids in the order that the mRNA specifies", "Ribosomes are not found inside the Golgi apparatus.")],
          "Translation takes place on ribosomes in the cytoplasm and on the rough ER.", difficulty="easy")

    B.mcq(T, "A tRNA molecule has the anticodon 3'-UAC-5'. Which mRNA codon does this anticodon pair with?",
          ch("5'-AUG-3', because each base of the anticodon pairs with its partner and the two strands are antiparallel", "U pairs with A, A with U, and C with G. The codon is 5'-AUG-3', the start codon."),
          [ch("5'-UAC-3', because the codon is the same sequence as the anticodon with which it pairs in the ribosome", "The codon is complementary to the anticodon and is not the same sequence."),
           ch("5'-GUA-3', because the codon has the bases of the anticodon in the reverse order and is not complementary to it", "5'-GUA-3' does not pair with 3'-UAC-5'. Its partner bases would be 3'-CAU-5'."),
           ch("5'-TAC-3', because the codon is made of DNA bases and pairs with the bases of the anticodon of the tRNA", "Codons are in mRNA, which has uracil and not thymine.")],
          "The anticodon of a tRNA pairs with a codon of the mRNA.", difficulty="medium")

    B.mcq(T, "Translation is started when the rRNA of the ribosome interacts with the mRNA at the start codon. Which statement is correct?",
          ch("The start codon is AUG, and it codes for the amino acid methionine, which is the first amino acid of the new polypeptide.", "Translation is initiated at the start codon, AUG, which codes for methionine."),
          [ch("The start codon is UAA, and it codes for the amino acid methionine, which is the first amino acid of the new polypeptide.", "UAA is a stop codon."),
           ch("The start codon is AUG, and it does not code for an amino acid, but instead it tells the ribosome to start to read the mRNA.", "AUG codes for methionine in addition to starting the translation."),
           ch("The start codon is the first codon at the 5' end of every mRNA, and it codes for a different amino acid in each of the mRNAs.", "The start codon is AUG and always codes for methionine.")],
          "Translation starts at the start codon AUG, which codes for methionine.", difficulty="easy")

    used = ["AUG", "GCU", "UGG", "UAA", "GCA", "CUU", "GGU", "AAG"]
    seq = "GCAUGGCUUGGUAAGC"
    right = translate(seq)
    wrong_frame = [amino(seq[i:i + 3]) for i in range(0, 15, 3)]
    assert right == ["Met", "Ala", "Trp"] and wrong_frame == ["Ala", "Trp", "Leu", "Gly", "Lys"]
    needed = set(codons(seq[seq.index("AUG"):])[:4]) | set(codons(seq)[:5])
    assert needed <= set(used) and {amino(c) for c in used} == {"Met", "Ala", "Trp", "Stop", "Leu", "Gly", "Lys"}
    B.mcq(T, f"The mRNA 5'-{seq}-3' is translated by a ribosome. Using the table of codons, what is the sequence of amino acids of the polypeptide that is made?",
          ch(f"{'-'.join(right)}, because translation starts at the first AUG and stops at the UAA codon", "The reading starts at AUG (Met), GCU is Ala, UGG is Trp, and UAA is a stop codon."),
          [ch(f"{'-'.join(wrong_frame)}, because the first three bases of the mRNA are read first and the reading continues in triplets", "Translation starts at the start codon AUG and not at the first base of the mRNA."),
           ch(f"{'-'.join(right[::-1])}, because the polypeptide is read from the 3' end of the mRNA and is made from the last codon first", "The mRNA is read from the 5' end, starting at the start codon."),
           ch(f"{'-'.join(right)}-Stop, because the stop codon is added to the polypeptide as the last amino acid in the chain", "A stop codon does not code for an amino acid. The polypeptide is released at the stop codon.")],
          "Translation starts at AUG, reads the mRNA in triplets, and stops at a stop codon.",
          diagram=codon_table(used), difficulty="hard")

    B.mcq(T, "The genetic code is described as redundant. What does this mean?",
          ch("Many amino acids are coded for by more than one codon, so different codons can specify the same amino acid.", "Many amino acids are encoded by more than one codon."),
          [ch("Every codon codes for more than one amino acid, so the ribosome has to choose between them for each codon.", "Each codon codes for a specific amino acid (or a stop)."),
           ch("Every amino acid is coded for by exactly one codon, so the 20 amino acids use only 20 of the possible codons.", "There are 64 codons, and many amino acids have more than one."),
           ch("The code is copied twice in each cell, so that a mistake in one copy of a codon does not change the protein.", "Redundancy refers to the codons, not to the copies of the code in the cell.")],
          "More than one codon can code for the same amino acid.", difficulty="medium")

    B.mcq(T, "A gene from a human is placed into a bacterium, and the bacterium makes the human protein with the correct sequence of amino acids. Which statement best explains this?",
          ch("Nearly all living organisms use the same genetic code, which is evidence for the common ancestry of living organisms.", "A shared genetic code allows the bacterium to translate the human mRNA correctly."),
          [ch("Bacteria and humans use different genetic codes, so the bacterium has to convert the code of the human gene into its own.", "The code is nearly the same in all organisms."),
           ch("The human gene changes its sequence when it enters the bacterium, so the sequence matches the code of the bacterium.", "The gene does not change its sequence to match the code of the host."),
           ch("The bacterium makes the protein without translation, because proteins can be made directly from the DNA in the plasmid.", "The protein is made by transcription and translation.")],
          "The universal genetic code is evidence for common ancestry.", difficulty="medium")

    B.mcq(T, "In a bacterial cell, ribosomes can begin to translate an mRNA while the mRNA is still being transcribed. In a eukaryotic cell this does not happen. Which statement best explains the difference?",
          ch("A bacterium has no nucleus, so ribosomes can reach the mRNA as it is made, but a eukaryote makes and processes its mRNA in the nucleus before translation.", "In prokaryotes translation of the mRNA occurs while it is being transcribed."),
          [ch("A bacterium has no ribosomes of its own, so it uses the ribosomes that are bound to the mRNA by the cell membrane.", "Bacteria have ribosomes."),
           ch("A eukaryote has no mRNA, so the DNA of a eukaryote is translated directly into a protein by the ribosomes of the cell.", "Eukaryotes use mRNA to make proteins."),
           ch("A bacterium does not need to process its mRNA, so the mRNA is transcribed more quickly than the mRNA of a eukaryote.", "The lack of a nucleus is what allows translation during transcription.")],
          "In prokaryotes there is no nucleus, so translation can start during transcription.", difficulty="medium")

    B.mcq(T, "A retrovirus has a genome made of RNA. A drug that inhibits reverse transcriptase is given to cells that are infected with the retrovirus. Which result is most likely?",
          ch("The viral RNA is not copied into DNA, so the DNA cannot be integrated into the host genome and new viruses are not made.", "Reverse transcriptase copies the viral RNA genome into DNA, which integrates into the host genome."),
          [ch("The viral DNA is not copied into RNA, so the host cells cannot make the proteins that are needed for the new viruses.", "The step that the drug inhibits is the copying of RNA into DNA, and not of DNA into RNA."),
           ch("The host DNA is not copied during replication, so the infected cells cannot divide and the virus cannot spread to other cells.", "Reverse transcriptase does not copy the DNA of the host cell."),
           ch("The viral proteins are not translated by the ribosomes, so the viral RNA is destroyed by the enzymes of the host cell.", "Reverse transcriptase acts before the translation of the viral proteins.")],
          "Retroviruses use reverse transcriptase to copy RNA into DNA.", difficulty="medium")

    aa = 120
    nt = (aa + 1) * 3
    assert nt == 363
    B.mcq(T, f"A polypeptide has {aa} amino acids. What is the minimum number of nucleotides in the coding region of the mRNA that codes for it, including the stop codon?",
          ch(f"{nt}, because each of the {aa} amino acids needs a codon of three nucleotides and the stop codon needs three nucleotides", f"({aa} + 1) x 3 = {nt}.", nt),
          [ch(f"{aa * 3}, because each of the {aa} amino acids needs a codon of three nucleotides, and the stop codon is not counted", f"A stop codon has three nucleotides that are part of the coding region: {aa * 3} + 3 = {nt}.", aa * 3),
           ch(f"{aa + 1}, because each of the amino acids, and the stop codon, is coded for by one nucleotide of the mRNA", "Each codon has three nucleotides.", aa + 1),
           ch(f"{(aa + 1) * 2}, because each of the amino acids, and the stop codon, is coded for by two nucleotides of the mRNA", "Each codon has three nucleotides.", (aa + 1) * 2)],
          "Codons are triplets; a stop codon ends the coding region.", difficulty="hard")

    B.mcq(T, "Which event occurs during the elongation stage of translation?",
          ch("A tRNA brings the amino acid that the next codon specifies, and the amino acid is transferred to the growing polypeptide chain.", "In elongation, tRNA brings the correct amino acid to the place specified by the codon, and the amino acid is added to the chain."),
          [ch("The rRNA of the ribosome interacts with the mRNA at the start codon, and the first tRNA binds the start codon.", "This happens in initiation."),
           ch("The ribosome reaches a stop codon, and the newly synthesized protein is released from the ribosome.", "This happens in termination."),
           ch("The introns are removed from the mRNA, and the exons are spliced together before they are read by the ribosome.", "Splicing takes place in the nucleus before translation.")],
          "Elongation: tRNA brings amino acids to the ribosome, and each one is added to the growing chain.", difficulty="medium")
