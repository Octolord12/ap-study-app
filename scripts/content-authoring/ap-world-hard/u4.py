from common import *

B = bank(4, "unit-4-transoceanic-interconnections")
T_TECH, T_CE, T_MAR, T_LAB = ("technology-and-exploration", "columbian-exchange", "maritime-empires", "labor-systems-and-slave-trade")

B.mcq(T_TECH, src("Account by a Portuguese court chronicler, fifteenth century", "“The prince sent his ships south along the coast to learn what lands lay beyond, to find the sources of gold, to carry the faith to those who had not heard it, and to trade directly with the peoples of the south and east, without paying tribute to the Muslim merchants who stand between us and those markets.”") + "\n\nWhich statement best explains the motivations described in the passage?",
      ch("Portuguese rulers sought direct access to African and Asian trade and wealth, and wanted to spread Christianity, by bypassing Muslim and Italian intermediaries.", "Portugal's voyages combined economic motives, such as gold and the spice trade, with religious aims and rivalry with the merchants who controlled existing routes."),
      [ch("They hoped to establish colonies in Australia to relieve overpopulation.", "The passage concerns Africa and Asian trade; European contact with Australia came much later."),
       ch("They were responding to a ban on foreign ships issued by the Mongol Empire.", "The passage does not mention a Mongol ban, and the motivations described are commercial and religious."),
       ch("They intended purely to gather scientific information without any commercial purpose.", "The passage explicitly mentions gold and trade as goals.")],
      "The passage shows both economic and religious motives for the voyages.")

B.mcq(T_TECH, "Which combination best explains how European sailors in the fifteenth century were able to make long voyages across the Atlantic and around Africa?",
      ch("The caravel, which combined square and lateen sails, together with navigational tools such as the compass and astrolabe that came to Europe from Asia and the Islamic world.", "Europeans adopted and improved ship designs and instruments from earlier traditions, enabling them to sail against the wind and to find their position at sea."),
      [ch("Steam engines and iron-hulled ships.", "Steamships developed in the nineteenth century."),
       ch("Treasure ships purchased from Ming China.", "The Portuguese and Spanish used their own caravels and later carracks."),
       ch("Radar and the satellite-based position system.", "These are twentieth-century technologies.")],
      "Improved ships and borrowed navigational instruments enabled long ocean voyages.")

B.mcq(T_CE, src("Report of a Spanish missionary in central Mexico, 1520s", "“The natives began to die in heaps from a sickness of pustules, so many that the living could not bury the dead. Whole villages were emptied, and the survivors were too weak to work their fields.”") + "\n\nThe situation described is best explained by which of the following?",
      ch("Native Americans had no previous exposure to diseases such as smallpox that Europeans brought with them.", "Populations without immunity to Old World diseases suffered catastrophic mortality, which also weakened their ability to resist conquest."),
      [ch("A famine caused by the sudden arrival of European crops.", "The passage describes a disease, and European crops did not cause such a catastrophe."),
       ch("The spread of the Black Death from Asia through Mongol trade routes.", "The Black Death of the fourteenth century was in Afro-Eurasia, not Mexico in the 1520s."),
       ch("Deliberate massacres by Spanish soldiers that explain nearly all of the deaths.", "Violence and forced labor killed many, but disease was the main cause of the population collapse.")],
      "The passage describes epidemic disease among populations lacking immunity.")

B.mcq(T_CE, "Which statement best describes an effect of the Columbian Exchange on Afro-Eurasian societies?",
      ch("American crops such as potatoes and maize increased food supplies and contributed to population growth in parts of Europe, Africa and China.", "High-yielding American crops adapted to many environments, supporting population growth in Afro-Eurasia."),
      [ch("European farmers began to grow wheat for the first time, introduced from the Americas.", "Wheat is an Old World crop that Europeans brought to the Americas."),
       ch("Horses were introduced to Europe from the Americas.", "Horses were domesticated in Eurasia and were brought to the Americas by Europeans."),
       ch("Sugarcane was first introduced to Europe from the Americas.", "Sugarcane came from the Old World and was later grown in the Americas.")],
      "American crops expanded food supplies in Afro-Eurasia.")

