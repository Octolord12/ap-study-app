from common import *

B = hard(9)
T_RC, T_EC, T_ET, T_WT, T_DC = ("reagan-and-conservatism", "end-of-cold-war", "economy-technology-globalization", "september-11-and-war-on-terror", "demographic-and-cultural-change")

# ---- The Reagan era and conservatism ----
B.mcq(T_RC, src("A historian, early twenty-first century", "“Despite campaigning against big government, the Reagan administration presided over rising federal deficits, as tax cuts and a defense buildup outpaced the spending cuts it achieved.”") + "\n\nWhich of the following best supports the historian's argument?",
      ch("The 1981 tax cuts and large increases in military spending coincided with growing federal budget deficits.", "Lower revenue and higher defense spending contributed to larger deficits."),
      [ch("President Reagan fired striking air traffic controllers in 1981.", "That concerned labor relations, not the deficit."),
       ch("The Moral Majority mobilized evangelical voters.", "That concerns political mobilization."),
       ch("The Iran-Contra affair was investigated by Congress.", "That concerns a scandal, not budget policy.")],
      "Tax cuts and defense spending increases coincided with growing deficits.")

B.mcq(T_RC, "The Republican victory in the 1994 midterm elections, associated with the Contract with America,",
      ch("gave Republicans control of both houses of Congress for the first time in decades, reflecting conservative gains and opposition to President Clinton's early agenda.", "The election was a major shift in congressional power."),
      [ch("gave Democrats a larger majority in the House.", "Republicans gained control."),
       ch("led to the impeachment of President Reagan.", "Reagan had left office in 1989."),
       ch("ended the two-party system.", "The system continued.")],
      "The 1994 elections shifted control of Congress to the Republicans.")

B.mcq(T_RC, "President Bill Clinton's approach as a New Democrat is best illustrated by",
      ch("his support for NAFTA, welfare reform and balanced budgets, which moved the Democratic Party toward the political center.", "Clinton adopted policies that appealed to moderates."),
      [ch("a call to expand the Great Society programs without change.", "Clinton moved away from traditional liberalism."),
       ch("his opposition to all free trade.", "He supported NAFTA."),
       ch("his proposal to abolish the income tax.", "Clinton did not propose that.")],
      "Clinton's centrist policies included NAFTA and welfare reform.")

# ---- The end of the Cold War ----
B.mcq(T_EC, src("A historian, early twenty-first century", "“Scholars disagree about why the Cold War ended. Some emphasize the pressure of American military spending and firm rhetoric; others argue that the internal weaknesses of the Soviet system and the reforms of Mikhail Gorbachev were decisive.”") + "\n\nWhich of the following best supports the second view described in the passage?",
      ch("The Soviet economy had stagnated, and Gorbachev's reforms unleashed forces within the Soviet Union and Eastern Europe that he could not control.", "Internal economic weakness and the effects of reform are the heart of the second view."),
      [ch("The United States proposed the Strategic Defense Initiative in 1983.", "That supports the view stressing American pressure."),
       ch("The United States increased defense spending in the early 1980s.", "That also supports the first view."),
       ch("NATO admitted new members in the late 1990s.", "That occurred after the Cold War ended.")],
      "Soviet internal problems and Gorbachev's reforms support the second view.")

B.mcq(T_EC, "The expansion of NATO in the 1990s to include former Warsaw Pact states",
      ch("extended the Western alliance eastward, which supporters saw as securing democracy and critics said provoked Russia.", "The expansion was controversial in Russia and in the West."),
      [ch("ended NATO as an organization.", "NATO continued and grew."),
       ch("was opposed by every Eastern European government.", "Many Eastern European governments sought membership."),
       ch("was a Soviet-led initiative.", "The Soviet Union no longer existed.")],
      "NATO's expansion eastward was supported by many but criticized by others.")

B.mcq(T_EC, "President George H. W. Bush ended the Gulf War after liberating Kuwait rather than invading Iraq because",
      ch("the coalition's authorized mission was limited to expelling Iraq from Kuwait, and he feared a long occupation and the breakup of the coalition.", "The administration wanted to keep the war's goals limited and the coalition united."),
      [ch("American forces had been defeated.", "The coalition had won a decisive victory."),
       ch("Congress had declared the war illegal.", "Congress had authorized force."),
       ch("the Soviet Union threatened to invade if the coalition advanced.", "That was not the reason.")],
      "Limited goals and coalition concerns led to the end of the war.")

