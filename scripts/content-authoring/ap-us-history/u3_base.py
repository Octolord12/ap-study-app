from common import *

B = base(3)
T_IC, T_RI, T_AC, T_EP, T_FA = ("imperial-crisis", "revolution-and-ideals", "articles-and-constitution", "early-republic-politics", "foreign-affairs-and-frontier")

# ---- The imperial crisis ----
B.mcq(T_IC, "Which was a major consequence of the French and Indian War for the British colonies?",
      ch("Britain's large war debt led Parliament to impose new taxes and tighter controls on the colonies.", "To pay for the war and for defending its enlarged empire, Britain turned to colonial taxation and stricter regulation."),
      [ch("France gained control of the Ohio River valley.", "France lost its North American empire east of the Mississippi in the Treaty of Paris of 1763."),
       ch("The colonies won independence from Britain.", "Independence did not come until after the Revolution."),
       ch("Spain took over the thirteen colonies.", "Spain did not gain control of the British colonies.")],
      "Britain's postwar debt and new imperial responsibilities led to new taxes and regulations.", difficulty="easy")

B.mcq(T_IC, "The Proclamation of 1763 was intended to",
      ch("reduce conflict with Native peoples by limiting colonial settlement west of the Appalachian Mountains.", "Britain wanted to avoid costly frontier wars after the French and Indian War by restricting settlement."),
      [ch("encourage rapid settlement of the lands won from France.", "The proclamation restricted settlement rather than encouraging it."),
       ch("punish Boston for the destruction of tea.", "That was the purpose of the Coercive Acts in 1774."),
       ch("end the transatlantic slave trade.", "The proclamation concerned western land, not the slave trade.")],
      "The proclamation limited westward settlement to reduce frontier conflict.", difficulty="medium")

B.mcq(T_IC, src("A colonial pamphlet, 1765", "“Parliament may regulate our commerce, but the money in our purses is ours to give by the voice of our own assemblies. We have no representatives in the House of Commons, and what we have not consented to cannot lawfully be taken from us.”") + "\n\nThe passage best reflects which of the following?",
      ch("Colonial opposition to taxation by a legislature in which colonists had no elected representatives.", "The author argues that taxation requires the consent of representatives the colonists elect."),
      [ch("A demand for immediate independence from Britain.", "The author accepts Parliament's right to regulate trade and does not call for independence."),
       ch("Support for the British doctrine of virtual representation.", "The author rejects the idea that Parliament represents the colonists."),
       ch("Opposition to all British regulation of colonial trade.", "The author concedes Parliament may regulate commerce.")],
      "The passage expresses the principle of no taxation without representation.", difficulty="medium")

B.mcq(T_IC, "How did Parliament respond to the Boston Tea Party of 1773?",
      ch("It passed the Coercive Acts (called the Intolerable Acts by colonists), which closed Boston Harbor and restricted self-government in Massachusetts.", "The acts punished Massachusetts and led other colonies to unite in support of Boston."),
      [ch("It repealed the Tea Act and all other taxes on the colonies.", "Parliament responded with punishment rather than repeal."),
       ch("It offered the colonies seats in the House of Commons.", "Parliament did not offer colonial representation."),
       ch("It apologized to colonists and compensated Boston merchants.", "Parliament demanded payment and imposed penalties.")],
      "Parliament punished Massachusetts with the Coercive Acts.", difficulty="medium")

B.mcq(T_IC, "The British doctrine of virtual representation held that",
      ch("members of Parliament represented the interests of all British subjects, including colonists who had not voted for them.", "British officials argued that colonists were represented in Parliament even without electing members."),
      [ch("colonists should elect their own members to Parliament.", "That was the colonial demand, which Britain rejected."),
       ch("colonial assemblies could override acts of Parliament.", "Britain claimed Parliament's authority was supreme."),
       ch("only property owners in the colonies should be taxed.", "Virtual representation concerned who spoke for the colonists, not property qualifications for taxation.")],
      "Virtual representation was the British argument that Parliament spoke for all subjects.", difficulty="hard")

