"""The course-level pool of document-based and long-essay prompts (content/ap-us-history/frqs/dbq-leq-pool.json).

Documents are original, with generic attributions; none is a quotation from a real source or from any exam."""
import json, os
from common import *

OUT = os.path.join(CONTENT, COURSE, "frqs", "dbq-leq-pool.json")
items = []


def docs(*pairs):
    out = []
    for i, (source, text) in enumerate(pairs, 1):
        out.append(f"**Document {i}**\n\nSource: {source}\n\n> \"{text}\"")
    return "\n\n".join(out)


def add(fid, unit, topic, ftype, prompt, rubric, sample):
    items.append({"id": fid, "unit": UNIT_SLUGS[unit], "topic": topic, "type": ftype, "prompt": prompt,
                  "pointValue": sum(p for p, _ in rubric),
                  "rubric": [{"id": f"r{i + 1}", "points": p, "description": d} for i, (p, d) in enumerate(rubric)],
                  "sampleResponse": sample, "reviewed": False})


DBQ_RUBRIC = lambda thesis, context, docs_line, outside, sourcing, complexity: [
    (1, "Thesis: " + thesis), (1, "Contextualization: " + context), (2, "Evidence from documents: " + docs_line),
    (1, "Evidence beyond documents: " + outside), (1, "Sourcing: " + sourcing), (1, "Complexity: " + complexity)]

DOCS_LINE = "Uses content from at least three documents to address the topic (1 point), and uses content from at least six documents to support an argument (2nd point)"
SOURCING = "Explains how or why the point of view, purpose, historical situation or audience of at least three documents is relevant to an argument"

# ---------------------------------------------------------------- DBQ 1: Britain and the colonies after 1763
add("ap-ush-dbq-1", 3, "imperial-crisis", "DBQ",
    "**Document-Based Question**\n\nEvaluate the extent to which British policies after 1763 changed the relationship between Britain and its North American colonies in the period 1763 to 1775.\n\n" + docs(
        ("A British government order, 1763", "To prevent further conflict with the Indian nations, no settlement shall be made on lands beyond the sources of the rivers that fall into the Atlantic. No governor shall grant land there, and no private person shall purchase land from the Indians."),
        ("A Virginia planter's letter to a London merchant, 1764", "The duties on sugar and molasses, so little noticed before, are now to be rigidly collected, and the courts of admiralty will decide without juries. These are not the old rules of the empire, which let us trade much as we pleased so long as we sent our tobacco home."),
        ("A British official's memorandum to the ministry, 1765", "The colonies have been defended at great cost by British arms and British taxes. It is reasonable that they should bear a share of the expense of their own defense, and Parliament, which governs the whole empire, may lay such a tax."),
        ("Resolutions of a colonial assembly, 1765", "Resolved, that the people of this colony have always enjoyed the right of being governed by laws to which their own representatives have consented, and that any attempt to give the power of taxation to any other body has a tendency to destroy British as well as American freedom."),
        ("An agreement signed by Boston merchants, 1768", "We, the undersigned merchants, will not import any goods from Great Britain, except a few necessary articles, until the duties on paper, glass, lead and tea are repealed. We will encourage the making of homespun cloth and avoid every luxury."),
        ("A British customs official's report, 1770", "Smuggling is so common in this port that honest officers cannot do their duty, and crowds threaten any person who informs against a smuggler. Without troops to support the law, the customs service in Boston is impossible."),
        ("A colonial Loyalist writer, 1774", "The people complain of tyranny, yet no people in the world are so lightly taxed. They have enjoyed protection for their frontiers and a market for their goods. To resist the lawful authority of Parliament is to choose anarchy."),
    ),
    DBQ_RUBRIC("Presents a historically defensible thesis that responds to the prompt and establishes a line of reasoning about the extent to which British policies changed the relationship",
               "Describes a broader historical context relevant to the prompt, such as the French and Indian War and its costs, or the era of salutary neglect",
               DOCS_LINE,
               "Uses at least one additional piece of specific historical evidence not found in the documents, such as the Stamp Act Congress, the Boston Massacre or the Coercive Acts",
               SOURCING,
               "Demonstrates a complex understanding, for example by showing that British officials saw their measures as continuity with an imperial tradition while colonists saw them as a break, or by weighing divisions among colonists such as Loyalist opposition"),
    "British policies after 1763 changed the relationship between Britain and the colonies profoundly, because they replaced a long period of loose supervision with an assertion of Parliament's authority to tax and regulate, though British officials themselves believed they were only asking the colonies to bear a fair share of imperial costs.\n\nAfter the French and Indian War left Britain with a large debt and a larger empire to defend, the earlier pattern of salutary neglect gave way to new measures (Contextualization). Document 1, a British order, limited settlement west of the Appalachians to avoid conflict with Native peoples, which shows the government taking direct control of colonial expansion. Document 2, written by a Virginia planter to a London merchant, complains that the rules of the empire have changed, which reflects the experience of an export-oriented elite accustomed to loose enforcement. Document 3, from a British official writing to the ministry, argues that colonists should pay for their own defense, which shows that policy makers saw continuity of imperial authority rather than a break. Documents 4 and 5 show colonial responses: an assembly resolution that taxation requires consent, and a merchants' boycott agreement, which used economic pressure; the latter was written by merchants who had a commercial interest in repeal. Document 6, a customs official's report, shows enforcement problems and was written to justify the use of troops. Document 7, from a Loyalist, argues that the colonists were lightly taxed and protected, which reflects a viewpoint of colonists who feared anarchy.\n\nBeyond the documents, the Stamp Act Congress of 1765, the Boston Massacre of 1770 and the Coercive Acts of 1774 show how disputes over taxation and authority escalated. However, the change was not universal: many colonists, such as the Loyalist writer in Document 7, still valued the imperial connection, and British officials believed they were maintaining, not altering, the empire. Thus British policy changed the relationship fundamentally in the eyes of many colonists while the British saw it as a continuation of existing rights.")

