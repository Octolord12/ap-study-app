from common import *

B = bank(8, "unit-8-cold-war-and-decolonization")
T_OR, T_CW, T_DEC, T_NEW, T_END = ("origins-of-the-cold-war", "the-cold-war", "decolonization", "newly-independent-states", "end-of-the-cold-war")

B.mcq(T_OR, src("An address by a United States president to Congress, 1947", "“It must be the policy of the United States to support free peoples who are resisting attempted subjugation by armed minorities or by outside pressures. If we falter in our leadership, we may endanger the peace of the world.”") + "\n\nThe policy described in the passage is best understood as part of which strategy?",
      ch("Containment, the effort to prevent the spread of Soviet influence and communism.", "The Truman Doctrine pledged American support to governments resisting communist pressure, beginning with Greece and Turkey."),
      [ch("Isolationism, the avoidance of foreign commitments.", "The passage commits the United States to supporting other countries abroad."),
       ch("Appeasement, the granting of concessions to an aggressor.", "The policy aimed to resist, not to concede."),
       ch("Non-alignment, the refusal to take sides in a rivalry between powers.", "The passage commits the United States to leading one side.")],
      "The passage describes containment of Soviet expansion.")

B.mcq(T_OR, "Which statement best explains why the United States and the Soviet Union became rivals after World War II?",
      ch("They had opposed ideologies (capitalist democracy and communism), disagreed about the future of Germany and Eastern Europe, and mistrusted each other's intentions.", "Their wartime alliance had been based on the defeat of Germany, and once it ended their conflicting systems and interests led to confrontation."),
      [ch("They disagreed mainly about the borders of the Pacific islands.", "The rivalry was centered on ideology and the postwar order in Europe and elsewhere."),
       ch("They shared the same ideology but competed for markets.", "Their ideologies were opposed."),
       ch("The Soviet Union had joined the Axis powers during the war.", "The Soviet Union was an Allied power in World War II.")],
      "Ideological, geopolitical and security conflicts produced the Cold War.")

B.mcq(T_CW, "The creation of NATO in 1949 and the Warsaw Pact in 1955 most directly reflects which of the following?",
      ch("The division of Europe into opposing military alliances led by the United States and the Soviet Union.", "NATO linked the United States with western European states, and the Warsaw Pact linked the Soviet Union with its Eastern European allies."),
      [ch("The end of the Cold War and the reunification of Germany.", "The alliances were products of the early Cold War."),
       ch("The creation of the European Union.", "The European Union was established later and is an economic and political union."),
       ch("A plan to disband all national armies.", "The alliances were military blocs.")],
      "NATO and the Warsaw Pact were opposing Cold War military alliances.")

B.mcq(T_CW, "Which statement best describes the Korean War (1950-1953) as an example of Cold War conflict?",
      ch("A conflict in which the United States and United Nations forces supported South Korea, while China and the Soviet Union supported North Korea, ending in a stalemate and the continued division of Korea.", "The war was a regional conflict with superpower involvement that ended with an armistice near the original dividing line."),
      [ch("A war that ended with the unification of Korea under communist rule.", "Korea remained divided."),
       ch("A conflict fought only between the Soviet Union and the United States armies.", "The main combatants were Korean, Chinese and UN forces, with the Soviets providing support."),
       ch("A war to end colonial rule by Japan, won by the Korean colonial administration.", "Japanese rule had ended in 1945.")],
      "The Korean War was a proxy-style conflict that left the peninsula divided.")

B.mcq(T_CW, "Which statement best describes the outcome of the Cuban Missile Crisis of 1962?",
      ch("It brought the superpowers close to nuclear war and ended with the Soviet withdrawal of its missiles from Cuba, a United States pledge not to invade Cuba, and later efforts to reduce tensions.", "The crisis was resolved by negotiation, and afterward the superpowers established better communication."),
      [ch("The United States invaded Cuba and overthrew the government.", "The United States did not invade Cuba."),
       ch("The Soviet Union attacked the United States with nuclear weapons.", "No nuclear weapons were used."),
       ch("The crisis ended the Cold War.", "The Cold War continued for nearly three more decades.")],
      "The crisis was resolved diplomatically and was followed by efforts to reduce tensions.")

B.mcq(T_CW, "The Great Leap Forward (1958-1962) in China is best understood as which of the following?",
      ch("A campaign to rapidly industrialize and collectivize the economy that caused severe disruption and a massive famine.", "Mao's policies reorganized agriculture into communes and pushed unrealistic production goals, leading to millions of deaths."),
      [ch("A successful program that doubled grain production and ended poverty.", "The campaign led to famine."),
       ch("A return to private farming and free markets.", "It extended state and collective control."),
       ch("A military campaign to conquer Taiwan.", "It was an economic campaign, not a military one.")],
      "The Great Leap Forward was a failed economic campaign with devastating consequences.")

