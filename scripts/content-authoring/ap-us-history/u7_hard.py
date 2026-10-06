from common import *

B = hard(7)
T_IM, T_PR, T_W1, T_TW, T_DN, T_W2 = ("imperialism-and-spanish-american-war", "progressive-era", "world-war-one", "twenties-and-culture", "depression-and-new-deal", "world-war-two")

# ---- Imperialism and the Spanish-American War ----
B.mcq(T_IM, src("A historian, late twentieth century", "“American expansion in the 1890s was driven less by a hunger for territory than by the search for markets, especially in Asia, and by the belief that a modern economy needed them.”") + "\n\nWhich of the following best supports the historian's argument?",
      ch("The Open Door notes asserted equal access to the Chinese market, and the acquisition of the Philippines gave the United States a base in Asia.", "Both developments show commercial goals in Asia shaping American expansion."),
      [ch("The Anti-Imperialist League opposed the annexation of the Philippines.", "That shows opposition to expansion, not its economic motives."),
       ch("The Maine exploded in Havana harbor in 1898.", "That event is linked to the origins of the war with Spain, not to Asian markets."),
       ch("Yellow journalism stirred public anger toward Spain.", "That concerns public opinion and the war with Spain, not markets.")],
      "The Open Door and the Philippines show economic interests in Asia.")

B.mcq(T_IM, "The Platt Amendment of 1901, attached to Cuba's constitution,",
      ch("gave the United States the right to intervene in Cuban affairs and to maintain a naval base at Guantanamo Bay.", "The amendment limited Cuban independence and ensured continued American influence."),
      [ch("granted Cuba complete independence from all outside influence.", "The amendment limited Cuban independence."),
       ch("annexed Cuba as an American territory.", "Cuba was not annexed."),
       ch("barred the United States from keeping troops in Cuba.", "The amendment permitted American intervention.")],
      "The Platt Amendment kept Cuba under American influence.")

B.mcq(T_IM, "The Roosevelt Corollary to the Monroe Doctrine (1904) asserted that",
      ch("the United States could act as an international police power in the Western Hemisphere to prevent instability that might invite European intervention.", "Roosevelt justified American intervention in Latin American affairs."),
      [ch("European nations had the right to collect debts in Latin America by force.", "The corollary aimed to prevent such intervention."),
       ch("the United States would stay out of all affairs in Latin America.", "The corollary expanded American involvement."),
       ch("Latin American nations should join the League of Nations.", "The League did not yet exist in 1904.")],
      "The corollary justified American intervention as a police power.")

# ---- The Progressive Era ----
B.mcq(T_PR, src("A historian, early twenty-first century", "“Progressivism was largely a reform movement for white America. It expanded democracy for white women and workers while ignoring, and sometimes deepening, racial segregation.”") + "\n\nWhich of the following best supports the historian's argument?",
      ch("President Wilson's administration segregated federal workplaces, and Black activists founded the NAACP in 1909 to fight discrimination.", "Both show racial discrimination persisting and Black activists organizing against it during the Progressive Era."),
      [ch("The Seventeenth Amendment provided for the direct election of senators.", "That reform expanded democracy but does not address race."),
       ch("The Meat Inspection Act regulated the meatpacking industry.", "That law concerned food safety."),
       ch("Theodore Roosevelt created national parks.", "Conservation did not address segregation.")],
      "Federal segregation and the founding of the NAACP support the argument.")

B.mcq(T_PR, "The Progressive conservation movement under Theodore Roosevelt led most directly to",
      ch("the creation of national forests, parks and monuments and greater federal management of natural resources.", "Roosevelt greatly expanded protected public lands."),
      [ch("the sale of most public lands to private developers.", "Roosevelt protected land."),
       ch("a ban on all logging and mining in the West.", "Resources were managed, not banned."),
       ch("the elimination of federal land agencies.", "Federal agencies expanded.")],
      "Conservation expanded federal protection and management of public lands.")

B.mcq(T_PR, "Which statement best compares the tactics of the National American Woman Suffrage Association and Alice Paul's National Woman's Party?",
      ch("The NAWSA pursued a state-by-state strategy and lobbying, while the National Woman's Party used pickets and protests to press for a federal amendment.", "The groups shared a goal but differed in methods."),
      [ch("Both groups opposed women's suffrage.", "Both supported suffrage."),
       ch("Only the NAWSA used public demonstrations.", "The Woman's Party was known for pickets."),
       ch("Both groups relied only on court cases to win the vote.", "Neither relied solely on court cases.")],
      "NAWSA used lobbying and state campaigns while the National Woman's Party used protests.")

