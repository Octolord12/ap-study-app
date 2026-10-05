from common import *

B = bank(3, "unit-3-land-based-empires")
T_EX, T_AD, T_REL, T_CMP = ("empires-expand", "empires-administration", "religion-and-state-power", "comparing-empires")

B.mcq(T_EX, src("A court historian's account of the siege of Constantinople, 1453", "“The great cannon of the Sultan's foundry hurled stones that no wall could withstand. After weeks of bombardment the defenders could no longer hold the breach, and the city that had stood for a thousand years was taken.”") + "\n\nWhich statement best explains the Ottoman success described in the passage?",
      ch("The Ottomans combined gunpowder artillery with a disciplined professional army to overcome strong fortifications.", "Large cannon and the sultan's organized forces, including the Janissaries, allowed Mehmed II to capture a city whose walls had resisted attackers for centuries."),
      [ch("The Ottomans captured the city after an alliance with the Mongol Empire.", "The Mongol Empire had divided centuries before and was not the Ottomans' ally in 1453."),
       ch("The Byzantine emperor surrendered because of a popular revolution inside the city.", "The city fell to a military assault after a siege; there was no revolution."),
       ch("The Ottomans used steam-powered ships to break the blockade.", "Steam power came centuries later.")],
      "The passage emphasizes cannon and bombardment, which together with a professional army explain the victory.")

B.mcq(T_AD, "The Ottoman devshirme system, in which boys from Christian villages in the Balkans were taken into state service, most directly served which purpose?",
      ch("It created a loyal professional military and administrative class, such as the Janissaries, whose members depended on the sultan rather than on hereditary nobility.", "Boys were raised as Muslims and trained for the army and administration, giving the sultan servants with no independent family power base."),
      [ch("It supplied enslaved labor for plantations in the Americas.", "The devshirme served the Ottoman state's military and administration, not American plantations."),
       ch("It selected scholars by written examinations to staff a Confucian-style bureaucracy.", "The devshirme drafted boys; it was not an examination system and was not Confucian."),
       ch("It enforced the conversion of all Muslims to Christianity.", "The system converted the drafted boys to Islam, not the reverse.")],
      "The devshirme created a loyal, professional elite directly dependent on the sultan.")

B.mcq(T_REL, src("Edict of a Mughal emperor, late sixteenth century", "“Let no man be molested on account of his religion, and let anyone be free to follow the faith he prefers. The special tax on those who are not Muslims is abolished, for all my subjects are alike under my protection.”") + "\n\nThe policy described in the passage is best understood as which of the following?",
      ch("An effort to win the loyalty of a diverse population, most of which was not Muslim, by tolerating religious differences.", "Akbar governed a mostly Hindu population and strengthened Mughal rule by tolerance, abolishing the jizya and including Hindus in the administration."),
      [ch("A response to a Hindu revolt that was meant to force all subjects to convert to Islam.", "The passage promotes religious freedom, not forced conversion."),
       ch("A rejection of Islam by the Mughal court in favor of Christianity.", "The Mughal rulers remained Muslim; the policy concerned toleration."),
       ch("A requirement that all subjects follow the same state religion.", "The edict allows each person to follow his own faith.")],
      "The passage reflects a policy of toleration that helped the Mughals rule a religiously diverse empire.")

B.mcq(T_REL, "Which statement describes a major consequence of the rise of the Safavid dynasty in Persia in the early sixteenth century?",
      ch("The Safavids made Twelver Shi'a Islam the state religion, which deepened the religious division between Persia and its Sunni Ottoman neighbors.", "Shah Ismail's establishment of Shi'ism as the state faith shaped Persian identity and added a religious dimension to the Safavid-Ottoman rivalry."),
      [ch("The Safavids adopted Sunni Islam in order to ally with the Ottomans.", "The Safavids were rivals of the Ottomans and promoted Shi'ism, not Sunni Islam."),
       ch("The Safavids converted Persia to Christianity.", "Persia remained Muslim under the Safavids."),
       ch("The Safavids abolished the influence of religion in government and law.", "Religion was central to Safavid rule, which relied on Shi'a clergy and religious legitimacy.")],
      "The Safavids' promotion of Shi'a Islam shaped Persia's identity and its conflicts with the Sunni Ottomans.")

