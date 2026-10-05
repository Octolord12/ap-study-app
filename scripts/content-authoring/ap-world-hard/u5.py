from common import *

B = bank(5, "unit-5-revolutions")
T_ENL, T_ATL, T_IND, T_REA, T_EFF = ("enlightenment-thought", "atlantic-revolutions", "industrial-revolution-begins", "reactions-to-industrialization", "effects-of-industrialization")

B.mcq(T_ENL, src("A French political treatise, 1748", "“In every state there are three kinds of power: the power to make laws, the power to carry them out, and the power to judge. When the power to make the laws and the power to carry them out are joined in one person or one body, there can be no liberty.”") + "\n\nThe idea expressed in the passage most directly influenced which later development?",
      ch("The division of government into separate legislative, executive and judicial branches in the United States Constitution.", "The principle of the separation of powers, associated with Montesquieu, was a model for constitutional design in the revolutionary era."),
      [ch("The belief that monarchs rule by divine right and need no checks.", "The passage argues for limits on concentrated power, the opposite of divine-right absolutism."),
       ch("The call for workers to seize the means of production.", "This is a nineteenth-century socialist idea unrelated to the passage."),
       ch("The principle that a strong sovereign must have all power to prevent disorder.", "This is closer to Hobbes; the passage warns against uniting powers.")],
      "The passage describes the separation of powers, which shaped later constitutions.")

B.mcq(T_ENL, "Which statement best contrasts the political ideas of Thomas Hobbes and John Locke?",
      ch("Hobbes argued that people needed a powerful sovereign to prevent chaos, while Locke argued that government exists to protect natural rights and may be replaced if it fails to do so.", "Hobbes supported strong authority and Locke supported government by consent, with a right of revolution against abuse."),
      [ch("Hobbes argued that governments could be overthrown at will, while Locke supported absolute monarchy.", "This reverses their positions."),
       ch("Both argued that kings rule by divine right.", "Neither defended the divine right of kings in the way traditional monarchists did, and Locke explicitly rejected it."),
       ch("Both argued that government should be abolished because people are naturally good.", "Neither argued for abolishing government.")],
      "Hobbes favored strong authority; Locke favored consent and natural rights.")

B.mcq(T_ENL, "Mary Wollstonecraft's argument that the apparent inferiority of women resulted from their lack of education is best understood as which of the following?",
      ch("An application of Enlightenment ideas about reason and natural rights to women.", "Wollstonecraft used Enlightenment principles to argue that women should be educated and share rights."),
      [ch("A rejection of all Enlightenment ideas in favor of traditional authority.", "She used Enlightenment reasoning to challenge traditional views."),
       ch("A defense of absolute monarchy.", "Her argument was about education and rights, not defending absolutism."),
       ch("A conservative reaction to the French Revolution.", "She supported the rights ideals of the revolutionary era.")],
      "Wollstonecraft extended Enlightenment reasoning to the question of women's rights.")

B.mcq(T_ATL, src("Proclamation attributed to a leader of the enslaved rebels in Saint-Domingue, 1791-1793", "“We who have been treated as beasts of burden know as well as any Frenchman what liberty and equality mean, for we have paid dearly to learn what their absence is. We claim our rights as men, and will not lay down our arms until slavery is ended.”") + "\n\nWhich statement best explains how the revolution described in the passage differed from the American Revolution?",
      ch("It was led by enslaved people, attacked slavery itself, and created a state in which slavery was abolished.", "The Haitian Revolution was the only successful slave revolt to produce an independent state, and it abolished slavery, whereas the United States preserved slavery after independence."),
      [ch("It was led by wealthy planters who wanted to keep slavery.", "The passage describes enslaved people fighting to end slavery."),
       ch("It was unaffected by Enlightenment ideas of liberty and equality.", "The passage uses the language of liberty and equality that the rebels drew from the French revolutionary era."),
       ch("It ended with the colony's return to Spanish rule.", "Saint-Domingue was a French colony and became independent Haiti in 1804.")],
      "The Haitian Revolution was a revolt of the enslaved that ended slavery and colonial rule.")

B.mcq(T_ATL, "Which group led the independence movements in Spanish America in the early nineteenth century, and what was one of their main grievances?",
      ch("Creole elites, who resented the dominance of Spanish-born officials in high offices and the trade restrictions imposed by Spain.", "Creoles, born in the Americas of European descent, were excluded from top positions and wanted political and economic control, influenced by Enlightenment ideas and by events in Spain."),
      [ch("Enslaved Africans, who wanted to restore African kingdoms.", "Enslaved people took part in some campaigns but did not lead the independence movements overall."),
       ch("Spanish-born officials, who wanted to abolish Spanish rule.", "Spanish-born officials generally supported the colonial system."),
       ch("The Catholic Church, which wanted to separate from Rome.", "The Church was not the leading force of independence movements and did not seek to separate from Rome.")],
      "Creole elites led the independence movements, seeking political and economic power.")

