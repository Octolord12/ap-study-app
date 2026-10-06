from common import *

B = base(1)
T_NA, T_EX, T_CE, T_SP, T_EF = ("native-american-societies", "european-exploration", "columbian-exchange", "spanish-colonial-system", "early-english-and-french-efforts")

# ---- Native American societies ----
B.mcq(T_NA, "Which crop was the agricultural foundation of many Native American societies, from the Southwest to the Eastern Woodlands, before European contact?",
      ch("Maize (corn)", "Maize, often grown with beans and squash, supported villages and growing populations across much of North America."),
      [ch("Wheat", "Wheat was an Old World grain brought to the Americas by Europeans after 1492."),
       ch("Rice", "Rice was not a staple of Native farming societies in North America before contact; it was introduced from the Old World."),
       ch("Sugarcane", "Sugarcane was introduced from the Old World and became important only under European plantation agriculture.")],
      "Maize cultivation spread widely across the Americas and underpinned many Native societies.", difficulty="easy")

B.mcq(T_NA, "Which statement best explains how Pueblo peoples of the Southwest adapted to their dry environment before European contact?",
      ch("They built permanent villages and used irrigation and careful water management to grow maize, beans and squash.", "Pueblo farmers settled in multistory stone and adobe villages and used irrigation and dry-farming methods to raise crops in an arid climate."),
      [ch("They lived as nomadic bison hunters who followed the herds on horseback.", "That describes Plains peoples after the Spanish introduced horses; Pueblo peoples were settled farmers."),
       ch("They relied on salmon fishing and trade along the Pacific coast.", "Salmon fisheries supported Native societies of the Pacific Northwest, not the dry Southwest."),
       ch("They lived in bark-covered longhouses organized in a political confederacy of five nations.", "Longhouses and a confederacy describe the Haudenosaunee of the Northeast.")],
      "Pueblo societies combined irrigation farming with permanent villages suited to an arid environment.")

B.mcq(T_NA, src("An archaeologist's field report on a large site in the Mississippi River valley", "“The central settlement covered several square miles and held more than a hundred earthen mounds, the largest rising in terraces above a great plaza. Storage pits show a large surplus of maize. The site was at its greatest size around the year 1100 and had been mostly abandoned two centuries before any European arrived in the region.”") + "\n\nWhich statement is best supported by the passage?",
      ch("Some Native societies had large, complex communities supported by farming surpluses well before European contact.", "The scale of the settlement, its mounds and its stored maize show a dense, organized society that existed centuries before Europeans came."),
      [ch("Native peoples lived only in small, scattered bands with no permanent settlements.", "The passage describes a large, permanent settlement with monumental earthworks."),
       ch("Native societies built large settlements only after European tools and animals arrived.", "The passage dates the settlement's peak to about 1100, long before Europeans arrived."),
       ch("The settlement was abandoned because of European conquest.", "The passage says it was mostly abandoned two centuries before any European arrived there.")],
      "The passage shows a large, organized, farming-based society that flourished and declined before contact.")

B.mcq(T_NA, "The Aztec and Inca empires were similar in that both",
      ch("built large, centralized states that drew tribute or labor from conquered peoples.", "The Aztecs collected tribute from subject city-states, and the Inca organized labor service (the mit'a) from the peoples they ruled."),
      [ch("were located in what is now the eastern United States.", "The Aztecs were centered in central Mexico and the Inca in the Andes of South America."),
       ch("relied on iron tools and horses to expand their territory.", "Neither empire had iron tools or horses; both were in the Americas before European contact."),
       ch("were conquered by English colonists in the late 1500s.", "Both were conquered by Spanish forces in the 1500s.")],
      "Both empires extracted tribute and labor from subject peoples through centralized rule.")