B.mcq(T_EX, "Which statement best explains Russian expansion across Siberia in the sixteenth and seventeenth centuries?",
      ch("Russian rulers, using military force and fortified outposts, extended their authority over a vast, thinly populated region in search of furs and other resources.", "Cossacks and other expeditions pushed east for the lucrative fur trade, building forts and collecting tribute from native peoples."),
      [ch("Russia conquered Siberia from the Ottoman Empire.", "The Ottoman Empire did not control Siberia."),
       ch("Russia expanded into Siberia at the request of the Ming dynasty.", "The Ming did not invite Russian expansion."),
       ch("Russia reached Siberia by sea power in the Pacific Ocean.", "Russian expansion into Siberia was overland, by rivers and land routes.")],
      "Russian expansion was an overland drive for resources, especially furs.")

B.mcq(T_CMP, src("Decree of the Qing court, 1645", "“All men within the realm shall shave their foreheads and wear the queue as the Manchu do. Those who comply are loyal subjects; those who refuse are rebels and shall be punished.”") + "\n\nThis policy is best understood as which of the following?",
      ch("A symbolic demand intended to enforce acceptance of Manchu rule over the Han Chinese majority.", "The queue order made hairstyle a sign of submission to the new dynasty, and resistance to it was treated as rebellion."),
      [ch("An attempt by the Ming dynasty to preserve Han Chinese traditions.", "The decree was issued by the Qing, who replaced the Ming."),
       ch("A fashion that spread voluntarily among Chinese merchants through trade with Europe.", "The decree required compliance and punished refusal."),
       ch("A reform that gave Han Chinese full political equality with the Manchus.", "The Qing maintained a distinction between Manchus and Han Chinese.")],
      "The queue order enforced acceptance of Manchu authority.")

B.mcq(T_CMP, "Which statement best compares the Ottoman and Mughal empires in the sixteenth and seventeenth centuries?",
      ch("Both used gunpowder weapons and governed religiously diverse populations; the Mughals ruled a mostly Hindu population, while the Ottomans allowed religious minorities to manage their own communal affairs through the millet system.", "Both were Muslim-ruled gunpowder empires with diverse subjects, but their circumstances differed in the religious composition of their populations."),
      [ch("The Ottomans ruled a mostly Hindu population and the Mughals ruled the Balkans.", "The Mughals ruled northern India and the Ottomans ruled Anatolia, the Balkans and the Arab lands."),
       ch("Neither used gunpowder weapons, relying instead on traditional cavalry.", "Both used cannon and muskets as important elements of their military power."),
       ch("Both were governed by Confucian bureaucracies chosen through examinations.", "Neither used a Confucian examination system.")],
      "The two empires shared gunpowder warfare and diversity but governed different religious populations.")

B.mcq(T_AD, "The Tokugawa shogunate's requirement that regional lords (daimyo) spend alternate years in the capital Edo, leaving their families there, most directly helped the shogunate to do which of the following?",
      ch("Control powerful regional lords by keeping their families as hostages and draining their resources through the cost of travel and maintaining two residences.", "Alternate attendance (sankin-kotai) reduced the daimyo's capacity to rebel and kept them under the shogun's observation."),
      [ch("Build a unified national army of conscripts from every region.", "The system controlled the lords; it did not create a conscript national army."),
       ch("Encourage the daimyo to found overseas colonies.", "Tokugawa policy limited overseas contacts and did not support colonization."),
       ch("Enforce the adoption of Christianity in the domains.", "The shogunate suppressed Christianity.")],
      "Alternate attendance kept the daimyo under Tokugawa control.")

B.mcq(T_AD, "Which statement best describes the Ottoman millet system?",
      ch("It allowed religious minority communities such as Christians and Jews to manage their own religious and communal affairs under their own leaders, in return for loyalty and taxes.", "The millet system gave recognized religious communities a degree of self-government, which helped the sultans rule a diverse empire."),
      [ch("It required all subjects to convert to Islam to remain in the empire.", "The Ottomans generally did not require conversion; non-Muslims paid special taxes and kept their faiths."),
       ch("It banned non-Muslims from trading and owning property.", "Non-Muslims took part in trade and other economic activity."),
       ch("It guaranteed non-Muslims equal political power in the sultan's government.", "Non-Muslims were protected subjects but were not equal in political rights.")],
      "The millet system gave religious minorities limited self-government.")