B.mcq(T_MAR, "Which factor best explains why large amounts of Spanish American silver flowed to China in the sixteenth and seventeenth centuries?",
      ch("Ming China's commercial economy and tax system created strong demand for silver, which paid for Chinese goods such as silk and porcelain.", "China needed silver for taxes and trade, and Europeans could pay for Chinese manufactured goods with silver from Potosi and Mexico."),
      [ch("China had banned the use of silver and sought to remove it from its economy.", "The opposite was true: China's economy increasingly used silver."),
       ch("Spain used silver only to pay Native American workers, who then sent it to China.", "Silver was shipped to Europe and across the Pacific through Manila to buy Chinese goods."),
       ch("Europeans wanted Chinese silver mines to be turned over to Spanish rule.", "China was not conquered, and the silver flowed from the Americas.")],
      "Chinese demand for silver connected the American mines to Asian markets.")

B.mcq(T_MAR, "Which feature of the Dutch East India Company (the VOC, founded in 1602) helped the Dutch raise capital and spread the financial risk of long voyages?",
      ch("It was a joint-stock company that sold shares to many investors.", "Investors could pool their money and share profits and losses, which allowed large-scale, high-risk overseas ventures."),
      [ch("It was funded entirely by a Dutch king who owned all of its ships.", "The Dutch Republic was governed by merchants and regents, and the VOC raised funds from many investors."),
       ch("It operated as a medieval craft guild limited to local artisans.", "The VOC was a large commercial company, not a guild."),
       ch("It used only barter and did not raise capital.", "The VOC raised substantial capital from investors.")],
      "Joint-stock financing allowed investors to share risk and profit.")

B.mcq(T_MAR, "The Treaty of Tordesillas (1494) is best understood as evidence of which of the following?",
      ch("Competition between European monarchies for overseas empires, with the Catholic Church's authority used to divide claims.", "Spain and Portugal agreed, with papal involvement, on a line dividing their claims in the newly reached lands outside Europe."),
      [ch("The end of rivalry between Spain and Portugal.", "The agreement was an attempt to manage rivalry, which continued."),
       ch("An agreement between Britain and France to divide North America.", "The treaty was between Spain and Portugal."),
       ch("A treaty negotiated with the rulers of Native American empires.", "Native rulers were not parties to the treaty.")],
      "The treaty shows European rivalry for empire and its Catholic framework.")

B.mcq(T_LAB, src("Letter of a Caribbean sugar planter, 1680s", "“A plantation cannot prosper without at least a hundred slaves, for the mill must run day and night in the season, and the cane must be cut before it spoils. The price of sugar in London is high, and every year more land is planted.”") + "\n\nWhich economic factor does the passage most directly connect to the expansion of the Atlantic slave trade?",
      ch("Rising European demand for sugar and other plantation crops, which created a large demand for forced labor in the Americas.", "Plantation agriculture producing sugar for European markets required large amounts of labor, which planters obtained by importing enslaved Africans."),
      [ch("A decline in European demand for sugar.", "The passage reports high prices and expanding planting, not declining demand."),
       ch("The need for soldiers to defend the colonies against Spain.", "The passage concerns plantation labor, not military needs."),
       ch("New laws abolishing the use of enslaved labor in Europe.", "Abolition came later; the passage shows demand for enslaved workers.")],
      "Demand for sugar in Europe drove plantation expansion and the demand for enslaved labor.")

