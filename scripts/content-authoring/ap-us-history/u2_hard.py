from common import *

B = hard(2)
T_FO, T_SL, T_AT, T_RE, T_BO = ("english-colonies-founding", "slavery-and-labor-systems", "atlantic-economy-and-mercantilism", "religion-and-enlightenment", "imperial-rivalry-and-borderlands")

# ---- Founding the English colonies ----
B.mcq(T_FO, src("A dissenting minister, 1630s", "“The civil magistrate has no authority over the conscience of any person. When the state compels worship, it makes hypocrites, not believers. Let every community order its own civil peace and leave the soul to God.”") + "\n\nWhich statement best explains why the leaders of Massachusetts Bay responded to such views by banishing their author?",
      ch("Puritan leaders believed that religious unity was essential to the stability of their community, so dissent threatened both church and civil order.", "In Massachusetts Bay the church and civil government were closely linked, and leaders treated disagreement over religion as a danger to the colony."),
      [ch("The Crown had ordered all dissenting ministers removed from the colonies.", "Banishment was a decision of colonial authorities, not a royal order."),
       ch("Massachusetts law protected the religious freedom of Anglicans only.", "Massachusetts Puritans were not protecting Anglican freedom."),
       ch("Puritan leaders feared the author's views would provoke Native attacks on the colony.", "The passage says nothing about Native peoples; the objection was religious and political.")],
      "Puritan leaders saw religious dissent as a threat to the unity of the community.")

B.mcq(T_FO, "Georgia, founded in 1732, differed from earlier English colonies in that it was established in part to",
      ch("serve as a military buffer protecting the Carolinas from Spanish Florida, with slavery initially banned.", "Georgia's founders wanted a defensive frontier colony, and early regulations prohibited slavery."),
      [ch("provide a refuge for Catholics fleeing persecution in England.", "That describes Maryland, founded a century earlier."),
       ch("expand tobacco farming on the model of the Chesapeake.", "Georgia's early plans emphasized defense and small farms rather than tobacco."),
       ch("create a base for the French fur trade.", "Georgia was an English colony.")],
      "Georgia was founded as a defensive buffer against Spanish Florida.")

B.mcq(T_FO, "Which pair of developments best explains how Virginia became economically viable after its early years of hardship?",
      ch("The success of tobacco as an export crop and the headright system, which granted land to those who paid for the passage of laborers.", "Tobacco created profit, and headrights encouraged the importation of workers and the spread of plantations."),
      [ch("A profitable fur trade and a policy of religious toleration.", "Virginia's economy rested on tobacco rather than furs."),
       ch("Silver mining and the use of Native mission labor.", "That describes the Spanish colonies."),
       ch("Steady dividends from the joint-stock company and royal subsidies.", "The Virginia Company struggled financially and lost its charter in 1624.")],
      "Tobacco and the headright system helped make Virginia economically successful.")

# ---- Slavery and labor systems ----
B.mcq(T_SL, src("A historian, early twenty-first century", "“Slavery in the English colonies grew out of two forces working together: the economic demand for cheap, controllable labor, and the creation of a racial ideology that justified lifelong bondage for Africans and their descendants.”") + "\n\nWhich of the following developments best supports the historian's argument?",
      ch("Colonial laws, such as the 1660s statutes making slavery hereditary and the Virginia slave code of 1705, that defined enslaved people as property and set them apart from white servants.", "These laws gave racial slavery a legal foundation in order to maintain a controlled labor force."),
      [ch("English laws requiring indentured servants to be released at the end of their terms.", "These rules protected white servants and do not show a racial justification for lifelong bondage."),
       ch("Parliament's passage of the Navigation Acts.", "The Navigation Acts regulated trade and do not concern the development of racial ideology."),
       ch("The spread of evangelical revivals during the Great Awakening.", "The Awakening was a religious movement that came later and does not address labor systems directly.")],
      "Laws creating hereditary, race-based slavery support the argument about both labor demand and racial ideology.")