# ---- World War I ----
B.mcq(T_W1, src("A historian, late twentieth century", "“Wartime fear led the government to treat dissent as disloyalty, and many Americans who criticized the war found themselves silenced or imprisoned.”") + "\n\nWhich of the following best supports the historian's argument?",
      ch("Eugene Debs was sentenced to prison under the Espionage Act for an antiwar speech.", "The prosecution of a prominent critic shows dissent being punished."),
      [ch("Congress established a draft with the Selective Service Act.", "The draft shows mobilization, not suppression of dissent."),
       ch("The Committee on Public Information produced posters supporting the war.", "That shows promotion of the war, not punishment of critics."),
       ch("Women took jobs in war industries.", "That concerns the labor force, not dissent.")],
      "Debs's imprisonment shows the government punishing wartime dissent.")

B.mcq(T_W1, "Which statement best explains the difference between Woodrow Wilson's goals and the Treaty of Versailles?",
      ch("Allied leaders insisted on punishing Germany through reparations and a war guilt clause, which departed from Wilson's hopes for a peace without victory and a fair settlement.", "The treaty was harsher on Germany than Wilson wanted."),
      [ch("The treaty exactly reflected all Fourteen Points.", "Many of Wilson's points were not adopted."),
       ch("Wilson insisted on harsh reparations, which the Allies rejected.", "The Allies wanted harsher terms than Wilson."),
       ch("The treaty gave Germany control of the League of Nations.", "Germany was not included in the League at first.")],
      "The treaty was more punitive than Wilson's vision.")

B.mcq(T_W1, "The Red Scare of 1919 and 1920 was fueled by",
      ch("fear of communism after the Russian Revolution, labor strikes and bombings, leading to the Palmer Raids and deportations of suspected radicals.", "Anxiety about radicalism after the war led to arrests and deportations."),
      [ch("the success of labor unions in winning major reforms.", "The Red Scare weakened radicals."),
       ch("a wave of immigration from northern Europe.", "The scare was about radicalism."),
       ch("the passage of the Nineteenth Amendment.", "The amendment did not cause the scare.")],
      "Fear of communism after the Russian Revolution led to the Palmer Raids.")

# ---- The 1920s ----
B.mcq(T_TW, src("A magazine editorial, 1926", "“The chief business of the American people is business. The government's duty is to keep taxes low and regulation light and to let enterprise do the rest.”") + "\n\nThe passage best reflects which of the following?",
      ch("The Republican policies of the 1920s that favored business and limited regulation.", "The editorial expresses a laissez-faire approach to government and business."),
      [ch("The Progressive trust-busting of Theodore Roosevelt.", "Roosevelt's approach emphasized regulation."),
       ch("The New Deal's expansion of federal regulation.", "The New Deal came in the 1930s."),
       ch("Populist demands for government ownership of railroads.", "The passage calls for light regulation.")],
      "The passage reflects 1920s laissez-faire policy toward business.")

B.mcq(T_TW, "Marcus Garvey's Universal Negro Improvement Association appealed to many African Americans in the early 1920s because it",
      ch("promoted racial pride, economic self-sufficiency and Black nationalism.", "Garvey urged Black Americans to build their own institutions and take pride in their heritage."),
      [ch("called for full assimilation into white culture.", "Garvey promoted racial pride and separatism."),
       ch("was supported by the federal government.", "The government investigated Garvey."),
       ch("focused on persuading Congress to pass a civil rights bill.", "The group focused on self-help and nationalism.")],
      "Garvey's movement promoted racial pride and self-sufficiency.")

# ---- The Great Depression and the New Deal ----
B.mcq(T_DN, "President Franklin Roosevelt's 1937 proposal to add new justices to the Supreme Court",
      ch("aimed to overcome Court rulings against New Deal laws, but it was widely criticized and failed in Congress.", "Critics saw the plan as an attempt to pack the Court."),
      [ch("passed easily and gave Roosevelt control of the Court.", "The plan failed."),
       ch("was supported by nearly all Democrats and Republicans.", "The plan was widely opposed."),
       ch("ended the New Deal.", "The New Deal continued.")],
      "The court-packing plan failed to pass despite Roosevelt's aims.")

