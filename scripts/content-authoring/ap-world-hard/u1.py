from common import *

B = bank(1, "unit-1-global-tapestry")
T_EA, T_DAI, T_SA, T_AA, T_EU = ("east-asian-states", "dar-al-islam", "south-and-southeast-asia", "state-building-americas-africa", "european-christendom")

B.mcq(T_EA, src("Report of a prefectural magistrate, Song dynasty China, written for the court", "“Of the thirty candidates our prefecture sent to the capital examination this year, twenty-six came from households holding more than a hundred mu of land. Poor scholars seldom have the leisure, or the tutors, to prepare for ten years.”") + "\n\nWhich statement about the Song civil service examination system is best supported by the passage?",
      ch("The examinations created a scholar-official class chosen by testing rather than birth, although wealth gave candidates a major advantage.", "The examinations were open in principle and produced officials whose status came from learning, but the cost of preparation meant that landowning families dominated success, as the magistrate reports."),
      [ch("The examinations had replaced the influence of wealth and family with a system open on equal terms to all social classes.", "The passage shows the opposite: most successful candidates came from landowning households because they could afford years of preparation."),
       ch("The state barred landowners from taking the examinations in order to prevent corruption.", "Landowning families were not excluded; the passage shows they were the main group passing the examinations."),
       ch("Buddhist monasteries controlled which candidates were allowed to take the examinations.", "The examinations were run by the imperial government and tested Confucian learning; monasteries had no such control.")],
      "The passage supports a qualified claim: the exams selected officials by learning, but access to that learning depended on wealth.")

B.mcq(T_EA, "Which statement best compares the political systems of Kamakura Japan (1185-1333) and feudal western Europe?",
      ch("In both, regional warrior elites held power through bonds of land and military service, while the nominal supreme ruler had limited direct authority.", "In Japan the emperor remained in the background while the shogun and warrior vassals (samurai) held real power; in western Europe kings relied on nobles and vassals who held land in return for military service."),
      [ch("In Japan, power was concentrated in a strong emperor, whereas in Europe it was divided among local lords.", "This reverses the situation: in Kamakura Japan the emperor was a figurehead and the shogun's government (the bakufu) held military and political power."),
       ch("Both relied on a bureaucracy of officials chosen by examination to govern the countryside.", "Examination-selected bureaucracies characterized China, not feudal Japan or feudal Europe."),
       ch("Neither society had a distinct warrior class, because both depended on conscript peasant armies.", "Both societies were dominated by a warrior aristocracy: samurai in Japan and knights in Europe.")],
      "Both were decentralized, with power held by local warriors whose loyalty was tied to land and service.")

B.mcq(T_DAI, src("A Cairo chronicler, 1260", "“The host that destroyed Baghdad was met in Palestine by the army of the Sultan, and for the first time its advance was broken. The people of Egypt gave thanks, for it was said that nothing could stop the Mongols.”") + "\n\nThe event described most directly contributed to which development?",
      ch("The survival of the Mamluk Sultanate in Egypt as a leading Islamic power, and a limit on Mongol expansion westward.", "The Mamluks defeated a Mongol force at Ain Jalut in 1260, protecting Egypt and halting the Mongol advance in the eastern Mediterranean."),
      [ch("The Mongol conquest of Egypt and the whole of North Africa.", "The Mongols did not conquer Egypt; the passage describes their advance being broken."),
       ch("The collapse of Mongol rule in China.", "The Yuan dynasty of the Mongols ruled China until 1368; this battle in the Middle East did not end it."),
       ch("The immediate conversion of the Mongol rulers of Persia to Christianity.", "The Ilkhanate rulers in Persia eventually converted to Islam, not Christianity, and not as a direct result of this battle.")],
      "The battle checked the Mongols, leaving Egypt under Mamluk rule.")

B.mcq(T_SA, "Which statement best explains the spread of Islam in South Asia between 1200 and 1450?",
      ch("The political power of Muslim rulers, together with the work of Sufi mystics and merchants, led many people to convert gradually, while most of the population remained non-Muslim.", "Muslim states such as the Delhi Sultanate provided political backing, and Sufi teachers and traders spread the religion over time, but Hindus remained the majority."),
      [ch("Muslim rulers forced the entire population of the subcontinent to convert.", "Conversion was gradual and partial; most people in South Asia stayed Hindu, and many rulers relied on non-Muslim subjects."),
       ch("Islam spread mainly because the Gupta Empire adopted it as its state religion.", "The Gupta Empire had declined by about 550 CE, long before this period, and was Hindu."),
       ch("Hindu kings of the powerful Vijayanagara Empire adopted Islam as their official religion.", "Vijayanagara (founded 1336) was a Hindu kingdom in southern India that resisted Muslim sultanates.")],
      "Islam's spread combined political patronage, Sufi missionary activity, and trade, but did not displace the Hindu majority.")

