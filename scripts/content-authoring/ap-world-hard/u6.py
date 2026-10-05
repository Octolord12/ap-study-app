from common import *

B = bank(6, "unit-6-consequences-of-industrialization")
T_RAT, T_EXP, T_RES, T_ECO, T_MIG = ("rationales-for-imperialism", "imperial-expansion", "resistance-to-imperialism", "global-economic-development", "migration-in-interconnected-world")

B.mcq(T_RAT, src("Speech by a British politician, 1890s", "“It is our duty to carry civilization, Christianity and commerce to the dark places of the earth. The races that cannot yet govern themselves must be guided by those that can, and it is for their own good that we do so.”") + "\n\nThe ideas expressed in the passage were most directly shaped by which of the following?",
      ch("Social Darwinism and the belief that Europeans had a duty to spread their culture to peoples considered less advanced.", "Many imperialists justified expansion with a claimed civilizing mission supported by racial theories and ideas about the survival of the fittest applied to societies."),
      [ch("Marxist ideas about the overthrow of capitalism.", "Marxists criticized imperialism; the passage defends it."),
       ch("The Enlightenment argument that all peoples have equal rights to self-government.", "The passage says some peoples cannot govern themselves, which contradicts that argument."),
       ch("A conviction that colonies were costly and should be abandoned.", "The passage promotes expansion, not abandonment.")],
      "The passage reflects a civilizing mission justified by racial and Social Darwinist ideas.")

B.mcq(T_RAT, "Which economic factor most directly motivated European imperial expansion in Africa and Asia in the late nineteenth century?",
      ch("Industrial economies needed raw materials such as rubber, cotton and minerals, and sought new markets and investment opportunities for their goods and capital.", "Industrialization increased demand for resources and markets, which encouraged states and companies to seek colonies."),
      [ch("The need for new sources of enslaved labor for plantations in the Americas.", "The Atlantic slave trade had largely been abolished by this period."),
       ch("A desire to protect European farmers by closing off all trade.", "Imperialism expanded trade and investment overseas."),
       ch("A shortage of land in Europe that required moving the population to Africa.", "Economic goals focused on resources and markets, and few Europeans settled in most African colonies.")],
      "Industrial demand for raw materials and markets motivated imperialism.")

B.mcq(T_EXP, "The Berlin Conference of 1884-1885 is best understood as which of the following?",
      ch("A meeting at which European powers established rules for dividing African territory among themselves, without African participation.", "The conference set guidelines for claiming territory in Africa, which accelerated the Scramble for Africa."),
      [ch("A negotiation in which African rulers won their independence from Europe.", "African rulers were not represented and independence was not granted."),
       ch("An agreement among all nations to end the slave trade in the Americas.", "The conference concerned partition and trade in Africa."),
       ch("The creation of the League of Nations.", "The League of Nations was created after World War I.")],
      "The conference helped European powers divide Africa without consulting Africans.")

B.mcq(T_EXP, src("Memorial of a Qing official after the First Opium War, 1840s", "“The foreigners have demanded that our ports be opened to their ships and that their subjects be tried only by their own officers. Having lost the war, we must pay a great sum of silver and give up the island, and we are unable to refuse.”") + "\n\nThe situation described in the passage is best understood as which of the following?",
      ch("The imposition of unequal treaties that forced Qing China to open ports and grant privileges to Western powers after a military defeat.", "The Treaty of Nanjing and later agreements opened ports, ceded Hong Kong, required indemnities and granted extraterritorial rights."),
      [ch("A voluntary free-trade agreement among equal partners.", "The passage says the Qing officials were unable to refuse."),
       ch("The tribute system by which foreign states paid tribute to China.", "The passage describes China giving concessions, not receiving tribute."),
       ch("The reforms of the Meiji government in Japan.", "The passage concerns China and its defeat.")],
      "The passage describes unequal treaties imposed after the Opium War.")