B.mcq(T_EX, "A historian argues that gunpowder weapons were important to the rise of the Ottoman, Safavid and Mughal empires. Which evidence would best support this argument?",
      ch("Evidence that rulers used cannon in sieges and musket-armed infantry, which strengthened central authority by making fortified strongholds and local armies less effective.", "Gunpowder weapons favored states with the resources to produce and organize them, helping rulers defeat rivals and fortifications."),
      [ch("Evidence that all three empires banned firearms in their armies.", "These empires embraced firearms, so a ban would contradict the claim."),
       ch("Evidence that all three empires were quickly defeated by nomadic cavalry.", "Such evidence would undermine the argument rather than support it."),
       ch("Evidence that all three empires used steam engines in their factories.", "Steam engines are an eighteenth-century and later development.")],
      "The best evidence shows gunpowder weapons actually strengthening rulers' military and political power.")

B.mcq(T_REL, src("Order issued by a Mughal emperor, 1679", "“It has come to our notice that the tax on those who are not Muslims, abolished in a former reign, shall be collected again, and the officers of the treasury shall see that none escape it.”") + "\n\nThe policy described in the passage was most likely to have which effect?",
      ch("Increased tension with Hindu and other non-Muslim subjects, contributing to unrest and revolts.", "Aurangzeb's reimposition of the jizya reversed the earlier policy of toleration and was resented, adding to opposition within the empire."),
      [ch("Strengthened the loyalty of non-Muslim subjects to the emperor.", "A new tax on non-Muslims was more likely to cause resentment than loyalty."),
       ch("Ended the need for any other taxation in the empire.", "The jizya did not replace other taxes."),
       ch("Led to the immediate conversion of the whole population to Islam.", "Most people remained non-Muslim, and the policy increased opposition.")],
      "Reimposing the tax reversed earlier toleration and increased resentment.")

B.mcq(T_CMP, "How did Qing rulers legitimize their rule over China?",
      ch("They adopted the Confucian bureaucracy and examination system while preserving Manchu identity and military institutions.", "The Qing kept the traditional imperial bureaucracy and Confucian ideology, which helped win elite support, while keeping Manchu military organization and distinct status."),
      [ch("They abolished Confucianism and examinations and governed only through Manchu officers.", "The Qing continued the examinations and used Confucian ideology."),
       ch("They allowed Han Chinese governors to rule independent states.", "The Qing ruled a centralized empire."),
       ch("They abolished the emperor's title and adopted a republic.", "China remained an empire under the Qing until 1912.")],
      "The Qing combined the existing Chinese system of rule with Manchu military and ethnic distinctions.")

B.mcq(T_EX, "Which statement best explains the rise of the Songhai Empire in West Africa in the fifteenth century?",
      ch("Songhai rulers captured trade centers such as Timbuktu and Gao, which gave them control of Saharan commerce, and used cavalry and river fleets to build a large empire after Mali weakened.", "Sunni Ali and later rulers built a large state from control of the trans-Saharan trade and the Niger River."),
      [ch("Songhai defeated the Portuguese navy in the middle of the fifteenth century and took over the Atlantic trade.", "Songhai was an inland Sahel empire, and it did not defeat the Portuguese navy."),
       ch("Songhai was created by the Mongol Empire as a province.", "The Mongols never ruled West Africa."),
       ch("Songhai expanded because it had gunpowder weapons that the Moroccans lacked in 1591.", "In 1591 it was the Moroccans, armed with gunpowder weapons, who defeated Songhai.")],
      "Control of Saharan trade centers and military strength built the Songhai Empire.")

B.mcq(T_CMP, src("Edict of the Tokugawa shogunate, 1630s", "“No Japanese ship shall leave for foreign lands, and no Japanese who has gone abroad shall return on pain of death. Foreign traders shall be confined to the port of Nagasaki, and the teaching of the foreign religion is strictly forbidden.”") + "\n\nWhich purpose is most strongly suggested by the edict?",
      ch("To restrict foreign influence, including Christianity, and preserve the stability of Tokugawa rule.", "The shogunate controlled contacts with outsiders in order to prevent challenges to its authority, which included suppressing Christianity."),
      [ch("To encourage the growth of overseas colonies.", "The edict restricts foreign travel and contact."),
       ch("To expand free trade with all European states.", "Foreign trade was confined to Nagasaki."),
       ch("To convert the Japanese people to Christianity.", "The edict forbids the teaching of the foreign religion.")],
      "The edict reflects a policy of controlling foreign contact to preserve Tokugawa stability.")