B.mcq(T_ATL, "Which statement best describes a long-term effect of the French Revolution and the Napoleonic era on Europe?",
      ch("Ideas such as nationalism, legal equality and constitutional government spread widely, even though conservative rulers tried to restore the old order after 1815.", "The revolution and Napoleon's conquests spread new political ideas, and the Congress of Vienna tried to restore monarchies but could not erase those ideas."),
      [ch("Monarchy was permanently abolished throughout Europe.", "Monarchies remained in most European states for generations."),
       ch("The Catholic Church became the sole legal authority in France.", "The revolution had reduced the Church's power."),
       ch("A European union with a common government was created in 1800.", "No such union existed at that time.")],
      "New ideas spread despite conservative efforts to restore the old order.")

B.mcq(T_IND, "Which combination of factors best explains why the Industrial Revolution began in Great Britain?",
      ch("Abundant coal and iron ore, capital from overseas trade and colonies, agricultural improvements that freed labor for other work, and a stable government that supported commerce.", "These conditions together encouraged innovation in textiles, mining and metallurgy."),
      [ch("A lack of coal and iron, which forced Britain to turn to machines.", "Britain had large coal and iron resources."),
       ch("Strong guild restrictions that required all production to remain in small workshops.", "Guild restrictions were weaker in Britain than elsewhere, and the factory system developed."),
       ch("The absence of overseas markets and colonies.", "Britain's colonies and trade provided capital, raw materials and markets.")],
      "Resources, capital, labor and a supportive state explain Britain's lead.")

B.mcq(T_IND, src("Report of a government factory inspector, Britain, 1830s", "“In the mills I found children of nine and ten years working twelve hours a day among dangerous machinery. Many were deformed and sickly, and none had received any schooling.”") + "\n\nThe conditions described in the passage most directly contributed to which development?",
      ch("Reform movements and laws that limited child labor and regulated working conditions in factories.", "Reports like this one helped bring about factory acts that restricted child labor and set standards in the nineteenth century."),
      [ch("The abolition of the factory system and a return to guild production.", "The factory system continued to expand."),
       ch("A government order that required all children to work in mills.", "Reforms limited, rather than required, child labor."),
       ch("An end to industrialization in Britain.", "Industrialization continued.")],
      "Investigations of factory conditions spurred reform laws.")

B.mcq(T_REA, src("A European pamphlet, 1848", "“In every age the many who labor have been ruled by the few who own. The workers of the factories have nothing to lose but their chains, and the day will come when they take the means of production into their own hands.”") + "\n\nThe pamphlet reflects which response to industrialization?",
      ch("Socialist ideas that criticized capitalism and predicted a workers' revolution.", "Marx and Engels and other socialists argued that industrial workers would overthrow the owners of capital."),
      [ch("A defense of laissez-faire capitalism as set out by Adam Smith.", "The passage criticizes owners and calls for workers to take over production."),
       ch("A call to return to feudal obligations and rule by nobles.", "The passage looks toward workers' control, not feudal rule."),
       ch("A statement of support for absolute monarchy.", "The passage concerns class conflict.")],
      "The pamphlet expresses socialist criticism of industrial capitalism.")

B.mcq(T_REA, "Which statement best describes laissez-faire capitalism, as advocated by economists such as Adam Smith?",
      ch("Economic growth is best promoted by free markets with little government interference.", "Laissez-faire economists argued that competition and markets guide economic activity better than government control."),
      [ch("The government should own all factories and farms.", "This describes socialism or communism."),
       ch("The government should set all prices and wages.", "Laissez-faire opposes such control."),
       ch("Overseas colonies should be closed to trade with all other nations.", "This is a mercantilist idea that Smith criticized.")],
      "Laissez-faire favors free markets and limited government.")

B.mcq(T_EFF, "Which was a social effect of industrialization in nineteenth-century Britain?",
      ch("Rapid urbanization, as workers moved to crowded industrial cities, and the growth of a larger middle class and an industrial working class.", "Factory jobs drew people from the countryside and created new social classes."),
      [ch("A decline in the size of cities as people returned to farming.", "Cities grew rapidly."),
       ch("The disappearance of class distinctions.", "Industrialization produced new class divisions."),
       ch("The return of feudal lords to political power.", "Industrialization weakened old landed power and created new classes.")],
      "Industrialization led to urban growth and new social classes.")

B.mcq(T_REA, src("Memorial of a Japanese official, 1870s", "“We must send students abroad to learn the arts of the West, build railways and factories, and raise a modern army, so that our country may stand equal to the great powers and not be reduced like the lands of China to the will of foreigners.”") + "\n\nThe approach described in the passage is best explained as which of the following?",
      ch("State-led industrialization and modernization intended to prevent domination by Western powers.", "The Meiji government used borrowed Western technology and institutions to strengthen Japan, as the passage proposes."),
      [ch("A rejection of all Western technology and ideas in favor of isolation.", "The passage urges learning from the West."),
       ch("A continuation of the Tokugawa policy of closing the country to outsiders.", "The Tokugawa policy of isolation was ended and replaced by active modernization."),
       ch("A proposal to colonize Europe.", "The passage concerns strengthening Japan, not colonizing Europe.")],
      "The passage reflects the state-sponsored modernization of Meiji Japan.")

