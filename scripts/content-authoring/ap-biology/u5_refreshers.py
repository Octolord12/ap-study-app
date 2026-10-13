"""Writes content/ap-biology/refreshers/unit-5.json (five refreshers, one per topic). Layout: ### The idea, ### Key facts, ### Watch out for, ### Worked example.
Facts are the CED's required content for each topic; every number in a worked example is asserted. Avoid a lone dollar sign, single-asterisk italics and
em dashes. Edit this script, not the JSON. Run: python3 u5_refreshers.py"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import refreshers_lib

# worked-example numbers
n_two = 8
assert (n_two // 2, n_two // 2 * 2, n_two // 2) == (4, 8, 4)  # 2n = 8: 4 chromosomes per cell after meiosis I, 8 chromatids in the cell before it
assert 2 ** 3 == 8 and 2 ** 23 == 8_388_608
obs, exp = [140, 60], [150, 50]
chi = sum((o - e) ** 2 / e for o, e in zip(obs, exp))
assert round(chi, 2) == 2.67 and chi < 3.84
assert (40 / 400) * 100 == 10.0
assert round((20 - 12) / 12 * 100, 1) == 66.7

ENTRIES = [
("meiosis", r"""
### The idea
Sexually reproducing organisms make gametes by meiosis. A diploid cell copies its DNA once and then divides twice, which makes four haploid cells. Meiosis I separates the homologous chromosomes, and meiosis II separates the sister chromatids.

### Key facts
- **Before meiosis I** the DNA is replicated, so each chromosome has two sister chromatids.
- **Prophase I:** homologous chromosomes pair up (synapsis), and chiasmata may form where non-sister chromatids cross over.
- **Metaphase I:** the homologous pairs line up at the equator. **Anaphase I:** the homologous chromosomes separate, and the sister chromatids stay attached. **Telophase I:** two haploid cells result.
- **Meiosis II:** the sister chromatids separate, and four haploid cells result, each with unduplicated chromosomes.
- Mitosis and meiosis both use a spindle. They differ in the **number of cells** (2 compared with 4) and the **genetic content** of the cells (identical diploid cells compared with different haploid cells).

### Watch out for
Mixing up the two divisions. Homologous chromosomes separate in meiosis **I**, and sister chromatids separate in meiosis **II**. Also, a cell is haploid when it has one chromosome of each pair, even if each chromosome still has two chromatids.

### Worked example
Prompt: "A diploid cell has 8 chromosomes. How many chromosomes does each cell have after meiosis I and after meiosis II?"

Meiosis I separates the homologous chromosomes, so each cell has 8 / 2 = 4 chromosomes (each with two chromatids). Meiosis II separates the sister chromatids and does not change the number of chromosomes, so each of the four cells has 4 chromosomes.
"""),
("meiosis-and-genetic-diversity", r"""
### The idea
Meiosis and fertilization mix alleles in many ways, so the offspring of two parents differ from each other. If the chromosomes separate incorrectly, the gametes do not have the right number of chromosomes.

### Key facts
- **Crossing over** in prophase I exchanges segments between non-sister chromatids of homologous chromosomes, which makes new combinations of alleles.
- **Independent assortment:** each homologous pair lines up in metaphase I in a random orientation, so the maternal and paternal chromosomes are mixed in the gametes. With n pairs there are $2^n$ combinations.
- **Random fertilization:** any sperm can fuse with any egg.
- **Nondisjunction** is the failure of homologous chromosomes (meiosis I) or sister chromatids (meiosis II) to separate. It makes gametes with an extra chromosome ($n + 1$) or a missing chromosome ($n - 1$). Trisomy 21 is an example.

### Watch out for
Nondisjunction in meiosis I makes **all four** gametes abnormal, and nondisjunction in meiosis II makes **two** abnormal gametes and two normal ones. Also, crossing over does not change the number of chromosomes. It changes which alleles are together.

### Worked example
Prompt: "An organism has 3 pairs of chromosomes. How many combinations of chromosomes are possible in its gametes if you ignore crossing over?"

Each pair has 2 possible orientations, and the pairs are independent, so there are $2^3 = 8$ combinations. For humans, with 23 pairs, there are $2^{23} = 8{,}388{,}608$ combinations.
"""),
("mendelian-genetics", r"""
### The idea
Mendel's model explains how traits are passed on: each individual has two alleles of a gene, one from each parent, and a dominant allele hides a recessive allele in the heterozygote. Probability rules let you predict the offspring of a cross, and a chi-square test tells you whether the data match the prediction.