B.mcq(T_NA, "Which statement best describes the Haudenosaunee (Iroquois) of the Northeast before and around the time of European contact?",
      ch("They farmed crops such as maize, beans and squash in villages of longhouses, and women held significant influence through clan kinship.", "Haudenosaunee society was matrilineal: clan mothers had a voice in choosing leaders, and farming was central to village life."),
      [ch("They were nomadic hunters whose way of life centered on following bison herds.", "Bison hunting characterized Plains societies, not the farming villages of the Northeast."),
       ch("They were ruled by a single emperor who collected tribute from distant provinces.", "The Haudenosaunee were organized in a confederacy governed by councils, not an empire under one emperor."),
       ch("They depended on irrigation canals to farm in a desert environment.", "The Haudenosaunee lived in a well-watered region and did not need desert irrigation.")],
      "The Haudenosaunee combined farming, longhouse villages and a council confederacy in which kinship through women mattered.", difficulty="hard")

B.mcq(T_NA, "Which factor best explains how Native peoples of the Pacific Northwest supported large, settled communities without relying mainly on farming?",
      ch("Abundant fish and other resources, especially salmon, allowed them to build permanent villages.", "Rich salmon runs and other coastal resources supplied enough food to support dense, settled populations."),
      [ch("They imported grain from Spanish missions in exchange for furs.", "Spanish missions did not supply the Pacific Northwest before European contact."),
       ch("They irrigated large maize fields using canals.", "Irrigated maize farming is associated with the Southwest, not the Pacific Northwest."),
       ch("They lived on the proceeds of tribute from conquered farming states.", "There was no tribute empire in the Pacific Northwest like those of the Aztecs or Inca.")],
      "Natural abundance in the environment, not agriculture, supported settled life in the Pacific Northwest.")

# ---- European exploration ----
B.mcq(T_EX, "Christopher Columbus's 1492 voyage, sponsored by the Spanish monarchy, was primarily intended to",
      ch("find a westward sea route to the wealth of Asia.", "Spain hoped a western route would give access to Asian trade goods such as spices; Columbus reached the Caribbean instead."),
      [ch("establish colonies where religious dissenters could worship freely.", "Religious refuge was a motive for some later English colonists, not for Columbus's voyage."),
       ch("claim land in North America for the English crown.", "Columbus sailed for Spain, not England."),
       ch("enforce a division of the world between Spain and the Dutch.", "The Dutch were not yet a colonial power, and the division of claims came with the Treaty of Tordesillas two years after Columbus's first voyage.")],
      "Columbus sought a western route to Asia's trade wealth, backed by Spain.", difficulty="easy")

B.mcq(T_EX, "Which development most directly made long Atlantic voyages by Europeans possible in the 1400s?",
      ch("Improved ship designs, such as the caravel, and better navigational tools, including the compass and astrolabe.", "Portuguese and Spanish sailors combined sturdier, more maneuverable ships with instruments that helped them find their position and direction."),
      [ch("The use of steam engines to power ocean-going ships.", "Steam-powered ships did not appear until the 1800s."),
       ch("Detailed charts of the Americas supplied by Chinese treasure fleets.", "Chinese fleets did not map the Americas for Europeans."),
       ch("The invention of the telegraph to coordinate fleets across the ocean.", "The telegraph is a nineteenth-century invention.")],
      "Better ships and navigational tools opened the Atlantic to European exploration.", difficulty="medium")

B.mcq(T_EX, src("A Portuguese court chronicler, mid-fifteenth century", "“The Prince wished to know what lay beyond the Cape, to bring the people of those coasts to the faith, and to find the gold and goods that Moorish merchants carry to the markets of the north. For if the ships can trade directly with those lands, the Moors will no longer hold the road.”") + "\n\nWhich statement best describes the motives for exploration reflected in the passage?",
      ch("Religious goals and the search for commercial profit, including an effort to bypass Muslim middlemen, shaped exploration.", "The passage mentions spreading the faith, finding gold, and cutting out the Muslim merchants who controlled existing trade routes."),
      [ch("Exploration was driven solely by scientific curiosity about geography.", "The passage names religious and commercial goals, not only scientific curiosity."),
       ch("Explorers sought to escape religious persecution in their home country.", "Nothing in the passage mentions escaping persecution."),
       ch("Exploration was intended to spread representative government to other lands.", "The passage does not mention political institutions.")],
      "Faith and profit, including breaking into trade controlled by others, motivated early Portuguese exploration.")

