"""Unit 3: six free-response prompts, one of each kind (CED Exam Overview structure), over five of the unit's five topics.

  RESULTS        (9)  3.2  catalase and temperature (table)
  RESULTS_GRAPH  (9)  3.5  yeast fermentation of different sugars (table -> bar graph with error bars)
  INVESTIGATION  (4)  3.1  lactase: variables, a control, a prediction (no data)
  CONCEPT        (4)  3.3  order, the second law, sequential pathways, a disrupted pathway
  MODEL          (4)  3.4  the thylakoid membrane model of the light reactions (a table is the "figure")
  DATA           (4)  3.2  inhibitors on a rate-versus-substrate graph

Part structure follows the CED: Q1 parts A 1, B 3, C 3, D 2; Q2 parts A 1, B 4 (construct the graph), C 2, D 2; Q3-Q6 four one-point parts.
The student answers in writing, so "construct a graph" asks for a description of the graph (type, axis labels, scale, plotted values, error bars).
Every one-point rubric line is a separate line so the self-grading checklist can award each point.
"""
from lib import *


def build(B):
    # ------------------------------------------------------------------ RESULTS (9): catalase and temperature
    temps = ["10 °C", "25 °C", "37 °C", "60 °C"]
    times = [30, 60, 90, 120]
    o2 = {"10 °C": [0.8, 1.6, 2.3, 3.0], "25 °C": [2.0, 3.9, 5.8, 7.6], "37 °C": [3.4, 6.7, 9.9, 12.6], "60 °C": [0.4, 0.5, 0.5, 0.5]}
    rate37 = (o2["37 °C"][2] - o2["37 °C"][0]) / (times[2] - times[0])
    pct = pct_change(o2["25 °C"][3], o2["37 °C"][3])
    assert round(rate37, 2) == 0.11 and round(pct) == 66, (rate37, pct)
    rows = [(str(t_),) + tuple(fix(o2[k][i]) for k in temps) for i, t_ in enumerate(times)]
    B.frq(2, "RESULTS",
          "Catalase is an enzyme in liver cells that breaks down hydrogen peroxide (H₂O₂), a toxic byproduct of metabolism, into water and oxygen gas (O₂). A student investigated the effect of temperature on the activity of catalase in liver extract. For each trial, 5 mL of liver extract and 5 mL of 3 percent hydrogen peroxide solution were separately brought to the test temperature and then combined in a sealed apparatus. The student measured the total volume of O₂ collected every 30 seconds. The results are shown in the table.\n\n"
          "**(a)** **Describe** how the enzyme catalase affects the activation energy of the breakdown of hydrogen peroxide. (1 point)\n\n"
          "**(b)** (i) **Identify** the dependent variable in the investigation. (ii) **Identify** one variable that the student controlled (kept the same) in every trial. (iii) **Describe** the relationship between temperature and the volume of O₂ collected at 120 seconds for the trials at 10 °C, 25 °C and 37 °C. (3 points)\n\n"
          "**(c)** (i) **Calculate** the rate of O₂ production, in mL per second, in the trial at 37 °C between 30 seconds and 90 seconds. Give your answer to the nearest 0.01 mL per second. (ii) **Calculate** the percent change in the volume of O₂ collected at 120 seconds between the trial at 25 °C and the trial at 37 °C. Give your answer to the nearest whole percent. (iii) **Identify** the trial in which the data suggest that catalase was denatured, and **support** your answer with data from the table. (3 points)\n\n"
          "**(d)** A competitive inhibitor of catalase is added to the trial at 37 °C. **Predict** how the volume of O₂ collected at 120 seconds will compare with the volume collected without the inhibitor, and **justify** your prediction. (2 points)",
          [(1, "(a) States that catalase lowers the activation energy of the reaction (so the reaction proceeds faster)."),
           (1, "(b)(i) Identifies the dependent variable as the volume of O₂ collected (in mL)."),
           (1, "(b)(ii) Identifies a controlled variable, such as the volume or concentration of hydrogen peroxide, the volume of liver extract, the pH, the time interval, or the type of apparatus."),
           (1, "(b)(iii) Describes that as the temperature increases from 10 °C to 37 °C, the volume of O₂ collected at 120 seconds increases (from 3.0 mL to 12.6 mL)."),
           (1, "(c)(i) Calculates the rate as (9.9 - 3.4) mL / 60 s = 0.11 mL/s (accept 0.108), with units."),
           (1, "(c)(ii) Calculates the percent change as (12.6 - 7.6) / 7.6 x 100 = 66 percent increase (accept 65.8)."),
           (1, "(c)(iii) Identifies the trial at 60 °C and supports it with data: very little O₂ (0.5 mL) was collected and the volume stopped increasing after 60 seconds."),
           (1, "(d) Predicts that the volume of O₂ collected will be less than (lower than) it was without the inhibitor."),
           (1, "(d) Justifies the prediction: the competitive inhibitor binds the active site of catalase, so fewer hydrogen peroxide molecules can bind and fewer enzyme-substrate complexes form.")],
          "(a) Catalase lowers the activation energy of the breakdown of hydrogen peroxide, which makes the reaction go faster.\n\n"
          "(b) (i) The dependent variable is the volume of O₂ collected. (ii) The volume and concentration of the hydrogen peroxide (5 mL of 3 percent) were the same in every trial. (iii) As the temperature rose from 10 °C to 37 °C, the volume of O₂ collected at 120 seconds increased from 3.0 mL to 7.6 mL to 12.6 mL.\n\n"
          "(c) (i) Rate = (9.9 mL - 3.4 mL) / (90 s - 30 s) = 6.5 mL / 60 s = 0.11 mL/s. (ii) Percent change = (12.6 - 7.6) / 7.6 x 100 = 66 percent increase. (iii) The 60 °C trial: only 0.5 mL of O₂ was collected, and the volume did not increase after 60 seconds, so the enzyme was probably denatured.\n\n"
          "(d) The volume of O₂ collected will be lower. A competitive inhibitor binds to the active site of catalase, so fewer hydrogen peroxide molecules can bind and fewer enzyme-substrate complexes form during the 120 seconds.",
          diagram=table(["Time (s)"] + temps, rows, caption="Total volume of O₂ collected (mL)", row_headers=True))

    # ------------------------------------------------------------------ RESULTS_GRAPH (9): yeast and sugars
    sugars = ["Glucose", "Fructose", "Sucrose", "Lactose", "None (water only)"]
    raw = {
        "Glucose": [11.8, 12.6, 13.1, 12.0, 12.9, 12.0],
        "Fructose": [10.9, 11.8, 12.2, 11.1, 12.0, 11.6],
        "Sucrose": [9.2, 10.1, 10.4, 9.5, 10.0, 9.6],
        "Lactose": [1.0, 1.4, 0.9, 1.2, 1.1, 1.0],
        "None (water only)": [0.8, 1.0, 0.9, 1.1, 0.9, 0.7],
    }
    means = [mean(raw[s_]) for s_ in sugars]
    ses = [se(raw[s_]) for s_ in sugars]
    assert [round(m_, 1) for m_ in means] == [12.4, 11.6, 9.8, 1.1, 0.9], means
    assert all(0.05 < e_ < 0.25 for e_ in ses) and [round(e_, 1) for e_ in ses] == [0.2, 0.2, 0.2, 0.1, 0.1], ses  # the sample response quotes these
    rate_glu = means[0] / 30
    assert round(rate_glu, 2) == 0.41
    rows = [(s_, fix(m_), fix(e_, 2)) for s_, m_, e_ in zip(sugars, means, ses)]
    B.frq(5, "RESULTS_GRAPH",
          "Yeast cells can carry out fermentation when oxygen is not available. A student investigated whether the type of sugar affects the amount of carbon dioxide (CO₂) produced by yeast. In each of six trials for each treatment, the student mixed yeast with a solution of one sugar, or with water only, in a sealed container with no oxygen, and measured the volume of CO₂ produced in 30 minutes. The means and standard errors of the six trials are shown in the table.\n\n"
          "**(a)** **Describe** the role of fermentation in the production of ATP by yeast cells that have no oxygen. (1 point)\n\n"
          "**(b)** **Construct** a graph of the data in the table. Because you are answering in writing, describe the graph you would draw: the type of graph, what is shown on each axis, with units, the scale of each axis, the values you would plot, and how you would show the standard errors. (4 points)\n\n"
          "**(c)** (i) **Calculate** the mean rate of CO₂ production, in mL per minute, for the yeast given glucose. Give your answer to the nearest 0.01 mL per minute. (ii) **State** a null hypothesis for this investigation. (2 points)\n\n"
          "**(d)** Lactase is an enzyme that breaks lactose into glucose and galactose. **Predict** how the volume of CO₂ produced would change if lactase were added to the yeast given lactose, and **justify** your prediction. (2 points)",
          [(1, "(a) Describes that fermentation allows glycolysis to continue (by regenerating NAD⁺) in the absence of oxygen, so the yeast can keep making ATP, with CO₂ (and ethanol) as products."),
           (1, "(b) Chooses an appropriate graph type: a bar graph, because the independent variable (type of sugar) is categorical."),
           (1, "(b) Labels both axes with units: the type of sugar provided on the horizontal axis, and the mean volume of CO₂ produced in 30 minutes (mL) on the vertical axis."),
           (1, "(b) Gives an appropriate scale: a vertical axis that starts at 0 and has equal intervals, extending to at least about 13 mL so all the means fit."),
           (1, "(b) Plots the data accurately (bar heights close to 12.4, 11.6, 9.8, 1.1 and 0.9 mL) and shows error bars of plus and minus one standard error for each bar."),
           (1, "(c)(i) Calculates the rate as 12.4 mL / 30 min = 0.41 mL/min."),
           (1, "(c)(ii) States a null hypothesis: the type of sugar has no effect on the volume of CO₂ produced by the yeast (any differences are due to chance)."),
           (1, "(d) Predicts that the volume of CO₂ produced with lactose would increase when lactase is added."),
           (1, "(d) Justifies the prediction: lactase breaks lactose into glucose (and galactose), which the yeast can ferment, so glycolysis and fermentation produce CO₂.")],
          "(a) With no oxygen, fermentation lets glycolysis keep going, because it regenerates NAD⁺. Glycolysis makes a small amount of ATP, and the fermentation products include CO₂ and ethanol.\n\n"
          "(b) A bar graph, because the sugars are categories. The horizontal axis is labeled \"Sugar provided\" with one bar for each of the five treatments. The vertical axis is labeled \"Mean volume of CO₂ produced in 30 minutes (mL)\", scaled from 0 to 14 in steps of 2. The bars are about 12.4 (glucose), 11.6 (fructose), 9.8 (sucrose), 1.1 (lactose) and 0.9 (water only), each with an error bar of plus and minus one standard error (about 0.2 mL for the first three and about 0.1 mL or less for the last two, from the table).\n\n"
          "(c) (i) Rate = 12.4 mL / 30 min = 0.41 mL/min. (ii) The type of sugar has no effect on the volume of CO₂ produced by yeast.\n\n"
          "(d) The volume of CO₂ would increase. Lactase breaks lactose into glucose and galactose, and yeast can ferment glucose, so more glycolysis and fermentation would occur and produce CO₂.",
          diagram=table(["Sugar provided", "Mean volume of CO₂ produced in 30 min (mL), n = 6", "Standard error (mL)"], rows, caption="Fermentation by yeast with different sugars", row_headers=True))

    # ------------------------------------------------------------------ INVESTIGATION (4): lactase
    B.frq(1, "INVESTIGATION",
          "A student wants to investigate how the amount of the enzyme lactase affects the breakdown of lactose in milk. Lactase breaks lactose into glucose and galactose. The student has milk, a lactase solution, distilled water, and test strips that measure the concentration of glucose. The student plans to add 0, 1, 2 or 4 drops of lactase solution to equal volumes of milk, keep the mixtures at 25 °C, and measure the glucose concentration after 10 minutes.\n\n"
          "**(a)** **Describe** how lactase affects the breakdown of lactose. (1 point)\n\n"
          "**(b)** **Identify** an appropriate negative control for the investigation. (1 point)\n\n"
          "**(c)** **Predict** how the glucose concentration after 10 minutes will change as the number of drops of lactase solution increases. (1 point)\n\n"
          "**(d)** **Justify** your prediction. (1 point)",
          [(1, "(a) Describes that lactase binds lactose at its active site and lowers the activation energy, which speeds up the breakdown of lactose."),
           (1, "(b) Identifies a negative control: milk with no lactase (with distilled water added instead), or milk with boiled (denatured) lactase."),
           (1, "(c) Predicts that the glucose concentration will increase as more lactase is added (assuming there is still lactose left)."),
           (1, "(d) Justifies: more lactase means more active sites available, so more enzyme-substrate complexes form in 10 minutes and more lactose is broken down to glucose.")],
          "(a) Lactase binds lactose at its active site and lowers the activation energy for its breakdown into glucose and galactose, so the reaction goes faster.\n\n"
          "(b) A tube with the same volume of milk and distilled water in place of the lactase solution.\n\n"
          "(c) The glucose concentration will be higher with more drops of lactase.\n\n"
          "(d) With more lactase there are more active sites, so more enzyme-substrate complexes form each minute. More lactose is broken down into glucose in the 10 minutes.")

    # ------------------------------------------------------------------ CONCEPT (4): order and pathways
    B.frq(3, "CONCEPT",
          "Cells are highly ordered, and they obtain energy from molecules such as glucose through metabolic pathways made up of many enzyme-catalyzed steps. In one such pathway, the product of each step is the reactant of the next step. A mutation causes the enzyme that catalyzes the third step of a five-step pathway to be nonfunctional.\n\n"
          "**(a)** **Describe** how a living cell can maintain its high degree of order without violating the second law of thermodynamics. (1 point)\n\n"
          "**(b)** **Explain** how carrying out a process in a series of steps, with the product of one step being the reactant of the next, allows the cell to transfer energy in a controlled way. (1 point)\n\n"
          "**(c)** **Predict** how the concentration of the substrate of the third-step enzyme, and the concentration of the final product of the pathway, will change in cells with the mutation. (1 point)\n\n"
          "**(d)** **Justify** your prediction. (1 point)",
          [(1, "(a) Describes that the cell takes in energy (an input of energy greater than the energy it loses) and releases heat, so order in the cell is maintained while disorder in the surroundings increases."),
           (1, "(b) Explains that a sequence of small steps transfers energy gradually, so the energy released at each step can be captured in molecules such as ATP rather than being lost all at once."),
           (1, "(c) Predicts that the substrate of the third-step enzyme will accumulate (increase) and the final product will decrease."),
           (1, "(d) Justifies: the nonfunctional enzyme cannot convert its substrate to product, so the substrate builds up, and the later steps do not receive their reactants, so less of the final product is made.")],
          "(a) A cell takes in more energy than it loses. It uses the energy to maintain order, and it releases heat to its surroundings, which increases the disorder of the surroundings. The total disorder still increases, so the second law is not violated.\n\n"
          "(b) In a series of steps, a little energy is released at each step and can be transferred to molecules such as ATP, so the transfer is more controlled than if all the energy were released in one reaction.\n\n"
          "(c) The substrate of the third-step enzyme will increase, and the final product will decrease.\n\n"
          "(d) The mutant enzyme cannot convert its substrate to the next product, so the substrate builds up. Steps four and five do not receive the reactants they need, so less of the final product is made.")

    # ------------------------------------------------------------------ MODEL (4): the thylakoid membrane
    model_rows = [("1", "Space inside the thylakoid (lumen)"), ("2", "Photosystem II (PSII), in the thylakoid membrane"), ("3", "Electron transport chain (ETC), in the thylakoid membrane"),
                  ("4", "Photosystem I (PSI), in the thylakoid membrane"), ("5", "ATP synthase, in the thylakoid membrane"), ("6", "Space outside the thylakoid (stroma)")]
    B.frq(4, "MODEL",
          "The model represents the thylakoid membrane in a chloroplast and the light reactions of photosynthesis. The table is the key to the model. In the model, light energy excites electrons in PSII, and water is split on the lumen side of PSII, which replaces the electrons that PSII loses. The electrons pass from PSII through the ETC to PSI, where light excites them again before they are transferred to NADP⁺ on the stroma side of the membrane. As electrons move through the ETC, hydrogen ions (H⁺) are moved from the stroma into the lumen. H⁺ then move back to the stroma through ATP synthase.\n\n"
          "**(a)** **Describe** the difference in H⁺ concentration between the lumen and the stroma that results from the processes shown in the model. (1 point)\n\n"
          "**(b)** **Explain** how the movement of electrons through the ETC results in the difference in H⁺ concentration that you described in part (a). (1 point)\n\n"
          "**(c)** The model uses an arrow to show the movement of H⁺ through ATP synthase. **Identify** the numbered locations that the arrow connects, in order from start to end, and **identify** the molecule that is made as a result of this movement. (1 point)\n\n"
          "**(d)** **Explain** how the products of the light reactions shown in the model are used in the stroma to store energy in carbohydrates. (1 point)",
          [(1, "(a) Describes that the H⁺ concentration is higher in the lumen (location 1) than in the stroma (location 6)."),
           (1, "(b) Explains that as electrons are transferred through the ETC in a series of oxidation-reduction reactions, the energy released is used to move H⁺ from the stroma into the lumen."),
           (1, "(c) Identifies the arrow as running from location 1 (the lumen) to location 6 (the stroma), and identifies ATP as the molecule that is made."),
           (1, "(d) Explains that the ATP and NADPH made in the light reactions provide the energy (and electrons) for the Calvin cycle in the stroma, which uses carbon dioxide to make carbohydrates.")],
          "(a) The concentration of H⁺ is higher in the lumen (1) than in the stroma (6).\n\n"
          "(b) Electrons pass from carrier to carrier through the ETC in oxidation-reduction reactions. The energy released as they move is used to pump H⁺ from the stroma into the lumen, which forms the gradient.\n\n"
          "(c) The arrow runs from location 1 (the lumen) to location 6 (the stroma), and the molecule made is ATP, from ADP and inorganic phosphate.\n\n"
          "(d) The ATP and NADPH made in the light reactions supply the energy and electrons for the Calvin cycle in the stroma, which uses them to build carbohydrates from carbon dioxide.",
          diagram=table(["Label", "Part of the model"], model_rows, caption="Key to the model of the thylakoid membrane", row_headers=True))

    # ------------------------------------------------------------------ DATA (4): inhibitors
    g = graph("Substrate concentration (mM)", "Reaction rate (µmol/min)", 0, 40, 0, 100,
              [line("No inhibitor", [(0, 0), (5, 50), (10, 75), (20, 92), (40, 100)], "blue"),
               line("Inhibitor 1", [(0, 0), (5, 20), (10, 40), (20, 70), (40, 95)], "green"),
               line("Inhibitor 2", [(0, 0), (5, 25), (10, 38), (20, 45), (40, 48)], "red")],
              "Reaction rate against substrate concentration for an enzyme with no inhibitor, with inhibitor 1 and with inhibitor 2. With no inhibitor the rate reaches 100 at 40 mM. With inhibitor 1 the rate is 20 at 5 mM and reaches 95 at 40 mM. With inhibitor 2 the rate levels off near 48.")
    B.frq(2, "DATA",
          "A researcher measured the rate of a reaction catalyzed by an enzyme at different substrate concentrations with no inhibitor, with inhibitor 1 and with inhibitor 2. The results are shown in the graph.\n\n"
          "**(a)** **Describe** the effect of inhibitor 1 on the reaction rate at a substrate concentration of 5 mM. (1 point)\n\n"
          "**(b)** **Describe** how the reaction rate with inhibitor 1 changes as the substrate concentration increases from 5 mM to 40 mM. (1 point)\n\n"
          "**(c)** A student hypothesizes that inhibitor 2 is a competitive inhibitor. **Evaluate** the hypothesis using the data in the graph. (1 point)\n\n"
          "**(d)** **Explain** how a noncompetitive inhibitor decreases the rate of an enzyme-catalyzed reaction. (1 point)",
          [(1, "(a) Describes that inhibitor 1 decreases the reaction rate at 5 mM from about 50 to about 20 µmol/min."),
           (1, "(b) Describes that with inhibitor 1 the rate increases as substrate increases and approaches the rate with no inhibitor (about 95 compared with 100 µmol/min at 40 mM)."),
           (1, "(c) Evaluates the hypothesis as not supported, using data: with inhibitor 2 the rate stays near 48 µmol/min at 40 mM, far below the 100 µmol/min with no inhibitor, so adding more substrate did not overcome the inhibitor."),
           (1, "(d) Explains that a noncompetitive inhibitor binds to an allosteric site (not the active site), which changes the shape (and so the activity) of the enzyme, so fewer substrate molecules are converted to product.")],
          "(a) At 5 mM, inhibitor 1 lowers the rate from about 50 to about 20 µmol/min.\n\n"
          "(b) With inhibitor 1 the rate increases as the substrate concentration increases, and at 40 mM it is about 95 µmol/min, close to the 100 µmol/min with no inhibitor.\n\n"
          "(c) The data do not support the hypothesis. A competitive inhibitor can be overcome by a high substrate concentration, but with inhibitor 2 the rate is only about 48 µmol/min at 40 mM, compared with 100 µmol/min with no inhibitor.\n\n"
          "(d) A noncompetitive inhibitor binds to an allosteric site that is not the active site. This changes the shape of the enzyme, so it is less able to convert substrate to product, and adding more substrate does not remove the effect.",
          diagram=g)