B.mcq(T_EXP, "Which statement best compares British rule in India with the Belgian Congo Free State under Leopold II?",
      ch("Both extracted resources for European economies, but the Congo Free State was Leopold's personal possession and became notorious for the brutality of forced labor in rubber collection, which led to an international outcry.", "Leopold's regime in the Congo was exceptionally harsh and was widely condemned, leading Belgium to take over the colony in 1908."),
      [ch("British rule in India was run as the personal possession of a single monarch, while the Congo was governed by a trading company.", "This reverses the situation: the Congo was Leopold's personal possession."),
       ch("Neither colony produced goods for the European market.", "Both were exploited for resources and goods: Indian cotton and tea, Congo rubber and ivory."),
       ch("Both were granted self-government in the nineteenth century.", "Neither was self-governing in the nineteenth century.")],
      "The Congo Free State was a personal possession of Leopold II, and its brutal rule caused an outcry.")

B.mcq(T_EXP, "The Sepoy Rebellion of 1857 in India led most directly to which of the following changes?",
      ch("The British government took direct control of India from the East India Company.", "After the rebellion, the Crown ended Company rule and established the British Raj."),
      [ch("India gained independence in the same year.", "India did not become independent until 1947."),
       ch("The British abolished their rule and returned authority to Mughal emperors.", "The last Mughal emperor was deposed, and British rule was strengthened."),
       ch("The East India Company expanded its control over the entire subcontinent.", "The Company was dissolved as a ruling power.")],
      "The rebellion led to direct Crown rule.")

B.mcq(T_RES, src("A European newspaper report, 1896", "“The army of the Emperor, well led and armed with modern rifles bought abroad, has destroyed the Italian column in the mountains. The conquest of the empire, so confidently announced, has failed.”") + "\n\nWhich factor best explains the outcome described in the passage?",
      ch("Ethiopia had a strong centralized leadership, acquired modern weapons and used military organization and diplomacy effectively.", "Under Emperor Menelik II, Ethiopia secured firearms and unified its forces, defeating Italy at Adwa and preserving its independence."),
      [ch("The Italians were fighting in their own homeland.", "The battle occurred in Ethiopia."),
       ch("Ethiopia was a colony of Britain and was defended by British troops.", "Ethiopia was independent and won with its own army."),
       ch("The Italian army was defeated because it had no firearms.", "The Italian army was armed with modern weapons.")],
      "Ethiopia's modern weapons, leadership and organization defeated Italy.")

B.mcq(T_RES, "Which statement best explains the causes of the Boxer Uprising (1899-1901) in China?",
      ch("It grew out of resentment of foreign influence, Christian missionary activity and the privileges of Western powers, combined with the weakness of the Qing state.", "Boxers attacked foreigners and Chinese Christians in response to foreign domination and economic distress."),
      [ch("It was a movement to support Western modernization led by the Meiji emperor.", "The Boxers were anti-foreign, and the Meiji emperor ruled Japan."),
       ch("It was a revolt by Mughal nobles who wanted to restore Mughal rule in China.", "The Mughals ruled in India, not China."),
       ch("It was a campaign of Qing officials to open more ports to Western trade.", "The Boxers opposed foreign privileges.")],
      "The Boxers reacted against foreign influence and domination.")

B.mcq(T_RES, "Which statement best compares the responses of Japan and China to Western pressure in the second half of the nineteenth century?",
      ch("After the Meiji Restoration, Japan pursued rapid state-sponsored industrialization and military modernization and became an imperial power itself, while the Qing government struggled to carry out reforms and lost control over important rights to foreign powers.", "Japan's centralized reforms strengthened it, while China was hindered by internal rebellions and foreign pressure."),
      [ch("Both countries rejected Western technology completely.", "Japan embraced Western technology and China's reformers adopted some Western methods."),
       ch("Both countries became colonies of Britain.", "Neither Japan nor China became a British colony."),
       ch("China industrialized more quickly than Japan under Qing leadership.", "Japan industrialized more quickly and thoroughly.")],
      "Japan modernized and became an imperial power; China struggled and faced foreign domination.")

