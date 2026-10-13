"""Writes content/ap-biology/refreshers/unit-4.json (six refreshers, one per topic). Layout: ### The idea, ### Key facts, ### Watch out for, ### Worked example.
Facts are the CED's required content for each topic; every number in a worked example is asserted. Avoid a lone dollar sign, single-asterisk italics and
em dashes. Edit this script, not the JSON. Run: python3 u4_refreshers.py"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import refreshers_lib

# worked-example numbers
assert 1 * 20 * 50 == 1000
assert (20 + 8 + 6 + 6) / 200 * 100 == 20.0 and round(20 / 200 * 24, 1) == 2.4

ENTRIES = [
("cell-communication", r"""
### The idea
Cells in a multicellular organism, and cells in a population of single-celled organisms, coordinate what they do by communicating. They can touch each other directly, or one cell can release a chemical signal that reaches other cells. The signal can act on neighbors or travel a long way.

### Key facts
- **Direct contact:** cells interact through contact, as immune cells do (for example, a helper T cell and an antigen-presenting cell).
- **Local regulators** act over short distances on cells near the signaling cell. Neurotransmitters, morphogens in embryos and signals in quorum sensing are examples.
- **Long-distance signals,** such as hormones, are released by one cell type and travel to target cells of another type, for example insulin and the sex hormones.
- **Quorum sensing:** bacteria release a signal, so the concentration of the signal tells the cells how many of them are present, and gene expression changes when it passes a threshold.
- A cell responds only if it has the receptor for the signal.

### Watch out for
Treating "short distance" and "long distance" as a difference in the kind of molecule. Both use chemical signals. What differs is how far they travel and which cells they reach. Also, a hormone reaches every tissue in the blood, but only target cells respond.

### Worked example
Prompt: "Explain why a hormone in the blood affects only some cells."

The hormone is carried to all the tissues, but only the target cells have a receptor with a ligand-binding domain that recognizes it. Cells without the receptor cannot detect the hormone, so they do not respond.
"""),
("introduction-to-signal-transduction", r"""
### The idea
A cell must change an outside signal into a response inside the cell. This is signal transduction. A chemical messenger, the ligand, binds to a receptor protein, and a series of steps inside the cell relays the message, often making it stronger, until the cell makes a response.

### Key facts
- **Ligand and receptor:** the ligand-binding domain of a receptor recognizes a specific chemical messenger, which can be a peptide or a small molecule. G protein-coupled receptors are one example.
- Receptors can be on the **cell surface** or in the **cytoplasm or nucleus**. A ligand that can cross the membrane, such as a steroid hormone, can bind an internal receptor.
- After the ligand binds, the **intracellular domain** of the receptor changes shape and starts the transduction.
- **Relay and amplification:** enzymes and second messengers, such as cAMP, pass the signal on and amplify it. Many pathways use **phosphorylation cascades**, in which one kinase activates the next.
- A **ligand-gated channel** opens or closes when a ligand binds.

### Watch out for
Confusing the ligand with the second messenger. The ligand is outside the cell and binds the receptor. The second messenger is made inside the cell. When you count amplification, multiply the numbers at each step.

### Worked example
Prompt: "One ligand activates one receptor. Each receptor activates 20 relay proteins, and each relay protein activates 50 enzyme molecules. How many enzyme molecules does one ligand activate?"

The numbers multiply at each step: 1 x 20 x 50 = 1,000 enzyme molecules. This is amplification: one signal molecule produces a large response.
"""),
("signal-transduction-pathways", r"""
### The idea
The end of a signal transduction pathway is a response, and the response can be large and varied. Because the pathway has many components, a change to any one of them, such as a mutation or a drug, can change the response.

### Key facts
- **Responses:** changes in gene expression and in cell function, which may alter the phenotype, or apoptosis, which is programmed cell death.
- Examples: epinephrine stimulates the breakdown of glycogen in mammals, yeast mating pheromones turn on mating genes, ethylene changes enzyme production as fruit ripens, and HOX genes regulate body plans in embryos.
- A **mutation in any domain of a receptor** or in any component of the pathway can change the downstream steps.
- **Chemicals can activate or inhibit** a pathway by interacting with any component. A molecule shaped like the ligand can block the receptor.
- A pathway component that is **always active** can produce a response without a signal.

### Watch out for
Assuming that every mutation switches a pathway off. A mutation can also switch it on all the time. Work out which step is changed and what that step does to the ones after it.

### Worked example
Prompt: "A mutation makes a protein kinase near the start of a growth-factor pathway active all the time. Predict the effect."