# ---------------------------------------------------------------- DBQ 2: Reconstruction and freedpeople
add("ap-ush-dbq-2", 5, "reconstruction-plans-and-amendments", "DBQ",
    "**Document-Based Question**\n\nEvaluate the extent to which Reconstruction changed the lives of formerly enslaved people in the South in the period 1865 to 1877.\n\n" + docs(
        ("A Freedmen's Bureau agent's report, 1866", "The schools for freedpeople are crowded. Men who have labored all day come at night to learn their letters, and parents sit beside their children. Many planters complain that the people no longer know their place, and in several counties my authority reaches no farther than the county seat."),
        ("A state law, 1865", "Persons of color who have no lawful employment shall be deemed vagrants and may be hired out to any citizen who will pay their fines. No person of color shall rent or own farm land outside the limits of an incorporated town."),
        ("A sharecropping contract, 1868", "The laborer shall work the land assigned to him and give the landlord one-half of the crop. The landlord shall furnish tools, seed and rations, the cost of which shall be taken from the laborer's share at the end of the season. The laborer shall not leave the plantation without the landlord's written permission."),
        ("A Black state legislator's speech, 1869", "We do not ask for revenge, only for the rights of citizens. We have the vote, and we are using it to build schools and roads and to open public institutions to all people. Those who say that we are unfit to govern should look at what we have already built."),
        ("A freedman's testimony to a congressional committee, 1871", "Masked men came to my cabin at night and said I had voted the wrong way and they would teach me a lesson. They beat me and burned the schoolhouse. When I went to the sheriff, he said there was nothing he could do."),
        ("A Northern newspaper editorial, 1876", "The nation has spent ten years and a great deal of treasure on the South. The freedmen must now stand on their own feet, and the Southern states must be left to manage their own affairs."),
        ("A Supreme Court opinion, 1876", "The Fourteenth Amendment protects citizens against action by the state, but it gives Congress no power to punish private individuals who violate the rights of others. Such wrongs must be remedied by the states."),
    ),
    DBQ_RUBRIC("Presents a historically defensible thesis that responds to the prompt and establishes a line of reasoning about the extent to which Reconstruction changed freedpeople's lives",
               "Describes a broader historical context, such as the end of the Civil War, emancipation and the Thirteenth Amendment, or the political conflict between Congress and President Johnson",
               DOCS_LINE,
               "Uses at least one additional piece of specific evidence not found in the documents, such as the Fourteenth and Fifteenth Amendments, the Civil Rights Act of 1866 or the Compromise of 1877",
               SOURCING,
               "Demonstrates a complex understanding, for example by showing that change varied over time (rapid gains followed by retreat after 1870) or by weighing legal change against economic dependence"),
    "Reconstruction changed the lives of formerly enslaved people significantly in education, family life and political participation, but its gains were limited and later undermined by economic dependence, violence and the withdrawal of federal support.\n\nEmancipation and the Thirteenth Amendment ended slavery, and Congress then sought to define freedpeople's place in the nation (Contextualization). Document 1, a Freedmen's Bureau agent's report, shows eager attendance at schools and also the limits of federal authority, which is relevant because the agent had firsthand knowledge but also an interest in showing the Bureau's work. Document 4, a Black legislator's speech, shows political participation and the use of the vote to build schools and public institutions, though the speaker was addressing an audience skeptical of Black officeholders. Together with the Fourteenth and Fifteenth Amendments, which granted citizenship and the right to vote, these documents show real change.\n\nHowever, other documents show limits. Document 2, a state law, reflects the intent of white legislators to restrict freedpeople's labor and land ownership. Document 3, a sharecropping contract, shows that many freedpeople stayed economically dependent on landowners, with debt and restrictions on movement. Document 5, a freedman's testimony, shows that violence by groups like the Ku Klux Klan and the failure of local officials limited political rights. Documents 6 and 7 show a retreat of federal commitment: Northern fatigue in a newspaper editorial and a Supreme Court opinion restricting federal power, which reflects the Court's narrowing of the Fourteenth Amendment in decisions such as United States v. Cruikshank.\n\nThus Reconstruction produced real, if uneven, change: the legal and political foundations of equality were established, but violence, sharecropping and the Compromise of 1877 limited their practical effect, making Reconstruction an unfinished revolution.")