B.mcq(T_DN, "Which statement best describes the effect of the New Deal on American politics?",
      ch("It created a coalition of urban workers, unions, African Americans, Southerners and others that supported the Democratic Party for decades, and it expanded federal responsibility for economic security.", "The New Deal reshaped both party politics and the role of government."),
      [ch("It ended the two-party system.", "Both parties continued."),
       ch("It eliminated federal involvement in the economy.", "It expanded federal involvement."),
       ch("It made the Republican Party dominant for decades.", "The Democratic coalition was dominant for decades.")],
      "The New Deal created a lasting Democratic coalition and expanded federal responsibility.")

# ---- World War II ----
B.mcq(T_W2, src("A Supreme Court dissent, 1944", "“The order rests on the assumption that an entire group is disloyal because of its ancestry. Such an assumption is racial discrimination of the worst kind, and the Constitution does not permit it.”") + "\n\nThe author of the passage would most likely have agreed with which of the following?",
      ch("The internment of Japanese Americans was unconstitutional discrimination.", "The author condemns treating a whole group as disloyal because of ancestry."),
      [ch("The internment was a justified wartime security measure.", "The author rejects the order."),
       ch("Japanese Americans should have been drafted into segregated units only.", "The passage concerns internment."),
       ch("The Supreme Court had no authority to review military orders.", "The author is reviewing the order.")],
      "The dissent describes the internment order as unconstitutional racial discrimination.")

B.mcq(T_W2, "The Allied invasion of Normandy in June 1944 was significant because it",
      ch("opened a second front in Western Europe, helping to bring about the defeat of Germany.", "The invasion forced Germany to fight on two fronts."),
      [ch("ended the war in the Pacific.", "The Pacific war ended in August 1945."),
       ch("was a Soviet operation on the Eastern Front.", "It was an Allied operation in France."),
       ch("caused Italy to join the Axis.", "Italy had joined the Axis earlier.")],
      "The invasion opened a second front and helped defeat Germany.")

# ---- Short-answer and long-essay ----
saq(B, T_W2,
    "Use the excerpt to answer parts A, B and C.\n\n" + src("A Black newspaper editorial, 1942", "“We are fighting for victory over fascism abroad and for victory over discrimination at home. A double victory is our aim.”") + "\n\n**a)** Identify ONE argument made in the excerpt.\n\n**b)** Explain ONE way in which World War II contributed to the civil rights movement.\n\n**c)** Explain ONE limit on wartime progress for racial equality in the United States.",
    [(1, "Part A: Identifies the argument that the fight against fascism abroad should be matched by a fight against racial discrimination at home"),
     (1, "Part B: Explains a contribution such as Executive Order 8802 banning discrimination in defense industries, the growth of the NAACP and CORE, or Black migration to industrial cities increasing political influence"),
     (1, "Part C: Explains a limit such as continued segregation in the armed forces, the internment of Japanese Americans, or race riots such as Detroit in 1943")],
    "a) The editorial argues that the war against fascism abroad should also be a war against discrimination at home.\nb) Pressure from A. Philip Randolph led President Roosevelt to issue Executive Order 8802, which banned discrimination in defense industries and opened some jobs to Black workers.\nc) The armed forces remained segregated throughout the war, and racial tensions led to riots such as the one in Detroit in 1943.")

leq(B, T_DN,
    "**Long Essay Question**\n\nEvaluate the extent to which the New Deal changed the relationship between the federal government and the American people in the period 1933 to 1945.",
    "A strong response states a defensible thesis, for example that the New Deal permanently expanded the government's responsibility for economic security and regulation while leaving some inequalities, including racial and gender inequalities, largely in place. It places the topic in the context of the Great Depression and earlier limited government, uses specific evidence (the FDIC and SEC, the Social Security Act, the Wagner Act, the WPA and CCC, the Agricultural Adjustment Act, critics such as Huey Long and the Supreme Court's rulings, and the continuing high unemployment until the war), and uses continuity and change over time to weigh transformation against limits.",
    "Thesis: Presents a defensible thesis that responds to the prompt and evaluates the extent to which the New Deal changed the federal government's relationship with the people",
    "Contextualization: Places the topic in a broader context, such as the Great Depression, Hoover's limited response or earlier Progressive-era reform",
    "Evidence: Provides at least two specific, accurate pieces of evidence relevant to the prompt (1 point for addressing the topic with evidence, 2nd point for using specific evidence to support the argument)",
    "Analysis and reasoning: Uses continuity and change over time to structure the argument (1 point), and demonstrates complex understanding, such as showing that the New Deal expanded government yet excluded some groups or failed to end the Depression before the war (2nd point)")

B.save()
B.brief()
