"""Unit 7, topics 7.9 Phylogeny (10 questions) and 7.10 Speciation (10).

Required content (CED 2025-26): 7.9.A phylogenetic trees and cladograms show hypothetical relationships that can be tested; trees show the amount of change over time (calibrated by fossils or a molecular clock),
cladograms do not show time or the size of the differences; gained or lost traits build them; the outgroup is the lineage least closely related; shared derived characters are informative; molecular data are typically
more reliable than morphology; 7.9.B nodes are the most recent common ancestor of two lineages; trees are hypotheses revised with evidence. 7.10.A speciation occurs when populations become reproductively isolated;
the biological species concept; 7.10.B punctuated equilibrium and gradualism; divergent evolution and adaptive radiation; convergent evolution; 7.10.C sympatric and allopatric speciation; pre-zygotic and post-zygotic
mechanisms. Suggested skills: 2.D, 2.B, 6.E.
"""
from lib import *


def vertebrate_tree():
    """Lamprey is the outgroup. Marks 1-4 number the branching points from the base to the tip; traits are gained on the branches that lead to them."""
    return tree({"children": [
        {"label": "Lamprey"},
        {"mark": "1", "trait": "Jaws", "children": [
            {"label": "Shark"},
            {"mark": "2", "trait": "Four limbs", "children": [
                {"label": "Salamander"},
                {"mark": "3", "trait": "Amniotic egg", "children": [
                    {"label": "Lizard"},
                    {"mark": "4", "trait": "Hair", "children": [{"label": "Mouse"}, {"label": "Human"}]}]}]}]}]},
        alt="Cladogram of six animals. The lamprey branches off first. The shark branches next, after the trait jaws appears at node 1. The salamander branches next, after four limbs appears at node 2. The lizard branches next, after the amniotic egg appears at node 3. The mouse and the human share node 4, after hair appears.")


