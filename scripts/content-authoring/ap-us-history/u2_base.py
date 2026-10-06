from common import *

B = base(2)
T_FO, T_SL, T_AT, T_RE, T_BO = ("english-colonies-founding", "slavery-and-labor-systems", "atlantic-economy-and-mercantilism", "religion-and-enlightenment", "imperial-rivalry-and-borderlands")

# ---- Founding the English colonies ----
B.mcq(T_FO, "Jamestown, the first permanent English settlement in North America, was founded in 1607 by",
      ch("a joint-stock company that expected to earn profits for its investors.", "The Virginia Company of London raised money from investors who hoped the colony would return a profit."),
      [ch("Puritans seeking to build a model Christian society.", "Puritans founded Massachusetts Bay in 1630, not Jamestown."),
       ch("Quakers seeking religious freedom under William Penn.", "Pennsylvania was founded in the 1680s."),
       ch("the Dutch West India Company.", "The Dutch founded New Netherland, not Jamestown.")],
      "Jamestown was a commercial venture financed through a joint-stock company.", difficulty="easy")

B.mcq(T_FO, "What most transformed the economy of the Chesapeake colonies by the 1620s?",
      ch("The profitable cultivation of tobacco for export to Europe.", "Tobacco gave Virginia a cash crop, which increased demand for land and labor."),
      [ch("A thriving fur trade with the French.", "The French, not the Chesapeake English, dominated the northern fur trade."),
       ch("The production of rice and indigo.", "Rice and indigo became important later in South Carolina."),
       ch("Large-scale textile manufacturing.", "Textile manufacturing was not a major colonial industry at this time.")],
      "Tobacco gave the Chesapeake a profitable export crop.", difficulty="medium")

B.mcq(T_FO, src("A founding agreement signed by male settlers aboard a ship, early 1620s", "“We who sign below, having come beyond the bounds of any grant we hold, bind ourselves together as a body of loyal subjects. We promise to make such laws and appoint such officers as the good of the colony shall require, and to give them all due obedience.”") + "\n\nThe passage best reflects which of the following?",
      ch("The early development of self-government among English colonists through voluntary agreement.", "The signers create their own rules and officers by mutual consent, illustrating a colonial tradition of self-government."),
      [ch("A belief that political authority rests only on the absolute power of the king.", "The signers base their authority on an agreement among themselves."),
       ch("A rejection of English culture and a call for independence.", "The signers describe themselves as loyal subjects."),
       ch("The direct control of colonial affairs by Parliament.", "The colonists, not Parliament, are creating the rules.")],
      "Voluntary compacts illustrate early self-government among English colonists.", difficulty="medium")

B.mcq(T_FO, "The Puritan founders of Massachusetts Bay in 1630 primarily intended to",
      ch("create a godly community whose reformed Christian society would serve as an example to others.", "Puritans hoped to purify the Church of England by building a model society."),
      [ch("separate completely from the Church of England and withdraw from English society.", "That describes the Separatist Pilgrims at Plymouth more than the Massachusetts Bay Puritans."),
       ch("establish religious toleration for people of all faiths.", "Massachusetts Bay did not practice broad toleration and banished dissenters such as Roger Williams."),
       ch("grow tobacco for export to England.", "Tobacco was the cash crop of the Chesapeake.")],
      "The Puritans sought a model of reformed Christian society, not toleration or tobacco profits.", difficulty="medium")

B.mcq(T_FO, "Which statement best compares the New England and Chesapeake colonies in the 1600s?",
      ch("New England was settled largely by families in religiously centered towns, while the Chesapeake was settled largely by single men seeking profit and living on dispersed plantations.", "New England's families and towns contrasted with the Chesapeake's tobacco economy, many young male servants and scattered farms."),
      [ch("The Chesapeake was settled by religious families in compact towns, while New England relied on plantation agriculture.", "This reverses the two regions."),
       ch("Both regions were settled mainly by Dutch merchants.", "Both were English colonies."),
       ch("Neither region had a significant economy based on agriculture.", "Agriculture was central in both, though in different forms.")],
      "Family-centered, religious New England differed from the profit-driven, male-dominated Chesapeake.", difficulty="hard")