B.mcq(T_EFF, "Which of the following contributed to the abolition of the Atlantic slave trade by Britain and other states in the early nineteenth century?",
      ch("Enlightenment ideas, humanitarian campaigns, resistance by the enslaved (including the Haitian Revolution), and changing economic interests.", "Many factors, including moral campaigns and enslaved people's own resistance, led Britain to abolish the trade in 1807 and slavery itself in its empire in 1833."),
      [ch("A single worldwide agreement that all slave-holding states signed in 1750.", "Abolition occurred gradually, in different countries, over many decades."),
       ch("A sudden collapse in European demand for sugar.", "Demand for sugar remained strong."),
       ch("Orders from African kings forbidding any sales of captives.", "African states did not control the end of the trade.")],
      "Abolition came about through several interacting factors.")

B.mcq(T_REA, "The reforms of Muhammad Ali in Egypt and the Tanzimat reforms in the Ottoman Empire in the early and mid-nineteenth century were similar in that both",
      ch("attempted to strengthen the state by adopting Western-style military, administrative and economic reforms in response to European power.", "Both sets of reformers tried to modernize armies and administration so their states could resist European pressure."),
      [ch("rejected all European technology and ideas.", "Both reformers borrowed European models."),
       ch("were led by Christian missionaries.", "The reforms were led by Muslim rulers and officials."),
       ch("ended Muslim rule in their regions.", "Muslim rule continued.")],
      "Both reform programs imitated Western methods to strengthen the state.")

B.mcq(T_ATL, src("Declaration of a revolutionary assembly, 1789", "“Sovereignty resides in the nation. All citizens are equal before the law and are equally eligible for public office, according to their abilities.”") + "\n\nWhich statement best describes a limitation of these principles in practice during the French Revolution?",
      ch("Women and enslaved people in the French colonies were largely excluded from the rights the declaration proclaimed.", "Although it proclaimed universal rights, women did not gain political equality, and slavery continued in the colonies until its abolition in 1794 (later reversed by Napoleon)."),
      [ch("The principles applied only to members of the nobility.", "The declaration was meant to apply to all citizens, and it challenged noble privilege."),
       ch("The principles were never written into any law.", "Many of the principles were incorporated into laws and constitutions."),
       ch("The principles protected the Church's property from any taxation.", "The revolution took Church lands and reduced its privileges.")],
      "The universal language of rights was applied unevenly.")

saq(B, T_IND,
    "Use the passage to answer parts A, B and C.\n\n" + src("Report of a government factory inspector, Britain, 1830s", "“In the mills I found children of nine and ten years working twelve hours a day among dangerous machinery. Many were deformed and sickly, and none had received any schooling.”") + "\n\n**a)** Identify ONE working condition described in the passage.\n\n**b)** Explain ONE way reformers or governments responded to conditions like those described.\n\n**c)** Explain ONE way that industrialization affected a society outside Europe in the nineteenth century.",
    [(1, "Part A: Identifies a condition such as long hours, child labor, dangerous machinery or lack of schooling"),
     (1, "Part B: Explains a response such as factory acts limiting child labor and hours, the growth of labor unions, or reformers' campaigns for education and safety"),
     (1, "Part C: Explains an effect outside Europe, such as Japan's state-led industrialization, Egypt's reforms under Muhammad Ali, India's textile industry being undermined by British manufactured goods, or the growth of plantation or mining economies serving industrial demand")],
    "a) The passage describes children as young as nine working twelve-hour days among dangerous machinery.\nb) Reformers and the British government responded with factory acts that limited the hours and ages of child workers and set up inspections, and workers also organized unions to seek better conditions.\nc) In India, cheap factory-made British textiles undermined traditional handloom weavers, while the colony supplied raw cotton to British mills, so industrialization in Britain reshaped India's economy.")

leq(B, T_REA,
    "**Long Essay Question**\n\nCompare the responses to industrialization in TWO of the following societies in the period 1750-1900: Great Britain, Japan, Egypt, the Ottoman Empire.",
    "A strong response states a thesis about similarities and differences (for example that Japan and Egypt both used state-led modernization, but Japan's was more sustained and successful, while in Britain private enterprise led the way and workers' movements and reformers shaped the response). It places the topic in the context of the spread of industrial technology and growing European power, and uses specific evidence (the Meiji Restoration, Muhammad Ali's army and factories, the factory acts, trade unions and socialist ideas, the Tanzimat reforms) and explains the reasons for similarities and differences.",
    "Thesis: Presents a defensible thesis that makes a comparative claim about the two societies' responses to industrialization",
    "Contextualization: Describes broader context, such as the spread of industrial technology and the growth of European economic and military power",
    "Evidence: Provides at least two specific, accurate examples for each society (1 point for addressing the topic, 2nd point for using specific evidence to support the comparison)",
    "Analysis and reasoning: Uses comparison to structure the argument (1 point), and demonstrates complexity by explaining reasons for the similarities and differences or by qualifying the argument (2nd point)")

B.save()
B.brief()