B.mcq(T_EX, "The Treaty of Tordesillas (1494) is best described as",
      ch("an agreement between Spain and Portugal, with papal backing, dividing newly claimed lands outside Europe between them.", "It set a line of demarcation that gave Spain most of the Americas and Portugal the right to claim eastern lands, which later included Brazil."),
      [ch("a treaty in which Spain recognized the rights of Native Americans to their lands.", "The treaty concerned claims between two European powers and did not protect Native land rights."),
       ch("an agreement that ended the Spanish Reconquista with the fall of Granada.", "Granada fell in 1492, and the treaty dealt with overseas claims, not the Reconquista."),
       ch("a treaty that granted England the right to colonize North America.", "England was not a party to the treaty.")],
      "Tordesillas divided overseas claims between Spain and Portugal.", difficulty="medium")

B.mcq(T_EX, "Which statement best explains how the Protestant Reformation, which began in 1517, affected European colonization of the Americas?",
      ch("Religious conflict among European states added to their rivalry over colonies, and Protestant England and the Netherlands later challenged Catholic Spain's claims.", "Religion became part of the competition for empire, with Spain linking colonization to spreading Catholicism and rivals contesting its dominance."),
      [ch("It ended European interest in colonization because Protestants opposed overseas expansion.", "Protestant powers such as England and the Netherlands became active colonizers."),
       ch("It led Catholic and Protestant states to form joint colonizing ventures.", "Religious rivalry made such cooperation unlikely; states competed instead."),
       ch("It convinced Spain to end the encomienda system in the first half of the 1500s.", "The encomienda was criticized for its abuses but was not ended because of the Reformation.")],
      "The Reformation intensified religious and political rivalry among European colonizing powers.", difficulty="hard")

B.mcq(T_EX, "Which factor most helped the Spanish conquistador Hernán Cortés defeat the Aztec Empire between 1519 and 1521?",
      ch("Alliances with Native peoples who resented Aztec rule, combined with the effects of epidemic disease.", "Cortés gained allies such as the Tlaxcalans, who were hostile to Aztec tribute demands, and smallpox severely weakened Tenochtitlan."),
      [ch("A large Spanish army shipped over from Spain after the first battles.", "Cortés began with a few hundred men; his strength came from allies and circumstances, not massive reinforcement from Spain."),
       ch("The Aztecs had no organized army or capital city.", "The Aztecs had a large army and a major capital at Tenochtitlan."),
       ch("The Aztec emperor ceded his empire to Spain by treaty at the start of the expedition.", "The conquest involved warfare and the destruction of Tenochtitlan, not a peaceful treaty.")],
      "Native allies and disease, along with Spanish weapons, enabled the conquest.", difficulty="medium")

# ---- Columbian Exchange ----
B.mcq(T_CE, "Which consequence of contact between Europeans and Native Americans in the 1500s caused the greatest loss of life among Native peoples?",
      ch("The spread of Old World diseases such as smallpox and measles.", "Native peoples had no prior exposure to these diseases, and epidemics killed a very large share of the population in many regions."),
      [ch("Heavy taxation by Spanish colonial officials.", "Tax burdens were harmful, but disease killed far more people."),
       ch("The introduction of European crops that replaced Native farming.", "New crops did not cause mass death; disease did."),
       ch("The mass migration of Native peoples to Europe.", "Very few Native people traveled to Europe in this period.")],
      "Epidemic disease was the leading cause of Native population decline after contact.", difficulty="easy")

B.mcq(T_CE, "Which of the following was carried from the Old World to the Americas as part of the Columbian Exchange?",
      ch("Sugarcane", "Sugarcane came from the Old World and became the basis of plantation agriculture in the Caribbean and Brazil."),
      [ch("Tobacco", "Tobacco was native to the Americas and was carried to Europe."),
       ch("Maize", "Maize was native to the Americas and spread to Europe, Africa and Asia."),
       ch("Potatoes", "The potato originated in the Andes and was carried to Europe.")],
      "Sugarcane moved from the Old World to the Americas, where it transformed economies.")

