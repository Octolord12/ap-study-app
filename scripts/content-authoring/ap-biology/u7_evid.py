"""Unit 7, topics 7.6 Evidence of Evolution (9 questions), 7.7 Common Ancestry (6) and 7.8 Continuing Evolution (8).

Required content (CED 2025-26): 7.6.A evolution is supported by geographical, geological, physical, biochemical and mathematical data; 7.6.B molecular, morphological and genetic evidence from living and extinct
organisms; fossils are dated by the age of the rocks, the decay of isotopes including carbon-14, and geographical data; morphological homologies, including vestigial structures, show common ancestry; DNA and protein
sequence comparisons show evolution and common ancestry. 7.7.A structural and functional evidence of the common ancestry of all eukaryotes: membrane-bound organelles, linear chromosomes, genes with introns.
7.8.A evolution is ongoing: genomic changes, a continuous fossil record, resistance to antibiotics, pesticides, herbicides and chemotherapy, and pathogens evolving to cause emergent diseases. Suggested skills: 4.B,
6.E, 3.D. Excluded: details of specific radiometric dating methods other than the idea of a decay rate.
"""
from lib import *


def build(B):
    # ------------------------------------------------------------------ 7.6 Evidence of evolution
    T = 6
    B.mcq(T, "Which of the following is an example of biochemical evidence for evolution?",
          ch("The sequence of amino acids in a protein is very similar in two species, and it differs more in a species that is less closely related.", "A comparison of DNA nucleotide sequences and protein amino acid sequences provides evidence for evolution and common ancestry."),
          [ch("The bones in the forelimbs of a bat, a whale and a human have the same arrangement, though they are used in different ways.", "This is morphological (anatomical) evidence and not biochemical evidence."),
           ch("The fossils of simple organisms are found in older layers of rock and the fossils of complex organisms are found in younger layers of rock.", "This is geological evidence from the fossil record."),
           ch("The species on a chain of islands are more similar to the species on the nearest mainland than to species on other continents.", "This is geographical evidence from the distribution of species.")],
          "Evolution is supported by geographical, geological, physical, biochemical and mathematical data.", difficulty="easy")

    B.mcq(T, "Which of the following can be used to determine the age of a fossil?",
          ch("The age of the layer of rock in which the fossil is found, and the rate of decay of radioactive isotopes such as carbon-14", "Fossils can be dated by the age of the rocks and by the rate of decay of isotopes including carbon-14."),
          [ch("The number of species that are alive today and that look similar to the fossil, and the habitat that those species now live in", "Living species do not determine the age of a fossil."),
           ch("The size of the fossil compared with a living relative, and the number of genes that the living relative has in its genome", "The size of a fossil does not give its age, and a fossil usually has no intact genome."),
           ch("The pH of the water that was used to clean the fossil in the laboratory, and the length of time that the fossil was stored", "The treatment of a fossil in the laboratory does not give its age.")],
          "Fossils are dated by the age of the rocks, isotope decay and geographical data.", difficulty="easy")

    half = 5730
    frac_left = 0.25
    n_half = 2
    assert 0.5 ** n_half == frac_left
    age = n_half * half
    B.mcq(T, f"The half-life of carbon-14 is {half:,} years. A wooden tool is found to have {int(frac_left * 100)}% of the carbon-14 that a living tree has. About how old is the tool?",
          ch(f"About {age:,} years, because {int(frac_left * 100)}% is what remains after two half-lives of {half:,} years each.", f"1 / 2 x 1 / 2 = 1 / 4, so two half-lives have passed: 2 x {half:,} = {age:,}.", age),
          [ch(f"About {half:,} years, because the amount of carbon-14 falls to {int(frac_left * 100)}% during the first half-life of the isotope.", "After one half-life, 50% remains. 25% remains after two half-lives.", half),
           ch(f"About {half * 4:,} years, because the amount of carbon-14 falls by {int(frac_left * 100)}% in each of the half-lives of the isotope.", "The amount of the isotope halves in each half-life, and it does not fall by 25%.", half * 4),
           ch(f"About {int(half * 0.75):,} years, because the tool has lost 75% of its carbon-14 and so 75% of one half-life has passed.", "Decay is exponential, not linear. Losing 75% takes two half-lives.", int(half * 0.75))],
          "After n half-lives, (1/2)^n of the isotope remains.", difficulty="medium")

    B.mcq(T, "The forelimbs of humans, bats and whales have the same arrangement of bones, though the limbs are used for grasping, flying and swimming. Which statement best explains this similarity?",
          ch("The three species descended from a common ancestor that had this arrangement of bones, which has been modified in each lineage.", "Morphological homologies provide evidence of common ancestry."),
          [ch("The three species each evolved the same arrangement of bones separately, because the arrangement is the best design for any kind of forelimb.", "The different uses of the limbs show that the shared arrangement is not the best design for all uses."),
           ch("The three species acquired the same arrangement of bones during their lives, because they all use their forelimbs often and in similar ways.", "The limbs are used in different ways, and acquired changes are not inherited."),
           ch("The three species have the same arrangement of bones by chance, because the bones form in a random order in the embryo of each species.", "The shared pattern is too detailed to be explained by chance.")],
          "Homologous structures are evidence of common ancestry.", difficulty="medium")

    B.mcq(T, "Whales have small pelvic bones that are not attached to the backbone and that have no function in swimming. Which statement is best supported by this observation?",
          ch("Whales descended from ancestors with hind limbs, and the structure is a vestigial remnant that provides evidence of common ancestry.", "Vestigial structures are morphological homologies that provide evidence of common ancestry."),
          [ch("Whales will evolve hind limbs in the next generations, because the bones show that the whales need them in order to survive.", "Evolution does not occur in response to needs, and vestigial structures are leftovers."),
           ch("Whales developed the pelvic bones during their lives, because the animals use the bones more as they grow older and larger.", "The bones are not used, and acquired characteristics are not inherited."),
           ch("Whales are not related to any land animals, because the pelvic bones of whales do not have any function in the animals.", "A vestigial structure supports a relationship with land animals that have functional pelvic bones.")],
          "Vestigial structures are evidence of common ancestry.", difficulty="medium")

    rows = [("Species 1", "2", "1.4"), ("Species 2", "9", "6.4"), ("Species 3", "21", "15.0")]
    length = 140
    for r in rows:
        assert round(int(r[1]) / length * 100, 1) == float(r[2])
    B.mcq(T, f"The table shows the number of differences in the amino acid sequence of a protein of {length} amino acids between a human and three other species. Which conclusion is best supported by the data?",
          ch("Species 1 is the most closely related to humans of the three, because its protein sequence has the fewest differences from the human sequence.", "A comparison of protein sequences provides evidence for relationships. Fewer differences suggest a more recent common ancestor."),
          [ch("Species 3 is the most closely related to humans of the three, because its protein sequence has the most differences from the human sequence.", "More differences suggest a more distant relationship."),
           ch("Species 2 is the most closely related to humans of the three, because its protein sequence differs from the human sequence by an intermediate amount.", "The species with the fewest differences is the most closely related."),
           ch("The three species are equally related to humans, because all of them have the same protein with the same number of amino acids.", "The numbers of differences are not the same, which shows different degrees of relatedness.")],
          "Fewer sequence differences suggest a more recent common ancestor.",
          diagram=table(["Species", "Differences from the human protein", "Differences (% of the amino acids)"], rows, caption="Differences in a protein of 140 amino acids", row_headers=True), difficulty="hard")

    d1, t1, d2 = 12, 24, 30
    rate = d1 / t1
    t2 = d2 / rate
    assert (rate, t2) == (0.5, 60.0)
    B.mcq(T, f"Differences in a protein sequence accumulate at a constant rate. Two species whose lineages separated {t1} million years ago differ at {d1} amino acids. Two other species differ at {d2} amino acids. About how long ago did the lineages of the other two species separate?",
          ch(f"About {t2:.0f} million years ago, because the rate is {rate:.1f} difference per million years and {d2} / {rate:.1f} = {t2:.0f}.", f"The rate is {d1} / {t1} = {rate:.1f} differences per million years, so {d2} differences take {t2:.0f} million years.", t2),
          [ch(f"About {d2 - d1 + t1} million years ago, because the extra {d2 - d1} differences are added to the {t1} million years of the first pair.", "The time is found from the rate of change, and not by adding the differences to the years.", d2 - d1 + t1),
           ch(f"About {t1 * (d1 / d2):.0f} million years ago, because the greater the number of differences, the shorter the time since the lineages separated.", "More differences mean more time has passed.", round(t1 * (d1 / d2))),
           ch(f"About {d2 * rate:.0f} million years ago, because the number of differences is multiplied by the rate of {rate:.1f} per million years.", "The number of differences must be divided by the rate to give the time.", d2 * rate)],
          "A molecular clock: time = differences / rate.", difficulty="hard")

    B.mcq(T, "In a series of undisturbed rock layers, fossils of simple, single-celled organisms are found in the deepest layers, and fossils of more complex organisms appear in higher layers. Which statement is best supported by this observation?",
          ch("Life on Earth has changed over time, because the oldest layers are deeper, and different organisms are found in layers of different ages.", "Geological data show that organisms have changed over time."),
          [ch("All of the species lived at the same time, because the fossils of the simple and the complex organisms are found in the same rock sequence.", "The layers have different ages, and the fossils in them are of different ages."),
           ch("The complex organisms changed into the simple organisms, because the simple organisms are found in the deeper layers of the rock.", "The deeper (older) layers contain the simple organisms, so the order is the opposite."),
           ch("New layers of rock form from the fossils, because the organisms in the higher layers made the rock from their own bodies.", "Layers form by deposition of sediments, and fossils are found in them.")],
          "The fossil record in layers of rock shows change over time.", difficulty="medium")

    B.mcq(T, "Two lizard species on separate continents have a similar body shape but are not closely related, according to DNA data. A student claims that the similar body shape shows that the two species have a recent common ancestor. How should the student's claim be evaluated?",
          ch("The claim is not well supported, because molecular data are usually more reliable than morphology, and similar shapes can evolve separately.", "Molecular data typically provide more accurate and reliable evidence than morphological traits."),
          [ch("The claim is well supported, because the body shape of an organism is always more reliable evidence than its DNA sequence.", "DNA data are typically more reliable than body shape."),
           ch("The claim is well supported, because two species with a similar body shape must have gotten it from a recent common ancestor.", "Similar traits can evolve separately in response to similar selective pressures."),
           ch("The claim cannot be evaluated, because the DNA of a species does not contain information about its evolutionary history.", "DNA sequences are used to infer evolutionary relationships.")],
          "Molecular data are typically more reliable than morphology for inferring relationships.", difficulty="medium")

    # ------------------------------------------------------------------ 7.7 Common ancestry
    T = 7
    B.mcq(T, "Which set of features is shared by all eukaryotes and provides evidence of their common ancestry?",
          ch("Membrane-bound organelles, linear chromosomes, and genes that contain introns", "Structural and functional evidence of the common ancestry of all eukaryotes includes these three features."),
          [ch("A circular chromosome, ribosomes, and genes that are grouped in operons that are transcribed together", "These are features of prokaryotes."),
           ch("A cell wall, chloroplasts, and the ability to carry out photosynthesis in the light from the sun", "These are not found in all eukaryotes. Animals lack all three."),
           ch("A plasma membrane, ribosomes, and DNA as the genetic material of the cell in all of the cell types", "These are found in all cells, including prokaryotes, and so they do not separate eukaryotes.")],
          "Shared features of eukaryotes: membrane-bound organelles, linear chromosomes, genes with introns.", difficulty="easy")

    B.mcq(T, "Genes that contain introns are found in plants, fungi and animals. Which statement best explains why this observation supports a common ancestry of eukaryotes?",
          ch("It is unlikely that such a complex feature evolved separately in each lineage, and so it was probably present in a common ancestor of the eukaryotes.", "Shared complex features suggest inheritance from a common ancestor."),
          [ch("Introns are needed for all organisms to survive, and so every organism has to have genes with introns in order to live.", "Prokaryotes lack introns and survive."),
           ch("Introns are produced by the environment in each organism, and so organisms in the same environment will have introns.", "Introns are part of the genes and are inherited."),
           ch("Introns are found in the genes of prokaryotes and eukaryotes alike, and so all of the organisms on Earth have a common ancestor.", "Introns are typical of eukaryotic genes and not of prokaryotes.")],
          "Genes with introns are shared by eukaryotes, evidence of common ancestry.", difficulty="medium")

    B.mcq(T, "Scientists discover a single-celled organism in a lake. It has a nucleus, several linear chromosomes, and genes that contain introns. Which prediction about the organism is best supported by these features?",
          ch("It is a eukaryote, and it shares a common ancestor with other eukaryotes such as plants, fungi and animals.", "Linear chromosomes and genes with introns are features of eukaryotes."),
          [ch("It is a prokaryote, because most of the single-celled organisms in lakes are prokaryotes and they have a nucleus.", "Prokaryotes do not have a nucleus, linear chromosomes or introns."),
           ch("It is a virus, because viruses have only a few genes and can be found in water in the lakes of all regions.", "A virus is not a cell and does not have a nucleus."),
           ch("It cannot be classified, because the features of cells do not show how an organism is related to the other organisms.", "Structural features are used to infer relationships.")],
          "Linear chromosomes and introns are shared eukaryotic features.", difficulty="medium")

    rows = [("Organism W", "Yes", "Yes", "Yes"), ("Organism X", "No", "No", "No"), ("Organism Y", "Yes", "Yes", "Yes"), ("Organism Z", "No", "No", "No")]
    B.mcq(T, "The table shows three features of four organisms. Which statement is best supported by the data?",
          ch("Organisms W and Y share the features of eukaryotes, which suggests that they share a common ancestor that was a eukaryote.", "Membrane-bound organelles, linear chromosomes and introns are features of eukaryotes."),
          [ch("Organisms X and Z share the features of eukaryotes, which suggests that they share a common ancestor that was a eukaryote.", "Organisms X and Z lack the three features, so they are probably prokaryotes."),
           ch("Organisms W and X share the features of eukaryotes, which suggests that they share a common ancestor that was a eukaryote.", "Organism X lacks all three features."),
           ch("All four organisms are eukaryotes, because every organism has a membrane and takes in energy from its environment.", "Two of the organisms lack the three features that are shared by eukaryotes.")],
          "Shared features of eukaryotes suggest a shared ancestor.",
          diagram=table(["Organism", "Membrane-bound organelles", "Linear chromosomes", "Genes with introns"], rows, caption="Features of four organisms", row_headers=True), difficulty="medium")

    B.mcq(T, "If all eukaryotes descended from a common ancestor, which observation would be expected in the cells of a newly discovered eukaryote?",
          ch("The cells have a nucleus and other membrane-bound organelles, and the DNA is organized into linear chromosomes.", "These are structural features that are expected in all eukaryotes."),
          [ch("The cells have no membrane-bound organelles, and the DNA is organized into a single circular chromosome.", "These are features of prokaryotes."),
           ch("The cells have chloroplasts and cell walls, and they carry out photosynthesis in the same way as all of the other eukaryotes.", "Not all eukaryotes have chloroplasts or cell walls."),
           ch("The cells have a different genetic code from every other organism, and their DNA is not made of nucleotides.", "A shared ancestor would be reflected in shared molecular features.")],
          "All eukaryotes share membrane-bound organelles and linear chromosomes.", difficulty="medium")

    B.mcq(T, "Which finding would be most difficult to explain if all eukaryotes share a common ancestor?",
          ch("A eukaryote whose cells have a nucleus but whose chromosomes and genes are in no way similar to those of any other eukaryote", "A common ancestor predicts shared features such as linear chromosomes and genes with introns."),
          [ch("A eukaryote whose genes contain introns that are similar to the introns in the genes of a distantly related eukaryote", "Shared introns are expected if there was a common ancestor."),
           ch("A eukaryote whose cells have mitochondria that are surrounded by a double membrane like those of other eukaryotes", "Shared organelles are expected."),
           ch("A eukaryote whose chromosomes are linear and are condensed with proteins during the division of the cell", "Linear chromosomes are a shared feature of eukaryotes.")],
          "Common ancestry predicts shared structural and genetic features.", difficulty="hard")

    # ------------------------------------------------------------------ 7.8 Continuing evolution
    T = 8
    B.mcq(T, "A hospital treats a bacterial infection with an antibiotic, and a few bacteria survive and multiply. Later infections in the hospital are resistant to the antibiotic. Which statement best explains this?",
          ch("A few bacteria already had a mutation for resistance, and the antibiotic selected for them, so they reproduced and became common.", "Resistance to antibiotics evolves by selection of mutations that are already in the population."),
          [ch("The antibiotic caused the bacteria to mutate in the way that they needed, so every bacterium became resistant to it in a single step.", "Mutations are random and are not directed by the antibiotic."),
           ch("Each bacterium learned to resist the antibiotic during its life, and then passed on its learned resistance to its offspring.", "Acquired traits are not inherited in this way."),
           ch("The patient developed resistance to the antibiotic, and the resistance was passed to the bacteria that live in the body.", "Resistance is a property of the bacteria and not of the patient.")],
          "Antibiotic resistance evolves by natural selection.", difficulty="easy")

    B.mcq(T, "A farmer uses the same insecticide each year, and over several years it kills fewer and fewer insects. Which statement best explains this?",
          ch("Insects with alleles for resistance survive and reproduce more than the others, so the frequency of the alleles rises in the population.", "Evolution of resistance to pesticides is an example of ongoing evolution."),
          [ch("The insecticide becomes weaker as it is used more, because the chemicals in it break down faster in each year than they did in the year before.", "The explanation is in the evolution of the insects and not in the chemistry of the insecticide."),
           ch("Each insect becomes immune to the insecticide after it is sprayed once, and the immunity is passed on to its offspring.", "Individual insects do not acquire heritable immunity in this way."),
           ch("The insects that are killed by the insecticide are replaced by insects of a different species that are better at finding food.", "The explanation is a change in the frequency of alleles within a species.")],
          "Resistance to pesticides evolves by natural selection.", difficulty="medium")

    B.mcq(T, "Influenza viruses change from year to year, so a new vaccine is needed in most years. Which statement best explains how the viruses change?",
          ch("Mutations in the viral genome add variation, and variants that evade the immune responses of people are selected, so pathogens evolve.", "Pathogens evolve and cause emergent diseases."),
          [ch("People who are vaccinated pass the vaccine to the viruses, and the viruses use the vaccine in order to change their genes.", "Vaccines do not change the genes of viruses."),
           ch("The viruses decide which genes to change in order to be able to infect more people in the next year of the season.", "Viruses do not make decisions, and mutations are random."),
           ch("The viruses never change from year to year, and so the new vaccines are made only to give people a chance to produce more antibodies each year.", "Viruses do change, and that is why the vaccines are updated.")],
          "Pathogens evolve, which can lead to emergent diseases.", difficulty="medium")

    B.mcq(T, "A tumor shrinks during chemotherapy, and then it regrows and no longer responds to the drug. Which statement is the most consistent with natural selection?",
          ch("A few cancer cells in the tumor were resistant to the drug, and they survived and divided, so the tumor cells became mostly resistant.", "Evolution of resistance to chemotherapy drugs is an example of ongoing evolution."),
          [ch("All of the cancer cells in the tumor changed together to become resistant, because the drug told them to change their DNA.", "A drug does not direct mutations."),
           ch("The healthy cells of the patient became resistant to the drug, and so they could also take over the place of the tumor cells.", "The resistance is in the tumor cells that survive."),
           ch("The cancer cells that survived stopped dividing completely, so the tumor grew back by a process other than cell division.", "Tumors regrow by the division of the cells that survive.")],
          "Cancer cells can evolve resistance to chemotherapy by selection.", difficulty="medium")

    B.mcq(T, "Which observation about the fossil record supports the claim that evolution is a continuing process?",
          ch("Fossils from successive layers of rock show gradual changes in the traits of a lineage, and there is no point at which change stops.", "A continuous change in the fossil record is evidence that species have evolved and continue to evolve."),
          [ch("Fossils of the same species are found in every layer of rock, and they have exactly the same traits in all of the layers.", "No change in the fossils would suggest that no evolution occurs."),
           ch("Fossils are found only in the youngest layers of rock, and none of the older layers of rock contain any traces of organisms.", "Fossils are found in older layers too."),
           ch("Fossils of extinct species are found, but the traits of the living species are exactly the same as the traits of the extinct species.", "Different traits in living and extinct species suggest change over time.")],
          "A continuous change in the fossil record shows that evolution is ongoing.", difficulty="medium")

    gens = [0, 1, 2, 3, 4, 5]
    use = [0, 10, 20, 30, 40, 50]
    resist = [2, 4, 9, 18, 33, 52]
    g = graph("Antibiotic use (doses per 1,000 people per day)", "Resistant bacteria in infections (%)", 0, 50, 0, 60,
              [line("Resistant bacteria", list(zip(use, resist)), "red")],
              "Percent of infections caused by resistant bacteria against antibiotic use. It rises from 2 percent at no use to 52 percent at 50 doses per 1,000 people per day.")
    B.mcq(T, "The graph shows the percent of infections caused by resistant bacteria in six regions that differ in their use of an antibiotic. Which conclusion is best supported by the data?",
          ch("Regions in which the antibiotic is used more have more resistant bacteria, which is consistent with selection for resistance by the antibiotic.", "Resistant bacteria are favored when the antibiotic is used, so they become a larger percent of the infections."),
          [ch("Using the antibiotic more often makes the bacteria in the infections mutate to become resistant, as the graph shows.", "The graph shows a correlation. It does not show that the antibiotic causes the mutations."),
           ch("Regions in which the antibiotic is used less have more resistant bacteria, because the resistant bacteria are favored when no antibiotic is used.", "The percent of resistant bacteria is lower where there is less use of the antibiotic."),
           ch("The use of the antibiotic has no effect on the percent of resistant bacteria, because some resistant bacteria are found in every region.", "The percent rises with use, which shows an effect.")],
          "Antibiotic use selects for resistant bacteria.", diagram=g, difficulty="hard")

    B.mcq(T, "A scientist hypothesizes that the resistance of a weed to a herbicide came from alleles that were already in the population before the herbicide was used. Which investigation would best test this hypothesis?",
          ch("Spray the herbicide on many seedlings from a population that has never been exposed to it, and see whether any of them survive.", "If some seedlings of an unexposed population survive, resistance alleles were present before exposure."),
          [ch("Spray the herbicide on many seedlings of the weed that have already been exposed to the herbicide for several years in the field.", "Previously exposed plants cannot show whether the alleles were there before exposure."),
           ch("Grow seedlings of the weed in a greenhouse with no herbicide, and measure the height of all of the seedlings after a month.", "This does not test resistance to the herbicide."),
           ch("Spray the herbicide on a single seedling of the weed and see whether the seedling survives for a week or more.", "A single plant is too small a sample, and the result would not show how common the alleles are.")],
          "To test whether variation preexisted, expose a population with no history of exposure.", difficulty="hard")

    B.mcq(T, "Scientists sequence the genomes of a virus from patients in each of five years. The genomes from the later years differ from the genomes from the first year in more positions. Which statement is best supported by this observation?",
          ch("The genome of the virus has changed over time, which is evidence that the virus is evolving.", "Genomic changes over time are an example of ongoing evolution."),
          [ch("The genome of the virus cannot change, because the sequences from the five years must all be identical in order to be of one virus.", "Viral genomes accumulate mutations over time."),
           ch("The patients changed the genome of the virus on purpose, because they chose the sequence that gave the best protection.", "Patients do not choose the genome of a virus."),
           ch("The virus has stopped evolving, because the differences are not equal in each of the five years that were studied.", "Differences that accumulate show evolution that is still occurring.")],
          "Genomic changes over time show that evolution is ongoing.", difficulty="medium")
