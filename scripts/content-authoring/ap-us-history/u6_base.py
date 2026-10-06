from common import *

B = base(6)
T_IB, T_LU, T_IU, T_WS, T_PJ = ("industrialization-and-business", "labor-and-unions", "immigration-and-urbanization", "western-settlement-and-native-americans", "politics-populism-and-jim-crow")

# ---- Industrialization and big business ----
B.mcq(T_IB, "The completion of the first transcontinental railroad in 1869 most directly",
      ch("linked eastern and western markets and encouraged settlement and the growth of a national economy.", "The railroad cut travel time and shipping costs across the continent."),
      [ch("ended the need for canals and steamboats in the East.", "Other forms of transportation continued to be used."),
       ch("connected the United States with Europe by land.", "The railroad crossed North America and did not connect the continents."),
       ch("was funded entirely by private investors without federal help.", "The federal government provided land grants and loans.")],
      "The transcontinental railroad tied national markets together.", difficulty="easy")

B.mcq(T_IB, "Andrew Carnegie's strategy of vertical integration meant that he",
      ch("controlled every stage of steel production, from raw materials and transportation to manufacturing.", "Owning each stage lowered costs and increased control."),
      [ch("bought up competing firms to control a single stage of production.", "That describes horizontal integration, a strategy used by Rockefeller."),
       ch("split his company into many small, independent businesses.", "Carnegie consolidated rather than split."),
       ch("placed his mills under government ownership.", "Carnegie's firms were privately owned.")],
      "Vertical integration meant control of all stages of production.", difficulty="medium")

B.mcq(T_IB, src("An industrialist's essay, 1889", "“The man who has gathered great wealth holds it as a trust for the community. Let him spend it in his lifetime on libraries, schools and parks, which help the worthy to help themselves, rather than on alms that encourage idleness.”") + "\n\nThe passage best reflects which of the following?",
      ch("The belief that wealthy individuals had a responsibility to use their fortunes for the public good, while opposing direct charity.", "This was the Gospel of Wealth, which justified great fortunes alongside philanthropy."),
      [ch("Support for government redistribution of wealth.", "The author wants individuals, not government, to spend wealth."),
       ch("A call for workers to form labor unions.", "The passage does not discuss unions."),
       ch("Socialist ideas calling for public ownership of industry.", "The author defends private fortunes.")],
      "The passage expresses the Gospel of Wealth.", difficulty="medium")

B.mcq(T_IB, "The Sherman Antitrust Act of 1890 was intended to",
      ch("prohibit monopolies and combinations that restrained trade, though it was weakly enforced at first.", "Congress responded to public fear of trusts, but courts and the government used the law cautiously."),
      [ch("break up all large corporations immediately.", "Large corporations continued to grow."),
       ch("set up federal ownership of railroads.", "The act did not provide federal ownership."),
       ch("protect labor unions from legal action.", "The act was often used against unions.")],
      "The Sherman Act aimed to stop monopolies but was weakly enforced.", difficulty="medium")

B.mcq(T_IB, "Which statement best describes the federal government's role in the economy during the Gilded Age?",
      ch("Government generally favored business through tariffs and land grants and took only cautious steps toward regulation, such as the Interstate Commerce Act.", "Laissez-faire attitudes dominated, with limited regulation."),
      [ch("Government regulated wages and prices in every industry.", "Government did not set wages and prices."),
       ch("Government owned and operated most major industries.", "Industry remained largely private."),
       ch("Government forbade corporations from growing beyond a fixed size.", "No such rule existed.")],
      "The government mostly supported business and regulated lightly.", difficulty="hard")

