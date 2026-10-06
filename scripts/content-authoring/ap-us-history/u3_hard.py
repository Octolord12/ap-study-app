from common import *

B = hard(3)
T_IC, T_RI, T_AC, T_EP, T_FA = ("imperial-crisis", "revolution-and-ideals", "articles-and-constitution", "early-republic-politics", "foreign-affairs-and-frontier")

# ---- The imperial crisis ----
B.mcq(T_IC, src("A historian, late twentieth century", "“The most important result of the British victory in 1763 was not the removal of French power but the removal of the colonists' reason to depend on Britain. Once the French threat was gone, the costs and restrictions of empire looked far less reasonable to those who paid them.”") + "\n\nWhich of the following best supports the historian's argument?",
      ch("With the French removed from Canada and the Ohio Valley, many colonists questioned the need for British troops and resented the taxes and restrictions that Britain imposed.", "Colonists saw less need for imperial protection and objected to paying for it."),
      [ch("Britain's victory made it the leading naval power in the Atlantic.", "That describes British strength but does not show colonial reasons for resentment."),
       ch("The Treaty of Paris of 1763 transferred Florida from Spain to Britain.", "This is a territorial result and says nothing about colonial attitudes toward dependence."),
       ch("Colonial assemblies had long controlled their own internal taxation.", "This explains why colonists resisted Parliament but does not address the effect of French defeat.")],
      "Colonial resentment grew once the French threat disappeared and the costs of empire remained.")

B.mcq(T_IC, "Colonial boycotts of British goods in the 1760s were effective largely because",
      ch("British merchants who depended on colonial markets lobbied Parliament, helping lead to repeal of the Stamp Act and most of the Townshend duties.", "Economic pressure on British merchants carried the colonial case to Parliament."),
      [ch("Parliament responded by granting the colonies representation in the House of Commons.", "Representation was never granted."),
       ch("The boycotts ended all trade with the West Indies, ruining British planters.", "Boycotts targeted British imports and did not end West Indies trade."),
       ch("The boycotts caused Parliament to repeal the Coercive Acts in 1774.", "The Coercive Acts were not repealed in response to boycotts.")],
      "Boycotts pressured British merchants, who pushed Parliament to repeal several measures.")

B.mcq(T_IC, "The Declaratory Act of 1766 is best understood as",
      ch("an assertion that Parliament could legislate for the colonies in all cases, passed as the Stamp Act was repealed.", "Parliament retreated on the Stamp Act but insisted on its supreme authority over the colonies."),
      [ch("a concession granting colonial assemblies the sole power to tax.", "The act asserted parliamentary authority, not colonial taxing power."),
       ch("a treaty with Native nations over western land.", "The act concerned Parliament's authority over the colonies."),
       ch("a declaration of war on France.", "The act had nothing to do with declaring war.")],
      "The Declaratory Act affirmed parliamentary supremacy even as the Stamp Act was repealed.")

# ---- Revolution and ideals ----
B.mcq(T_RI, "Lord Dunmore's Proclamation of 1775, which offered freedom to enslaved people of rebel owners who joined the British, most directly illustrates",
      ch("how the British tried to weaken the Patriots, while exposing the contradiction between Patriot claims to liberty and the practice of slavery.", "The offer drew many enslaved people to British lines and highlighted a tension in the Patriot cause."),
      [ch("a British commitment to abolish slavery throughout the empire.", "The proclamation was a wartime measure aimed at rebels, not a general abolition."),
       ch("unanimous Patriot support for ending slavery.", "Many Patriots were slaveholders and the proclamation angered them."),
       ch("an alliance between Britain and Native nations against the colonies.", "The proclamation addressed enslaved people, not Native alliances.")],
      "The proclamation was a military strategy that exposed contradictions in the Patriot cause.")

B.mcq(T_RI, "Which statement best describes the effect of the Revolutionary War and the Treaty of Paris (1783) on Native Americans?",
      ch("Native nations divided over which side to support, and most were left worse off because the treaty ignored their claims and opened more land to American expansion.", "Native peoples were not consulted in the peace and faced growing pressure from settlers."),
      [ch("Native nations united in support of the Patriots and were rewarded with recognized sovereignty.", "Native nations were divided and were not rewarded with recognition."),
       ch("The treaty guaranteed Native nations control of all land east of the Mississippi River.", "The treaty made no such guarantee."),
       ch("Native peoples gained full citizenship in the new nation.", "Native peoples were not made citizens.")],
      "The war divided Native nations and the peace left them vulnerable to expansion.")

B.mcq(T_RI, "Which factor best explains why several states ended tax support for established churches after the Revolution?",
      ch("Enlightenment ideas about liberty of conscience and the growth of religious diversity, including dissenting Baptists, made official churches harder to defend.", "Revolutionary ideals and pressure from religious minorities led several states to disestablish churches, as in Virginia's Statute for Religious Freedom."),
      [ch("The Constitution required every state to abolish its established church in 1788.", "The First Amendment limited the federal government, and some New England states kept established churches into the 1800s."),
       ch("A decline of religious belief across the new states.", "Religious belief remained strong and grew in the early republic."),
       ch("A British order requiring colonies to end establishments.", "Disestablishment occurred as states acted after independence.")],
      "Enlightenment ideas and religious diversity encouraged disestablishment.")

