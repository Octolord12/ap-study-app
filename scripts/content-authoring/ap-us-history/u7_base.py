from common import *

B = base(7)
T_IM, T_PR, T_W1, T_TW, T_DN, T_W2 = ("imperialism-and-spanish-american-war", "progressive-era", "world-war-one", "twenties-and-culture", "depression-and-new-deal", "world-war-two")

# ---- Imperialism and the Spanish-American War ----
B.mcq(T_IM, "As a result of the Spanish-American War of 1898, the United States",
      ch("gained control of the Philippines, Guam and Puerto Rico and emerged as a major world power.", "The Treaty of Paris transferred Spanish territories to the United States."),
      [ch("annexed Cuba as a state.", "Cuba became formally independent, though under American influence."),
       ch("lost control of Hawaii.", "Hawaii was annexed by the United States in 1898."),
       ch("agreed to pay Spain for damages.", "The United States paid Spain for the Philippines but did not pay damages.")],
      "The war gave the United States overseas possessions and greater power.", difficulty="easy")

B.mcq(T_IM, "Yellow journalism contributed to the outbreak of the Spanish-American War by",
      ch("publishing sensational stories about Spanish brutality in Cuba that inflamed public opinion.", "Newspapers competing for readers fueled demands for action."),
      [ch("reporting that Spain had accepted all American demands.", "The press stirred anger, not calm."),
       ch("urging Americans to remain neutral in the conflict.", "Yellow journalism promoted intervention."),
       ch("hiding the sinking of the USS Maine from the public.", "Papers gave the sinking wide and dramatic coverage.")],
      "Sensational newspapers built public pressure for war.", difficulty="medium")

B.mcq(T_IM, src("A naval strategist's essay, 1890s", "“The nation that wishes to hold a place among the great powers must have a strong navy, coaling stations abroad and markets overseas, for the future of commerce lies upon the sea.”") + "\n\nThe passage best reflects which of the following?",
      ch("Arguments that economic and strategic interests justified building a navy and acquiring overseas territories.", "The author links naval power, bases and trade to national greatness."),
      [ch("A demand that the United States avoid all foreign involvement.", "The author calls for overseas expansion."),
       ch("A defense of laissez-faire economics at home.", "The passage concerns foreign policy."),
       ch("Support for disarmament.", "The author promotes building a strong navy.")],
      "The passage expresses the strategic and commercial case for imperialism.", difficulty="medium")

B.mcq(T_IM, "The Open Door notes of 1899 and 1900 asked the great powers to",
      ch("respect equal trading opportunities in China and preserve its territorial integrity.", "The United States wanted access to Chinese markets without partitioning China."),
      [ch("divide China into exclusive spheres of influence.", "The notes opposed exclusive spheres."),
       ch("withdraw all trade from China.", "The notes sought open trade."),
       ch("recognize American control of China.", "The notes did not claim American control.")],
      "The Open Door policy sought equal access to China's markets.", difficulty="medium")

B.mcq(T_IM, "Opponents of acquiring the Philippines, such as members of the Anti-Imperialist League, argued that",
      ch("ruling people without their consent contradicted American principles of self-government.", "Anti-imperialists said empire betrayed the nation's founding ideals."),
      [ch("the Philippines had no strategic or economic value.", "Many opponents focused on principle rather than value."),
       ch("the United States should annex all of Asia.", "Opponents rejected expansion."),
       ch("Spain should keep its colonies forever.", "Opponents did not argue for preserving Spanish rule.")],
      "Anti-imperialists argued that colonial rule violated the principle of consent.", difficulty="hard")

# ---- The Progressive Era ----
B.mcq(T_PR, "Muckrakers such as Upton Sinclair and Ida Tarbell",
      ch("used investigative journalism to expose corruption, unsafe food and business abuses.", "Their reporting aroused public support for reform."),
      [ch("defended large corporations against criticism.", "Muckrakers criticized abuses."),
       ch("opposed all reform movements.", "They supported reform."),
       ch("supported the spoils system.", "They criticized corrupt politics.")],
      "Muckrakers exposed problems and encouraged reform.", difficulty="easy")

