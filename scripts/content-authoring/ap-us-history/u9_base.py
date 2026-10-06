from common import *

B = base(9)
T_RC, T_EC, T_ET, T_WT, T_DC = ("reagan-and-conservatism", "end-of-cold-war", "economy-technology-globalization", "september-11-and-war-on-terror", "demographic-and-cultural-change")

# ---- The Reagan era and conservatism ----
B.mcq(T_RC, "Supply-side economics, associated with the Reagan administration, argued that",
      ch("cutting taxes and regulation would stimulate investment and economic growth.", "Supporters argued that lower taxes would encourage business expansion and eventually benefit the whole economy."),
      [ch("raising taxes on all incomes would reduce inflation.", "That is the opposite of supply-side thinking."),
       ch("the government should take over major industries.", "Supply-side policy relied on private markets."),
       ch("tariffs should be eliminated and replaced by a federal income guarantee.", "That is not part of supply-side economics.")],
      "Supply-side economics promoted tax cuts and deregulation to spur growth.", difficulty="easy")

B.mcq(T_RC, "President Reagan's firing of striking air traffic controllers in 1981",
      ch("weakened organized labor and signaled a tougher stance toward unions.", "The firing of the PATCO strikers encouraged employers to take harder positions against strikes."),
      [ch("strengthened the power of public employee unions.", "The action weakened unions."),
       ch("was overturned by the Supreme Court.", "The firings stood."),
       ch("led to a general strike across the nation.", "No general strike followed.")],
      "The PATCO firings weakened the labor movement.", difficulty="medium")

B.mcq(T_RC, src("A president's inaugural address, 1981", "“In this present crisis, government is too often the cause of our troubles, not the cure. We must reduce its size and its reach and restore power to the states and the people.”") + "\n\nThe passage best reflects which of the following?",
      ch("The conservative critique of big government that gained strength after the 1960s and 1970s.", "The speaker argues that government should be smaller and that power should go back to the states and individuals."),
      [ch("Support for expanding the Great Society.", "The speaker criticizes large government."),
       ch("A call for greater federal control of the economy.", "The speaker wants to reduce government's reach."),
       ch("A defense of New Deal liberalism.", "The speaker questions government's role.")],
      "The passage expresses the conservative view that government had become too large.", difficulty="medium")

B.mcq(T_RC, "The Moral Majority and other conservative Christian groups in the 1980s",
      ch("mobilized evangelical voters around issues such as abortion and school prayer and became an important force in the Republican Party.", "The Religious Right brought a large group of voters into conservative politics."),
      [ch("supported the Equal Rights Amendment and expanded abortion access.", "They opposed these positions."),
       ch("were created by the Democratic Party to win Southern votes.", "They aligned increasingly with Republicans."),
       ch("sought to end all religious involvement in politics.", "They sought a stronger role for religion in public life.")],
      "The Religious Right became a major force in conservative politics.", difficulty="medium")

B.mcq(T_RC, "The Iran-Contra affair revealed that",
      ch("officials in the Reagan administration had secretly sold arms to Iran and used the proceeds to fund Contra rebels in Nicaragua despite restrictions passed by Congress.", "The scandal raised questions about presidential power and congressional oversight."),
      [ch("the United States had formally declared war on Nicaragua.", "There was no declaration of war."),
       ch("Reagan had been impeached by the House.", "He was not impeached."),
       ch("Congress had secretly approved the arms sales.", "The sales violated congressional restrictions on aid to the Contras.")],
      "Iran-Contra involved secret arms sales and illegal funding of rebels.", difficulty="hard")

B.mcq(T_RC, "The Personal Responsibility and Work Opportunity Act of 1996",
      ch("ended the federal guarantee of welfare and set time limits and work requirements for aid.", "The law reshaped the welfare system and moved responsibility toward the states."),
      [ch("expanded unlimited welfare benefits.", "The law limited benefits."),
       ch("created Medicare.", "Medicare was created in 1965."),
       ch("abolished Social Security.", "Social Security was not abolished.")],
      "The 1996 law ended the federal entitlement to welfare.", difficulty="hard")

# ---- The end of the Cold War ----
B.mcq(T_EC, "The fall of the Berlin Wall in 1989",
      ch("symbolized the collapse of communist rule in Eastern Europe and led to German reunification in 1990.", "The event was a turning point in the end of the Cold War."),
      [ch("marked the start of the Cold War.", "The Cold War began in the late 1940s."),
       ch("was a Soviet victory over West Germany.", "It reflected communism's collapse."),
       ch("occurred during the Korean War.", "It occurred in 1989.")],
      "The fall of the Wall symbolized the end of communism in Eastern Europe.", difficulty="easy")

