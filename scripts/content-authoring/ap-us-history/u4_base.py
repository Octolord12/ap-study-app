from common import *

B = base(4)
T_JW, T_MR, T_JD, T_RR, T_RE = ("jefferson-and-war-of-1812", "market-revolution", "jacksonian-democracy", "religion-and-reform", "regional-economies-and-slavery")

# ---- Jefferson, Louisiana and the War of 1812 ----
B.mcq(T_JW, "The Supreme Court case Marbury v. Madison (1803) is significant because it",
      ch("established the principle of judicial review, the Court's power to declare laws unconstitutional.", "Chief Justice Marshall's opinion asserted that the Court could strike down laws that conflict with the Constitution."),
      [ch("upheld the Alien and Sedition Acts.", "Those acts were not the subject of the case."),
       ch("ended the Bank of the United States.", "The case did not concern the national bank."),
       ch("gave states the power to nullify federal laws.", "The case strengthened the power of the federal judiciary.")],
      "Marbury v. Madison established judicial review.", difficulty="easy")

B.mcq(T_JW, "Jefferson's purchase of the Louisiana Territory in 1803 created a constitutional dilemma because",
      ch("the Constitution did not clearly give the president the power to acquire territory, and Jefferson favored a strict reading of federal powers.", "Jefferson set aside his strict interpretation because the opportunity to double the nation's size seemed too important to lose."),
      [ch("France refused to sell any land to the United States.", "France agreed to sell the entire territory."),
       ch("Congress was unanimous in opposing any expansion.", "Congress approved the treaty."),
       ch("the Constitution forbade treaties with France.", "The Constitution does not prohibit such a treaty.")],
      "Jefferson, a strict constructionist, acted on a power not explicitly granted.", difficulty="medium")

B.mcq(T_JW, src("A New England merchant's petition to Congress, 1808", "“Our ships rot at the wharves and our sailors are without bread. The embargo, meant to punish the nations that molest our commerce, punishes none so severely as ourselves.”") + "\n\nThe passage best reflects which of the following?",
      ch("Opposition, especially in New England, to Jefferson's embargo, which hurt American shipping and trade more than it pressured Britain or France.", "The merchant complains that the embargo damaged American commerce."),
      [ch("Support among merchants for war against Britain.", "The petition complains about the embargo, not a call for war."),
       ch("The success of the embargo in forcing Britain to respect American neutrality.", "The passage describes harm to Americans, not success."),
       ch("The growth of southern cotton exports during the embargo.", "The passage concerns the effects on northern shipping.")],
      "The embargo hurt American commerce and met strong opposition in New England.", difficulty="medium")

B.mcq(T_JW, "Which of the following was a cause of the War of 1812?",
      ch("British impressment of American sailors and restrictions on neutral trade, along with British support for Native resistance on the frontier.", "These grievances led Congress to declare war in 1812."),
      [ch("A British invasion of the Louisiana Territory.", "Britain did not invade Louisiana before the war."),
       ch("A French attack on American ports in 1811.", "The war was fought against Britain."),
       ch("The Hartford Convention of Federalists.", "The Hartford Convention met during the war, not before it.")],
      "Impressment, trade restrictions and frontier tensions brought war with Britain.", difficulty="easy")

B.mcq(T_JW, "Which of the following was a result of the War of 1812?",
      ch("A surge of American nationalism and the discrediting of the Federalist Party after the Hartford Convention.", "The war ended with a sense of national pride, while Federalist opposition to the war damaged the party."),
      [ch("The United States annexed Canada.", "The treaty restored prewar boundaries and the United States did not gain Canada."),
       ch("Britain agreed to pay reparations for impressment.", "The Treaty of Ghent did not provide reparations."),
       ch("The embargo became permanent law.", "The embargo had ended before the war.")],
      "The war encouraged nationalism and ruined the Federalists' reputation.", difficulty="hard")