B.mcq(T_PR, "Upton Sinclair's novel The Jungle (1906) most directly led to",
      ch("passage of the Meat Inspection Act and the Pure Food and Drug Act.", "Public outrage over conditions in meatpacking helped build support for federal regulation."),
      [ch("the creation of the Federal Reserve.", "That was passed in 1913 and was a banking reform."),
       ch("the Sherman Antitrust Act.", "That was passed in 1890."),
       ch("the end of child labor.", "Child labor was not ended by that law.")],
      "The Jungle prompted federal food and drug regulation.", difficulty="medium")

B.mcq(T_PR, src("A reform governor's address, 1905", "“The people must be given the tools to govern themselves directly: to propose laws by initiative, to approve them by referendum and to remove corrupt officials by recall, so that the interests of the many are not sold to the few.”") + "\n\nThe passage best reflects which of the following?",
      ch("Progressive efforts to make government more democratic and responsive to ordinary citizens.", "Initiative, referendum and recall were reforms that gave voters more direct power."),
      [ch("Support for the spoils system.", "The speaker wants to remove corrupt officials."),
       ch("Opposition to democratic reforms.", "The speaker supports them."),
       ch("A defense of laissez-faire economics.", "The passage concerns political reform.")],
      "The passage reflects Progressive democratic reforms.", difficulty="medium")

B.mcq(T_PR, "Theodore Roosevelt's approach to big business is best described as",
      ch("distinguishing between good and bad trusts, regulating or prosecuting those that harmed the public, as in the Northern Securities case.", "Roosevelt used federal power selectively against abusive combinations."),
      [ch("prosecuting every large corporation without exception.", "Roosevelt did not oppose all large business."),
       ch("taking no action against any corporation.", "He prosecuted trusts."),
       ch("placing all industries under government ownership.", "He did not support government ownership.")],
      "Roosevelt targeted abusive trusts while accepting large corporations.", difficulty="medium")

B.mcq(T_PR, "Which pair of constitutional amendments best reflects Progressive goals of making government more democratic?",
      ch("The Seventeenth, providing for the direct election of senators, and the Nineteenth, giving women the right to vote.", "Both extended the people's direct role in government."),
      [ch("The Thirteenth and Fourteenth, abolishing slavery and defining citizenship.", "Those are Reconstruction-era amendments."),
       ch("The Fifteenth and Eighteenth, protecting voting and banning alcohol.", "The Eighteenth concerned Prohibition, a different Progressive goal."),
       ch("The Tenth and Twelfth, reserving state powers and revising the Electoral College.", "These do not reflect Progressive-era democratic reforms.")],
      "The Seventeenth and Nineteenth Amendments expanded democratic participation.", difficulty="hard")

# ---- World War I ----
B.mcq(T_W1, "The Zimmermann Telegram of 1917 was",
      ch("a secret German proposal for a military alliance with Mexico against the United States, which, along with unrestricted submarine warfare, helped bring the United States into the war.", "The message angered Americans when it was made public."),
      [ch("an American request for a peace conference.", "It was a German message."),
       ch("a British declaration of war on Germany.", "It was not a declaration of war."),
       ch("a French offer of military aid to the United States.", "It was a German proposal to Mexico.")],
      "The Zimmermann Telegram and submarine warfare pushed the United States toward war.", difficulty="easy")

B.mcq(T_W1, "In Schenck v. United States (1919), the Supreme Court",
      ch("upheld limits on free speech during wartime when speech posed a clear and present danger.", "The Court allowed conviction under the Espionage Act for antiwar leaflets."),
      [ch("struck down the Espionage Act.", "The Court upheld the conviction."),
       ch("ruled that free speech cannot be limited under any circumstances.", "The Court recognized limits."),
       ch("ended American involvement in the war.", "The case did not affect the war.")],
      "Schenck allowed wartime limits on speech that created a clear and present danger.", difficulty="medium")

