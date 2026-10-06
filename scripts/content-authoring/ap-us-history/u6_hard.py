from common import *

B = hard(6)
T_IB, T_LU, T_IU, T_WS, T_PJ = ("industrialization-and-business", "labor-and-unions", "immigration-and-urbanization", "western-settlement-and-native-americans", "politics-populism-and-jim-crow")

# ---- Industrialization and big business ----
B.mcq(T_IB, src("A journalist, 1890", "“A handful of corporations now control the railroads, the oil and the steel of this country, and they use that power to fix prices, hold down wages and even shape the laws that are supposed to govern them.”") + "\n\nWhich of the following best supports the argument made in the passage?",
      ch("Standard Oil used horizontal integration and trusts to buy or drive out competitors and dominate the oil industry.", "The company's consolidation of the oil industry shows how a single firm could control prices and markets."),
      [ch("Thomas Edison invented the electric light bulb.", "An invention does not show control over prices or wages."),
       ch("Farmers formed the Grange to cooperate against railroad rates.", "That shows resistance to corporate power, not the power itself."),
       ch("Congress passed the Pendleton Civil Service Act.", "That law addressed federal hiring and patronage.")],
      "Standard Oil's consolidation illustrates the concentration of corporate power.")

B.mcq(T_IB, "Which of the following was a direct effect of the expansion of railroads on American business practices in the late 1800s?",
      ch("Railroads helped create national markets and led to the adoption of standardized time zones in 1883.", "Railroad schedules required common time standards, and national markets supported large-scale business."),
      [ch("Railroads reduced the need for telegraphs and mail service.", "Railroads and the telegraph often worked together."),
       ch("Railroads encouraged businesses to produce only for local markets.", "Railroads made national markets possible."),
       ch("Railroads weakened the power of large corporations.", "Railroads helped large corporations grow.")],
      "Railroads created national markets and led to standardized time.")

B.mcq(T_IB, "In Munn v. Illinois (1877), the Supreme Court ruled that",
      ch("states could regulate businesses that served the public interest, such as grain elevators and railroads.", "The decision upheld state authority to regulate private businesses affecting the public, which later supported railroad regulation."),
      [ch("the Fourteenth Amendment prevented all state regulation of business.", "The Court upheld regulation in this case."),
       ch("only Congress could regulate railroads.", "The Court upheld a state law."),
       ch("monopolies were protected from all regulation.", "The Court allowed regulation.")],
      "Munn v. Illinois allowed states to regulate businesses affecting the public interest.")

# ---- Labor and unions ----
B.mcq(T_LU, src("A historian, late twentieth century", "“In the great labor disputes of the era, government at every level usually acted to protect property and to suppress strikes rather than to mediate between workers and owners.”") + "\n\nWhich of the following best supports the historian's argument?",
      ch("In 1877, President Hayes sent federal troops to help end a nationwide railroad strike.", "The use of troops against strikers shows the government acting to restore order for employers."),
      [ch("Congress created the Interstate Commerce Commission in 1887.", "That law regulated railroad rates and was not about strikes."),
       ch("The Knights of Labor called for the eight-hour day.", "That shows a labor demand, not government action."),
       ch("Samuel Gompers organized skilled workers into craft unions.", "That shows union organization, not government response.")],
      "Federal troops against the railroad strike support the claim that government sided against strikers.")

B.mcq(T_LU, "Eugene Debs's role in the Pullman Strike and his later turn to socialism most directly illustrates which of the following?",
      ch("Some labor leaders concluded that unions alone could not succeed against a system backed by courts and government, and turned to political alternatives such as socialism.", "The government's use of an injunction and troops convinced Debs that political change was necessary."),
      [ch("A belief that the government was always neutral in labor disputes.", "Debs experienced the government acting against the strikers."),
       ch("A rejection of all labor organization.", "Debs remained committed to organizing workers."),
       ch("Support for the Gospel of Wealth.", "Debs rejected the argument for business leadership.")],
      "Debs's experience led him to look for political solutions.")

B.mcq(T_LU, "Which best explains the decline of the Knights of Labor after 1886?",
      ch("A public backlash after the Haymarket Affair, failed strikes and competition from the more narrowly focused American Federation of Labor.", "Several setbacks combined to cause the Knights to lose members and influence."),
      [ch("A federal law that banned the organization.", "No such law existed."),
       ch("The achievement of all of its goals, making it unnecessary.", "The Knights did not achieve their major goals."),
       ch("A merger with the Populist Party.", "The Knights did not merge with the Populists.")],
      "Haymarket, failed strikes and AFL competition weakened the Knights.")