B.mcq(T_JW, "McCulloch v. Maryland (1819) established that",
      ch("Congress has implied powers to carry out its duties, and federal law is supreme over conflicting state law.", "The Court upheld the national bank and ruled that Maryland could not tax it."),
      [ch("the national bank was unconstitutional.", "The Court upheld the bank."),
       ch("states could tax federal institutions.", "The Court ruled the opposite."),
       ch("Congress could use only powers explicitly listed in the Constitution.", "The Court affirmed implied powers.")],
      "McCulloch v. Maryland affirmed implied powers and federal supremacy.", difficulty="medium")

# ---- The market revolution ----
B.mcq(T_MR, "The Erie Canal, completed in 1825, most directly",
      ch("lowered shipping costs and linked the Great Lakes region to New York City and the Atlantic, encouraging settlement and trade.", "The canal made it cheaper to move goods between the interior and the coast."),
      [ch("connected the Mississippi River to the Pacific Ocean.", "The canal ran across New York State."),
       ch("was built to ship cotton from the Deep South.", "The canal served the northern interior."),
       ch("was financed entirely by the federal government.", "New York State financed it.")],
      "The Erie Canal sharply reduced transportation costs and linked regions.", difficulty="easy")

B.mcq(T_MR, "Eli Whitney's cotton gin, invented in 1793, had which effect?",
      ch("It made cotton processing faster and more profitable, expanding cotton cultivation and increasing demand for enslaved labor.", "Greater profitability encouraged planters to expand cotton acreage and the slave labor that worked it."),
      [ch("It reduced demand for enslaved labor by automating the plantation.", "The gin sped up one step, while the planting and harvesting still required labor, which grew."),
       ch("It ended Southern dependence on slavery.", "It strengthened that dependence."),
       ch("It shifted the South toward manufacturing.", "The South remained agricultural.")],
      "The cotton gin made cotton more profitable and strengthened slavery.", difficulty="medium")

B.mcq(T_MR, src("A young woman's letter from a textile mill, 1840s", "“I rise at five and the bell calls us to the looms until seven in the evening. The pay is good for a farm daughter, and I send part of it home. But the air is thick with lint, and I am not mistress of my own hours.”") + "\n\nThe passage best illustrates which of the following developments?",
      ch("A shift in labor patterns as factory work drew young women from farms into wage labor under strict discipline.", "The writer describes wage labor and strict schedules in a mill."),
      [ch("The growth of slave labor in New England.", "The writer describes wage work, not slavery."),
       ch("A decline in textile manufacturing.", "The passage describes active factory work."),
       ch("A return to self-sufficient family farming.", "The writer left farm life for a mill.")],
      "The passage reflects the growth of factory wage labor.", difficulty="medium")

B.mcq(T_MR, "Which statement best describes a change in many middle-class northern families during the market revolution?",
      ch("Work moved from the household to workplaces outside the home, and an ideal of separate spheres assigned women to the domestic sphere.", "As production shifted away from home, the ideal that men worked outside and women managed the home spread."),
      [ch("Families became more self-sufficient and produced nearly everything they needed.", "The market revolution made families more dependent on the market."),
       ch("Women gained the right to vote in most states.", "Women did not have the right to vote in most states."),
       ch("Children stopped working entirely.", "Children's labor continued in many settings.")],
      "The market revolution reshaped work and gender roles in middle-class families.", difficulty="medium")

B.mcq(T_MR, "Which statement best describes regional economic specialization by the 1840s?",
      ch("The Northeast was industrializing and trading, the Midwest was producing grain and livestock using new transportation links, and the South was concentrating on cotton grown by enslaved labor.", "Each region developed a distinctive economy tied together through trade."),
      [ch("Each region produced nearly all of its own goods.", "The regions specialized and traded."),
       ch("The South led the nation in factory production.", "Industry was concentrated in the Northeast."),
       ch("The West relied on large slave plantations producing cotton.", "The Midwest relied mainly on family farms producing grain and livestock.")],
      "Regional specialization linked North, West and South in a national market.", difficulty="hard")