B.mcq(T_DEC, src("Speech by a nationalist leader on the day of his country's independence, 1957", "“At long last the battle has ended, and our beloved country is free forever. We have awakened. We shall show the world that the African is capable of managing his own affairs.”") + "\n\nThe speech is best understood as part of which development?",
      ch("The postwar nationalist movements in Asia and Africa that challenged European colonial rule and led to independence.", "Ghana in 1957 was the first sub-Saharan African colony to gain independence, and it inspired other movements."),
      [ch("The expansion of the Ottoman Empire into Africa.", "The Ottoman Empire had been dissolved by the 1920s."),
       ch("The establishment of the Warsaw Pact.", "The speech concerns independence from colonial rule, not a military alliance."),
       ch("Colonial reforms intended to preserve European rule permanently.", "The speech celebrates the end of colonial rule.")],
      "The speech reflects the postwar independence movements.")

B.mcq(T_DEC, "Which statement best explains the partition of British India in 1947?",
      ch("Political and religious tensions between Hindu and Muslim leaders led to the creation of the separate states of India and Pakistan, accompanied by mass migration and violence.", "The British withdrew and the subcontinent was divided along religious lines, causing displacement of millions."),
      [ch("The British decided to keep India united and rejected demands for independence.", "India became independent and was divided."),
       ch("The Soviet Union invaded and divided India.", "The partition was carried out under British authority."),
       ch("The Mughal Empire was restored in the north.", "The Mughal Empire had ended in the nineteenth century.")],
      "Partition resulted from religious and political tensions and caused massive upheaval.")

B.mcq(T_DEC, "Which statement best compares the paths to independence of India and Algeria?",
      ch("India's movement relied largely on mass nonviolent mobilization and negotiation with Britain, while Algeria's required a long, violent war against France (1954-1962), partly because of a large French settler population.", "Different colonial situations produced different routes to independence."),
      [ch("Both won independence without any political organization or protest.", "Both involved organized nationalist movements."),
       ch("India fought a long war against France, while Algeria negotiated with Britain.", "India was a British colony and Algeria a French colony."),
       ch("Both became independent in 1914.", "India became independent in 1947 and Algeria in 1962.")],
      "India's independence was gained mainly by nonviolent mobilization and negotiation, whereas Algeria's came through war.")

B.mcq(T_DEC, "The Bandung Conference of 1955 and the Non-Aligned Movement reflected which goal of many newly independent states?",
      ch("To avoid formal alignment with either superpower bloc and to promote solidarity and independence among Asian and African nations.", "Leaders of newly independent states sought to maintain independence and cooperation outside the Cold War alliances."),
      [ch("To join NATO as full members.", "The movement aimed at nonalignment, not membership in NATO."),
       ch("To restore European colonial rule.", "The movement opposed colonialism."),
       ch("To adopt the constitution of the Soviet Union.", "Nonaligned states did not formally adopt the Soviet system.")],
      "Nonalignment sought independence from both Cold War blocs.")

B.mcq(T_NEW, src("Statement by an African political leader, 1960s", "“We have our flag and our anthem, but the mines, the plantations and the banks are still owned by foreign companies, and the price of our crops is set in far-off cities. Political independence without economic independence is an empty gift.”") + "\n\nThe statement most directly expresses concern about which of the following?",
      ch("Neocolonialism, the continued foreign economic influence over countries that had gained political independence.", "Many new states remained economically dependent on former colonial powers and foreign firms."),
      [ch("The failure of the Soviet Union to provide military aid.", "The passage concerns economic ownership, not military aid."),
       ch("The threat of a return to feudalism.", "The passage describes foreign economic control."),
       ch("The danger of too much government ownership of industry.", "The passage criticizes foreign ownership.")],
      "The speaker is describing economic dependence after political independence.")

B.mcq(T_NEW, "Which statement best explains the significance of the Suez Crisis of 1956?",
      ch("The failure of the British, French and Israeli attack after Egypt nationalized the canal showed the decline of British and French power and the growing influence of the United States and the Soviet Union.", "Pressure from the superpowers forced the attackers to withdraw, and Egypt kept control of the canal."),
      [ch("It restored British control of Egypt.", "Egypt kept control of the canal."),
       ch("It led to the immediate collapse of the Soviet Union.", "The Soviet Union lasted until 1991."),
       ch("It was a victory for the colonial powers that strengthened their empires.", "The crisis was a humiliation for Britain and France.")],
      "The crisis showed the limits of British and French power.")