B.mcq(T_EC, "Mikhail Gorbachev's policies of glasnost and perestroika",
      ch("introduced political openness and economic restructuring in the Soviet Union, which contributed to the end of the Cold War.", "The reforms loosened controls and unleashed forces that Gorbachev could not contain."),
      [ch("expanded Soviet control over Eastern Europe.", "The reforms helped loosen control."),
       ch("ended arms control negotiations with the United States.", "Gorbachev negotiated arms agreements."),
       ch("restored Stalinist policies.", "The reforms moved away from Stalinist practices.")],
      "Gorbachev's reforms helped bring about the end of the Cold War.", difficulty="medium")

B.mcq(T_EC, src("A president's address, 1991", "“The tide of freedom has swept across Eastern Europe, and now the Soviet Union itself has dissolved. The United States stands today as the world's leading power, with a responsibility to help build a peaceful order in a new age.”") + "\n\nThe passage best reflects which of the following?",
      ch("The emergence of the United States as the sole superpower after the Soviet collapse.", "The speaker describes the United States as the leading power after the Cold War."),
      [ch("The start of an arms race with the Soviet Union.", "The passage describes the Soviet Union's dissolution."),
       ch("An argument for isolationism.", "The speaker speaks of responsibility in the world."),
       ch("The beginning of the Cold War.", "The passage describes its end.")],
      "The passage reflects the new American role after the Soviet collapse.", difficulty="medium")

B.mcq(T_EC, "The Persian Gulf War of 1991",
      ch("involved a United States-led coalition, acting with United Nations authorization, that expelled Iraqi forces from Kuwait after Iraq's invasion in 1990.", "The coalition's goal was to liberate Kuwait."),
      [ch("was fought to overthrow the government of Iraq.", "The coalition's mission was limited to expelling Iraq from Kuwait."),
       ch("was a war between the United States and the Soviet Union.", "The Soviet Union did not fight the United States."),
       ch("ended with the occupation of Iraq by American forces for a decade.", "Iraq was not occupied after 1991.")],
      "The Gulf War liberated Kuwait.", difficulty="medium")

B.mcq(T_EC, "Which factors contributed most to the end of the Cold War?",
      ch("Economic stagnation and political reform in the Soviet Union, popular movements in Eastern Europe and the pressures of the arms race.", "Several internal and external factors combined to end the Cold War."),
      [ch("A Soviet military defeat in a direct war with the United States.", "There was no such war."),
       ch("The success of communist economic planning.", "Soviet economic problems contributed to its collapse."),
       ch("A nuclear exchange between the superpowers.", "No nuclear exchange occurred.")],
      "Soviet economic problems, reforms, Eastern European movements and the arms race all contributed.", difficulty="hard")

B.mcq(T_EC, "In the 1990s, United States foreign policy",
      ch("involved humanitarian and peacekeeping interventions in places such as Somalia, Bosnia and Kosovo, often with NATO or United Nations support.", "The end of the Cold War led to new kinds of overseas involvement."),
      [ch("withdrew from NATO and the United Nations.", "The United States remained in both organizations."),
       ch("focused solely on containing the Soviet Union.", "The Soviet Union no longer existed."),
       ch("avoided all military interventions abroad.", "The United States intervened in several conflicts.")],
      "The 1990s saw interventions in Somalia, Bosnia and Kosovo.", difficulty="hard")

# ---- Economy, technology and globalization ----
B.mcq(T_ET, "Which technological developments most transformed the American economy in the 1990s?",
      ch("The personal computer and the Internet.", "Computers and the Internet changed communication, business and daily life."),
      [ch("The assembly line and the telegraph.", "Those developments came much earlier."),
       ch("The steam engine and the railroad.", "Those were nineteenth-century innovations."),
       ch("The cotton gin and the telephone.", "Those were earlier inventions.")],
      "The personal computer and the Internet reshaped the 1990s economy.", difficulty="easy")

B.mcq(T_ET, "The North American Free Trade Agreement (NAFTA), which took effect in 1994, aimed to",
      ch("eliminate most trade barriers among the United States, Canada and Mexico.", "NAFTA created a large free-trade area."),
      [ch("create a common currency for North America.", "NAFTA did not create a common currency."),
       ch("increase tariffs on goods from Canada and Mexico.", "NAFTA reduced barriers."),
       ch("end trade between the United States and Asia.", "NAFTA concerned North America.")],
      "NAFTA reduced trade barriers among three countries.", difficulty="medium")