B.mcq(T_W1, src("A Black newspaper editorial, 1917", "“The mills of the North are calling for workers, and thousands of our people are answering. They go for better wages, and to leave behind the lynch rope and the poor schools of the South.”") + "\n\nThe passage best reflects which of the following developments?",
      ch("The Great Migration, in which wartime labor demand and the desire to escape southern racism drew African Americans to northern cities.", "The editorial links northern jobs and the escape from southern conditions to a mass movement north."),
      [ch("The return of African Americans to the rural South.", "The passage describes a movement north."),
       ch("The end of racial discrimination in northern cities.", "Discrimination continued in the North."),
       ch("A government policy of forced relocation.", "The migration was voluntary.")],
      "The passage describes the Great Migration.", difficulty="medium")

B.mcq(T_W1, "Woodrow Wilson's Fourteen Points called for",
      ch("self-determination for peoples, free trade, open diplomacy and a League of Nations to keep the peace.", "Wilson outlined principles for a postwar settlement."),
      [ch("harsh punishment and large reparations for Germany.", "Those were demands of some Allied leaders, not the Fourteen Points."),
       ch("a return to isolationism.", "Wilson called for a League of Nations."),
       ch("the creation of new colonies for the Allies.", "The points called for self-determination.")],
      "The Fourteen Points proposed principles including a League of Nations.", difficulty="medium")

B.mcq(T_W1, "The Senate rejected the Treaty of Versailles largely because",
      ch("many senators feared that membership in the League of Nations would commit the United States to future wars and limit Congress's power to declare war, and Wilson refused to accept compromises.", "Opponents objected to the League's collective security obligations."),
      [ch("the treaty required the United States to pay Germany reparations.", "The treaty required Germany to pay reparations."),
       ch("Congress wanted the United States to join the League without conditions.", "Many senators opposed joining."),
       ch("the treaty ended the war with a German victory.", "The treaty followed an Allied victory.")],
      "Fears of League commitments and Wilson's refusal to compromise defeated the treaty.", difficulty="hard")

# ---- The 1920s ----
B.mcq(T_TW, "Henry Ford's assembly line and the Model T",
      ch("lowered the cost of cars so that many middle-class Americans could afford them, transforming daily life and the economy.", "Mass production made automobiles widely available."),
      [ch("made cars a luxury only for the wealthy.", "Ford's methods lowered prices."),
       ch("ended the need for railroads.", "Railroads continued to be important."),
       ch("reduced demand for steel.", "The auto industry increased demand for steel.")],
      "Ford's mass production made cars affordable and reshaped American life.", difficulty="easy")

B.mcq(T_TW, "The Scopes Trial of 1925 is best understood as",
      ch("a highlight of the clash between traditional religious fundamentalism and modern science over the teaching of evolution.", "The trial symbolized cultural conflict over modernism."),
      [ch("a dispute over the regulation of railroads.", "The trial concerned the teaching of evolution."),
       ch("a labor strike in Tennessee.", "The trial was about a teacher."),
       ch("a challenge to Prohibition.", "The trial did not concern Prohibition.")],
      "The Scopes Trial symbolized the conflict between fundamentalism and modern science.", difficulty="medium")

B.mcq(T_TW, src("A poet's essay, 1926", "“We younger artists intend to express our dark-skinned selves without fear or shame. If white people are pleased, we are glad. If they are not, it does not matter. We know we are beautiful.”") + "\n\nThe passage best reflects which of the following?",
      ch("The Harlem Renaissance's assertion of Black cultural pride and artistic independence.", "The author calls for artists to express their own identity without seeking approval."),
      [ch("Support for racial assimilation into white culture.", "The author rejects seeking approval."),
       ch("A call for Black Americans to leave the United States.", "The passage concerns cultural expression."),
       ch("A defense of segregation.", "The author does not defend segregation.")],
      "The passage expresses Harlem Renaissance themes of pride and independence.", difficulty="medium")

