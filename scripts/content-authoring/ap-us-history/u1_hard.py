from common import *

B = hard(1)
T_NA, T_EX, T_CE, T_SP, T_EF = ("native-american-societies", "european-exploration", "columbian-exchange", "spanish-colonial-system", "early-english-and-french-efforts")

# ---- Native American societies ----
B.mcq(T_NA, src("A historian, early twenty-first century", "“Europeans did not arrive in an empty continent. They landed amid confederacies, tributary empires, trading networks and farming towns, each with its own laws and diplomacy, and every European colony had to deal with those realities from its first day.”") + "\n\nWhich of the following developments from 1491 to 1607 best supports the historian's argument?",
      ch("French traders in the St. Lawrence region built alliances with Native trading partners such as the Huron in order to obtain furs.", "French access to furs depended on Native hunters, traders and diplomats, showing that Europeans had to work within existing Native networks."),
      [ch("Epidemic diseases caused a sharp decline in Native populations after contact.", "Disease is an important development, but it does not by itself show that Native political and trading systems shaped European colonies."),
       ch("Spain and Portugal divided overseas claims between themselves at Tordesillas.", "That agreement ignored Native societies rather than showing that Europeans had to negotiate with them."),
       ch("Europeans introduced cattle and pigs to the Americas.", "The introduction of livestock concerns the Columbian Exchange, not the strength of Native political or trading systems.")],
      "The fur trade shows Europeans working within Native networks and diplomacy.")

B.mcq(T_NA, src("An archaeologist's excavation report, Ohio River valley", "“A burial mound dating to several centuries before 1492 held copper from the Lake Superior region, shell beads from the Gulf of Mexico, and mica from the southern Appalachian mountains, alongside locally made pottery and stone tools.”") + "\n\nWhich of the following statements is best supported by the evidence in the passage?",
      ch("Native societies in North America were connected by long-distance exchange networks that moved valued goods across the continent before European contact.", "Materials from the Great Lakes, the Gulf coast and the southern mountains were all found in one mound, which indicates extensive trade."),
      [ch("Native trade before 1492 was limited to the food and tools needed for survival.", "The goods described, such as shell beads and mica, were valued for reasons beyond everyday survival."),
       ch("A single empire controlled all of eastern North America by 1492.", "Trade connections do not show political unification, and the passage describes no empire."),
       ch("Native economies were already dependent on metal goods from Europe.", "The copper came from the Lake Superior region, and the passage dates the mound to before 1492.")],
      "The distant origins of the materials show long-distance exchange among Native societies.")

B.mcq(T_NA, "Which statement best describes how Spanish rule in central Mexico after 1521 related to the Aztec tributary system that came before it?",
      ch("Spanish colonists adapted existing tribute and labor obligations, often claiming for themselves what Native communities had paid to Aztec rulers.", "The conquerors built on the Aztec system of tribute and labor, redirecting it to benefit Spaniards."),
      [ch("Spain abolished all tribute and labor obligations in order to win Native loyalty.", "Spanish rule kept and extended obligations such as tribute and labor."),
       ch("Spain removed every Native noble from authority and ruled only through officials from Spain.", "Spanish authorities often worked through surviving Native elites to collect tribute and organize labor."),
       ch("Spain moved its capital away from the former Aztec capital to avoid reminders of Native rule.", "Mexico City was built on the site of Tenochtitlan.")],
      "Spain exploited and adapted Aztec tributary structures rather than abolishing them.")

# ---- European exploration ----
B.mcq(T_EX, src("A Genoese captain in Spanish service, report to the Crown, 1493", "“The people of these islands go naked and have no iron, and are of a gentle disposition. They would make good servants, and could easily be taught our faith. They tell me there is gold in the hills, and if Your Majesties grant me men and supplies I will bring back as much as you desire.”") + "\n\nWhich later Spanish colonial practice most directly reflected the attitudes expressed in the passage?",
      ch("The encomienda, which compelled Native labor and tribute while requiring colonists to instruct Native people in Christianity.", "The captain combines labor, religion and the search for gold, which are the same elements that the encomienda system joined."),
      [ch("The creation of Native-governed communities free from Spanish authority.", "The passage assumes Native people will serve the Spanish, not govern themselves."),
       ch("The founding of joint-stock companies in which investors shared profits.", "Joint-stock companies were an English financing method and are not a practice suggested by the passage."),
       ch("The establishment of towns in which Native people and colonists voted together on laws.", "Nothing in the passage suggests shared political rights.")],
      "The passage's mix of exploiting labor, conversion and gold seeking points toward the encomienda.")