def build(B):
    # ------------------------------------------------------------------ 7.9 Phylogeny
    T = 9
    B.mcq(T, "What does a node (a branching point) on a phylogenetic tree or a cladogram represent?",
          ch("The most recent common ancestor of the two groups or lineages that branch from it", "The nodes on a tree represent the most recent common ancestor of any two groups or lineages."),
          [ch("The point at which one of the two lineages that branch from it changed into the other lineage in the tree", "A node is an ancestor of both lineages. One lineage did not change into the other."),
           ch("The time at which all of the organisms on the tree died out and a new group of organisms began to form", "A node represents a split of a lineage and not an extinction of all of the organisms."),
           ch("The single trait that is most different between the two lineages that branch from it on the tree", "A node represents a common ancestor, and not a difference between the two lineages.")],
          "A node is the most recent common ancestor of the lineages that branch from it.", difficulty="easy")

    B.mcq(T, "In a phylogenetic tree or cladogram, what does the outgroup represent?",
          ch("The lineage that is least closely related to the other organisms in the tree, and that is used as a reference for the comparison", "The outgroup is the lineage that is least closely related to the remainder of the organisms."),
          [ch("The lineage that is most closely related to all of the other organisms in the tree, and that has the most derived traits", "The outgroup is the least closely related lineage."),
           ch("The lineage that has become extinct before any of the other organisms in the tree appeared, and that has no living relatives at all", "The outgroup is not necessarily extinct."),
           ch("The lineage that has the largest number of species in the tree, and that is located at the top of the diagram", "The outgroup is defined by how closely it is related, not by its number of species.")],
          "The outgroup is the lineage least closely related to the rest.", difficulty="easy")

    B.mcq(T, "The cladogram shows the relationships of six animals, with the numbered branching points. Which number represents the most recent common ancestor of the lizard, the mouse and the human?",
          ch("3, because the lizard branches from the lineage that leads to the mouse and the human at that node, and no other node includes all three.", "Node 3 is where the lizard lineage splits from the lineage of the mouse and the human."),
          [ch("4, because the mouse and the human branch from each other at that node, which is the most recent branching point on the tree.", "Node 4 is the common ancestor of the mouse and the human only. It does not include the lizard."),
           ch("2, because it is the node at which the salamander branches off from the lineage that leads to the lizard, the mouse and the human.", "Node 2 is the common ancestor of the salamander, the lizard, the mouse and the human."),
           ch("1, because it is the oldest node that is shared by the lineages that have jaws, and so it includes all of the animals.", "Node 1 includes the shark and the salamander as well as the other three animals.")],
          "A node is the most recent common ancestor of the groups that branch from it.", diagram=vertebrate_tree(), difficulty="medium")

    B.mcq(T, "According to the cladogram, which trait is a shared derived character that supports a closer relationship between the mouse and the human than between either of them and the lizard?",
          ch("Hair, because it was gained in the lineage that leads to the mouse and the human, after the lizard had branched off.", "A trait that appears on the branch into node 4 is shared only by the mouse and the human."),
          [ch("The amniotic egg, because it was gained before the lizard branched off, so the lizard has it too and it does not separate them.", "The amniotic egg is shared by the lizard, the mouse and the human."),
           ch("Jaws, because it was gained before the shark branched off, so it is found in most of the animals and does not separate them.", "Jaws are shared by five of the six animals."),
           ch("Four limbs, because it is a trait that the mouse and the human share, and the lizard does not have it in this tree.", "The lizard is placed after the trait four limbs was gained, so it has four limbs.")],
          "Shared derived characters indicate common ancestry.", diagram=vertebrate_tree(), difficulty="medium")

    B.mcq(T, "Which statement correctly compares a phylogenetic tree with a cladogram?",
          ch("A phylogenetic tree can show the amount of change over time, calibrated by fossils or a molecular clock, but a cladogram does not show time or the size of the differences.", "Trees show the amount of change over time, and cladograms do not show a time scale or the evolutionary differences between groups."),
          [ch("A cladogram can show the amount of change over time, calibrated by fossils or a molecular clock, but a phylogenetic tree does not show time.", "This reverses the two kinds of diagram."),
           ch("A phylogenetic tree and a cladogram are the same, because both of them show the exact dates at which each group of organisms first appeared.", "A cladogram does not show a time scale."),
           ch("A cladogram shows the evolutionary relationships of living organisms only, and a phylogenetic tree shows the relationships of fossil organisms only.", "Both kinds of diagram can include living and fossil organisms.")],
          "Phylogenetic trees can show time and the amount of change; cladograms do not.", difficulty="medium")

    B.mcq(T, "A phylogenetic tree built from the morphology of species conflicts with a tree built from DNA sequences of the same species. Which statement is the best evaluation?",
          ch("The tree built from the DNA sequences is typically more accurate and reliable, because similar body shapes can evolve separately.", "Molecular data typically provide more accurate and reliable evidence than morphological traits."),
          [ch("The tree built from the morphology is always more accurate, because body shape is a trait that is under direct natural selection.", "Selection can produce similar shapes in unrelated species, which makes morphology less reliable."),
           ch("Neither tree can be correct, because phylogenetic trees cannot be built from either the morphology or the DNA of the species.", "Both kinds of data are used to build trees."),
           ch("Both trees must be exactly correct, because all of the data that are used to build a tree have the same level of reliability.", "Molecular data are typically more reliable.")],
          "Molecular data are typically more reliable than morphology for building trees.", difficulty="medium")

    rows = [("Outgroup", "No", "No", "No"), ("Species A", "Yes", "No", "No"), ("Species B", "Yes", "Yes", "No"), ("Species C", "Yes", "Yes", "Yes")]
    B.mcq(T, "The table shows three derived traits in an outgroup and in three species. Which statement about the relationships is best supported by the data?",
          ch("Species B and Species C share a more recent common ancestor with each other than either of them does with Species A, because they share trait 2.", "Trait 2 is a shared derived character of B and C only, which indicates a more recent common ancestor."),
          [ch("Species A and Species B share a more recent common ancestor with each other than either of them does with Species C, because they share trait 1.", "Trait 1 is shared by all three species, so it does not separate A from B and C."),
           ch("Species A and Species C share a more recent common ancestor with each other than either of them does with Species B, because they share trait 1.", "Trait 1 is shared by all three species and it is not informative about which pair is closer."),
           ch("The outgroup is the most closely related to Species C, because the outgroup has none of the traits and so it is similar to Species C.", "The outgroup lacks the derived traits and is the least closely related to the other species.")],
          "Shared derived characters group species into nested lineages.",
          diagram=table(["Organism", "Trait 1", "Trait 2", "Trait 3"], rows, caption="Derived traits in an outgroup and three species", row_headers=True), difficulty="hard")

    B.mcq(T, "Use the cladogram to count how many of the four labeled traits were gained in the lineage that leads from the base of the tree to the human.",
          ch("Four, because jaws, four limbs, the amniotic egg and hair were gained one after the other on the branches that lead to the human.", "The path from the base to the human passes through the four labeled traits."),
          [ch("Three, because the human has jaws, four limbs and hair, but the amniotic egg is a trait that is found only in the lizard.", "The amniotic egg is gained before the lizard branched off, and the human is on the same lineage."),
           ch("Two, because the human shares hair with the mouse and four limbs with the salamander, and these are the only traits that it shares.", "The human has all of the traits that were gained on the path to it."),
           ch("One, because the tree shows only the trait hair on the final branch to the human, and the other traits belong to other animals.", "The traits gained earlier on the path are also traits of the human.")],
          "Traits gained along a lineage are inherited by every descendant on that lineage.", diagram=vertebrate_tree(), difficulty="hard")

    B.mcq(T, "Sequence data from a newly sequenced species show that a species that was placed in one branch of a cladogram is more closely related to a different branch. What should scientists do with the cladogram?",
          ch("Revise the cladogram to match the new evidence, because cladograms represent hypotheses that are constantly revised.", "Phylogenetic trees and cladograms represent hypotheses that are constantly being revised based on evidence."),
          [ch("Keep the cladogram without changing it, because a cladogram that has been published cannot be changed by new evidence.", "Cladograms are hypotheses that are revised with new evidence."),
           ch("Discard all of the cladograms of all of the species, because one new result shows that no cladogram can be used.", "One revision does not invalidate the method."),
           ch("Change the DNA sequence of the species, because the cladogram is correct and so the sequence data must be wrong.", "The data are the evidence, and the hypothesis is revised.")],
          "Cladograms are hypotheses that are revised as evidence changes.", difficulty="medium")

    B.mcq(T, "According to the cladogram, why is the presence of four limbs not useful for deciding whether the mouse is more closely related to the human or to the lizard?",
          ch("All three animals have four limbs, which were gained in a common ancestor of the three, so the trait does not separate them.", "A trait that is shared by all of the lineages being compared is not informative for the grouping."),
          [ch("Only the lizard has four limbs, so the trait is found in one animal and cannot be used to compare the three animals.", "The mouse and the human also have four limbs."),
           ch("Four limbs is a trait that was lost in the human, so it cannot tell us anything about the relationships of the three animals.", "The tree shows the trait as gained, not lost, on the path to the human."),
           ch("Four limbs is a trait of the salamander only, so it can be used only to separate the salamander from the other animals.", "The trait is also found in the lizard, the mouse and the human.")],
          "Shared derived characters must separate the groups being compared to be informative.", diagram=vertebrate_tree(), difficulty="hard")

    # ------------------------------------------------------------------ 7.10 Speciation
    T = 10
    B.mcq(T, "According to the biological species concept, which statement defines a species of sexually reproducing organisms?",
          ch("A group of organisms that can interbreed and exchange genetic information to produce viable and fertile offspring", "The biological species concept defines a species as a group capable of interbreeding to produce viable, fertile offspring."),
          [ch("A group of organisms that look alike and that live in the same habitat, whether or not they are able to interbreed", "Similar appearance is not the criterion of the biological species concept."),
           ch("A group of organisms that can mate with each other to produce offspring, whether or not the offspring are fertile", "The offspring have to be viable and fertile."),
           ch("A group of organisms that share the same ancestor, however distant, and that are found in the same part of the world", "The biological species concept is based on interbreeding and not on distant ancestry.")],
          "The biological species concept: a group capable of producing viable, fertile offspring.", difficulty="easy")

    B.mcq(T, "A river changes its course and divides a population of mice into two groups that cannot cross the river. Over thousands of generations the two groups become different species. Which term describes this process?",
          ch("Allopatric speciation, because the two populations were geographically isolated from each other when they first diverged.", "Allopatric speciation occurs in populations that are geographically isolated."),
          [ch("Sympatric speciation, because the two populations were found in the same place and exchanged alleles when they diverged.", "In sympatric speciation, the populations overlap geographically. Here they were separated by the river."),
           ch("Convergent evolution, because the two populations became more similar to each other as they adapted to different habitats.", "Convergent evolution involves unrelated populations that become more similar."),
           ch("Punctuated equilibrium, because the two populations did not change at all during the thousands of generations that passed.", "Punctuated equilibrium describes the rate of change and not geographic separation.")],
          "Allopatric speciation occurs in geographically isolated populations.", difficulty="medium")

    B.mcq(T, "In a single lake, a population of fish splits into two groups. One group feeds only near the surface and the other group feeds only at the bottom, and the two groups no longer mate with each other. Which term describes this process?",
          ch("Sympatric speciation, because the two groups diverge while living in the same area, without a geographic barrier between them.", "Sympatric speciation occurs in populations with geographic overlap."),
          [ch("Allopatric speciation, because the two groups are separated by a physical barrier and are in different places in the lake.", "There is no geographic barrier. The groups live in the same lake."),
           ch("Convergent evolution, because the two groups become more similar to each other as they feed in different parts of the same lake.", "The two groups become more different, not more similar."),
           ch("The founder effect, because a few individuals left the lake and started a new population in another part of the world.", "The groups are in the same lake, and no new population was started elsewhere.")],
          "Sympatric speciation occurs in populations with geographic overlap.", difficulty="medium")

    B.mcq(T, "Two closely related species of frogs live in the same pond. The males of one species call at a frequency that females of the other species do not respond to. Which statement describes this mechanism?",
          ch("It is a pre-zygotic mechanism, because it prevents mating, so no zygote is formed, and it maintains reproductive isolation.", "Pre-zygotic mechanisms act before the formation of a zygote."),
          [ch("It is a post-zygotic mechanism, because the offspring of a mating between the two species do not survive or else are sterile.", "In this example mating does not happen, so it acts before a zygote forms."),
           ch("It is a mechanism that increases gene flow between the species, because the frogs share the same pond in all seasons.", "The mechanism prevents gene flow."),
           ch("It is not a mechanism of reproductive isolation, because the two species of frogs can still be found in the same pond.", "Behavioral differences can isolate species that live in the same place.")],
          "Pre-zygotic and post-zygotic mechanisms maintain reproductive isolation.", difficulty="medium")

    B.mcq(T, "A horse and a donkey can mate and produce a mule, but the mule is sterile. Which statement best describes what this shows about the horse and the donkey?",
          ch("They are separate species, because a post-zygotic mechanism, the sterility of the hybrid offspring, prevents gene flow between them.", "The offspring are not fertile, so the horse and the donkey do not exchange genes through them."),
          [ch("They are the same species, because they can mate and produce offspring, and this is the only criterion for a species.", "The offspring must be viable and fertile."),
           ch("They are separate species, because a pre-zygotic mechanism prevents the horse and the donkey from ever mating with each other in the wild.", "They do mate. The isolation acts after the zygote forms."),
           ch("They are the same species, because the mule is healthy and alive and so it will be able to produce a lineage of mules.", "The mule is sterile and so it does not start a lineage.")],
          "Sterile hybrids are a post-zygotic isolating mechanism.", difficulty="medium")

    B.mcq(T, "The fossil record of a lineage of snails shows almost no change for millions of years, followed by a short period in which new forms appear. Which term describes this pattern?",
          ch("Punctuated equilibrium, in which evolution occurs rapidly after a long period of stasis.", "Punctuated equilibrium is when evolution occurs rapidly after a long period of stasis."),
          [ch("Gradualism, in which evolution occurs slowly and steadily over hundreds of thousands or millions of years.", "Gradualism would show steady change over the whole period."),
           ch("Convergent evolution, in which unrelated lineages become more similar because of similar selective pressures.", "The pattern describes the rate of change in one lineage."),
           ch("Genetic drift, in which allele frequencies in a small population change because of chance events from one generation to the next.", "Genetic drift is a mechanism and not a pattern of change in the fossil record.")],
          "Punctuated equilibrium: rapid change after a long period of stasis.", difficulty="medium")

    B.mcq(T, "When a volcano forms a new island, a single species of finch reaches it and, over time, produces several species that use different foods. Which term best describes this rapid formation of many species from one ancestor?",
          ch("Adaptive radiation, which is divergent evolution that is especially rapid when new habitats become available to species.", "Speciation rates can be especially rapid during times of adaptive radiation as new habitats become available."),
          [ch("Convergent evolution, which makes unrelated species look alike when they are subject to the same selective pressures.", "The species came from one ancestor and became different."),
           ch("The bottleneck effect, which reduces the genetic diversity of a population after a large part of the population has died.", "The finches radiated into new species. The bottleneck effect is about loss of diversity."),
           ch("Gene flow, which prevents separate populations from diverging into different species by moving alleles between them.", "Gene flow prevents divergence, which is the opposite of what happened.")],
          "Adaptive radiation is rapid divergent evolution when new habitats open up.", difficulty="medium")

    B.mcq(T, "Sharks (fish) and dolphins (mammals) have a similar streamlined body shape, though they are not closely related. Which statement best explains this?",
          ch("Similar selective pressures in the water produced similar adaptations in the two lineages, and so it is convergent evolution.", "Convergent evolution occurs when similar selective pressures result in similar adaptations in different species."),
          [ch("Sharks and dolphins inherited the body shape from a recent common ancestor, which was a streamlined animal that lived in water.", "They are not closely related, and the shape evolved separately."),
           ch("Dolphins changed into sharks over time, because the dolphins that lived in the sea had to change in order to be able to survive.", "One lineage did not change into the other."),
           ch("The two lineages were isolated from each other in different places, which caused the two to diverge from a shared body shape.", "That would describe divergence and not the evolution of a similar shape in unrelated lineages.")],
          "Convergent evolution: similar selective pressures produce similar adaptations in different lineages.", difficulty="medium")

    rows = [("1 and 2", "Yes", "Yes"), ("1 and 3", "Yes", "No"), ("1 and 4", "No", "Not applicable")]
    B.mcq(T, "Four populations of a plant were crossed in the laboratory. The table shows whether each cross produced offspring and whether the offspring were fertile. According to the biological species concept, which conclusion is best supported by the data?",
          ch("Populations 1 and 2 are the same species, because only their cross produced viable, fertile offspring.", "Only the cross of populations 1 and 2 gave viable, fertile offspring."),
          [ch("Populations 1 and 3 are the same species, because their cross produced offspring, and that is the only criterion for a species.", "The offspring are sterile, so the populations are isolated post-zygotically."),
           ch("Populations 1 and 4 are the same species, because they did not produce offspring, which shows that they are alike in every trait.", "No offspring means that the populations are reproductively isolated."),
           ch("All four populations are the same species, because they were all crossed in the same laboratory with the same methods.", "The result of a cross, and not the place where it is made, determines whether populations are the same species.")],
          "The biological species concept requires viable, fertile offspring.",
          diagram=table(["Cross between populations", "Offspring produced", "Offspring fertile"], rows, caption="Crosses of four populations of a plant", row_headers=True), difficulty="hard")

    B.mcq(T, "Two populations of a fish were separated when a lake divided into two lakes. Many generations later the water levels rose and the lakes joined again. Which observation would show that the two populations had become separate species?",
          ch("The fish from the two populations no longer interbreed, or they produce offspring that are either not viable or not fertile.", "Reproductive isolation, with no gene flow between the populations, shows that speciation occurred."),
          [ch("The fish from the two populations interbreed freely and produce fertile offspring, which are found in both of the original lakes.", "Free interbreeding with fertile offspring shows that they are still one species."),
           ch("The fish from the two populations look different in color but they produce fertile offspring when they mate with each other.", "Differences in appearance do not make separate species if they interbreed and produce fertile offspring."),
           ch("The fish from the two populations are the same size as each other, though they lived for generations in separate lakes.", "Size alone does not show whether the populations are reproductively isolated.")],
          "Speciation is shown by reproductive isolation.", difficulty="hard")