B.mcq(T_IC, "Why did the Boston Massacre of 1770 matter in the growing conflict between the colonies and Britain?",
      ch("Patriot leaders used it in speeches and prints to build opposition to the presence of British troops and to British policy.", "Accounts of the shooting, such as Paul Revere's engraving, shaped colonial opinion against British rule."),
      [ch("British soldiers were convicted of murder, ending the crisis.", "Most of the soldiers were acquitted after being defended by John Adams."),
       ch("It began the Revolutionary War.", "Open warfare began at Lexington and Concord in 1775."),
       ch("It caused Parliament to repeal the Stamp Act.", "The Stamp Act had been repealed in 1766, before the massacre.")],
      "Patriots used the Boston Massacre to build colonial resistance.", difficulty="medium")

# ---- Revolution and ideals ----
B.mcq(T_RI, "Thomas Paine's pamphlet Common Sense (1776) argued that",
      ch("the colonies should declare independence and form a republic rather than remain under a monarchy.", "Paine's plain language made a powerful case for independence and against monarchy."),
      [ch("the colonies should seek reconciliation with the king.", "Paine argued against reconciliation."),
       ch("Parliament should grant the colonies seats in the House of Commons.", "Paine wanted independence, not representation within the British system."),
       ch("the colonies should form a monarchy of their own.", "Paine rejected monarchy.")],
      "Common Sense argued for independence and republican government.", difficulty="easy")

B.mcq(T_RI, src("A declaration of rights, 1770s", "“We hold that all persons are born with equal claims to life, liberty and the pursuit of happiness; that governments are made to secure these rights; and that when a government becomes destructive of them, the people may alter or abolish it.”") + "\n\nThe passage most directly reflects the influence of which of the following?",
      ch("Enlightenment ideas of natural rights and government by consent.", "The author uses natural rights, consent and a right to change government, all central ideas in Enlightenment political thought."),
      [ch("Mercantilist economic theory.", "The passage is about political rights, not trade."),
       ch("The Puritan belief in a covenant community led by church members.", "The passage does not mention religion or church membership."),
       ch("The doctrine of the divine right of kings.", "The author argues that people may alter or abolish government.")],
      "The passage expresses Enlightenment natural rights ideas.", difficulty="medium")

B.mcq(T_RI, "The American victory at Saratoga in 1777 was significant because",
      ch("it helped persuade France to ally with the United States, providing crucial military and financial support.", "The victory showed that the Americans could win, which encouraged the French alliance of 1778."),
      [ch("it ended the war and forced Britain to recognize independence.", "The war continued until 1781, and Britain recognized independence in 1783."),
       ch("it convinced Spain to cede Florida to the United States.", "Spain did not give Florida to the United States at this time."),
       ch("it ended Loyalist support for Britain in the South.", "Loyalist support in the South continued after Saratoga.")],
      "Saratoga was a turning point because it brought France into the war.", difficulty="medium")

B.mcq(T_RI, "Which statement best describes the Loyalists during the American Revolution?",
      ch("They were a significant minority of the population, and many left the United States after the war.", "Loyalists included many royal officials, merchants and others who remained loyal, and thousands emigrated afterward."),
      [ch("They made up a clear majority of colonists.", "Patriots and Loyalists were both substantial groups, but Loyalists were a minority."),
       ch("They lived only in New England.", "Loyalists were found in all regions."),
       ch("They quickly joined the Patriots when the war began.", "Many Loyalists stayed loyal to Britain throughout the war.")],
      "Loyalists were a significant minority, and many departed after the war.", difficulty="medium")

B.mcq(T_RI, "Which development most clearly shows revolutionary ideals leading to challenges to slavery in the late 1700s?",
      ch("Several northern states, beginning with Vermont in 1777 and Pennsylvania in 1780, abolished slavery or began ending it gradually.", "The language of liberty and rights led northern states to act against slavery, although slavery continued in the South."),
      [ch("The Declaration of Independence abolished slavery in the new nation.", "The Declaration did not abolish slavery."),
       ch("The Articles of Confederation banned slavery in all states.", "The Articles did not ban slavery."),
       ch("Southern states banned slavery in the 1780s.", "Southern states kept slavery, and it grew.")],
      "Northern states moved against slavery, while the South kept and expanded it.", difficulty="hard")