# ---- From the Articles to the Constitution ----
B.mcq(T_AC, "The Three-Fifths Compromise at the Constitutional Convention reflects which of the following?",
      ch("A bargain between delegates that increased the representation of slaveholding states in Congress and the Electoral College while counting enslaved people as part of the population for that purpose.", "Southern delegates wanted enslaved people counted for representation, and the compromise counted three-fifths of them."),
      [ch("A decision to abolish slavery gradually in all states.", "The Constitution did not abolish slavery."),
       ch("An agreement that enslaved people could vote in federal elections.", "Enslaved people had no political rights."),
       ch("A resolution that equalized representation in the Senate.", "Equal Senate representation resulted from the Great Compromise.")],
      "The compromise gave slaveholding states added power by counting three-fifths of enslaved people.")

B.mcq(T_AC, src("A Federalist essayist, 1788", "“Ambition must be made to counteract ambition. The great security against a gradual concentration of power in one department is to give those who administer each department the means and the motives to resist encroachments by the others.”") + "\n\nThe approach described in the passage is best reflected in which feature of the Constitution?",
      ch("The separation of powers among three branches, with checks and balances among them.", "The author describes giving each branch the means to resist the others, which is the idea behind checks and balances."),
      [ch("The Bill of Rights.", "The Bill of Rights protects individual liberties and is not mainly about balancing branches."),
       ch("The Three-Fifths Compromise.", "That concerns representation and has nothing to do with checks between departments."),
       ch("The equal representation of states in the Senate.", "That reflects the Great Compromise.")],
      "The passage describes separation of powers and checks and balances.")

B.mcq(T_AC, "The Bill of Rights was added to the Constitution in 1791 primarily to",
      ch("address Anti-Federalist demands for explicit protection of individual liberties, which had helped win ratification in several states.", "Several states ratified with the expectation that amendments protecting rights would follow."),
      [ch("give the president authority to veto state laws.", "The Bill of Rights did not expand presidential power in that way."),
       ch("end slavery in the new nation.", "The Bill of Rights did not address slavery."),
       ch("replace the Articles of Confederation.", "The Articles had already been replaced by the Constitution.")],
      "The Bill of Rights answered demands for protection of individual liberties.")

# ---- Politics in the early republic ----
B.mcq(T_EP, src("A historian, late twentieth century", "“Hamilton's financial plan was designed to bind wealthy creditors to the national government by giving them a direct stake in its success.”") + "\n\nWhich of the following best supports the historian's argument?",
      ch("The federal government's assumption of state debts at full value benefited holders of government bonds, many of whom were wealthy investors.", "Repaying bondholders in full tied creditors' fortunes to the new government."),
      [ch("The excise tax on whiskey angered farmers in western Pennsylvania.", "This shows resistance to taxation, not the link between creditors and the national government."),
       ch("Jefferson and Madison formed the Democratic-Republican Party.", "This shows opposition to Hamilton, not support for the historian's claim."),
       ch("Washington warned against permanent foreign alliances.", "The warning concerns foreign policy, not Hamilton's financial plan.")],
      "Assumption at full value benefited wealthy bondholders and linked them to the government.")

B.mcq(T_EP, "President Washington's response to the Whiskey Rebellion of 1794 demonstrated that",
      ch("the national government was willing and able to enforce federal law, including the excise tax, with military force.", "Washington sent a large militia force, showing that the federal government could uphold its authority."),
      [ch("states had the right to nullify federal taxes.", "The federal government rejected resistance to its laws."),
       ch("farmers in the West would be exempt from federal taxes.", "The taxes remained in force."),
       ch("the federal government was too weak to act without state permission.", "The federal government acted on its own authority.")],
      "The government showed it could enforce federal law with force.")

B.mcq(T_EP, "President John Adams's decision in 1799 and 1800 to seek a diplomatic settlement with France most directly",
      ch("ended the Quasi-War but divided the Federalist Party, whose leaders in Hamilton's wing favored a stronger military response.", "The settlement avoided full war and angered Federalists who wanted a tougher policy."),
      [ch("led to a formal declaration of war on France.", "Adams avoided a declaration of war."),
       ch("secured the Louisiana Territory for the United States.", "The United States acquired Louisiana in 1803."),
       ch("united Federalists and Democratic-Republicans behind Adams.", "The decision deepened divisions among Federalists.")],
      "Adams ended the Quasi-War at the cost of splitting his party.")

