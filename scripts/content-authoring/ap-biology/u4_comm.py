"""Unit 4, topics 4.1 Cell Communication (8 questions), 4.2 Introduction to Signal Transduction (11) and 4.3 Signal Transduction Pathways (10).

Required content (CED 2025-26): 4.1.A cells communicate by direct contact or by chemical signaling from a distance; 4.1.B local regulators act over short distances on cells near the signaling cell,
signals (such as hormones) can travel long distances to target cells of another type; 4.2.A signal transduction links signal reception with a cellular response and often involves protein
modification and phosphorylation cascades; 4.2.B a chemical messenger (ligand) is recognized by the ligand-binding domain of a receptor protein (a G protein-coupled receptor is an example; receptors may
be on the surface or in the cytoplasm or nucleus), after binding the receptor changes shape, enzymes and second messengers such as cAMP relay and amplify the signal, ligand-gated channels open or
close; 4.3.A responses include changes in gene expression and cell function (which may change phenotype) and apoptosis; 4.3.B a change in the structure of any signaling molecule (a mutation in any
domain of a receptor or any component) can alter the pathway, and chemicals that interact with a component can activate or inhibit it. Suggested skills: 1.A/1.B, 6.C.
"""
from lib import *


def build(B):
    # ------------------------------------------------------------------ 4.1 Cell communication
    B.mcq(1, "In which two ways can cells communicate with one another?",
          ch("By direct contact with other cells, or from a distance by chemical signaling", "Cells communicate through direct contact between cells and through chemical signals that can act at a distance."),
          [ch("By direct contact only, because chemical signals cannot move from one cell to another", "Chemical signals such as hormones and local regulators do travel between cells."),
           ch("By chemical signals only, because the plasma membranes of different cells never touch one another", "Cells can interact by direct contact, as immune cells do."),
           ch("By the exchange of whole organelles, because all signals are carried by organelles between the cells", "Signals are not carried between cells by organelles. Cells use contact and chemical signals.")],
          "Cells communicate by direct contact or by chemical signaling.", difficulty="easy")

    B.mcq(1, "A neuron releases neurotransmitter molecules that affect only the neighboring cell across a tiny gap. Which term best describes the neurotransmitter?",
          ch("A local regulator, which targets cells in the vicinity of the cell that releases it, over a short distance", "Local regulators act over short distances on nearby target cells."),
          [ch("A hormone, which travels through the bloodstream and acts only on cells that are far away from the signaling cell", "A neurotransmitter crossing a small gap is acting over a short distance, not in the bloodstream."),
           ch("A receptor protein, which is built into the plasma membrane of the target cell and binds the signal", "The neurotransmitter is the signal and not the receptor."),
           ch("A second messenger, which relays the signal inside the cytoplasm of the target cell after the signal binds", "A second messenger acts inside the cell, whereas the neurotransmitter acts between cells.")],
          "Local regulators act over short distances on cells near the signaling cell.", difficulty="medium")

    B.mcq(1, "Cells in the pancreas release insulin into the blood, and insulin affects the cells of the liver and muscles. Which statement correctly describes this signaling?",
          ch("It is long-distance signaling, in which a signal released by one cell type travels to target cells of another type.", "Hormones such as insulin travel long distances through the blood to target cells of different types."),
          [ch("It is short-distance signaling, in which a local regulator reaches only the cells that are next to the pancreas cells.", "Insulin reaches the liver and muscle, which are far from the pancreas, so it is long-distance signaling."),
           ch("It is signaling by direct contact, in which the pancreas cells must touch every cell that receives the insulin.", "Insulin is released into the blood and does not depend on direct contact."),
           ch("It is not a form of signaling, because the insulin is made by the cells of the pancreas and used by the same cells.", "Insulin is made by pancreas cells and acts on other cells, which is signaling.")],
          "Signals released by one cell type can travel long distances to target cells of another type.", difficulty="medium")

    B.mcq(1, "Which of the following is an example of cell-to-cell communication through direct contact?",
          ch("A helper T cell recognizes an antigen that is displayed on the surface of an antigen-presenting cell", "Immune cells interact through direct contact, for example T cells with antigen-presenting cells."),
          [ch("A pancreas cell releases insulin that moves in the blood to target cells in the liver and the muscles", "This is long-distance signaling by a hormone."),
           ch("A neuron releases neurotransmitter that diffuses across a small gap to a neighboring neuron or muscle cell", "This is signaling by a local regulator."),
           ch("A plant cell releases ethylene gas that diffuses through the air and affects fruit on a different plant", "This is signaling by a chemical released into the surroundings, not by contact.")],
          "Immune cells interact through direct cell-to-cell contact.", difficulty="medium")

    B.mcq(1, "Some species of bacteria produce light only when many cells are present in the same place. Which statement best explains how the bacteria sense that many cells are present?",
          ch("Each cell releases a chemical signal, so the concentration of the signal in the surroundings rises as the population density rises, and gene expression changes at a threshold.", "This is quorum sensing: bacteria use chemical messengers to respond to population density."),
          [ch("Each cell counts the cells that touch it, and then it passes the number of cells to the neighbors by moving an organelle.", "Quorum sensing relies on a chemical signal, not on counting touching cells or moving organelles."),
           ch("Each cell makes light whenever it makes a signal, so the light increases only when the cells each make less of the signal.", "A rising signal concentration, not less of the signal, is what leads to the response."),
           ch("Each cell is given a signal by the environment that tells it to make light, so the cells never communicate with each other.", "In quorum sensing the bacteria communicate with each other by releasing and detecting a signal.")],
          "Bacteria use chemical messengers to communicate with nearby cells and to respond to population density (quorum sensing).", difficulty="medium")

    lum = [("10³", "Low", "None"), ("10⁴", "Low", "None"), ("10⁶", "High", "Low"), ("10⁸", "Very high", "High")]
    B.mcq(1, "Researchers grew a species of bacteria in cultures of different cell densities and measured the concentration of a signal molecule in the medium and the amount of light produced. The table shows the results. Which conclusion is best supported by the data?",
          ch("The bacteria produce light only after the concentration of the signal molecule has increased, which is consistent with the signal reflecting how many cells are present.", "Light appeared when the signal concentration was high, and the signal concentration increased with the density of the culture."),
          [ch("The bacteria produce light in proportion to the number of cells at every density, because even the sparse cultures made some light.", "The two lowest densities made no light, so light is not produced in proportion at every density."),
           ch("The concentration of the signal molecule is the same at every density, because each cell releases only one molecule of the signal.", "The signal concentration rose from low to very high as the density increased."),
           ch("The signal molecule prevents the production of light, because the cultures with the most signal had the highest light production.", "The data show light increasing as the signal increased, so the signal does not prevent light.")],
          "Quorum sensing links the concentration of a signal to the density of the population.",
          diagram=table(["Cell density (cells/mL)", "Concentration of signal in the medium", "Light produced"], lum, caption="Cultures of bacteria at four densities", row_headers=True), difficulty="hard")

    B.mcq(1, "A hormone is carried in the blood to all of the tissues of the body, but only some of the cell types respond to it. Which statement best explains why only some cells respond?",
          ch("Only the target cells have the specific receptor protein that recognizes the hormone, so only they can respond to it.", "A signal affects a cell only if the cell has a receptor with a ligand-binding domain that recognizes it."),
          [ch("Only the target cells are close enough to the blood vessels, so the hormone is unable to reach the other kinds of cells.", "The hormone is carried in the blood to all of the tissues, so the distance from vessels is not what decides the response."),
           ch("Only the target cells contain DNA, so the hormone is unable to affect cells that have no genetic material in them.", "All of the cells of the body, apart from some specialized cells such as mature red blood cells, contain DNA."),
           ch("Only the target cells can make the hormone, so the other cells have no use for a hormone that they cannot produce.", "Target cells do not have to make the hormone. They have to have a receptor that recognizes it.")],
          "Target cells have specific receptors for a signal.", difficulty="medium")

    B.mcq(1, "A drug stops a cell from releasing a local regulator. Which prediction about the cells that are near the treated cell is most consistent with what is known about local signaling?",
          ch("The nearby target cells will not receive the signal, so they will not make the response that the regulator would normally cause.", "Local regulators target cells in the vicinity of the signaling cell. Without the signal there is no response."),
          [ch("The nearby cells will make the response anyway, because the receptors in the cells are always active in the absence of any signal.", "A receptor is normally activated when its ligand binds. Without the ligand there is no response."),
           ch("The nearby cells will make a stronger response, because the lack of the regulator makes their receptors more sensitive to it.", "Without the signal, the nearby cells do not receive the message and make no response."),
           ch("The cells that are far away in the body will stop responding to the local regulator, because it has been blocked at its source.", "A local regulator acts on nearby cells and not on cells that are far away in the body.")],
          "Without the release of a local regulator, nearby target cells do not receive the signal.", difficulty="hard")

    # ------------------------------------------------------------------ 4.2 Introduction to signal transduction
    B.mcq(2, "In a signal transduction pathway, what is a ligand?",
          ch("A chemical messenger that is recognized by, and binds to, a receptor protein in a target cell of the body", "Signaling begins with the recognition of a ligand by a receptor protein."),
          [ch("A protein that carries the signal inside the cell, relaying it from the plasma membrane to the nucleus", "This describes a relay protein or a second messenger, not the ligand."),
           ch("A part of the DNA that stores the information about how the cell should respond to the signal that arrives", "A ligand is a chemical messenger, not a part of the DNA."),
           ch("An enzyme that adds a phosphate group to other proteins in the cell, which changes the activity of those proteins", "This describes a protein kinase. The ligand is the signal.")],
          "A ligand is a chemical messenger that binds a receptor.", difficulty="easy")

    B.mcq(2, "Which choice lists the main stages of a signal transduction pathway in the correct order?",
          ch("The ligand binds a receptor, the signal is relayed inside the cell, and the cell makes a response", "Pathways link the reception of a signal with a cellular response through relay steps."),
          [ch("The cell makes a response, the signal is relayed inside the cell, and the ligand binds a receptor", "This reverses the order. The response is the last step."),
           ch("The signal is relayed inside the cell, the ligand binds a receptor, and the cell makes a response", "A signal cannot be relayed before the ligand has bound the receptor."),
           ch("The ligand binds a receptor, the cell makes a response, and the signal is relayed inside the cell", "The relay of the signal takes place before the response.")],
          "Reception, transduction (relay), response.", difficulty="easy")

    B.mcq(2, "Which statement best explains why a receptor responds to one kind of ligand and not to others?",
          ch("The ligand-binding domain of the receptor recognizes a specific chemical messenger, so only that ligand binds to it.", "The binding domain has a shape that recognizes a specific peptide or small molecule."),
          [ch("The receptor binds any ligand that is present, and the cell decides which ligands to respond to inside the nucleus.", "A receptor binds specific ligands. It does not bind every ligand that is present."),
           ch("The receptor responds only to the ligands that are made by the same cell that carries the receptor in its membrane.", "Receptors respond to ligands from other cells as well, and the specificity comes from the binding domain."),
           ch("The receptor is made of lipid, so it binds only to the ligands that are made of lipids and no other kinds of molecules.", "Receptor proteins are proteins, and their binding domains recognize both peptide and small-molecule ligands.")],
          "The ligand-binding domain of a receptor recognizes a specific chemical messenger.", difficulty="medium")

    B.mcq(2, "A steroid hormone is a small, nonpolar molecule that can cross the plasma membrane of a cell. Where is the receptor for such a hormone most likely to be located?",
          ch("Inside the target cell, in the cytoplasm or in the nucleus, because the hormone can enter the cell", "Receptors may be on the cell surface or in the cytoplasm or nucleus. A ligand that can cross the membrane can bind a receptor inside."),
          [ch("Only on the outside surface of the plasma membrane, because all of the receptors for hormones are exposed to the blood", "Receptors can be inside the cell, in the cytoplasm or the nucleus."),
           ch("Only in the lipid bilayer of the plasma membrane, because the hormone is nonpolar and dissolves in the fatty acid tails", "A receptor that is a protein is not located only in the bilayer, and an internal receptor is possible."),
           ch("Only in the cell wall of the target cell, because the hormone must be stopped before it enters the cell membrane", "Animal cells do not have cell walls, and the receptor is not located to stop the hormone from entering.")],
          "Receptors may be on the surface of a target cell or in its cytoplasm or nucleus.", difficulty="medium")

    B.mcq(2, "After a ligand binds to a G protein-coupled receptor in the plasma membrane, which change occurs in the receptor?",
          ch("The part of the receptor that lies inside the cell changes shape, which starts the transduction of the signal.", "After the ligand binds, the intracellular domain of the receptor changes shape and initiates transduction."),
          [ch("The receptor moves out of the plasma membrane and into the nucleus, where it copies the ligand into a new molecule.", "The receptor does not leave the membrane to copy the ligand."),
           ch("The receptor breaks down the ligand into amino acids, which then diffuse to the nucleus and start the response.", "The ligand is not broken down by the receptor to start the response."),
           ch("The receptor becomes a part of the lipid bilayer, which makes the membrane unable to bind any more ligand molecules.", "The receptor changes shape and continues to be a signaling protein.")],
          "Binding of the ligand causes the intracellular domain of the receptor to change shape.", difficulty="medium")

    B.mcq(2, "Cyclic AMP (cAMP) is often involved in signal transduction pathways. Which statement best describes the role of cAMP?",
          ch("It is a second messenger that relays and amplifies the signal inside the cell after the receptor is activated.", "Enzymes and second messengers such as cAMP relay and amplify the intracellular signal."),
          [ch("It is the ligand that binds to the receptor on the outside of the cell and starts the pathway in the membrane.", "The ligand is the extracellular signal, and cAMP acts inside the cell."),
           ch("It is a receptor protein that spans the plasma membrane and changes shape when the hormone arrives at the cell.", "cAMP is a small molecule and not a receptor protein."),
           ch("It is a transcription factor that binds to the DNA of the cell and copies the genes into messenger RNA molecules.", "A second messenger relays the signal. It does not copy genes into mRNA.")],
          "Second messengers such as cAMP relay and amplify the intracellular signal.", difficulty="medium")

    r1, r2, r3 = 1, 20, 50
    total = r1 * r2 * r3
    assert total == 1000
    B.mcq(2, f"One ligand molecule binds to one receptor and activates it. In the cell, each activated receptor activates {r2} molecules of a relay protein, and each activated relay protein activates {r3} molecules of an enzyme. How many enzyme molecules are activated by one ligand molecule?",
          ch("1,000", "The signal is amplified at each step: 1 receptor x 20 relay proteins x 50 enzyme molecules = 1,000 enzyme molecules.", 1000),
          [ch("70", "This adds the numbers (1 + 20 + 50). The amplification at each step multiplies the number of molecules.", 70),
           ch("50", "This counts only the final step of the cascade. The relay proteins were also activated in large numbers.", 50),
           ch("20", "This counts only the first step. The activated relay proteins each activate many enzyme molecules.", 20)],
          "A cascade amplifies a signal because each step multiplies the number of activated molecules.", difficulty="medium")

    B.mcq(2, "Many signal transduction pathways include a phosphorylation cascade. Which statement best describes a phosphorylation cascade?",
          ch("One protein kinase adds a phosphate group to the next protein, activating it, and this continues in a series of steps.", "A cascade of protein modifications by phosphorylation relays the signal and often amplifies it."),
          [ch("One protein removes the DNA from the next protein, and this continues in a series of steps until the nucleus is reached.", "Phosphorylation involves the addition of a phosphate group and does not involve removing DNA."),
           ch("A single protein adds a phosphate group to the ligand, so the ligand can be recognized by every receptor in the cell.", "The cascade modifies proteins inside the cell, not the ligand outside it."),
           ch("Each protein destroys the one before it, and the response is produced only when all of the proteins have been destroyed.", "A cascade relays the signal by activating the next component, not by destroying the previous one.")],
          "Phosphorylation cascades relay a signal by activating one protein after another.", difficulty="medium")

    B.mcq(2, "A ligand binds to a protein in the plasma membrane that forms a channel, and the channel opens. Which term describes this type of receptor?",
          ch("A ligand-gated channel, because the binding of the ligand causes the channel to open or close", "The binding of ligands to ligand-gated channels can cause the channel to open or close."),
          [ch("A second messenger, because it relays the signal from the surface of the cell to the inside of the nucleus", "A second messenger is a small molecule inside the cell, and a channel is a membrane protein."),
           ch("A phosphorylation cascade, because it adds phosphate groups to a series of proteins that are located inside the cell", "A channel that opens when the ligand binds is not a cascade of phosphorylation."),
           ch("A transcription factor, because it binds to the DNA and starts the copying of a gene into messenger RNA", "A channel is in the plasma membrane. A transcription factor works on the DNA.")],
          "Ligand-gated channels open or close when a ligand binds.", difficulty="medium")

    B.mcq(2, "G protein-coupled receptors are an example of a type of receptor protein in eukaryotic cells. Which statement best describes a receptor of this type?",
          ch("It is a membrane protein that binds a ligand outside the cell and relays the signal to components inside the cell.", "Receptor proteins recognize a chemical messenger and, after it binds, start the transduction of the signal inside the cell."),
          [ch("It is a protein inside the nucleus that copies the ligand into messenger RNA and sends the copy to the cytoplasm.", "A receptor does not copy the ligand. It relays the signal."),
           ch("It is a lipid in the plasma membrane that releases the ligand into the cytoplasm after the lipid has been broken down.", "Receptors are proteins and not lipids, and the ligand does not need to enter the cell for the receptor to work."),
           ch("It is a protein that carries the ligand across the plasma membrane and then releases it to the DNA of the target cell.", "A cell-surface receptor passes on the signal and does not usually carry the ligand across the membrane.")],
          "G protein-coupled receptors are receptor proteins that start signal transduction after a ligand binds.", difficulty="medium")

    ko_rows = [("Normal cells", "Yes", "Cell division"), ("Cells without the receptor", "Yes", "None"), ("Cells without kinase 2", "Yes", "None"), ("Cells without kinase 2, with a drug that activates the transcription factor directly", "Yes", "Cell division")]
    B.mcq(2, "Researchers study a pathway in which a growth factor causes cell division. They add the growth factor to four cell types and record the response, as shown in the table. Which conclusion is best supported by the data?",
          ch("Kinase 2 acts between the receptor and the transcription factor, because activating the transcription factor directly restores the response in cells that lack kinase 2.", "Without kinase 2 there is no response, but a drug that activates the transcription factor gives a response, so the transcription factor acts after kinase 2."),
          [ch("Kinase 2 acts after the transcription factor, because cells that lack kinase 2 do not divide when the growth factor is added.", "The response returns when the transcription factor is activated directly, so kinase 2 acts before it."),
           ch("The receptor is not needed for the response, because the cells that lack the receptor have had the growth factor added to them.", "The cells without the receptor have no response, so the receptor is needed."),
           ch("The growth factor acts inside the cell and not at a receptor, because the drug is able to produce the same response as the growth factor.", "The drug bypasses the earlier steps. This does not show that the growth factor acts inside the cell.")],
          "Comparing mutants, and bypassing a step with a drug, shows the order of the components of a pathway.",
          diagram=table(["Cell type", "Growth factor added", "Response"], ko_rows, caption="Responses of four cell types", row_headers=True), difficulty="hard")

    # ------------------------------------------------------------------ 4.3 Signal transduction pathways
    B.mcq(3, "Which of the following can be a cellular response to a signal transduction pathway?",
          ch("A change in gene expression, a change in cell function, or programmed cell death, which is called apoptosis", "Signal transduction can change gene expression and function, which may alter phenotype, or result in apoptosis."),
          [ch("A change in the sequence of the DNA of every gene in the cell, which is a permanent change in its genotype", "Signaling changes how genes are used. It does not change the DNA sequence of every gene."),
           ch("A change in the type of ligand that the cell receives from the neighboring cells in the surrounding tissue", "The response is a change in the cell that receives the signal."),
           ch("A change in the shape of the ligand, which turns it into a receptor protein that is built into the cell membrane", "A ligand is not turned into a receptor in response to a signal.")],
          "Signal transduction can change gene expression and cell function or lead to apoptosis.", difficulty="easy")

    B.mcq(3, "A mutation changes the intracellular domain of a receptor so that it cannot change shape when the ligand binds. Which effect is most likely?",
          ch("The ligand can still bind the receptor, but the signal is not transduced, so the cell does not make the response.", "Mutations in any domain of a receptor can alter the transduction of the signal to the downstream components."),
          [ch("The ligand cannot bind the receptor, so the cell responds as if the ligand were absent and makes the normal response.", "The mutation is in the intracellular domain, so the ligand-binding domain still works."),
           ch("The cell makes the response all of the time, because the receptor no longer needs the ligand to start the pathway.", "A receptor that cannot change shape cannot start the pathway at all."),
           ch("The ligand is changed into a different molecule, which causes the cell to respond to many other signals as well.", "The ligand is not changed by the mutation of the receptor.")],
          "A mutation in any domain of the receptor can alter the transduction of the signal.", difficulty="medium")

    B.mcq(3, "A drug has a shape like that of a ligand. It binds to the ligand-binding domain of the receptor but does not cause the receptor to change shape. Which effect is most likely?",
          ch("The drug blocks the pathway, because it occupies the receptor, so the real ligand cannot bind and start the signal.", "Chemicals that interact with a component of a pathway can inhibit it."),
          [ch("The drug activates the pathway, because anything that binds to the receptor is able to start the response in the cell.", "The receptor changes shape only if the drug activates it, and here it does not."),
           ch("The drug has no effect on the pathway, because only the ligand is able to bind the ligand-binding domain of the receptor.", "A molecule with a similar shape can bind the domain and so block the real ligand."),
           ch("The drug destroys the receptor, which removes the pathway from the cell permanently after one dose of the drug.", "Nothing in the description suggests that the receptor is destroyed.")],
          "Chemicals that interact with a signaling component may inhibit the pathway.", difficulty="medium")

    B.mcq(3, "A chemical inhibits a protein kinase in the middle of a phosphorylation cascade. Which prediction is most consistent with this change?",
          ch("The proteins after the inhibited step will not be activated, so the cell will not make the response even if the ligand binds.", "A chemical that interacts with a component of the pathway can inhibit it, and this blocks the downstream components."),
          [ch("The proteins after the inhibited step will be activated by other signals, so the response will be larger than normal.", "Nothing in the description supports activation by other signals."),
           ch("The proteins before the inhibited step will be destroyed, so the receptor will no longer be in the plasma membrane.", "Inhibiting a kinase does not destroy the components before it."),
           ch("The ligand will no longer bind the receptor, because the kinase is necessary for the ligand to reach the surface of the cell.", "The kinase works inside the cell and does not affect the binding of the ligand.")],
          "Inhibiting one component of a cascade blocks the components that follow it.", difficulty="medium")

    B.mcq(3, "A mutation makes a protein kinase near the start of a growth-factor pathway active all of the time, even when no growth factor is present. Which prediction is most consistent with this mutation?",
          ch("The cell will make the response, such as cell division, without a signal, which could lead to uncontrolled cell division.", "A mutation in any component of the pathway can change downstream events. An always-active kinase keeps the pathway on."),
          [ch("The cell will never make the response, because a kinase that is always active cannot pass the signal to the next protein.", "An always-active kinase continues to activate the proteins after it."),
           ch("The cell will make the response only when the growth factor is present, because the receptor must still be active.", "The kinase is active without the ligand, so the response does not depend on the receptor."),
           ch("The cell will undergo apoptosis at once, because every active kinase causes a cell to destroy itself by programmed death.", "Not every active kinase leads to apoptosis, and this pathway is a growth pathway.")],
          "A mutation can make a pathway active without a signal.", difficulty="hard")

    B.mcq(3, "During the development of a human hand, the tissue between the fingers is removed. Which cellular response, triggered by signal transduction, best accounts for this?",
          ch("Apoptosis, which is the programmed death of the cells between the fingers and so removes the tissue that lies between them", "Signal transduction can result in programmed cell death, and removal of tissue during development is an example."),
          [ch("Mitosis, which is the division of the cells to make new cells between the fingers and so to enlarge the tissue", "Mitosis would add cells and would not remove the tissue."),
           ch("Active transport, which is the movement of ions by pumps and which makes the cells between the fingers swell", "Active transport does not remove tissue."),
           ch("Endocytosis, which is the taking in of the material by the cell membrane and which makes the cells between the fingers larger", "Endocytosis does not account for the removal of cells.")],
          "Signal transduction can result in programmed cell death (apoptosis).", difficulty="medium")

    B.mcq(3, "Yeast cells of one mating type release a pheromone that binds to receptors on yeast cells of the other mating type. Which response is most likely in the cells that receive the pheromone?",
          ch("A change in gene expression, in which genes that are needed for mating are turned on in the cells that receive it", "Mating pheromones in yeast trigger the expression of mating genes through a signal transduction pathway."),
          [ch("A change in the sequence of the yeast DNA, in which the genes needed for mating are made from new nucleotides", "Signaling changes gene expression and does not rewrite the DNA sequence."),
           ch("A change in the cell wall into a rigid shell, in which the cell stops responding to any signal for the rest of its life", "The pheromone triggers a response that prepares the cell for mating."),
           ch("A change in the pheromone into a receptor, in which the cell starts to bind the pheromone that it has released", "A signal is not changed into a receptor by the response to it.")],
          "Signal transduction can change gene expression, as in the response of yeast cells to mating pheromones.", difficulty="medium")

    B.mcq(3, "In a liver cell, epinephrine binds to a receptor on the cell surface, and this leads through a signal transduction pathway to the breakdown of glycogen to glucose. Which statement best describes the response of the liver cell?",
          ch("The signal changes the function of the cell, since glycogen is broken down to release glucose, without changing its DNA.", "Signal transduction can alter cell function, and epinephrine stimulates the breakdown of glycogen in mammals."),
          [ch("The signal enters the nucleus and rewrites the sequence of the genes, so the cell can break down glycogen from then on.", "A signal transduction pathway changes how the cell functions and does not rewrite the DNA sequence."),
           ch("The signal is broken down by the cell into glucose, so the glucose that is released comes from the epinephrine itself.", "The glucose comes from glycogen, not from the epinephrine."),
           ch("The signal causes the cell to make more receptors, so the epinephrine that binds is removed from the blood for good.", "The response described is the breakdown of glycogen.")],
          "Signal transduction can change cell function, as when epinephrine stimulates glycogen breakdown.", difficulty="hard")

    B.mcq(3, "Which statement best describes how signal transduction pathways contribute to the development of the body plan of an embryo?",
          ch("Signals between cells change gene expression in the cells that receive them, which affects how those cells specialize and where body parts form.", "Signaling pathways regulate gene expression during embryonic development, for example with morphogens and with the HOX genes that regulate body plans."),
          [ch("Signals between cells change the DNA sequence of the cells that receive them, which gives each body part its own set of genes.", "Cells in an embryo carry the same DNA. Signals change which genes are expressed."),
           ch("Signals between cells are not used in development, because each cell of the embryo follows a plan that is stored only in its own cytoplasm.", "Cells in an embryo communicate, and signals help to direct development."),
           ch("Signals between cells cause the cells of the embryo to stop dividing, which fixes the final shape of the body at an early stage.", "Signaling can promote or limit division, but the shape of the body results from the pattern of gene expression.")],
          "Signals regulate gene expression in embryonic development.", difficulty="hard")

    dr = [(0, 0), (1, 38), (2, 62), (5, 88), (10, 98), (20, 100)]
    dose = graph("Concentration of ligand (nM)", "Response of the cell (% of maximum)", 0, 20, 0, 100,
                 [line("Response", dr, "blue")],
                 "Response against ligand concentration. The response rises steeply from 0 at 0 nanomolar to about 88 percent at 5 nanomolar and then levels off at about 100 percent by 20 nanomolar.")
    B.mcq(3, "The graph shows the response of a cell to different concentrations of a ligand. Which statement best explains why the response levels off at high ligand concentrations?",
          ch("Nearly all of the receptors are occupied at high concentrations, so adding more ligand cannot activate more receptors.", "The number of receptors is limited. When they are all bound, the response reaches its maximum."),
          [ch("The cell destroys the extra ligand at high concentrations, so none of it can bind to a receptor in the membrane.", "Nothing in the data suggests that the cell destroys the ligand."),
           ch("The ligand turns into a different molecule at high concentrations, so it is no longer recognized by the receptor.", "A ligand does not change into a different molecule because of its concentration."),
           ch("The receptors are removed by the cell as the ligand concentration rises, so the response falls to zero at high concentrations.", "The graph shows the response leveling off near 100 percent and not falling to zero.")],
          "A limited number of receptors sets a maximum response.", diagram=dose, difficulty="hard")