B.mcq(T_MIG, src("Terms of a labor contract, 1860s", "“The laborer agrees to work for the planter for a period of five years in return for passage across the sea, a fixed wage, and food and lodging. If the laborer leaves before the end of the term, he shall be returned and punished.”") + "\n\nThe labor system described in the passage most directly developed because of which of the following?",
      ch("The abolition of slavery in many places, which created a demand for cheap contract labor drawn from India and China.", "Planters replaced enslaved workers with indentured laborers, often under harsh conditions."),
      [ch("The rise of medieval guilds that regulated labor.", "Guilds belonged to an earlier period and did not recruit overseas indentured workers."),
       ch("The decline of plantation agriculture.", "Plantation agriculture was expanding and needed workers."),
       ch("The Mongol conquest of Southeast Asia.", "Mongol conquests were centuries earlier.")],
      "Indentured labor developed as a substitute after the abolition of slavery.")

B.mcq(T_ECO, "Which combination of technological developments most directly helped integrate the world economy in the later nineteenth century?",
      ch("Steamships, railroads, the telegraph and canals such as the Suez Canal.", "These innovations lowered the cost and time of moving goods, people and information across the world."),
      [ch("The printing press, the caravel and the compass.", "These were earlier developments."),
       ch("Airplanes, television and the internet.", "These came in the twentieth century."),
       ch("Sailing galleons and horse-drawn caravans.", "These had been in use for centuries and did not mark a new level of integration.")],
      "Steam transport, railroads, the telegraph and canals tied the global economy together.")

B.mcq(T_MIG, "The Chinese Exclusion Act (1882) in the United States and similar laws in other settler societies reflect which broader trend?",
      ch("Growing restrictions on Asian immigration, driven by racial prejudice and fears of competition for jobs.", "Settler societies passed laws to limit Chinese and other Asian immigration."),
      [ch("Governments competing to recruit large numbers of Chinese workers.", "The laws restricted and excluded Chinese immigrants."),
       ch("A ban on emigration issued by the Chinese emperor.", "The act was passed by the United States."),
       ch("An agreement to open all borders to free migration.", "The act did the opposite.")],
      "The act is an example of restrictions on Asian immigration.")

B.mcq(T_MIG, "Which statement best explains the large-scale migration of Europeans to the Americas, Australia and southern Africa in the nineteenth century?",
      ch("Population growth, poverty and famine (such as the Irish famine) pushed people to leave, while opportunities for land and work and cheaper steamship travel drew them to the new lands.", "Both push and pull factors shaped these migrations."),
      [ch("European governments prohibited all emigration, so people left illegally.", "Most European states allowed emigration, which grew substantially."),
       ch("The Mongols forced Europeans to relocate.", "The Mongols were not involved."),
       ch("Europe had a labor shortage, so workers moved to find more laborers.", "Europe had a growing population and, in many areas, a surplus of workers.")],
      "Push and pull factors, including cheaper transport, explain mass migration.")

B.mcq(T_ECO, "Which statement best describes the economic relationship between Latin America and the industrialized nations in the late nineteenth century?",
      ch("Latin American economies exported raw materials and agricultural products such as coffee, beef and nitrates, and depended on foreign investment and imported manufactured goods.", "Many Latin American economies were oriented toward exports for industrial markets and were financed by foreign capital."),
      [ch("Latin America was the leading exporter of manufactured goods to Europe.", "Europe exported manufactured goods to Latin America."),
       ch("Latin American economies were isolated from world trade.", "They were closely linked to world trade."),
       ch("Latin American countries led the world in industrial production.", "Industrial production was concentrated in Europe and the United States.")],
      "Latin American economies were export-oriented suppliers of raw materials.")