B.mcq(T_SL, "Which statement best describes cultural change among enslaved Africans in the English colonies of the 1700s?",
      ch("They preserved and adapted African traditions in language, music, religion and crafts, creating new African American cultural forms such as the Gullah language of the Carolina coast.", "Enslaved people combined African heritage with their new circumstances, forming distinctive cultures."),
      [ch("They abandoned all African traditions and adopted the culture of their enslavers.", "Many African traditions survived in adapted form."),
       ch("They were allowed to practice only the Puritan form of Christianity.", "Enslaved people practiced varied forms of religion, and Puritanism was not imposed on all of them."),
       ch("Their culture remained identical to that of West Africa because they had no contact with Europeans.", "Enslaved Africans lived under European control and blended traditions.")],
      "Enslaved Africans adapted and preserved traditions, creating new cultural forms.")

B.mcq(T_SL, "Spanish policy in Florida in the early 1700s, including the establishment of Fort Mose in 1738, most directly led to which development?",
      ch("Florida became a destination for enslaved people escaping from English colonies, increasing tension with South Carolina.", "Spain offered freedom to enslaved people from English colonies who adopted Catholicism, drawing freedom seekers southward."),
      [ch("English colonists abandoned slavery after seeing Spanish success.", "English colonists continued and expanded slavery."),
       ch("Spain ended slavery throughout its American empire.", "Spain's empire continued to practice slavery."),
       ch("Florida became the main source of enslaved labor for northern colonies.", "Florida was not a major supplier of enslaved labor to the North.")],
      "Spanish Florida's offer of freedom attracted people escaping slavery and increased conflict with South Carolina.")

# ---- Atlantic economy and mercantilism ----
B.mcq(T_AT, src("A historian, late twentieth century", "“Although colonists often complained of British regulation, the day-to-day effect of the Navigation Acts was modest, and many colonists benefited from belonging to a protected imperial market.”") + "\n\nWhich of the following best supports the historian's argument?",
      ch("New England's shipbuilders prospered because ships built in the colonies counted as English vessels under the trade laws.", "The Navigation Acts required English or colonial ships, which created demand for colonial shipbuilders."),
      [ch("The Dominion of New England replaced colonial assemblies with royal appointees.", "That shows regulation that colonists resented, not a benefit."),
       ch("Colonial merchants smuggled goods to the French West Indies.", "Smuggling shows evasion of regulations, not benefit from them."),
       ch("The colonies' protests against the Stamp Act in the 1760s.", "The Stamp Act came later and shows opposition, not benefit.")],
      "Colonial shipbuilding benefited from the protected market created by the Navigation Acts.")

B.mcq(T_AT, "Which development best explains the growing availability of British manufactured goods in the colonies by the mid-1700s?",
      ch("Colonial population growth and rising prosperity expanded the market for British goods and linked colonists to a transatlantic consumer economy.", "More people with more income meant more demand for imported goods from Britain."),
      [ch("Colonial manufacturers had stopped producing goods because of Spanish competition.", "Spain was not a manufacturing competitor in this period."),
       ch("Silver imported from Spanish America made British goods unnecessary.", "Spanish silver did not replace British manufactured goods."),
       ch("Native American trade networks replaced European imports.", "Native trade did not replace European manufactured goods.")],
      "Growth in colonial population and wealth created demand for British imports.")

B.mcq(T_AT, "Which was a consequence of the Glorious Revolution of 1688 for the English colonies?",
      ch("Colonists overthrew the Dominion of New England, and Massachusetts received a new charter in 1691 that based the right to vote on property rather than church membership.", "The Glorious Revolution emboldened colonists to remove Andros, and the new charter changed the basis of political participation in Massachusetts."),
      [ch("Parliament repealed the Navigation Acts.", "The Navigation Acts remained in force."),
       ch("The Crown granted independence to Massachusetts.", "The colonies remained under the Crown."),
       ch("The colonies were placed under the authority of the Church of England.", "The Glorious Revolution did not subject the colonies to the Church of England in this way.")],
      "After the Glorious Revolution the Dominion fell and a new Massachusetts charter extended political participation based on property.")