# ---------------------------------------------------------------- DBQ 3: industrialization and workers
add("ap-ush-dbq-3", 6, "labor-and-unions", "DBQ",
    "**Document-Based Question**\n\nEvaluate the extent to which industrialization improved the lives of American workers in the period 1870 to 1900.\n\n" + docs(
        ("An industrialist's essay, 1889", "The cheapening of goods, which now gives the laborer comforts that a king could not buy a century ago, is the result of production on a great scale. The law of competition may be hard on the individual, but it is best for the race."),
        ("A state factory inspector's report, 1884", "In the mills I found children of ten working twelve hours a day among unguarded machinery. The wages of a family of five are hardly enough for rent, fuel and food, and the children's earnings are counted on to make up the difference."),
        ("A machinist's letter to a union newspaper, 1890", "My wages have risen by a quarter in ten years, but the foreman can discharge me without cause, and when the shop is slack I am put on half time. I own nothing but my tools, and a man of forty is thought too old to be hired."),
        ("A circular of a labor organization, 1880s", "We declare that the wealth created by labor belongs to those who create it. We demand the eight-hour day, the abolition of child labor and the end of the use of convict labor against honest workers."),
        ("An immigrant's letter to relatives, 1895", "I came here with two dollars. Now I earn more in a week than my father earned in a month at home, and my children go to school. The tenement is crowded and I work from dawn to dusk, but I do not regret coming."),
        ("A newspaper editorial on a railway strike, 1894", "The government has a duty to keep the mails moving. When a union paralyzes the nation's railways, the law must be enforced even if soldiers are required."),
        ("A reformer's report on tenement districts, 1890", "Families of seven live in two rooms, and the air shafts carry smells but not light. The rent consumes a third of a laborer's wages, and the landlord lives in a distant part of the city."),
    ),
    DBQ_RUBRIC("Presents a historically defensible thesis that responds to the prompt and establishes a line of reasoning about the extent to which industrialization improved workers' lives",
               "Describes a broader historical context, such as the growth of railroads and national markets, Reconstruction's end or large-scale immigration",
               DOCS_LINE,
               "Uses at least one additional piece of specific evidence not found in the documents, such as the Haymarket Affair, the Homestead Strike, the Sherman Antitrust Act or the Great Railroad Strike of 1877",
               SOURCING,
               "Demonstrates a complex understanding, for example by showing that experiences differed among skilled and unskilled workers, native-born and immigrant workers, or by weighing material gains against insecurity and loss of control"),
    "Industrialization improved the material lives of many American workers by lowering prices and offering higher wages than many had known, but it also brought insecurity, dangerous conditions and a loss of control, so its benefits were real but uneven and often came with serious costs.\n\nThe expansion of railroads, steel and national markets after the Civil War created huge industries and drew workers from farms and abroad (Contextualization). Document 1, from an industrialist, argues that mass production benefits workers by cheapening goods, a perspective that reflects the writer's interest in defending large-scale business. Document 5, an immigrant's letter, shows that some workers earned more than they could at home and saw opportunities for their children, which was written to relatives and may emphasize success. Document 3, a machinist's letter, shows wage gains but also insecurity from arbitrary dismissal and short time, a view of a skilled worker writing for a union audience.\n\nOther documents show the costs. Document 2, a factory inspector's report, describes child labor and low family incomes, written to document abuses and support reform. Document 7, a reformer's report, shows crowded housing that took a large share of wages, again from a reform perspective. Document 4, a labor organization's circular, demands the eight-hour day and the end of child labor, which shows workers organizing to protect themselves. Document 6, a newspaper editorial, shows that business-friendly voices supported using force to end strikes, as occurred in the Pullman Strike.\n\nBeyond the documents, the Haymarket Affair and the Homestead Strike illustrate how conflict between workers and owners often ended in defeat for unions. Overall, industrialization raised living standards for some, especially skilled workers and some immigrants, while exposing many others to unsafe work, poverty and vulnerability, so its effects were mixed rather than uniformly beneficial.")