The kinase keeps activating the components after it, whether or not the growth factor has bound the receptor. The cell therefore makes the response, such as cell division, without a signal, which could lead to uncontrolled division.
"""),
("feedback", r"""
### The idea
Organisms keep their internal conditions within a narrow range by feedback. In negative feedback, a response reduces the change that caused it and returns the system to its set point. In positive feedback, a response makes the change bigger.

### Key facts
- **Negative feedback** reduces the initial stimulus and returns the system to its set point. Example: insulin and glucagon regulating blood sugar. It works at molecular, cellular and organismal levels.
- **Positive feedback** amplifies a response and moves the variable further from the starting set point. Examples: the onset of labor, lactation and the ripening of fruit.
- Positive feedback needs an end point or another mechanism to stop it. Negative feedback is what maintains homeostasis.
- To classify a mechanism, ask what the response does to the original stimulus: it reduces it (negative) or increases it (positive).

### Watch out for
Calling a mechanism "positive" because the response seems good for the body. The word describes what the response does to the stimulus and not whether the outcome is helpful.

### Worked example
Prompt: "After a meal, blood glucose rises, insulin is released, cells take up glucose and the concentration falls. Which kind of feedback is this?"

It is negative feedback, because the response (the uptake of glucose after the release of insulin) reduces the stimulus (the high concentration of glucose) and returns the concentration toward its set point.
"""),
("cell-cycle", r"""
### The idea
The cell cycle is the ordered series of events by which a eukaryotic cell grows and divides. It has a long phase called interphase, when the cell grows and copies its DNA, followed by mitosis, which divides the nucleus, and cytokinesis, which divides the cytoplasm. Mitosis gives two daughter cells that are genetically identical.

### Key facts
- **Interphase:** G1 (the cell is active and duplicates organelles), S (DNA replicates and each chromosome has two sister chromatids joined at a centromere), G2 (protein synthesis, ATP production, centrosomes replicate).
- **G0:** a stage in which a cell does not divide. Some cells can re-enter the cycle when they receive the right cues.
- **Mitosis:** prophase (chromatids condense, spindle forms, centrosomes move to the poles), metaphase (chromosomes line up at the equator), anaphase (sister chromatids separate), telophase (spindle breaks down, nuclear envelope re-forms).
- **Cytokinesis:** a cleavage furrow in animal cells and a cell plate in plant cells.
- Mitosis is used for growth, tissue repair and asexual reproduction.
- Count chromosomes by centromeres: replication makes chromatids, not chromosomes.

### Watch out for
Mixing up chromosomes and chromatids. A replicated chromosome with two chromatids is still one chromosome until the chromatids separate in anaphase.

### Worked example
Prompt: "In 200 onion root-tip cells, 20 are in prophase, 8 in metaphase, 6 in anaphase and 6 in telophase. What percent are in mitosis, and, for a 24-hour cycle, how long is prophase?"

Cells in mitosis = 20 + 8 + 6 + 6 = 40, and 40 / 200 x 100 = 20 percent. Prophase takes (20 / 200) x 24 = 2.4 hours.
"""),
("regulation-of-cell-cycle", r"""
### The idea
A cell does not simply run through the cell cycle. Internal controls called checkpoints check whether conditions are right before the cell goes on to the next stage. Proteins called cyclins, working with cyclin-dependent kinases (CDKs), drive the cycle. When regulation fails, the result can be cancer or the cell can die by apoptosis.

### Key facts
- **Checkpoints** are internal controls that regulate progress through the cell cycle. They check, for example, that DNA is undamaged and fully replicated before mitosis, and that the chromosomes are attached to the spindle before anaphase.
- **Cyclins and CDKs:** interactions between cyclins and CDKs control the cycle. The concentration of a cyclin rises and falls through the cycle. Specific cyclin and CDK pairs are not tested.
- **Disruptions** to the cell cycle may result in **cancer** (cells that divide when they should not) or **apoptosis** (programmed cell death).
- A buildup of cells at one stage suggests that they are being held at the checkpoint that follows it.

### Watch out for
On the exam, a common error is failing to explain the purpose and timing of a checkpoint. Say what the checkpoint checks, and what goes wrong if it is missing.

### Worked example
Prompt: "A mutation inactivates a protein that stops the cycle when DNA is damaged. Predict what happens to a cell with damaged DNA."

The checkpoint no longer stops the cycle, so the cell continues to divide with damaged DNA and passes the mutations on to its daughter cells, which can lead to cancer.
"""),
]

refreshers_lib.write("ap-biology", 4, ENTRIES)