# ---- Religion and the Enlightenment ----
B.mcq(T_RE, src("A Boston minister, 1740s", "“These traveling preachers stir the passions of common people and turn them against their settled ministers. Religion is a matter of the understanding as well as the heart, and disorder in the church is no sign of the Spirit.”") + "\n\nThe author would most likely have agreed with which of the following?",
      ch("Established clergy should be concerned that emotional revivals undermine their authority and the order of the churches.", "The author, an Old Light, objects to the revivalists' emotional style and their challenge to settled ministers."),
      [ch("Conversion should be understood as an individual emotional experience open to all.", "That is the New Light position that the author is criticizing."),
       ch("Churches should be separated entirely from the colonial government.", "The passage is about order within churches, not church-state separation."),
       ch("Itinerant preachers should replace settled ministers.", "The author opposes the preachers who challenge settled ministers.")],
      "The author represents the Old Light concern about disorder and challenges to established clergy.")

B.mcq(T_RE, "Which of the following best illustrates the influence of Enlightenment ideas in the English colonies before 1754?",
      ch("Benjamin Franklin's scientific experiments, his Poor Richard's Almanack and his promotion of the American Philosophical Society.", "Franklin's work promoted reason, scientific inquiry and practical improvement."),
      [ch("The Salem witch trials of 1692.", "The trials reflected fear and religious anxiety rather than Enlightenment rationalism."),
       ch("The Half-Way Covenant of 1662.", "That concerned church membership in Puritan New England."),
       ch("George Whitefield's open-air revivals.", "Whitefield's revivals were part of the Great Awakening, which stressed emotion and personal faith.")],
      "Franklin's work reflects Enlightenment emphasis on reason and science.")

B.mcq(T_RE, "Which factor most encouraged religious diversity in the Middle Colonies in the early 1700s?",
      ch("Policies of toleration by proprietors such as William Penn, together with the arrival of German, Scots-Irish and other immigrants of different faiths.", "Toleration and varied immigration produced a mix of Quakers, Lutherans, Presbyterians, Catholics and others."),
      [ch("A requirement that all residents belong to a single established church.", "The Middle Colonies did not require uniformity."),
       ch("The expulsion of all non-English settlers.", "The Middle Colonies were diverse and welcomed many nationalities."),
       ch("Spanish missionary work among the colonists.", "Spain's missions were in Florida and the Southwest.")],
      "Toleration and varied immigration encouraged religious diversity.")

# ---- Imperial rivalry and the borderlands ----
B.mcq(T_BO, "Which statement best explains why many Native peoples of the Great Lakes region allied with the French rather than the English in the 1700s?",
      ch("French traders wanted trading partnerships rather than large areas of farmland, so they posed less of a threat to Native land than did English settlers.", "The fur trade made the French dependent on Native partners, while English settlement pressed onto Native lands."),
      [ch("The French had conquered the region and forced Native nations to ally.", "French alliances were largely based on trade and diplomacy rather than conquest."),
       ch("English settlers refused to trade with Native peoples.", "English colonists did trade with Native peoples."),
       ch("The French promised to give Native peoples independence from all European powers.", "The French sought their own interests, not Native independence from all Europeans.")],
      "French fur-trade relations were less threatening to Native land than English settlement.")

B.mcq(T_BO, "New Netherland, established by the Dutch in the 1620s, is best characterized by which of the following?",
      ch("A commercial colony with a diverse population and relative religious toleration, taken by England in 1664 and renamed New York.", "New Netherland was driven by trade and attracted settlers from many backgrounds, and it passed to England in 1664."),
      [ch("A Puritan colony intended as a model Christian community.", "That describes Massachusetts Bay."),
       ch("A colony founded by Spain to protect its treasure fleets.", "That describes Spanish Florida."),
       ch("A royal colony that never traded furs.", "The Dutch colony's economy included the fur trade.")],
      "New Netherland was a diverse commercial colony that became New York in 1664.")