# ---- Economy, technology and globalization ----
B.mcq(T_ET, src("A historian, early twenty-first century", "“Globalization lowered prices for consumers and created new export industries, but it also contributed to the decline of American manufacturing communities.”") + "\n\nWhich of the following best supports the second part of the historian's claim?",
      ch("Factory closings and lost manufacturing jobs in many Midwestern communities as production moved overseas and to Mexico.", "The loss of factory jobs in particular regions illustrates the decline of manufacturing communities."),
      [ch("The growth of the Internet in the 1990s.", "That concerns technology rather than the decline of manufacturing communities."),
       ch("The expansion of cheap imported goods in stores.", "That supports the claim about lower prices for consumers."),
       ch("The rise of the Silicon Valley technology industry.", "That reflects growth in one region, not decline elsewhere.")],
      "Factory closings in Midwestern communities show the decline of manufacturing.")

B.mcq(T_ET, "The dot-com boom and bust of the late 1990s and early 2000s",
      ch("reflected speculative investment in Internet companies, many of which failed when the bubble burst, although the Internet continued to reshape the economy.", "Overinvestment led to a market crash but did not end technological change."),
      [ch("showed that the Internet had no commercial value.", "The Internet continued to grow."),
       ch("occurred during the Great Depression.", "It occurred decades later."),
       ch("led to the end of personal computers.", "Computers continued to spread.")],
      "The dot-com bubble burst, yet the Internet continued to transform the economy.")

B.mcq(T_ET, "The Dodd-Frank Act of 2010 sought to",
      ch("increase regulation of the financial system, including by creating the Consumer Financial Protection Bureau, in response to the 2008 crisis.", "The law aimed to reduce the risk of another financial crisis."),
      [ch("abolish the Federal Reserve.", "The Federal Reserve remained."),
       ch("end all regulation of banks.", "The law increased regulation."),
       ch("create the Social Security system.", "Social Security was created in 1935.")],
      "Dodd-Frank expanded financial regulation after the 2008 crisis.")

# ---- September 11 and the war on terror ----
B.mcq(T_WT, src("A historian, early twenty-first century", "“After 2001, presidents of both parties asserted broad executive authority in national security matters, often without explicit new approval from Congress.”") + "\n\nWhich of the following best supports the historian's argument?",
      ch("Congress's 2001 Authorization for Use of Military Force was cited for many years to justify military action against terrorist groups in several countries.", "A single authorization was used to support a widening set of actions."),
      [ch("Congress passed the Gulf of Tonkin Resolution in 1964.", "That occurred decades earlier."),
       ch("The Department of Homeland Security was created in 2002.", "That shows institutional change but not an assertion of executive authority beyond congressional approval."),
       ch("The United States joined the United Nations in 1945.", "That occurred long before 2001.")],
      "The 2001 authorization was used to justify broad executive action.")

B.mcq(T_WT, "Which of the following best describes the aftermath of the 2003 invasion of Iraq?",
      ch("The overthrow of Saddam Hussein was followed by a prolonged insurgency and sectarian violence, which eroded American public support for the war.", "The occupation proved long and costly."),
      [ch("A quick, peaceful transition to a stable democracy.", "Violence continued for years."),
       ch("An immediate withdrawal of American forces within months.", "American forces remained for years."),
       ch("The discovery of large stockpiles of chemical weapons.", "Such stockpiles were not found.")],
      "A prolonged insurgency and violence followed the invasion.")

B.mcq(T_WT, "The Arab Spring of 2011 presented United States policymakers with",
      ch("the challenge of responding to popular uprisings against authoritarian governments, some of which were American allies.", "American leaders had to balance support for democratic aspirations with alliances."),
      [ch("a simple choice to support every government in the region.", "Responses varied by country."),
       ch("a united Middle East aligned with Soviet power.", "The Soviet Union no longer existed."),
       ch("an end to American involvement in the region.", "American involvement continued.")],
      "The Arab Spring raised difficult questions about supporting allies and democracy.")

# ---- Demographic and cultural change ----
B.mcq(T_DC, src("A governor's statement, 1994", "“Our state spends millions on services for people who entered the country illegally. The voters are saying enough. We must end public benefits for those here illegally.”") + "\n\nThe passage best reflects which of the following?",
      ch("Growing political conflict over immigration, as in California's Proposition 187.", "The statement reflects efforts to restrict benefits for undocumented immigrants."),
      [ch("The expansion of the Great Society.", "The statement calls for ending benefits."),
       ch("Support for the Immigration Act of 1965.", "The statement reflects a restrictive position."),
       ch("A call for open borders.", "The statement calls for restrictions.")],
      "The passage reflects the immigration debates of the 1990s.")

