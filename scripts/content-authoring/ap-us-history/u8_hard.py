from common import *

B = hard(8)
T_PO, T_CF, T_CR, T_GS, T_PR = ("postwar-economy-and-society", "cold-war-foreign-policy", "civil-rights-movement", "great-society-and-liberalism", "protest-and-the-1970s")

# ---- Postwar prosperity and society ----
B.mcq(T_PO, src("A historian, early twenty-first century", "“Postwar suburbanization expanded the middle class, but mostly the white middle class, because federal mortgage programs and private practices steered Black families away from the new neighborhoods.”") + "\n\nWhich of the following best supports the historian's argument?",
      ch("Levittown's original rules barred Black buyers, and federal underwriting practices rated Black neighborhoods as poor risks, a practice known as redlining.", "Both examples show how housing policy and private practice excluded Black families from suburban homeownership."),
      [ch("The GI Bill offered low-interest loans to veterans.", "That describes the benefits available but not the exclusion of Black families."),
       ch("The interstate highway system made commuting easier.", "That shows the growth of suburbs but not racial exclusion."),
       ch("Television became common in American homes.", "That concerns popular culture.")],
      "Levittown's restrictions and redlining support the historian's claim about exclusion.")

B.mcq(T_PO, "Beat writers and early rock and roll music in the 1950s",
      ch("challenged the conformity and materialism of mainstream culture, especially among young people.", "Both expressed discontent with the conformity of the postwar era."),
      [ch("promoted the values of traditional suburban life.", "They challenged those values."),
       ch("were supported by government cultural programs.", "They were often viewed with suspicion."),
       ch("ended racial segregation in music.", "They did not end segregation, though rock and roll mixed musical traditions.")],
      "Beat writers and rock and roll challenged mainstream conformity.")

B.mcq(T_PO, "Which statement best explains the slower growth of unions in the South and West after 1947?",
      ch("The Taft-Hartley Act allowed states to adopt right-to-work laws, which many Southern and Western states passed.", "Right-to-work laws weakened union organizing in those regions."),
      [ch("The Wagner Act banned unions in those regions.", "The Wagner Act protected organizing."),
       ch("The AFL-CIO decided not to organize outside the Northeast.", "The AFL-CIO did organize elsewhere."),
       ch("A large majority of workers in the South and West were employed as farm laborers.", "The change reflects state law, not a farm-labor majority.")],
      "Right-to-work laws made union growth harder in many Southern and Western states.")

# ---- Cold War foreign policy ----
B.mcq(T_CF, src("A diplomat's telegram, 1946", "“The Soviet government is committed to expansion and sees no permanent peace with the capitalist world. It is sensitive to force but not to reason. A policy of firm and patient resistance wherever it shows signs of pushing outward is required.”") + "\n\nThe policy recommendation in the passage most directly led to which of the following?",
      ch("The adoption of containment, as expressed in the Truman Doctrine and the Marshall Plan.", "The author's advice of firm resistance to Soviet expansion shaped early Cold War policy."),
      [ch("A policy of isolationism from European affairs.", "The author calls for resistance, not withdrawal."),
       ch("A military alliance with the Soviet Union.", "The author warns against Soviet expansion."),
       ch("The immediate use of nuclear weapons against the Soviet Union.", "The author recommends firm and patient resistance, not immediate war.")],
      "The telegram's advice became the basis of containment.")

B.mcq(T_CF, "The Korean War ended in 1953 with",
      ch("an armistice that left Korea divided near the 38th parallel, reinforcing containment rather than the rollback of communism.", "The war ended in a stalemate and a divided peninsula."),
      [ch("a complete victory for the United States and unification of Korea.", "Korea remained divided."),
       ch("the withdrawal of the United States from East Asia.", "American forces remained in South Korea."),
       ch("a communist victory across the whole peninsula.", "South Korea remained independent.")],
      "The war ended in stalemate and division.")

B.mcq(T_CF, "The release of the Pentagon Papers in 1971 contributed most directly to",
      ch("public distrust of the government's honesty about Vietnam, often called the credibility gap.", "The documents showed that officials had misled the public about the war."),
      [ch("a surge in public support for the war.", "The release increased distrust."),
       ch("the immediate end of the draft.", "The draft ended later, in 1973."),
       ch("a formal declaration of war on North Vietnam.", "Congress did not declare war.")],
      "The Pentagon Papers deepened distrust of the government over Vietnam.")