# ---------------------------------------------------------------- DBQ 4: the home front in World War II
add("ap-ush-dbq-4", 7, "world-war-two", "DBQ",
    "**Document-Based Question**\n\nEvaluate the extent to which World War II changed the lives of Americans on the home front in the period 1941 to 1945.\n\n" + docs(
        ("A government recruiting poster, 1943", "Women: the war needs you in the factory. Take a job and free a man to fight. Every hour at the bench helps bring him home sooner."),
        ("A woman war worker's letter to her sister, 1943", "I earn more at the riveting bench than I ever did as a clerk, and for the first time I am sending money home. But everyone says that when the men return my job will go back to them, and I do not know where I will be then."),
        ("A statement by a Black union leader, 1941", "We call upon the president to forbid discrimination in the factories that make the weapons of war. A nation that fights for freedom abroad cannot deny its own citizens a fair chance to work for it at home."),
        ("A Japanese American's account, 1942", "We were given one week to sell our farm and our belongings. The camp was a barracks surrounded by a wire fence. In spite of this, our sons volunteered from the camp to prove their loyalty."),
        ("A government rationing notice, 1942", "Sugar, coffee, gasoline and meat will be rationed. Each family will receive ration books. Hoarding is unpatriotic, and every citizen must share the burden equally."),
        ("A labor union newsletter, 1943", "The no-strike pledge keeps production flowing, but prices are rising and wages are frozen. Many members say that the fight against fascism cannot mean the end of any gains for working people."),
        ("A Detroit manufacturer's memorandum, 1942", "We have converted our assembly lines to tanks and planes, and we need more workers than the city can house. Migration from the South has doubled our labor force and strained housing and schools, and tensions among the new arrivals have grown."),
    ),
    DBQ_RUBRIC("Presents a historically defensible thesis that responds to the prompt and establishes a line of reasoning about the extent to which the war changed life on the home front",
               "Describes a broader historical context, such as the end of the Great Depression, the attack on Pearl Harbor or the mobilization of the economy for war",
               DOCS_LINE,
               "Uses at least one additional piece of specific evidence not found in the documents, such as Executive Order 8802, Executive Order 9066 and Korematsu v. United States, the Detroit riot of 1943 or the GI Bill",
               SOURCING,
               "Demonstrates a complex understanding, for example by showing that change differed by group (women, Black Americans, Japanese Americans) or by weighing wartime gains against postwar expectations that they would be reversed"),
    "World War II changed life on the American home front dramatically through mobilization, rationing, new jobs and population movement, but many changes were temporary or uneven, and the war exposed as well as altered inequalities.\n\nThe war ended the Great Depression by creating huge demand for workers and goods and brought Americans into a war economy after Pearl Harbor (Contextualization). Document 1, a government poster, urged women to work in factories, and Document 2, a woman war worker's letter, shows both the new opportunities and higher earnings and the expectation that she would give up her job when the men returned, a view written privately to a sister. Document 5 shows rationing, which imposed shared sacrifice on families and was written by the government to encourage cooperation. Document 7, written by a manufacturer, shows how war production drew migrants and strained housing, a perspective focused on the business's labor needs.\n\nThe documents also show inequality and conflict. Document 3, a Black union leader's statement, demanded fair access to defense jobs, which led to Executive Order 8802. Document 4, a Japanese American's account, shows that the government forced a group of citizens into camps, and that families still sought to prove their loyalty, which beyond the documents is shown by Executive Order 9066 and Korematsu v. United States. Document 6, from a union newsletter, shows tension between the no-strike pledge and workers' desire to protect their gains.\n\nThus the war transformed economic opportunity and daily life for many Americans, especially women and Black workers who found new jobs, while also deepening injustices such as internment and discrimination. Many changes were limited, with tensions such as the Detroit riot of 1943 and the assumption that women would return to domestic roles.")