B.mcq(T_EX, "Which development in the Iberian Peninsula most directly shaped Spain's approach to conquering the Americas?",
      ch("The Reconquista, completed in 1492, which tied military expansion to religious mission and rewarded soldiers with land and authority.", "Centuries of warfare against Muslim-ruled territory produced a military tradition linking conquest, Christianity and rewards for conquerors."),
      [ch("The Protestant Reformation, which divided Spain into Catholic and Protestant regions.", "Spain remained Catholic, and the Reformation began in 1517, after Spain's first American conquests were already underway."),
       ch("The Hundred Years' War, in which Spain defeated England.", "That war was fought between England and France."),
       ch("The defeat of the Spanish Armada in 1588, which ended Spanish ambitions in the Atlantic.", "The Armada's defeat came much later and did not end Spanish colonization.")],
      "The Reconquista shaped Spanish conquest by joining warfare, religion and rewards of land and authority.")

B.mcq(T_EX, "Portuguese voyages along the African coast and to Atlantic islands such as Madeira in the 1400s most directly influenced later European colonization of the Americas by",
      ch("developing sugar plantations worked by enslaved Africans that became a model for plantation economies in the Americas.", "Atlantic island sugar plantations combined European investment, enslaved labor and export crops, a pattern later transferred to Brazil and the Caribbean."),
      [ch("creating an overland trade route to Asia that avoided the Atlantic.", "Portuguese exploration was about sea routes, not an overland route."),
       ch("persuading the Catholic Church to prohibit all enslavement of Africans.", "Portuguese expansion was linked to the growth of the slave trade, not its prohibition."),
       ch("founding English joint-stock companies to settle North America.", "English joint-stock colonization came later and did not grow out of Portuguese voyages.")],
      "Atlantic island plantations provided the plantation-and-slavery model later applied in the Americas.")

# ---- Columbian Exchange ----
B.mcq(T_CE, src("A historian, late twentieth century", "“Europeans carried with them more than ships and weapons. Their cattle, pigs, weeds and, above all, their germs went ahead of them and changed landscapes and peoples before the newcomers themselves arrived.”") + "\n\nWhich of the following best supports the historian's argument?",
      ch("Epidemics of smallpox swept through Native communities before or alongside Spanish expeditions, weakening resistance to conquest.", "Disease moving ahead of or with the Spanish illustrates how living things, not only weapons, altered the Americas."),
      [ch("The Spanish crown sent royal officials called viceroys to govern conquered territories.", "Administration shows political control and does not bear on biological change."),
       ch("Spain and Portugal divided overseas claims at Tordesillas in 1494.", "This was a diplomatic agreement, not evidence of biological change."),
       ch("Missionaries built churches in conquered towns.", "Church building shows religious activity, not the spread of germs, plants or animals.")],
      "Epidemics preceding or accompanying Spanish expeditions best support the claim about biological forces.")

B.mcq(T_CE, "Which of the following was a consequence of the introduction of European livestock such as pigs and cattle into the Americas?",
      ch("Changes to the landscape and conflicts with Native farmers, whose crops were damaged by free-ranging animals.", "Livestock altered land use and sometimes trampled or ate Native crops, creating disputes between colonists and Native communities."),
      [ch("The disappearance of maize as Europeans replaced it entirely with wheat.", "Maize survived and spread widely, including to Europe and Africa."),
       ch("The extinction of the bison on the Great Plains by 1600.", "Bison remained abundant on the Plains long after 1600."),
       ch("The end of farming in Mesoamerica.", "Farming continued in Mesoamerica, and Native crops remained important.")],
      "Livestock changed the landscape and created conflict over crops and land.")

B.mcq(T_CE, "Which statement best describes the demographic result of the first century after 1492 in Spanish America?",
      ch("Native populations fell dramatically, while a new, mixed population of Europeans, Africans and people of mixed descent grew.", "Disease, violence and forced labor reduced Native numbers, and new arrivals and intermarriage created a changing population."),
      [ch("Native populations rose steadily because of new crops and animals, while the number of Europeans stayed small.", "Native populations declined sharply in most regions."),
       ch("Native populations stayed about the same, with Europeans living only in a few port towns.", "Native populations fell sharply, and Europeans spread far beyond the ports."),
       ch("Africans formed the largest group in the Spanish colonies by 1550.", "Native people and people of mixed descent still outnumbered Africans in most Spanish colonies.")],
      "Native decline and the growth of mixed populations characterized Spanish America.")