# ---- The civil rights movement ----
B.mcq(T_CR, src("A historian, late twentieth century", "“The civil rights movement succeeded when local protest forced the federal government to act against the resistance of southern states.”") + "\n\nWhich of the following best supports the historian's argument?",
      ch("President Eisenhower sent federal troops to Little Rock in 1957 to enforce school desegregation, and President Johnson pressed for the Voting Rights Act after the Selma marches.", "Federal action followed local resistance and protest."),
      [ch("The Supreme Court decided Plessy v. Ferguson in 1896.", "That decision upheld segregation."),
       ch("The Taft-Hartley Act restricted union power.", "That law concerned labor."),
       ch("The Marshall Plan rebuilt Europe.", "That concerned foreign policy.")],
      "Federal intervention in Little Rock and after Selma supports the claim.")

B.mcq(T_CR, "The challenge by the Mississippi Freedom Democratic Party at the 1964 Democratic National Convention",
      ch("highlighted the exclusion of Black Mississippians from the political process, although the party rejected the limited compromise it was offered.", "The challenge drew national attention to the denial of voting rights."),
      [ch("won full recognition of the party's delegates.", "The party was offered only a limited compromise."),
       ch("ended the Democratic Party's support for civil rights.", "The challenge did not end that support."),
       ch("was organized by Southern segregationists.", "It was organized by civil rights activists.")],
      "The challenge exposed political exclusion in Mississippi.")

B.mcq(T_CR, "Cesar Chavez and the United Farm Workers used which tactics in the 1960s?",
      ch("Strikes, boycotts and marches to win better conditions for farmworkers, drawing on the nonviolent methods of the civil rights movement.", "The union used nonviolent pressure and public support."),
      [ch("Armed uprisings against growers.", "The union relied on nonviolent methods."),
       ch("A ban on all farm production.", "The union used boycotts and strikes, not a ban."),
       ch("Court-ordered integration of farm labor camps.", "The union relied on strikes, boycotts and marches rather than court-ordered integration.")],
      "The UFW used nonviolent strikes and boycotts.")

# ---- The Great Society and liberalism ----
B.mcq(T_GS, src("A historian, early twenty-first century", "“The Great Society did not end poverty, but it sharply reduced poverty among the elderly and expanded access to health care and education.”") + "\n\nWhich of the following best supports the historian's argument?",
      ch("Medicare and increases in Social Security benefits improved the incomes and health coverage of older Americans.", "These programs targeted the elderly and reduced their poverty."),
      [ch("The Taft-Hartley Act limited union power.", "That law concerned labor and not poverty among the elderly."),
       ch("The Gulf of Tonkin Resolution authorized force in Vietnam.", "That concerns foreign policy."),
       ch("The Marshall Plan rebuilt European economies.", "That concerns European recovery.")],
      "Medicare and Social Security improvements reduced poverty among the elderly.")

B.mcq(T_GS, "Richard Nixon's appeals to the silent majority in 1968 and 1972 were aimed at",
      ch("voters, many of them white working-class and Southern, who reacted against antiwar protest, urban unrest and liberal social policies.", "Nixon built a coalition from voters who felt alienated by the changes of the 1960s."),
      [ch("antiwar student activists.", "They were not his target audience."),
       ch("civil rights leaders and Black Power organizers.", "Those groups were not his main audience."),
       ch("members of the Democratic leadership.", "He appealed to voters, not party leaders.")],
      "The silent majority appeal targeted voters upset by protest and social change.")

B.mcq(T_GS, "The Supreme Court's decision in Engel v. Vitale (1962)",
      ch("ruled that organized prayer in public schools violated the First Amendment's establishment clause, angering some religious conservatives.", "The decision limited state-sponsored prayer in schools."),
      [ch("required daily prayer in public schools.", "The Court ruled against it."),
       ch("upheld segregation in public schools.", "The case concerned prayer."),
       ch("banned religious groups from meeting at all.", "The decision concerned school-sponsored prayer.")],
      "Engel v. Vitale ended organized school prayer and fueled conservative reaction.")