B.mcq(T_AA, src("A Cairo official, early fourteenth century", "“When the king of Mali came to Cairo on pilgrimage, he gave out so much gold that its value fell in the markets and did not recover for many years. His followers numbered in the thousands.”") + "\n\nThe passage best illustrates which of the following about Mali?",
      ch("Its wealth, based on gold, connected it to the wider Islamic world and Mediterranean commerce.", "Mali's rulers profited from the gold trade across the Sahara, and the king's pilgrimage to Mecca through Cairo (Mansa Musa's in 1324-1325) tied Mali to Muslim lands."),
      [ch("Its economy depended mainly on maritime trade across the Indian Ocean.", "Mali was in the West African Sahel; its wealth depended on gold and salt trade across the Sahara, not on Indian Ocean shipping."),
       ch("Its armies had recently been defeated by Moroccan forces armed with gunpowder weapons.", "The Moroccan conquest of the Songhai Empire, which succeeded Mali, came in 1591, much later than this passage."),
       ch("Its rulers had adopted Christianity after contact with Ethiopian traders.", "Mali's rulers were Muslim, which is why the king made the pilgrimage described.")],
      "The passage shows Mali's gold wealth and its place in Islamic and trans-Saharan networks.")

B.mcq(T_AA, "Excavations at Great Zimbabwe have uncovered Chinese porcelain, Persian pottery and glass beads. Which conclusion do these finds best support?",
      ch("Great Zimbabwe took part in Indian Ocean trade through the Swahili coastal cities.", "Gold and ivory from the interior moved to coastal ports, and goods from Asia came back; the imported objects show that the Shona state was linked to these networks."),
      [ch("Great Zimbabwe was a colony ruled by Portuguese merchants.", "The Portuguese arrived on the East African coast only around 1500, after Great Zimbabwe's peak."),
       ch("Great Zimbabwe controlled the trans-Saharan caravan routes.", "Great Zimbabwe lay in southeastern Africa, far from the Sahara; its trade ran toward the Indian Ocean coast."),
       ch("Great Zimbabwe was built by Arab architects working for the Mali Empire.", "The stone city was built by Shona-speaking people, and Mali was in West Africa.")],
      "Imported Asian goods in an inland city show its connection to the Indian Ocean trade network.")

B.mcq(T_AA, "Which statement best compares the Aztec and Inca empires?",
      ch("Both extracted resources from conquered peoples, the Aztecs mainly through tribute payments and the Inca through a labor-service system called the mit'a.", "The Aztec Triple Alliance demanded tribute in goods, while the Inca required subject peoples to supply labor for state projects such as roads and terraces."),
      [ch("Both moved goods across their empires using wheeled carts pulled by draft animals.", "Neither empire used wheeled transport for goods; the Inca used llamas and porters along their road system."),
       ch("Both recorded their laws and histories in an alphabetic script.", "The Aztecs used pictographic codices and the Inca used knotted cords (quipu); neither used an alphabet."),
       ch("Both were overthrown by Portuguese expeditions in the early sixteenth century.", "Both empires fell to Spanish conquistadors, in 1521 (Aztec) and in the 1530s (Inca).")],
      "Both empires exploited subject peoples, but through different mechanisms: tribute versus labor service.")

B.mcq(T_EU, src("A manorial survey, western Europe, thirteenth century", "“Each villein shall labor three days in the week on the lord's demesne and render a share of his harvest at Michaelmas. He may not leave the manor, nor marry his daughter outside it, without the lord's leave.”") + "\n\nThe system described in the passage is best understood as a result of which of the following?",
      ch("Weak central authority after the decline of Roman rule, which left local lords providing protection in exchange for peasants' labor.", "Manorialism developed in a decentralized Europe where lords offered protection and land in exchange for peasants' labor and loyalty."),
      [ch("The growth of long-distance trade, which had made most peasants wealthy and mobile.", "The passage shows peasants tied to the land; mobility and wealth for peasants came later, with towns and trade."),
       ch("The labor shortages caused by the Black Death, which gave lords more power over peasants.", "The Black Death (mid-1300s) came after this thirteenth-century document, and the labor shortage it caused tended to improve peasants' bargaining position."),
       ch("The conquest of Europe by the Mongols, who imposed the system.", "The Mongols did not conquer western Europe, and manorialism developed locally.")],
      "Manorialism grew out of political fragmentation and the need for local protection.")