B.mcq(T_TW, "The Immigration Act of 1924",
      ch("set national origins quotas that sharply limited immigration from southern and eastern Europe and barred immigration from Asia.", "The law reflected nativism and the desire to restrict newcomers."),
      [ch("removed all limits on immigration.", "The law reduced immigration."),
       ch("favored immigrants from southern and eastern Europe.", "The quotas favored northern and western Europe."),
       ch("ended the Chinese Exclusion Act.", "The act expanded exclusion of Asians.")],
      "The 1924 act restricted immigration through national origins quotas.", difficulty="hard")

B.mcq(T_TW, "Which statement best describes the American economy of the 1920s?",
      ch("Rapid growth and consumer spending, supported by installment buying and advertising, coexisted with weak farm incomes and unequal distribution of wealth.", "Prosperity was real but uneven."),
      [ch("Prosperity was shared equally by all groups.", "Many farmers and workers did not share equally."),
       ch("The economy was in a deep depression throughout the decade.", "The decade saw growth until 1929."),
       ch("Government regulation of business expanded greatly.", "The decade featured limited regulation.")],
      "The 1920s combined growth and consumerism with uneven prosperity.", difficulty="hard")

# ---- The Great Depression and the New Deal ----
B.mcq(T_DN, "Which of the following contributed to the stock market crash of 1929?",
      ch("Widespread speculation with borrowed money, known as buying on margin.", "Investors borrowed to buy stocks, so falling prices triggered panic selling and losses."),
      [ch("A sharp increase in federal spending.", "Federal spending was low."),
       ch("The abolition of the gold standard.", "The gold standard remained in place."),
       ch("A wave of labor strikes.", "The crash was driven by speculation, not strikes.")],
      "Buying on margin contributed to the crash.", difficulty="easy")

B.mcq(T_DN, "President Hoover's response to the early Depression emphasized",
      ch("voluntary cooperation and limited government aid, such as the Reconstruction Finance Corporation, rather than direct relief to individuals.", "Hoover believed in limited federal intervention."),
      [ch("large-scale direct federal relief to the unemployed.", "Hoover resisted direct relief."),
       ch("government ownership of banks.", "Hoover did not support that."),
       ch("a ban on all imports.", "Hoover signed high tariffs, not a ban.")],
      "Hoover favored voluntary measures and limited aid.", difficulty="medium")

B.mcq(T_DN, src("A president's radio address, 1933", "“Our people ask for action, and for action now. The government has a duty to put the unemployed to work and to protect the savings of the people.”") + "\n\nThe passage best reflects which of the following?",
      ch("A new view that the federal government should take an active role in relief and recovery.", "The president promises direct government action."),
      [ch("A defense of laissez-faire government.", "The passage calls for government action."),
       ch("A call to leave relief to private charity.", "The passage assigns the duty to government."),
       ch("Support for isolationist foreign policy.", "The passage concerns domestic relief.")],
      "The passage reflects the New Deal's activist approach to relief.", difficulty="medium")

B.mcq(T_DN, "The Social Security Act of 1935",
      ch("established old-age pensions and unemployment insurance funded by payroll taxes.", "The act created the foundation of the national social insurance system."),
      [ch("abolished all federal taxes.", "The law was funded by taxes."),
       ch("provided free housing for all citizens.", "That was not part of the act."),
       ch("guaranteed jobs for all unemployed workers.", "That describes work relief programs, not Social Security.")],
      "Social Security created pensions and unemployment insurance.", difficulty="medium")

