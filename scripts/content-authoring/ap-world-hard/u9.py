from common import *

B = bank(9, "unit-9-globalization")
T_TECH, T_RIGHTS, T_CULT, T_ENV, T_ECON = ("technological-advances", "rights-based-movements", "globalized-culture", "environment-and-globalization", "economic-globalization")

B.mcq(T_TECH, "Which statement best describes the Green Revolution of the mid-twentieth century?",
      ch("The use of high-yield crop varieties, fertilizers and irrigation to increase food production in parts of Asia and Latin America, which also brought environmental and social costs.", "The Green Revolution raised crop yields and helped feed growing populations, but it depended on costly inputs and had environmental consequences."),
      [ch("A political movement to restore forests in Europe.", "The term refers to agricultural technology, not a forest-protection movement."),
       ch("The development of nuclear power plants for farming.", "The Green Revolution was not about nuclear power."),
       ch("A return to traditional farming methods without fertilizers or machinery.", "It involved modern inputs, not traditional methods alone.")],
      "The Green Revolution used improved seeds and inputs to increase yields.")

B.mcq(T_TECH, src("Statement by a telecommunications executive, 1999", "“With the internet and satellite links, a firm in one country can employ designers in a second, build its product in a third, and sell to customers in a fourth, all within a single working day.”") + "\n\nThe passage best illustrates which effect of technological change in the late twentieth century?",
      ch("Communication and transport technologies reduced the importance of distance and enabled the global organization of production and services.", "New technologies let firms coordinate across borders, supporting outsourcing and global supply chains."),
      [ch("A return to local self-sufficiency in production.", "The passage describes production spread across countries."),
       ch("A decline in the role of multinational firms.", "The passage describes firms operating internationally."),
       ch("The closing of national borders to trade.", "The passage describes cross-border activity.")],
      "The passage shows technology enabling global production networks.")

B.mcq(T_RIGHTS, src("Article 1 of a declaration adopted by the United Nations General Assembly, 1948", "“All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act toward one another in a spirit of brotherhood.”") + "\n\nThe declaration is best understood as which of the following?",
      ch("A statement of basic rights that later movements invoked, though the declaration itself is not a legally binding treaty.", "The Universal Declaration of Human Rights set out a common standard, and activists and later treaties drew on it."),
      [ch("A binding treaty that created an international police force to enforce human rights.", "The declaration was not a binding treaty and did not create such a force."),
       ch("A document written by the League of Nations in 1919.", "It was adopted by the United Nations in 1948."),
       ch("A statement that rights depend on a person's nationality and social class.", "The passage states that all human beings are born free and equal.")],
      "The declaration set a standard of human rights, although it is not legally binding.")

B.mcq(T_RIGHTS, "Which statement best describes a development in women's rights in the twentieth century?",
      ch("Many countries extended voting rights to women, and movements campaigned for greater legal, educational and economic equality.", "Women gained the vote in many countries during the first half of the century, and later movements pressed for equality in other areas."),
      [ch("No country allowed women to vote until the twenty-first century.", "Women won the vote in many countries in the early twentieth century."),
       ch("Women's rights movements disappeared after World War II.", "Women's movements continued and grew in the later twentieth century."),
       ch("All countries gave women full legal equality by 1900.", "Full equality was not achieved by 1900, and it is still an ongoing goal in many places.")],
      "Suffrage and later campaigns for equality expanded women's rights.")

B.mcq(T_RIGHTS, "Which statement best compares the civil rights movement in the United States with the anti-apartheid struggle in South Africa?",
      ch("Both challenged legal racial discrimination through protests, boycotts and appeals to public opinion, and the anti-apartheid movement also relied on international sanctions and pressure.", "Both movements fought laws that enforced racial inequality, and external pressure played a notable role in South Africa."),
      [ch("Both movements aimed to establish racial segregation.", "Both opposed segregation."),
       ch("Neither movement used nonviolent methods.", "Nonviolent protest was central to the American movement and used by many in the South African struggle."),
       ch("The civil rights movement took place in South Africa and the anti-apartheid movement in the United States.", "The locations are the reverse.")],
      "Both opposed racial discrimination; the South African struggle also drew on international sanctions.")

B.mcq(T_CULT, src("A cultural critic, 1990s", "“Wherever you travel, you find the same fast-food chains, the same Hollywood films and the same pop songs on the radio. Local traditions are being swept away by a single global culture.”") + "\n\nWhich evidence would best challenge the critic's claim?",
      ch("Evidence that people often adapt global cultural products to local tastes, and that local music and film industries, such as Bollywood, have also found global audiences.", "Cultural exchange runs in several directions, and local cultures often blend or reinterpret global influences."),
      [ch("Evidence that the same fast-food chains operate in many countries.", "This supports the critic's claim."),
       ch("Evidence that Hollywood films are shown around the world.", "This also supports the critic."),
       ch("Evidence that local languages are disappearing in many places.", "This supports the claim that local traditions are declining.")],
      "Evidence of adaptation and of two-way cultural flows challenges the idea of one global culture.")