B.mcq(T_FO, "Pennsylvania, founded by William Penn in 1681, was distinctive among the English colonies because it",
      ch("offered religious toleration and attracted settlers of many backgrounds, with Quakers prominent in government.", "Penn's colony welcomed diverse settlers and practiced toleration."),
      [ch("required all settlers to join the Church of England.", "Pennsylvania did not require membership in the Church of England."),
       ch("was governed only by members of a Puritan congregation.", "Puritans governed Massachusetts, not Pennsylvania."),
       ch("banned immigration from outside England.", "Pennsylvania attracted many Germans and others.")],
      "Pennsylvania's toleration and diverse population set it apart.", difficulty="medium")

# ---- Slavery and labor systems ----
B.mcq(T_SL, "Indentured servants in the English colonies were people who",
      ch("agreed to work for a fixed number of years in exchange for passage to America.", "Indentured servants paid for passage with several years of labor and were meant to be freed at the end of their terms."),
      [ch("were enslaved for life and their children after them.", "That describes chattel slavery."),
       ch("were Native Americans forced to work for English colonists.", "Indentured servants were mostly Europeans who contracted to serve."),
       ch("held large tracts of land granted by the Crown.", "Servants generally owned little or no land.")],
      "Indentured servitude was a time-limited labor arrangement exchanged for passage.", difficulty="easy")

B.mcq(T_SL, "Which long-term development is associated with Bacon's Rebellion (1676) in Virginia?",
      ch("Wealthy planters became more worried about a large class of landless former servants and increasingly relied on enslaved Africans for labor.", "The rebellion alarmed elites about unrest among poor freedmen, contributing to a shift toward African slavery."),
      [ch("Virginia abolished slavery.", "Slavery expanded in Virginia after the rebellion."),
       ch("The Crown repealed the Navigation Acts.", "The rebellion did not end the Navigation Acts."),
       ch("Native peoples recovered their lands in Virginia.", "Native peoples lost more land after the rebellion.")],
      "Bacon's Rebellion encouraged planters to turn to African slavery rather than rely on indentured servants.", difficulty="medium")

B.mcq(T_SL, src("A colonial assembly law, 1660s", "“Whereas some doubt has arisen whether a child born of an enslaved mother and a free father shall be bond or free, it is enacted that all children born in this colony shall be bond or free according to the condition of the mother.”") + "\n\nThe law most directly contributed to which development?",
      ch("The growth of hereditary, race-based slavery in the English colonies.", "Making children's status follow the mother's meant enslaved status passed down through generations."),
      [ch("The end of indentured servitude in the colonies.", "Indentured servitude continued for many years after this law."),
       ch("The expansion of political rights for free Black colonists.", "The law restricted freedom, it did not expand rights."),
       ch("The spread of slavery only to New England.", "Slavery spread across many colonies and was not limited to New England.")],
      "Hereditary slavery was written into law, helping entrench racial slavery.", difficulty="medium")

B.mcq(T_SL, "Which statement best explains the growth of slavery in South Carolina in the late 1600s and early 1700s?",
      ch("Planters with ties to Barbados brought slave-based agriculture, and the labor and knowledge of enslaved Africans made rice cultivation profitable.", "Enslaved Africans' labor and skills in rice growing underpinned a plantation economy in which they became a majority along the coast."),
      [ch("The colony's proprietors prohibited slavery, so planters relied on indentured servants.", "South Carolina permitted and expanded slavery."),
       ch("Slavery was introduced there only after the American Revolution.", "Slavery was well established in South Carolina long before the Revolution."),
       ch("Enslaved Africans were used mainly in the fur trade.", "Enslaved Africans worked mainly on plantations and in related labor.")],
      "Barbadian planters and the profitability of rice cultivated by enslaved Africans fueled slavery in the Carolinas.", difficulty="hard")

B.mcq(T_SL, "The Stono Rebellion of 1739 was",
      ch("an uprising of enslaved Africans in South Carolina that led to harsher slave codes.", "The rebellion alarmed planters and was followed by stricter laws controlling enslaved people."),
      [ch("a protest by colonists against taxes imposed by Parliament.", "That describes the later Stamp Act resistance."),
       ch("a revolt of Native peoples against Spanish missions in New Mexico.", "The Pueblo Revolt was in 1680."),
       ch("a rebellion of frontier farmers against the governor of Virginia.", "That describes Bacon's Rebellion in 1676.")],
      "Stono was a slave uprising that was followed by stricter control of enslaved people.", difficulty="medium")