B.mcq(T_RI, "The ideal of republican motherhood that developed after the Revolution held that",
      ch("women could serve the republic by raising virtuous, educated citizens, which supported expanded education for girls.", "The idea gave women a civic role through the family and encouraged more schooling."),
      [ch("women should have the right to vote and hold office.", "Republican motherhood did not extend political rights to women."),
       ch("women should have no education beyond household skills.", "The idea supported the education of girls and women."),
       ch("women's main duty was to support the monarchy.", "The idea concerned service to a republic, not a monarchy.")],
      "Republican motherhood gave women a civic role through raising citizens.", difficulty="hard")

# ---- From the Articles to the Constitution ----
B.mcq(T_AC, "A major weakness of the Articles of Confederation was that Congress",
      ch("lacked the power to levy taxes and to regulate trade between the states.", "Congress could request money from the states but could not tax or regulate commerce directly."),
      [ch("held too much power over the states.", "The central government was weak, not too strong."),
       ch("was led by a strong president who could veto laws.", "The Articles created no president."),
       ch("had the authority to draft citizens into the army.", "Congress had to rely on state militias and requests for troops.")],
      "The Articles gave Congress too little power over taxes and trade.", difficulty="easy")

B.mcq(T_AC, "The Northwest Ordinance of 1787 was significant because it",
      ch("set up a process for admitting new states on equal terms and banned slavery in the Northwest Territory.", "The ordinance created a path to statehood and prohibited slavery north of the Ohio River."),
      [ch("legalized slavery throughout the Northwest Territory.", "It prohibited slavery there."),
       ch("gave Native peoples ownership of the territory.", "The ordinance treated the land as open to American settlement."),
       ch("created the first national bank.", "The national bank was created in the 1790s.")],
      "The ordinance set a precedent for orderly expansion and limited slavery in the territory.", difficulty="medium")

B.mcq(T_AC, src("A Massachusetts farmer's petition, 1786", "“We are taxed to pay the debts of the state, and when we cannot pay in hard money the sheriff takes our farms. The courts will not hear our petitions, and our families go hungry. We ask only that the government not ruin those who bore the war.”") + "\n\nThe conditions described in the passage most directly contributed to which of the following?",
      ch("Calls to strengthen the national government through a new constitution.", "Shays' Rebellion alarmed many leaders, who concluded that the Articles could not maintain order."),
      [ch("The passage of the Alien and Sedition Acts.", "Those laws came in 1798."),
       ch("The ratification of the Bill of Rights.", "The Bill of Rights followed the Constitution in 1791."),
       ch("The Louisiana Purchase.", "That was a land purchase in 1803, unrelated to these grievances.")],
      "Unrest such as Shays' Rebellion strengthened the argument for a stronger national government.", difficulty="medium")

B.mcq(T_AC, "The Great Compromise at the Constitutional Convention resolved a dispute over",
      ch("representation in Congress, by creating a House based on population and a Senate with equal representation for each state.", "Large and small states agreed to a two-house legislature that combined both principles."),
      [ch("whether enslaved people would be counted for representation.", "That was addressed in the Three-Fifths Compromise."),
       ch("how long the president could serve.", "That was not the issue resolved by the Great Compromise."),
       ch("whether to include a bill of rights.", "The Bill of Rights was added after ratification.")],
      "The Great Compromise created a bicameral Congress.", difficulty="medium")

B.mcq(T_AC, src("A Federalist essayist, 1787", "“A large republic, embracing many interests and parties, is less likely than a small one to be ruled by a single faction. The greater the variety of interests, the harder it is for a majority to unite to oppress the rest.”") + "\n\nThe argument in the passage was most often used to defend which of the following?",
      ch("A strong national government over a large and diverse republic.", "The author argues that a large republic is safer against faction, supporting the Constitution's stronger national government."),
      [ch("The sovereignty of the individual states under the Articles of Confederation.", "The argument supports a large republic, not small, sovereign states."),
       ch("A bill of rights added to the Constitution.", "The passage is about the size of the republic and factions, not a bill of rights."),
       ch("A direct democracy conducted in small towns.", "The author argues that small republics are more at risk of faction.")],
      "The argument supports a strong national government over a large republic.", difficulty="hard")

B.mcq(T_AC, "The primary objection of the Anti-Federalists to the Constitution was that it",
      ch("created a central government that was too powerful and lacked a bill of rights protecting individual liberties.", "Anti-Federalists feared distant, concentrated power and demanded explicit protections for rights."),
      [ch("left the national government too weak to defend the country.", "That was the Federalist concern about the Articles."),
       ch("gave the states too much power over national affairs.", "Anti-Federalists feared national power over the states."),
       ch("ended slavery in the new nation.", "The Constitution did not end slavery.")],
      "Anti-Federalists feared a powerful central government without a bill of rights.", difficulty="hard")