B.mcq(T_CE, src("A Spanish friar's letter to his superiors, 1540s", "“Where I once passed through villages of a thousand souls, I now find a dozen families. The fever came upon them and none was spared. The fields are grown over, and the encomenderos complain that there are no hands left to work them.”") + "\n\nThe conditions described in the passage most directly contributed to which development?",
      ch("Increased reliance by Spanish colonists on enslaved Africans as the Native labor force shrank.", "As disease reduced the Native population, colonists turned to the transatlantic slave trade to replace lost labor."),
      [ch("A Native American victory that drove the Spanish out of Mexico.", "Depopulation weakened Native resistance rather than strengthening it."),
       ch("A sharp decline in European interest in the Americas.", "European colonization continued and expanded."),
       ch("The shift of Spain's colonial economy toward manufacturing.", "Spain's colonies remained based on agriculture, ranching and mining.")],
      "Native depopulation increased demand for other sources of labor, including enslaved Africans.", difficulty="medium")

B.mcq(T_CE, "How did the horse, introduced to the Americas by the Spanish, change the lives of many Plains peoples by the 1700s?",
      ch("It increased their mobility and effectiveness in hunting bison and in warfare.", "Horses allowed Plains peoples to cover greater distances, hunt bison more efficiently and fight more effectively."),
      [ch("It encouraged them to become sedentary irrigation farmers.", "Horses made nomadic hunting more attractive, not settled irrigation farming."),
       ch("It led them to abandon hunting in favor of wheat farming.", "Many Plains peoples increased their reliance on bison hunting after acquiring horses."),
       ch("It allowed them to build large mound-building cities.", "Mound-building cities such as Cahokia declined before the horse arrived.")],
      "Horses gave Plains peoples new mobility for hunting and war.", difficulty="medium")

B.mcq(T_CE, "Which statement best describes a long-term effect of the Columbian Exchange on the Atlantic world?",
      ch("The movement of crops, animals and diseases reshaped economies and societies on several continents, including the growth of plantation agriculture worked by enslaved Africans.", "Crops such as sugar and tobacco fed a plantation economy built on the transatlantic slave trade, while American crops changed diets in the Old World."),
      [ch("Only precious metals were exchanged, so crops and animals had little effect.", "Crops and animals had huge effects on populations and economies."),
       ch("Native American societies gained control of transatlantic trade.", "European powers, not Native societies, dominated transatlantic trade."),
       ch("European demand for goods from the Americas declined after the 1500s.", "European demand for American products such as sugar, tobacco and silver grew.")],
      "The exchange transformed economies and societies on both sides of the Atlantic.", difficulty="hard")

B.mcq(T_CE, "How did American crops such as the potato and maize affect Europe, Africa and Asia?",
      ch("They improved food supplies and helped support population growth.", "These high-yield crops grew in many climates and provided reliable nutrition for growing populations."),
      [ch("They were rejected everywhere and had little effect on diets.", "They were widely adopted and changed diets."),
       ch("They caused widespread famine by replacing native grains.", "Over time, they usually increased food supplies, though overreliance could be risky."),
       ch("They were used only as ornamental plants.", "They became major food crops.")],
      "American crops helped feed growing populations in the Old World.")

# ---- Spanish colonial system ----
B.mcq(T_SP, "The encomienda system in Spanish America was a system in which",
      ch("Spanish colonists received the right to the labor or tribute of Native communities, supposedly in return for protecting and converting them.", "The Crown granted colonists authority over Native people, who were often forced into harsh labor despite the stated obligation to Christianize them."),
      [ch("Native Americans were granted full citizenship and equal rights.", "The system exploited Native labor and did not grant equality."),
       ch("English joint-stock companies financed colonies in exchange for shares of profit.", "Joint-stock companies were an English financing method, not the encomienda."),
       ch("poor Europeans paid for their passage by working for several years as servants.", "That describes indentured servitude.")],
      "The encomienda gave colonists control over Native labor and tribute.", difficulty="easy")