B.mcq(T_SL, "Which statement best compares slavery in the northern and southern colonies by the mid-1700s?",
      ch("In the North enslaved people were fewer and worked as domestic servants, artisans and farm laborers, while in the South slavery was central to large-scale export agriculture.", "Slavery existed in both regions, but only the plantation South was built around it."),
      [ch("Slavery was illegal in all of the northern colonies.", "Slavery was legal and practiced in the northern colonies."),
       ch("Enslaved people in the North were mostly rice workers on large plantations.", "Rice cultivation was concentrated in the South."),
       ch("Slavery was more economically central in New England than in the Chesapeake.", "It was more central to the Chesapeake and the lower South.")],
      "Slavery was widespread but economically central mainly in the South.", difficulty="hard")

# ---- Atlantic economy and mercantilism ----
B.mcq(T_AT, "Mercantilism was an economic theory that held that",
      ch("a nation's power rested on exporting more than it imported, and colonies should supply raw materials and markets for the home country.", "Mercantilist thinking aimed to build national wealth through a favorable balance of trade and controlled colonial commerce."),
      [ch("governments should leave trade entirely unregulated.", "That describes free-market thinking, the opposite of mercantilism."),
       ch("colonies should develop economies fully independent of the home country.", "Mercantilism aimed to keep colonies dependent."),
       ch("wealth comes only from farming and never from trade.", "Mercantilists emphasized trade and a favorable balance of trade.")],
      "Mercantilism sought to enrich the home country through regulated trade and colonial supply.", difficulty="easy")

B.mcq(T_AT, "The Navigation Acts of the mid-1600s required that",
      ch("certain colonial products be shipped on English or colonial vessels and sent through England before going elsewhere.", "The acts regulated colonial trade to benefit England, directing enumerated goods such as tobacco through English ports."),
      [ch("colonists pay a direct tax to Parliament on every legal document.", "That describes the later Stamp Act."),
       ch("colonial merchants trade directly with France and the Netherlands.", "The acts restricted trade with other nations."),
       ch("colonies stop trading with the West Indies.", "The West Indies trade was important and was not ended by the acts.")],
      "The Navigation Acts were mercantilist laws that regulated colonial shipping and trade.", difficulty="medium")

B.mcq(T_AT, src("A Massachusetts merchant's letter, 1730s", "“The laws forbid us to carry our lumber and fish to any port but those of England and her islands. Yet the customs officers are few and poorly paid, and many a cargo goes to the French islands for molasses and returns with no questions asked. We trade where the price is best.”") + "\n\nThe passage best illustrates which of the following?",
      ch("A gap between mercantilist regulations and their enforcement during the period of salutary neglect.", "The merchant describes widespread evasion of trade laws because enforcement was weak."),
      [ch("Full colonial compliance with the Navigation Acts.", "The merchant describes evading the laws."),
       ch("A colonial demand for independence from Britain.", "The merchant complains about regulations but does not call for independence."),
       ch("The repeal of the Navigation Acts.", "The laws still existed; they were just poorly enforced.")],
      "Weak enforcement allowed colonists to trade around mercantilist restrictions.", difficulty="medium")

B.mcq(T_AT, "The Dominion of New England (1686) is best described as",
      ch("an attempt by the Crown to consolidate northern colonies under royal control and tighten enforcement of trade laws, which colonists resisted.", "Royal governor Edmund Andros ruled the Dominion, which curtailed colonial assemblies and was overthrown after the Glorious Revolution."),
      [ch("a Puritan plan to unite the colonies under church leadership.", "The Dominion was imposed by the Crown, not created by Puritan leaders."),
       ch("a military alliance between the colonies and France.", "The Dominion was a political administrative unit, not an alliance with France."),
       ch("a Dutch trading company that controlled the fur trade.", "The Dutch had lost New Netherland to England in 1664.")],
      "The Dominion tried to centralize royal control and was resisted by colonists.", difficulty="medium")

B.mcq(T_AT, "Which statement best describes the Atlantic economy of the 1700s?",
      ch("New England shipping, Caribbean sugar and the slave trade were linked, so northern merchants profited from slavery even in colonies where fewer people were enslaved.", "The Atlantic economy tied the northern and southern colonies and the West Indies together through trade connected to slavery."),
      [ch("The northern colonies had no economic ties to slavery.", "Northern shipping, distilling and trade were closely tied to the slave economy."),
       ch("Native American merchants controlled Atlantic trade.", "European and colonial merchants controlled it."),
       ch("Colonial trade was limited to exchanges between neighboring colonies.", "The colonies were active in transatlantic and Caribbean trade.")],
      "Atlantic trade connected colonial merchants to the slave economy.", difficulty="hard")

