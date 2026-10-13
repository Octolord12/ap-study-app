"""Unit 3, topic 3.3 Cellular Energy (10 questions).

Required content (CED 2025-26): 3.3.A.1 all living systems need an input of energy; 3.3.A.2 life is highly ordered and does not violate the first and
second laws of thermodynamics (energy input must exceed energy loss; releasing processes may be coupled to requiring ones; a significant loss of order or
energy flow means death); 3.3.A.3 pathways are sequential for more controlled transfer, the product of one step typically the reactant of the next;
3.3.B.1 core pathways (glycolysis, oxidative phosphorylation) are conserved across Archaea, Bacteria and Eukarya, which supports common ancestry.
Excluded by the CED: the Gibbs free energy equation (so none is used here). Suggested skill 6.C: justify a claim by connecting evidence to theory.
"""
from lib import *


def build(B):
    B.mcq(3, "Which statement best explains why living cells need a continual input of energy?",
          ch("Energy is needed to maintain the highly ordered structure of the cell, and some is lost to the surroundings as heat.",
             "Cells are highly ordered, and maintaining that order and powering processes requires energy. Energy transfers are never perfectly efficient, so some energy is released as heat."),
          [ch("Cells make new energy during chemical reactions, and this energy must be replaced when it is released.",
              "Energy cannot be created. Cells transfer energy that is already present in their food or in sunlight."),
           ch("Cells need energy only when they divide or grow, because other cell processes do not use energy.",
              "Transport, synthesis, movement and many other cell processes use energy continuously."),
           ch("Once cells have stored enough energy, the first law of thermodynamics requires them to release all of that energy as heat.",
              "The first law says energy is conserved. It does not require cells to release stored energy.")],
          "All living systems require an input of energy to maintain order and to power cellular processes.", difficulty="easy")

    B.mcq(3, "A student claims that a living cell, which is highly ordered, must violate the second law of thermodynamics. Which response is best?",
          ch("The cell does not violate the law: it takes in energy and releases heat, so the disorder of its surroundings increases.",
             "A cell is not an isolated system. Energy input lets it maintain order, and the heat it releases increases the disorder of the surroundings."),
          [ch("Cells are alive, so the laws of thermodynamics do not apply to them in the same way that they apply to nonliving matter such as rocks.", "The laws of thermodynamics apply to all matter and energy, including living systems."),
           ch("The cell does violate the law, but only for as long as it remains alive and is able to grow.", "A living cell does not violate the law at any point. Its order is paid for by energy input."),
           ch("The cell avoids the law by making new energy from nothing, which is what keeps the cell ordered.", "Energy cannot be made from nothing. That would violate the first law of thermodynamics.")],
          "Living systems maintain order by an input of energy and do not violate the first or second laws of thermodynamics.", difficulty="medium")

    B.mcq(3, "A cell is exposed to conditions in which its rate of energy input stays well below its rate of energy loss for a long time. Which outcome is most likely?",
          ch("The cell can no longer maintain its order or power its processes, and it eventually dies.", "Energy input must exceed energy loss for a cell to maintain order. A significant loss of order or energy flow results in death."),
          [ch("The cell becomes more highly ordered, because less energy is available to be lost.", "Order requires energy input. With too little energy, order is lost, not gained."),
           ch("The cell makes up the difference by converting its own waste heat back into useful energy.", "Heat released to the surroundings is not recaptured by the cell to do work."),
           ch("The cell continues to function normally, because the first law ensures that energy is never lost.", "Energy is conserved overall, but a cell loses usable energy to the surroundings. If it is not replaced, the cell cannot function.")],
          "For a cell to maintain order, energy input must exceed energy loss.", difficulty="medium")

    B.mcq(3, "Which statement best describes coupled reactions in cells?",
          ch("An energy-releasing reaction, such as ATP hydrolysis, is linked to an energy-requiring reaction and drives it.",
             "Coupling lets energy released in one process be used by a process that requires energy."),
          [ch("Two reactions that both require energy take place at the same time in the same part of the cell.", "Coupling involves one process that releases energy and one that requires it."),
           ch("Two reactions that are catalyzed by the same enzyme, which therefore works twice as fast on each of the two reactions.", "Coupling is about energy transfer between processes. It is not about two reactions sharing an enzyme."),
           ch("Reactions in which the product of one reaction is destroyed before the next reaction can use it.", "In coupled reactions, the energy released by one process is used by the other, not wasted by destroying a product.")],
          "Coupling links an energy-releasing process to an energy-requiring process.", difficulty="medium")

    B.mcq(3, "Many cellular processes that release energy occur through a series of small steps rather than in a single reaction. Which statement best explains the advantage of a series of steps?",
          ch("A sequence of steps allows energy to be transferred in a more controlled way, with each product becoming the next reactant.", "In a metabolic pathway, the product of one reaction is typically the reactant of the next, so energy is released and transferred gradually."),
          [ch("Each step creates a small amount of new energy, and the amounts add up to a much larger total than a single reaction would give.", "Energy is not created in any step. It is transferred between molecules, with some lost as heat."),
           ch("A series of steps makes sure that all of the energy released is lost as heat to the surroundings of the cell.", "A pathway transfers much of the energy to molecules such as ATP rather than losing it all as heat."),
           ch("A single large reaction could not be catalyzed by an enzyme, so the process must be divided into steps.", "Enzymes can catalyze reactions of many sizes. The advantage of steps is controlled energy transfer.")],
          "Sequential pathways allow a more controlled transfer of energy.", difficulty="medium")

    B.mcq(3, "A mutation in a cell prevents it from converting ADP and inorganic phosphate to ATP. Which prediction about the cell is best supported by what is known about energy in living systems?",
          ch("Processes that need energy, such as active transport and synthesis, will slow or stop, and the cell will die.", "ATP couples energy-releasing processes to energy-requiring ones. Without ATP production the cell cannot maintain its order or power its processes."),
          [ch("Processes that require energy will continue unchanged, because energy cannot be lost from a cell once it is taken in.", "Cells lose energy to the surroundings. Without a new input of usable energy, processes that need energy slow down."),
           ch("The cell will become more highly ordered, because it is no longer using energy to make ATP and so wastes less.", "A cell maintains order by using energy. Without it, order is lost."),
           ch("The cell will use the heat it releases to make ATP, so there will be little change in the cell's function.", "Heat released to the surroundings is not recaptured to make ATP.")],
          "Cells that cannot make ATP lose the ability to maintain order and eventually die.", difficulty="hard")

    B.mcq(3, "Glycolysis is found in organisms in the domains Bacteria, Archaea and Eukarya. Which statement best explains how this observation supports the claim that all living organisms share a common ancestor?",
          ch("A pathway present in all three domains was most likely inherited from a common ancestor that already had the pathway.", "Core metabolic pathways such as glycolysis are conserved across all domains. A feature shared by all groups is best explained by inheritance from a common ancestor."),
          [ch("Glycolysis requires no enzymes, so any organism can carry it out without having inherited the ability from an ancestor.", "Glycolysis is a series of enzyme-catalyzed reactions. Its presence in all three domains is evidence of shared ancestry."),
           ch("Glycolysis occurs only in organisms that have mitochondria, which shows that they are closely related.", "Glycolysis occurs in the cytosol of cells with or without mitochondria."),
           ch("Each domain evolved glycolysis independently, which shows that the pathway is the best way to release energy.", "The claim of common ancestry rests on a shared, inherited pathway, not on independent origins.")],
          "Conserved pathways across the three domains are evidence for common ancestry.", difficulty="medium")

    org_rows = [("Organism 1", "Bacteria", "Yes", "Yes"), ("Organism 2", "Bacteria", "Yes", "No"), ("Organism 3", "Archaea", "Yes", "No"), ("Organism 4", "Eukarya", "Yes", "Yes")]
    B.mcq(3, "A researcher tests four organisms from three domains for the enzymes of two metabolic pathways. The results are shown in the table. Which claim is best supported by the data?",
          ch("Glycolysis was found in organisms from all three domains, which supports the claim that they share a common ancestor with the pathway.", "A pathway found in every organism tested, across three domains, is consistent with its being inherited from a common ancestor."),
          [ch("Oxidative phosphorylation is older than glycolysis, because it is found in the organisms that are the most complex of the four that were tested.", "The data show that glycolysis is present in all four organisms and oxidative phosphorylation in only two."),
           ch("Organisms that lack oxidative phosphorylation cannot make any ATP, because oxidative phosphorylation is the only pathway that makes ATP.", "Every organism in the table has glycolysis, which forms ATP. The data do not show that ATP cannot be made."),
           ch("Because oxidative phosphorylation is missing in some organisms, the data provide no evidence for common ancestry.", "The presence of glycolysis in every organism is evidence for common ancestry, even though one pathway is not found in all of them.")],
          "Evidence for common ancestry comes from features shared by organisms in different groups, such as glycolysis.",
          diagram=table(["Organism", "Domain", "Glycolysis enzymes detected", "Oxidative phosphorylation enzymes detected"], org_rows, caption="Metabolic pathways in four organisms", row_headers=True), difficulty="hard")

    intake, stored = 1000, 400
    released = intake - stored
    assert released == 600
    B.mcq(3, f"A cell takes in {intake:,} J of chemical energy from its food. During a series of reactions, {stored} J of this energy is transferred to molecules of ATP. According to the first law of thermodynamics, what happened to the remaining {released} J?",
          ch(f"It was transferred to the surroundings, mostly as heat.", "Energy cannot be destroyed. The energy that was not stored in ATP was released to the surroundings, mostly as heat."),
          [ch(f"It was destroyed during the reactions.", "The first law says that energy cannot be created or destroyed."),
           ch(f"It was stored in the cell as additional ATP that has not yet been measured.", "The question states that the energy transferred to ATP is 400 J. The rest was not stored in ATP."),
           ch(f"It was converted into new matter in the cell.", "The energy released in these reactions is not converted into matter. Most of it is lost as heat.")],
          "Energy is conserved. Energy that is not captured in a useful form is released to the surroundings, mostly as heat.", difficulty="medium")

    B.mcq(3, "A student claims that a reaction that builds a large molecule from smaller ones, which requires an input of energy, can occur on its own if enough of the right enzyme is present. Which response best evaluates the claim?",
          ch("The claim is not supported, because enzymes do not supply energy; the reaction must be coupled to an energy-releasing one.", "Enzymes speed up reactions but do not provide energy. Energy-requiring reactions in cells are coupled to processes that release energy."),
          [ch("The claim is supported, because enzymes provide the energy needed by reactions that build large molecules from small ones in cells.", "Enzymes do not provide energy to reactions."),
           ch("The claim is supported, because adding more enzyme lowers the amount of energy the reaction needs to the point of zero.", "More enzyme can increase the rate. It does not remove the need for energy input."),
           ch("The claim is not supported, because the large molecules of cells are built without the help of enzymes in most cases.", "Enzymes catalyze the synthesis of most large molecules in cells. The problem is energy, not the presence of enzymes.")],
          "Enzymes do not supply energy. Reactions that require energy are coupled to reactions that release it.", difficulty="hard")