B.mcq(T_ET, src("A factory worker's testimony, 2000", "“They told us the plant was moving to Mexico where wages are lower. After twenty years on the line I was out of work and told to retrain for a computer job in a city two hundred miles away.”") + "\n\nThe passage best reflects which of the following?",
      ch("The loss of manufacturing jobs to outsourcing and globalization and the economic adjustment it required of workers.", "The worker describes a plant moving abroad and the need to retrain."),
      [ch("The growth of unions in manufacturing.", "The worker lost a job."),
       ch("An increase in domestic factory employment.", "The plant moved away."),
       ch("The success of protectionist trade policy.", "The passage describes the loss of jobs to a lower-wage country.")],
      "The passage reflects job losses from outsourcing and globalization.", difficulty="medium")

B.mcq(T_ET, "The financial crisis of 2008 was triggered in large part by",
      ch("the collapse of the housing bubble and risky mortgage lending, which damaged major financial institutions and the broader economy.", "Falling home values and mortgage defaults spread losses through the financial system."),
      [ch("a sudden increase in tariffs.", "Tariffs were not the cause."),
       ch("the end of the gold standard.", "That occurred in the 1970s."),
       ch("a surge in manufacturing exports.", "The crisis arose from housing and finance.")],
      "The housing bubble and risky lending triggered the 2008 crisis.", difficulty="medium")

B.mcq(T_ET, "The federal response to the 2008 financial crisis included",
      ch("bank rescues through the Troubled Asset Relief Program under President Bush and a stimulus package and new financial regulation under President Obama.", "Both administrations took major steps to stabilize the economy."),
      [ch("a decision to take no federal action.", "The government intervened extensively."),
       ch("the elimination of the Federal Reserve.", "The Federal Reserve took an active role."),
       ch("a return to the gold standard.", "The gold standard was not restored.")],
      "TARP, a stimulus and new regulation were part of the response.", difficulty="hard")

B.mcq(T_ET, "Which statement best describes economic trends in the decades after 1980?",
      ch("Productivity and incomes at the top grew rapidly, while wages for many middle- and lower-income workers stagnated, widening economic inequality.", "Economists have documented a growing gap between high and middle incomes."),
      [ch("Incomes of the poorest households grew faster than those of the wealthiest.", "The gap widened in the other direction."),
       ch("Manufacturing employment rose steadily.", "Manufacturing employment declined."),
       ch("Economic inequality fell sharply.", "Inequality increased.")],
      "Inequality widened after 1980.", difficulty="hard")

# ---- September 11 and the war on terror ----
B.mcq(T_WT, "The terrorist attacks of September 11, 2001",
      ch("were carried out by al-Qaeda, killed nearly three thousand people and led to the war in Afghanistan.", "The attacks prompted the invasion of Afghanistan, where the Taliban sheltered al-Qaeda."),
      [ch("were carried out by Iraq and led to the end of the Gulf War.", "The attacks were carried out by al-Qaeda, not by Iraq."),
       ch("caused a decline in federal security spending.", "Security spending increased."),
       ch("occurred in 1991.", "They occurred in 2001.")],
      "The 9/11 attacks led to the war in Afghanistan.", difficulty="easy")

B.mcq(T_WT, "The USA Patriot Act of 2001",
      ch("expanded government surveillance and law enforcement powers in the name of counterterrorism, raising concerns about civil liberties.", "The law increased investigative powers and sparked debate."),
      [ch("limited the power of intelligence agencies.", "The law expanded their powers."),
       ch("ended the war in Afghanistan.", "The war continued."),
       ch("guaranteed new rights for suspects.", "The law drew criticism for weakening protections.")],
      "The Patriot Act expanded surveillance and raised civil liberties debates.", difficulty="medium")

B.mcq(T_WT, src("A president's speech, 2002", "“We cannot wait for threats to fully materialize. America must be ready to act preemptively against terrorists and hostile regimes that seek weapons of mass destruction before they can strike.”") + "\n\nThe passage best reflects which of the following?",
      ch("The doctrine of preemption, which was used to justify the invasion of Iraq.", "The speaker argues for acting before threats fully develop."),
      [ch("The policy of containment.", "Containment was a Cold War approach and not preemptive."),
       ch("A call for isolationism.", "The speaker calls for active measures."),
       ch("The Truman Doctrine.", "The passage concerns a doctrine from 2002.")],
      "The passage expresses the doctrine of preemption.", difficulty="medium")