B.mcq(T_IB, "The Interstate Commerce Act of 1887 was passed mainly in response to",
      ch("complaints, especially from farmers, about unfair and discriminatory railroad rates; it created the Interstate Commerce Commission.", "The law was the first federal attempt to regulate the railroads."),
      [ch("a proposal to nationalize the steel industry.", "The act dealt with the railroads."),
       ch("a request by railroads for lower taxes.", "The act regulated railroads."),
       ch("a strike by railroad workers in Chicago.", "The act was not a response to a strike.")],
      "The act responded to complaints about railroad rates.", difficulty="medium")

# ---- Labor and unions ----
B.mcq(T_LU, "The American Federation of Labor under Samuel Gompers focused mainly on",
      ch("organizing skilled workers by craft to win better wages, hours and conditions through collective bargaining.", "The AFL pursued practical, workplace goals rather than broad political change."),
      [ch("organizing all unskilled workers into one large union.", "That describes the Knights of Labor."),
       ch("overthrowing the capitalist system.", "Gompers rejected revolutionary goals."),
       ch("establishing government ownership of industry.", "The AFL did not seek government ownership.")],
      "The AFL focused on skilled workers and bread-and-butter goals.", difficulty="easy")

B.mcq(T_LU, "The Knights of Labor differed from the American Federation of Labor in that the Knights",
      ch("tried to organize all workers, skilled and unskilled, and pursued broader reforms such as the eight-hour day.", "The Knights had an inclusive approach and wide reform goals."),
      [ch("organized only skilled craft workers.", "That describes the AFL."),
       ch("avoided all political goals.", "The Knights pursued political and social reforms."),
       ch("were created and funded by employers.", "They were a labor organization.")],
      "The Knights sought to unite all workers around broad goals.", difficulty="medium")

B.mcq(T_LU, src("A railway workers' leader, 1894", "“The company cut our wages by a quarter but not the rent on its houses nor the price of its goods. We have asked to be heard and been refused. We will not move the trains for a company that treats its workers so.”") + "\n\nWhich of the following was the most direct result of the events described in the passage?",
      ch("A federal court injunction and the use of federal troops to break the strike, showing the government's tendency to side with business.", "The government intervened to keep trains running and the strike collapsed."),
      [ch("Congress passed a law guaranteeing the right to strike.", "No such law was passed."),
       ch("The company agreed to raise wages and lower rents.", "The company refused concessions."),
       ch("The strike succeeded in winning union recognition.", "The strike was broken.")],
      "The Pullman Strike was ended by an injunction and troops.", difficulty="medium")

B.mcq(T_LU, "The Haymarket Affair of 1886 damaged the labor movement because",
      ch("a bombing at a labor rally led to a public backlash that linked unions to anarchism and violence.", "The Knights of Labor in particular lost members and public support."),
      [ch("the government agreed to the eight-hour day.", "The affair set back, not advanced, such demands."),
       ch("unions were made illegal by federal law.", "Unions were not outlawed."),
       ch("workers turned against the idea of striking and left unions entirely.", "The labor movement continued, though weakened.")],
      "The Haymarket bombing created a backlash against unions.", difficulty="medium")

B.mcq(T_LU, "Which factor best explains why labor unions struggled to win lasting gains in the Gilded Age?",
      ch("Employers used blacklists, strikebreakers, private police and court injunctions, and government often sided with business, while abundant immigrant labor weakened workers' bargaining power.", "Unions faced strong opposition from employers, courts and a plentiful supply of workers."),
      [ch("The Constitution banned unions.", "The Constitution did not ban unions."),
       ch("Workers had little interest in joining unions.", "Millions joined unions or took part in strikes."),
       ch("Employers voluntarily raised wages to prevent strikes.", "Employers more often resisted.")],
      "Employer tactics, government support for business and abundant labor limited unions.", difficulty="hard")

B.mcq(T_LU, "The Homestead Strike of 1892 against Carnegie Steel ended with",
      ch("the defeat of the union after armed clashes with Pinkerton guards and the arrival of the state militia, weakening unions in the steel industry.", "The company defeated the strike and unions lost ground in steel."),
      [ch("a federal law guaranteeing union recognition.", "No such law was passed."),
       ch("the nationalization of the steel mills.", "The mills stayed in private hands."),
       ch("a union victory and higher wages for all steelworkers.", "The union lost.")],
      "The strike was broken and the steel union weakened.", difficulty="hard")

