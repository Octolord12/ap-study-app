from common import *

B = bank(7, "unit-7-global-conflict")
T_C1, T_W1, T_IW, T_C2, T_W2 = ("causes-of-world-war-one", "world-war-one-and-russian-revolution", "interwar-period", "causes-of-world-war-two", "world-war-two-and-mass-atrocities")

B.mcq(T_C1, "Which statement best describes the role of the European alliance system in the outbreak of World War I?",
      ch("Rival alliances committed the major powers to support their partners, so a regional crisis after the assassination in Sarajevo expanded into a general war.", "Austria-Hungary's conflict with Serbia drew in Russia, Germany, France and Britain through alliance obligations and mobilization plans."),
      [ch("The alliances prevented conflict by making every state friendly with every other.", "The system divided Europe into opposing blocs and increased the chance that a local crisis would spread."),
       ch("The alliances were created by the League of Nations to keep peace.", "The League of Nations was created after the war."),
       ch("Germany and France were allies against Russia from the beginning.", "Germany and France were on opposite sides.")],
      "Rival alliances turned a regional conflict into a world war.")

B.mcq(T_W1, src("A soldier's letter from the Western Front, 1916", "“We have been under shell fire for six days. The dead lie in the wire between the lines, and after all the attacks the front has moved only a few hundred yards. They tell us the next push will break through.”") + "\n\nWhich statement best explains the situation described in the passage?",
      ch("Machine guns, barbed wire and artillery gave defenders a major advantage, so frontal assaults were extremely costly and produced trench warfare.", "New weapons favored defense, and neither side could achieve a breakthrough without heavy casualties."),
      [ch("Cavalry charges had proven to be the decisive weapon for attackers.", "Cavalry was largely ineffective against machine guns and artillery."),
       ch("Neither army had artillery, so both relied on rifles alone.", "Artillery was extensively used on the Western Front."),
       ch("The war was ended by an armistice that was in effect in 1916.", "The armistice came in November 1918.")],
      "Defensive technology produced a deadlock and heavy casualties.")

B.mcq(T_W1, src("A slogan used by the Bolsheviks in Russia, 1917", "“Peace, land and bread.”") + "\n\nWhich factor best explains the appeal of the slogan to many Russians in 1917?",
      ch("Widespread discontent with Russia's costly war, shortages of food, and peasants' hunger for land under the Provisional Government.", "The slogan addressed the main grievances of soldiers, workers and peasants."),
      [ch("Support for the restoration of the tsar.", "The slogan promised change after the tsar's fall."),
       ch("A desire to continue the war with greater effort.", "The slogan called for peace."),
       ch("Gratitude for German help with the harvest.", "Germany was an enemy and had not helped the harvest.")],
      "The slogan responded to war weariness, hunger and land hunger.")

B.mcq(T_W1, "Which statement best describes the effect of World War I on the home fronts of the combatant nations?",
      ch("Governments mobilized economies and populations by rationing, controlling industry and using propaganda, and women took jobs in factories and other work.", "Total war involved the whole society and increased the power of the state."),
      [ch("Civilians were separated from the war and their lives were unchanged.", "Civilians were deeply affected by shortages, labor demands and sometimes direct attack."),
       ch("Governments reduced their control over the economy in order to promote free enterprise.", "Governments expanded control during the war."),
       ch("Industries shut down because they were not needed for the war.", "Industries expanded to produce war materials.")],
      "Total war increased state control and changed work for women.")

B.mcq(T_W1, src("A summary of a clause of the Treaty of Versailles, 1919", "“The Allied governments affirm, and Germany accepts, that Germany and her allies are responsible for causing all the loss and damage suffered by the Allied governments and their peoples as a result of the war imposed upon them.”") + "\n\nWhich development was most directly connected to the clause described?",
      ch("Widespread German resentment over blame and reparations, which later nationalist and Nazi propaganda exploited.", "Many Germans considered the treaty humiliating, and extremist movements used that resentment."),
      [ch("German gratitude toward the Allies for the generous terms.", "Many Germans felt the terms were harsh and unfair."),
       ch("The immediate entry of the United States into the League of Nations.", "The United States Senate refused to ratify the treaty and did not join the League."),
       ch("The restoration of the German monarchy.", "The German monarchy had fallen at the end of the war.")],
      "The war guilt clause and reparations fueled German resentment.")

B.mcq(T_IW, "Which factor best explains why the Great Depression that began in 1929 spread around the world?",
      ch("Interconnected economies, including international trade, loans and investment, meant that the collapse of the American economy and credit spread to other countries.", "The financial and trade links among industrial economies carried the crisis across borders."),
      [ch("Only the United States was affected, because other economies were isolated.", "Many countries suffered high unemployment and falling trade."),
       ch("A sudden discovery of new gold supplies raised prices everywhere.", "The Depression was marked by falling prices and production."),
       ch("The collapse of the Soviet Union in 1929.", "The Soviet Union existed until 1991.")],
      "Links among national economies carried the crisis worldwide.")