B.mcq(T_WT, "The Department of Homeland Security was created in 2002 and 2003 to",
      ch("coordinate domestic security agencies in response to the 9/11 attacks.", "The department combined many agencies concerned with protecting the nation."),
      [ch("replace the Department of Defense.", "It did not replace Defense."),
       ch("manage the nation's public schools.", "It dealt with security."),
       ch("oversee the Federal Reserve.", "That is a separate institution.")],
      "The department consolidated domestic security efforts.", difficulty="medium")

B.mcq(T_WT, "The 2003 invasion of Iraq was justified mainly by",
      ch("the administration's claim that Iraq possessed weapons of mass destruction, although no stockpiles were later found.", "The WMD claim was central to the case for war."),
      [ch("the fall of the Berlin Wall.", "That occurred in 1989."),
       ch("a request from the United Nations to occupy Iraq.", "The invasion lacked explicit United Nations authorization."),
       ch("Iraq's attack on the United States on September 11.", "Iraq did not carry out the 9/11 attacks.")],
      "The administration cited weapons of mass destruction, which were not found.", difficulty="hard")

B.mcq(T_WT, "Debates over the Guantanamo Bay detention facility and National Security Agency surveillance reflected",
      ch("tension between national security and civil liberties.", "Critics argued that security measures threatened individual rights."),
      [ch("agreement that civil liberties should never be limited.", "The debates were contested."),
       ch("a dispute over tariffs.", "The debates concerned security and rights."),
       ch("a plan to expand the draft.", "These were not debates about the draft.")],
      "The debates centered on balancing security and civil liberties.", difficulty="hard")

# ---- Demographic and cultural change ----
B.mcq(T_DC, "Since the 1970s, immigration to the United States has come largely from",
      ch("Latin America and Asia.", "Immigration patterns shifted away from Europe."),
      [ch("northern and western Europe.", "That described earlier periods."),
       ch("the Middle East and Central Asia.", "These regions were not the largest sources of recent immigration."),
       ch("eastern Europe and the former Soviet Union.", "Immigration from these regions was far smaller than from Latin America and Asia.")],
      "Most recent immigration has come from Latin America and Asia.", difficulty="easy")

B.mcq(T_DC, "The Immigration Reform and Control Act of 1986",
      ch("granted legal status to many undocumented immigrants who had lived in the country since before 1982 and imposed penalties on employers who knowingly hired undocumented workers.", "The law combined legalization with enforcement."),
      [ch("ended all legal immigration.", "The law did not end legal immigration."),
       ch("deported all undocumented immigrants.", "It granted legal status to many."),
       ch("created national origins quotas.", "Quotas were ended in 1965.")],
      "IRCA combined legalization with employer sanctions.", difficulty="medium")

B.mcq(T_DC, src("A Supreme Court opinion, 2015", "“No union is more profound than marriage. It embodies the highest ideals of love, fidelity, devotion and family. Same-sex couples seek equal dignity in the eyes of the law.”") + "\n\nThe passage best reflects which of the following?",
      ch("The Court's recognition of same-sex marriage as a constitutional right in Obergefell v. Hodges.", "The opinion held that same-sex couples may not be denied the right to marry."),
      [ch("A ruling that states could ban same-sex marriage.", "The Court ruled the opposite."),
       ch("The passage of the Equal Rights Amendment.", "The passage concerns marriage."),
       ch("A decision on school prayer.", "The passage concerns marriage.")],
      "The passage reflects the Obergefell decision.", difficulty="medium")

B.mcq(T_DC, "The election of Barack Obama in 2008 was significant because",
      ch("he became the first African American elected president of the United States.", "The election marked a milestone in American political history."),
      [ch("he was the first president elected without a college degree.", "The significance of the election lay in his being the first African American president."),
       ch("he won the first election decided by the House of Representatives.", "He won the Electoral College outright."),
       ch("he ended the two-party system.", "The two-party system continued.")],
      "Obama became the first African American president.", difficulty="medium")

B.mcq(T_DC, "Which factor contributed to increasing political polarization in the late twentieth and early twenty-first centuries?",
      ch("The realignment of the parties along ideological lines, partisan media and divisions over cultural issues.", "Multiple developments reinforced partisan divisions."),
      [ch("The abolition of political parties.", "Parties remained central."),
       ch("A decline in the role of the media.", "Media options expanded."),
       ch("Agreement among the parties on major social issues.", "Disagreements deepened.")],
      "Party realignment, partisan media and cultural conflicts increased polarization.", difficulty="hard")