# ---- Immigration and urbanization ----
B.mcq(T_IU, src("A historian, early twenty-first century", "“Immigrants did not simply abandon their old ways. They built ethnic neighborhoods, newspapers, churches and mutual aid societies that eased their adjustment while preserving their cultures.”") + "\n\nWhich of the following best supports the historian's argument?",
      ch("Neighborhoods such as Little Italy and the Jewish communities of New York's Lower East Side supported foreign-language newspapers and religious institutions.", "Such institutions let immigrants keep their cultures while adapting to the United States."),
      [ch("Congress passed the Chinese Exclusion Act in 1882.", "That law restricted immigration."),
       ch("Political machines traded jobs for votes.", "That shows political incorporation, not cultural preservation."),
       ch("Skyscrapers changed the skylines of American cities.", "That concerns urban architecture.")],
      "Ethnic neighborhoods and institutions show immigrants preserving cultures.")

B.mcq(T_IU, "Advocates of the Social Gospel, such as Walter Rauschenbusch, argued that",
      ch("Christians had a duty to address social problems such as poverty and poor housing by applying religious principles to reform society.", "The Social Gospel connected religion to efforts to improve urban conditions."),
      [ch("religion should stay entirely separate from social problems.", "Social Gospel leaders wanted religious engagement."),
       ch("poverty was a sign of moral failure and not society's concern.", "The Social Gospel rejected that view."),
       ch("the government should have no role in reform.", "Many Social Gospel leaders supported reform, including by government.")],
      "The Social Gospel applied Christian ethics to urban and industrial problems.")

B.mcq(T_IU, "Jacob Riis's photographs and writings in How the Other Half Lives (1890) were significant because they",
      ch("exposed conditions in crowded tenements and helped build support for urban reform.", "Riis brought attention to slum conditions in New York."),
      [ch("defended conditions in the tenements as acceptable.", "Riis criticized those conditions."),
       ch("argued that immigrants should be excluded.", "Riis's work was aimed at reform and not exclusion."),
       ch("promoted the construction of skyscrapers.", "Skyscrapers were not the subject of the book.")],
      "Riis's work exposed urban poverty and encouraged reform.")

# ---- Western settlement and Native Americans ----
B.mcq(T_WS, src("A school superintendent, 1880s", "“The aim is to remove the Indian from the child and save the man. Taken from their villages, the children will learn English, wear our clothes and give up tribal ways, that they may take their place as citizens.”") + "\n\nThe passage best reflects which of the following?",
      ch("Federal assimilation policy that sought to eliminate Native cultures through boarding schools.", "The speaker describes removing children from their communities and teaching them to give up their customs."),
      [ch("Federal support for the preservation of Native languages.", "The passage calls for giving up tribal ways."),
       ch("A treaty guaranteeing Native self-government.", "The passage is about assimilation of children."),
       ch("Native efforts to create their own schools.", "The speaker describes a government policy.")],
      "The passage reflects the boarding school policy of forced assimilation.")

B.mcq(T_WS, "The Wounded Knee massacre of 1890",
      ch("marked the effective end of armed Native resistance on the Great Plains, after United States troops killed many Lakota people.", "The event is often seen as the end of the Indian Wars."),
      [ch("was a Native victory that expelled the army from the Plains.", "Many Lakota were killed by troops."),
       ch("led Congress to return land to the Lakota.", "Land was not returned."),
       ch("occurred during the Civil War.", "It occurred in 1890.")],
      "Wounded Knee marked the end of major armed resistance on the Plains.")

B.mcq(T_WS, "Which factors brought the era of open-range cattle ranching to an end by the late 1880s?",
      ch("Barbed wire, severe winters and overgrazing, and expanding farm settlement.", "Fencing, harsh weather and settlement closed the open range."),
      [ch("A federal ban on cattle drives.", "No such ban was the main cause."),
       ch("The decline in demand for beef.", "Demand for beef remained strong."),
       ch("The end of railroads in the West.", "Railroads expanded in the West.")],
      "Fencing, harsh weather and settlement ended open-range ranching.")