B.mcq(T_MR, "Large-scale Irish and German immigration in the 1840s contributed to",
      ch("growth of the urban labor force and rising nativist hostility toward immigrants, especially Catholics.", "Many immigrants settled in cities and worked in growing industries, and nativists responded with prejudice and organizing."),
      [ch("the disappearance of nativism.", "Immigration increased nativism."),
       ch("a large shift of immigrants into Southern plantation agriculture.", "Most immigrants settled in the North and Midwest."),
       ch("a decline in urbanization.", "Immigration helped cities grow.")],
      "Immigration fueled urban growth and nativist reactions.", difficulty="hard")

# ---- Jacksonian democracy ----
B.mcq(T_JD, "The spoils system associated with Andrew Jackson refers to",
      ch("the practice of rewarding political supporters with government jobs.", "Jackson's followers received appointments, which critics called the spoils system."),
      [ch("distributing western land to war veterans.", "This describes land bounties, not the spoils system."),
       ch("taxing imported goods to raise revenue.", "That describes tariffs."),
       ch("punishing banks that refused to lend.", "That has no connection to the spoils system.")],
      "The spoils system gave government jobs to political loyalists.", difficulty="easy")

B.mcq(T_JD, "Which development contributed most to the expansion of political participation among white men in the 1820s and 1830s?",
      ch("States dropped property requirements for voting, and parties used conventions and popular campaigns to appeal to voters.", "More white men could vote, and campaigns became more popular."),
      [ch("The Fifteenth Amendment guaranteed the vote to all men.", "That amendment was ratified in 1870."),
       ch("Federal law gave women the right to vote.", "Women gained the vote nationally in 1920."),
       ch("The Electoral College was abolished.", "The Electoral College remained.")],
      "Dropping property requirements and popular campaigning expanded white male participation.", difficulty="medium")

B.mcq(T_JD, src("A Cherokee leader's petition to Congress, 1830s", "“We are a people with our own laws, our own schools and a written language. We have held these lands from time beyond memory. We ask only that treaties be kept and that we be left to live in peace.”") + "\n\nThe passage best illustrates which of the following?",
      ch("Native resistance to removal through legal and political appeals.", "The Cherokee used petitions and lawsuits, appealing to treaties and their established institutions."),
      [ch("Native acceptance of removal as beneficial.", "The petition asks to be left in peace on their lands."),
       ch("Support for the Indian Removal Act.", "The petition opposes removal."),
       ch("A call for armed attack on the United States.", "The petition appeals to treaties and peace.")],
      "The Cherokee resisted removal by legal and political means.", difficulty="medium")

B.mcq(T_JD, "In Worcester v. Georgia (1832), the Supreme Court ruled that",
      ch("Georgia had no authority over Cherokee lands, but President Jackson did not enforce the decision and removal went forward.", "The Court sided with the Cherokee, but the decision was not enforced."),
      [ch("states could remove Native peoples within their borders.", "The Court ruled against state authority over Cherokee territory."),
       ch("the Cherokee were citizens of Georgia.", "The Court did not rule that the Cherokee were citizens."),
       ch("the Cherokee must move west of the Mississippi.", "The decision did not order removal.")],
      "The Court supported Cherokee sovereignty but the ruling was not enforced.", difficulty="medium")

B.mcq(T_JD, "How was the Nullification Crisis of 1832-1833 resolved?",
      ch("Congress passed a compromise tariff that lowered rates while also passing the Force Act authorizing the president to enforce federal law, and South Carolina withdrew its nullification.", "A compromise tariff and a show of federal authority ended the standoff."),
      [ch("South Carolina seceded from the Union.", "South Carolina did not secede in 1833."),
       ch("The federal government accepted the right of states to nullify federal laws.", "Jackson rejected nullification."),
       ch("The Supreme Court upheld nullification.", "The Court did not endorse nullification.")],
      "A compromise tariff and the Force Act ended the crisis.", difficulty="hard")

B.mcq(T_JD, "Jackson vetoed the recharter of the Second Bank of the United States in 1832 mainly because he believed that the bank",
      ch("was a privileged institution that favored wealthy elites over ordinary Americans, and that it was unconstitutional.", "Jackson attacked the bank as a symbol of special privilege."),
      [ch("had too little power to manage the nation's currency.", "Jackson thought the bank had too much power."),
       ch("had been declared illegal in McCulloch v. Maryland.", "McCulloch v. Maryland upheld the bank."),
       ch("was owned entirely by the federal government.", "Private investors owned most of the bank's stock.")],
      "Jackson saw the bank as a privileged institution that favored the wealthy.", difficulty="hard")

