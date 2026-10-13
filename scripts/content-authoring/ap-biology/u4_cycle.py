"""Unit 4, topics 4.4 Feedback (9 questions), 4.5 Cell Cycle (12) and 4.6 Regulation of Cell Cycle (10).

Required content (CED 2025-26): 4.4.A negative feedback reduces the initial stimulus and returns a system to its set point (blood sugar by insulin and glucagon); positive feedback amplifies a response and
moves the variable further from the set point (lactation, onset of labor, fruit ripening); 4.5.A the cell cycle (interphase G1, S, G2, mitosis, cytokinesis; G1 duplicates organelles, S replicates DNA
into sister chromatids joined at a centromere, G2 protein synthesis, ATP and centrosome replication, G0 cells exit but can re-enter); 4.5.B mitosis transfers a complete genome to two genetically identical
daughter cells (growth, tissue repair, asexual reproduction) in prophase, metaphase, anaphase, telophase, with cytokinesis by a cleavage furrow (animal) or a cell plate (plant); 4.6.A checkpoints and
cyclin-CDK interactions regulate the cycle (specific pairs excluded); 4.6.B disruptions may result in cancer or apoptosis. Suggested skills: 6.E, 4.B (describe data), 5.A (calculations).
"""
from lib import *


def build(B):
    # ------------------------------------------------------------------ 4.4 Feedback
    B.mcq(4, "Which statement correctly describes negative feedback?",
          ch("It reduces the initial stimulus, so a system that has been disturbed is returned toward its set point.", "Negative feedback mechanisms maintain homeostasis by reducing the initial stimulus."),
          [ch("It amplifies the initial stimulus, so a system that has been disturbed is moved further from its set point.", "This describes positive feedback."),
           ch("It has no effect on the initial stimulus, so a system that has been disturbed stays at the new value for good.", "Negative feedback acts on the stimulus to return the system to its set point."),
           ch("It removes the set point, so a system that has been disturbed no longer has a value to which it can return.", "A set point is the target value that negative feedback restores.")],
          "Negative feedback returns a system toward its set point.", difficulty="easy")

    B.mcq(4, "Which statement correctly describes positive feedback?",
          ch("It amplifies a response, so the variable that started the response moves further away from its initial set point.", "Positive feedback intensifies the stimulus, which starts an additional response and produces a system change."),
          [ch("It reduces a response, so the variable that started the response is brought back toward its initial set point.", "This describes negative feedback."),
           ch("It stops a response at once, so the variable that started the response stays at the value that it had at the start.", "Positive feedback does not stop the response. It amplifies it."),
           ch("It keeps a response constant, so the variable that started the response does not change from its initial set point.", "Positive feedback produces change and does not hold a variable constant.")],
          "Positive feedback amplifies a response and moves the variable away from its set point.", difficulty="easy")

    B.mcq(4, "After a meal, the concentration of glucose in the blood rises, and the pancreas releases insulin, which causes cells to take up glucose, so the concentration of glucose in the blood falls. Which type of mechanism is this?",
          ch("Negative feedback, because the response reduces the stimulus and returns the blood glucose toward its set point", "The rise in glucose causes a response that lowers it again, which is negative feedback."),
          [ch("Positive feedback, because the response amplifies the stimulus and moves the blood glucose further from its set point", "The response lowers the glucose, so it reduces the stimulus."),
           ch("Positive feedback, because the release of insulin is a response to the rise in the concentration of glucose in the blood", "Having a response to a stimulus does not make the feedback positive. What matters is whether the response reduces or amplifies the stimulus."),
           ch("Neither type of feedback, because blood glucose is not a variable that is controlled by the body in any kind of way", "Blood glucose is regulated, for example by insulin and glucagon.")],
          "Regulation of blood sugar by insulin and glucagon is an example of negative feedback.", difficulty="medium")

    B.mcq(4, "During childbirth, the stretching of the cervix causes the release of oxytocin, which causes stronger contractions of the uterus, which stretch the cervix more and cause the release of more oxytocin. Which type of mechanism is this?",
          ch("Positive feedback, because the response intensifies the stimulus that caused it, so the process is amplified until the end", "The stronger contractions increase the stretching of the cervix, which amplifies the response until the baby is born."),
          [ch("Negative feedback, because the response intensifies the stimulus that caused it and returns the system to its set point", "Negative feedback reduces the stimulus. Here the stimulus is intensified."),
           ch("Negative feedback, because the release of oxytocin is a response to a stimulus and the response is made by a hormone", "A response to a stimulus is not enough to make a mechanism negative feedback."),
           ch("Neither type of feedback, because the contractions of the uterus are controlled only by the muscles of the uterus", "The release of oxytocin and the stretching of the cervix form a feedback loop.")],
          "The onset of labor is an example of positive feedback.", difficulty="medium")

    B.mcq(4, "Ripe fruit releases ethylene gas, and ethylene causes nearby fruit to ripen and to release more ethylene. Which statement best describes this process?",
          ch("It is positive feedback, because the response (the release of more ethylene) amplifies the stimulus (the ethylene).", "The ripening of fruit is an example of positive feedback, because each response increases the stimulus."),
          [ch("It is negative feedback, because the response (the release of more ethylene) reduces the stimulus (the ethylene).", "The release of more ethylene increases the stimulus and does not reduce it."),
           ch("It is negative feedback, because the fruit returns to the set point of the unripe fruit after the ethylene is released.", "The fruit moves away from its starting state and does not return to it."),
           ch("It is not feedback of any kind, because ethylene is a gas that is released into the air and not into the blood.", "Feedback does not depend on the way in which a signal travels.")],
          "Ripening of fruit is an example of positive feedback.", difficulty="medium")

    t_pts = [(0, 37.0), (15, 38.0), (30, 38.2), (45, 37.4), (60, 37.0)]
    temp = graph("Time after the start of heat exposure (min)", "Body temperature (°C)", 0, 60, 36, 40,
                 [line("Body temperature", t_pts, "red")],
                 "Body temperature against time. It rises from 37.0 to 38.2 degrees Celsius in the first 30 minutes and then falls back to 37.0 by 60 minutes.")
    B.mcq(4, "A person exercises in a hot room. The graph shows the body temperature of the person. Which statement best describes the data?",
          ch("The temperature rises above the set point of 37 °C and then returns to it, which is consistent with negative feedback such as sweating.", "A disturbance moves the temperature away from the set point, and a response returns it. This is what negative feedback does."),
          [ch("The temperature rises further and further away from 37 °C during the whole time, which is consistent with positive feedback.", "The graph shows that the temperature comes back to 37 °C after 30 minutes."),
           ch("The temperature does not change from 37 °C at any time, which shows that body temperature is not controlled by feedback.", "The temperature changes during the first 30 minutes and then returns to 37 °C."),
           ch("The temperature falls below 37 °C at 30 minutes, which shows that the body is no longer able to control its temperature.", "The temperature rises to 38.2 °C at 30 minutes and does not fall below 37 °C.")],
          "Negative feedback returns a variable toward its set point after a disturbance.", diagram=temp, difficulty="medium")

    B.mcq(4, "A mutation prevents the insulin receptor from working in the cells of a person. Which prediction about the blood glucose of the person after a meal is most consistent with how negative feedback regulates it?",
          ch("The blood glucose will stay high for longer, because cells cannot respond to insulin by taking up glucose and so the stimulus is not reduced.", "Without a working receptor the response to insulin does not occur, so the negative feedback loop cannot lower the glucose."),
          [ch("The blood glucose will fall faster than normal, because the pancreas will release a larger amount of insulin to make up for the mutation.", "A larger amount of insulin cannot act on cells that cannot respond to it."),
           ch("The blood glucose will not change after the meal, because glucose from food does not reach the blood in a person with the mutation.", "Glucose from food enters the blood as usual. The mutation affects the response of the cells."),
           ch("The blood glucose will fall below the set point, because the loss of the receptor removes the signal that tells cells to keep glucose.", "Glucose is more likely to stay high because cells cannot take it up in response to insulin.")],
          "Negative feedback needs a working response to reduce the stimulus.", difficulty="hard")

    B.mcq(4, "Which statement best explains why positive feedback cannot be used by a cell or an organism to maintain homeostasis over a long period?",
          ch("Positive feedback amplifies a change and moves the variable further from its set point, so it needs an end point or another mechanism to stop it.", "Positive feedback intensifies the stimulus. A process such as labor ends when the baby is born."),
          [ch("Positive feedback reduces a change and moves the variable toward its set point, so it holds the variable at a fixed value for too long.", "Positive feedback does not move a variable toward the set point. This describes negative feedback."),
           ch("Positive feedback stops all responses in the body, so the variable has no way of changing from the value that it has at the start.", "Positive feedback produces more of a response and does not stop responses."),
           ch("Positive feedback works only in plants, so animals have no mechanism that is able to amplify a response to a stimulus.", "Positive feedback occurs in animals as well, as in labor and lactation.")],
          "Positive feedback moves a variable away from its set point.", difficulty="hard")

    B.mcq(4, "A person goes outside on a cold day, and the body temperature begins to fall. The person begins to shiver, which produces heat, and the temperature returns to normal. Which statement is correct?",
          ch("The shivering is part of a negative feedback mechanism, because it reduces the fall in temperature that was the stimulus.", "Shivering is a response that returns the temperature toward the set point."),
          [ch("The shivering is part of a positive feedback mechanism, because it makes the temperature fall further from the normal value.", "Shivering raises the temperature, so it opposes the change."),
           ch("The shivering is not related to temperature, because muscles move only as a response to signals about the position of the body.", "Shivering is a response to the lower temperature of the body."),
           ch("The shivering is a stimulus that lowers the temperature, because the movement of the muscles loses heat to the air outside.", "Shivering generates heat and raises the temperature.")],
          "Negative feedback mechanisms operate at the organismal level, for example in regulating body temperature.", difficulty="medium")

    # ------------------------------------------------------------------ 4.5 Cell cycle
    B.mcq(5, "Which choice lists the stages of interphase of the cell cycle in order?",
          ch("G1, then S, then G2", "Interphase has three stages: G1, S and G2."),
          [ch("S, then G1, then G2", "DNA is replicated in S phase, which comes after G1."),
           ch("G1, then G2, then S", "DNA is replicated in S phase, which comes before G2."),
           ch("G2, then S, then G1", "The order of the stages is G1, S and G2.")],
          "Interphase consists of G1, S and G2.", difficulty="easy")

    B.mcq(5, "What happens to the DNA of a cell during S phase?",
          ch("It replicates, so each chromosome consists of two sister chromatids connected at a centromere.", "In S phase, DNA in the form of chromatin replicates to form two sister chromatids connected at a centromere."),
          [ch("It condenses, so each chromosome is compact and is moved along the spindle fibers to the equator of the cell.", "This describes events in mitosis and not S phase."),
           ch("It is divided between two cells, so each of the two cells has half of the DNA that the original cell had.", "DNA is divided between cells at the end of mitosis, and each daughter cell gets a complete copy."),
           ch("It is broken down by enzymes, so the cell has no DNA for a period before it enters the next stage of the cell cycle.", "The DNA is not broken down. It is copied.")],
          "DNA replicates in S phase, forming sister chromatids.", difficulty="easy")

    B.mcq(5, "Which of the following events take place during G1 and G2 of the cell cycle?",
          ch("In G1 the cell is metabolically active and duplicates organelles, and in G2 proteins are made and the centrosomes replicate.", "G1 involves growth and duplication of organelles, and G2 involves protein synthesis, large amounts of ATP and replication of centrosomes."),
          [ch("In G1 the DNA is replicated and sister chromatids form, and in G2 the chromosomes line up along the equator of the cell.", "DNA is replicated in S phase, and chromosomes line up in metaphase."),
           ch("In G1 the cell divides its cytoplasm, and in G2 the nuclear envelope breaks down and the spindle forms in the cell.", "The cytoplasm divides in cytokinesis, and the nuclear envelope breaks down in mitosis."),
           ch("In G1 the sister chromatids are pulled apart, and in G2 the cell is separated into two daughter cells by a furrow.", "These events occur during mitosis and cytokinesis, after interphase.")],
          "G1 and G2 are phases of growth and preparation.", difficulty="medium")

    B.mcq(5, "A mature nerve cell no longer divides, but some nondividing cells can re-enter the cell cycle if they receive appropriate cues. Which term describes the stage of a cell that has left the cell cycle but may re-enter it?",
          ch("G0, a stage in which a cell no longer divides but can reenter the cell cycle in response to appropriate cues", "A cell can enter G0, in which it does not divide, and may re-enter the cycle."),
          [ch("S phase, a stage in which a cell is replicating its DNA and then divides when the replication is finished", "S phase is a part of the cell cycle in which DNA replicates."),
           ch("Telophase, a stage in which a cell is separating its cytoplasm and then enters a new cycle of mitosis at once", "Telophase is a stage of mitosis, and cells in it are part of the cell cycle."),
           ch("G2, a stage in which a cell is making proteins for mitosis and cannot leave the cycle after it has entered this stage", "G2 is a part of the cell cycle that comes before mitosis.")],
          "Cells can enter G0 and may re-enter the cell cycle in response to cues.", difficulty="medium")

    B.mcq(5, "Which choice lists the stages of mitosis in the correct order?",
          ch("Prophase, metaphase, anaphase, telophase", "The stages of mitosis occur in this order, followed by cytokinesis."),
          [ch("Prophase, anaphase, metaphase, telophase", "Chromosomes line up at the equator in metaphase, which comes before anaphase."),
           ch("Metaphase, prophase, anaphase, telophase", "Prophase is the first stage of mitosis."),
           ch("Prophase, metaphase, telophase, anaphase", "Anaphase, in which sister chromatids separate, comes before telophase.")],
          "Mitosis occurs in the order prophase, metaphase, anaphase, telophase.", difficulty="easy")

    B.mcq(5, "Which of the following events occurs in prophase of mitosis?",
          ch("The sister chromatids condense, the mitotic spindle begins to form, and the centrosomes move to opposite poles of the cell.", "These are the events of prophase."),
          [ch("The spindle fibers align the chromosomes along the equator of the cell, and each chromosome is attached to fibers from both poles.", "This describes metaphase."),
           ch("The paired sister chromatids separate, and the spindle fibers pull the chromatids toward the opposite poles of the cell.", "This describes anaphase."),
           ch("The spindle breaks down, a new nuclear envelope forms around each set of chromosomes, and then the cytoplasm divides.", "This describes telophase and cytokinesis.")],
          "In prophase the chromatids condense and the spindle begins to form.", difficulty="medium")

    B.mcq(5, "In which stage of mitosis do the paired sister chromatids separate and are pulled toward opposite poles of the cell?",
          ch("Anaphase, in which the spindle fibers pull the separated chromatids toward the opposite poles of the cell", "In anaphase the sister chromatids separate and are pulled toward the poles."),
          [ch("Metaphase, in which the spindle fibers align the chromosomes along the equator before they separate", "Chromosomes line up in metaphase, and they separate in anaphase."),
           ch("Prophase, in which the chromosomes condense and the spindle starts to form before the chromatids separate", "The chromatids are still joined in prophase."),
           ch("Telophase, in which the spindle breaks down and a new nuclear envelope forms after the chromatids have separated", "In telophase the chromatids have already reached the poles.")],
          "Sister chromatids separate in anaphase.", difficulty="medium")

    B.mcq(5, "How does cytokinesis differ in animal cells and plant cells?",
          ch("In animal cells a cleavage furrow forms, and in plant cells a cell plate forms, and each results in two new daughter cells.", "Cytokinesis divides the cytoplasm by a cleavage furrow in animal cells and by a cell plate in plant cells."),
          [ch("In animal cells a cell plate forms, and in plant cells a cleavage furrow forms, and each results in two new daughter cells.", "This reverses the two structures."),
           ch("In animal cells the cytoplasm divides after mitosis, but in plant cells it never divides, so the cells have many nuclei.", "The cytoplasm of plant cells divides too, by the formation of a cell plate."),
           ch("In animal cells and plant cells a cleavage furrow forms, but in plant cells the furrow is made of cellulose and stays.", "Plant cells form a cell plate and not a cleavage furrow.")],
          "Cytokinesis uses a cleavage furrow in animal cells and a cell plate in plant cells.", difficulty="medium")

    counts = [("Interphase", 160), ("Prophase", 20), ("Metaphase", 8), ("Anaphase", 6), ("Telophase", 6)]
    total = sum(n for _, n in counts)
    mitotic = sum(n for p, n in counts if p != "Interphase")
    pct_mit = mitotic / total * 100
    cycle_h = 24
    t_pro = counts[1][1] / total * cycle_h
    assert (total, mitotic, round(pct_mit, 1), round(t_pro, 1)) == (200, 40, 20.0, 2.4)
    onion = table(["Stage", "Number of cells"], [(p, str(n)) for p, n in counts], caption=f"Cells in the root tip of an onion ({total} cells counted)", row_headers=True)
    B.mcq(5, f"A student counts {total} cells in a stained onion root tip and records the stage of each cell, as shown in the table. What percent of the cells are in mitosis?",
          ch("20%", "The cells in prophase, metaphase, anaphase and telophase are in mitosis: 20 + 8 + 6 + 6 = 40. 40 / 200 x 100 = 20 percent.", 20),
          [ch("80%", "This is the percent of the cells that are in interphase (160 / 200). Mitosis includes the other stages.", 80),
           ch("10%", "This is the percent of the cells that are in prophase only (20 / 200).", 10),
           ch("40%", "This is the number of cells in mitosis (40) and not the percent. The percent is the number divided by the total.", 40)],
          "Percent of cells in mitosis = cells in prophase, metaphase, anaphase and telophase divided by the total.", diagram=onion, difficulty="medium")

    B.mcq(5, f"The cells in the onion root tip complete a cell cycle in {cycle_h} hours. Assuming that the cells are at random stages of the cycle, about how long does a cell spend in prophase, based on the table?",
          ch("2.4 hours", "The fraction of the cells in prophase is 20 / 200 = 0.10, so the time in prophase is 0.10 x 24 hours = 2.4 hours.", 2.4),
          [ch("1.2 hours", "This uses a cycle of 12 hours instead of the 24 hours that the question gives.", 1.2),
           ch("20 hours", "This is the number of cells in prophase (20) and not a time.", 20),
           ch("9.6 hours", "This is the time for 40 percent of the cycle (0.40 x 24), which uses the number of cells in mitosis, 40, instead of the number in prophase.", 9.6)],
          "The time in a stage = the fraction of the cells in that stage x the length of the whole cycle.", diagram=onion, difficulty="hard")

    B.mcq(5, "Mitosis results in the transfer of a complete genome from a parent cell to daughter cells. Which statement correctly describes the result of mitosis in eukaryotes?",
          ch("Two daughter cells that are genetically identical to the parent cell, which are used for growth, tissue repair and asexual reproduction", "Mitosis ensures the transfer of a complete genome to two genetically identical daughter cells."),
          [ch("Four daughter cells that each have half of the chromosomes of the parent cell, which are used for sexual reproduction", "This describes meiosis."),
           ch("Two daughter cells that each have half of the genes of the parent cell, so that the cells can specialize in different jobs", "Each daughter cell receives a complete genome. They can specialize because of gene expression."),
           ch("One daughter cell that has twice the genome of the parent cell, so that the organism can grow by making larger cells", "Mitosis produces two daughter cells that have the same genome as the parent.")],
          "Mitosis produces two genetically identical daughter cells.", difficulty="medium")

    n2 = 6
    chrom_g2, chat_g2, chrom_ana = n2, 2 * n2, 2 * n2
    assert (chrom_g2, chat_g2, chrom_ana) == (6, 12, 12)
    B.mcq(5, f"A diploid cell of an animal has {n2} chromosomes before DNA replication (2n = {n2}). How many chromosomes and how many chromatids are present in the cell during G2, and how many chromosomes are present during anaphase of mitosis?",
          ch("In G2 there are 6 chromosomes and 12 chromatids, and in anaphase there are 12 chromosomes", "DNA replication makes each chromosome consist of two sister chromatids, so the number of chromosomes does not change in G2. In anaphase the sister chromatids separate and each is then a chromosome."),
          [ch("In G2 there are 12 chromosomes and 12 chromatids, and in anaphase there are 12 chromosomes", "Replication doubles the chromatids, not the chromosomes, because sister chromatids are counted as one chromosome."),
           ch("In G2 there are 6 chromosomes and 12 chromatids, and in anaphase there are 6 chromosomes", "In anaphase the sister chromatids separate, and each one counts as a chromosome, so there are 12."),
           ch("In G2 there are 6 chromosomes and 6 chromatids, and in anaphase there are 12 chromosomes", "In G2 each chromosome has been replicated and has two chromatids, so there are 12 chromatids.")],
          "Count chromosomes by the number of centromeres. Replication makes sister chromatids but does not add chromosomes.", difficulty="hard")

    dna_pts = [(0, 2), (8, 2), (14, 4), (20, 4), (21, 2), (24, 2)]
    dna = graph("Time (hours)", "Relative amount of DNA per cell", 0, 24, 0, 5,
                [line("DNA per cell", dna_pts, "blue")],
                "Relative amount of DNA per cell over a 24 hour cell cycle. It is 2 from 0 to 8 hours, rises to 4 between 8 and 14 hours, stays at 4 until 20 hours, and falls to 2 by 21 hours.")
    B.mcq(5, "The graph shows the amount of DNA in a cell during one cell cycle. Which statement best explains the rise in the amount of DNA between 8 and 14 hours?",
          ch("The cell is in S phase, in which the DNA is replicated, so the amount of DNA doubles from 2 to 4.", "The doubling of the amount of DNA corresponds to S phase."),
          [ch("The cell is in G1, in which the cell duplicates its organelles, so the amount of DNA doubles as each organelle gets a copy.", "The amount of DNA doubles in S phase. In G1 the amount of DNA stays the same."),
           ch("The cell is in anaphase, in which the sister chromatids separate, so the amount of DNA doubles in the one cell.", "Anaphase separates chromatids, and the cell at the end of mitosis divides into two cells with half the amount."),
           ch("The cell is in cytokinesis, in which the cytoplasm divides, so the amount of DNA doubles in each of the two new cells.", "Cytokinesis reduces the amount of DNA per cell. It does not double it.")],
          "The amount of DNA per cell doubles in S phase and halves when the cell divides.", diagram=dna, difficulty="hard")

    # ------------------------------------------------------------------ 4.6 Regulation of the cell cycle
    B.mcq(6, "What is the role of a checkpoint in the cell cycle?",
          ch("It is an internal control that checks conditions in the cell and lets the cycle continue only if they are suitable.", "A number of internal controls, or checkpoints, regulate progression through the cell cycle."),
          [ch("It is a stage of the cell cycle in which the cell makes copies of its DNA so that the next stage can begin.", "A checkpoint is a control. The copying of DNA happens in S phase."),
           ch("It is an enzyme that joins the fragments of DNA after replication, so that the DNA of the cell is complete.", "A checkpoint is not an enzyme that joins DNA fragments."),
           ch("It is a signal from outside the body that makes every cell divide at the same time and at the same rate as the others.", "Checkpoints are internal controls and do not make all of the cells divide at the same time.")],
          "Checkpoints are internal controls of the cell cycle.", difficulty="easy")

    B.mcq(6, "At the checkpoint that comes just before the cell begins mitosis, the cell checks whether its DNA has been replicated correctly. What is the purpose of this timing?",
          ch("It makes sure that the DNA is complete and undamaged before the cell divides, so each daughter cell receives a complete genome.", "The timing of a checkpoint is related to the process it protects. Checking replicated DNA before mitosis prevents the passing on of errors."),
          [ch("It makes sure that the cell is as small as possible before the cell divides, so that each daughter cell is smaller than the parent.", "A checkpoint does not aim to make the cell as small as possible."),
           ch("It makes sure that the DNA is replicated more than once before the cell divides, so that each daughter cell has extra copies.", "The DNA is replicated once in each cell cycle. Extra copies are not the aim of the checkpoint."),
           ch("It makes sure that mitosis begins at once whatever the state of the DNA, so that the cycle is never delayed for any reason.", "A checkpoint is a place where the cycle can be stopped if conditions are not suitable.")],
          "Checkpoints give the cell a chance to check conditions before it goes on to the next stage.", difficulty="medium")

    B.mcq(6, "Which statement best describes how cyclins and cyclin-dependent kinases (CDKs) control the cell cycle?",
          ch("Cyclins interact with CDKs to activate them, and the resulting activity of the CDKs moves the cell from one stage of the cycle to the next.", "Interactions between cyclins and CDKs control the cell cycle."),
          [ch("Cyclins and CDKs are the DNA that is copied in S phase, so the cell cycle ends when they have been copied twice.", "Cyclins and CDKs are proteins and not DNA."),
           ch("Cyclins are made only at the end of the cell cycle, so the concentration of cyclin does not change during the earlier stages.", "The concentration of cyclin changes through the cycle."),
           ch("CDKs are active all the time at the same level, so the cyclins have no effect on the stages through which a cell passes.", "CDKs are controlled by the cyclins they interact with, and so their activity changes.")],
          "Interactions between cyclins and CDKs control the cell cycle.", difficulty="medium")

    cy = [(0, 10), (6, 10), (10, 20), (14, 40), (18, 85), (20, 100), (21, 15), (24, 10)]
    cyc = graph("Time (hours)", "Relative concentration of cyclin", 0, 24, 0, 100,
                [line("Cyclin", cy, "purple")],
                "Relative concentration of a cyclin over a 24 hour cell cycle. It is low at first, rises slowly to about 40 at 14 hours and then steeply to 100 at 20 hours, and falls to 15 at 21 hours.")
    B.mcq(6, "The graph shows the concentration of a cyclin in a dividing cell over one cell cycle. Which statement is best supported by the graph?",
          ch("The concentration of the cyclin rises and falls in a cycle, which is consistent with its role in controlling the progress of the cell through the stages of the cycle.", "The cyclin rises to a peak and then drops sharply, as expected for a protein that controls the progress of the cell cycle."),
          [ch("The concentration of the cyclin increases at a steady rate through the whole cell cycle, which shows that it is never broken down.", "The graph shows a sharp fall at 21 hours."),
           ch("The concentration of the cyclin stays at the same value through the whole cell cycle, which shows that it has no role in the cycle.", "The concentration changes a great deal during the cycle."),
           ch("The concentration of the cyclin is highest at the start of the cycle, which shows that it is made only during the stage of G1.", "The graph shows that the concentration is lowest at the start and highest at 20 hours.")],
          "The concentrations of cyclins vary in a cycle, which helps to control the cell cycle.", diagram=cyc, difficulty="medium")

    B.mcq(6, "A mutation inactivates a protein that normally stops the cell cycle at a checkpoint when the DNA is damaged. Which outcome is most likely for a cell that has damaged DNA and this mutation?",
          ch("The cell continues to divide with damaged DNA, which can pass mutations on to daughter cells and may lead to cancer.", "Disruptions to the cell cycle may result in cancer. Without the checkpoint the damage is not stopped."),
          [ch("The cell stops dividing for good, because the loss of the protein causes every damaged cell to enter G0 at once.", "Loss of a protein that stops the cycle does not cause the cell to stop dividing."),
           ch("The cell repairs the DNA more quickly than before, because the protein that was lost normally slows down repair.", "The protein is a checkpoint control. Its loss does not speed up repair."),
           ch("The cell makes more copies of its DNA in S phase, because the protein normally makes sure that the DNA is replicated once.", "The effect on damaged cells is that they continue to divide.")],
          "Disruptions to the cell cycle may result in cancer or apoptosis.", difficulty="medium")

    B.mcq(6, "Which statement best describes the fate of a cell that has damaged DNA that cannot be repaired, when its checkpoints are working normally?",
          ch("The cell may undergo apoptosis, which is programmed cell death, so that the damaged DNA is not passed on.", "Disruptions to the cell cycle may result in cancer or apoptosis, and apoptosis removes damaged cells."),
          [ch("The cell divides at once, because the damage is copied into both of the daughter cells, which can repair it.", "Working checkpoints stop the cycle, and daughter cells do not repair DNA that the parent could not."),
           ch("The cell moves to the next stage of the cycle without delay, because the damage is detected only at the end of mitosis.", "Damage is detected at the checkpoints before the cell goes on to the next stage."),
           ch("The cell makes a second nucleus, because this lets the cell keep the damaged DNA apart from the healthy DNA.", "A cell does not make a second nucleus to separate damaged DNA.")],
          "Apoptosis can remove cells that cannot pass the checkpoints.", difficulty="medium")

    ph_rows = [("Untreated cells", "55", "30", "15"), ("Cells treated with a drug for 24 hours", "20", "25", "55")]
    B.mcq(6, "Researchers measure the percent of cells in each stage of the cell cycle in untreated cells and in cells that were treated with a drug, as shown in the table. Which conclusion is best supported by the data?",
          ch("The drug causes the cells to accumulate at the G2 and mitosis stages, which suggests that it prevents the cells from completing mitosis.", "The percent of the cells in G2/M increased from 15 to 55 percent, so more cells are held at that point of the cycle."),
          [ch("The drug causes the cells to accumulate in G1, which suggests that it prevents the cells from starting the replication of DNA.", "The percent of the cells in G1 decreased from 55 to 20 percent."),
           ch("The drug has no effect on the cell cycle, because the percent of the cells in S phase is almost the same in both groups.", "The percent of cells in S phase is similar, but the percentages in G1 and in G2/M differ a great deal."),
           ch("The drug causes all of the cells to divide faster, because the percent of the cells in G2 and mitosis increased in the treated cells.", "Cells accumulating in a stage suggests that they are held there, not that they divide faster.")],
          "A build-up of cells in a stage suggests that they are held at the following checkpoint.",
          diagram=table(["Cell group", "G1 (% of cells)", "S (% of cells)", "G2 and mitosis (% of cells)"], ph_rows, caption="Percent of cells in each stage of the cell cycle", row_headers=True), difficulty="hard")

    B.mcq(6, "A cell has a mutation that stops it from checking whether all of its chromosomes are attached to the spindle before anaphase begins. Which prediction is most consistent with this mutation?",
          ch("Chromosomes may be separated incorrectly, so the daughter cells may have too many or too few chromosomes.", "Without the check, anaphase can begin before all of the chromosomes are attached, which leads to errors in the separation of the chromosomes."),
          [ch("Chromosomes will be separated correctly all of the time, because the spindle attaches to them whether or not a check takes place.", "The check is there to prevent errors. Without it, errors are more likely."),
           ch("Chromosomes will not be separated at all, because the cell will wait for ever at the stage before anaphase begins.", "Without the check the cell does not wait, so anaphase can begin too early."),
           ch("Chromosomes will be replicated a second time, because the cell will return to S phase when the check is not made.", "The missing check affects the separation of the chromosomes and does not cause a second round of replication.")],
          "Checkpoints help to make sure that chromosomes are separated correctly.", difficulty="hard")

    B.mcq(6, "Why do most mature nerve cells in an adult not divide?",
          ch("They have exited the cell cycle and entered G0, in which a cell no longer divides, although some nondividing cells can re-enter the cycle.", "Nondividing cells may exit the cell cycle or be held at a particular stage."),
          [ch("They have no DNA, so the cells cannot copy their genetic information and so cannot enter the next stage of the cycle.", "Nerve cells contain DNA."),
           ch("They are stuck at the end of mitosis, so each cell has two nuclei that cannot be separated in the cytoplasm.", "Mature nerve cells are not stuck in mitosis."),
           ch("They are in S phase all of the time, so the DNA is replicated again and again without the cell ever dividing.", "A cell in G0 is not continuously replicating DNA.")],
          "Cells that do not divide may exit the cell cycle (G0).", difficulty="medium")

    fuse_rows = [("S-phase cell fused with a G1 cell", "The nucleus of the G1 cell began to replicate its DNA"), ("G2 cell fused with a G1 cell", "The nucleus of the G1 cell did not begin to replicate its DNA until it would normally have done so")]
    B.mcq(6, "Researchers fused cells in different stages of the cell cycle and observed what happened to the nucleus of the cell that was in G1, as shown in the table. Which conclusion is best supported by the data?",
          ch("The cytoplasm of a cell in S phase contains a factor that triggers the start of DNA replication in a nucleus that is in G1.", "The G1 nucleus began to replicate its DNA when fused with an S-phase cell and not when fused with a G2 cell, so a signal in the S-phase cell starts replication."),
          [ch("The cytoplasm of a cell in G2 contains a factor that triggers the start of DNA replication in a nucleus that is in G1.", "The G1 nucleus did not begin to replicate when fused with the G2 cell."),
           ch("The DNA replication of a nucleus that is in G1 is controlled only by the nucleus, and the cytoplasm of the cell has no effect.", "The nucleus of the G1 cell began to replicate in the cytoplasm of the S-phase cell, so the cytoplasm has an effect."),
           ch("All of the cells begin to replicate their DNA when they are fused with any other cell, whatever the stage of that other cell.", "Only the fusion with an S-phase cell caused the early start of replication.")],
          "Cell fusion experiments show that regulators in the cytoplasm control the progress of the cell cycle.",
          diagram=table(["Cells that were fused", "What was observed"], fuse_rows, caption="Fusion of cells at different stages of the cell cycle", row_headers=True), difficulty="hard")
