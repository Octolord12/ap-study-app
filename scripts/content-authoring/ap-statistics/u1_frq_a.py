"""Unit 1 free response, part 1: eight COLLECT_DATA prompts (the exam's Question 1: practices 1 and 2: formulate questions, collect data), 10 points each.

  F1 1.11 three survey methods in a park      F2 1.13 a completely randomized experiment (music and a vocabulary test)
  F3 1.13 matched pairs (an energy drink)     F4 1.12 a customer survey with nonresponse and a leading question
  F5 1.10 observational study and confounding F6 1.11 stratified and cluster samples for a school district
  F7 1.13 a randomized block design           F8 1.10 an investigative question, a census and a sample
"""
from lib import *


def L(*lines):
    return [(1, t) for t in lines]


def build(B):
    # ----------------------------------------------------------------------------------------------------------- F1
    setup = ("A national park wants to learn how visitors rate its trails. About 12,000 visitors come to the park on a typical weekend. The park is considering three methods of collecting data.\n\n"
             "Method 1: Each visitor is given a different number when entering the park. A random number generator selects 400 different numbers, and the visitors with those numbers are surveyed.\n\n"
             "Method 2: The park has three entrances (North, East, and South) that are used by different kinds of visitors. At each entrance, a random number generator selects 150 visitors, and these visitors are surveyed.\n\n"
             "Method 3: A comment box is placed near the visitor center, and visitors are invited to drop in a rating card if they wish.")
    parts = [("A", "(i) Identify the sampling method for Method 1.\n\n(ii) Identify the sampling method for Method 2."),
             ("B", "(i) Explain why the results of Method 1 can be generalized to all of the visitors to the park that weekend.\n\n(ii) Describe one advantage of Method 2 over Method 1."),
             ("C", "(i) Identify the type of bias that is most likely to affect the results of Method 3.\n\n(ii) Describe how the ratings from Method 3 would likely differ from the ratings of all of the visitors."),
             ("D", "Each surveyed visitor will rate the trails as Excellent, Good, Fair, or Poor. (i) Identify a graphical display that is appropriate for the percent of visitors who chose each rating.\n\n(ii) Explain why the display is appropriate."),
             ("E", "The park wants to know whether the mean rating of the trails, on a scale from 1 to 5, is greater for visitors who come with children than for visitors who come without children. Determine a valid investigative question for this study. Ensure that all three components of a valid investigative question are included in your response.")]
    ans = [("A", "(i) Method 1 is a simple random sample. (ii) Method 2 is a stratified random sample, with the three entrances as the strata."),
           ("B", "(i) The visitors were selected using a random number generator, so the sample is likely to be representative of all of the visitors that weekend, and the results can be generalized to them. (ii) Method 2 makes sure that visitors from each of the three entrances are included, which helps if visitors who use different entrances have different opinions."),
           ("C", "(i) Voluntary response bias. (ii) Visitors who choose to drop in a card are likely to be those with strong opinions, for example very happy or very unhappy, so the ratings are probably not representative of all of the visitors."),
           ("D", "(i) A bar chart (or a pie chart) of the percents. (ii) The rating is a categorical variable, and a bar chart shows the relative frequency of each category."),
           ("E", "Is the mean rating of the trails, on a scale from 1 to 5, greater for visitors to the park who come with children than for visitors who come without children? The visitors who are selected at random from all of the visitors to the park should be used, and since this is an observational study the conclusion can be about an association for those visitors, not about cause and effect.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(11, "COLLECT_DATA", prompt,
          L("A(i): Identifies Method 1 as a simple random sample.",
            "A(ii): Identifies Method 2 as a stratified random sample (with the entrances as the strata).",
            "B(i): Explains that the visitors were selected using a random mechanism, so the sample is representative and the results can be generalized to all of the visitors that weekend.",
            "B(ii): Describes an advantage of Method 2: it guarantees that each of the entrances is represented in the sample (which helps when visitors at the entrances differ).",
            "C(i): Identifies voluntary response bias.",
            "C(ii): Describes the likely difference: visitors with strong opinions (very satisfied or very dissatisfied) would be more likely to respond, so the ratings would not represent all of the visitors.",
            "D(i): Identifies a bar chart (or a pie chart) of the relative frequencies.",
            "D(ii): Explains that the rating is a categorical variable and that a bar chart displays the relative frequency of each category.",
            "E: Gives an investigative question that is about the variable (the trail rating) and the parameter with the direction of the alternative (the mean rating greater for visitors with children).",
            "E: Includes the population to which the conclusion applies (the visitors to the park) and the type of conclusion (association, since it is an observational study, not cause and effect)."),
          sample)

    # ----------------------------------------------------------------------------------------------------------- F2
    setup = ("A teacher wants to know whether listening to instrumental music while studying changes how well students do on a vocabulary test. Sixty students who volunteered will take part. Each student will study the same list of words for 20 minutes and will then take the same test.")
    parts = [("A", "Describe a completely randomized design for an experiment that can be used to investigate the teacher's question. Include the treatments and describe how the treatments are assigned to the students using a random method."),
             ("B", "(i) Identify the experimental units in the experiment.\n\n(ii) Identify the response variable."),
             ("C", "Explain why the students cannot be blinded to the treatment in this experiment, and identify a person who could be blinded."),
             ("D", "Identify one extraneous variable that the teacher should control in this experiment, and describe how the teacher could control it."),
             ("E", "Suppose that the group that listened to music scores higher, on average, than the other group, by more than would be expected from chance alone. (i) Explain why the teacher can conclude that the music caused the higher scores.\n\n(ii) The students were volunteers. To which group of students can the conclusion be applied?")]
    ans = [("A", "The two treatments are studying with instrumental music and studying without music. Number the 60 students from 1 to 60, use a random number generator to select 30 different numbers, and assign the students with those numbers to the music group. The other 30 students are assigned to the group with no music."),
           ("B", "(i) The experimental units are the 60 students. (ii) The response variable is the score on the vocabulary test."),
           ("C", "A student knows whether music is playing, so the students cannot be blinded. The person who grades the tests could be blinded by not being told which group each student was in."),
           ("D", "The amount of study time, the word list, the room, or the time of day. For example, the teacher could have all of the students study in the same room, at the same time of day, with the same word list and for exactly 20 minutes."),
           ("E", "(i) The students were randomly assigned to the treatments, so the two groups should be similar in all of the other variables that could affect the scores. A difference in the scores is therefore likely to have been caused by the music. (ii) Only students who are similar to the volunteers, because the students were not randomly selected from a larger population.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(13, "COLLECT_DATA", prompt,
          L("A: Identifies two treatments (instrumental music and no music, or a control).",
            "A: Describes a random assignment method (for example, numbering the 60 students and using a random number generator to select 30 different students for the music group).",
            "A: Makes the design completely randomized with more than one student per treatment (30 in each group, or all of the students assigned at random with no grouping).",
            "B(i): Identifies the experimental units as the 60 students.",
            "B(ii): Identifies the response variable as the score on the vocabulary test.",
            "C: Explains that the students know whether they are listening to music (so they cannot be blinded) and identifies someone who could be blinded, such as the person who grades the tests.",
            "D(i): Identifies an extraneous variable, such as the amount of study time, the word list, the room, or the time of day.",
            "D(ii): Describes how to control it directly (keep it the same for all of the students).",
            "E(i): Explains that random assignment makes the groups similar with respect to other variables, so that a difference in scores can be attributed to (caused by) the music.",
            "E(ii): Identifies that the conclusion applies only to students similar to the volunteers (the volunteers were not randomly selected from a larger population)."),
          sample)

    # ----------------------------------------------------------------------------------------------------------- F3
    setup = ("A company claims that its energy drink shortens a person's reaction time. A researcher recruits 24 volunteers. Each volunteer will have their reaction time measured twice, on two different days: once after drinking the energy drink and once after drinking a drink that looks and tastes the same but has no active ingredient. For each volunteer, a coin flip will decide which drink is taken first.")
    parts = [("A", "(i) Identify the type of experimental design that the researcher is using.\n\n(ii) Identify the response variable."),
             ("B", "Explain why using each volunteer for both treatments can make the comparison of the two drinks more precise than assigning each volunteer to only one drink."),
             ("C", "Explain why a coin flip is used to decide which drink each volunteer takes first."),
             ("D", "(i) Explain how the researcher can make the experiment double-blind.\n\n(ii) Identify one reason why a double-blind design is helpful."),
             ("E", "The volunteers were not selected at random from all adults. Explain what type of conclusion the researcher can make if the mean reaction time is shorter after the energy drink than after the other drink, by more than would be expected from chance alone.")]
    ans = [("A", "(i) A matched pairs design, since every volunteer gets both treatments and the order is randomized. (ii) The response variable is the reaction time (for example, in milliseconds)."),
           ("B", "Each volunteer is compared with himself or herself, so the variation in reaction time from one person to another (an extraneous source of variation) does not affect the comparison of the drinks."),
           ("C", "It randomizes the order of the treatments, so that effects of the day or of learning from the first test are balanced between the two drinks, and are not confounded with the drink."),
           ("D", "(i) A person who has no information about which drink is which prepares the drinks, so neither the volunteers nor the people who measure reaction time know which one has the active ingredient. (ii) It prevents expectations of the volunteers or of the researchers from influencing the measured reaction times."),
           ("E", "Because the order of the treatments was randomized, the researcher can conclude that the energy drink caused the shorter reaction times, but only for people who are similar to the volunteers.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(13, "COLLECT_DATA", prompt,
          L("A(i): Identifies a matched pairs design (each volunteer receives both treatments in a random order).",
            "A(ii): Identifies the response variable as the reaction time.",
            "B: Explains that each volunteer is compared with himself or herself, so the comparison is not affected by differences between volunteers.",
            "B: Explains that this removes an extraneous source of variation (the variation in reaction time from one person to another), which makes the comparison more precise.",
            "C: Explains that randomizing the order balances out effects of the order (for example, practice or the day) between the two drinks.",
            "C: Explains that this keeps the order from being confounded with the drink.",
            "D(i): Describes how to make the experiment double-blind: the drinks look the same, and neither the volunteers nor the people who measure the reaction time know which drink was given.",
            "D(ii): Explains that blinding prevents the expectations of the volunteers and the researchers from affecting the responses.",
            "E: States that a cause-and-effect conclusion is possible because of the random assignment of the order of the treatments.",
            "E: States that the conclusion applies only to people who are similar to the volunteers, since they were not randomly selected."),
          sample)

    # ----------------------------------------------------------------------------------------------------------- F4
    setup = ("A company has 5,000 customers. To estimate the proportion of its customers who are satisfied with its service, the company emails a survey to all of its customers. The email begins, \"We take great pride in our excellent service. How satisfied were you with our excellent service?\" Of the 5,000 customers, 600 respond, and 540 of the 600 say they are satisfied.")
    parts = [("A", "Is the company's survey a census or a sample? Explain."),
             ("B", "(i) Identify one type of bias that might result from the number of customers who responded.\n\n(ii) Explain how this type of bias could affect the estimate of the proportion of all of the customers who are satisfied."),
             ("C", "(i) Identify one type of bias that might result from the wording of the question.\n\n(ii) Rewrite the question so that it does not lead the customers to a particular answer."),
             ("D", "The company reports that 90% of all customers are satisfied. Explain why this conclusion may not be justified. Give two different reasons."),
             ("E", "Describe a different method that the company could use to select a sample of customers that would reduce the bias from the number of customers who respond. Include how the customers are selected and how the company can reduce nonresponse among the selected customers.")]
    ans = [("A", "It is a sample, not a census, because only the 600 customers who responded provided data. Information was not obtained from every one of the 5,000 customers."),
           ("B", "(i) Nonresponse bias (and voluntary response bias). (ii) The 600 customers who responded may differ from the customers who did not respond. For example, customers who were very satisfied (or very unhappy) may be more likely to respond, so the proportion in the sample could be too large (or too small)."),
           ("C", "(i) Response bias (question wording bias), because the wording leads the customers to say that they are satisfied. (ii) \"How satisfied were you with the service that you received from our company?\", with response choices that include very satisfied and very dissatisfied."),
           ("D", "First, only 600 of the 5,000 customers responded, and the customers who responded may differ from the ones who did not, so the 90% may not be close to the proportion for all 5,000 customers. Second, the question was written in a leading way that encourages a satisfied answer, so the responses may be too positive."),
           ("E", "Select a simple random sample of 400 customers by numbering the customers from 1 to 5,000 and using a random number generator to select 400 different numbers. Then follow up with the customers who do not reply, by phone or by another email, so that nearly all of the selected customers respond.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(12, "COLLECT_DATA", prompt,
          L("A: Identifies the survey as a sample (not a census) because data were obtained from only the 600 customers who responded, and not from all of the customers.",
            "B(i): Identifies nonresponse bias (or voluntary response bias).",
            "B(ii): Explains that the customers who responded could differ from the customers who did not respond, so the sample proportion could be consistently too large or too small.",
            "C(i): Identifies response bias (question wording bias, a leading question).",
            "C(ii): Rewrites the question in a neutral way (without the words about excellent service) and without suggesting an answer.",
            "D: Gives the first reason: nonresponse (the customers who responded may differ from those who did not), so the statistic may not be close to the proportion for all of the customers.",
            "D: Gives the second reason: the wording of the question leads the customers to a satisfied answer, so the responses may be too positive.",
            "E: Describes a random selection method, such as a simple random sample of the customers.",
            "E: Describes the procedure (for example, numbering the customers from 1 to 5,000 and using a random number generator to select a number of different customers).",
            "E: Describes a way of reducing nonresponse (following up with the selected customers so that nearly all of them respond)."),
          sample)

    # ----------------------------------------------------------------------------------------------------------- F5
    setup = ("Researchers used the medical records of 3,000 adults to compare the rates of heart disease for adults who said that they eat fish at least once a week and adults who said that they eat fish less often than once a week. They found that the rate of heart disease was lower for the adults who eat fish at least once a week.")
    parts = [("A", "(i) Identify the type of study (experiment or observational study) that the researchers conducted.\n\n(ii) Is the study prospective or retrospective? Explain."),
             ("B", "Identify the explanatory variable and the response variable in this study."),
             ("C", "Explain why the researchers cannot conclude that eating fish causes a lower rate of heart disease."),
             ("D", "Identify a variable that could be a confounding variable in this study, and explain how it must be related to the other variables."),
             ("E", "Describe an experiment that could be used to investigate whether eating fish causes a lower rate of heart disease. Include how the treatments would be assigned.")]
    ans = [("A", "(i) An observational study. (ii) Retrospective, because the researchers used records of data that had already been collected."),
           ("B", "The explanatory variable is how often the adult eats fish (at least once a week or less often). The response variable is whether the adult has heart disease."),
           ("C", "The adults chose how much fish to eat, and the researchers did not assign the treatments. There could be other differences between the two groups, so the study shows an association but not a cause."),
           ("D", "The amount of exercise is a possible confounding variable. It must be associated with eating fish (adults who eat fish may exercise more) and also with the rate of heart disease (adults who exercise more may have less heart disease)."),
           ("E", "Select volunteers and use a random method, such as a random number generator, to assign half of the volunteers to a diet that includes fish at least once a week and half to a diet without fish. After some years compare the rates of heart disease of the two groups.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(10, "COLLECT_DATA", prompt,
          L("A(i): Identifies the study as an observational study.",
            "A(ii): Identifies the study as retrospective, because data from the past (records) were used.",
            "B: Identifies the explanatory variable as how often the adult eats fish.",
            "B: Identifies the response variable as whether the adult has heart disease.",
            "C: Explains that the treatments were not assigned by the researchers (the adults chose), so an observational study can show an association but not cause and effect.",
            "D(i): Identifies a plausible confounding variable (for example, amount of exercise, diet in general, income, or smoking).",
            "D(ii): Explains that the variable must be associated with both the explanatory variable (eating fish) and the response variable (heart disease).",
            "E: Describes an experiment that compares at least two treatments (a diet with fish and a diet without fish).",
            "E: Describes random assignment of the treatments to the experimental units (for example, a random number generator or a coin flip).",
            "E: Explains that, with random assignment, the experiment can show cause and effect (the potential for confounding is reduced)."),
          sample)

    # ----------------------------------------------------------------------------------------------------------- F6
    setup = ("A school district has 6,000 high school students at 12 high schools, with about 500 students at each school. The students are in grades 9, 10, 11, and 12, with about the same number in each grade. The district wants to survey a sample of about 1,000 students about the amount of homework they have each night.")
    parts = [("A", "Describe how the district could select a stratified random sample of 1,000 students, using the grades as the strata. Include how the random numbers are used and how many students are selected from each grade."),
             ("B", "Explain one advantage of using the grades as the strata."),
             ("C", "Describe how the district could select a cluster random sample of about 1,000 students, using the schools as the clusters. Include the number of schools that you choose."),
             ("D", "Identify one disadvantage of the cluster sample in part C compared with the stratified random sample in part A."),
             ("E", "The district wants the sample to represent students of all four grades. Which of the two samples, the stratified sample or the cluster sample, is better for this purpose? Justify your answer.")]
    ans = [("A", "Make a list of the students in each grade. Select 250 students from each grade (since the four grades are about the same size). Number the students in a grade from 1 to the number of students in the grade, use a random number generator to select 250 different numbers, and use the students with those numbers. Combine the four groups of 250 into one sample of 1,000."),
           ("B", "Each grade is guaranteed to be represented in the sample. If the amount of homework differs between the grades, the sample will include the right amount of students from each grade."),
           ("C", "Number the 12 schools from 1 to 12 and use a random number generator to select 2 different schools (about 500 students each). Then survey every one of the students at the 2 selected schools, which is about 1,000 students."),
           ("D", "The students at the chosen schools could be different from the students at the schools that were not chosen (if the schools are not alike), so the sample may not be representative of all of the students. The sample is also less spread out over the whole district."),
           ("E", "The stratified sample is better, because it selects students from each of the four grades. A cluster sample of schools may not have students from the same proportion of each grade, though each school has all grades, and it only includes some of the schools.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(11, "COLLECT_DATA", prompt,
          L("A: Describes dividing the students into the four grades (strata), selecting a simple random sample within each grade, and combining the four samples.",
            "A: Describes the use of random numbers (numbering the students in each grade and using a random number generator to select different numbers).",
            "A: Gives sample sizes for the grades that add to 1,000 (for example, 250 for each grade, because the grades are about the same size).",
            "B: Explains an advantage of using the grades as the strata: each grade is represented in the sample, and the amount of homework may differ between grades.",
            "C: Describes selecting a simple random sample of the schools (for example, numbering the schools and using a random number generator).",
            "C: Describes surveying every student at the chosen schools.",
            "C: Gives a number of schools that makes sense for the sample size (2 schools, which is about 1,000 students).",
            "D: Identifies a disadvantage of the cluster sample: the schools that are chosen may differ from the other schools, so the sample may not be representative of the district.",
            "E: Chooses the stratified random sample as the better method for representing all four grades.",
            "E: Justifies the choice: a stratified sample includes students from every grade, which is controlled by the sampling method, and a cluster sample does not control the grades."),
          sample)

    # ----------------------------------------------------------------------------------------------------------- F7
    setup = ("An agronomist wants to compare three fertilizers, A, B, and C, for growing corn. The agronomist has 24 equal plots of land in four fields. Each field has 6 plots, and the soil quality is different from one field to another but is about the same within a field.")
    parts = [("A", "Identify a blocking variable for an experiment on the fertilizers, and explain why it should be used as a blocking variable."),
             ("B", "Describe how the agronomist could randomly assign the fertilizers to the plots in a randomized block design."),
             ("C", "Explain what replication means in this experiment, and how many plots are assigned to each fertilizer."),
             ("D", "Explain one advantage of a randomized block design over a completely randomized design in this experiment."),
             ("E", "The agronomist finds that the mean yield is greater for fertilizer B than for fertilizers A and C. What type of conclusion is justified by the design of the experiment? Explain.")]
    ans = [("A", "The field (the soil quality) is a blocking variable. Soil quality is a source of variation in the yield that is not the fertilizer, and the plots within one field are alike."),
           ("B", "Treat each field as a block of 6 plots. Within each field, use a random number generator to assign two of the 6 plots to each fertilizer (for example, number the plots 1 to 6 and randomly select two for A, two for B and two for C). Do this separately for each of the four fields."),
           ("C", "Replication means that more than one experimental unit is assigned to each treatment. Each fertilizer is assigned to 8 plots (2 in each of the 4 fields)."),
           ("D", "Blocking separates the variation in yield that is caused by the soil quality from the variation caused by the fertilizers, so the fertilizers can be compared within the fields without the differences in soil, which makes the comparison more precise."),
           ("E", "A cause-and-effect conclusion, because the fertilizers were randomly assigned to the plots within each block, which reduces the potential for confounding variables. The conclusion applies to plots similar to those in the experiment.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(13, "COLLECT_DATA", prompt,
          L("A: Identifies the field (soil quality) as the blocking variable.",
            "A: Explains that soil quality is a source of variation in yield that is not the fertilizer, and the plots within a field are alike.",
            "B: Describes randomly assigning the fertilizers to the plots separately within each field (block).",
            "B: States that each fertilizer is assigned to the same number of plots in each field (2 plots for each fertilizer in each field).",
            "C: Explains that replication means more than one experimental unit is assigned to each treatment.",
            "C: States that 8 plots are assigned to each fertilizer (24 / 3).",
            "D: Explains that blocking separates the variation in yield caused by soil from the variation caused by the fertilizers.",
            "D: Explains that this allows a more precise comparison of the fertilizers (the treatments are compared within blocks).",
            "E: Concludes that a cause-and-effect conclusion is justified because of random assignment of the treatments.",
            "E: Notes that the conclusion applies to plots similar to those that were used in the experiment."),
          sample)

    # ----------------------------------------------------------------------------------------------------------- F8
    setup = ("A company has 450 employees. The human resources department wants to know whether the mean number of days per week that employees would like to work from home is greater than 2 days. The department is considering collecting data from every employee or from a sample of the employees.")
    parts = [("A", "Determine a valid investigative question for the study. Ensure that all three components of a valid investigative question are included in your response."),
             ("B", "Collecting data from every employee is a census. Identify one reason why the department might choose a sample instead."),
             ("C", "Describe a method for selecting a simple random sample of 60 employees from the company's list of its 450 employees."),
             ("D", "Describe one source of bias that could occur if the department emails a survey to all of the employees and uses only the responses it receives."),
             ("E", "If the sample is a simple random sample, to what group of people can the department generalize its conclusion? Explain.")]
    ans = [("A", "Is the mean number of days per week that employees of the company would like to work from home greater than 2 days? The department should randomly select employees from the company, so that the conclusion can be made about all of the employees of the company."),
           ("B", "A census can be time-consuming and costly, and it may be difficult to obtain a response from every employee. A sample can answer the question with less effort."),
           ("C", "Number the employees from 1 to 450, use a random number generator to select 60 different numbers from 1 to 450, and use the employees with those numbers."),
           ("D", "Nonresponse (or voluntary response) bias. The employees who respond may have stronger opinions about working from home than the employees who do not, so the mean of the responses could be too large or too small."),
           ("E", "The department can generalize to all 450 employees of the company, because a simple random sample is selected using a random mechanism, so it is representative. It cannot generalize to employees of other companies.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(10, "COLLECT_DATA", prompt,
          L("A: States an investigative question that is about the variable of interest (the number of days per week employees want to work from home).",
            "A: Names the parameter (the mean for the employees) and the direction of the alternative (greater than 2 days).",
            "A: Includes the population to which the conclusion will apply (all employees of the company) in the question or its description.",
            "B: Gives a reason for a sample: a census would take much more time or cost, or it could be difficult to get everyone to respond.",
            "C: Describes numbering the employees (1 to 450) and using a random number generator to select 60 different numbers.",
            "C: Specifies that the employees with the selected numbers are the sample (selected without repeats).",
            "D: Identifies nonresponse bias or voluntary response bias.",
            "D: Explains that the employees who respond may differ from the ones who do not, so the mean could be consistently too large or too small.",
            "E: States that the conclusion can be generalized to all of the employees of the company.",
            "E: Explains that this is because the sample was selected at random from the employees (and does not apply to employees of other companies)."),
          sample)