# ---- Religion and reform ----
B.mcq(T_RR, "The Second Great Awakening encouraged",
      ch("a belief in individual responsibility for salvation and inspired many reform movements, including abolitionism and temperance.", "Revivalists such as Charles Finney taught that individuals could improve themselves and society."),
      [ch("a rejection of all religion in public life.", "The Awakening increased religious participation."),
       ch("strict control of religion by the federal government.", "The federal government did not control religion."),
       ch("support for the Puritan ideal of an established church.", "The Awakening emphasized personal choice and voluntary churches.")],
      "The Second Great Awakening inspired reform by emphasizing personal responsibility.", difficulty="easy")

B.mcq(T_RR, "William Lloyd Garrison's newspaper The Liberator, begun in 1831, advocated",
      ch("the immediate end of slavery without compensation to slaveholders.", "Garrison demanded immediate abolition and rejected gradual plans."),
      [ch("gradual emancipation with colonization of freed people in Africa.", "That was the program of the American Colonization Society."),
       ch("the expansion of slavery into the western territories.", "Garrison opposed slavery entirely."),
       ch("a compromise that would preserve slavery in the South.", "Garrison refused to compromise.")],
      "Garrison called for immediate abolition.", difficulty="medium")

B.mcq(T_RR, src("A convention declaration, 1848", "“We hold that women are endowed with the same natural rights as men; that laws which deny them the vote and the control of their own property are unjust; and that we are entitled to a share in making the laws we are bound to obey.”") + "\n\nThe passage most directly reflects which of the following?",
      ch("The adaptation of Revolutionary-era ideas of natural rights to demand greater rights for women, as at the Seneca Falls convention.", "The writers apply the language of natural rights and consent to women."),
      [ch("The ideal of republican motherhood.", "The passage demands political rights rather than a domestic role."),
       ch("Opposition to the abolition movement.", "Many women's rights leaders were also abolitionists."),
       ch("Support for a national temperance law.", "The passage concerns voting and property rights.")],
      "The passage adapts natural rights ideas to women's rights.", difficulty="medium")

B.mcq(T_RR, "Horace Mann's reforms in Massachusetts in the 1830s and 1840s promoted",
      ch("common public schools that would educate children from all backgrounds.", "Mann argued that public education would create informed citizens and reduce social divisions."),
      [ch("private schools reserved for wealthy families.", "Mann supported public schools."),
       ch("the closure of schools for girls.", "Mann did not call for closing schools for girls."),
       ch("religious schools run by a state church.", "Mann promoted nonsectarian public schools.")],
      "Mann advocated publicly funded common schools.", difficulty="medium")

B.mcq(T_RR, "Transcendentalists such as Ralph Waldo Emerson and Henry David Thoreau",
      ch("emphasized individualism, self-reliance and the value of nature, and criticized materialism and conformity.", "They argued that people should trust their own conscience and experience."),
      [ch("promoted strict obedience to church authorities.", "They stressed individual conscience over institutional authority."),
       ch("argued that industrial expansion should be the nation's top goal.", "They criticized materialism."),
       ch("championed the Puritan doctrine of predestination.", "Transcendentalism departed from Puritan doctrine.")],
      "Transcendentalists valued individualism and nature over conformity and materialism.", difficulty="hard")

B.mcq(T_RR, "Which statement best explains why many northerners who supported reforms such as temperance and public education still opposed abolitionism?",
      ch("Many feared that abolition would threaten the Union and trade with the South or bring economic competition from freed Black workers, and many held racial prejudice.", "Support for reform did not necessarily mean support for racial equality."),
      [ch("Abolitionism was promoted mainly by Southern slaveholders.", "Abolitionism was led mainly by northerners, including free Black activists, and was condemned in the South."),
       ch("Free Black northerners opposed ending slavery.", "Free Black northerners were among the most active opponents of slavery."),
       ch("The Constitution explicitly forbade antislavery societies.", "The Constitution did not forbid them.")],
      "Fear for the Union, economic concerns and prejudice limited northern support for abolition.", difficulty="hard")