# ---- Politics in the early republic ----
B.mcq(T_EP, "Alexander Hamilton's financial program for the new nation included",
      ch("federal assumption of state debts and the creation of a national bank.", "Hamilton aimed to establish national credit and a stable financial system."),
      [ch("the elimination of all federal taxes.", "Hamilton's plan relied on taxes, including tariffs and an excise tax."),
       ch("a default on the national debt.", "Hamilton wanted the debt honored to build credit."),
       ch("a ban on all banking by the federal government.", "Hamilton favored a national bank.")],
      "Hamilton's program assumed state debts and created a national bank.", difficulty="easy")

B.mcq(T_EP, "The Democratic-Republican Party led by Jefferson and Madison opposed Federalist policies mainly because it",
      ch("feared that Hamilton's programs concentrated power in the national government and favored commercial elites over farmers and the states.", "Jeffersonians stressed limited national government and agrarian interests."),
      [ch("wanted a larger national bank and higher tariffs.", "Those were Hamilton's positions."),
       ch("favored a close alliance with Britain.", "Jeffersonians were generally more sympathetic to France."),
       ch("believed the United States should have a monarchy.", "Jeffersonians favored republican government.")],
      "Democratic-Republicans opposed concentrated national power and Hamilton's programs.", difficulty="medium")

B.mcq(T_EP, src("A retiring president's farewell address, 1796", "“The spirit of party serves to distract the public councils and to inflame the passions of the people. As to foreign nations, let us extend our commercial relations but have as little political connection with them as possible, and let us steer clear of permanent alliances with any part of the world.”") + "\n\nWhich statement best describes the foreign policy advice in the passage?",
      ch("The nation should trade widely but avoid permanent political alliances.", "The author recommends commerce with all nations and avoiding entangling alliances."),
      [ch("The nation should ally with France against Britain.", "The author advises against permanent alliances."),
       ch("The nation should expand its influence throughout Latin America.", "The passage does not call for expansion."),
       ch("The nation should aid republican revolutions around the world.", "The author warns against political connections abroad.")],
      "The passage advises commercial ties without permanent alliances.", difficulty="medium")

B.mcq(T_EP, "Jeffersonians criticized the Alien and Sedition Acts of 1798 because the laws",
      ch("restricted criticism of the government and threatened freedom of speech and of the press.", "The Sedition Act criminalized some criticism of the government, which opponents saw as a violation of the First Amendment."),
      [ch("abolished the Federalist Party.", "The acts targeted critics of the government, not the Federalists."),
       ch("encouraged mass immigration from France.", "The acts made it harder for immigrants to become citizens."),
       ch("authorized war against Britain.", "The acts did not authorize war against Britain.")],
      "The acts were seen as an attack on free speech and press.", difficulty="medium")

B.mcq(T_EP, "The Virginia and Kentucky Resolutions of 1798 and 1799 argued that",
      ch("states had the right to judge whether federal laws, such as the Alien and Sedition Acts, were constitutional.", "Madison and Jefferson asserted state authority to judge federal overreach."),
      [ch("the federal courts had the final say on all questions of constitutionality.", "The resolutions challenged national authority rather than affirming it."),
       ch("states should immediately secede from the union.", "The resolutions did not call for secession."),
       ch("the president could set aside laws he considered unwise.", "The resolutions concerned states' power, not presidential power.")],
      "The resolutions claimed state power to judge federal laws.", difficulty="hard")

B.mcq(T_EP, "The presidential election of 1800 is often called the Revolution of 1800 because",
      ch("power passed peacefully from one political party to another after a bitter campaign.", "The Federalists yielded to the Democratic-Republicans without violence, demonstrating that the new system could transfer power peacefully."),
      [ch("the Federalists seized control of the military to remain in office.", "The Federalists accepted the result."),
       ch("the election led to a civil war between the parties.", "The transfer of power was peaceful."),
       ch("a new constitution was adopted after the election.", "The Constitution remained in force.")],
      "The election showed a peaceful transfer of power between parties.", difficulty="hard")