B.mcq(T_SP, src("A Spanish Dominican friar, 1540s", "“I have seen the Indians driven to the mines until they fall, and when they fall they are replaced. These men are not beasts but rational souls with rights of their own. If the Crown does not end these cruelties, we will have no Christians to save, only graves.”") + "\n\nThe passage best reflects which development in the Spanish Empire?",
      ch("Debate within the Spanish Empire over the treatment of Native peoples under the encomienda system.", "Some clergy criticized colonists' abuse of Native labor, which led to debates and reform efforts such as the New Laws."),
      [ch("Native demands for independence from Spain.", "The author is a Spanish friar criticizing colonists, not a Native leader seeking independence."),
       ch("An English challenge to Spanish control of the Caribbean.", "The passage concerns treatment of Native people, not English rivalry."),
       ch("Protestant criticism of Catholic missionary activity.", "The author is a Catholic friar who wants to save souls.")],
      "Criticism of the treatment of Native people was part of internal Spanish debate.")

B.mcq(T_SP, "Which statement best describes the social structure of colonial Spanish America?",
      ch("A hierarchy based largely on birthplace and ancestry, with people born in Spain at the top and Native and African people at the bottom.", "The casta system ranked people by origin and descent, with peninsulares (born in Spain) holding the highest status."),
      [ch("A system of equality among all Catholics regardless of ancestry.", "Status differed sharply by ancestry despite shared religion."),
       ch("A society in which Native elites ruled independently of Spain.", "Spain held ultimate authority, and Native elites were subordinate."),
       ch("A class system based solely on ownership of land, open equally to all.", "Birth and ancestry strongly shaped opportunity.")],
      "The casta system ranked people by birth and ancestry.", difficulty="medium")

B.mcq(T_SP, "The Spanish missions established in Florida and in the Southwest were primarily intended to",
      ch("convert Native peoples to Catholicism and bring them into the colonial economy.", "Missionaries sought converts and often organized Native labor on mission lands."),
      [ch("form trade alliances with English merchants.", "Spain and England were rivals, not partners."),
       ch("create self-governing democratic communities for Native peoples.", "Missions were controlled by Spanish clergy and officials."),
       ch("supply goods to the Dutch West India Company.", "The missions served Spanish goals, not Dutch trade.")],
      "Missions combined religious conversion with colonial control.")

B.mcq(T_SP, "How did the discovery of rich silver deposits at Potosí (in 1545) and in Mexico affect the global economy?",
      ch("Silver flowing from the Americas enriched Spain and stimulated trade across the Atlantic and with Asia.", "American silver financed Spanish power and moved through global trade networks, including the Manila galleon trade to China."),
      [ch("It ended Spain's dependence on forced labor in the colonies.", "Silver mining relied heavily on forced Native labor."),
       ch("It caused Spain to lose interest in its American colonies.", "The wealth made the colonies more important to Spain."),
       ch("It led Spain to rapidly industrialize its economy.", "Industrialization came much later and Spain did not industrialize rapidly as a result.")],
      "American silver reshaped trade and enriched the Spanish crown.", difficulty="hard")

B.mcq(T_SP, "Spain founded St. Augustine in Florida in 1565 mainly to",
      ch("protect its treasure fleet routes and eliminate a French Protestant settlement nearby.", "St. Augustine secured Spanish shipping lanes and followed the destruction of the French outpost of Fort Caroline."),
      [ch("provide a refuge for Spanish Protestants.", "Spain was a Catholic power and did not seek to shelter Protestants."),
       ch("grow tobacco for English markets.", "The settlement was a military outpost, not a tobacco colony for England."),
       ch("trade furs with Dutch merchants.", "The Dutch had no role in founding St. Augustine.")],
      "St. Augustine was a defensive outpost founded to protect Spanish interests against rivals.", difficulty="medium")

# ---- Early English and French efforts ----
B.mcq(T_EF, "The English colony at Roanoke, founded in the 1580s, is best described as",
      ch("an early attempt at English settlement in North America that failed, with its colonists disappearing by 1590.", "Roanoke's settlers were gone when supply ships returned in 1590, leaving a mystery known as the Lost Colony."),
      [ch("a profitable tobacco colony that became the model for later settlements.", "Tobacco became profitable later at Jamestown, not Roanoke."),
       ch("a Spanish mission community that converted many Native people.", "Roanoke was an English colony."),
       ch("a French fur-trading outpost on the St. Lawrence River.", "Roanoke was on the coast of present-day North Carolina and was English.")],
      "Roanoke was an English attempt at settlement that ended in failure.", difficulty="easy")