B.mcq(T_EU, "Which was a long-term effect of the Crusades on western Europe?",
      ch("Greater European demand for Asian goods and increased contact with the Islamic world, which helped Italian trading cities such as Venice and Genoa.", "The Crusades stimulated trade and exposed Europeans to goods and knowledge from the eastern Mediterranean, enriching the Italian city-states that carried the trade."),
      [ch("Permanent Christian control of the Holy Land.", "The crusader states were eventually reconquered by Muslim forces, ending in 1291."),
       ch("The end of all trade between Europe and Muslim lands.", "Trade continued and grew; the Crusades did not end it."),
       ch("The collapse of the Byzantine Empire in the twelfth century.", "The Byzantine Empire survived, though weakened (including by the Fourth Crusade in 1204), until 1453.")],
      "The Crusades increased contact and trade, strengthening Italian maritime cities.")

B.mcq(T_EA, "Which statement best compares Song China and western Europe around 1200?",
      ch("Song China had a centralized government, large commercial cities and technologies such as printing and gunpowder, while western Europe was politically fragmented and less urbanized.", "The Song state governed through a bureaucracy and had some of the world's largest cities and advanced technologies, whereas Europe was divided into many feudal lordships."),
      [ch("Both were ruled by centralized governments that selected officials through examinations.", "Only China used an examination system; western Europe was decentralized."),
       ch("Europe had larger cities and more advanced technology than China.", "In this period Chinese cities and technology generally exceeded Europe's."),
       ch("China was divided into many feudal kingdoms while Europe was a single unified state.", "This reverses the situation: China had a centralized state and Europe was fragmented.")],
      "Around 1200 Song China was more centralized, more urban and technologically ahead of western Europe.")

B.mcq(T_SA, "The Khmer temple of Angkor Wat, built in the twelfth century and dedicated to the Hindu god Vishnu, is best understood as evidence of which of the following?",
      ch("The adaptation of Indian religious and political ideas by Southeast Asian rulers through trade and cultural contact.", "Southeast Asian rulers adopted Hindu and Buddhist ideas and symbols from India, adapting them to legitimize their own power."),
      [ch("The military conquest of mainland Southeast Asia by Indian empires.", "Indian religious influence spread mainly through trade and cultural exchange, not conquest by Indian states."),
       ch("The spread of Islam into mainland Southeast Asia by Arab merchants.", "Angkor Wat is a Hindu temple of the twelfth century; Islam became prominent in maritime Southeast Asia later."),
       ch("A rejection of outside influences in favor of purely local religious traditions.", "The temple's Hindu dedication shows the opposite: outside religious ideas were adopted.")],
      "Angkor Wat shows Indian religion adapted by a Southeast Asian state, spread by contact rather than conquest.")

B.mcq(T_SA, src("A Chinese traveler's account of the southern seas, twelfth century", "“Ships passing between the southern seas and the Middle Kingdom must put into the harbor of Srivijaya, where the king's officers collect fees. Those who try to pass by without stopping are pursued and seized.”") + "\n\nThe passage best supports which explanation for Srivijaya's power?",
      ch("It controlled a strategic strait linking Indian Ocean and South China Sea trade.", "Srivijaya's location on the Strait of Malacca region let it tax and regulate shipping between the two seas."),
      [ch("It dominated the interior of the Indian subcontinent through conquest.", "Srivijaya was a maritime state based in Sumatra, not a conqueror of India's interior."),
       ch("It monopolized silk production for European markets.", "Silk production was centered in China, and the passage concerns shipping fees."),
       ch("It controlled the caravan routes of the Sahara.", "The Sahara is in Africa and unrelated to Srivijaya's maritime location.")],
      "The passage shows Srivijaya gaining wealth and power from control of a key maritime route.")

B.mcq(T_EA, src("Lecture notes of a Song-dynasty scholar", "“To cultivate the self, one must investigate the principle in all things. The way of the sage is found in the daily duties of family and office, not in withdrawal from the world.”") + "\n\nThe passage most directly reflects which development in Song China?",
      ch("The rise of Neo-Confucianism, which revived Confucian ethics while responding to Buddhist and Daoist ideas.", "Neo-Confucian thinkers emphasized moral cultivation and social duty, partly in response to Buddhism's emphasis on withdrawal."),
      [ch("The replacement of Confucianism by Buddhism as the official state philosophy.", "The passage criticizes withdrawal from the world and stresses Confucian duties; Confucian thought grew stronger in this period."),
       ch("The adoption of Legalism as the state's governing philosophy.", "Legalism was associated with the Qin dynasty centuries earlier, and the passage emphasizes moral self-cultivation instead."),
       ch("The introduction of Christianity to the imperial court.", "Christianity did not become influential at the Song court.")],
      "The emphasis on moral cultivation and worldly duty reflects Neo-Confucianism.")