B.mcq(T_AT, "Which statement best describes the economy of the Middle Colonies in the 1700s?",
      ch("Fertile farmland produced wheat and other grains that were exported through ports such as Philadelphia and New York.", "The Middle Colonies were known as the bread colonies for their grain exports."),
      [ch("A plantation economy based on rice and indigo dominated.", "That describes South Carolina and Georgia."),
       ch("The economy depended almost entirely on whaling and cod fishing.", "That is more typical of New England."),
       ch("Silver mining for the crown was the leading industry.", "Silver mining was a feature of Spanish America.")],
      "The Middle Colonies exported grain and had diverse economies.", difficulty="medium")

# ---- Religion and the Enlightenment ----
B.mcq(T_RE, "The First Great Awakening was",
      ch("a religious revival of the 1730s and 1740s that emphasized personal religious experience.", "Preachers such as Jonathan Edwards and George Whitefield encouraged emotional, individual conversion."),
      [ch("a Puritan law requiring church membership for voting.", "That was an earlier feature of Puritan Massachusetts, not the Great Awakening."),
       ch("an Enlightenment movement that rejected religion altogether.", "The Awakening was a religious revival, not a rejection of religion."),
       ch("a Spanish campaign to convert Native peoples in Florida.", "The Awakening took place in the English colonies.")],
      "The Great Awakening was an evangelical revival stressing personal faith.", difficulty="easy")

B.mcq(T_RE, "Which was a result of the First Great Awakening?",
      ch("It challenged the authority of established clergy and encouraged religious diversity and shared experiences across the colonies.", "Revivals divided congregations into New Lights and Old Lights and created common experiences among the colonies."),
      [ch("It strengthened the authority of established churches in all colonies.", "The Awakening often undermined established clergy."),
       ch("It ended religious divisions among colonists.", "It created new divisions."),
       ch("It led the colonies to adopt a single official church.", "No single official church was adopted for the colonies.")],
      "The Awakening challenged traditional authority and encouraged religious pluralism.", difficulty="medium")

B.mcq(T_RE, src("A colonial printer's essay, 1730s", "“Reason is the gift of God to every person, and from it we may learn the laws of nature without need of any prince or priest. Government is a compact made for the safety of the governed, and when it fails of that end, the people may change it.”") + "\n\nThe passage most directly reflects which of the following?",
      ch("The Enlightenment emphasis on reason, natural rights and government based on consent.", "The author stresses human reason and government as a compact serving the governed, both Enlightenment ideas."),
      [ch("The Puritan belief that church leaders should govern society.", "The author rejects the need for prince or priest."),
       ch("The belief in the divine right of kings.", "The author says people may change government."),
       ch("The mercantilist view that colonies exist to serve the home country.", "The passage is about political theory, not trade.")],
      "The passage expresses Enlightenment political ideas.", difficulty="medium")

B.mcq(T_RE, "The Half-Way Covenant of 1662 in New England is best understood as a response to",
      ch("concern about declining religious commitment among the children and grandchildren of the first Puritan settlers.", "It allowed the children of baptized members to be baptized even if they had not themselves had a conversion experience."),
      [ch("growing toleration for Quakers in Massachusetts.", "Puritans persecuted Quakers rather than tolerating them."),
       ch("a push to separate church and state in New England.", "The covenant kept church and community closely connected."),
       ch("the arrival of large numbers of Catholic immigrants.", "Catholic immigrants were not the issue here.")],
      "The Half-Way Covenant addressed declining church membership among later generations.", difficulty="hard")

B.mcq(T_RE, "Which statement best explains the Salem witch trials of 1692?",
      ch("Fear, social tensions and religious anxiety in a Massachusetts community under strain from frontier warfare and political uncertainty.", "Historians link the accusations to local conflicts, anxiety about the frontier and the loss of Massachusetts's original charter."),
      [ch("A royal order to suppress Puritan dissent.", "The trials were carried out by colonial authorities, not ordered by the king."),
       ch("The revivals of the First Great Awakening.", "The Great Awakening came decades later."),
       ch("A Spanish attack on New England.", "Spain did not attack New England in 1692.")],
      "Salem reflected social strain and fear in a changing, anxious community.", difficulty="hard")

B.mcq(T_RE, "The 1735 trial of the New York printer John Peter Zenger is significant in the history of freedom of the press because",
      ch("his acquittal supported the idea that printing the truth about officials should not be punished as libel.", "The jury found Zenger not guilty of seditious libel, strengthening later press freedom."),
      [ch("it established that the Crown could censor colonial newspapers.", "The verdict worked against censorship."),
       ch("it led Parliament to pass the Stamp Act.", "The Stamp Act (1765) was unrelated to the Zenger trial."),
       ch("it established that colonial governors could jail their critics without trial.", "The verdict went against the governor's attempt to punish criticism.")],
      "The Zenger verdict supported press freedom and the defense of truth.", difficulty="medium")