B.mcq(T_LAB, "Which statement best describes the role of West African states and merchants in the Atlantic slave trade?",
      ch("Some African states and merchants captured and sold enslaved people to Europeans in exchange for goods such as firearms and textiles, which affected warfare and political power in the region.", "African rulers and traders took part on their own terms in many places; the trade changed regional politics and fueled conflict."),
      [ch("African states took no part in the trade, and Europeans captured all enslaved people inland by themselves.", "Europeans usually bought captives at coastal trading posts from African rulers and merchants."),
       ch("All African states banned the sale of captives to Europeans.", "Some states participated extensively, and others resisted; there was no universal ban."),
       ch("The Atlantic slave trade involved only the movement of captives between African kingdoms.", "The Atlantic trade carried millions of people across the ocean to the Americas.")],
      "Some African elites participated and gained from the trade, while its effects were devastating for many African societies.")

B.mcq(T_LAB, "The Spanish encomienda and mita systems in the Americas were similar in that both",
      ch("relied on the labor of Native Americans under the control of the colonial authorities and settlers.", "The encomienda granted settlers the right to Native labor and tribute, and the mita adapted the Inca labor draft for mines and other projects."),
      [ch("paid Native workers market wages in silver.", "Workers under both systems were coerced and poorly paid."),
       ch("relied exclusively on enslaved Africans.", "These systems used Native American labor; African slavery was a separate system."),
       ch("were ended by the Spanish crown in the early sixteenth century.", "Both systems lasted for generations, in modified forms.")],
      "Both systems extracted forced labor from Native Americans.")

B.mcq(T_LAB, "The casta system of Spanish America was primarily based on which of the following?",
      ch("Birth and ancestry, which shaped a person's legal and social status.", "People were classified by ancestry and mixture (Spaniards born in Europe, creoles, mestizos, mulattoes, Native Americans and Africans), and these categories affected rights and opportunities."),
      [ch("Wealth alone, regardless of ancestry.", "Wealth mattered but ancestry formally shaped status."),
       ch("Examination results in a colonial civil service.", "The system was not based on examinations."),
       ch("Religious conversion only.", "Religion mattered, but the categories centered on ancestry.")],
      "Ancestry was the foundation of the colonial hierarchy.")

B.mcq(T_MAR, "Which statement best compares the Spanish and Dutch overseas empires in the seventeenth century?",
      ch("Spain governed large territories in the Americas and drew great wealth from silver mining, while the Dutch relied more on trading posts, fleets and chartered companies to control commerce.", "The Spanish empire was territorial, with administrative control over Native populations and mines; the Dutch emphasized maritime trade networks."),
      [ch("The Dutch conquered large territories in Mexico and Peru, while the Spanish relied on trading posts alone.", "This reverses the characteristics of the two empires."),
       ch("Neither empire was involved in the Atlantic slave trade.", "Both took part in the trade in some form."),
       ch("Both were governed by hereditary monarchs who owned all trading companies.", "The Dutch Republic had no king and its companies were chartered private enterprises.")],
      "Spain built a territorial empire based on mining, while the Dutch built a commercial maritime empire.")

B.mcq(T_TECH, "Which factor best helps explain why European states rather than Ming China led overseas expansion after 1450?",
      ch("The Ming court ended state-sponsored treasure fleet expeditions after 1433, while competing European monarchies sponsored voyages to gain trade and wealth.", "Chinese policy turned away from large maritime expeditions, while rivalry among European states motivated them to seek new routes."),
      [ch("China did not have ships capable of crossing the ocean.", "Ming ships of the early fifteenth century were among the largest in the world."),
       ch("China had no interest in silver or foreign trade.", "Chinese demand for silver and trade was strong and was a major force in global exchange."),
       ch("European ships were far more advanced than Chinese ships in 1405.", "Chinese treasure ships were larger and in many ways comparable to or more advanced than European vessels at that time.")],
      "Policy choices and competition among states help explain the difference.")