# ---- Protest movements and the 1970s ----
B.mcq(T_PR, src("A student group's manifesto, 1962", "“We are people of this generation, raised in at least modest comfort, housed now in universities, looking uncomfortably at the world we inherit. We seek a democracy of individual participation, in which people share in the decisions that affect their lives.”") + "\n\nThe passage best reflects which of the following?",
      ch("The New Left's emphasis on participatory democracy and its criticism of mainstream society.", "The authors call for greater direct participation and question the world they inherit."),
      [ch("Support for the policy of containment.", "The passage criticizes society."),
       ch("A defense of the status quo.", "The authors question it."),
       ch("A call for a return to traditional values.", "The authors call for change.")],
      "The passage expresses the New Left's call for participatory democracy.")

B.mcq(T_PR, "The Stonewall uprising of 1969 in New York City",
      ch("became a catalyst for the modern gay rights movement.", "The resistance to a police raid inspired activists to organize."),
      [ch("led to the passage of the Equal Rights Amendment.", "The ERA was not ratified."),
       ch("ended the Vietnam War.", "It was not related to the war's end."),
       ch("was a protest against the draft.", "It concerned police raids on a bar.")],
      "Stonewall inspired the growth of the gay rights movement.")

B.mcq(T_PR, "Which statement best explains the economic changes of the 1970s?",
      ch("Foreign competition and the energy crisis weakened heavy industry in the Northeast and Midwest, while population and investment shifted toward the South and West, called the Sun Belt.", "Deindustrialization and migration reshaped regional economies."),
      [ch("American manufacturing expanded rapidly in the Northeast.", "Manufacturing declined there."),
       ch("The South and West lost population to the Midwest.", "The Sun Belt gained population."),
       ch("Energy prices fell, supporting industry.", "Energy prices rose in the 1970s.")],
      "Deindustrialization and the rise of the Sun Belt changed the economy.")

# ---- Short-answer and long-essay ----
saq(B, T_CF,
    "Use the excerpt to answer parts A, B and C.\n\n" + src("A retiring president's farewell address, 1961", "“We have been compelled to create a permanent armaments industry of vast proportions. We must guard against the unwarranted influence of the military-industrial complex, whether sought or unsought.”") + "\n\n**a)** Identify ONE concern expressed in the excerpt.\n\n**b)** Explain ONE development in the 1950s that contributed to the growth of the military establishment described in the excerpt.\n\n**c)** Explain ONE way in which the Cold War shaped American society in the 1950s.",
    [(1, "Part A: Identifies the concern that a permanent, large armaments industry and its influence on government could threaten democratic government"),
     (1, "Part B: Explains a development such as the Korean War and NSC-68 leading to higher defense spending, the nuclear arms race, or competition with the Soviet Union after Sputnik"),
     (1, "Part C: Explains an effect such as the Red Scare and McCarthyism, civil defense drills, the National Defense Education Act, or the interstate highway system's defense rationale")],
    "a) The president worries that a permanent armaments industry and military establishment could gain too much influence over government.\nb) The Korean War and the policy outlined in NSC-68 led to large increases in defense spending, and the nuclear arms race with the Soviet Union created a permanent military industry.\nc) The Cold War produced a Red Scare in which people were investigated for supposed communist ties, and schools held civil defense drills to prepare for nuclear attack.")

leq(B, T_CR,
    "**Long Essay Question**\n\nEvaluate the extent to which the strategies of the civil rights movement changed over time in the period 1945 to 1980.",
    "A strong response states a defensible thesis, for example that the movement moved from legal and nonviolent direct action strategies in the 1950s and early 1960s toward political mobilization and, later, Black Power and broader coalitions, while retaining a commitment to protest and legal challenge throughout. It places the topic in the context of the postwar era and the Cold War, uses specific evidence (the NAACP's legal strategy and Brown v. Board, the Montgomery Bus Boycott, sit-ins and Freedom Rides, the March on Washington, Selma and the Voting Rights Act, Black Power, urban unrest, the Chicano movement and the American Indian Movement), and uses continuity and change over time to analyze the shifts.",
    "Thesis: Presents a defensible thesis that responds to the prompt and evaluates the extent to which the movement's strategies changed",
    "Contextualization: Places the topic in a broader context, such as the Cold War, the Great Migration or the legacy of Jim Crow",
    "Evidence: Provides at least two specific, accurate pieces of evidence relevant to the prompt (1 point for addressing the topic with evidence, 2nd point for using specific evidence to support the argument)",
    "Analysis and reasoning: Uses continuity and change over time to structure the argument (1 point), and demonstrates complex understanding, such as showing that different strategies coexisted or that strategies responded to changing political conditions (2nd point)")

B.save()
B.brief()