# ---------------------------------------------------------------- LEQs
LEQ_RUBRIC = lambda t, c, e, a: [(1, "Thesis: " + t), (1, c), (2, e), (2, a)]
EVID = "Evidence: Provides at least two specific, accurate pieces of evidence relevant to the prompt (1 point for addressing the topic with evidence, 2nd point for using specific evidence to support the argument)"

add("ap-ush-leq-1", 2, "english-colonies-founding", "LEQ",
    "**Long Essay Question**\n\nCompare the development of the New England colonies and the Chesapeake colonies in the period 1607 to 1700.",
    LEQ_RUBRIC("Presents a defensible thesis that responds to the prompt with a claim about similarities and differences",
               "Contextualization: Places the topic in a broader context, such as English religious conflict, the growth of the Atlantic economy or competition with other European powers",
               EVID,
               "Analysis and reasoning: Uses comparison to structure the argument (1 point), and demonstrates complex understanding, such as explaining reasons for differences or noting that both regions came to rely on coerced labor (2nd point)"),
    "A strong response states a thesis such as that New England developed as a family-centered, religiously motivated society of towns with a diversified economy, while the Chesapeake developed as a commercial, tobacco-based society with dispersed plantations and a reliance on servants and later enslaved labor, although both regions shared English law and became tied to the Atlantic economy. It places the colonies in the context of English religious conflict and economic opportunity, uses evidence (the Puritans' covenant communities and town governance, the Chesapeake's tobacco economy, headrights and indentured servitude, Bacon's Rebellion and the shift to slavery), and uses comparison and explanations for differences.")