B.mcq(T_NEW, "Which statement best describes South Africa's system of apartheid and its end?",
      ch("A system of legal racial segregation and white minority rule, established in 1948, that ended in the early 1990s after internal resistance and international pressure, with multiracial elections in 1994.", "Apartheid was dismantled after decades of protest and sanctions, and Nelson Mandela became president in 1994."),
      [ch("A policy of equal rights for all races that began in 1948.", "Apartheid enforced racial inequality."),
       ch("A system that ended in 1948 when South Africa left the British Empire.", "Apartheid began in 1948."),
       ch("A system imposed by the Soviet Union on South Africa.", "Apartheid was established by the South African government.")],
      "Apartheid was legal racial segregation, ended after resistance and international pressure.")

B.mcq(T_END, src("Speech by a Soviet leader, 1987", "“We need openness in our public life, so that the people may know the truth about our affairs, and we need the restructuring of our economy, which has too long been held back by rigid central planning.”") + "\n\nThe policies described in the passage are best understood as which of the following?",
      ch("Gorbachev's reforms of glasnost (openness) and perestroika (restructuring), intended to revive the Soviet system but which contributed to its collapse.", "The reforms loosened controls and encouraged criticism, which weakened the Communist Party's authority."),
      [ch("Stalin's Five-Year Plans for rapid industrialization.", "Stalin centralized economic planning; the passage criticizes rigid central planning."),
       ch("Lenin's New Economic Policy of the 1920s.", "The passage refers to the late Soviet period."),
       ch("A plan to expand Soviet control over Western Europe.", "The reforms focused on internal change.")],
      "The passage describes glasnost and perestroika.")

B.mcq(T_END, "Which combination of factors best explains the fall of communist governments in Eastern Europe in 1989?",
      ch("Economic stagnation, growing popular protest movements, and the Soviet leadership's decision not to use force to keep those governments in power.", "Without Soviet military intervention, popular movements were able to bring down communist regimes."),
      [ch("A NATO invasion of Eastern Europe.", "NATO did not invade."),
       ch("A Soviet reinvasion that restored order in every country.", "The Soviet Union did not use force to save the governments."),
       ch("Chinese military support for the protesters.", "China did not intervene in Eastern Europe.")],
      "Economic problems, protests and the absence of Soviet intervention led to the fall of these governments.")

saq(B, T_DEC,
    "Use the passage to answer parts A, B and C.\n\n" + src("Speech by a nationalist leader on the day of his country's independence, 1957", "“At long last the battle has ended, and our beloved country is free forever. We have awakened. We shall show the world that the African is capable of managing his own affairs.”") + "\n\n**a)** Identify ONE belief or goal expressed by the speaker.\n\n**b)** Explain ONE way in which World War II contributed to the growth of independence movements in Asia and Africa.\n\n**c)** Explain ONE challenge that newly independent states commonly faced.",
    [(1, "Part A: Identifies a goal or belief such as national self-rule, freedom from colonial control, or the capacity of Africans to govern themselves"),
     (1, "Part B: Explains a contribution such as the weakening of European powers, colonial soldiers' wartime experience, the example of Japan's defeat of European forces in Asia, or the war's rhetoric of self-determination"),
     (1, "Part C: Explains a challenge such as economic dependence on former colonial powers or foreign firms (neocolonialism), ethnic divisions created by colonial borders, building political institutions, or Cold War pressure to align with a superpower")],
    "a) The speaker expresses the belief that the country is free and that Africans are capable of governing themselves.\nb) World War II weakened Britain and France economically and militarily, so they were less able to hold their colonies, and colonial soldiers who fought in the war returned with new skills and expectations. The war's language of freedom and self-determination also encouraged nationalists.\nc) Many new states had economies that were dependent on exporting a few raw materials to former colonial powers or on foreign-owned companies, which limited their real independence.")

leq(B, T_NEW,
    "**Long Essay Question**\n\nEvaluate the extent to which the Cold War shaped the process of decolonization and the development of newly independent states in Asia and Africa between 1945 and 1991.",
    "A strong response takes a position (for example that the Cold War shaped the choices and conflicts of new states, but that the main drivers of independence were nationalist movements and the weakening of European powers). It places the topic in context (the end of World War II and the rivalry of the superpowers) and uses specific evidence such as the Bandung Conference and non-alignment, superpower aid and proxy wars (Korea, Vietnam, the Congo, Angola), the Suez Crisis, India and Pakistan, and Ghana. It analyzes causation and continuity and change, and considers how colonial borders and economic dependence also shaped the new states.",
    "Thesis: Presents a defensible thesis that responds to the prompt and evaluates the extent to which the Cold War shaped decolonization and the new states",
    "Contextualization: Describes broader context, such as the end of World War II, weakened European empires and the superpower rivalry",
    "Evidence: Provides at least two specific, accurate examples (such as non-alignment, proxy wars, superpower aid, the Suez Crisis, partition) and uses them to support the argument",
    "Analysis and reasoning: Uses causation to structure the argument (1 point), and shows complexity by weighing the Cold War against other factors such as nationalist movements, colonial borders or economic dependence (2nd point)")

B.save()
B.brief()