# ---- Foreign affairs and the frontier ----
B.mcq(T_FA, "The American victory at Fallen Timbers in 1794 led most directly to",
      ch("the Treaty of Greenville of 1795, in which Native nations ceded much of present-day Ohio.", "After defeat, a Native confederacy gave up large territories in the Ohio country."),
      [ch("the withdrawal of the United States from the Ohio Valley.", "The United States expanded into the Ohio country."),
       ch("the recognition of an independent Native nation north of the Ohio River.", "No such nation was recognized."),
       ch("the Louisiana Purchase.", "The purchase came in 1803 and was unrelated to this battle.")],
      "Fallen Timbers led to the Treaty of Greenville and Native land cessions.")

B.mcq(T_FA, src("A Jeffersonian newspaper, 1793", "“Shall we abandon the cause of liberty in the very hour when the French people have broken their chains? Our own revolution was fought for the same principles, and to turn our backs now would be ingratitude.”") + "\n\nThe view expressed in the passage most directly reflects which of the following?",
      ch("Democratic-Republican sympathy for the French Revolution, which contrasted with the Federalist preference for closer ties with Britain.", "Jeffersonians tended to support revolutionary France, while Federalists leaned toward Britain for trade and order."),
      [ch("Federalist support for the policy of neutrality.", "The passage opposes abandoning the French cause."),
       ch("Anti-Federalist opposition to the Constitution.", "The passage concerns foreign policy."),
       ch("A call for the United States to ally with Britain.", "The author sympathizes with France, not Britain.")],
      "The passage reflects Democratic-Republican sympathy for revolutionary France.")

B.mcq(T_FA, "Which provision of the Treaty of Paris of 1783 most directly shaped later westward expansion?",
      ch("Britain recognized American independence and agreed to boundaries reaching the Mississippi River, giving the new nation vast claims in the interior.", "The treaty set the western boundary at the Mississippi, opening the interior to American settlement."),
      [ch("Britain kept control of the land between the Appalachians and the Mississippi.", "The treaty gave that land to the United States."),
       ch("France received the Ohio Valley.", "France was not given the Ohio Valley."),
       ch("Native nations were granted ownership of the Mississippi valley.", "The treaty did not recognize Native ownership.")],
      "The treaty gave the United States claims to land east of the Mississippi.")

# ---- Short-answer and long-essay ----
saq(B, T_EP,
    "Use the excerpt to answer parts A, B and C.\n\n" + src("A Virginia congressman's speech, 1791", "“The Constitution grants no power to charter a bank. If Congress may do whatever it thinks useful, then no limit remains on its power, and the states become mere provinces of a single government.”") + "\n\n**a)** Identify ONE argument made in the excerpt about how the Constitution should be interpreted.\n\n**b)** Explain ONE way in which supporters of the national bank, such as Alexander Hamilton, answered this argument.\n\n**c)** Explain ONE way in which debates like this one contributed to the development of political parties in the 1790s.",
    [(1, "Part A: Identifies the argument that Congress may exercise only powers specifically granted in the Constitution (strict interpretation), or that a broad reading would remove limits on federal power"),
     (1, "Part B: Explains that Hamilton argued for implied powers under the Necessary and Proper Clause, so Congress could create a bank to carry out its financial responsibilities"),
     (1, "Part C: Explains that disagreement over the powers of the national government, the bank and Hamilton's financial program divided supporters into Federalists and Democratic-Republicans")],
    "a) The speaker argues that Congress may do only what the Constitution specifically allows and that a bank is not among its powers, since a broad reading would leave Congress without limits.\nb) Hamilton argued that the Necessary and Proper Clause gave Congress implied powers to take actions, such as creating a bank, that helped carry out its authority over taxes, debt and commerce.\nc) Disputes over strict versus broad interpretation of the Constitution and over Hamilton's financial program divided leaders into Federalists, who favored a stronger national government, and Democratic-Republicans, who favored limited national power.")

leq(B, T_RI,
    "**Long Essay Question**\n\nEvaluate the extent to which the American Revolution represented a break from colonial political and social traditions in the period 1763 to 1800.",
    "A strong response states a defensible thesis, for example that the Revolution broke sharply with monarchy and aristocratic privilege in politics while leaving much of colonial social life, especially slavery and the limited rights of women, largely intact. It places the topic in the context of British imperial reform after 1763 and Enlightenment thought, uses specific evidence (republican state constitutions, the Declaration of Independence, disestablishment of churches, the Constitution, northern emancipation laws, the Three-Fifths Compromise, republican motherhood), and uses continuity and change over time to weigh the Revolution's radical and conservative effects.",
    "Thesis: Presents a defensible thesis that responds to the prompt and evaluates the extent to which the Revolution broke with colonial traditions",
    "Contextualization: Places the topic in a broader context, such as British imperial reform after 1763, the colonial tradition of self-government or Enlightenment ideas",
    "Evidence: Provides at least two specific, accurate pieces of evidence relevant to the prompt (1 point for addressing the topic with evidence, 2nd point for using specific evidence to support the argument)",
    "Analysis and reasoning: Uses continuity and change over time to structure the argument (1 point), and demonstrates complex understanding, such as showing that the Revolution changed politics and religion more than slavery or the status of women (2nd point)")

B.save()
B.brief()
