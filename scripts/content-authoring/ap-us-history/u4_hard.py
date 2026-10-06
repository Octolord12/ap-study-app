from common import *

B = hard(4)
T_JW, T_MR, T_JD, T_RR, T_RE = ("jefferson-and-war-of-1812", "market-revolution", "jacksonian-democracy", "religion-and-reform", "regional-economies-and-slavery")

# ---- Jefferson, Louisiana and the War of 1812 ----
B.mcq(T_JW, src("A retired statesman's letter, 1820", "“The debate over Missouri has alarmed me like a bell rung in the night. For now the danger is quieted, but I fear it is only a pause, and that the line drawn between the sections will be drawn again in anger.”") + "\n\nThe concern expressed in the passage most directly reflects which of the following?",
      ch("Fear that disputes over the expansion of slavery would produce lasting sectional conflict that threatened the Union.", "The author expects that the Missouri crisis foreshadows deeper division over slavery between the North and South."),
      [ch("Satisfaction that the Missouri Compromise had permanently settled the slavery question.", "The author describes the calm as only a pause."),
       ch("Alarm that Britain might intervene in the dispute over Missouri.", "The passage concerns a division between sections, not a foreign threat."),
       ch("Anxiety about a financial panic following the end of the War of 1812.", "The passage concerns the sectional debate over Missouri.")],
      "The author fears that the slavery dispute will return and divide the Union.")

B.mcq(T_JW, "Which factor best explains why the Monroe Doctrine of 1823 could be enforced in practice?",
      ch("British naval power, since Britain also opposed new European colonization in the Americas in order to protect its own trade.", "The United States lacked a large navy, but Britain's interests in Latin American markets made it a de facto enforcer."),
      [ch("The United States possessed the strongest navy in the world.", "The United States had a small navy in the 1820s."),
       ch("Spain agreed to withdraw from all of its colonies in the hemisphere.", "Spain did not agree to this."),
       ch("Latin American nations formed a military alliance with the United States.", "No such alliance was formed.")],
      "Britain's navy and trade interests made enforcement of the doctrine possible.")

B.mcq(T_JW, "Henry Clay's American System, proposed after the War of 1812, called for",
      ch("a protective tariff, a national bank and federal spending on internal improvements to strengthen the national economy.", "Clay's program aimed to build an interdependent national economy."),
      [ch("free trade with Britain and the abolition of the national bank.", "The program favored protective tariffs and a national bank."),
       ch("state control of all transportation projects.", "The program called for federal support for internal improvements."),
       ch("a ban on manufacturing in the Northeast.", "The program encouraged manufacturing.")],
      "The American System combined tariffs, a bank and internal improvements.")

# ---- The market revolution ----
B.mcq(T_MR, src("A historian, late twentieth century", "“Canals and railroads tied the farms of the Old Northwest to the Northeast rather than to the South, so that by the 1850s the region's economic connections had shifted away from the Mississippi River.”") + "\n\nWhich of the following best supports the historian's argument?",
      ch("Midwestern farm products increasingly traveled east on the Erie Canal and railroads rather than south on the Mississippi to New Orleans.", "Shifting trade routes tied the Midwest more closely to the Northeast."),
      [ch("Cotton exports from the South to Britain increased in the 1840s.", "That shows Southern trade patterns, not the Midwest's shift."),
       ch("New England mills hired large numbers of immigrant workers.", "That concerns the labor force of northeastern mills."),
       ch("Congress passed the Missouri Compromise.", "That addressed slavery's expansion and not trade routes.")],
      "The eastward shift of Midwestern trade supports the argument.")

B.mcq(T_MR, "Which of the following best explains the Panic of 1837?",
      ch("Land speculation fueled by easy credit from state banks, followed by Jackson's Specie Circular requiring hard money for public land and a downturn in cotton prices and British lending.", "A speculative boom and policies that tightened credit contributed to bank failures and depression."),
      [ch("The recharter of the Second Bank of the United States.", "Jackson vetoed the recharter in 1832."),
       ch("The passage of the Tariff of 1828.", "That tariff was a source of the Nullification Crisis, not the Panic of 1837."),
       ch("The outbreak of the War of 1812.", "The war occurred in 1812-1815.")],
      "Speculation, loose credit, hard-money policy and falling cotton prices contributed to the panic.")

B.mcq(T_MR, "Early labor protests in the 1830s and 1840s, such as the strikes by Lowell mill workers, were most directly a response to",
      ch("wage cuts, longer hours and strict factory discipline.", "Workers protested deteriorating conditions in textile mills."),
      [ch("the elimination of the spoils system.", "The spoils system concerned government jobs, not factory conditions."),
       ch("the passage of the Embargo Act.", "The embargo was an earlier trade measure."),
       ch("a federal ban on women working in factories.", "No such ban existed.")],
      "Workers protested wage cuts and harsher conditions.")