# ---- Foreign affairs and the frontier ----
B.mcq(T_FA, "President Washington's Proclamation of Neutrality in 1793 was a response to",
      ch("the war between Britain and revolutionary France and divisions among Americans over which side to support.", "The proclamation declared that the United States would not take sides."),
      [ch("a Spanish invasion of Louisiana.", "Spain was not invading the United States."),
       ch("the outbreak of Shays' Rebellion.", "Shays' Rebellion occurred in 1786 and 1787."),
       ch("a request from Native nations for an alliance.", "The proclamation concerned war among European powers.")],
      "The proclamation kept the United States neutral in the European war.", difficulty="medium")

B.mcq(T_FA, "Jay's Treaty of 1795 was controversial because",
      ch("it settled disputes with Britain, including British withdrawal from forts in the Northwest, but many Americans thought it gave too much to Britain and ignored the impressment of sailors.", "The treaty avoided war but was seen as favoring Britain."),
      [ch("it declared war on Britain.", "The treaty helped avoid war."),
       ch("it gave the United States the Louisiana Territory.", "The United States acquired Louisiana from France in 1803."),
       ch("it repealed the Alien and Sedition Acts.", "Those acts were passed in 1798, after the treaty.")],
      "Jay's Treaty avoided war with Britain but angered many Americans.", difficulty="medium")

B.mcq(T_FA, src("A Native leader, 1795", "“We have agreed to give up the lands north of the river and to keep the peace. We do not give them gladly. Our towns are burned and our young men have fallen, and we cannot stand against so many.”") + "\n\nThe passage best reflects which of the following developments?",
      ch("The loss of Native land after military defeat as the United States expanded into the Ohio Valley.", "The speaker describes giving up land because of military defeat, as in the Treaty of Greenville of 1795."),
      [ch("Native nations gaining recognition as independent allies of the United States.", "The speaker describes a forced concession."),
       ch("The success of a Native confederacy in stopping American expansion.", "The speaker says his people cannot stand against the Americans."),
       ch("A voluntary sale of Native land for fair payment.", "The speaker says the land is not given gladly.")],
      "The passage reflects forced land cessions after military defeat in the Ohio Valley.", difficulty="medium")

B.mcq(T_FA, "Pinckney's Treaty of 1795 benefited western farmers primarily because Spain",
      ch("agreed to let Americans navigate the Mississippi River and store goods at New Orleans.", "Western farmers depended on the Mississippi to ship goods to market."),
      [ch("ceded Florida to the United States.", "Spain did not cede Florida until 1819."),
       ch("closed the Mississippi River to American shipping.", "The treaty opened the river."),
       ch("granted the United States control of Texas.", "Texas remained part of the Spanish empire.")],
      "Pinckney's Treaty gave Americans access to the Mississippi and New Orleans.", difficulty="hard")

B.mcq(T_FA, "The XYZ Affair of 1797-1798 contributed to",
      ch("an undeclared naval conflict with France and anti-French feeling in the United States.", "French demands for bribes angered Americans and led to the Quasi-War."),
      [ch("an alliance between the United States and France.", "The affair pushed the countries toward conflict."),
       ch("a declaration of war against Spain.", "The affair involved France, not Spain."),
       ch("the purchase of Louisiana.", "The purchase came later, in 1803.")],
      "The XYZ Affair led to the Quasi-War and anti-French sentiment.", difficulty="hard")

B.mcq(T_FA, "Which development most encouraged American settlement west of the Appalachian Mountains in the 1780s and 1790s?",
      ch("Policies that surveyed and sold land, together with military campaigns that forced Native peoples to give up territory.", "The Land Ordinance and Northwest Ordinance, along with treaties after military defeat, opened the Ohio Valley to settlers."),
      [ch("Recognition by Congress of Native nations' ownership of the Ohio Valley.", "Congress treated Native land as available for American settlement."),
       ch("A ban on all western migration by the Constitution.", "The Constitution did not ban migration."),
       ch("Spanish control of the Ohio River.", "Spain did not control the Ohio region.")],
      "Land policy and military pressure on Native peoples encouraged western settlement.", difficulty="medium")