# ---- Politics, Populism and Jim Crow ----
B.mcq(T_PJ, src("A historian, late twentieth century", "“The election of 1896 marked the triumph of the industrial Northeast over the agrarian movements of the South and West and ushered in a long period of Republican dominance.”") + "\n\nWhich of the following best supports the historian's argument?",
      ch("McKinley defeated Bryan, who was backed by the Populists and Democrats, and Republicans held the presidency for most of the next three decades.", "The result and its aftermath fit the claim of lasting Republican dominance."),
      [ch("The Populist Party won several Southern states in 1892.", "That shows Populist strength earlier."),
       ch("Congress passed the Sherman Antitrust Act in 1890.", "That concerns business regulation."),
       ch("The Supreme Court decided Plessy v. Ferguson in 1896.", "That concerns segregation and not the election's political results.")],
      "McKinley's victory and later Republican control support the historian's claim.")

B.mcq(T_PJ, "In the Civil Rights Cases of 1883, the Supreme Court ruled that",
      ch("the Fourteenth Amendment did not prohibit discrimination by private individuals and businesses, striking down the Civil Rights Act of 1875.", "The Court limited federal power to prohibit private discrimination."),
      [ch("the federal government could ban segregation in all public places.", "The Court ruled against that reading."),
       ch("separate but equal facilities were unconstitutional.", "That was not the holding."),
       ch("states could not pass laws that restricted voting.", "The decision concerned private discrimination.")],
      "The decision limited federal power over private discrimination.")

B.mcq(T_PJ, "Ida B. Wells's antilynching campaign in the 1890s",
      ch("documented lynchings and challenged the claim that they punished crime, bringing national and international attention to the violence.", "Wells's investigations exposed the use of lynching to enforce racial control."),
      [ch("led Congress to pass a federal antilynching law in the 1890s.", "No federal antilynching law was passed then."),
       ch("persuaded the Supreme Court to overturn Plessy v. Ferguson.", "Plessy was not overturned until much later."),
       ch("ended lynching throughout the South within a few years.", "Lynching continued for decades.")],
      "Wells documented lynching and challenged its justifications.")

# ---- Short-answer and long-essay ----
saq(B, T_PJ,
    "Use the excerpt to answer parts A, B and C.\n\n" + src("A Black intellectual's essay, 1903", "“The problem of the twentieth century is the problem of the color line. To make a person a servant in the economic world while denying a voice in making the laws is to rob that person of the chance to rise.”") + "\n\n**a)** Identify ONE argument made in the excerpt.\n\n**b)** Explain ONE way in which the approach of Booker T. Washington differed from the view expressed in the excerpt.\n\n**c)** Explain ONE way in which Jim Crow laws in the period 1877 to 1900 limited the political or economic rights of African Americans.",
    [(1, "Part A: Identifies an argument such as that racial discrimination limited opportunity, that political rights are necessary for economic advancement, or that the color line was the major problem of the century"),
     (1, "Part B: Explains that Washington urged vocational education and economic self-improvement and accepted social segregation for the time being, while the author demanded political rights and full equality"),
     (1, "Part C: Explains a limit such as poll taxes, literacy tests and grandfather clauses disfranchising Black voters, segregation laws separating public facilities, or sharecropping and convict leasing restricting economic opportunity")],
    "a) The author argues that denying Black Americans a voice in making laws while limiting them economically robs them of opportunity.\nb) Booker T. Washington urged African Americans to focus on vocational training and economic progress and to accept segregation for the time being, while the author demanded political rights and equality.\nc) Southern states used poll taxes, literacy tests and grandfather clauses to prevent African Americans from voting, which took away their political power.")

leq(B, T_IB,
    "**Long Essay Question**\n\nEvaluate the extent to which industrialization and urbanization changed American society and politics in the period 1865 to 1898.",
    "A strong response states a defensible thesis, for example that industrialization and urbanization transformed the economy, labor and city life and produced new political movements, while older patterns of limited government and racial inequality persisted. It places the topic in the context of the end of the Civil War and the growth of national markets, uses specific evidence (railroads, Carnegie and Rockefeller, labor strikes and unions, immigration, tenements and political machines, the Populists, the Interstate Commerce Act and Sherman Act), and uses continuity and change over time to weigh the extent of transformation.",
    "Thesis: Presents a defensible thesis that responds to the prompt and evaluates the extent to which industrialization and urbanization changed society and politics",
    "Contextualization: Places the topic in a broader context, such as Reconstruction, technological change or the growth of national markets",
    "Evidence: Provides at least two specific, accurate pieces of evidence relevant to the prompt (1 point for addressing the topic with evidence, 2nd point for using specific evidence to support the argument)",
    "Analysis and reasoning: Uses continuity and change over time to structure the argument (1 point), and demonstrates complex understanding, such as showing that economic change outpaced political reform or that change affected groups differently (2nd point)")

B.save()
B.brief()