# ---- Spanish colonial system ----
B.mcq(T_SP, src("A Spanish scholar, mid-sixteenth century", "“It is the nature of some peoples to be ruled by others who are wiser and more skilled in the arts of government and religion. These Indians, who lack letters and our laws, are fitted to labor under Christian guidance, and it is for their own good that they be so directed.”") + "\n\nThe author of the passage would most likely have supported which policy?",
      ch("The continuation of compelled Native labor under the encomienda system.", "The author argues that Native people should work under Spanish direction, which is the premise of the encomienda."),
      [ch("The New Laws of 1542, which limited the encomienda.", "The author defends Spanish control of Native labor, while the New Laws tried to restrict it."),
       ch("A guarantee of freedom of religion for Native converts.", "The passage concerns direction of Native people by Spaniards, not religious freedom."),
       ch("The return of Native lands to communities that had lost them.", "Nothing in the passage supports returning land to Native communities.")],
      "The author's argument justifies Spanish control of Native labor.")

B.mcq(T_SP, "Spanish colonization of New Mexico, beginning with Juan de Oñate's expedition in 1598 and including missions, forced labor and efforts to suppress Pueblo religion, most directly led to which later event?",
      ch("The Pueblo Revolt of 1680, in which Pueblo peoples drove the Spanish out of New Mexico.", "Resentment over forced labor, tribute and attacks on Native religion helped unite Pueblo communities against Spanish rule in 1680."),
      [ch("The French and Indian War, which began in the 1750s.", "That war was an imperial conflict between Britain and France in the 1750s, not a response to Spanish rule in New Mexico."),
       ch("Bacon's Rebellion in colonial Virginia.", "Bacon's Rebellion concerned frontier policy and Native relations in Virginia in 1676."),
       ch("The Stono Rebellion in South Carolina.", "The Stono Rebellion was a 1739 uprising of enslaved Africans.")],
      "Spanish colonial pressure on the Pueblo peoples led to a successful revolt in 1680.")

B.mcq(T_SP, "Which statement best describes how the Spanish crown governed its American empire in the 1500s?",
      ch("Through a centralized bureaucracy of royal officials, including viceroys, who were answerable to the Council of the Indies in Spain.", "The crown established viceroyalties and a supervising council to keep control over distant colonies."),
      [ch("Through assemblies elected by colonists who passed their own laws.", "Spanish colonies were governed from above, not mainly by elected assemblies."),
       ch("Through royal charters that handed colonies to private trading companies.", "That is a better description of English and Dutch methods."),
       ch("Through councils of Native leaders who held independent authority.", "Native leaders could serve as intermediaries but did not hold independent sovereign authority.")],
      "The Spanish empire relied on a centralized bureaucracy led by viceroys and the Council of the Indies.")

# ---- Early English and French efforts ----
B.mcq(T_EF, src("An English promoter of colonization, 1580s", "“If Her Majesty planted colonies upon that coast, the idle poor of our cities would be set to work, the Queen's customs would grow with the trade in timber and furs, and the Spaniard's treasure fleets would lie within easy reach of our ships. Nor should we forget the duty to bring the Indians from darkness to the Gospel.”") + "\n\nWhich combination of motives for colonization is reflected in the passage?",
      ch("Economic opportunity, rivalry with Spain and the desire to spread Christianity.", "The author cites jobs and trade, the chance to threaten Spanish treasure fleets, and religious conversion."),
      [ch("A desire for political independence from the crown and toleration for Catholics.", "The passage assumes royal sponsorship and does not mention independence or toleration for Catholics."),
       ch("A wish to avoid conflict with Spain by settling far from Spanish territory.", "The author wants to bring colonies close enough to threaten Spanish ships."),
       ch("A plan to create self-governing communities free of royal authority.", "The passage says the colonies would be planted by Her Majesty.")],
      "The promoter combines economic, strategic and religious reasons.")