# ---- Immigration and urbanization ----
B.mcq(T_IU, "Ellis Island, opened in 1892, was",
      ch("the main immigration station in New York Harbor, where arriving immigrants were processed.", "Millions of immigrants entered through Ellis Island."),
      [ch("a prison for convicted criminals.", "Ellis Island was an immigration station."),
       ch("a military base for the Union army.", "It was not a military base."),
       ch("the first capital of the United States.", "It was never the national capital.")],
      "Ellis Island was the main entry point for immigrants in the Northeast.", difficulty="easy")

B.mcq(T_IU, "Compared with earlier immigrants, the so-called new immigrants who arrived after the 1880s came largely from",
      ch("southern and eastern Europe, including Italy, Poland and Russia.", "Many were Catholics and Jews who differed in language and religion from earlier arrivals."),
      [ch("northern and western Europe, including Britain and Germany.", "That describes earlier immigration."),
       ch("Latin America and the Caribbean.", "Those were not the main sources of the new immigrants."),
       ch("sub-Saharan Africa.", "Africa was not a major source of voluntary migration.")],
      "New immigrants came largely from southern and eastern Europe.", difficulty="medium")

B.mcq(T_IU, src("A congressman's speech, 1882", "“The Chinese laborer, who works for wages no white man can live upon, threatens the American workman and cannot be assimilated to our institutions. Let this nation close its gates to him.”") + "\n\nThe attitudes expressed in the passage most directly contributed to which of the following?",
      ch("The Chinese Exclusion Act, the first federal law to ban immigration based on nationality.", "Anti-Chinese sentiment led Congress to pass the Exclusion Act in 1882."),
      [ch("The Dawes Act.", "That concerned Native American land."),
       ch("The Pendleton Civil Service Act.", "That concerned federal hiring."),
       ch("The Homestead Act.", "That concerned western land.")],
      "Anti-Chinese sentiment led to the Chinese Exclusion Act.", difficulty="medium")

B.mcq(T_IU, "Political machines such as Tammany Hall gained power in cities by",
      ch("providing jobs, services and help to immigrants in exchange for their votes, while often engaging in corruption.", "Machines built loyalty among immigrant voters through practical assistance."),
      [ch("opposing all immigration.", "Machines relied on immigrant votes."),
       ch("eliminating the use of patronage.", "Machines depended on patronage."),
       ch("promoting civil service reform.", "Machines opposed civil service reform.")],
      "Machines exchanged services for votes and often practiced corruption.", difficulty="medium")

B.mcq(T_IU, "Hull House, founded by Jane Addams in Chicago in 1889, was",
      ch("a settlement house that offered services such as childcare, education and health care to immigrants and the urban poor.", "Settlement houses helped newcomers adjust to city life."),
      [ch("a political machine that controlled Chicago's government.", "Hull House was a reform institution, not a machine."),
       ch("a factory that employed immigrant workers.", "It was a social service center."),
       ch("a prison for juvenile offenders.", "It was not a prison.")],
      "Hull House was a settlement house for immigrants and the urban poor.", difficulty="hard")

B.mcq(T_IU, "Which innovations most directly allowed American cities to grow upward and outward in the late 1800s?",
      ch("Steel-frame construction and elevators, which made skyscrapers possible, and electric streetcars, which extended commuting distance.", "New technology reshaped the urban landscape."),
      [ch("The automobile and the interstate highway.", "Those came much later."),
       ch("The telegraph and the printing press.", "These affected communication more than city form."),
       ch("The cotton gin and the steam engine.", "These were earlier innovations tied to other industries.")],
      "Steel frames, elevators and electric streetcars reshaped cities.", difficulty="hard")