B.mcq(T_ENV, "Which statement best explains why environmental problems such as climate change require international cooperation?",
      ch("Greenhouse gas emissions and other pollution cross borders and affect the whole planet, so no single country can solve the problem alone.", "Climate agreements such as the Kyoto Protocol and the Paris Agreement reflect the need for coordinated action."),
      [ch("Climate change is unaffected by human activity and industrialization.", "Scientific evidence links industrial emissions to climate change."),
       ch("Only developing countries produce greenhouse gases.", "Industrialized and developing countries both produce emissions."),
       ch("International agreements can compel every nation to act through a world government.", "No world government exists, and agreements depend on states' voluntary participation.")],
      "Pollution and climate change are transnational problems.")

B.mcq(T_ENV, src("A scientific report, 1980s", "“The chemicals used in refrigerators and aerosol sprays are destroying the layer of ozone above the poles. Unless their production is halted, ultraviolet radiation reaching the surface will increase and harm people and ecosystems.”") + "\n\nWhich international response is most directly connected to the concern described in the passage?",
      ch("The Montreal Protocol (1987), an agreement to phase out substances that deplete the ozone layer, often cited as a successful example of international environmental cooperation.", "States agreed to reduce and eliminate ozone-depleting chemicals, and the ozone layer has begun to recover."),
      [ch("The Kyoto Protocol, which dealt with the destruction of the rainforests in Brazil.", "The Kyoto Protocol (1997) dealt with greenhouse gas emissions."),
       ch("The establishment of the League of Nations.", "The League of Nations was created after World War I."),
       ch("The Treaty of Versailles.", "The Treaty of Versailles ended World War I.")],
      "The Montreal Protocol addressed ozone-depleting chemicals.")

B.mcq(T_ECON, "The creation of the World Trade Organization (1995) and regional agreements such as NAFTA (1994) reflect which trend?",
      ch("Efforts to reduce trade barriers and promote the movement of goods, services and capital across borders.", "These institutions and agreements aimed to expand trade by lowering tariffs and setting rules."),
      [ch("A return to mercantilist policies of high tariffs and strict state control of trade.", "These agreements reduced barriers."),
       ch("A movement to end all international trade.", "They promoted trade."),
       ch("A plan to make all countries adopt the same currency immediately.", "These agreements did not create a single currency.")],
      "The WTO and trade agreements promoted freer trade.")

B.mcq(T_ECON, "Which statement best explains why many corporations moved manufacturing to developing countries in the late twentieth century?",
      ch("Lower labor costs and fewer regulations, together with improvements in transportation and communications, made it profitable to produce goods abroad.", "Companies could reduce costs and coordinate production across long distances."),
      [ch("Labor costs were much higher in developing countries.", "Lower labor costs were a primary reason."),
       ch("Governments in developing countries banned all foreign trade.", "Many developing countries welcomed foreign investment."),
       ch("The invention of the steam engine made overseas production possible for the first time.", "The shift followed late twentieth-century developments in transport and communication.")],
      "Cost advantages and better technology encouraged global production.")

B.mcq(T_ECON, src("A statement by critics of economic globalization, 1999", "“The free movement of capital has let corporations shift factories to wherever wages are lowest and protections weakest, while local farmers and workers are left to compete against giants. The gap between rich and poor grows wider each year.”") + "\n\nWhich criticism of economic globalization is best reflected in the passage?",
      ch("It can increase inequality, weaken workers' protections and local industries, and give multinational corporations too much power.", "Critics argued that globalization benefits large corporations while harming workers and small producers."),
      [ch("It reduces all trade and isolates economies.", "The passage criticizes the free movement of capital, not isolation."),
       ch("It strengthens governments' control over corporations.", "The passage argues that corporations gain power."),
       ch("It eliminates the gap between rich and poor.", "The passage claims the gap is growing.")],
      "The passage reflects concerns about inequality and corporate power.")

B.mcq(T_TECH, "Which statement best explains why diseases such as HIV/AIDS and COVID-19 spread rapidly across the world in the late twentieth and early twenty-first centuries?",
      ch("Increased global travel, trade and urbanization allowed pathogens to spread quickly between regions.", "Faster and more frequent movement of people carried diseases across borders."),
      [ch("Countries had become more isolated from one another.", "Greater connectivity, not isolation, accelerated the spread."),
       ch("Medical research stopped in the twentieth century.", "Medical research advanced, although it did not prevent every pandemic."),
       ch("Diseases spread only through wars between nations.", "Disease spread through travel and trade as well as through conflict.")],
      "Global connectivity speeds the spread of diseases.")