B.mcq(T_AD, "The Ottoman timar system granted cavalrymen the right to collect taxes from peasants on state land in return for military service. This system is most similar to which of the following?",
      ch("The exchange of land revenues for military service in medieval European feudal systems.", "Both systems rewarded soldiers with income from land in exchange for armed service."),
      [ch("The Chinese civil service examination system.", "The examination system selected bureaucrats and was unrelated to land grants for military service."),
       ch("The Inca mit'a labor tax.", "The mit'a was a labor obligation of subjects, not a grant of land revenue for soldiers."),
       ch("The use of railroads to move troops.", "Railroads did not exist in the Ottoman Empire's early period.")],
      "The timar resembled the exchange of land revenue for military service in European feudalism.")

saq(B, T_REL,
    "Use the passages to answer parts A, B and C.\n\n" + src("Edict of a Mughal emperor, late sixteenth century", "“Let no man be molested on account of his religion, and let anyone follow the faith he prefers. The special tax on those who are not Muslims is abolished.”") + "\n\n" + src("Order issued by a Mughal emperor, 1679", "“The tax on those who are not Muslims, abolished in a former reign, shall be collected again.”") + "\n\n**a)** Identify ONE difference between the policies described in the two passages.\n\n**b)** Explain ONE reason the first policy helped the Mughal rulers govern their empire.\n\n**c)** Explain ONE way in which another empire from this period, such as the Ottoman or Safavid Empire, dealt with religious diversity or religion as a source of state authority.",
    [(1, "Part A: Identifies that the first policy ended the tax on non-Muslims and promised religious tolerance, while the second reinstated the tax"),
     (1, "Part B: Explains that toleration won the loyalty or cooperation of the large non-Muslim (Hindu) majority and reduced rebellion"),
     (1, "Part C: Explains, for example, that the Ottomans used the millet system to let minorities govern their own religious affairs, or that the Safavids made Shi'a Islam the state religion to unify their state and distinguish it from the Sunni Ottomans")],
    "a) The first passage abolishes the special tax on non-Muslims and allows freedom of religion, while the second reinstates that tax.\nb) The Mughals ruled a population that was mostly Hindu. Religious toleration and the abolition of the tax helped win the loyalty and cooperation of non-Muslim subjects and elites, reducing the likelihood of rebellion.\nc) The Ottomans used the millet system, which let religious minority communities such as Christians and Jews run their own religious and communal affairs under their own leaders in exchange for loyalty and taxes, helping the sultan govern a diverse empire.")

leq(B, T_CMP,
    "**Long Essay Question**\n\nEvaluate the extent to which TWO of the following empires were similar in the methods they used to administer and maintain control of their territories between about 1450 and 1750: the Ottoman Empire, the Mughal Empire, the Qing Empire, the Russian Empire.",
    "A strong response states a thesis about the degree of similarity (for example that the Ottomans and Mughals were similar in using gunpowder weapons, military-service land grants and religious accommodation but different in the religious makeup of their subjects). It places the empires in the context of the rise of centralized, gunpowder-enabled land empires and uses specific evidence (the devshirme and Janissaries, timars and millets; Akbar's toleration, the mansabdari system, the jizya; the Qing examinations and banner system; Peter the Great's reforms). It compares methods and explains reasons for similarities and differences.",
    "Thesis: Presents a defensible thesis that evaluates the extent of similarity in the two empires' methods of administration and control",
    "Contextualization: Describes the broader context of the rise of centralized land empires in this period, such as the effects of gunpowder technology",
    "Evidence: Provides at least two specific, accurate examples for each of the two empires (1 point for addressing the topic, 2nd point for using specific evidence to support the argument)",
    "Analysis and reasoning: Uses comparison to structure the argument (1 point), and demonstrates complexity by explaining reasons for similarities and differences or by qualifying the argument (2nd point)")

B.save()
B.brief()