B.mcq(T_IW, "Which statement best explains the appeal of fascist movements in Italy and Germany in the 1920s and 1930s?",
      ch("They promised national revival, order and economic recovery in societies shaken by wartime defeat or disappointment, depression and fear of communism, and they used propaganda and violence.", "Fascists appealed to nationalism and to people seeking strong leadership in a period of crisis."),
      [ch("They offered a democratic socialist program based on international cooperation.", "Fascists rejected democracy and internationalism."),
       ch("They opposed all forms of nationalism.", "Nationalism was central to fascism."),
       ch("They advocated that the League of Nations should govern the world.", "Fascist regimes opposed and ignored the League.")],
      "Fascism combined extreme nationalism, authoritarian leadership and promises of recovery.")

B.mcq(T_IW, "Stalin's policies of collectivization and the Five-Year Plans in the Soviet Union aimed primarily to",
      ch("rapidly industrialize the country and put agriculture under state control, at enormous human cost.", "The policies sought to build heavy industry and control food production, and they caused famine and repression."),
      [ch("restore private farms and a market economy.", "The policies abolished private farms and market incentives."),
       ch("reduce state control and encourage small business.", "State control increased."),
       ch("focus the economy on consumer goods rather than heavy industry.", "The Five-Year Plans emphasized heavy industry and military goods.")],
      "Stalin's plans were meant to industrialize rapidly under state control.")

B.mcq(T_IW, src("Statement by an Indian nationalist leader announcing a protest, 1930", "“We shall march to the sea and take salt from its shores in defiance of the law that forbids it. We shall use no violence, but we shall refuse to obey a law that is unjust.”") + "\n\nWhich statement best describes the strategy of the movement described in the passage?",
      ch("It used nonviolent civil disobedience to challenge British authority and win popular support.", "Gandhi's Salt March was a nonviolent act of civil disobedience that mobilized Indians across social groups."),
      [ch("It was an armed insurrection against the British army.", "The passage rejects violence."),
       ch("It was an alliance with Japan against the British.", "The passage does not mention any alliance."),
       ch("It was a campaign to encourage emigration from India.", "The passage concerns protest within India.")],
      "The passage describes nonviolent civil disobedience.")

B.mcq(T_C2, "Which statement best describes the policy of appeasement toward Nazi Germany in the 1930s?",
      ch("Britain and France made concessions to Hitler, such as accepting the German takeover of the Sudetenland at Munich in 1938, in the hope of avoiding war.", "Appeasement was an attempt to satisfy Hitler's demands to preserve peace, and it was not successful."),
      [ch("Britain and France formed a military alliance to invade Germany immediately.", "They avoided military confrontation until Germany invaded Poland in 1939."),
       ch("Britain and France enforced strict military sanctions through the League of Nations.", "The League's sanctions were weak and appeasement involved concessions."),
       ch("Britain and France supported Germany's war against Poland.", "Britain and France declared war on Germany after the invasion of Poland.")],
      "Appeasement meant making concessions to avoid war.")

B.mcq(T_C2, "Which statement best explains Japan's expansion in East Asia in the 1930s?",
      ch("Japanese leaders, increasingly influenced by the military, sought raw materials, markets and regional dominance, and invaded Manchuria in 1931 and China in 1937.", "Japan's expansion was driven by resource needs, nationalism and militarist influence."),
      [ch("Japan was fulfilling an obligation to the League of Nations to protect China.", "The League criticized Japan's actions in Manchuria, and Japan left the League."),
       ch("Japan was the colony of a European power seeking independence.", "Japan was an independent imperial power."),
       ch("Japan was a member of the Allies and was defending against Germany.", "Japan joined the Axis powers.")],
      "Japan's expansion was motivated by resources, nationalism and militarism.")

B.mcq(T_W2, "Which statement best describes how the Holocaust differed from earlier episodes of religious or ethnic persecution?",
      ch("It used the state's bureaucracy, modern technology and a racial ideology to carry out systematic mass murder.", "The Nazi regime organized the identification, transport and killing of about six million Jews, along with millions of other victims, through state institutions."),
      [ch("It was a spontaneous series of riots without government involvement.", "The persecution was planned and carried out by the state."),
       ch("It was directed only against soldiers in wartime.", "The victims were mostly civilians."),
       ch("It was carried out by the Soviet Union against its own population.", "The Holocaust was carried out by Nazi Germany and its collaborators.")],
      "The Holocaust was an organized, state-run genocide using modern bureaucracy and technology.")