B.mcq(T_RIGHTS, "Which statement best describes the Arab Spring that began in 2010-2011?",
      ch("A wave of protests against authoritarian governments in the Middle East and North Africa, aided by social media, which led to varied outcomes in different countries.", "The protests began in Tunisia and spread to other countries, with some governments falling, others surviving and some countries suffering civil war."),
      [ch("A series of revolts led by the Soviet Union against Ottoman rule.", "The Soviet Union and the Ottoman Empire were not involved in these events."),
       ch("A single election in one country that changed the region.", "The Arab Spring was a series of protest movements across several countries."),
       ch("A movement that produced democracy in every country where it occurred.", "Outcomes varied widely, and many countries did not become democracies.")],
      "The Arab Spring was a wave of protests with varied results.")

B.mcq(T_CULT, "Which statement best explains the growth of immigrant communities in Europe and North America after World War II?",
      ch("Migration from former colonies and developing countries, where people sought economic opportunity or fled conflict, and the demand for labor in industrialized countries.", "Both economic and political factors encouraged migration to wealthier countries."),
      [ch("Governments in Europe and North America forbade all immigration after World War II.", "Many governments allowed or recruited immigrant workers."),
       ch("All immigrants moved from Europe to Asia.", "Large movements went from Asia, Africa and Latin America to Europe and North America."),
       ch("Immigration was caused by the collapse of the global economy in 1950.", "Postwar economic growth increased the demand for workers.")],
      "Economic opportunity, labor demand and conflict drove postwar migration.")

B.mcq(T_ECON, "Which statement best describes China's economic policies after 1978 under Deng Xiaoping?",
      ch("The government introduced market-oriented reforms and opened the country to foreign investment while maintaining Communist Party political control, leading to rapid economic growth.", "China combined economic liberalization with one-party rule."),
      [ch("China abandoned all trade and returned to complete self-sufficiency.", "China opened to foreign trade and investment."),
       ch("China ended Communist Party rule and became a multiparty democracy.", "The Communist Party retained power."),
       ch("China collectivized all agriculture and banned private enterprise.", "The reforms ended collectivization and permitted private enterprise.")],
      "The reforms opened the economy while the Communist Party kept power.")

saq(B, T_CULT,
    "Use the passage to answer parts A, B and C.\n\n" + src("A cultural critic, 1990s", "“Wherever you travel, you find the same fast-food chains, the same Hollywood films and the same pop songs on the radio. Local traditions are being swept away by a single global culture.”") + "\n\n**a)** Identify ONE concern expressed by the critic.\n\n**b)** Explain ONE development since 1950 that helped spread the global cultural products described in the passage.\n\n**c)** Explain ONE way in which local cultures have responded to or influenced global culture.",
    [(1, "Part A: Identifies a concern such as the loss of local traditions or the dominance of a single global culture"),
     (1, "Part B: Explains a development such as satellite television and the internet, cheaper air travel, multinational corporations and advertising, or trade agreements that opened markets"),
     (1, "Part C: Explains a response or influence such as adapting global products to local tastes, the global popularity of local forms (such as Bollywood films or K-pop), or movements to protect local languages and traditions")],
    "a) The critic is concerned that local traditions are being replaced by a uniform global culture dominated by a few brands and industries.\nb) Satellite television, the internet and cheaper travel and communication, along with the global advertising and distribution networks of multinational corporations, made it easy to spread products such as American films and fast food worldwide.\nc) Local cultures often adapt global products to local tastes, such as restaurant chains offering regional menu items, and some local forms of culture, such as Bollywood films or Korean pop music, have gained audiences around the world.")

leq(B, T_RIGHTS,
    "**Long Essay Question**\n\nEvaluate the extent to which rights-based movements changed societies in TWO of the following regions between 1900 and the present: the United States, South Africa, India, the Middle East.",
    "A strong response takes a position (for example that rights-based movements brought major legal changes in the United States and South Africa but that social and economic inequalities persisted). It places the topic in context (decolonization, the Cold War and the spread of human rights ideas) and uses specific evidence such as the civil rights movement and the Civil Rights Act, the Universal Declaration of Human Rights, the anti-apartheid struggle and the 1994 elections, women's suffrage, or the Arab Spring. It analyzes change and continuity and the role of international influences.",
    "Thesis: Presents a defensible thesis that responds to the prompt and evaluates the extent of change brought by rights-based movements in two regions",
    "Contextualization: Describes broader context, such as decolonization, the Cold War or the spread of human rights ideas",
    "Evidence: Provides at least two specific, accurate examples for each region (1 point for addressing the topic, 2nd point for using specific evidence to support the argument)",
    "Analysis and reasoning: Uses continuity and change over time to structure the argument (1 point), and shows complexity by noting remaining inequalities or the role of international pressure (2nd point)")

B.save()
B.brief()