B.mcq(T_EF, "Which statement best describes the French approach to colonization in North America during the 1500s and early 1600s?",
      ch("The French settled in small numbers and relied on the fur trade and trading relationships with Native peoples.", "French traders exchanged European goods for furs and formed alliances with Native peoples rather than settling large farming communities."),
      [ch("They established large farming colonies that displaced Native peoples from their land.", "That better describes English settlement patterns."),
       ch("They forced Native peoples into labor under the encomienda.", "The encomienda was a Spanish system."),
       ch("They set up self-governing religious communities for dissenters.", "French settlement did not center on religious refuge for dissenters.")],
      "French colonization emphasized the fur trade and Native alliances.", difficulty="easy")

B.mcq(T_EF, "England's defeat of the Spanish Armada in 1588 contributed to English colonization primarily because it",
      ch("weakened Spain's dominance at sea and made it more possible for England to challenge Spain in the Atlantic.", "The victory boosted English confidence and reduced Spain's ability to block rivals."),
      [ch("gave Spain complete control of the North Atlantic.", "Spain was the loser in the battle."),
       ch("ended English interest in North America for the rest of the century.", "English colonial efforts continued after 1588."),
       ch("led England to return to the Catholic Church.", "England remained Protestant.")],
      "The Armada's defeat undermined Spanish naval supremacy, encouraging English expansion.", difficulty="hard")

B.mcq(T_EF, "Which condition in England helped encourage interest in overseas colonies in the late 1500s?",
      ch("Population growth and the displacement of rural people from farmland, which created many people without land or work.", "Economic pressures at home made colonies seem like an outlet for the poor and a source of new wealth."),
      [ch("A severe shortage of workers throughout England.", "England had a surplus of landless poor, not a shortage."),
       ch("A papal order directing England to settle North America.", "Protestant England did not follow papal orders."),
       ch("An invitation from Spain to share the Americas.", "Spain regarded England as a rival.")],
      "Economic pressures and rivalry with Spain increased English interest in colonization.", difficulty="medium")

B.mcq(T_EF, src("A French fur trader's account, early seventeenth century", "“Each spring the Huron bring their canoes down the river laden with beaver pelts. In return we give them copper kettles, iron knives, and cloth. They value these goods highly, and we value the furs more, for in France they command a great price.”") + "\n\nThe passage best illustrates which of the following?",
      ch("A trading relationship in which both Europeans and Native peoples sought goods that were valuable to them.", "Each side gained goods it wanted, with Europeans seeking furs for profit and Native peoples acquiring useful metal goods and cloth."),
      [ch("A conquest in which Native peoples were forced into labor.", "The passage describes voluntary trade, not forced labor."),
       ch("English control of the fur trade.", "The trader is French."),
       ch("The total dependence of Native peoples on Europeans for survival.", "The passage shows valued exchange, not total dependence.")],
      "The fur trade involved mutually beneficial exchange of valued goods.", difficulty="medium")

B.mcq(T_EF, "Which statement best describes the state of European competition in North America by about 1600?",
      ch("Spain held Florida, the Southwest approaches and much of the Caribbean and Mexico, while England and France were only beginning to challenge it.", "Spain was the dominant European power in the Americas, with rivals making early, limited efforts."),
      [ch("England controlled most of North America and Spain had withdrawn.", "Spain remained dominant, and England had only attempted a failed colony."),
       ch("The Dutch had established settled colonies along the Pacific coast.", "The Dutch were not on the Pacific coast of North America."),
       ch("France and England had formed a joint empire in the Caribbean.", "They were rivals, not partners.")],
      "Spain was dominant in the Americas around 1600, while England and France were just beginning to challenge it.", difficulty="hard")

