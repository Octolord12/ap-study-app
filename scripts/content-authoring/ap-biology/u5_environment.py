"""Unit 5, topic 5.5 Environmental Effects on Phenotype (7 questions).

Required content (CED 2025-26): 5.5.A the phenotype of an organism is determined by its genotype and by the environment; the same genotype can give different phenotypes in different environments
(hydrangea flower color and soil pH, the Himalayan rabbit and temperature, nutrition and height, identical twins); some environmental effects are on gene expression (seasonal changes of coat color).
Suggested skills: 1.C, 4.B, 5.A, 6.E.
"""
from lib import *


def build(B):
    T = 5

    B.mcq(T, "Two genetically identical twins are raised in different homes. As adults, one is taller than the other. Which statement best explains this difference?",
          ch("The phenotype of a person depends on the environment as well as on the genotype, so differences such as nutrition can result in different heights.", "Genetically identical individuals can differ in phenotype because of differences in the environment."),
          [ch("The twins must have different DNA sequences, because genetically identical individuals always show the same phenotype in every kind of environment in which they live.", "The twins are genetically identical. The same genotype can give different phenotypes."),
           ch("Height is not influenced by genes, because the twins have a different height and so the genotype has no effect on the phenotype.", "Genes influence height and the environment influences it too."),
           ch("The twins had nondisjunction in meiosis, because one of the twins has a different number of chromosomes from the number in the other.", "Identical twins arise from the division of one zygote and are not formed by separate gametes.")],
          "Phenotype is determined by genotype and by the environment.", difficulty="easy")

    B.mcq(T, "Hydrangea plants with the same genotype produce blue flowers in acidic soil and pink flowers in basic soil. Which statement is best supported by this observation?",
          ch("The environment, in this case the pH of the soil, can influence the phenotype produced by a genotype.", "The same genotype gives different flower colors in different soils, so the environment affects the phenotype."),
          [ch("The plants in the two soils have different alleles for flower color, because a single genotype can only give a single phenotype.", "A single genotype can give different phenotypes in different environments."),
           ch("The color of flowers is inherited only through the cytoplasm, because the soil changes the alleles that are present in the nucleus.", "Soil pH does not change the alleles in the nucleus."),
           ch("The pH of the soil mutates the DNA of the plants, because the flower color is changed in the plants that grow in acidic soil.", "A change in flower color with the environment is not evidence for a change in the DNA sequence.")],
          "The same genotype can produce different phenotypes in different environments.", difficulty="medium")

    B.mcq(T, "The fur of a Himalayan rabbit is white on most of its body and dark on its ears, feet and nose, which are cooler. Researchers shave a patch of fur on the back of a rabbit and keep the patch cold, and the new fur that grows is dark. Which statement best explains these observations?",
          ch("The enzyme that produces the dark pigment is active only at lower temperatures, so the temperature of the tissue affects the phenotype.", "Temperature affects the activity of the pigment-making enzyme, which results in a change in the phenotype of the fur."),
          [ch("The cells in the back of the rabbit lost the gene for the dark pigment, because the new fur from the cold patch has a different DNA sequence.", "The cold patch did not change the DNA sequence. The cells have the same genes in all of the body."),
           ch("The cold caused a mutation that changed the genotype, because the dark fur that grew is different from the fur that was shaved.", "The cells of the rabbit have the same genotype in all places. The temperature affects how the genotype is expressed."),
           ch("The rabbit has different genes in the cooler parts of the body, because the dark fur is only found on the ears, feet and nose.", "All of the body cells of the rabbit have the same genes. The difference in phenotype results from the difference in temperature.")],
          "Temperature affects the activity of an enzyme, and so it affects the phenotype produced by the same genotype.", difficulty="medium")

    # Genotype x environment bar graph
    g1_cold, g1_warm, g2_cold, g2_warm = 12.0, 20.0, 14.0, 15.0
    inc1 = pct_change(g1_cold, g1_warm)
    inc2 = pct_change(g2_cold, g2_warm)
    assert round(inc1, 1) == 66.7 and round(inc2, 1) == 7.1
    graph_ = bars("Genotype", "Mean height of plants (cm)", 25, ["Genotype 1", "Genotype 2"],
                  [{"values": [g1_cold, g2_cold], "label": "15 °C", "color": "blue"}, {"values": [g1_warm, g2_warm], "label": "25 °C", "color": "red"}],
                  alt=f"Bar graph. Genotype 1: mean height {fix(g1_cold, 0)} cm at 15 degrees Celsius and {fix(g1_warm, 0)} cm at 25 degrees Celsius. Genotype 2: {fix(g2_cold, 0)} cm at 15 degrees Celsius and {fix(g2_warm, 0)} cm at 25 degrees Celsius.")
    B.mcq(T, "Researchers grew plants of two genotypes at two temperatures and measured their heights. Which conclusion is best supported by the data in the graph?",
          ch(f"Temperature changes the height of genotype 1 a lot (about {inc1:.0f}% taller) but of genotype 2 very little (about {inc2:.0f}%), so the effect depends on the genotype.", f"Genotype 1 increases from {fix(g1_cold, 0)} to {fix(g1_warm, 0)} cm, and genotype 2 increases from {fix(g2_cold, 0)} to {fix(g2_warm, 0)} cm."),
          [ch("Temperature has the same effect on both genotypes, because the plants of each genotype are taller at 25 °C than at 15 °C.", "The sizes of the increases are very different between the two genotypes."),
           ch("The height of the plants is determined only by the genotype, because the plants of the two genotypes differ in height at 15 °C.", "The height of genotype 1 differs between the temperatures, so the environment also influences the phenotype."),
           ch("The height of the plants is determined only by the temperature, because the plants of genotype 1 are taller at 25 °C than at 15 °C, and so the genotype is not important.", "The two genotypes respond differently to the temperature, so the genotype is also important.")],
          "The phenotype depends on the genotype, on the environment, and on how the genotype responds to the environment.", diagram=graph_, difficulty="hard")

    B.mcq(T, "In some reptiles, eggs that are incubated at a lower temperature develop into males and eggs that are incubated at a higher temperature develop into females. Which statement best describes this observation?",
          ch("The sex of the offspring is influenced by the temperature of the environment during development, which is an environmental effect on the phenotype.", "In these reptiles the temperature during incubation determines the sex of the offspring."),
          [ch("The sex of the offspring is determined only by the sex chromosomes that each egg receives, which are not affected by the environment.", "In these reptiles the temperature influences the sex of the offspring."),
           ch("The temperature changes the DNA sequence of the eggs, which results in new alleles for sex that are inherited by the offspring.", "Temperature affects how the genes are expressed during development. It does not change the DNA sequence in this way."),
           ch("The temperature has no effect on the offspring, because all of the eggs that a female lays have the same genotype as each other.", "Eggs with the same genotype can develop differently at different temperatures.")],
          "The environment can determine a trait such as the sex of the offspring.", difficulty="medium")

    B.mcq(T, "A student wants to know whether a difference in height between plants from a high-elevation population and plants from a low-elevation population results from genes or from the environment. Which experiment would best answer this question?",
          ch("Grow seeds from both populations together in the same garden under the same conditions, and then compare the heights of the plants.", "If the plants differ when they grow in the same environment, the difference is likely to be caused by genetic differences."),
          [ch("Measure the heights of more plants in each of the two populations where they grow naturally and then compare the average heights.", "The plants grow in different environments, so differences might still result from the environment."),
           ch("Grow seeds from the high-elevation population in the garden and the seeds from the low-elevation population in their natural habitat.", "The two groups would be in different environments and so the experiment cannot separate the effects of the environment and the genotype."),
           ch("Compare the DNA of one plant from each population with the DNA of a plant from a third species that grows in the same area.", "The question is about the two populations, and a plant of a different species is not an appropriate comparison.")],
          "To separate genetic and environmental effects, compare organisms from different populations in the same environment.", difficulty="hard")

    B.mcq(T, "The Arctic fox has a brown coat in summer and a white coat in winter. The change is triggered by the length of the day and the temperature. Which statement best explains this change?",
          ch("Signals from the environment change which genes are expressed in the cells of the fox, so the same genotype produces different phenotypes in different seasons.", "Environmental cues can alter gene expression, and this changes the phenotype without a change in the DNA sequence."),
          [ch("The DNA sequence of the fox mutates each autumn and then mutates back in spring, so the genes for the color of the coat are changed twice each year.", "Gene expression changes with the environment while the DNA sequence stays the same."),
           ch("The fox has two different genotypes, one for each season, so the coat color is the result of the genotype that is present at that time.", "The fox has one genotype, which gives two phenotypes depending on the environment."),
           ch("The change in the color of the coat is random, so the environment has no effect on the genes that are expressed in the fox.", "The change is triggered by signals in the environment, such as the length of the day, and it is not random.")],
          "The environment can change gene expression and so change the phenotype.", difficulty="medium")