# ---- Regional economies and slavery ----
B.mcq(T_RE, "By the 1830s the dominant export crop of the South was",
      ch("cotton", "Cotton, grown largely by enslaved labor, was the nation's leading export."),
      [ch("indigo", "Indigo was important in colonial South Carolina but declined."),
       ch("wheat", "Wheat was a staple of the Middle Atlantic and Midwest."),
       ch("sugar beets", "Sugar beets were not a major Southern export crop.")],
      "Cotton dominated Southern agriculture and exports.", difficulty="easy")

B.mcq(T_RE, "The domestic slave trade in the early 1800s",
      ch("forcibly moved hundreds of thousands of enslaved people from the Upper South to the Deep South, often breaking up families.", "The expansion of cotton increased demand in the Deep South and fueled this internal trade."),
      [ch("was banned by the Constitution in 1808.", "The ban in 1808 applied to the importation of enslaved people from abroad."),
       ch("mostly moved enslaved people to the North.", "It moved people to the cotton-growing South."),
       ch("ended after the invention of the cotton gin.", "The cotton gin increased demand.")],
      "The domestic slave trade moved large numbers of people to the Deep South.", difficulty="medium")

B.mcq(T_RE, src("A Southern writer, 1840s", "“The enslaved are better provided for than the laborers of Northern factories, who are cast off when sick or old. Slavery is no evil but a positive good, resting upon the natural order of society.”") + "\n\nThe passage reflects which of the following?",
      ch("The proslavery argument that defended slavery as beneficial, which developed in response to the growth of abolitionism.", "Southern defenders increasingly called slavery a positive good."),
      [ch("The view of earlier generations that slavery was a necessary evil.", "The passage calls slavery a positive good, not an evil."),
       ch("Support for gradual emancipation.", "The author defends slavery."),
       ch("The arguments of Northern abolitionists.", "The author is defending slavery.")],
      "The passage expresses the proslavery positive good argument.", difficulty="medium")

B.mcq(T_RE, "Nat Turner's rebellion of 1831 in Virginia",
      ch("alarmed white Southerners and led to stricter laws controlling enslaved and free Black people.", "The uprising increased fear among slaveholders and led to harsher restrictions."),
      [ch("led Virginia to abolish slavery.", "Virginia tightened controls instead."),
       ch("was an uprising of poor white farmers.", "It was led by an enslaved man."),
       ch("was supported by the federal government.", "The federal government did not support the rebellion.")],
      "Turner's rebellion led to harsher slave codes.", difficulty="medium")

B.mcq(T_RE, "Although most white Southerners did not own enslaved people, many supported slavery because",
      ch("slavery shaped the region's economy, social order and racial hierarchy, and many yeoman farmers hoped to become slaveholders or valued the status it gave them.", "The slave system structured Southern society beyond the planter class."),
      [ch("the Constitution required all white Southerners to own at least one enslaved person.", "No such requirement existed."),
       ch("Southern law forced nonslaveholders to vote for proslavery candidates.", "No such law existed."),
       ch("nonslaveholding farmers earned most of their income from cotton plantations.", "Many yeoman farmers practiced subsistence or small-scale farming.")],
      "Slavery shaped the economy and social hierarchy, and many nonslaveholders hoped to gain from it.", difficulty="hard")

B.mcq(T_RE, "Free Black communities in northern cities in the early 1800s",
      ch("built independent institutions such as the African Methodist Episcopal Church while facing discrimination in jobs, schools and voting.", "Free Black northerners created their own churches and organizations in response to exclusion."),
      [ch("enjoyed full legal and social equality with whites.", "They faced widespread discrimination."),
       ch("were barred from forming their own churches.", "They formed independent churches, such as the AME Church."),
       ch("were mostly sent to Africa by state governments.", "Colonization attracted few free Black northerners and was largely opposed by them.")],
      "Free Black communities built institutions in response to discrimination.", difficulty="hard")