B.mcq(T_CE, "Which was an effect of the reintroduction of horses and the introduction of European livestock to the Americas?",
      ch("Horses transformed hunting and warfare for some Plains peoples, and livestock such as cattle and pigs changed land use and diets.", "Horses spread through Native societies and changed life on the Plains; European animals also altered environments."),
      [ch("Horses had been native to the Americas in 1492 and the arrival of Europeans changed nothing.", "Horses had disappeared from the Americas thousands of years earlier and were reintroduced by Europeans."),
       ch("Livestock were introduced to Europe from the Americas, increasing the European food supply.", "Cattle, pigs, sheep and horses came from the Old World to the Americas."),
       ch("The animals had no effect on Native American societies.", "The animals had major effects on many societies.")],
      "The introduction of horses and livestock altered Native American societies and environments.")

B.mcq(T_MAR, "Which statement best describes the economic policy of mercantilism in early modern Europe?",
      ch("Governments sought to increase national wealth by accumulating precious metals and maintaining favorable trade balances, using colonies as sources of raw materials and markets.", "Mercantilism treated colonies and trade as instruments to strengthen the state."),
      [ch("States promoted free trade with little government involvement.", "Mercantilism involved extensive government regulation, tariffs and monopolies."),
       ch("States redistributed land and wealth equally among peasants.", "Mercantilism was concerned with state power and trade, not equality."),
       ch("States banned overseas colonies to protect domestic industries.", "Colonies were central to mercantilist policy.")],
      "Mercantilism used regulation and colonies to build national wealth.")

saq(B, T_LAB,
    "Use the passage to answer parts A, B and C.\n\n" + src("Letter of a Caribbean sugar planter, 1680s", "“A plantation cannot prosper without at least a hundred slaves, for the mill must run day and night in the season, and the cane must be cut before it spoils. The price of sugar in London is high, and every year more land is planted.”") + "\n\n**a)** Identify ONE economic factor in the passage that contributed to the use of enslaved labor.\n\n**b)** Explain ONE way in which the plantation labor system described differed from the Spanish mita or encomienda systems.\n\n**c)** Explain ONE effect of the Atlantic slave trade on societies in West or Central Africa.",
    [(1, "Part A: Identifies high European demand and prices for sugar, or the labor-intensive nature of sugar production"),
     (1, "Part B: Explains that plantation labor relied on enslaved Africans bought and owned as property and transported across the Atlantic, whereas the mita and encomienda relied on Native American labor drafts or tribute"),
     (1, "Part C: Explains an effect such as population loss, increased warfare and slave raiding, or the rise of states that gained power through the trade")],
    "a) The passage notes that the price of sugar in London is high and that more land is planted every year, showing that European demand for sugar made plantations profitable and increased the demand for labor.\nb) Plantations relied on enslaved Africans who were bought, owned and transported across the Atlantic, while the mita and encomienda relied on forced labor drafted from Native American communities.\nc) The slave trade removed millions of people from West and Central Africa, and it encouraged warfare and raiding to capture people, while some states gained power and firearms by participating in it.")

leq(B, T_MAR,
    "**Long Essay Question**\n\nEvaluate the extent to which the flow of silver transformed the global economy in the period 1450-1750.",
    "A strong response takes a position, for example that silver substantially connected and reshaped economies but that other factors also mattered, such as European competition and the demand for labor. It places the topic in context (the voyages of exploration and the creation of colonial empires) and uses specific evidence such as the mines at Potosi, the Manila galleons, Chinese demand for silver and its tax system, the price revolution in Europe, and the effects on Native American labor (the mita). It analyzes causation, continuity and change, and the extent of the impact.",
    "Thesis: Presents a defensible thesis that responds to the prompt and evaluates the extent to which silver transformed the global economy",
    "Contextualization: Describes broader context, such as European exploration and the creation of colonial empires or China's commercialized economy",
    "Evidence: Provides at least two specific, accurate examples (such as Potosi, the Manila galleons, China's silver-based tax system, inflation in Europe) and uses them to support the argument",
    "Analysis and reasoning: Uses causation or change and continuity over time to structure the argument (1 point), and shows complexity by weighing other factors or by considering the varying effects on different regions (2nd point)")

B.save()
B.brief()