add("ap-ush-leq-2", 4, "market-revolution", "LEQ",
    "**Long Essay Question**\n\nEvaluate the extent to which the market revolution contributed to differences among the Northeast, the West and the South in the period 1800 to 1850.",
    LEQ_RUBRIC("Presents a defensible thesis that responds to the prompt and evaluates the extent to which the market revolution contributed to regional differences",
               "Contextualization: Places the topic in a broader context, such as the end of the War of 1812, nationalism or advances in transportation and technology",
               EVID,
               "Analysis and reasoning: Uses causation to structure the argument (1 point), and demonstrates complex understanding, such as showing that the market revolution also tied the regions together through trade and credit (2nd point)"),
    "A strong response states a thesis such as that the market revolution deepened regional differences by encouraging factory production and commerce in the Northeast, commercial farming in the West and cotton plantation slavery in the South, while also linking the regions through trade, transportation and credit. It uses evidence (the Erie Canal and railroads, the Lowell mills, the cotton gin and the expansion of slavery, the domestic slave trade, western grain and livestock), and uses causation to explain how economic change shaped social and political divisions.")

add("ap-ush-leq-3", 5, "manifest-destiny", "LEQ",
    "**Long Essay Question**\n\nEvaluate the extent to which westward expansion intensified sectional conflict in the period 1844 to 1860.",
    LEQ_RUBRIC("Presents a defensible thesis that responds to the prompt and evaluates the extent to which expansion intensified sectional conflict",
               "Contextualization: Places the topic in a broader context, such as Manifest Destiny, the growth of the cotton economy or earlier compromises over slavery such as the Missouri Compromise",
               EVID,
               "Analysis and reasoning: Uses causation to structure the argument (1 point), and demonstrates complex understanding, such as weighing expansion against other causes of conflict like the Fugitive Slave Act and the growth of antislavery politics (2nd point)"),
    "A strong response states a thesis such as that expansion was the central cause of sectional conflict because each acquisition raised the question of whether slavery would spread, while other factors, such as the Fugitive Slave Act, Uncle Tom's Cabin and the rise of the Republican Party, also deepened divisions. It uses evidence (the annexation of Texas, the Mexican-American War and the Wilmot Proviso, the Compromise of 1850, the Kansas-Nebraska Act and Bleeding Kansas, Dred Scott), and uses causation to analyze how expansion and slavery connected.")

add("ap-ush-leq-4", 8, "cold-war-foreign-policy", "LEQ",
    "**Long Essay Question**\n\nEvaluate the extent to which the policy of containment shaped United States foreign policy in the period 1947 to 1975.",
    LEQ_RUBRIC("Presents a defensible thesis that responds to the prompt and evaluates the extent to which containment shaped foreign policy",
               "Contextualization: Places the topic in a broader context, such as the end of World War II, the Soviet takeover of Eastern Europe or the nuclear arms race",
               EVID,
               "Analysis and reasoning: Uses continuity and change over time to structure the argument (1 point), and demonstrates complex understanding, such as showing how containment led to successes in Europe and costly failures in Vietnam, or how détente modified it (2nd point)"),
    "A strong response states a thesis such as that containment guided American foreign policy throughout the period, shaping aid to Europe, alliances, interventions in Korea and Vietnam, and the nuclear strategy, while later policies such as détente adjusted it in response to costs and changing conditions. It uses evidence (the Truman Doctrine and Marshall Plan, NATO, the Korean War, the domino theory and Vietnam, the Cuban Missile Crisis, Nixon's opening to China and arms control), and uses continuity and change to weigh how far containment drove policy.")

with open(OUT, "w") as fh:
    json.dump(items, fh, indent=2, ensure_ascii=False)
    fh.write("\n")
print(f"wrote {len(items)} prompts to {OUT}")