B.mcq(T_DC, "Population trends in the United States since 1980 have included",
      ch("continued growth of the South and West, an aging population and growing racial and ethnic diversity.", "The census documents these patterns."),
      [ch("a steady move of population from the South to the Northeast.", "The movement was toward the South and West."),
       ch("a decline in racial and ethnic diversity.", "Diversity increased."),
       ch("a falling average age of the population.", "The population has been aging.")],
      "Population growth in the South and West, aging and diversity characterized recent decades.", difficulty="hard")

# ---- Short-answer questions ----
saq(B, T_RC,
    "Use the excerpt to answer parts A, B and C.\n\n" + src("A historian, early twenty-first century", "“The conservative revival of the 1980s drew on a backlash against the liberalism of the 1960s and 1970s, uniting those who opposed taxes and regulation with those who wanted to restore traditional values.”") + "\n\n**a)** Identify ONE claim made by the historian.\n\n**b)** Explain ONE development of the 1960s or 1970s that contributed to the conservative backlash.\n\n**c)** Explain ONE way in which the Reagan presidency reflected conservative goals.",
    [(1, "Part A: Identifies a claim, such as that the conservative revival grew out of a backlash against 1960s and 1970s liberalism or that it united economic and cultural conservatives"),
     (1, "Part B: Explains a development such as the expansion of the federal government under the Great Society, rising taxes and stagflation, controversies over Roe v. Wade or school prayer, or opposition to busing"),
     (1, "Part C: Explains an example such as tax cuts, deregulation, a military buildup, or support from the Religious Right")],
    "a) The historian argues that the conservative revival was a reaction against 1960s and 1970s liberalism and united economic conservatives with cultural conservatives.\nb) Stagflation in the 1970s and frustration with higher taxes and the growth of government under the Great Society led many voters to support conservative candidates.\nc) Reagan carried out major tax cuts and reduced regulation, which reflected conservative beliefs in lower taxes and a smaller role for government in the economy.")

saq(B, T_EC,
    "Use the excerpt to answer parts A, B and C.\n\n" + src("A Soviet leader's speech, 1987", "“The old ways cannot continue. We need restructuring of our economy and openness in our society, for a country cannot remain strong when its people are not free to speak.”") + "\n\n**a)** Identify ONE reason for the reforms described in the excerpt.\n\n**b)** Explain ONE way in which United States policy in the 1980s contributed to the end of the Cold War.\n\n**c)** Explain ONE effect of the collapse of the Soviet Union on United States foreign policy in the 1990s.",
    [(1, "Part A: Identifies a reason such as economic stagnation in the Soviet Union or the need for greater openness and restructuring"),
     (1, "Part B: Explains a contribution such as the military buildup and the Strategic Defense Initiative pressuring the Soviet economy, or summit diplomacy and arms control such as the INF Treaty of 1987"),
     (1, "Part C: Explains an effect such as the United States becoming the sole superpower, the expansion of NATO, or new humanitarian and peacekeeping interventions")],
    "a) The speaker says the Soviet economy needed restructuring and that society needed more openness because the country could not stay strong without freedom of speech.\nb) The Reagan administration increased military spending and proposed the Strategic Defense Initiative, which added to the economic strain on the Soviet Union, while summit meetings led to the INF Treaty of 1987.\nc) With the collapse of the Soviet Union, the United States became the sole superpower and took part in new interventions such as those in Bosnia and Kosovo.")

saq(B, T_WT,
    "Using your knowledge of United States history, answer parts A, B and C.\n\n**a)** Identify ONE way in which the United States government responded abroad to the attacks of September 11, 2001.\n\n**b)** Identify ONE way in which the United States government responded at home to the attacks of September 11, 2001.\n\n**c)** Explain ONE controversy that arose from the American response to September 11 in the period 2001 to 2010.",
    [(1, "Part A: Identifies a response such as the invasion of Afghanistan in 2001 or the invasion of Iraq in 2003"),
     (1, "Part B: Identifies a response such as the USA Patriot Act, the creation of the Department of Homeland Security, or increased airport security"),
     (1, "Part C: Explains a controversy such as the debate over the claim that Iraq had weapons of mass destruction, the detention of prisoners at Guantanamo Bay, or surveillance and civil liberties")],
    "a) The United States invaded Afghanistan in 2001 to remove the Taliban government that sheltered al-Qaeda.\nb) Congress passed the USA Patriot Act, which expanded government surveillance and law enforcement powers.\nc) The invasion of Iraq in 2003 was controversial because the administration claimed Iraq had weapons of mass destruction, but none were found, and critics questioned the decision to go to war.")

B.save()
B.brief()