# ---- Western settlement and Native Americans ----
B.mcq(T_WS, "The Homestead Act of 1862",
      ch("granted 160 acres of public land to settlers who farmed it for five years.", "The act encouraged western settlement."),
      [ch("gave free land to former Confederates.", "The act did not target former Confederates."),
       ch("banned settlement west of the Mississippi.", "It encouraged settlement."),
       ch("required settlers to buy land at high prices.", "The land was nearly free after five years of farming.")],
      "The Homestead Act offered public land to farmers.", difficulty="easy")

B.mcq(T_WS, "The Dawes Act of 1887 aimed to",
      ch("divide reservation land into individual plots in order to encourage Native Americans to farm and assimilate, which opened leftover land to white settlers and greatly reduced Native landholdings.", "The policy undermined communal landholding and led to major land loss."),
      [ch("return land to Native nations.", "The act reduced Native land."),
       ch("recognize tribal governments as sovereign.", "The act aimed to dismantle tribal land systems."),
       ch("end the reservation system.", "Reservations continued.")],
      "The Dawes Act promoted assimilation and led to significant loss of Native land.", difficulty="medium")

B.mcq(T_WS, src("A Native leader at a surrender council, 1870s", "“The buffalo are gone and our people are hungry. The soldiers have burned our camps and our children are cold. I am tired of fighting, and I will lead my people no further against you.”") + "\n\nThe passage best reflects which of the following?",
      ch("The use of military force and the destruction of the buffalo to confine Native peoples to reservations.", "Military campaigns and the loss of the buffalo broke Native resistance."),
      [ch("A voluntary agreement in which Native nations traded their land for goods.", "The speaker describes defeat and hunger."),
       ch("The success of Native armies in defeating the United States.", "The speaker is surrendering."),
       ch("A federal policy of protecting Native hunting rights.", "The passage describes the destruction of the buffalo and camps.")],
      "The passage shows how military force and loss of the buffalo ended Native resistance.", difficulty="medium")

B.mcq(T_WS, "Frederick Jackson Turner's 1893 frontier thesis argued that",
      ch("the frontier had shaped American democracy and individualism, and the end of the frontier marked a turning point in national history.", "Turner linked American character to westward expansion."),
      [ch("the frontier had no effect on American values.", "Turner argued the frontier was central."),
       ch("Native peoples were the main creators of American democracy.", "Turner did not make that argument."),
       ch("the frontier would never close.", "Turner pointed to the 1890 census announcing the end of a continuous frontier line.")],
      "Turner's thesis connected the frontier to American democracy and individualism.", difficulty="medium")

B.mcq(T_WS, "Which statement best describes farmers' economic problems in the late 1800s?",
      ch("Falling crop prices, high railroad rates and mortgage debt squeezed many farmers, especially in the South and West.", "Farmers faced deflation and debts that made it hard to profit."),
      [ch("Rising crop prices made most farmers wealthy.", "Prices fell in this period."),
       ch("Railroads offered low rates and plentiful credit.", "Farmers complained of high rates."),
       ch("Farmers were protected by strong federal price supports.", "Price supports came later.")],
      "Falling prices, high rates and debt created widespread farm distress.", difficulty="hard")

B.mcq(T_WS, "The Exodusters of 1879 were",
      ch("African Americans who migrated from the South to Kansas to escape racial violence and seek economic opportunity.", "Thousands left after the end of Reconstruction in search of land and safety."),
      [ch("Chinese laborers who built the transcontinental railroad.", "The Exodusters were African American migrants."),
       ch("Mormon settlers who moved to Utah.", "The Mormon migration was in the 1840s."),
       ch("Native Americans forced to leave their homelands.", "They were African American migrants who left voluntarily.")],
      "The Exodusters left the South for Kansas seeking safety and opportunity.", difficulty="hard")