B.mcq(T_DAI, "Which statement best describes the role of scholars in the Abbasid caliphate in the history of mathematics and science?",
      ch("They translated and built on Greek, Persian and Indian works, and results such as algebra and Hindu-Arabic numerals later reached Europe.", "Scholars in centers such as Baghdad preserved and extended earlier knowledge and added their own advances, which were later transmitted to Europe."),
      [ch("They invented the printing press that was later copied in Europe.", "Printing developed in China, and the European printing press came in the 1400s; it was not an Abbasid invention."),
       ch("They rejected all foreign learning as contrary to Islamic teaching.", "Abbasid rulers sponsored the translation of foreign works."),
       ch("Their work was unknown outside the Muslim world until the twentieth century.", "Muslim scholarship was translated into Latin and strongly influenced medieval and Renaissance Europe.")],
      "Abbasid scholars were important in preserving, extending and transmitting knowledge.")

B.mcq(T_AA, "Which statement best compares the Swahili city-states of East Africa and the empire of Mali around 1300?",
      ch("Both were influenced by Islam and gained wealth from long-distance trade, but the Swahili states were independent coastal cities while Mali was a large territorial empire.", "Swahili ports such as Kilwa traded across the Indian Ocean and Mali profited from the Sahara trade; their political structures differed."),
      [ch("Both were tributary provinces of the Mongol Empire.", "Neither the Swahili coast nor West Africa was ruled by the Mongols."),
       ch("The Swahili states depended on trans-Saharan trade, while Mali depended on Indian Ocean trade.", "This reverses their trade orientations."),
       ch("Neither had any trade contact with Muslim merchants.", "Both had extensive contact with Muslim merchants, and Islam was influential in both.")],
      "Both were trade-based and Islamic-influenced, but one was a set of city-states and the other an empire.")

saq(B, T_AA,
    "Use the passage to answer parts A, B and C.\n\n" + src("A Cairo official, early fourteenth century", "“When the king of Mali came to Cairo on pilgrimage, he gave out so much gold that its value fell in the markets and did not recover for many years. His followers numbered in the thousands.”") + "\n\n**a)** Identify ONE piece of evidence in the passage that shows Mali was connected to the wider Islamic world.\n\n**b)** Explain ONE historical development that helps explain why Mali's rulers had so much gold.\n\n**c)** Explain ONE way that Mali's connections to the Islamic world affected West African societies in this period.",
    [(1, "Part A: Identifies the king's pilgrimage to Mecca through Cairo (or the presence of the king in Cairo) as evidence of connection to the Islamic world"),
     (1, "Part B: Explains that Mali controlled or taxed gold production and the trans-Saharan trade, in which gold was exchanged for salt and other goods"),
     (1, "Part C: Explains an effect such as the spread of Islam, the growth of centers of Islamic learning such as Timbuktu, or increased trade and contact with the Mediterranean world")],
    "a) The passage describes the king of Mali traveling to Cairo on pilgrimage, showing Mali's rulers were Muslims connected to the wider Islamic world.\nb) Mali's rulers controlled the trans-Saharan trade in gold from West African goldfields, which they exchanged for goods such as salt, and they taxed the traders who passed through their territory.\nc) Contact with the Islamic world encouraged the growth of centers of Islamic learning such as Timbuktu, where scholars, mosques and libraries flourished, and spread Islamic practice and literacy in Arabic through the region.")

leq(B, T_EU,
    "**Long Essay Question**\n\nEvaluate the extent to which religion shaped the political authority of states in TWO of the following regions between about 1200 and 1450: East Asia, West Africa, South Asia, western Europe.",
    "A strong response states a defensible thesis, for example that religion shaped political authority powerfully in West Africa and western Europe but less decisively than administration and military power in East Asia. It describes the broader context (such as the spread of universal religions along trade routes), uses specific evidence (such as Mansa Musa's pilgrimage and Mali's Muslim rulers; the Catholic Church's influence over European kings and the Crusades; Neo-Confucian ideology and the Song examination system; the Sufis and the Delhi Sultanate), and analyzes similarity and difference in how religion legitimized rulers or competed with other sources of authority.",
    "Thesis: Presents a defensible thesis that responds to the prompt and evaluates the extent to which religion shaped political authority in two regions",
    "Contextualization: Places the topic in a broader context, such as the spread of Islam, Christianity and Neo-Confucian thought and the growth of trade and states in 1200-1450",
    "Evidence: Provides at least two specific, accurate pieces of evidence relevant to each region (1 point for addressing the topic with evidence, 2nd point for using specific evidence to support the argument)",
    "Analysis and reasoning: Uses comparison, causation or continuity and change to structure the argument (1 point), and demonstrates complex understanding, such as qualifying the argument or noting that religion interacted with trade, military power or administration (2nd point)")

B.save()
B.brief()