# ---- Short-answer questions ----
saq(B, T_CE,
    "Use the excerpt to answer parts A, B and C.\n\n" + src("A historian's interpretation, late twentieth century", "“The voyages of 1492 began an exchange of plants, animals and microbes that remade the world. The animals and crops of the Old World spread across the Americas, but the greatest transfer was invisible: the diseases that cut Native populations by a staggering proportion within a few generations.”") + "\n\n**a)** Identify ONE claim the historian makes about the effects of contact on the Americas.\n\n**b)** Explain ONE way in which an exchange of crops or animals changed economies or societies in the period 1491 to 1607.\n\n**c)** Explain ONE way in which the demographic changes described in the excerpt affected European colonization.",
    [(1, "Part A: Identifies a claim from the excerpt, such as that diseases caused a staggering decline in Native populations or that the exchange of plants, animals and microbes remade the world"),
     (1, "Part B: Explains an effect such as horses transforming Plains societies, sugar and other crops enabling plantation economies, or American crops like maize and potatoes supporting population growth in the Old World"),
     (1, "Part C: Explains an effect such as Native depopulation weakening resistance to conquest, reducing the Native labor force and leading colonists to turn to enslaved Africans, or opening land to European settlement")],
    "a) The historian claims that disease was the greatest effect of contact, sharply reducing Native populations within a few generations.\nb) Horses brought by the Spanish gave Plains peoples greater mobility for hunting bison and warfare, changing their societies and economies.\nc) With Native populations devastated, Spanish colonists lost much of their labor force and increasingly turned to enslaved Africans, while depopulation also weakened Native resistance to conquest.")

saq(B, T_SP,
    "Use the excerpt to answer parts A, B and C.\n\n" + src("A Spanish Dominican friar, 1540s", "“I have seen the Indians driven to the mines until they fall, and when they fall they are replaced. These men are not beasts but rational souls with rights of their own. If the Crown does not end these cruelties, we will have no Christians to save, only graves.”") + "\n\n**a)** Identify ONE point of view expressed in the excerpt about the treatment of Native peoples.\n\n**b)** Explain ONE way in which the encomienda system or Spanish colonial labor practices shaped relations between colonists and Native peoples.\n\n**c)** Explain ONE reason that some Spanish colonists opposed reform of their treatment of Native peoples.",
    [(1, "Part A: Identifies that the author condemns the cruel treatment of Native people, views them as rational beings with rights, or argues the Crown must end abuses"),
     (1, "Part B: Explains that the encomienda gave colonists control over Native labor and tribute, leading to exploitation, forced labor and demographic and cultural disruption"),
     (1, "Part C: Explains that colonists relied on Native labor for wealth from mining and agriculture, and reform would have reduced their profits and power")],
    "a) The friar argues that Native peoples are rational souls with rights and that the Crown must end the cruelty of forced labor.\nb) The encomienda gave Spanish colonists the right to demand labor and tribute from Native communities, which led to forced labor in mines and fields and exploitation of Native peoples.\nc) Many colonists opposed reform because their wealth depended on Native labor in mining and farming, and limits on that labor would have cut their income and status.")

saq(B, T_NA,
    "Using your knowledge of United States history, answer parts A, B and C.\n\n**a)** Identify ONE way in which the environment shaped the way of life of a Native American society in North America before 1492.\n\n**b)** Identify ONE way in which the environment shaped the way of life of a DIFFERENT Native American society in North America before 1492.\n\n**c)** Explain ONE reason that Native American societies in different regions developed different political and social structures.",
    [(1, "Part A: Identifies an accurate environmental adaptation of one society (for example, Pueblo irrigation farming in the arid Southwest, or bison hunting on the Plains)"),
     (1, "Part B: Identifies an accurate adaptation of a different society (for example, salmon fishing in the Pacific Northwest, or the farming villages of the Eastern Woodlands)"),
     (1, "Part C: Explains that differences in climate, resources and food supply, together with agricultural surpluses or their absence, shaped population density, social organization and political structures")],
    "a) Pueblo peoples of the Southwest used irrigation and careful water management to grow maize, beans and squash in permanent villages in an arid environment.\nb) Peoples of the Pacific Northwest relied on abundant salmon and other coastal resources, which let them build permanent villages without depending mainly on farming.\nc) Differences in climate, available food and farming surpluses affected how many people a region could support and how they organized, so densely settled farming societies developed larger political structures than small, mobile hunting groups.")

B.save()
B.brief()
