"""Unit 5, topic 5.4 Non-Mendelian Genetics (12 questions).

Required content (CED 2025-26): 5.4.A patterns of inheritance that do not follow Mendel's simple model: incomplete dominance (heterozygote intermediate), codominance (both alleles expressed, ABO blood
types), polygenic traits (many genes, continuous variation), pleiotropy (one gene, several traits), sex-linked genes on the X chromosome (more males than females express a recessive X-linked trait),
linked genes (close together on a chromosome, inherited together more often than expected; the recombination frequency is the percent of recombinant offspring and one map unit is 1% recombination),
and non-nuclear inheritance (mitochondrial and chloroplast DNA, passed on by the maternal parent). Suggested skills: 5.A, 6.D.
"""
import collections
import itertools
from fractions import Fraction as F

from lib import *


def frac_(x):
    return f"{x.numerator}/{x.denominator}"


def cross(g1, g2):
    """Offspring genotype counts for one gene. Genotypes are two-character strings such as "Aa". Order within a genotype is ignored."""
    c = collections.Counter()
    for a, b in itertools.product(g1, g2):
        c["".join(sorted((a, b)))] += 1
    return c


def build(B):
    T = 4

    B.mcq(T, "When a snapdragon plant with red flowers is crossed with a snapdragon plant with white flowers, all of the offspring have pink flowers. Which statement best explains this result?",
          ch("The two alleles show incomplete dominance, so the heterozygous offspring have a phenotype that is intermediate between those of the parents.", "In incomplete dominance the phenotype of the heterozygote is a blend of the two homozygous phenotypes."),
          [ch("The two alleles show codominance, so the heterozygous offspring have both red and white flowers on the same plant.", "In codominance, both alleles are fully expressed, as red and white patches. The offspring here are uniformly pink."),
           ch("The allele for red flowers is completely dominant, so the heterozygous offspring have the red phenotype of one parent.", "With complete dominance, the heterozygotes would be red and not pink."),
           ch("The color of the flowers is controlled by many genes, so the offspring have a mixture of the phenotypes of the two parents in a continuous range.", "A cross of two true-breeding plants with a single gene shows the intermediate phenotype from incomplete dominance. It does not need many genes.")],
          "Incomplete dominance produces a heterozygous phenotype that is intermediate between the two homozygous phenotypes.", difficulty="easy")

    # ABO: AB x O
    kids = cross(["A", "B"], ["i", "i"])
    assert kids == collections.Counter({"Ai": 2, "Bi": 2})
    B.mcq(T, "A man with blood type AB and a woman with blood type O have children. The alleles are IA, IB and i, where IA and IB are codominant and i is recessive. Which blood types are possible in their children?",
          ch("Only type A and type B, because each child receives either IA or IB from the father and the allele i from the mother", "The father passes on IA or IB, and the mother passes on i, so the genotypes are IAi (type A) or IBi (type B)."),
          [ch("Type A, type B, type AB and type O, because each parent can pass on either of its alleles to a child with equal probability", "The woman has type O, so she is ii and passes on only the i allele. Type AB and type O are not possible."),
           ch("Only type AB, because the father has type AB and the codominant alleles of the father are both expressed in all of the children", "Each child receives only one of the two alleles of the father."),
           ch("Only type O, because the recessive allele of the mother is expressed in each of the children that she has with this father", "The alleles IA and IB are not recessive, so a child with one of them is not type O.")],
          "Codominant alleles are both expressed in the heterozygote; each child receives one allele from each parent.", difficulty="medium")

    B.mcq(T, "A person with blood type AB has red blood cells that have both the A antigen and the B antigen on their surface. Which statement best explains this?",
          ch("The alleles for A and B are codominant, so both alleles are fully expressed in a person who inherits one of each.", "Codominance means that both alleles of the heterozygote are expressed at the same time and not blended."),
          [ch("The alleles for A and B show incomplete dominance, so the antigens of the person are an intermediate form between A and B.", "In incomplete dominance an intermediate phenotype is seen. Here, the two separate antigens are both present."),
           ch("The allele for A is dominant over the allele for B, so the antigen B is made only in the cells that do not make the antigen A.", "If one allele were dominant, only one antigen would be present."),
           ch("A new mutation occurred in the cells of the person, so that a new allele makes the second antigen in addition to the first one.", "A person with type AB inherited an allele for each of the two antigens from the parents. A new mutation is not needed.")],
          "In codominance, both alleles are expressed in the heterozygote.", difficulty="easy")

    # X-linked: carrier mother x normal father, sons
    xx = collections.Counter()
    for m, f in itertools.product(["XB", "Xb"], ["XB", "Y"]):
        xx[(m, f)] += 1
    sons = [(m, f) for (m, f) in xx if f == "Y"]
    affected_sons = [(m, f) for (m, f) in sons if m == "Xb"]
    assert len(sons) == 2 and len(affected_sons) == 1
    p_son = F(len(affected_sons), len(sons))
    p_any = F(len(affected_sons), 4)
    assert p_son == F(1, 2) and p_any == F(1, 4)
    B.mcq(T, "Red-green color blindness is caused by a recessive allele on the X chromosome. A woman who is a carrier $(X^B X^b)$ and a man with normal color vision $(X^B Y)$ have a child. What is the probability that a son of this couple is color-blind?",
          ch(f"{frac_(p_son)}, because the son receives his X chromosome from his mother and half of her X chromosomes carry the recessive allele", "A son receives the Y chromosome from his father and one X chromosome from his mother, who passes on $X^b$ with a probability of 1/2.", 0.5),
          [ch(f"{frac_(p_any)}, because the probability that one of the four possible children is a color-blind son is one fourth", "1/4 is the probability that a child (of either sex) is a color-blind son. The question asks about a son.", 0.25),
           ch("0, because the father has normal color vision and so he cannot have a son with a recessive trait that is X-linked", "The son receives his X chromosome from his mother and not from his father.", 0.0),
           ch("1, because the recessive allele is on the X chromosome and every son has the X chromosome from the carrier mother", "The mother has one normal X chromosome and one with the recessive allele and so she passes on each with equal probability.", 1.0)],
          "A son receives his X chromosome from his mother; a carrier mother passes the recessive allele to half of her sons.", difficulty="medium")

    B.mcq(T, "Recessive X-linked disorders, such as hemophilia, are more common in males than in females. Which statement best explains this?",
          ch("Males have only one X chromosome, so a single recessive allele on it is expressed, while a female needs two copies of the recessive allele.", "A male has one X chromosome and no second allele that can mask the recessive allele."),
          [ch("Males have two X chromosomes, so the recessive alleles on both of them are more likely to be expressed than the alleles in females.", "Females have two X chromosomes and males have one X and one Y."),
           ch("Males make more of the proteins that are coded for by genes on the X chromosome, so the recessive alleles are expressed more strongly.", "The difference is in the number of copies of the allele and not in the amounts of protein that are made."),
           ch("Males receive the X chromosome from the father, so the fathers with the recessive allele always pass the disorder to their sons.", "A son receives his X chromosome from his mother and the Y chromosome from his father.")],
          "Males express any allele on their single X chromosome.", difficulty="medium")

    B.mcq(T, "A mutation in a gene in the mitochondrial DNA causes a disorder. Which pattern of inheritance is expected?",
          ch("All of the children of an affected mother have the mutation, and none of the children of an affected father inherit it.", "Mitochondria in the zygote come from the egg, so mitochondrial DNA is inherited from the mother."),
          [ch("All of the children of an affected father have the mutation, and none of the children of an affected mother inherit it.", "The sperm contributes almost no mitochondria to the zygote."),
           ch("Half of the sons of an affected mother have the mutation, and none of the daughters of an affected mother inherit it.", "The pattern of mitochondrial inheritance is the same in sons and daughters, as they all receive their mitochondria from the egg."),
           ch("Half of the children of each affected parent have the mutation, as the alleles of the two parents separate in meiosis in the usual way.", "Mitochondrial genes are not located on the nuclear chromosomes that segregate in meiosis.")],
          "Genes in mitochondrial and chloroplast DNA are inherited from the maternal parent.", difficulty="medium")

    B.mcq(T, "The heights of adults in a large population show a continuous range of values and the distribution is bell-shaped. Which statement best explains this variation?",
          ch("Height is a polygenic trait, so many genes each add a small effect and the environment also influences the phenotype.", "Polygenic traits are controlled by many genes and show continuous variation."),
          [ch("Height is controlled by a single gene with two alleles, so the phenotypes are in a 3:1 ratio of tall to short people.", "A single gene with two alleles gives two discrete phenotypes and not a continuous range."),
           ch("Height is controlled by a single gene that has codominant alleles, so each person has both the tall and the short phenotype.", "Codominance does not produce a continuous range of values."),
           ch("Height is controlled by genes on the Y chromosome, so the range in the population depends only on the number of males.", "Both males and females show a range of heights, and the Y chromosome is found only in males.")],
          "Polygenic inheritance and environmental effects produce continuous variation.", difficulty="medium")

    B.mcq(T, "The allele that causes sickle cell disease changes the structure of hemoglobin, and it leads to anemia, pain, damage to organs, and a greater resistance to malaria. Which term describes a single gene that affects several traits?",
          ch("Pleiotropy, because one gene has effects on several different characteristics of the organism", "Pleiotropy is the situation in which a single gene affects more than one trait."),
          [ch("Polygenic inheritance, because the several traits that are affected are controlled by many genes in the organism", "Polygenic inheritance describes one trait that is influenced by many genes. This is the reverse of the situation here."),
           ch("Incomplete dominance, because the effects on the traits are intermediate between the effects of the two homozygotes", "Incomplete dominance describes the phenotype of the heterozygote for one trait."),
           ch("Nondisjunction, because the several traits are affected by the failure of the chromosomes to separate in meiosis", "Sickle cell disease is caused by a change in the sequence of the gene and not by a change in the number of chromosomes.")],
          "Pleiotropy: one gene affects several traits.", difficulty="medium")

    # Recombination frequency
    parental = {"AB": 460, "ab": 440}
    recomb = {"Ab": 55, "aB": 45}
    total = sum(parental.values()) + sum(recomb.values())
    rf = sum(recomb.values()) / total * 100
    assert total == 1000 and rf == 10.0
    rows = [(k, str(v), "Parental") for k, v in parental.items()] + [(k, str(v), "Recombinant") for k, v in recomb.items()]
    B.mcq(T, "A heterozygous fly (AaBb, with A and B on one chromosome) is crossed with a fly that is homozygous recessive (aabb). The table shows the 1,000 offspring. What is the distance between the two genes in map units (1% recombination = 1 map unit)?",
          ch(f"{rf:.0f} map units, because 100 of the 1,000 offspring (55 + 45) are recombinants, and 100/1,000 is 10%", "Recombination frequency = recombinants / total offspring = 100/1,000 = 10%, which is 10 map units.", rf),
          [ch(f"{100 - rf:.0f} map units, because 900 of the 1,000 offspring show the parental combinations of the alleles", "900/1,000 is the frequency of the parental types. The map distance is based on the recombinants.", 100 - rf),
           ch("50 map units, because the genes assort independently and so half of the offspring are recombinants", "If the genes assorted independently, 50% of the offspring would be recombinants. The data show only 10%.", 50.0),
           ch("5 map units, because only one of the two kinds of recombinant offspring is counted in the calculation of the distance", "Both kinds of recombinant offspring are counted: (55 + 45)/1,000.", 5.0)],
          "Map distance (in map units) = percent of recombinant offspring.",
          diagram=table(["Offspring genotype", "Number of offspring", "Class"], rows, caption="Offspring of a test cross of two linked genes", row_headers=True), difficulty="hard")

    # Gene order
    ab, bc, ac = 8, 12, 20
    assert ab + bc == ac
    rows2 = [("A and B", str(ab)), ("B and C", str(bc)), ("A and C", str(ac))]
    B.mcq(T, "Three linked genes (A, B and C) are on the same chromosome. The table shows the recombination frequencies between each pair of genes. What is the order of the genes on the chromosome?",
          ch("A, B, C, because the distance between A and C is the sum of the distances between A and B and between B and C", f"{ab} + {bc} = {ac}, so B is between A and C."),
          [ch("A, C, B, because the genes that are the closest together are A and C", f"A and C are the genes that are the furthest apart ({ac} map units)."),
           ch("B, A, C, because the genes that are the furthest apart are the genes B and C and so they are at the ends", f"The greatest distance is between A and C ({ac} map units), so those genes are at the two ends."),
           ch("It cannot be determined, because the recombination frequencies do not show on which chromosome the genes are located", "The sum of the two shorter distances equals the longest distance, which shows the order of the genes.")],
          "The two genes that are the furthest apart are at the ends of the map, and the third gene is between them.",
          diagram=table(["Pair of genes", "Recombination frequency (%)"], rows2, caption="Recombination frequencies for three linked genes", row_headers=True), difficulty="hard")

    # Drosophila reciprocal: white-eyed female x red-eyed male
    kids = collections.Counter()
    for m, f in itertools.product(["Xw", "Xw"], ["XW", "Y"]):
        sex = "male" if f == "Y" else "female"
        eyes = "white" if (sex == "male" and m == "Xw") else ("red" if "XW" in (m, f) else "white")
        kids[(sex, eyes)] += 1
    assert kids == collections.Counter({("female", "red"): 2, ("male", "white"): 2})
    B.mcq(T, "In fruit flies, the allele for white eyes is recessive and is on the X chromosome. A white-eyed female is crossed with a red-eyed male. Which phenotypes are expected in the offspring?",
          ch("All of the daughters have red eyes and all of the sons have white eyes, because each son receives his X chromosome from his mother.", "Daughters receive the X chromosome with the dominant allele from the father, and sons receive the X chromosome with the recessive allele from the mother."),
          [ch("All of the offspring have red eyes, because the allele for red eyes of the father is dominant and so it is expressed in both sexes.", "Sons receive their X chromosome from the mother, who has only the recessive allele, so the sons have white eyes."),
           ch("Half of the daughters and half of the sons have white eyes, because each parent passes on one of its two alleles at random.", "The mother is homozygous recessive and so she passes only the recessive allele. The pattern depends on the sex of the offspring."),
           ch("All of the daughters have white eyes and all of the sons have red eyes, because each son receives his X chromosome from his father.", "A son receives the Y chromosome from his father and the X chromosome from his mother.")],
          "In a cross of a recessive X-linked trait in the mother with the dominant trait in the father, the sons show the trait of the mother.", difficulty="hard")

    # Incomplete dominance ratio
    pink = cross(["R", "W"], ["R", "W"])
    assert pink == collections.Counter({"RR": 1, "RW": 2, "WW": 1})
    B.mcq(T, "Two snapdragon plants with pink flowers (RW) are crossed. Red flowers (RR) and white flowers (WW) show incomplete dominance. What is the expected ratio of red to pink to white flowers among the offspring?",
          ch("1 red : 2 pink : 1 white, because the phenotype ratio is the same as the genotype ratio when there is incomplete dominance", "The genotypes are in a ratio of 1 RR : 2 RW : 1 WW, and each genotype has its own phenotype."),
          [ch("3 red : 1 white, because the allele for red flowers is dominant over the allele for white flowers in the offspring", "This ratio is for complete dominance. In incomplete dominance the heterozygote is pink."),
           ch("All pink, because both of the parents have pink flowers and so all of their offspring have the same phenotype as the parents", "Heterozygous parents produce gametes with either allele, and so the three genotypes appear in the offspring."),
           ch("1 red : 1 pink : 1 white, because there are three phenotypes and each one is equally likely in the offspring of this cross", "The pink phenotype is expected to be twice as common as each of the others, as the RW genotype can form in two ways.")],
          "With incomplete dominance, a cross of two heterozygotes gives a 1:2:1 ratio of both genotypes and phenotypes.", difficulty="medium")
