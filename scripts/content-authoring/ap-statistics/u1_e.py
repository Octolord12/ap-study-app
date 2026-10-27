"""Unit 1, topics 1.12 and 1.13.

Required content (CED effective Fall 2026): 1.12 bias is a systematic error that makes a statistic consistently larger or smaller than the parameter; voluntary response bias, undercoverage bias, nonresponse bias, response bias
(confusing or leading questions, self-reported answers); nonrandom methods (convenience, voluntary response) introduce potential bias. 1.13 a well-designed experiment has comparison of at least two treatment groups (one may be a
control or placebo), random assignment of treatments to experimental units, replication and direct control of extraneous variables; single- and double-blind; the purpose of random assignment is similar groups; confounding;
completely randomized design, randomized block design (blocking variable, treatments randomly assigned within each block) and matched pairs; random assignment allows cause-and-effect conclusions; volunteers limit
generalization to similar individuals. Skills 2.A, 2.B.
"""
from lib import *


def build(B):
    # ------------------------------------------------------------------------------------------------------------ 1.12
    T = 12
    B.mcq(T, "A radio station asks its listeners to call in to say whether they support building a new stadium. Of the 800 callers, 72% say they are against it. Which type of bias is most likely to affect this result?",
          ch("Voluntary response bias, because the sample consists only of listeners who chose to call in", "Voluntary response bias may occur when a sample consists entirely of volunteers, who often have strong opinions."),
          [ch("Undercoverage bias, because the listeners who have a telephone are the only people who are included in the survey", "Undercoverage is about a part of the population that has no chance of being included. The main issue here is that the callers volunteered."),
           ch("Nonresponse bias, because many of the people who were chosen to be in the sample did not give any response", "No one was chosen. Listeners decided for themselves to call."),
           ch("Response bias, because the question in the survey that the radio station asked of the callers was written in a leading way", "Nothing in the description says that the question was leading.")],
          "A sample that consists entirely of volunteers may suffer from voluntary response bias.", difficulty="easy")

    B.mcq(T, "A researcher wants to estimate the proportion of all adults in a large city who use public transportation. The researcher selects a simple random sample of the telephone numbers in the city's landline telephone directory and calls them. Which of the following is the most likely source of bias?",
          ch("Undercoverage bias, because adults who do not have a landline telephone listed in the directory have no chance of being selected", "Undercoverage bias may occur when part of the population is left out of the sampling method or is less likely to be selected."),
          [ch("Voluntary response bias, because the adults who were called decided to answer the telephone for the researcher", "The numbers were selected at random. The adults did not volunteer to be in the sample."),
           ch("Response bias, because adults are always less honest with a researcher who calls them on the telephone", "Nothing suggests that the questions are leading, or that adults answer dishonestly."),
           ch("There is no source of bias, because the telephone numbers were selected from the directory using a simple random sample", "A random selection from a list that leaves out part of the population can still be biased.")],
          "Using a landline directory leaves out part of the population: undercoverage.", difficulty="medium")

    B.mcq(T, "A school mails a survey to 1,000 randomly selected parents. Only 120 of the surveys are returned. Which of the following is the most likely source of bias?",
          ch("Nonresponse bias, because the parents who returned the survey may differ in important ways from the parents who did not", "Nonresponse bias may occur because of a failure to obtain responses from some individuals who were chosen."),
          [ch("Voluntary response bias, because the parents who sent the survey back chose to take part in the study", "The parents were randomly selected, so they did not volunteer to be in the sample. The main problem is that most of the selected parents did not respond."),
           ch("Undercoverage bias, because some of the parents in the school were not included in the list from which the sample was selected", "The 1,000 parents were selected from the parents. The main problem is that most of them did not respond."),
           ch("There is no source of bias, because the 1,000 parents were selected at random and a random sample has no bias", "Nonresponse can bias even a random sample.")],
          "The respondents and nonrespondents could differ in important ways: nonresponse bias.", difficulty="medium")

    B.mcq(T, "A survey asks, \"Do you agree that the city's wonderful new park is an excellent use of tax money?\" Which type of bias is most likely to result from the wording of this question?",
          ch("Response bias, because the wording of the question leads respondents to answer in one direction", "Questions that are confusing or leading (question wording bias) can cause responses to differ from the true value in one direction."),
          [ch("Undercoverage bias, because some residents who live in the city will not see the question of the survey", "Undercoverage is about who can be selected. The problem here is the wording."),
           ch("Nonresponse bias, because many residents who are asked the question will refuse to give any answer at all", "The wording of the question is the problem, not a failure to respond."),
           ch("Voluntary response bias, because respondents who like the park will choose to answer the question in the survey", "The problem is the leading wording, not a sample of volunteers.")],
          "A leading question is a source of response bias.", difficulty="easy")

    B.mcq(T, "A researcher asks a random sample of adults how many hours they exercise each week. Many of the adults in the sample report more exercise than they actually do. Which of the following best describes this problem?",
          ch("Response bias, because the self-reported answers tend to differ from the true values in one direction", "Self-reported responses are an example of response bias."),
          [ch("Undercoverage bias, because the adults who exercise the most are not included in the list that was used to select the sample", "The problem is not a part of the population that was left out. It is the accuracy of the answers."),
           ch("Voluntary response bias, because the adults who exercise are the ones who answer questions about their exercise", "The adults were selected at random. They did not volunteer."),
           ch("Sampling error only, because the amount of the exercise differs from one random sample of the adults to another", "The responses are consistently too large, which is a systematic error, not random variation.")],
          "Self-reported responses that tend to differ from the truth in one direction are response bias.", difficulty="medium")

    B.mcq(T, "To estimate the proportion of students at a school who own a smartphone, a researcher stands at the school's main door and asks the first 50 students who arrive. Which of the following is correct?",
          ch("The method is a convenience sample, which is not random, so students who arrive early may differ from the others", "Nonrandom sampling methods, such as samples chosen by convenience, introduce potential bias."),
          [ch("The method is a simple random sample, because the students were selected without the researcher knowing who they were", "Not knowing who will arrive does not make the selection random."),
           ch("The method is not biased, because the proportion of students who own a smartphone cannot depend on when they arrive", "The students who arrive first may differ, and the method does not use random chance."),
           ch("The method is a stratified random sample, because the students at the door arrive in groups by grade level", "Strata require a simple random sample within each of the groups.")],
          "A convenience sample does not use random chance, so it has potential bias.", difficulty="medium")

    B.mcq(T, "Which of the following describes bias in a sampling method?",
          ch("A systematic error that results in a statistic being consistently larger, or consistently smaller, than the parameter it is used to estimate", "Bias is a systematic error in the sampling procedure."),
          [ch("The difference between the value of a statistic for one sample and its value for another sample that is selected from the same population, which is called sampling variability", "This is the natural variation from sample to sample, not bias."),
           ch("The error that results from a sample that is too small, so that a statistic is not exactly the same as the parameter", "A small sample causes more variability, but bias is a systematic error that does not average out."),
           ch("Any mistake in recording the data, such as typing an incorrect value for one of the observations in the sample", "A recording mistake is not a systematic error of the sampling procedure.")],
          "Bias is a systematic error in the sampling procedure that makes a statistic consistently too large or too small.", difficulty="medium")

    B.mcq(T, "An online poll about a political issue receives 50,000 responses from people who chose to visit the website and vote. A student says that, because the sample is so large, the poll results must be a good estimate of the opinion of all adults. Which of the following is the best response to the student?",
          ch("A large sample does not remove bias. The sample consists of volunteers, so the results may not represent all adults", "Nonrandom sampling methods, such as voluntary response, introduce potential bias that a larger sample does not remove."),
          [ch("The student is correct, because the larger a sample is, the smaller the bias of the results of a poll will be", "Increasing the sample size does not reduce bias from a poor sampling method."),
           ch("The student is correct, because a sample of 50,000 responses is far larger than the samples that most polls use", "The number of responses does not make the sample representative."),
           ch("The student is incorrect, because an online poll can never be used to estimate the opinions of any group of people", "The problem is the voluntary response method, not the Internet.")],
          "A large nonrandom sample still has bias.", difficulty="hard")

    B.mcq(T, "A researcher surveys only members of a gym about how often they exercise, and uses the result to estimate the proportion of all adults in the city who exercise at least three times a week. Which of the following is the most likely effect on the estimate?",
          ch("The estimate is likely to be consistently larger than the true proportion, because gym members are more likely to exercise than the other adults", "The method leaves out people who are less likely to exercise, so the statistic tends to be too large."),
          [ch("The estimate is likely to be consistently smaller than the true proportion, because gym members have less free time to exercise than other adults do", "Nothing indicates that gym members exercise less often."),
           ch("The estimate is equally likely to be too large as it is to be too small, because the gym members are a random group of adults", "Gym members are not a random group, and the error is in one direction."),
           ch("The estimate has no bias, because every gym member was included in the survey that the researcher conducted", "Including every gym member does not make the sample represent all of the adults.")],
          "The sampling method leaves out adults who are less likely to exercise, so the estimate is biased high.", difficulty="hard")

    # ------------------------------------------------------------------------------------------------------------ 1.13
    T = 13
    B.mcq(T, "A researcher gives all 40 of the participants in a study a new fertilizer for their garden plants and records the growth of the plants. Which element of a well-designed experiment is missing?",
          ch("A comparison of at least two treatment groups, such as a group that gets the new fertilizer and a control group that does not", "A well-designed experiment compares at least two treatments, one of which could be a control group."),
          [ch("Replication, because a study with 40 participants has too few participants to apply the treatment more than once", "There are 40 participants, so the treatment is applied to more than one experimental unit."),
           ch("A response variable, because the growth of the plants is not a quantity that the researcher can measure in a garden", "The growth of the plants is a measurable response variable."),
           ch("A sample, because a sample of 40 participants cannot be used in an experiment that is designed to compare treatments", "Experiments are conducted with groups of experimental units.")],
          "With only one treatment group there is nothing to compare with.", difficulty="medium")

    B.mcq(T, "In a study of a new pain medicine, one group of patients takes the medicine and another group takes a pill that has no active ingredient. What is the purpose of the group that takes the pill with no active ingredient?",
          ch("It is a control group that provides a comparison, so that any effect of the medicine can be separated from the effect of simply taking a pill", "A control group may be given an inactive substance (a placebo) to determine whether the treatment of interest has an effect."),
          [ch("It makes sure that every patient in the study has the same chance of getting the new medicine, so that the two groups are alike at the start of the study", "That is the purpose of random assignment, not of a placebo group."),
           ch("It makes the study a double-blind study, because the patients in the group do not take any of the active medicine", "Blinding refers to who knows which treatment is received, which is a separate part of the design."),
           ch("It increases the number of patients in the study, so that the medicine can be tested on many more patients", "The group is for comparison. It is not just for adding more patients.")],
          "A placebo control group is used for comparison.", difficulty="easy")

    B.mcq(T, "In an experiment, the patients do not know which treatment they receive, but the doctors who give the treatments and measure the results do know. Which of the following describes this experiment?",
          ch("It is a single-blind experiment, because the participants do not know which treatment they receive but members of the research team do", "In a single-blind experiment the participants do not know the treatment, but the research team members who interact with them do."),
          [ch("It is a double-blind experiment, because the patients do not know which of the treatments they have been given", "In a double-blind experiment neither the participants nor the research team members who interact with them know."),
           ch("It is not blind at all, because the doctors know which treatment each of the patients receives in the experiment", "The patients do not know, so the experiment is single-blind."),
           ch("It is a placebo experiment, because the patients do not know the treatment and the doctors do know the treatment", "A placebo is an inactive treatment. Blinding is about who knows the treatments.")],
          "Only the participants are blinded: a single-blind experiment.", difficulty="medium")

    B.mcq(T, "What is the main purpose of the random assignment of treatments to experimental units in an experiment?",
          ch("To create treatment groups that are as similar as possible with respect to extraneous variables, so the groups differ only by the treatment", "If random assignment is successful, the distributions of each extraneous variable will be approximately the same in all of the treatment groups."),
          [ch("To make sure that the experimental units in the study are representative of a larger population of units", "That is the purpose of random selection from a population."),
           ch("To make sure that the experimenters and the participants cannot know which of the treatments each unit receives", "That is the purpose of blinding."),
           ch("To make sure that each treatment is applied to exactly one experimental unit, so that the result can be compared", "Each treatment should be applied to more than one unit (replication).")],
          "Random assignment creates groups that are similar with respect to extraneous variables.", difficulty="medium")

    B.mcq(T, "A teacher tests a new study method. Students in a morning class use the new method, and students in an afternoon class use the usual method. The students in the morning class score higher on the next test. Which of the following is a confounding variable in this study?",
          ch("The time of day of the class, because it is related to the study method that each class used and could also affect the scores", "A confounding variable is related to the explanatory variable in a way that makes it hard to tell which variable influences the response."),
          [ch("The test score, because it is the outcome that the teacher measured for each of the students in the classes", "The score is the response variable."),
           ch("The study method, because it is the treatment that the teacher chose for each one of the two classes", "The study method is the explanatory variable."),
           ch("The number of students in each class, because it is the same for the two classes that were in the study", "A variable that is the same for both groups cannot explain a difference between them.")],
          "The time of day goes together with the method, so its effect cannot be separated from the effect of the method.", difficulty="medium")

    B.mcq(T, "In an experiment, replication means which of the following?",
          ch("More than one experimental unit is assigned to each treatment, rather than a single unit", "Replication means more than one experimental unit is assigned to each treatment."),
          [ch("The same experimental unit receives each treatment more than one time during the experiment", "That describes repeated measurements on one unit, not replication."),
           ch("The experiment is repeated by other researchers in different locations on a later date", "That describes a repetition of the whole study by other researchers."),
           ch("Each experimental unit is given a treatment that has been used in an earlier experiment by the researcher", "Replication is about the number of units per treatment.")],
          "Replication means that more than one experimental unit is assigned to each treatment.", difficulty="easy")

    B.mcq(T, "In an experiment on plant growth, the researcher keeps the amount of water, the type of soil and the temperature of the room the same for every plant. Which element of a well-designed experiment does this describe?",
          ch("Direct control of potential extraneous sources of variation", "Direct control keeps the settings of extraneous variables the same from one experimental unit to another."),
          [ch("Random assignment of the treatments to the plants", "Random assignment uses chance to decide which unit gets which treatment."),
           ch("Replication of each treatment on several of the plants", "Replication means using more than one unit for each treatment."),
           ch("Blocking of the plants into groups that are similar", "Blocking groups similar units and randomizes treatments within each of the groups.")],
          "Keeping extraneous variables the same for all of the units is direct control.", difficulty="easy")

    B.mcq(T, "A researcher has 60 volunteers. The researcher uses a random number generator to assign 20 of the volunteers to each of three diets, with no other grouping of the volunteers. Which of the following experimental designs is this?",
          ch("A completely randomized design, because the treatments are assigned to the volunteers completely at random", "In a completely randomized design, treatments are assigned to experimental units completely at random."),
          [ch("A randomized block design, because the volunteers were divided into three groups for the three different diets", "Blocks are groups of similar units that are formed before the treatments are randomly assigned within each block."),
           ch("A matched pairs design, because the volunteers were assigned in equal numbers to the diets of the study", "A matched pairs design has two treatments and pairs of similar units."),
           ch("An observational study, because the researcher is working with a group of volunteers who chose to take part", "The researcher assigned the diets, so this is an experiment.")],
          "Randomly assigning treatments to all of the units without grouping is a completely randomized design.", difficulty="medium")

    B.mcq(T, "A researcher believes that the effect of a medicine may be different for men and for women. The researcher separates 60 men and 60 women into two groups, and within each group randomly assigns half to the medicine and half to a placebo. Which of the following describes the design and the purpose of the grouping?",
          ch("It is a randomized block design with sex as the blocking variable, and blocking allows the treatments to be compared without variation from the blocking variable", "In a randomized block design, units are grouped by a blocking variable, and treatments are randomly assigned within each block."),
          [ch("It is a completely randomized design, and the grouping by sex is used to make the volunteers a random sample", "In a completely randomized design there is no grouping before the assignment."),
           ch("It is a randomized block design, and the grouping by sex is used to blind the volunteers to the treatment they get", "Blocking is not used for blinding."),
           ch("It is a matched pairs design, because there are two treatments that are given to two groups of volunteers", "Matched pairs arranges units into pairs, and each pair gets both treatments.")],
          "Grouping by a source of variation and randomizing within each group is a randomized block design.", difficulty="hard")

    B.mcq(T, "A company wants to compare two brands of running shoes. Each of 25 runners runs a race in one brand of shoe and, on another day, in the other brand of shoe. A coin flip decides which brand each runner wears first. Which of the following describes the design?",
          ch("It is a matched pairs design, because each runner receives both treatments and the order of the treatments is randomized", "In a matched pairs design each experimental unit may get both treatments while the order of the treatments is randomized."),
          [ch("It is a completely randomized design, because a coin flip is used to decide the treatment of each of the runners", "In a completely randomized design each unit receives only one treatment."),
           ch("It is an observational study, because the runners are free to choose which brand of shoe they wear on the first day", "The coin flip, not the runner, decides, so this is an experiment."),
           ch("It is a randomized block design with 25 treatments, because there are 25 runners in the study of the two brands", "There are two treatments, so the design with blocks of pairs is a matched pairs design.")],
          "Each runner gets both treatments in a random order: matched pairs.", difficulty="medium")

    B.mcq(T, "A well-designed experiment finds that the mean response is greater for the treatment group than for the control group. Which of the following conclusions is justified by the use of random assignment?",
          ch("The difference in the responses was caused by the treatment, because random assignment reduces the potential for confounding variables", "Random assignment of treatments allows cause-and-effect conclusions."),
          [ch("The treatment would cause the same difference for every individual in the population from which the units were selected", "The conclusion about the population depends on how the units were selected."),
           ch("The treatment caused the difference, but this cannot be a cause-and-effect conclusion, because no experiment can show cause and effect", "A well-designed experiment can show cause and effect."),
           ch("The difference in the responses must be due to chance alone, because the units were assigned to the groups using chance", "Random assignment does not mean that a difference is due to chance.")],
          "Random assignment allows cause-and-effect conclusions.", difficulty="medium")

    B.mcq(T, "Researchers recruit 100 volunteers for an experiment, and randomly assign 50 to a new exercise program and 50 to a control group. The group with the program lowers its blood pressure more. For which of the following is it appropriate to conclude that the program causes a lowering of blood pressure?",
          ch("People who are similar to the volunteers, because the treatments were randomly assigned but the volunteers were not randomly selected", "The experimental units were obtained from volunteers, so the results represent experimental units similar to those who took part."),
          [ch("All adults in the country, because the volunteers were assigned to the treatments by the use of chance", "Random assignment supports cause and effect. It does not support generalizing to all adults."),
           ch("Only the 50 volunteers in the group that took the program, because the control group did not get the program", "The comparison of the two groups supports the conclusion for similar volunteers, not just one group."),
           ch("Nobody, because a study that uses volunteers cannot support a cause-and-effect conclusion about any group of people", "Random assignment still supports cause and effect for similar individuals.")],
          "Volunteers limit generalization to similar individuals; random assignment allows cause and effect.", difficulty="hard")