# ---- Short-answer questions ----
saq(B, T_MR,
    "Use the excerpt to answer parts A, B and C.\n\n" + src("A historian, early twenty-first century", "“The market revolution did not simply bring prosperity. It divided the nation by region and class: the Northeast into factory and commerce, the West into farms tied to eastern markets by canals and railroads, and the South into plantations that supplied cotton to the world.”") + "\n\n**a)** Identify ONE claim made by the historian.\n\n**b)** Explain ONE development in the period 1800 to 1848 that supports the historian's argument.\n\n**c)** Explain ONE way in which the market revolution affected politics or society in the United States in the period 1800 to 1848.",
    [(1, "Part A: Identifies a claim, such as that the market revolution divided the nation by region and class, or that each region specialized in a different economic activity"),
     (1, "Part B: Explains a development such as canals and railroads linking western farms to eastern markets, factory production in the Northeast, or the cotton boom increasing slavery in the South"),
     (1, "Part C: Explains an effect such as the growth of cities and wage labor, the rise of nativism, changes in family roles, or political conflicts over tariffs, the bank and internal improvements")],
    "a) The historian argues that the market revolution divided the country by region and class, with each region developing a distinct economy.\nb) The Erie Canal and later railroads linked western farms to eastern markets, while the cotton boom in the South expanded plantation slavery to supply textile mills.\nc) The market revolution fueled the growth of cities and wage labor, and debates over tariffs, the national bank and internal improvements became central to national politics.")

saq(B, T_JD,
    "Use the excerpt to answer parts A, B and C.\n\n" + src("A president's veto message, 1832", "“The bank gives special privileges to a few wealthy stockholders at the expense of farmers and laborers. Where the government grants favors to the rich, ordinary citizens have just cause to complain.”") + "\n\n**a)** Identify ONE perspective expressed in the excerpt about the Second Bank of the United States.\n\n**b)** Explain ONE way in which the excerpt reflects broader ideas of Jacksonian democracy.\n\n**c)** Explain ONE consequence of the conflict over the national bank in the 1830s.",
    [(1, "Part A: Identifies the view that the bank favored wealthy stockholders and harmed ordinary citizens"),
     (1, "Part B: Explains that Jacksonian democracy stressed the common man, opposed special privilege and expanded popular influence over government"),
     (1, "Part C: Explains a consequence such as the removal of federal deposits to state banks, the rise of the Whig Party, inflation and the Panic of 1837, or the reelection of Jackson")],
    "a) The president argues that the bank gave special privileges to wealthy stockholders at the expense of ordinary farmers and laborers.\nb) The message reflects Jacksonian democracy's emphasis on ordinary white men and its opposition to special privilege and concentrated economic power.\nc) After the veto, Jackson moved federal deposits to state banks, which encouraged speculation that contributed to the Panic of 1837, and opposition to Jackson helped form the Whig Party.")

saq(B, T_RR,
    "Using your knowledge of United States history, answer parts A, B and C.\n\n**a)** Identify ONE reform movement in the United States in the period 1820 to 1848.\n\n**b)** Identify a SECOND, DIFFERENT reform movement in the same period.\n\n**c)** Explain ONE way in which the Second Great Awakening influenced reform movements in the period 1820 to 1848.",
    [(1, "Part A: Identifies a reform movement such as abolitionism, temperance, women's rights, public education reform or prison and asylum reform"),
     (1, "Part B: Identifies a second, different reform movement from the same list"),
     (1, "Part C: Explains that the Second Great Awakening stressed individual responsibility and the possibility of moral improvement, which motivated people to reform society (for example, evangelical activism in abolitionism and temperance)")],
    "a) The temperance movement sought to reduce or end the consumption of alcohol.\nb) The abolitionist movement sought to end slavery in the United States.\nc) The Second Great Awakening taught that individuals could improve themselves and that Christians had a duty to reform society, which inspired many evangelical Protestants to join movements such as abolitionism and temperance.")

B.save()
B.brief()