# ---- Imperial rivalry and the borderlands ----
B.mcq(T_BO, "What was the primary economic activity of New France?",
      ch("The fur trade, conducted largely through trade with Native peoples.", "French colonists, traders and Native partners exchanged furs and European goods."),
      [ch("Large cotton plantations worked by enslaved labor.", "Cotton plantations became important later in the South."),
       ch("Tobacco farming on dispersed plantations.", "Tobacco was a Chesapeake crop."),
       ch("Commercial grain farming for export to Europe.", "New France's economy depended mainly on furs.")],
      "New France's economy was built on the fur trade.", difficulty="easy")

B.mcq(T_BO, "King Philip's War (1675-1676) was",
      ch("a conflict between New England colonists and Native peoples led by Metacom that devastated both sides and ended Native power in southern New England.", "The war caused heavy losses for colonists and Native peoples, and the Native nations of southern New England were left much weaker."),
      [ch("a war between England and France over control of Canada.", "That was a different type of conflict."),
       ch("a rebellion of Virginia frontier settlers against their governor.", "That was Bacon's Rebellion."),
       ch("a religious conflict between Puritans and Quakers.", "King Philip's War was a conflict with Native peoples.")],
      "King Philip's War was a bloody conflict that broke Native power in southern New England.", difficulty="medium")

B.mcq(T_BO, src("A Native leader in southern New England, 1670s", "“Your people multiply and your cattle trample our corn. You build towns on the ground where our fathers hunted, and your courts judge our people by your laws. We have been patient, but our patience is ended.”") + "\n\nWhich of the following was the most important cause of the conflict reflected in the passage?",
      ch("The expansion of English settlement, which threatened Native land and independence.", "The speaker complains of towns on Native land, trampled crops and English control of justice."),
      [ch("Competition with France over the fur trade.", "The passage concerns English settlers and not the French."),
       ch("Disagreement over the use of enslaved labor.", "The passage does not mention slavery."),
       ch("A desire by Native people to join the Church of England.", "The speaker is opposing English encroachment.")],
      "English expansion onto Native land and authority over Native people drove the conflict.", difficulty="medium")

B.mcq(T_BO, "Which statement about the Pueblo Revolt of 1680 is accurate?",
      ch("Pueblo peoples united to drive the Spanish out of New Mexico in response to forced labor and suppression of their religion, although Spain returned about twelve years later.", "The revolt briefly ended Spanish rule, but the Spanish reconquered the region in 1692."),
      [ch("Spain permanently lost control of New Mexico after the revolt.", "Spain returned in the 1690s."),
       ch("It was led by Spanish settlers against the viceroy.", "It was a Native-led uprising."),
       ch("The Pueblo allied with the English to fight the Spanish.", "The revolt was led by Pueblo peoples without an English alliance.")],
      "The Pueblo Revolt briefly expelled the Spanish, who returned in 1692.", difficulty="medium")

B.mcq(T_BO, "The Iroquois Confederacy's policy of balancing between the English and the French in the early 1700s best illustrates which of the following?",
      ch("Native peoples used diplomacy and European rivalries to protect their own interests.", "The Iroquois often traded with and negotiated with both powers to maintain independence."),
      [ch("The complete military dependence of Native nations on Europeans.", "The Iroquois acted as an independent power."),
       ch("The adoption of European political systems by Native nations.", "The Confederacy maintained its own council-based system."),
       ch("The elimination of Native political independence by 1700.", "The Iroquois remained politically important after 1700.")],
      "Native diplomacy played European powers against one another.", difficulty="hard")

B.mcq(T_BO, "King William's War, Queen Anne's War and King George's War are best understood as",
      ch("North American extensions of European power struggles, in which Native allies fought on several sides.", "These conflicts began in Europe and spread to the colonies, with Native nations allied to both England and France."),
      [ch("disputes among the English colonies over boundaries.", "They were imperial wars, not disputes among colonies."),
       ch("Native campaigns to expel all Europeans from North America.", "Native nations were participants and allies, not the sole actors."),
       ch("civil wars within New France.", "They involved England, France and Native allies.")],
      "These wars were colonial theaters of European conflicts.", difficulty="hard")