B.mcq(T_RAT, src("Report of a colonial administrator, 1900s", "“We have built railways and schools, and the people of this colony have never been so prosperous. They should be grateful for the benefits of our rule.”") + "\n\nWhich perspective would most likely challenge the claim made in the passage?",
      ch("A nationalist from the colony who argued that the railways mainly served to extract resources and strengthen colonial control.", "Anti-colonial writers often argued that colonial infrastructure was built to serve the colonizer's economy rather than local needs."),
      [ch("A shareholder in a company that profited from the colony's exports.", "This person would be likely to support the administrator's claim."),
       ch("A European settler who held land in the colony.", "A settler would likely support colonial rule."),
       ch("A government minister who wanted the colony to remain under imperial control.", "A supporter of imperial control would be likely to agree with the claim.")],
      "A colonized person's perspective would most likely challenge the administrator's claim.")

saq(B, T_EXP,
    "Use the passage to answer parts A, B and C.\n\n" + src("Memorial of a Qing official after the First Opium War, 1840s", "“The foreigners have demanded that our ports be opened to their ships and that their subjects be tried only by their own officers. Having lost the war, we must pay a great sum of silver and give up the island, and we are unable to refuse.”") + "\n\n**a)** Identify ONE concession that the passage says China was forced to make.\n\n**b)** Explain ONE reason that Britain pressed for greater access to the Chinese market in this period.\n\n**c)** Explain ONE way that Chinese people or the Qing government responded to foreign pressure in the second half of the nineteenth century.",
    [(1, "Part A: Identifies a concession such as opening ports, extraterritoriality (trial by foreign officers), paying an indemnity or ceding an island (Hong Kong)"),
     (1, "Part B: Explains a reason such as the trade imbalance in Britain's trade with China, the demand for Chinese tea and silk, the desire for new markets for industrial goods, or the profits of the opium trade"),
     (1, "Part C: Explains a response such as the Self-Strengthening Movement, the Taiping Rebellion, the Boxer Uprising, or the reform proposals of the Hundred Days")],
    "a) The passage says that China had to open its ports to foreign ships, to allow foreigners to be tried by their own officers, to pay a large indemnity and to give up an island (Hong Kong).\nb) Britain bought large amounts of Chinese tea and silk while China wanted little from Britain, creating a trade imbalance. British merchants therefore sold opium to China, and Britain wanted to open the Chinese market to its goods and protect this trade.\nc) Some Qing officials began the Self-Strengthening Movement, which adopted Western weapons and industries to strengthen the state, while others and popular groups responded with rebellions such as the Boxer Uprising, which attacked foreign influence.")

leq(B, T_MIG,
    "**Long Essay Question**\n\nEvaluate the extent to which industrialization changed patterns of global migration in the period 1750-1900.",
    "A strong response takes a position (for example that industrialization greatly increased the scale of migration through population growth, new transportation and demand for labor, while some earlier patterns such as forced migration and labor migration continued). It places the topic in context (population growth, urbanization, the end of the Atlantic slave trade) and uses specific evidence such as migration from Europe to the Americas and Australia, Irish migration during the famine, Indian and Chinese indentured laborers, rural-to-urban migration, and restrictions such as the Chinese Exclusion Act. It analyzes continuity and change and considers causes such as steamships, railroads and the abolition of slavery.",
    "Thesis: Presents a defensible thesis that responds to the prompt and evaluates the extent of change in migration patterns",
    "Contextualization: Describes broader context such as population growth, urbanization or the abolition of the slave trade and slavery",
    "Evidence: Provides at least two specific, accurate examples of migration (such as indentured labor, European migration to settler societies, Irish famine migration, or rural-to-urban migration) and uses them to support the argument",
    "Analysis and reasoning: Uses continuity and change over time to structure the argument (1 point), and shows complexity by explaining varying causes or by noting restrictions and differing experiences of migrants (2nd point)")

B.save()
B.brief()
