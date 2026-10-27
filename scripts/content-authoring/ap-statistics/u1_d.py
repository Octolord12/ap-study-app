"""Unit 1, topics 1.10 and 1.11.

Required content (CED effective Fall 2026): 1.10 an investigative question has components: the variable(s) of interest; for a test, the parameter and the direction of the alternative (not equal, greater than, less than,
association); for an interval, the parameter and the goal of estimation; the population the conclusions apply to and, for an experiment with random assignment, a cause-and-effect conclusion. Census; experiment (treatments
assigned to experimental units; explanatory variable or factor, treatments, response variable); observational study (prospective, retrospective, survey), confounding variable (associated with both variables);
generalize to the population when the sample is random, otherwise only to similar individuals. 1.11 sampling with and without replacement; simple random sample (every sample of size n equally likely); stratified (SRS within
non-overlapping strata of similar individuals); cluster (SRS of clusters, then every unit in each selected cluster); systematic (random start, fixed interval). Skills 1.A, 2.A, 2.B.
"""
from lib import *


def build(B):
    # ------------------------------------------------------------------------------------------------------------ 1.10
    T = 10
    B.mcq(T, "A researcher wants to know whether the mean time that students at a large high school spend on homework each night is less than 90 minutes. Which of the following is an investigative question that makes clear both the parameter and the direction of the alternative hypothesis?",
          ch("Is the mean time that students at the high school spend on homework each night less than 90 minutes?", "It names the parameter (the mean homework time for the students at the school) and the direction (less than 90 minutes)."),
          [ch("Do the students at the high school spend a lot of time on homework each night during the whole school year?", "It does not name a parameter or a direction that can be tested."),
           ch("Is the mean time that students at the high school spend on homework each night different from the median time?", "This compares two summaries of the same data. It does not name the parameter and the direction of the question."),
           ch("What is the time that the first student who is surveyed at the high school spends on homework each night?", "This asks about one student and not about the parameter for the students at the school.")],
          "For a hypothesis test, the question should make clear the parameter and the direction of the alternative.", difficulty="medium")

    B.mcq(T, "A city official wants to estimate the proportion of all households in the city that recycle. Which of the following investigative questions guides the choice of a confidence interval?",
          ch("What is the proportion of all households in the city that recycle, estimated within a range of plausible values?", "For a confidence interval, the question should make clear the parameter and the goal of estimating it within a range of values."),
          [ch("Is the proportion of all households in the city that recycle greater than the proportion that own a car?", "This compares two proportions and asks for a direction, which guides a test."),
           ch("Do the households in the city that recycle also have a higher mean income than the households that do not?", "This is a question about a difference between means, which does not name a proportion to estimate."),
           ch("Why do some of the households in the city choose to recycle while some of the other households do not?", "This asks for reasons. It does not name a parameter to estimate.")],
          "A confidence interval question names the parameter and the goal of estimating it within a range of values.", difficulty="medium")

    B.mcq(T, "A researcher randomly assigns 80 volunteers to one of two exercise programs and compares the changes in their resting heart rates after 8 weeks. Which of the following is the type of conclusion that can be applied from this study?",
          ch("A cause-and-effect conclusion about the effect of the exercise programs on the resting heart rate, for people who are similar to the volunteers", "Random assignment of treatments allows a cause-and-effect conclusion. The volunteers are not a random sample, so the conclusion applies to similar people."),
          [ch("A cause-and-effect conclusion about all people in the world, because the 80 volunteers were assigned to the two exercise programs at random in the study of heart rate", "The volunteers were not randomly selected, so the conclusion cannot be applied to everyone."),
           ch("Only an association between the programs and the heart rate, because the heart rate was measured after the eight weeks", "Random assignment allows a cause-and-effect conclusion."),
           ch("No conclusion of any kind, because a study that uses volunteers cannot give any information about a population", "The results apply to individuals that are similar to the volunteers.")],
          "Random assignment supports a cause-and-effect conclusion; volunteers limit generalization to similar individuals.", difficulty="hard")

    B.mcq(T, "The principal of a school with 800 students asks every one of the students to complete a survey about their lunch preferences. What is this type of study?",
          ch("A census, because information is recorded from every individual in the population", "A census consists of recording information from all of the items or individuals in a population."),
          [ch("An experiment, because the students are asked the same questions and so they are all treated in the same way", "An experiment assigns treatments. Asking questions is a survey, which is an observational study."),
           ch("A simple random sample, because every one of the students has the same chance of being included in the survey", "A sample includes only part of the population. Here every student is included."),
           ch("A cluster sample, because the students of the school are in groups of classes that are surveyed during the day", "All students are surveyed, not a sample of groups.")],
          "Recording information from every member of the population is a census.", difficulty="easy")

    B.mcq(T, "A researcher flips a coin for each of 60 patients to decide whether the patient takes a new medicine or a placebo, and then compares the changes in blood pressure of the two groups. Which of the following describes this study?",
          ch("It is an experiment, because the researcher assigned the treatments to the patients", "In an experiment a researcher assigns conditions, or treatments, to experimental units."),
          [ch("It is an observational study, because the blood pressure was recorded for each patient after the medicine was taken", "Recording a response is part of both types of study. Here the researcher imposed the treatments."),
           ch("It is a census, because the researcher recorded the blood pressure of every one of the 60 patients in the study", "A census is about the whole population. The 60 patients are not a whole population of interest."),
           ch("It is a survey, because the researcher asked each patient a standard set of questions about the medicine", "A survey collects data with a standard set of questions. Here the treatments were assigned.")],
          "The researcher imposed the treatments, so this is an experiment.", difficulty="easy")

    B.mcq(T, "A researcher looks at the records of 500 patients, some of whom chose to take a vitamin supplement, and compares the rates of colds of the patients who took the supplement with the rates of the patients who did not. Which of the following describes this study?",
          ch("It is an observational study, because the researcher did not impose the treatments but recorded what the patients chose", "In an observational study treatments are not imposed. The researcher records the values of the variables."),
          [ch("It is an experiment, because the patients in the records are divided into two groups that are compared by the researcher", "Dividing the data into groups is not the same as assigning treatments."),
           ch("It is an experiment, because the researcher recorded a response variable on each one of the 500 patients", "Experiments assign the treatments. Here the patients chose."),
           ch("It is a census, because the researcher used the records of 500 patients that were recorded in the past", "A census records every member of a population, not just 500 patients.")],
          "Treatments were chosen by the patients, not imposed by the researcher: an observational study.", difficulty="easy")

    B.mcq(T, "A farmer assigns 12 plots of land to receive one of three fertilizers, with 4 plots for each fertilizer, and then measures the yield of each plot. Which of the following correctly identifies the experimental units, the treatments, and the response variable?",
          ch("The experimental units are the 12 plots, the treatments are the three fertilizers, and the response variable is the yield", "The experimental unit is the unit to which a treatment is assigned. The treatments are the levels of the explanatory variable (fertilizer)."),
          [ch("The experimental units are the three fertilizers, the treatments are the 12 plots, and the response variable is the yield", "The units and the treatments are reversed."),
           ch("The experimental units are the 12 plots, the treatments are the yields, and the response variable is the fertilizer", "The yield is the outcome that is measured, so it is the response variable."),
           ch("The experimental unit is the farmer, the treatments are the 12 plots, and the response variable is the fertilizer", "The farmer does not receive a treatment. The plots do.")],
          "Plots are the experimental units, fertilizers are the treatments, and yield is the response.", difficulty="medium")

    B.mcq(T, "A study selects 500 adults today, and then collects data on their diets now and on their health every year for the next 10 years. Which of the following describes this study?",
          ch("It is a prospective study, because the individuals are selected at one point in time and data are gathered both then and in the future", "A prospective study gathers data at the time of selection and into the future."),
          [ch("It is a retrospective study, because the individuals are selected now and the data are about their health during the next years", "A retrospective study gathers data from the past."),
           ch("It is an experiment, because the adults were followed for many years while the same researcher recorded their data", "No treatments are assigned, so it is an observational study."),
           ch("It is a census, because all of the adults who were selected were followed for the entire 10 years of the study", "A census includes the whole population. This study follows 500 adults.")],
          "Selecting individuals now and gathering data now and in the future is a prospective study.", difficulty="medium")

    B.mcq(T, "An observational study finds that adults who drink coffee every day have a lower rate of a certain disease than adults who do not drink coffee. A researcher suggests that exercise could be a confounding variable. Which of the following is required for exercise to be a confounding variable?",
          ch("Exercise must be associated with both coffee drinking and the rate of the disease", "To be a confounding variable, a variable must be associated with both the explanatory variable and the response variable."),
          [ch("Exercise must be associated with the rate of the disease, but it does not need to be associated with coffee drinking", "A confounding variable must be associated with both variables."),
           ch("Exercise must be a variable that the researcher assigned to the adults who took part in the study of the disease", "In an observational study the researcher does not assign values of variables."),
           ch("Exercise must have a larger effect on the disease than coffee drinking has on the rate of the disease", "A confounding variable provides an alternative explanation if it is related to both variables. Its size is not the requirement.")],
          "A confounding variable is associated with both the explanatory variable and the response variable.", difficulty="hard")

    B.mcq(T, "A researcher selects a simple random sample of 200 students from a school of 1,500 students and surveys them. For which population is it appropriate to generalize the results of the survey?",
          ch("All 1,500 students at the school, because the sample was selected from the population using a random mechanism", "When units are randomly selected from a population, it is appropriate to generalize to the whole population."),
          [ch("Only the 200 students who were surveyed, because a sample cannot be used to describe any students who were not surveyed", "A random sample allows generalizations to the whole population it came from."),
           ch("All of the students at all of the schools in the same state, because a random sample is representative of any school", "The sample was selected only from this school, so the conclusions apply to this school."),
           ch("Only the students at the school who are similar to the ones who volunteered, because the survey was a voluntary survey", "The sample was random, not a group of volunteers.")],
          "A random sample supports generalizing to the entire population it was selected from.", difficulty="medium")

    # ------------------------------------------------------------------------------------------------------------ 1.11
    T = 11
    B.mcq(T, "To choose 30 students from a list of 600 students, a teacher writes each student's name on a slip of paper, mixes the slips in a large box, and draws out 30 slips. What is the sampling method?",
          ch("A simple random sample, because every possible group of 30 students has the same chance of being the sample", "In a simple random sample of size n, every sample of size n has the same chance of being selected."),
          [ch("A stratified random sample, because the 600 students were put in a single list before the slips were drawn from the box", "Strata are non-overlapping groups, with a simple random sample from each of the groups."),
           ch("A cluster random sample, because the slips of paper were mixed in one box and a group of them was drawn out", "A cluster sample selects whole groups of students and includes every one of the students in the groups."),
           ch("A systematic random sample, because the slips were taken out of the box one after another in a regular order", "A systematic sample uses a random start and a fixed interval.")],
          "Drawing slips from a well-mixed box gives a simple random sample.", difficulty="easy")

    B.mcq(T, "A school has 400 freshmen, 350 sophomores, 300 juniors and 250 seniors. The principal selects a simple random sample of 20 students from each of the four grades and combines the four groups into one sample. What is the sampling method?",
          ch("A stratified random sample, because the population was divided into grades and a simple random sample was selected from each grade", "A stratified sample divides the population into non-overlapping strata, selects a simple random sample from each, and combines them."),
          [ch("A cluster random sample, because each of the four grades was a group of students that was included in the sample", "In a cluster sample, a random sample of the groups is chosen and every individual in the chosen groups is included."),
           ch("A simple random sample, because the same number of students was selected from each of the four grades, and each student had the same chance", "In a simple random sample every sample of 80 students has the same chance. Here exactly 20 come from each grade, and a senior (20 of 250) is more likely to be chosen than a freshman (20 of 400)."),
           ch("A systematic random sample, because the principal selected the same number of students from each one of the grades", "A systematic sample uses a random start and a fixed interval.")],
          "Dividing the population into strata and taking an SRS within each stratum is a stratified random sample.", difficulty="medium")

    B.mcq(T, "A company has 30 delivery trucks. The manager randomly selects 4 of the trucks and inspects every one of the packages in each of the 4 trucks. What is the sampling method?",
          ch("A cluster random sample, because a random sample of groups (trucks) was selected and every unit in the selected groups was observed", "A simple random sample of clusters is selected and data are collected from all of the units in each selected cluster."),
          [ch("A stratified random sample, because the packages are divided into groups by truck and some packages are inspected from each of the groups", "In a stratified sample, a sample is taken from every stratum. Here only 4 of the trucks were used."),
           ch("A simple random sample, because the trucks were selected by chance from all of the trucks that the company has", "The packages were not selected individually. Whole trucks were selected."),
           ch("A systematic random sample, because the trucks were inspected one after another with the same procedure", "A systematic sample uses a random start and a fixed interval.")],
          "Randomly choosing groups and observing every unit in them is a cluster random sample.", difficulty="medium")

    B.mcq(T, "A quality inspector chooses a random starting point among the first 10 items that come off a production line, and then inspects every 10th item after that starting point. What is the sampling method?",
          ch("A systematic random sample, because the items are selected using a random start and a fixed interval", "A systematic random sample has a random starting point and a fixed, periodic interval."),
          [ch("A simple random sample, because the starting point of the inspector was chosen at random from the first 10 items", "Not every group of items has the same chance. The items after the start are determined."),
           ch("A stratified random sample, because the items were divided into groups of 10 before one item was chosen from each", "A stratified sample has a simple random sample in each of the strata, which are groups of similar items."),
           ch("A cluster random sample, because the inspector examined the items that were in several groups of 10 items", "A cluster sample includes every unit in the selected clusters. Here only one item in 10 is inspected.")],
          "A random start with a fixed interval is a systematic random sample.", difficulty="medium")

    B.mcq(T, "Which of the following describes a difference between a stratified random sample and a cluster random sample?",
          ch("In a stratified sample, a simple random sample is taken from every stratum, and in a cluster sample, a simple random sample of the clusters is taken and every unit in each selected cluster is observed", "These are the definitions of the two methods."),
          [ch("In a stratified sample, every unit in each selected group is observed, and in a cluster sample, a simple random sample is taken from every group", "These are reversed."),
           ch("In a stratified sample, the groups should be as different from each other as possible, and in a cluster sample, the groups should be alike inside", "Strata are groups of similar individuals, and clusters should each be like the whole population."),
           ch("A stratified sample is always a larger sample than a cluster sample, because it must include every individual in the population", "Neither method requires a sample that includes everyone.")],
          "Stratified: SRS within every stratum. Cluster: SRS of clusters, then every unit in each selected cluster.", difficulty="hard")

    B.mcq(T, "In which of the following is an observational unit selected without replacement?",
          ch("A name is drawn from a hat, and it is not put back before the next name is drawn, so no one can be chosen twice", "In sampling without replacement a unit can be selected only once."),
          [ch("A name is drawn from a hat, and it is put back in the hat before the next name is drawn, so a name can be chosen twice", "This is sampling with replacement."),
           ch("A student is chosen by a random number generator that may give the same number for more than one of the draws", "If a number can repeat, the units are selected with replacement."),
           ch("A card is drawn from a deck, and the card is returned to the deck and shuffled before the next of the draws", "Returning the card to the deck is sampling with replacement.")],
          "Sampling without replacement means a unit can be selected only once.", difficulty="medium")

    B.mcq(T, "A population has 10 individuals. A sampling method selects a sample of 2 individuals by choosing individual number 1, 2, 3, 4 or 5 at random, and then always selecting the individual who is 5 places after the first one. Which of the following is true about the method?",
          ch("Every individual has the same chance of being selected, but the method is not a simple random sample, because some pairs of individuals can never be the sample", "In a simple random sample every sample of size n has the same chance. Here pairs that are not 5 apart are impossible."),
          [ch("The method is a simple random sample, because every one of the individuals has the same chance of being in the sample", "Equal chances for individuals are not enough. Every sample of size 2 must have the same chance."),
           ch("The method is a simple random sample, because the first individual that was selected was chosen by a random mechanism", "Only the first individual is chosen at random. The second one is determined."),
           ch("The method is not random, because the first individual in the sample is not chosen with the help of any random mechanism", "The first individual is chosen at random.")],
          "A simple random sample needs every sample of size n to be equally likely. This is a systematic-type method.", difficulty="hard")

    B.mcq(T, "A teacher wants to select a simple random sample of 25 students from a list of 400 students. Which of the following describes a correct procedure?",
          ch("Number the students from 1 to 400, use a random number generator to select 25 different numbers from 1 to 400, and use the students with those numbers", "Assign each individual a number, and randomly select n different numbers."),
          [ch("Choose the first 25 students on the alphabetical list, because the order of the names of the students in a list is random, so they are a fair sample of the 400", "The first 25 names are not selected using a random mechanism."),
           ch("Select the 25 students who volunteer first when the teacher asks for volunteers from the whole group of 400 students", "A sample of volunteers is not selected using a random mechanism."),
           ch("Number the students from 1 to 400, and then use every 16th student, starting from the student with the number 1", "This is a systematic method with a fixed start. It is not a simple random sample.")],
          "A random number generator applied to a numbered list gives a simple random sample.", difficulty="medium")

    B.mcq(T, "The manager of a mall wants to survey shoppers and wants to make sure that adults younger than 30, adults from 30 to 59, and adults 60 or older are all represented in the sample in proportion to their numbers. Which of the following sampling methods is the most appropriate?",
          ch("A stratified random sample, because the three age groups are the strata and a random sample is selected from each", "A stratified sample guarantees that each stratum is represented in the sample."),
          [ch("A cluster random sample, with the three age groups as the clusters to be selected one at a time by the manager", "A cluster sample could leave out entire age groups."),
           ch("A simple random sample, because it always has exactly the same percent of each age group as the whole population has", "A simple random sample does not guarantee the same percent of each of the groups."),
           ch("A convenience sample of the shoppers who walk by the manager, since they are of all of the ages of the group", "A convenience sample is not random and does not control the representation of the age groups.")],
          "To represent each of the groups, use a stratified random sample.", difficulty="medium")

    B.mcq(T, "A school wants to survey its students, who are organized in 40 homerooms of similar composition and size. To save time, the school wants to visit only some of the homerooms. Which of the following sampling methods is the most appropriate?",
          ch("A cluster random sample, in which several homerooms are selected at random and every student in each of the selected homerooms is surveyed", "Clusters that are similar to one another and to the population make a cluster sample appropriate and convenient."),
          [ch("A stratified random sample, in which one student is surveyed in each of the homerooms that are in the school", "This visits every homeroom, which does not save time in visiting only some of them."),
           ch("A systematic random sample, in which the students are surveyed in the order in which they arrive at the school", "That would not limit the survey to some of the homerooms."),
           ch("A convenience sample, in which the homerooms that are closest to the office are chosen to be in the survey", "Choosing the closest homerooms is not random.")],
          "When clusters are similar to the population, selecting some clusters at random saves effort.", difficulty="medium")