B.mcq(T_DN, "The National Labor Relations Act (Wagner Act) of 1935 helped unions grow by",
      ch("guaranteeing workers the right to organize and bargain collectively and creating the National Labor Relations Board.", "The law protected union organizing and barred certain employer tactics."),
      [ch("banning all strikes.", "The law protected organizing."),
       ch("requiring all workers to join unions.", "The law did not require union membership."),
       ch("ending federal involvement in labor disputes.", "The law created a federal board.")],
      "The Wagner Act protected collective bargaining.", difficulty="hard")

# ---- World War II ----
B.mcq(T_W2, "Japan's attack on Pearl Harbor on December 7, 1941",
      ch("led the United States to declare war on Japan and fully enter World War II.", "The attack ended the debate between isolationists and interventionists."),
      [ch("led the United States to sign a peace treaty with Japan.", "The attack led to war."),
       ch("took place after Germany surrendered.", "Germany surrendered in 1945."),
       ch("occurred in the Philippines.", "Pearl Harbor is in Hawaii.")],
      "Pearl Harbor brought the United States into the war.", difficulty="easy")

B.mcq(T_W2, "The Lend-Lease Act of 1941 allowed the United States to",
      ch("supply weapons and materials to Britain and other Allies without requiring immediate payment, while remaining formally out of the war.", "The act increased American aid to nations fighting the Axis."),
      [ch("send American troops to fight in Europe.", "The act did not send troops."),
       ch("sell weapons only to Germany.", "The act aided the Allies."),
       ch("end American neutrality laws completely.", "The act modified policy but did not declare war.")],
      "Lend-Lease supported the Allies before American entry into the war.", difficulty="medium")

B.mcq(T_W2, src("A West Coast resident's letter, 1942", "“We were told to bring only what we could carry. My father, born in Japan, and I, born here, are both being sent to a camp in the desert. I am a citizen, and I have done nothing wrong.”") + "\n\nThe passage best reflects which of the following?",
      ch("The forced relocation of Japanese Americans based on race and wartime fear, which the Supreme Court upheld in Korematsu v. United States.", "The writer describes internment under Executive Order 9066."),
      [ch("A voluntary move by Japanese Americans to defense jobs.", "The relocation was forced."),
       ch("A policy that also relocated German Americans in large numbers.", "Internment targeted Japanese Americans much more broadly."),
       ch("The protection of Japanese Americans from discrimination.", "The government interned them.")],
      "The passage describes Japanese American internment during the war.", difficulty="medium")

B.mcq(T_W2, "Which statement best describes the effect of World War II on women and African Americans?",
      ch("Wartime labor needs opened new jobs for women and Black workers, and pressure from leaders such as A. Philip Randolph led to a ban on discrimination in defense industries, though discrimination persisted.", "The war expanded opportunities but did not end inequality."),
      [ch("The war ended racial segregation in the armed forces.", "The armed forces were desegregated in 1948."),
       ch("Women were barred from all war production jobs.", "Millions of women worked in war industries."),
       ch("African Americans were drafted but could not work in defense plants.", "They gained access to some defense jobs."),],
      "The war created new opportunities and challenged discrimination without eliminating it.", difficulty="hard")

B.mcq(T_W2, "President Truman and his advisers justified the use of atomic bombs on Hiroshima and Nagasaki in 1945 as a way to",
      ch("bring a quick end to the war with Japan without a costly invasion.", "Truman argued the bombs would save American lives."),
      [ch("start a war with the Soviet Union.", "That was not the stated purpose."),
       ch("end the war in Europe.", "Germany had already surrendered."),
       ch("test the weapon on a neutral nation.", "Japan was an enemy.")],
      "The stated purpose was to end the war quickly and avoid an invasion.", difficulty="hard")