B.mcq(T_W2, "The use of atomic bombs on Hiroshima and Nagasaki in August 1945 most directly contributed to which of the following?",
      ch("Japan's surrender, which ended World War II, and the beginning of the nuclear age and the arms race.", "The bombings were followed by Japan's surrender and shaped later rivalry between the superpowers."),
      [ch("The end of the war in Europe.", "The war in Europe had ended in May 1945."),
       ch("The beginning of World War II.", "The war began in 1939."),
       ch("The immediate surrender of the Soviet Union.", "The Soviet Union was an Allied power.")],
      "The bombs were followed by Japan's surrender and ushered in the nuclear age.")

B.mcq(T_W2, "The Armenian Genocide of 1915 is best understood as which of the following?",
      ch("The deportation and mass killing of Armenians by the Ottoman government during World War I, an example of mass violence linked to nationalism and wartime fears.", "Ottoman authorities deported and killed large numbers of Armenians in 1915 and afterwards."),
      [ch("A battle between the Ottoman and Russian armies.", "The genocide targeted a civilian population."),
       ch("A peaceful population exchange agreed by the Ottoman and Armenian leaders.", "It was a campaign of forced deportation and killing."),
       ch("A Russian campaign against the Ottoman people.", "It was carried out by the Ottoman government against Armenians.")],
      "The Armenian Genocide was a government-led campaign of deportation and killing during World War I.")

B.mcq(T_IW, "The mandate system created after World War I is best described as",
      ch("the League of Nations' assignment of former Ottoman and German territories to Britain and France and other powers, which governed them as mandates while local nationalists sought independence.", "The mandates were a new form of imperial control, justified as preparation for self-government."),
      [ch("an immediate grant of independence to all former colonies of the defeated powers.", "Most mandated territories were not independent, and nationalists continued their struggle."),
       ch("a system in which the United States governed the former German colonies in Africa.", "The mandatory powers were mainly Britain, France and Japan."),
       ch("a plan for the former colonies to rejoin the German Empire.", "Germany lost its colonies in the peace settlement.")],
      "Mandates transferred defeated powers' territories to the victors under League authority.")

saq(B, T_W1,
    "Use the passage to answer parts A, B and C.\n\n" + src("A summary of a clause of the Treaty of Versailles, 1919", "“The Allied governments affirm, and Germany accepts, that Germany and her allies are responsible for causing all the loss and damage suffered by the Allied governments and their peoples as a result of the war imposed upon them.”") + "\n\n**a)** Identify ONE obligation or burden the treaty placed on Germany, based on the passage or your knowledge of the treaty.\n\n**b)** Explain ONE way in which the treaty contributed to political instability in Germany in the 1920s and 1930s.\n\n**c)** Explain ONE way in which the postwar settlement affected the Middle East or Africa.",
    [(1, "Part A: Identifies an obligation such as accepting responsibility for the war, paying reparations, losing territory and colonies, or limits on the German military"),
     (1, "Part B: Explains that resentment of the treaty, economic hardship from reparations, or the perceived humiliation helped weaken the Weimar Republic and strengthened extremist movements such as the Nazis"),
     (1, "Part C: Explains an effect such as the mandate system placing former Ottoman and German territories under British and French control, or the redrawing of borders without regard to local wishes, which fueled nationalism and later conflicts")],
    "a) The passage says Germany had to accept responsibility for all of the loss and damage caused by the war (the war guilt clause), and the treaty also required reparations and limited the German army.\nb) Many Germans resented the treaty as a humiliating dictated peace, and the burden of reparations contributed to economic hardship. This weakened support for the Weimar Republic and helped extremist parties such as the Nazis win followers.\nc) The mandate system placed former Ottoman territories such as Syria, Lebanon, Iraq and Palestine under French or British control. Borders were drawn without regard to local wishes, which strengthened nationalist movements.")

leq(B, T_W2,
    "**Long Essay Question**\n\nEvaluate the extent to which the experience of total war in the first half of the twentieth century changed the role of governments in society.",
    "A strong response takes a position (for example that total war significantly expanded state power over economies and societies, though some governments rolled back controls after the wars). It places the topic in context (industrial warfare and mass armies) and uses specific evidence such as rationing, propaganda, conscription, the mobilization of women's labor, state-run economies in the Soviet Union, the Nazi state's control of society and the economy, and wartime mobilization in Britain or the United States. It analyzes continuity and change and may consider differences between democratic and authoritarian states.",
    "Thesis: Presents a defensible thesis that responds to the prompt and evaluates the extent to which total war changed the role of governments",
    "Contextualization: Describes broader context, such as industrial warfare, mass armies or the effects of the Great Depression",
    "Evidence: Provides at least two specific, accurate examples (such as rationing, conscription, propaganda, controlled economies, mobilization of women) and uses them to support the argument",
    "Analysis and reasoning: Uses continuity and change over time to structure the argument (1 point), and shows complexity by comparing democratic and authoritarian states or by noting what changed after the wars (2nd point)")

B.save()
B.brief()