B.mcq(T_BO, "Which of the following best explains the outbreak of the Yamasee War in 1715?",
      ch("Native resentment of abuses by English traders, including debts and the enslavement of Native people, and of settler encroachment on their land.", "Grievances over trade practices, debt and land led many Native peoples to attack the Carolina colony."),
      [ch("Spanish demands for tribute from Native nations in the Carolinas.", "The war was aimed at English colonists, not caused by Spanish demands."),
       ch("A dispute among Native groups over access to French fur markets.", "The war centered on English trade practices in the South."),
       ch("English efforts to convert Native peoples to Catholicism.", "The English colonists were mostly Protestant and the issue was trade and land.")],
      "Trade abuses, debt, enslavement and settler expansion provoked the Yamasee War.")

# ---- Short-answer and long-essay ----
saq(B, T_RE,
    "Use the excerpt to answer parts A, B and C.\n\n" + src("An account of a revival meeting, 1740s", "“The preacher spoke for two hours in the open field, and the people cried out and wept. Merchants stood beside servants, and enslaved men and women listened among the rest. Many who had never entered a church were moved to tears, and some declared that their own ministers had never preached to the heart.”") + "\n\n**a)** Identify ONE way in which the revival described in the excerpt differed from earlier religious practice in the colonies.\n\n**b)** Explain ONE way in which the Great Awakening affected colonial society in the period 1740 to 1754.\n\n**c)** Explain ONE way in which Enlightenment thinking differed from the ideas of the Great Awakening.",
    [(1, "Part A: Identifies a difference such as emotional preaching in open fields, appeal across social ranks, or criticism of settled ministers"),
     (1, "Part B: Explains an effect such as challenging the authority of established clergy, creating new denominations or divisions between New Lights and Old Lights, or building shared colonial experiences"),
     (1, "Part C: Explains that the Enlightenment emphasized reason, science and natural rights, while the Great Awakening emphasized emotion, personal conversion and the authority of scripture")],
    "a) The revival took place outdoors with emotional preaching that attracted people of all ranks, including servants and the enslaved, rather than being limited to church services led by settled ministers.\nb) The Awakening challenged the authority of established clergy, split congregations into New Lights and Old Lights, and created new, more diverse denominations while giving colonists a shared religious experience.\nc) Enlightenment thinkers emphasized reason, science and natural rights as the way to understand the world, while Awakening preachers emphasized emotion and personal conversion.")

leq(B, T_FO,
    "**Long Essay Question**\n\nEvaluate the extent to which religious beliefs, rather than economic goals, shaped the development of the English colonies in North America in the period 1607 to 1754.",
    "A strong response states a defensible thesis, for example that religion shaped New England, Pennsylvania and Maryland most directly, while economic motives dominated the Chesapeake and the Carolinas and eventually shaped all regions through the Atlantic economy. It places the topic in the context of the Protestant Reformation and English expansion, uses specific evidence (Puritan Massachusetts Bay and the banishment of dissenters, Pennsylvania's toleration, Maryland's refuge for Catholics, Virginia's tobacco and the headright system, the Atlantic trade and slavery, the Great Awakening), and uses comparison or causation to weigh religion against economic goals.",
    "Thesis: Presents a defensible thesis that responds to the prompt and evaluates the extent to which religion rather than economics shaped colonial development",
    "Contextualization: Places the topic in a broader context, such as the Protestant Reformation, English religious conflict or the growth of the Atlantic economy",
    "Evidence: Provides at least two specific, accurate pieces of evidence relevant to the prompt (1 point for addressing the topic with evidence, 2nd point for using specific evidence to support the argument)",
    "Analysis and reasoning: Uses comparison or causation to structure the argument (1 point), and demonstrates complex understanding, such as noting that religion and economics interacted, or that motives varied by region and changed over time (2nd point)")

B.save()
B.brief()