# ---- Jacksonian democracy ----
B.mcq(T_JD, "The charge of a corrupt bargain in the presidential election of 1824 arose because",
      ch("the House chose John Quincy Adams even though Jackson had won more popular and electoral votes, and Adams then named Henry Clay Secretary of State.", "No candidate won an electoral majority, and Jackson's supporters believed Clay's support for Adams was rewarded."),
      [ch("Jackson was disqualified because he was a military officer.", "Jackson was not disqualified."),
       ch("Adams won both the electoral and the popular vote but was accused of fraud.", "Jackson led in both counts."),
       ch("the Supreme Court decided the election.", "The House of Representatives decided it.")],
      "The House's choice and Clay's appointment led Jackson's supporters to allege a corrupt bargain.")

B.mcq(T_JD, src("A historian, early twenty-first century", "“Jacksonian democracy widened the rights of white men while narrowing those of others. Even as property requirements fell, Native peoples were removed from their homelands, free Black men lost the vote in several states, and women remained excluded from politics.”") + "\n\nWhich of the following best supports the historian's argument?",
      ch("States such as Pennsylvania restricted the vote to white men, and the Indian Removal Act forced Native nations to move west.", "These developments show rights for some groups expanding while others lost ground."),
      [ch("Jackson vetoed the recharter of the Second Bank of the United States.", "That concerned economic policy rather than the exclusion of groups."),
       ch("The Erie Canal lowered shipping costs.", "That concerns economic development, not political rights."),
       ch("The Second Great Awakening inspired temperance societies.", "That concerns reform movements and not changes to political rights.")],
      "Restrictions on Black voters and the removal of Native nations support the historian's argument.")

B.mcq(T_JD, "The Whig Party, formed in the 1830s, drew its support primarily from",
      ch("opponents of Jackson who favored an active federal role in the economy, including a national bank, tariffs and internal improvements, and who criticized what they called executive tyranny.", "Whigs united those who objected to Jackson's use of presidential power and favored economic development."),
      [ch("supporters of Jackson who wanted a smaller federal government.", "Those supporters were Democrats."),
       ch("abolitionists who wanted the immediate end of slavery.", "The Whigs were not an abolitionist party."),
       ch("southern planters who wanted to annex Cuba.", "Whig support was not defined by that goal.")],
      "The Whigs opposed Jackson and favored an active national economic program.")

# ---- Religion and reform ----
B.mcq(T_RR, "The migration of Mormons to what is now Utah in 1846-1847 was primarily a response to",
      ch("religious persecution and violent conflict in Missouri and Illinois, which led Brigham Young to lead followers beyond the borders of the United States.", "After the killing of Joseph Smith in 1844, Mormons sought a refuge far from their persecutors."),
      [ch("a federal law requiring Mormons to move west.", "No federal law required the migration."),
       ch("the discovery of gold in California.", "The gold rush began in 1848 and was not the reason for the migration."),
       ch("an order from the Church of England.", "Mormons were a distinct American religious movement.")],
      "Persecution drove the Mormons west to Utah.")

B.mcq(T_RR, "Utopian communities of the antebellum era, such as the Shakers and the Oneida Community, were similar in that they",
      ch("tried to create alternative societies based on communal living and religious or social ideals.", "Both groups experimented with communal organization and distinctive beliefs."),
      [ch("were financed and managed by the federal government.", "These communities were private experiments."),
       ch("were founded mainly in the Deep South.", "They were founded mainly in the North."),
       ch("rejected all forms of shared property.", "Both relied on shared property and communal organization.")],
      "Utopian groups sought to build alternative communal societies.")

B.mcq(T_RR, "The autobiography and speeches of Frederick Douglass strengthened the antislavery movement primarily by",
      ch("providing firsthand testimony of slavery's brutality from someone who had escaped it, which challenged proslavery claims.", "Douglass's eloquence and personal experience gave abolitionists powerful evidence."),
      [ch("persuading Congress to repeal the Fugitive Slave Act in the 1840s.", "No such repeal occurred then."),
       ch("convincing most Southern states to end slavery.", "Southern states did not end slavery because of his work."),
       ch("leading a colonization movement to send freed people to Africa.", "Douglass opposed colonization.")],
      "Douglass's firsthand testimony countered proslavery arguments.")