# ---- Short-answer questions ----
saq(B, T_PR,
    "Use the excerpt to answer parts A, B and C.\n\n" + src("A historian, early twenty-first century", "“Progressives believed that the problems of industrial society could be solved by expert regulation and an active government, but their reforms often reached only some Americans.”") + "\n\n**a)** Identify ONE claim made by the historian.\n\n**b)** Explain ONE development in the period 1900 to 1920 that supports the claim that Progressives favored an active government.\n\n**c)** Explain ONE way in which Progressive-era reforms or attitudes excluded or limited the rights of some groups.",
    [(1, "Part A: Identifies a claim, such as that Progressives favored regulation and an active government, or that their reforms did not reach all Americans"),
     (1, "Part B: Explains a development such as the Meat Inspection Act and Pure Food and Drug Act, trust-busting, the Federal Reserve Act, or the Federal Trade Commission"),
     (1, "Part C: Explains a limit such as segregation continuing or expanding under Jim Crow and in the Wilson administration, immigration restriction, or the exclusion of Black women from major suffrage organizations")],
    "a) The historian claims that Progressives wanted an active, expert-led government but that reform benefited only some Americans.\nb) The Meat Inspection Act and the Pure Food and Drug Act of 1906 gave the federal government authority to regulate food and drug safety.\nc) Jim Crow segregation continued in the South and was extended to federal workplaces under the Wilson administration, so many African Americans did not share in Progressive reforms.")

saq(B, T_W1,
    "Use the excerpt to answer parts A, B and C.\n\n" + src("A president's address to Congress, 1917", "“The world must be made safe for democracy. We have no quarrel with the German people, but with a government that has sunk our ships and sought to make allies against us.”") + "\n\n**a)** Identify ONE reason for American entry into World War I expressed or implied in the excerpt.\n\n**b)** Explain ONE way in which the war affected civil liberties in the United States.\n\n**c)** Explain ONE way in which Americans disagreed about the peace settlement after the war.",
    [(1, "Part A: Identifies a reason such as German attacks on American ships, the Zimmermann Telegram or the goal of making the world safe for democracy"),
     (1, "Part B: Explains an effect such as the Espionage and Sedition Acts limiting dissent, the prosecution of critics such as Eugene Debs, or the Schenck decision allowing limits on speech"),
     (1, "Part C: Explains a disagreement such as debates in the Senate over joining the League of Nations and whether it would limit Congress's power to declare war")],
    "a) The speaker says Germany had sunk American ships and sought allies against the United States, which was part of the reason for entering the war.\nb) The Espionage and Sedition Acts limited dissent and led to prosecutions of antiwar critics such as Eugene Debs, and the Supreme Court allowed such limits in Schenck v. United States.\nc) Senators disagreed over the League of Nations, with some fearing it would limit Congress's power to declare war, which led the Senate to reject the Treaty of Versailles.")

saq(B, T_DN,
    "Using your knowledge of United States history, answer parts A, B and C.\n\n**a)** Identify ONE New Deal program or law intended to provide relief or jobs.\n\n**b)** Identify ONE New Deal program or law intended to reform the financial system or regulate the economy.\n\n**c)** Explain ONE criticism of the New Deal made by opponents in the period 1933 to 1940.",
    [(1, "Part A: Identifies a program such as the Civilian Conservation Corps, the Works Progress Administration or the Public Works Administration"),
     (1, "Part B: Identifies a law or agency such as the Federal Deposit Insurance Corporation, the Securities and Exchange Commission or the Glass-Steagall Act"),
     (1, "Part C: Explains a criticism such as conservatives like the American Liberty League arguing that the New Deal expanded government too much, or critics such as Huey Long and Father Coughlin arguing it did not do enough, or Supreme Court rulings that struck down parts of it")],
    "a) The Civilian Conservation Corps gave jobs to young men to work on conservation projects.\nb) The Federal Deposit Insurance Corporation insured bank deposits to restore trust in banks.\nc) Conservative critics such as the American Liberty League argued that the New Deal expanded the power of the federal government too much and threatened individual liberty and free enterprise.")

B.save()
B.brief()