### Key facts
- **Rule of multiplication:** the probability that independent events all occur is the product of their probabilities. **Rule of addition:** the probability that one of several mutually exclusive events occurs is the sum.
- A **monohybrid cross** of two heterozygotes gives a 3:1 ratio of phenotypes. A **dihybrid cross** (two genes on different chromosomes) gives 9:3:3:1.
- A **test cross** of an individual with a dominant phenotype with a homozygous recessive reveals its genotype.
- **Independent assortment:** genes on different chromosomes are sorted independently, because the homologous pairs line up at random in metaphase I.
- **Chi-square:** $\chi^2 = \sum \frac{(o - e)^2}{e}$, with degrees of freedom equal to the number of categories minus 1. If $\chi^2$ is less than the critical value (p = 0.05), you do not reject the null hypothesis.

### Watch out for
"Fail to reject" is not "proved." A small chi-square means that the difference can be due to chance. Also, calculate the expected counts from the total number of offspring, and not from the number in one category.

### Worked example
Prompt: "A 3:1 ratio is expected. Among 200 offspring, 140 show the dominant phenotype and 60 show the recessive phenotype. Is the difference significant? (The critical value for 1 degree of freedom is 3.84.)"

The expected counts are 150 and 50. $\chi^2 = (140 - 150)^2/150 + (60 - 50)^2/50 = 0.67 + 2.00 = 2.67$. This is less than 3.84, so the null hypothesis is not rejected, and the difference could be due to chance.
"""),
("non-mendelian-genetics", r"""
### The idea
Many traits do not follow the simple pattern of one gene with a dominant and a recessive allele. Some alleles blend or are both expressed, some traits depend on many genes, and the position of a gene on a chromosome can change how it is inherited.

### Key facts
- **Incomplete dominance:** the heterozygote has an intermediate phenotype (red x white gives pink, and a cross of two pink plants gives 1 red : 2 pink : 1 white). **Codominance:** both alleles are expressed in the heterozygote (type AB blood).
- **Polygenic traits** depend on many genes and show continuous variation. **Pleiotropy:** one gene affects several traits.
- **Sex-linked genes** on the X chromosome: a male has one X chromosome, so a single recessive allele is expressed. A son receives his X chromosome from his mother. Reciprocal crosses give different results.
- **Linked genes** are close together on a chromosome and are inherited together more often than expected. The **recombination frequency** is the percent of recombinant offspring, and 1% is 1 **map unit**. A frequency near 50% means that the genes assort independently.
- **Non-nuclear inheritance:** genes in mitochondrial and chloroplast DNA are passed on by the maternal parent.

### Watch out for
Parental types are the **more common** classes of offspring when genes are linked, and recombinants are the **less common** classes. Also, a father cannot pass an X-linked allele to his son.

### Worked example
Prompt: "In a test cross of two linked genes, 40 of 400 offspring have a new combination of traits. What is the distance between the genes?"

The recombination frequency is 40 / 400 x 100 = 10%, so the genes are 10 map units apart. If they were on different chromosomes, about 50% of the offspring would be recombinants.
"""),
("environmental-effects-on-phenotype", r"""
### The idea
The phenotype of an organism depends on its genotype and on its environment. Two organisms with the same genotype can look or behave differently because they developed in different conditions.

### Key facts
- **Examples:** the color of hydrangea flowers depends on the pH of the soil, the fur of the Himalayan rabbit is dark where it is cool, and the sex of some reptiles depends on the temperature of the egg. Nutrition affects height, and identical twins can differ.
- The environment often acts through **gene expression** or the **activity of an enzyme.** The DNA sequence does not change. Seasonal changes in the coat of an Arctic fox are an example.
- A **common-environment** experiment (raising organisms from different populations in the same conditions) separates genetic effects from environmental effects. Raising **genetically identical** organisms in different conditions shows environmental effects.
- The effect of the environment can **depend on the genotype:** two genotypes may respond differently to the same change.

### Watch out for
Saying that the environment "changes the genes." Usually the environment changes how the genes are expressed. Also, a difference between two natural populations can be genetic, environmental or both, so you need a controlled comparison.

### Worked example
Prompt: "Plants of one genotype have a mean height of 12 cm at 15 degrees Celsius and 20 cm at 25 degrees Celsius. What is the percent increase, and what does it show?"

The increase is (20 - 12) / 12 x 100 = 66.7%. Because the genotype is the same, the difference in height is caused by the environment (temperature).
"""),
]

refreshers_lib.write("ap-biology", 5, ENTRIES)