# ---- Politics, Populism and Jim Crow ----
B.mcq(T_PJ, "The Pendleton Civil Service Act of 1883",
      ch("created a merit-based system for hiring some federal employees, in response to patronage abuses and the assassination of President Garfield.", "The law began to reduce the spoils system."),
      [ch("abolished all federal jobs.", "The act reformed hiring."),
       ch("gave the president unlimited power to fire officials.", "The act reduced patronage power."),
       ch("created the Interstate Commerce Commission.", "That was done in 1887.")],
      "The Pendleton Act started civil service reform.", difficulty="easy")

B.mcq(T_PJ, "The Populist Party's Omaha Platform of 1892 called for",
      ch("free coinage of silver, a graduated income tax, direct election of senators and government ownership of railroads.", "The platform aimed to relieve farmers and limit corporate power."),
      [ch("the elimination of all income taxes.", "Populists wanted an income tax on the wealthy."),
       ch("a ban on labor unions.", "Populists sought allies among workers."),
       ch("the repeal of the Fourteenth Amendment.", "The platform did not call for that.")],
      "The Omaha Platform proposed economic and political reforms.", difficulty="medium")

B.mcq(T_PJ, src("A presidential candidate's convention speech, 1896", "“The farmer and the wage earner are the foundation of our prosperity. We will not allow them to be crushed beneath a gold standard that serves the banks of the East.”") + "\n\nThe passage best reflects which of the following?",
      ch("Agrarian demands to expand the money supply through the coinage of silver in order to ease the burden of debt.", "The speaker attacks the gold standard on behalf of farmers and workers."),
      [ch("Support for a stronger gold standard.", "The speaker opposes the gold standard."),
       ch("A call for the creation of a new national bank.", "The speaker does not call for a bank."),
       ch("A defense of high tariffs for manufacturers.", "The passage concerns the money supply.")],
      "The speech attacked the gold standard and promoted silver coinage.", difficulty="medium")

B.mcq(T_PJ, "In Plessy v. Ferguson (1896), the Supreme Court",
      ch("upheld racial segregation under the doctrine of separate but equal.", "The decision gave legal cover to Jim Crow laws."),
      [ch("struck down segregation in public schools.", "That was Brown v. Board of Education in 1954."),
       ch("overturned the Fourteenth Amendment.", "The Court did not overturn the amendment."),
       ch("declared poll taxes unconstitutional.", "The Court did not do that in this case.")],
      "Plessy allowed segregation if facilities were called equal.", difficulty="medium")

B.mcq(T_PJ, "Southern states used poll taxes, literacy tests and grandfather clauses to",
      ch("prevent African Americans from voting without directly violating the Fifteenth Amendment.", "The measures looked race-neutral on paper but were applied to exclude Black voters."),
      [ch("expand Black voting rights.", "The measures reduced Black voting."),
       ch("comply with federal voting rights laws.", "They were methods of evading the amendment."),
       ch("encourage immigration to the South.", "They were aimed at limiting voters.")],
      "These devices disfranchised Black voters while avoiding direct mention of race.", difficulty="hard")

B.mcq(T_PJ, "Booker T. Washington's Atlanta Compromise address of 1895 argued that",
      ch("African Americans should focus on economic self-improvement and vocational education and accept social segregation for the time being.", "Washington urged patience on civil rights in exchange for economic opportunity."),
      [ch("African Americans should demand immediate political and social equality.", "That was closer to the position of W. E. B. Du Bois."),
       ch("African Americans should leave the United States.", "Washington did not call for leaving."),
       ch("African Americans should avoid all education.", "Washington promoted vocational education.")],
      "Washington advocated economic advancement and accommodation to segregation.", difficulty="hard")

