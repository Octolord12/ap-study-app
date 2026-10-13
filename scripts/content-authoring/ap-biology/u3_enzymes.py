"""Unit 3, topics 3.1 Enzymes (12 questions) and 3.2 Environmental Impacts on Enzyme Function (14).

Required content (CED 2025-26): 3.1.A.1 enzymes are protein catalysts that lower activation energy; 3.1.A.2 the substrate's shape and charge must be
compatible with the active site (enzyme-substrate complex); 3.2.A denaturation by temperature, pH or chemicals (disrupting hydrogen bonds), sometimes
reversible; 3.2.B substrate/product concentrations, temperature up to the optimum raises collision frequency, competitive inhibitors bind the active site
reversibly, noncompetitive inhibitors bind allosteric sites. Suggested skills: 1.B explain, 3.C experimental procedures and controls, 6.E predict effects.
"""
from lib import *


def build(B):
    # ------------------------------------------------------------------ 3.1 Enzymes
    B.mcq(1, "Which statement correctly describes how an enzyme affects a chemical reaction in a cell?",
          ch("It lowers the activation energy of the reaction, so the reaction proceeds faster.",
             "Enzymes are protein catalysts. By lowering the activation energy they let many more collisions between substrate molecules lead to product."),
          [ch("It supplies the energy the reactants need to reach the transition state, using energy stored in the enzyme.",
              "An enzyme does not provide energy to a reaction. It lowers the energy barrier that the reactants must cross."),
           ch("It changes the reaction so that its products hold more energy than the substrates had at the start.",
              "An enzyme does not change the energy of the substrates or of the products. It changes only how quickly the reaction proceeds."),
           ch("It is used up as the reaction proceeds, so more enzyme must be made for every reaction that occurs.",
              "An enzyme is not consumed. It is released unchanged and can catalyze the same reaction again.")],
          "Enzymes are biological catalysts: they speed up a reaction by lowering its activation energy without being used up.", difficulty="easy")

    B.mcq(1, "A student states that an enzyme catalyzes a reaction only when the substrate is compatible with the enzyme's active site. What does it mean for a substrate to be compatible?",
          ch("The substrate's shape and charge match the active site, so it can form an enzyme-substrate complex.",
             "Binding depends on both the shape and the charge distribution of the substrate and the active site, which is why most enzymes act on only one or a few substrates."),
          [ch("The substrate is a protein built from the same amino acids as the enzyme, so the two can bind each other.",
              "Compatibility does not depend on the substrate's composition. Many enzymes act on carbohydrates, lipids or nucleic acids."),
           ch("The substrate and the active site are about the same size, even if their charges are very different.",
              "Size alone is not enough. The charges of the substrate and the active site must also fit, or the substrate will not bind."),
           ch("The substrate carries the same charge as the active site, so the two are strongly attracted to each other.",
              "Like charges repel. Binding is favored when the charges and shapes are complementary, not identical.")],
          "The enzyme-substrate complex forms when the substrate's shape and charge are compatible with the active site.", difficulty="medium")

    ea_graph = graph("Reaction progress", "Free energy (kJ/mol)", 0, 10, 0, 120,
                     [line("Without enzyme", [(0, 30), (5, 120), (10, 0)], "blue"), line("With enzyme", [(0, 30), (5, 60), (10, 0)], "red")],
                     "Free energy against reaction progress for one reaction with and without an enzyme. Both start at 30 and end at 0 kJ/mol. The uncatalyzed curve peaks at 120 and the catalyzed curve peaks at 60.")
    ea_no, ea_yes = 120 - 30, 60 - 30
    lowered = ea_no - ea_yes
    released = 30 - 0
    assert (ea_no, ea_yes, lowered, released) == (90, 30, 60, 30)
    B.mcq(1, "The graph shows the free energy of the same reaction with and without an enzyme. By how much does the enzyme lower the activation energy of the reaction?",
          ch("60 kJ/mol", "The activation energy is the rise from the energy of the reactants (30) to the top of the curve: 120 - 30 = 90 kJ/mol without the enzyme and 60 - 30 = 30 kJ/mol with it. The enzyme lowers it by 90 - 30 = 60 kJ/mol.", lowered),
          [ch("90 kJ/mol", "This is the activation energy without the enzyme (120 - 30). The question asks for how much the enzyme lowers it, which is a difference between the two curves.", ea_no),
           ch("30 kJ/mol", "This is the activation energy with the enzyme (60 - 30), which is also the energy released by the reaction (30 - 0). Neither is the amount the enzyme lowers the activation energy.", ea_yes),
           ch("120 kJ/mol", "This is the height of the uncatalyzed peak. Activation energy is measured from the energy of the reactants up to the peak, not from zero.", 120)],
          "Subtract the energy of the reactants from each peak to find the two activation energies, then subtract them.", diagram=ea_graph, difficulty="easy")

    B.mcq(1, "Which conclusion about the enzyme-catalyzed reaction is best supported by the graph?",
          ch("The energy released is the same with or without the enzyme, but the enzyme lowers the energy barrier.",
             "Both curves start at the same energy and end at the same energy, so the energy released is unchanged. Only the height of the peak, the activation energy, differs."),
          [ch("The enzyme makes the products lower in energy than they would be without the enzyme, so more energy is released.",
              "Both curves end at the same level, so the products have the same energy either way."),
           ch("The enzyme raises the energy of the reactants, which makes it easier for the reaction to get started.",
              "Both curves start at the same energy. The enzyme does not change the energy of the reactants."),
           ch("The enzyme removes the activation energy completely, so the reaction no longer has an energy barrier.",
              "The catalyzed curve still rises to a peak. The enzyme lowers the activation energy; it does not remove it.")],
          "An enzyme changes how fast a reaction proceeds by lowering the peak, not the overall energy change from reactants to products.", diagram=ea_graph, difficulty="medium")

    B.mcq(1, "A student investigates whether the concentration of the enzyme catalase affects the rate at which hydrogen peroxide is broken down. Four tubes receive the same volume of hydrogen peroxide and 0, 1, 2 or 3 mL of catalase solution, with water added so that every tube has the same total volume. The volume of oxygen gas collected in 60 seconds is recorded for each tube. What is the dependent variable?",
          ch("The volume of oxygen gas collected in 60 seconds", "The dependent variable is the quantity that is measured and expected to respond to the change the student makes. Here that is the oxygen collected."),
          [ch("The volume of catalase solution added to each tube", "This is the independent variable, the factor the student deliberately changes from tube to tube."),
           ch("The volume of hydrogen peroxide in each tube", "This is kept the same in every tube, so it is a controlled variable, not the measured outcome."),
           ch("The total volume of liquid in each tube", "The student adds water to keep this the same in every tube, so it is a controlled variable.")],
          "Independent variable: what is changed. Dependent variable: what is measured. Controlled variables: what is held constant.", difficulty="medium")

    B.mcq(1, "In the catalase investigation, one tube contains the hydrogen peroxide and 3 mL of water but no catalase. What is the purpose of this tube?",
          ch("It shows how much oxygen forms without the enzyme, so the effect of catalase can be identified.",
             "A control tube lacking only the factor being tested provides the baseline. Any oxygen in the other tubes beyond this baseline can be attributed to the catalase."),
          [ch("It provides a constant amount of enzyme in each trial, which the other tubes can be compared with.",
              "The tube contains no enzyme. Its purpose is to show what happens without it."),
           ch("It shows that hydrogen peroxide is the only substrate that catalase is able to act on.",
              "A tube without the enzyme cannot show anything about which substrates the enzyme acts on. That would need other substrates to be tested."),
           ch("It reduces random error in the volume measurements by averaging the results from all four tubes.",
              "Averaging is done with repeated trials. A control tube is not a replicate; it tests a different condition.")],
          "A control lets the investigator attribute the results to the factor being tested, here the presence of the enzyme.", difficulty="medium")

    B.mcq(1, "A mutation replaces an amino acid in the active site of an enzyme. The substrate is positively charged and is normally held at the active site by attraction to a negatively charged R group. The new amino acid has a positively charged R group. Which outcome is most likely?",
          ch("The substrate binds less tightly or not at all, so the rate of the reaction decreases.",
             "The positively charged R group now repels the positively charged substrate, so the substrate is no longer held in the active site and the enzyme-substrate complex forms less often."),
          [ch("The substrate binds more tightly, so the reaction rate increases because the substrate stays at the active site longer.",
              "Two positive charges repel each other. The change removes the attraction that held the substrate in place."),
           ch("The reaction rate is unchanged, because the active site recognizes a substrate by its overall size only.",
              "Both shape and charge determine whether a substrate fits. Changing the charge of an active-site R group can change binding."),
           ch("The enzyme can now bind any positively charged molecule, so its activity increases.",
              "A change like this usually reduces the match with the original substrate. It does not make the enzyme work on every molecule with a positive charge.")],
          "The active site must be compatible with the substrate's shape and charge. Changing the charge of an active-site amino acid can weaken binding.", difficulty="medium")

    rows = [("Substrate only", 0.2), ("Substrate + enzyme", 15.8), ("Substrate + enzyme boiled for 10 min, then cooled", 0.3)]
    B.mcq(1, "A student measures the initial rate of formation of a product from a substrate under three conditions, with the results shown. Which conclusion is best supported by the data?",
          ch("The enzyme must keep its three-dimensional structure to speed up the reaction, since boiling returned the rate to about its value without enzyme.",
             "Boiling destroyed the enzyme's shape and so its ability to catalyze. The rate with boiled enzyme (0.3) is close to the rate with no enzyme (0.2)."),
          [ch("The enzyme is used up as the reaction proceeds, which explains why the rate is so high in the second condition but not the third.",
              "The data say nothing about the enzyme being consumed. Enzymes are not used up in the reactions they catalyze."),
           ch("The reaction does not need a working enzyme, since the substrate is converted to product in all three conditions at some rate.",
              "The rates in the first and third conditions are very small compared with 15.8. The enzyme is needed for the high rate."),
           ch("Boiling made the enzyme more active, but the cooling that followed lowered the rate again almost to zero.",
              "The rate after boiling and cooling is 0.3, almost the rate with no enzyme at all. The enzyme did not become more active.")],
          "Comparing the three conditions: the enzyme raises the rate a great deal, and boiling removes that effect.",
          diagram=table(["Condition", "Initial rate of product formation (µmol/min)"], [(c_, fix(r)) for c_, r in rows], caption="Rate of product formation under three conditions"), difficulty="medium")

    conc = [0, 2, 4, 6, 8]
    rate_per = 0.8
    rates = [round(c_ * rate_per, 1) for c_ in conc]
    assert rates == [0.0, 1.6, 3.2, 4.8, 6.4]
    expected = 10 * rate_per
    assert round(expected, 1) == 8.0
    B.mcq(1, "The table shows the initial rate of an enzyme-catalyzed reaction at different enzyme concentrations. Substrate was present in excess in every trial. If the pattern continues, what rate would be expected at an enzyme concentration of 10 µg/mL?",
          ch("8.0 µmol/min", "The rate rises by 0.8 µmol/min for every 1 µg/mL, so at 10 µg/mL the rate is 10 x 0.8 = 8.0 µmol/min. With substrate in excess, more enzyme means more active sites and a proportionally higher rate.", 8.0),
          [ch("6.4 µmol/min", "This assumes the rate has leveled off at its value at 8 µg/mL. The rate would level off only if substrate ran short, but substrate is in excess.", 6.4),
           ch("16.0 µmol/min", "This multiplies 10 by 1.6, which is the rate gain for each 2 µg/mL step, not for each 1 µg/mL.", 16.0),
           ch("9.6 µmol/min", "This is the expected rate at 12 µg/mL (12 x 0.8). At 10 µg/mL the rate is 8.0 µmol/min.", 9.6)],
          "The data show a constant increase in rate per unit of enzyme, so the rate is proportional to enzyme concentration while substrate is in excess.",
          diagram=table(["Enzyme concentration (µg/mL)", "Initial rate (µmol/min)"], [(c_, fix(r)) for c_, r in zip(conc, rates)], caption="Initial rate at five enzyme concentrations (substrate in excess)"), difficulty="hard")

    B.mcq(1, "Enzyme 1 catalyzes reactions of both substrate X and substrate Y. Enzyme 2 catalyzes the reaction of substrate Y only. X and Y have very similar shapes, but X has an extra negatively charged group. Which statement best explains the difference between the enzymes?",
          ch("Enzyme 1's active site fits the shape and charge of both X and Y, but enzyme 2's active site fits only Y.",
             "Substrate specificity comes from the match between the substrate and the active site. The extra charged group on X prevents it from fitting the active site of enzyme 2."),
          [ch("Enzyme 2 is not a protein, so it is able to act on only one kind of substrate, whereas enzyme 1 is.",
              "Enzymes are proteins (with rare exceptions), and being a protein does not limit an enzyme to one substrate. Specificity comes from the active site."),
           ch("Enzyme 1 supplies more energy to its reactions than enzyme 2 does, so it can act on a wider range of substrates.",
              "Enzymes do not supply energy to reactions. They lower the activation energy."),
           ch("Substrate Y has a lower activation energy than X, so both enzymes react with Y more easily than with X.",
              "This does not explain why enzyme 1 acts on X and enzyme 2 does not. That difference is due to what the active sites can bind.")],
          "An enzyme acts on the substrates whose shape and charge fit its active site.", difficulty="hard")

    B.mcq(1, "After an enzyme molecule has catalyzed a reaction, what is most likely to happen to that enzyme molecule?",
          ch("It is released unchanged and can bind another substrate molecule.", "Enzymes are catalysts. They are not changed by the reactions they speed up, so one enzyme molecule can catalyze many reactions."),
          [ch("It is broken down into amino acids, which are recycled to make new enzymes.", "Enzymes are eventually broken down in cells, but not by catalyzing a reaction. Each use does not destroy the enzyme."),
           ch("It stays attached to the product, so it can no longer bind to a substrate.", "The product is released from the active site. Products that stay bound would stop the enzyme working after one reaction, which is not how catalysts act."),
           ch("It is converted into one of the products of the reaction.", "An enzyme is a protein catalyst, not a reactant. It is not converted into the products.")],
          "An enzyme is a catalyst: it is not used up and can act on many substrate molecules.", difficulty="easy")

    B.mcq(1, "Which statement best describes the enzyme-substrate complex?",
          ch("A temporary association in which the substrate is bound at the enzyme's active site.", "The substrate binds to the active site, the reaction occurs, and the product or products are released."),
          [ch("A permanent bond between the enzyme and the product, which ends the activity of the enzyme.", "The products are released and the enzyme can be used again. The complex is temporary."),
           ch("The structure that forms when two substrate molecules bind to each other before an enzyme acts.", "The complex is formed between an enzyme and a substrate, not between two substrates."),
           ch("A group of enzymes that act one after another in a metabolic pathway and pass products along.", "A series of enzymes in a pathway is not an enzyme-substrate complex, which involves a single enzyme and its substrate.")],
          "The enzyme-substrate complex is the temporary state in which the substrate is bound at the active site.", difficulty="easy")

    # ------------------------------------------------------------------ 3.2 Environmental impacts on enzyme function
    B.mcq(2, "What happens to an enzyme when it is denatured by a high temperature?",
          ch("Hydrogen bonds that maintain its three-dimensional shape are disrupted, so the active site changes and substrate can no longer bind.",
             "Denaturation changes the shape of the protein without breaking the peptide bonds. Because the shape of the active site is lost, the enzyme cannot bind its substrate."),
          [ch("Its peptide bonds break, which separates the polypeptide into individual amino acids that cannot form an active site.", "Denaturation does not break peptide bonds. The order of amino acids stays the same, but the folding is lost."),
           ch("Its active site becomes larger as the protein stretches out, so the enzyme can bind a wider range of substrates.", "A denatured active site does not become a better binding site for more substrates. The loss of shape usually means substrates cannot bind."),
           ch("Its substrate molecules are denatured by the heat as well, so they can no longer fit into any enzyme.", "Denaturation affects the enzyme protein. Substrates are not denatured by the same change.")],
          "Denaturation is a loss of the three-dimensional structure of a protein, which removes its function.", difficulty="easy")

    B.mcq(2, "Pepsin works in the stomach, where the pH is about 2, and its activity is very low at pH 8. Which statement best explains the low activity at pH 8?",
          ch("The change in pH alters the ionic and hydrogen bonds in pepsin, which changes the shape of its active site.",
             "Each enzyme has an optimal pH range. Outside it, changes in charge disrupt the bonds that hold the enzyme's shape."),
          [ch("All enzymes work best at acidic pH, so any enzyme would be slowed at pH 8, as it would be in the small intestine.", "Many enzymes have optimum pH values in the neutral or basic range. Each enzyme has its own optimum."),
           ch("A higher pH raises the activation energy of the reaction itself without affecting the enzyme.", "The pH affects the enzyme's structure, which is why its activity changes. The explanation does not rely on a change to the reaction itself."),
           ch("At pH 8 there are too few hydrogen ions, which pepsin needs as its substrate, for the reaction to occur.", "Pepsin's substrates are proteins, not hydrogen ions.")],
          "Enzymes function best in a particular pH range. Outside it, the enzyme's structure is disrupted.", difficulty="easy")

    temp_graph = graph("Temperature (°C)", "Relative enzyme activity (%)", 0, 100, 0, 100,
                       [line("Human enzyme", [(0, 0), (10, 15), (20, 40), (30, 80), (37, 100), (45, 55), (55, 10), (65, 0), (100, 0)], "blue"),
                        line("Hot-spring bacterial enzyme", [(0, 0), (20, 5), (40, 20), (55, 45), (70, 100), (80, 60), (90, 10), (100, 0)], "red")],
                       "Relative activity against temperature for two enzymes. The human enzyme peaks at 100 percent at 37 degrees and falls to near zero by 65. The bacterial enzyme peaks at 100 percent at 70 degrees.")
    B.mcq(2, "The graph shows the activity of an enzyme from human cells and an enzyme from a bacterium that lives in hot springs at different temperatures. Between 37 °C and 55 °C, the activity of the human enzyme decreases while the activity of the bacterial enzyme increases. Which statement best explains these observations?",
          ch("At 55 °C the human enzyme is denaturing, but the bacterial enzyme keeps its structure and collides with substrate more often than at 37 °C.",
             "A rise in temperature increases collisions between enzyme and substrate until the optimum is passed. Past its optimum an enzyme denatures. The two enzymes have different optimum temperatures."),
          [ch("Hot-spring bacteria make more of their enzyme as the temperature rises, which the human cells cannot do, so it appears more active.", "The graph shows the activity of the enzymes at each temperature, not the amount of enzyme made. Making more enzyme is not shown."),
           ch("The bacterial enzyme has no activation energy, so heat does not affect it, while the human enzyme requires heat to work.", "Every enzyme-catalyzed reaction has an activation energy. The bacterial enzyme is affected by temperature too, as the graph shows."),
           ch("Higher temperatures lower the activation energy of reactions in bacteria but raise it in human cells, so the rates differ.", "Temperature does not do this. The difference arises from how the enzymes' structures respond to heat.")],
          "Each enzyme has an optimum temperature. Below it, higher temperature raises the rate; above it, denaturation lowers the rate.", diagram=temp_graph, difficulty="medium")

    ph_rows = [("Pepsin", 100, 25, 0), ("Trypsin", 0, 10, 100), ("Salivary amylase", 0, 60, 30)]
    B.mcq(2, "The table gives the relative activity of three digestive enzymes at three pH values. Pepsin is made in the stomach and passes into the small intestine, where the pH is about 8. Based on the data, what is most likely to happen to the activity of pepsin in the small intestine?",
          ch("Its activity will fall to almost zero, because the higher pH changes the structure of the enzyme.", "The data show pepsin has no measurable activity at pH 8. A pH far from the optimum changes the enzyme's structure and so the active site."),
          [ch("Its activity will increase, because the conditions in the small intestine are the optimum for trypsin.", "An enzyme's optimum pH is its own property. Conditions that suit trypsin do not suit pepsin."),
           ch("Its activity will stay the same, because enzymes in the digestive system function at any pH level.", "The data show that the activity of each enzyme depends strongly on pH."),
           ch("Its activity will fall to about 25 percent, as at pH 5, because the intestine is not much less acidic than the stomach.", "The 25 percent figure is pepsin's activity at pH 5. The small intestine is at about pH 8, where the table shows pepsin's activity is 0 percent.")],
          "Each enzyme has an optimum pH. Pepsin is active at low pH and is inactive at pH 8.",
          diagram=table(["Enzyme", "pH 2", "pH 5", "pH 8"], [(n_, a, b, c_) for n_, a, b, c_ in ph_rows], caption="Relative activity (%) at three pH values", row_headers=True), difficulty="medium")

    rev_rows = [("None (control, kept at 25 °C)", 100), ("50 °C for 5 min, then returned to 25 °C", 92), ("90 °C for 5 min, then returned to 25 °C", 4)]
    B.mcq(2, "Samples of the same enzyme were exposed to different temperatures for 5 minutes and then returned to 25 °C, where their activity was measured. Which statement best explains the difference between the two heated samples?",
          ch("Heating to 50 °C disrupted the enzyme's structure only temporarily and it refolded on cooling, but heating to 90 °C caused lasting changes.",
             "In some cases denaturation is reversible and the enzyme regains its shape and activity. Greater disruption can leave the enzyme permanently unable to fold correctly."),
          [ch("Enzymes are permanently denatured by any temperature above 25 °C, so the sample heated to 50 °C should also have lost its activity.", "The data show the sample heated to 50 °C kept most of its activity. Not all denaturation is permanent."),
           ch("Heating at 50 °C increased the amount of enzyme in the sample, which explains why its activity stayed high after the heating.", "Heating does not make more enzyme. The activity stayed high because the enzyme returned to its active structure."),
           ch("The sample heated to 90 °C lost activity because its substrate was used up during the heating, but the other sample's was not.", "Substrate was not part of the heating treatment. The loss of activity points to a change in the enzyme.")],
          "Denaturation can be reversible when the disruption is small, and irreversible when the structure is severely altered.",
          diagram=table(["Treatment of enzyme sample", "Activity at 25 °C (% of control)"], rev_rows, caption="Enzyme activity after heating"), difficulty="medium")

    B.mcq(2, "The rate of a reaction catalyzed by an enzyme increases as the temperature rises from 10 °C to 30 °C. Which statement best explains this increase?",
          ch("Higher temperature increases the average speed of molecules, so enzyme and substrate collide more often.", "More frequent collisions between enzymes and substrates mean more enzyme-substrate complexes form per second, until the temperature rises past the optimum."),
          [ch("Higher temperature lowers the activation energy of the reaction by more than the enzyme itself does in the cell.", "Temperature does not lower activation energy. It increases the rate by raising the frequency of collisions."),
           ch("Higher temperature makes the active site larger, so more substrate molecules can be bound at the same time.", "The active site's shape is not enlarged by heating. Heating beyond the optimum would disrupt it."),
           ch("Higher temperature makes the enzyme produce more substrate, so the reaction has more reactants available.", "Enzymes do not make substrate. The substrate concentration is unchanged by the temperature.")],
          "Below the optimum temperature, a rise in temperature raises the rate because molecules collide more often.", difficulty="medium")

    t_min = [0, 2, 4, 6, 8]
    prod = [0.0, 3.4, 6.0, 7.6, 8.0]
    r_late = (prod[4] - prod[2]) / (t_min[4] - t_min[2])
    r_early = (prod[2] - prod[0]) / (t_min[2] - t_min[0])
    r_whole = prod[4] / t_min[4]
    change = prod[4] - prod[2]
    assert (round(r_late, 2), round(r_early, 2), round(r_whole, 2), round(change, 2)) == (0.5, 1.5, 1.0, 2.0)
    prod_table = table(["Time (min)", "Product concentration (mM)"], [(t_, fix(p_)) for t_, p_ in zip(t_min, prod)], caption="Product formed in an enzyme-catalyzed reaction")
    B.mcq(2, "The table shows the concentration of product over time in an enzyme-catalyzed reaction. What is the average rate of product formation between 4 and 8 minutes?",
          ch("0.50 mM/min", "Rate is the change in product concentration divided by the change in time: (8.0 - 6.0) mM / (8 - 4) min = 0.50 mM/min.", r_late),
          [ch("1.5 mM/min", "This is the rate over the first 4 minutes (6.0 / 4). The question asks about 4 to 8 minutes, when the rate has slowed.", r_early),
           ch("1.0 mM/min", "This divides the final concentration by the total time (8.0 / 8), which gives the average over the whole experiment rather than between 4 and 8 minutes.", r_whole),
           ch("2.0 mM/min", "This is the change in concentration (8.0 - 6.0) without dividing by the elapsed time.", change)],
          "Average rate = change in product concentration / change in time over the interval asked about.", diagram=prod_table, difficulty="hard")

    B.mcq(2, "Using the data in the table, which statement best explains why the rate of product formation decreases as the reaction proceeds?",
          ch("As substrate is used up and product builds up, fewer enzyme-substrate complexes form and the reaction slows.", "The relative concentrations of substrate and product affect how efficiently an enzyme-catalyzed reaction proceeds. As substrate falls, collisions with enzyme that lead to product become less frequent."),
          [ch("The enzyme is consumed as it catalyzes the reaction, so less enzyme is available later in the reaction to bind substrate.", "Enzymes are not consumed by the reactions they catalyze."),
           ch("The activation energy of the reaction increases over time, so fewer collisions lead to product in the later minutes.", "Activation energy is a property of the reaction and the enzyme. It does not rise as the reaction proceeds."),
           ch("The temperature of the reaction mixture falls steadily, which lowers the rate of the enzyme in the later minutes.", "Nothing in the data suggests a falling temperature. The pattern is what is expected when substrate is used up.")],
          "A reaction slows as its substrate is depleted and its product builds up.", diagram=prod_table, difficulty="medium")

    B.mcq(2, "A molecule similar in structure to an enzyme's substrate is added to an enzyme-catalyzed reaction, and the rate of the reaction decreases. When the concentration of substrate is greatly increased, the rate returns to nearly its original value. Which statement best explains these observations?",
          ch("The molecule is a competitive inhibitor that binds the active site reversibly, so extra substrate competes with it for the active sites.", "A competitive inhibitor resembles the substrate and binds the active site reversibly. A high substrate concentration makes it much more likely that the substrate occupies the active sites."),
          [ch("The molecule is a noncompetitive inhibitor that binds to an allosteric site and permanently changes the enzyme's structure.", "A noncompetitive inhibitor binds somewhere other than the active site, and extra substrate cannot overcome its effect."),
           ch("The molecule denatures the enzyme, and the extra substrate causes the enzyme to refold into its active shape.", "Denaturation does not explain the restoration of the rate by substrate. Substrate does not refold enzymes."),
           ch("The molecule lowers the activation energy of the reaction, and the extra substrate raises it again to the original level.", "A competitive inhibitor does not alter the activation energy. It blocks access to the active site.")],
          "Competitive inhibitors bind the active site reversibly, so adding more substrate can overcome them.", difficulty="medium")

    inh_graph = graph("Substrate concentration (mM)", "Reaction rate (µmol/min)", 0, 40, 0, 100,
                      [line("No inhibitor", [(0, 0), (5, 60), (10, 85), (20, 95), (40, 100)], "blue"),
                       line("Inhibitor X", [(0, 0), (5, 25), (10, 50), (20, 80), (40, 97)], "green"),
                       line("Inhibitor Y", [(0, 0), (5, 30), (10, 42), (20, 48), (40, 50)], "red")],
                      "Reaction rate against substrate concentration. Without inhibitor the rate levels off near 100. With inhibitor X the rate is lower at low concentrations but reaches about 97 at 40 mM. With inhibitor Y the rate levels off near 50.")
    B.mcq(2, "The graph shows the rate of an enzyme-catalyzed reaction at different substrate concentrations with no inhibitor and with each of two inhibitors. Which statement is best supported by the graph?",
          ch("Inhibitor Y is more likely noncompetitive, because adding substrate does not restore the maximum rate seen with no inhibitor.", "A noncompetitive inhibitor binds at an allosteric site and changes the enzyme's activity, so extra substrate cannot overcome it. The rate with Y stays near 50."),
          [ch("Inhibitor X is more likely a noncompetitive inhibitor, because it lowers the rate at low substrate concentrations.", "Both types of inhibitor lower the rate at low substrate concentration. The rate with X approaches the maximum at high substrate, as expected for a competitive inhibitor."),
           ch("The two inhibitors act in the same way, because both lower the rate at every substrate concentration shown on the graph.", "They differ at high substrate concentration, where the rate with X nearly reaches the maximum but the rate with Y does not."),
           ch("Inhibitor Y is a competitive inhibitor, because it lowers the rate at the low substrate concentrations shown.", "Competitive inhibition can be overcome by high substrate concentration. The rate with Y does not recover.")],
          "Competitive inhibition can be overcome by more substrate; noncompetitive inhibition cannot.", diagram=inh_graph, difficulty="hard")

    sat_graph = graph("Substrate concentration (mM)", "Reaction rate (µmol/min)", 0, 40, 0, 100,
                      [line("No inhibitor", [(0, 0), (5, 60), (10, 85), (20, 95), (40, 100)], "blue")],
                      "Reaction rate rises steeply with substrate concentration and levels off near 100 micromoles per minute above about 20 millimolar.")
    B.mcq(2, "The graph shows that the rate of an enzyme-catalyzed reaction rises as the substrate concentration increases, and then levels off. Which statement best explains why the rate levels off at high substrate concentrations?",
          ch("Nearly all the active sites are occupied at high substrate concentration, so more substrate cannot increase the rate.", "When the enzyme is saturated, each active site is already working as fast as it can, so extra substrate cannot be bound."),
          [ch("The high concentration of substrate denatures the enzyme, so no further product can form at any concentration.", "The graph shows the rate leveling off, not falling. Denaturation would lower the rate."),
           ch("The activation energy of the reaction rises as more substrate is added, which cancels the extra substrate.", "Substrate concentration does not change the activation energy."),
           ch("The enzyme molecules are converted into product once the substrate concentration becomes high, so less enzyme remains.", "Enzymes are catalysts and are not converted into the products.")],
          "Enzyme-catalyzed reaction rates level off when the enzyme is saturated with substrate.", diagram=sat_graph, difficulty="medium")

    B.mcq(2, "A student heats an enzyme to 60 °C and finds that its activity at that temperature is zero. The student claims that the enzyme has been denatured and cannot regain activity. Which additional investigation would best test whether the loss of activity is irreversible?",
          ch("Cooling a sample of the heated enzyme to its optimum temperature and measuring whether its activity returns.", "If the loss of activity were due to reversible changes in structure, activity would be restored on cooling. If no activity returns, the denaturation was irreversible."),
          [ch("Adding much more substrate at 60 °C and measuring whether the rate of the reaction increases.", "Extra substrate overcomes competitive inhibition or low substrate concentration, but it cannot show whether the enzyme's structure can recover."),
           ch("Measuring the activity of the enzyme at 80 °C to see whether the activity falls even further.", "This would show how activity changes at a higher temperature, not whether the loss at 60 °C can be reversed."),
           ch("Repeating the measurement at 60 °C with the same enzyme sample to see whether the result is the same.", "Repeating the measurement at 60 °C only checks that the result can be reproduced. It does not test whether the change is reversible.")],
          "To test reversibility, return the enzyme to favorable conditions and see whether activity is restored.", difficulty="hard")

    B.mcq(2, "In a metabolic pathway, enzyme 1 converts substance A to B, enzyme 2 converts B to C, and enzyme 3 converts C to D. A drug that competitively inhibits enzyme 2 is added to cells that are making D. Which prediction about the concentrations of B, C and D is most consistent with the effect of the drug?",
          ch("The concentration of B will increase, and the concentrations of C and D will decrease.", "With enzyme 2 inhibited, B is converted to C more slowly, so B builds up. Less C is made, and so less D is made."),
          [ch("The concentration of B will decrease, and the concentrations of C and D will increase.", "Inhibiting enzyme 2 slows the conversion of B to C, so B would accumulate rather than fall."),
           ch("The concentrations of B, C and D will all increase, because the drug causes the pathway to run backward.", "A competitive inhibitor slows a reaction. It does not reverse the direction of a pathway."),
           ch("The concentration of B will not change, but the concentration of D will increase.", "B is the substrate of the inhibited enzyme. D is made from C, which is now being produced more slowly.")],
          "Inhibiting one enzyme of a pathway causes its substrate to accumulate and its products to decrease.", difficulty="hard")

    # The last 3.2 item: error bars (this replaces a bare "read the optimum" item, so the unit has one statistics question).
    temps = ["20 °C", "30 °C", "37 °C", "50 °C"]
    means = [3.1, 6.2, 9.8, 8.4]
    err = [0.8, 1.0, 1.2, 1.8]  # +/- 2 SE, about a 95 percent confidence interval
    lo = [m - e for m, e in zip(means, err)]
    hi = [m + e for m, e in zip(means, err)]
    assert lo[2] <= hi[3] and hi[1] < lo[2]  # 37 and 50 overlap; 30 and 37 do not
    assert hi[0] < lo[1]
    B.mcq(2, "The graph shows the mean rate of an enzyme-catalyzed reaction at four temperatures. Each bar is the mean of five trials, and the error bars show plus or minus 2 standard errors of the mean, which is approximately a 95 percent confidence interval. Which conclusion is best supported by the data?",
          ch("The rate at 37 °C is higher than at 30 °C, but the data do not support a difference between 37 °C and 50 °C.", "The error bars for 30 °C and 37 °C do not overlap, so that difference is unlikely to be due to chance. The error bars for 37 °C and 50 °C overlap, so the data do not support a real difference."),
          [ch("The rate at 50 °C is lower than the rate at 37 °C, because the mean value at 50 °C is the smaller one.", "A smaller mean is not enough. The error bars overlap, so the difference may be due to chance variation."),
           ch("The rates at 20 °C and 30 °C are not different, because both are lower than the rates at 37 °C and at 50 °C.", "The error bars for 20 °C and 30 °C do not overlap, so these two rates probably differ."),
           ch("The enzyme is denatured at 50 °C, because its mean rate is lower than the mean rate at 37 °C.", "The data do not show that the rate at 50 °C is lower than the rate at 37 °C, so they do not support denaturation at 50 °C.")],
          "When 95 percent confidence intervals overlap, the data do not support a real difference between the means.",
          diagram=bars("Temperature", "Mean reaction rate (µmol/min)", 16, temps, [{"values": means, "errors": err, "color": "blue"}]), difficulty="hard")