# ---- Short-answer questions ----
saq(B, T_IC,
    "Use the excerpt to answer parts A, B and C.\n\n" + src("A historian, late twentieth century", "“The conflict that led to independence did not begin with a settled love of liberty. It grew out of a quarrel over who held the authority to tax and govern the colonies, and out of a conviction among colonists that Britain was changing the rules after 1763.”") + "\n\n**a)** Identify ONE claim made by the historian.\n\n**b)** Explain ONE development between 1763 and 1775 that supports the historian's argument.\n\n**c)** Explain ONE way in which a factor other than the one emphasized by the historian contributed to the movement toward independence.",
    [(1, "Part A: Identifies a claim, such as that the conflict began over authority to tax and govern or that colonists believed Britain was changing the rules after 1763"),
     (1, "Part B: Explains a development such as the Proclamation of 1763 or the Stamp Act and Townshend duties showing Parliament asserting new taxing authority, and colonial responses such as boycotts or the Stamp Act Congress"),
     (1, "Part C: Explains another factor such as Enlightenment ideas of natural rights, economic interests of merchants and planters, or the spread of Common Sense building support for independence")],
    "a) The historian claims that the conflict grew out of a dispute over who had authority to tax and govern the colonies and over British changes to the rules after 1763.\nb) After the French and Indian War, Parliament passed the Stamp Act in 1765 and the Townshend duties in 1767, asserting its authority to tax the colonies directly, and colonists responded with boycotts and the Stamp Act Congress.\nc) Enlightenment ideas of natural rights and government by consent, spread through pamphlets such as Common Sense, gave colonists a justification for independence beyond disputes over taxes.")

saq(B, T_AC,
    "Use the excerpt to answer parts A, B and C.\n\n" + src("A Virginia farmer's letter, 1788", "“The proposed constitution gives Congress power to raise armies and lay taxes at will, yet it contains no declaration of the rights of the people. Liberty is safe only when government is close to the people and bound by written limits.”") + "\n\n**a)** Identify ONE concern expressed in the excerpt about the proposed Constitution.\n\n**b)** Explain ONE way in which supporters of the Constitution responded to concerns such as those in the excerpt.\n\n**c)** Explain ONE outcome of the debate over ratification.",
    [(1, "Part A: Identifies a concern such as the broad powers of Congress to raise armies and levy taxes or the lack of a bill of rights"),
     (1, "Part B: Explains a response such as the Federalist Papers arguing that checks and balances and a large republic would protect liberty, or promises to add a bill of rights"),
     (1, "Part C: Explains an outcome such as ratification of the Constitution in 1788, or the adoption of the Bill of Rights in 1791")],
    "a) The writer is concerned that Congress has too much power to raise armies and levy taxes and that the Constitution lacks a declaration of individual rights.\nb) Supporters such as Madison, Hamilton and Jay argued in the Federalist Papers that separation of powers and checks and balances would prevent tyranny, and some promised to add a bill of rights after ratification.\nc) The Constitution was ratified in 1788, and in 1791 the first ten amendments, the Bill of Rights, were added to protect individual liberties.")

saq(B, T_RI,
    "Using your knowledge of United States history, answer parts A, B and C.\n\n**a)** Identify ONE way in which the ideals of the American Revolution led to political change in the new states and nation between 1776 and 1800.\n\n**b)** Identify ONE way in which the American Revolution had limited effects on the rights of enslaved people or women.\n\n**c)** Explain ONE way in which revolutionary ideals were used to challenge slavery in the period 1775 to 1800.",
    [(1, "Part A: Identifies a change such as new state constitutions based on popular sovereignty, expanded voting rights in some states, or Virginia's Statute for Religious Freedom"),
     (1, "Part B: Identifies a limit such as the Constitution protecting slavery through the Three-Fifths Compromise and the fugitive slave clause, or women's continued exclusion from voting and public office"),
     (1, "Part C: Explains an example such as northern states abolishing slavery or beginning gradual abolition, enslaved people petitioning for freedom using the language of rights, or the growth of antislavery societies")],
    "a) The new states wrote constitutions that rested on the authority of the people, and Virginia passed a Statute for Religious Freedom separating church from state.\nb) Although revolutionary ideals spoke of liberty and equality, the Constitution protected slavery through the Three-Fifths Compromise and the fugitive slave clause, and women remained unable to vote or hold office.\nc) Enslaved people in Massachusetts petitioned for freedom using the language of natural rights, and several northern states, including Pennsylvania in 1780, passed laws that gradually ended slavery.")

B.save()
B.brief()