# ---- Short-answer questions ----
saq(B, T_IB,
    "Use the excerpt to answer parts A, B and C.\n\n" + src("A historian, early twenty-first century", "“The industrial boom of the late nineteenth century created both unprecedented wealth and unprecedented conflict. The same system that built fortunes for a few left many workers insecure and angry.”") + "\n\n**a)** Identify ONE claim made by the historian.\n\n**b)** Explain ONE development in the period 1865 to 1898 that supports the historian's claim about the creation of great wealth.\n\n**c)** Explain ONE way in which workers or reformers responded to the conflicts described in the excerpt in the period 1865 to 1898.",
    [(1, "Part A: Identifies a claim, such as that industrialization produced both great wealth and conflict, or that it left many workers insecure"),
     (1, "Part B: Explains a development such as the expansion of railroads, consolidation of industries such as steel and oil, or technological innovation that allowed a few industrialists to build vast fortunes"),
     (1, "Part C: Explains a response such as the growth of unions like the Knights of Labor and the AFL, strikes such as Homestead and Pullman, or the Populist movement and political reform proposals")],
    "a) The historian argues that industrialization created great wealth for some people and also created conflict because many workers felt insecure.\nb) Industrialists such as Carnegie and Rockefeller used railroads and consolidation of production to build enormous steel and oil businesses that produced huge fortunes.\nc) Workers formed unions such as the Knights of Labor and the American Federation of Labor and carried out strikes such as the Homestead Strike to demand better wages and conditions.")

saq(B, T_PJ,
    "Use the excerpt to answer parts A, B and C.\n\n" + src("A farmers' convention platform, 1892", "“We believe that the money of the country should be expanded to relieve debtors, that the railroads should be owned by the people, and that senators should be chosen by direct vote of the people rather than by legislatures controlled by corporations.”") + "\n\n**a)** Identify ONE grievance expressed in the excerpt.\n\n**b)** Explain ONE way in which the demands in the excerpt reflected economic conditions faced by farmers in the late 1800s.\n\n**c)** Explain ONE reason that the Populist movement declined after 1896.",
    [(1, "Part A: Identifies a grievance such as debt, the power of railroads or corporate influence over legislatures"),
     (1, "Part B: Explains a connection such as falling crop prices and deflation making debts harder to repay, so farmers wanted more money in circulation, or high railroad rates motivating a call for public ownership"),
     (1, "Part C: Explains a reason such as the defeat of William Jennings Bryan in 1896, the Democratic Party absorbing the silver issue, or improving economic conditions and new gold discoveries")],
    "a) The platform objects to the burden of debt on farmers and to corporate influence over government.\nb) Crop prices were falling, so farmers' debts became harder to repay, and they wanted an expanded money supply and public ownership of railroads whose rates they believed were unfair.\nc) Populism declined after Bryan, backed by the Populists and Democrats, lost the election of 1896, and the Democratic Party absorbed the silver issue.")

saq(B, T_IU,
    "Using your knowledge of United States history, answer parts A, B and C.\n\n**a)** Identify ONE reason that immigrants came to the United States in the period 1865 to 1900.\n\n**b)** Identify ONE challenge that immigrants faced in American cities in the same period.\n\n**c)** Explain ONE way in which nativists or the federal government responded to immigration in the period 1865 to 1900.",
    [(1, "Part A: Identifies a reason such as economic opportunity, escape from poverty, or escape from religious persecution such as pogroms against Jews"),
     (1, "Part B: Identifies a challenge such as crowded tenement housing, low wages, discrimination or cultural adjustment"),
     (1, "Part C: Explains a response such as the Chinese Exclusion Act of 1882 limiting immigration, or nativist organizations calling for restrictions on immigration")],
    "a) Many immigrants came to the United States seeking jobs in growing industries and cities.\nb) Many immigrants lived in crowded tenements with poor sanitation and worked for low wages.\nc) In 1882 Congress passed the Chinese Exclusion Act, which banned the immigration of Chinese laborers in response to anti-Chinese prejudice and economic competition fears.")

B.save()
B.brief()