B.mcq(T_EF, "Which statement best explains why French traders generally maintained closer working alliances with Native peoples than the Spanish did?",
      ch("The French economy in North America depended on Native hunters and trading partners to supply furs, and French settlers were few, while Spanish colonies relied on Native labor and tribute.", "French success depended on cooperation with Native trading partners, whereas Spanish systems such as the encomienda were based on control of labor."),
      [ch("France had a larger army in North America and could force Native peoples to trade.", "French settlement was small; the French generally relied on partnership rather than force."),
       ch("The French wanted to establish large farming colonies and needed Native advice on agriculture.", "The French colonies of this period were mainly trading posts, not large farming colonies."),
       ch("Catholic missionaries were forbidden in French colonies, so there was less conflict.", "French Catholic missionaries were active in North America.")],
      "The French fur trade depended on Native partners, shaping a different relationship from Spain's.")

B.mcq(T_EF, "Which factor most contributed to the failure of the English colony at Roanoke?",
      ch("Poor supply and support from England, worsened because war with Spain delayed relief ships, along with strained relations with nearby Native peoples.", "The colonists were isolated; relief ships were delayed in part by England's conflict with Spain, and tensions with local peoples added to their difficulties."),
      [ch("A Spanish army destroyed the colony in 1587.", "Spain searched for the English colony but did not destroy it."),
       ch("A smallpox epidemic spread by the colonists killed all of them.", "There is no evidence that an epidemic caused the colony's end."),
       ch("The colony was made unnecessary when Spain gave England a share of Florida.", "Spain did not give England territory.")],
      "Isolation, delayed support during the war with Spain and tension with Native peoples contributed to Roanoke's failure.")

# ---- Short-answer and long-essay ----
saq(B, T_SP,
    "Use the excerpt to answer parts A, B and C.\n\n" + src("Royal instructions from the Spanish Crown on new settlements, 1570s", "“The governors shall see that the Indians are treated with kindness and instructed in the faith. They shall not be compelled to labor beyond what is just, and shall be paid for their work. Settlements shall be planned around a central plaza, with a church and the houses of the officials.”") + "\n\n**a)** Identify ONE goal of the Spanish Crown that is reflected in the excerpt.\n\n**b)** Explain ONE way in which the actual practices of Spanish colonists in the Americas differed from the policy stated in the excerpt.\n\n**c)** Explain ONE way in which Spanish colonization differed from French colonization in North America in the period 1491 to 1607.",
    [(1, "Part A: Identifies a goal such as spreading Christianity, regulating the treatment of Native peoples, or creating orderly, controlled settlements"),
     (1, "Part B: Explains a difference such as colonists forcing Native labor beyond what was just, mistreating Native peoples under the encomienda, or failing to pay for labor"),
     (1, "Part C: Explains a difference such as Spain building large colonial societies based on Native labor and tribute while the French emphasized the fur trade and small trading communities")],
    "a) The Crown wanted to spread Christianity among Native peoples and to organize settlements in an orderly way under royal and church authority.\nb) Although the Crown said Native people should not be forced to work beyond what was just and should be paid, colonists in the encomienda system often forced them to labor in mines and fields under harsh conditions.\nc) Spain built large colonial societies that depended on Native labor and tribute, while the French in this period focused on a small-scale fur trade and relied on trading partnerships with Native peoples.")

leq(B, T_CE,
    "**Long Essay Question**\n\nEvaluate the extent to which contact with Europeans transformed Native American societies in the period 1491 to 1607.",
    "A strong response states a defensible thesis, for example that contact transformed Native societies profoundly through disease and demographic collapse, new animals, new labor systems and missions, while some Native political structures, trading roles and ways of life persisted or adapted. It places contact in context (European exploration and the Columbian Exchange), uses specific evidence (smallpox epidemics, horses on the Plains, the encomienda, Spanish missions, the fur trade and Native alliances), and uses causation or continuity and change to weigh transformation against adaptation.",
    "Thesis: Presents a defensible thesis that responds to the prompt and evaluates the extent to which contact transformed Native American societies",
    "Contextualization: Places the topic in a broader context, such as European exploration, competition among European states, or the Columbian Exchange",
    "Evidence: Provides at least two specific, accurate pieces of evidence relevant to the prompt (1 point for addressing the topic with evidence, 2nd point for using specific evidence to support the argument)",
    "Analysis and reasoning: Uses causation or continuity and change to structure the argument (1 point), and demonstrates complex understanding, such as showing that some Native societies adapted, kept political independence or shaped colonial relations (2nd point)")

B.save()
B.brief()