# ---- Regional economies and slavery ----
B.mcq(T_RE, "Which statement best describes the resistance of enslaved people in the antebellum South?",
      ch("Most resistance took everyday forms, such as working slowly, breaking tools, running away and preserving family and religious life, with armed rebellions being rare.", "Enslaved people resisted in many ways and developed family and community life under slavery."),
      [ch("Armed rebellions were frequent and widespread across the South.", "Armed rebellions were rare and harshly put down."),
       ch("Enslaved people did not resist, because they accepted slavery.", "Enslaved people resisted constantly in many ways."),
       ch("Resistance occurred only in the border states.", "Resistance occurred throughout the slave states.")],
      "Everyday resistance was widespread, while armed rebellions were rare.")

B.mcq(T_RE, "The House of Representatives' gag rule of 1836 to 1844 was adopted in order to",
      ch("prevent consideration of antislavery petitions, which critics said violated the right of petition.", "Southern members tried to suppress debate on slavery, and opponents such as John Quincy Adams fought the rule."),
      [ch("end the importation of enslaved people from Africa.", "That ban took effect in 1808."),
       ch("approve the annexation of Texas.", "The gag rule concerned petitions."),
       ch("protect the rights of free Black voters.", "The rule was aimed at antislavery petitions.")],
      "The gag rule tried to block petitions against slavery.")

B.mcq(T_RE, "The South's heavy dependence on cotton exports tied its economy most closely to",
      ch("British textile manufacturing and northern merchants, shippers and bankers, making the region part of a global economy while limiting its own industrial development.", "Cotton went to mills in Britain and the North, and Northern firms handled shipping and credit."),
      [ch("Spanish silver mines.", "Southern cotton was not tied to Spanish silver mining."),
       ch("Midwestern grain markets.", "Cotton was tied to textile markets, not grain."),
       ch("French wine production.", "Southern cotton was not tied to wine production.")],
      "Cotton connected the South to British mills and northern commerce.")

# ---- Short-answer and long-essay ----
saq(B, T_JD,
    "Use the excerpt to answer parts A, B and C.\n\n" + src("A president's message to Congress, 1830", "“The removal of the Indians beyond the Mississippi will open fertile lands to our citizens, end a cause of conflict between the states and the tribes, and give the Indians a place to live undisturbed under the care of the government.”") + "\n\n**a)** Identify ONE argument made in the excerpt in support of Indian removal.\n\n**b)** Explain ONE way in which Native nations resisted removal in the 1830s.\n\n**c)** Explain ONE effect of the removal policy on Native peoples in the period 1830 to 1848.",
    [(1, "Part A: Identifies an argument such as opening land to white settlers, ending conflict between states and Native nations, or providing Native peoples a place to live under federal protection"),
     (1, "Part B: Explains a form of resistance such as the Cherokee suing in the Supreme Court, petitioning Congress, or the Seminoles fighting a war in Florida"),
     (1, "Part C: Explains an effect such as forced migration on the Trail of Tears with great loss of life, loss of homelands, or disruption of Native societies")],
    "a) The president argues that removal would open fertile land for American citizens and end conflicts between states and Native nations.\nb) The Cherokee Nation challenged removal in the Supreme Court and won in Worcester v. Georgia, and the Seminoles fought the United States in Florida.\nc) Removal forced tens of thousands of Native people to leave their homelands, and many died on journeys such as the Trail of Tears, disrupting their societies and communities.")

leq(B, T_JD,
    "**Long Essay Question**\n\nEvaluate the extent to which Jacksonian democracy expanded democratic participation and ideals in the United States in the period 1824 to 1848.",
    "A strong response states a defensible thesis, for example that Jacksonian democracy greatly expanded political participation among white men but did so while excluding or restricting Native peoples, free Black men, enslaved people and women. It places the topic in the context of the market revolution, the end of property requirements and the decline of the early party system, uses specific evidence (the elimination of property qualifications, party conventions and popular campaigns, the spoils system, the Bank War, the Indian Removal Act, restrictions on free Black voters, the gag rule), and uses continuity and change to weigh expansion against exclusion.",
    "Thesis: Presents a defensible thesis that responds to the prompt and evaluates the extent to which democratic participation and ideals expanded",
    "Contextualization: Places the topic in a broader context, such as the end of the Era of Good Feelings, the market revolution or the rise of the second party system",
    "Evidence: Provides at least two specific, accurate pieces of evidence relevant to the prompt (1 point for addressing the topic with evidence, 2nd point for using specific evidence to support the argument)",
    "Analysis and reasoning: Uses continuity and change over time to structure the argument (1 point), and demonstrates complex understanding, such as showing that expansion for some groups coincided with restrictions on others (2nd point)")

B.save()
B.brief()