# ---- Short-answer questions ----
saq(B, T_SL,
    "Use the excerpt to answer parts A, B and C.\n\n" + src("A historian, late twentieth century", "“In the Chesapeake, the demand for labor in the tobacco fields was met first by indentured servants from England and later increasingly by enslaved Africans. The shift was not inevitable; it came as planters feared the unrest of poor freed servants and as the supply of English servants dwindled.”") + "\n\n**a)** Identify ONE argument made by the historian.\n\n**b)** Explain ONE historical development in the period 1607 to 1754 that contributed to the shift described in the excerpt.\n\n**c)** Explain ONE way in which the growth of slavery shaped colonial society in the period 1607 to 1754.",
    [(1, "Part A: Identifies an argument, such as that the shift to slavery was not inevitable, that planters feared unrest among poor freed servants, or that the supply of English servants fell"),
     (1, "Part B: Explains a development such as Bacon's Rebellion alarming elites, rising English wages reducing migration, or growing access to enslaved Africans through the Atlantic slave trade"),
     (1, "Part C: Explains an effect such as slave codes creating hereditary, race-based slavery, the growth of a plantation economy in the South, or the development of a racial hierarchy in colonial law")],
    "a) The historian argues that planters shifted from indentured servants to enslaved Africans in part because they feared the unrest of freed servants and the supply of English servants fell, and that the shift was not inevitable.\nb) Bacon's Rebellion in 1676 alarmed Virginia's elite about the danger of large numbers of poor, landless former servants, which contributed to a preference for enslaved African labor.\nc) Colonial assemblies passed slave codes that made slavery hereditary and race-based, creating a legal and social hierarchy that shaped the plantation economy of the Chesapeake and the lower South.")

saq(B, T_FO,
    "Use the excerpt to answer parts A, B and C.\n\n" + src("A Massachusetts minister's sermon, 1630s", "“We must remember that the eyes of the world are upon us. If we keep covenant with God and with one another, we shall be an example to all peoples; if we fail, we shall be a warning to them.”") + "\n\n**a)** Identify ONE belief about the purpose of the colony reflected in the excerpt.\n\n**b)** Explain ONE way in which Puritan beliefs shaped New England society in the period 1630 to 1700.\n\n**c)** Explain ONE way in which the founding goals of ANOTHER English colony differed from those of Massachusetts Bay.",
    [(1, "Part A: Identifies a belief such as that the colony should be a model for others or that its success depends on keeping a covenant with God and one another"),
     (1, "Part B: Explains an effect such as town-centered communities, a focus on education and literacy, church membership shaping political rights, or the punishment and banishment of dissenters"),
     (1, "Part C: Explains a difference such as Virginia's commercial, profit-seeking purpose, Pennsylvania's toleration, Maryland's refuge for Catholics, or Rhode Island's separation of church and civil government")],
    "a) The minister believed the colony should be a model Christian society whose success depended on keeping its covenant with God and with one another.\nb) Puritan beliefs led to town-centered communities, an emphasis on literacy so people could read scripture, and laws that tied political participation to church membership while punishing dissenters such as Anne Hutchinson.\nc) Virginia was founded as a commercial venture by a joint-stock company seeking profit, rather than as a religious model community like Massachusetts Bay.")

saq(B, T_AT,
    "Using your knowledge of United States history, answer parts A, B and C.\n\n**a)** Identify ONE way in which the Navigation Acts were intended to benefit England.\n\n**b)** Identify ONE way in which colonists responded to or evaded the Navigation Acts in the period 1650 to 1750.\n\n**c)** Explain ONE reason that the British government enforced its trade regulations loosely in the early 1700s.",
    [(1, "Part A: Identifies a benefit such as keeping colonial trade within the empire, increasing English shipping and customs revenue, or ensuring colonies supplied raw materials"),
     (1, "Part B: Identifies a response such as smuggling, trading with the French West Indies, resisting the Dominion of New England, or ignoring customs officers"),
     (1, "Part C: Explains a reason such as distance and weak enforcement, Britain's focus on wars in Europe, or the benefit Britain gained from colonial growth, often called salutary neglect")],
    "a) The Navigation Acts forced colonial goods to travel through England and on English ships, which increased English shipping, customs revenue and control of raw materials.\nb) Colonial merchants smuggled goods and traded with the French West Indies to avoid restrictions and duties.\nc) Britain's government was distracted by wars and politics in Europe, and since the colonies were growing and profitable, officials allowed lax enforcement, a policy later called salutary neglect.")

B.save()
B.brief()