B.mcq(T_DC, "The Deferred Action for Childhood Arrivals program of 2012",
      ch("allowed certain undocumented immigrants who had arrived as children to remain temporarily and work, but did not provide a path to citizenship.", "The program offered temporary protection, not permanent status."),
      [ch("granted citizenship to all undocumented immigrants.", "It did not provide citizenship."),
       ch("ended all deportations.", "It applied to a limited group."),
       ch("was passed as a constitutional amendment.", "It was an executive action.")],
      "DACA offered temporary relief without citizenship.")

B.mcq(T_DC, "Which developments reflect the expansion of legal recognition of LGBTQ rights between 2003 and 2015?",
      ch("Lawrence v. Texas (2003), the repeal of Don't Ask, Don't Tell (2010) and Obergefell v. Hodges (2015).", "These events ended criminal penalties, allowed open military service and recognized same-sex marriage."),
      [ch("Plessy v. Ferguson, the Taft-Hartley Act and Roe v. Wade.", "These concern other issues and time periods."),
       ch("The Chinese Exclusion Act, the Dawes Act and the Sherman Act.", "These are nineteenth-century laws."),
       ch("The Civil Rights Act of 1964, the Voting Rights Act and Medicare.", "These are 1960s laws and are not about LGBTQ rights.")],
      "Lawrence, the repeal of Don't Ask, Don't Tell and Obergefell expanded LGBTQ rights.")

# ---- Short-answer and long-essay ----
saq(B, T_ET,
    "Use the excerpt to answer parts A, B and C.\n\n" + src("A homeowner's letter, 2009", "“We took a mortgage with a low starting rate that we could afford. When the rate rose and the house lost value, we owed more than it was worth, and we could not sell or refinance.”") + "\n\n**a)** Identify ONE cause of the financial crisis reflected in the excerpt.\n\n**b)** Explain ONE way in which the federal government responded to the financial crisis in the period 2008 to 2010.\n\n**c)** Explain ONE way in which the crisis and its aftermath affected American politics or society in the period 2008 to 2012.",
    [(1, "Part A: Identifies a cause such as risky mortgage lending, adjustable-rate mortgages, or the fall in home values after the housing bubble"),
     (1, "Part B: Explains a response such as the Troubled Asset Relief Program, the 2009 stimulus package or the Dodd-Frank financial regulation law"),
     (1, "Part C: Explains an effect such as widespread job loss and foreclosures, the rise of movements such as the Tea Party and Occupy Wall Street, or debates over the role of government in the economy")],
    "a) The letter describes an adjustable-rate mortgage whose payments rose as home values fell, showing how risky mortgage lending and falling prices contributed to the crisis.\nb) Congress passed the Troubled Asset Relief Program in 2008 to rescue banks, and in 2009 the government passed a stimulus package to boost the economy.\nc) The crisis led to widespread job losses and foreclosures and contributed to political movements such as the Tea Party and Occupy Wall Street, which expressed anger over government spending and Wall Street.")

leq(B, T_RC,
    "**Long Essay Question**\n\nEvaluate the extent to which conservatism changed the role of government in American life in the period 1980 to 2000.",
    "A strong response states a defensible thesis, for example that conservatism reduced taxes and regulation and changed the way Americans debated government's role, while major programs such as Social Security and Medicare remained and government continued to grow in some areas, such as defense. It places the topic in the context of the 1960s liberalism, stagflation and the backlash against federal expansion, uses specific evidence (the 1981 tax cuts, deregulation, the PATCO strike, the rise of the Religious Right, the 1994 elections and the Contract with America, the 1996 welfare reform, Clinton's New Democrat approach, deficits and defense spending), and uses continuity and change over time to weigh how far government's role actually changed.",
    "Thesis: Presents a defensible thesis that responds to the prompt and evaluates the extent to which conservatism changed government's role",
    "Contextualization: Places the topic in a broader context, such as the Great Society, stagflation or the backlash against 1960s liberalism",
    "Evidence: Provides at least two specific, accurate pieces of evidence relevant to the prompt (1 point for addressing the topic with evidence, 2nd point for using specific evidence to support the argument)",
    "Analysis and reasoning: Uses continuity and change over time to structure the argument (1 point), and demonstrates complex understanding, such as showing that conservative goals were achieved in some areas but that large programs and defense spending continued (2nd point)")

B.save()
B.brief()
