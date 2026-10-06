from common import *

B = base(8)
T_PO, T_CF, T_CR, T_GS, T_PR = ("postwar-economy-and-society", "cold-war-foreign-policy", "civil-rights-movement", "great-society-and-liberalism", "protest-and-the-1970s")

# ---- Postwar prosperity and society ----
B.mcq(T_PO, "The GI Bill of 1944 helped expand the American middle class by",
      ch("providing veterans with education benefits, low-interest home loans and other aid.", "Many veterans attended college and bought homes with federal help."),
      [ch("banning all unions in defense industries.", "The GI Bill did not restrict unions."),
       ch("giving every citizen a guaranteed annual income.", "The benefits were targeted at veterans."),
       ch("ending all taxes on corporations.", "The GI Bill did not address corporate taxes.")],
      "The GI Bill provided education and housing benefits to veterans.", difficulty="easy")

B.mcq(T_PO, "Which factors most encouraged the rapid growth of suburbs after World War II?",
      ch("Federally backed mortgages, mass-produced housing such as Levittown, and the automobile and highway construction.", "Government programs, building methods and cars made suburban homes widely available."),
      [ch("Strict laws that forced families to leave cities.", "Suburban growth was largely voluntary."),
       ch("A decline in the birth rate.", "The postwar years saw a baby boom."),
       ch("The elimination of the automobile industry.", "Automobiles were central to suburban growth.")],
      "Mortgages, mass-produced housing and highways drove suburban growth.", difficulty="medium")

B.mcq(T_PO, src("A housewife's letter to a magazine, 1960", "“I have a lovely house, a kind husband and three healthy children. Yet there are days I feel as if something is missing, as if my education and my talents are going to waste.”") + "\n\nThe passage best reflects which of the following?",
      ch("Growing dissatisfaction among some middle-class women with the ideal of domesticity, which helped inspire a new feminist movement.", "The writer describes an unease that works such as The Feminine Mystique helped to name."),
      [ch("Satisfaction with the traditional roles of women in the 1950s.", "The writer expresses dissatisfaction."),
       ch("A demand for women to be drafted into military service.", "The passage does not discuss the draft."),
       ch("Support for the Equal Rights Amendment in 1920.", "The passage is from 1960 and expresses personal unease.")],
      "The passage reflects the discontent that fueled second-wave feminism.", difficulty="medium")

B.mcq(T_PO, "The Taft-Hartley Act of 1947",
      ch("restricted union practices such as the closed shop and allowed states to pass right-to-work laws.", "The law limited union power."),
      [ch("guaranteed workers the right to a closed shop in every industry.", "The act restricted the closed shop."),
       ch("banned all strikes permanently.", "The act did not ban all strikes."),
       ch("created the Social Security system.", "That was done in 1935.")],
      "Taft-Hartley limited the power of unions.", difficulty="medium")

B.mcq(T_PO, "Which statement best describes how postwar prosperity affected African Americans and the poor?",
      ch("Many were excluded from suburban housing through redlining and discrimination and remained concentrated in declining cities or rural poverty.", "Prosperity was not shared equally."),
      [ch("All groups benefited equally from federal housing programs.", "Many programs excluded minorities."),
       ch("Poverty was eliminated by the 1950s.", "Poverty remained."),
       ch("African Americans moved to the suburbs in large numbers.", "Discrimination limited their access to suburbs.")],
      "Discrimination limited access to prosperity.", difficulty="hard")

B.mcq(T_PO, "The Federal-Aid Highway Act of 1956",
      ch("funded the interstate highway system, justified partly by defense needs, and encouraged suburban growth and automobile dependence.", "The law transformed American transportation and settlement."),
      [ch("ended federal spending on roads.", "The act greatly increased spending."),
       ch("created a national railroad system.", "It created highways."),
       ch("banned automobile travel across state lines.", "It promoted travel.")],
      "The highway act created the interstate system and encouraged suburbs.", difficulty="hard")

# ---- Cold War foreign policy ----
B.mcq(T_CF, "The policy of containment aimed to",
      ch("stop the spread of communism rather than roll it back where it already existed.", "Containment was the central strategy of early Cold War policy."),
      [ch("invade the Soviet Union.", "Containment did not seek direct invasion."),
       ch("withdraw American troops from Europe.", "The policy led to a stronger presence."),
       ch("encourage communist revolutions abroad.", "Containment opposed communism's spread.")],
      "Containment sought to limit communism's spread.", difficulty="easy")

B.mcq(T_CF, "The Marshall Plan of 1948 sought to",
      ch("rebuild Western European economies with American aid, promoting stability and limiting communist influence.", "American aid helped European recovery."),
      [ch("send American troops to occupy Western Europe.", "The plan provided economic aid."),
       ch("provide military aid only to Asia.", "The plan was for Europe."),
       ch("punish Germany with harsh reparations.", "The plan aided recovery, including in West Germany.")],
      "The Marshall Plan aided European recovery to counter communism.", difficulty="medium")

B.mcq(T_CF, src("An administration spokesman, 1954", "“If one nation in Southeast Asia falls to communism, its neighbors will fall one after another, like a row of dominoes.”") + "\n\nThe idea expressed in the passage was most often used to justify which of the following?",
      ch("American involvement in Vietnam.", "The domino theory supported intervention to stop communism's spread in Asia."),
      [ch("American isolationism.", "The theory justified involvement, not isolation."),
       ch("The Marshall Plan in Europe.", "The Marshall Plan was in 1948 and aimed at Europe."),
       ch("The creation of the League of Nations.", "The League was created after World War I.")],
      "The domino theory justified American involvement in Vietnam.", difficulty="medium")

B.mcq(T_CF, "The Cuban Missile Crisis of 1962 was resolved when",
      ch("the Soviet Union agreed to remove its missiles from Cuba in exchange for an American pledge not to invade Cuba and a secret agreement to remove American missiles from Turkey.", "Both sides made concessions to avoid war."),
      [ch("the United States invaded Cuba.", "The United States did not invade."),
       ch("the Soviet Union launched missiles at the United States.", "No missiles were launched."),
       ch("Cuba withdrew from the Western Hemisphere.", "That is not what occurred.")],
      "A negotiated settlement ended the crisis.", difficulty="medium")

B.mcq(T_CF, "The Gulf of Tonkin Resolution of 1964",
      ch("gave President Johnson broad authority to use military force in Vietnam without a formal declaration of war.", "The resolution became the basis for escalation."),
      [ch("declared war on North Vietnam.", "Congress did not declare war."),
       ch("ended American involvement in Vietnam.", "The resolution allowed escalation."),
       ch("required Johnson to seek approval for each military action.", "It gave him broad authority.")],
      "The resolution authorized broad presidential action in Vietnam.", difficulty="hard")

B.mcq(T_CF, "President Nixon's policy of détente included",
      ch("arms control agreements with the Soviet Union, such as SALT I, and the opening of relations with China.", "Nixon eased tensions with both communist powers."),
      [ch("an immediate military attack on China.", "Nixon opened relations with China."),
       ch("the withdrawal of the United States from NATO.", "The United States stayed in NATO."),
       ch("a ban on all trade with communist countries.", "Détente increased contact and trade.")],
      "Détente involved arms control and the opening to China.", difficulty="hard")

# ---- The civil rights movement ----
B.mcq(T_CR, "In Brown v. Board of Education (1954), the Supreme Court ruled that",
      ch("racial segregation in public schools was unconstitutional.", "The Court overturned the separate but equal doctrine in education."),
      [ch("segregation in public schools was permitted if facilities were equal.", "That was the rule of Plessy that Brown rejected."),
       ch("states could ban integration.", "The Court ruled against segregation."),
       ch("Congress could not pass civil rights laws.", "The case concerned segregated schools.")],
      "Brown held that segregated public schools were unconstitutional.", difficulty="easy")

B.mcq(T_CR, "The Montgomery Bus Boycott of 1955 and 1956",
      ch("was sparked by Rosa Parks's arrest, led by local activists including Martin Luther King Jr., and ended with a Supreme Court ruling against bus segregation.", "The boycott showed the power of sustained nonviolent protest."),
      [ch("was a boycott of stores by white Southerners.", "The boycott was led by African Americans."),
       ch("ended without any change to segregation.", "Bus segregation was ruled unconstitutional."),
       ch("began after the Civil Rights Act of 1964.", "It occurred nearly a decade earlier.")],
      "The boycott led to the end of segregated buses in Montgomery.", difficulty="medium")

B.mcq(T_CR, src("A minister's letter from jail, 1963", "“We have waited for more than three hundred years for our God-given rights. Injustice anywhere is a threat to justice everywhere. Those who break an unjust law openly, and accept the penalty, show the highest respect for law.”") + "\n\nThe passage best reflects which of the following?",
      ch("The strategy of nonviolent civil disobedience.", "The writer justifies breaking unjust laws openly while accepting punishment."),
      [ch("A call for violent revolution.", "The writer describes accepting the penalty."),
       ch("Support for gradual change over many generations.", "The writer criticizes waiting."),
       ch("Opposition to protest.", "The writer defends protest.")],
      "The passage expresses nonviolent civil disobedience.", difficulty="medium")

B.mcq(T_CR, "The Civil Rights Act of 1964",
      ch("banned discrimination in public accommodations and employment based on race, color, religion, sex or national origin.", "The law was a major federal civil rights measure."),
      [ch("ended literacy tests for voting.", "That was the Voting Rights Act of 1965."),
       ch("outlawed segregation in the military.", "Military desegregation came in 1948."),
       ch("created the Peace Corps.", "That was established in 1961.")],
      "The Civil Rights Act banned discrimination in public places and employment.", difficulty="medium")

B.mcq(T_CR, "The Voting Rights Act of 1965",
      ch("outlawed literacy tests and authorized federal oversight of voter registration in areas with a history of discrimination, leading to a sharp rise in Black voter registration.", "The law enforced the Fifteenth Amendment."),
      [ch("gave women the right to vote.", "That was the Nineteenth Amendment."),
       ch("lowered the voting age to eighteen.", "That was the Twenty-sixth Amendment in 1971."),
       ch("ended poll taxes in federal elections only and left other tests in place.", "The act addressed literacy tests and registration.")],
      "The Voting Rights Act removed barriers to Black voting.", difficulty="hard")

B.mcq(T_CR, "Black Power advocates such as Stokely Carmichael differed from earlier civil rights leaders in that they",
      ch("emphasized racial pride, self-determination and sometimes self-defense rather than integration and strict nonviolence.", "Black Power marked a shift in emphasis within the movement."),
      [ch("opposed all political activity.", "Black Power advocates were politically active."),
       ch("supported Jim Crow laws.", "They opposed segregation."),
       ch("believed the movement should end.", "They wanted to continue it in a different form.")],
      "Black Power emphasized pride, self-determination and self-defense.", difficulty="hard")

# ---- The Great Society and liberalism ----
B.mcq(T_GS, "Medicare and Medicaid, created in 1965,",
      ch("provided health insurance for the elderly and for the poor.", "The programs expanded access to health care."),
      [ch("banned private health insurance.", "Private insurance remained."),
       ch("provided free college education.", "They were health programs."),
       ch("replaced Social Security.", "Social Security continued.")],
      "Medicare covers the elderly and Medicaid covers the poor.", difficulty="easy")

B.mcq(T_GS, "The Economic Opportunity Act of 1964, part of the War on Poverty, created programs such as",
      ch("Head Start and the Job Corps, aimed at fighting poverty through education and job training.", "The programs aimed to give disadvantaged Americans opportunities."),
      [ch("the Marshall Plan and NATO.", "Those were foreign policy programs."),
       ch("the GI Bill and the Federal-Aid Highway Act.", "Those were earlier programs."),
       ch("the Peace Corps and the Interstate Commerce Commission.", "These were not War on Poverty programs.")],
      "The act created Head Start and the Job Corps among other programs.", difficulty="medium")

B.mcq(T_GS, src("A president's commencement address, 1964", "“We are going to build a Great Society, a place where no child is denied an education because of poverty and no elderly citizen goes without care. The challenge is not just to grow rich but to improve the quality of our lives.”") + "\n\nThe passage best reflects which of the following?",
      ch("The liberal belief that the federal government should act to reduce poverty and expand opportunity.", "The speaker promises federal action on education and care."),
      [ch("A call for smaller government and lower taxes.", "The speaker promises expanded programs."),
       ch("Support for isolationism.", "The passage concerns domestic policy."),
       ch("Opposition to federal involvement in education.", "The speaker supports it.")],
      "The passage reflects the Great Society's liberal agenda.", difficulty="medium")

B.mcq(T_GS, "The Warren Court's decisions in cases such as Gideon v. Wainwright (1963) and Miranda v. Arizona (1966)",
      ch("expanded the rights of criminal defendants.", "The Court strengthened protections in the legal process."),
      [ch("limited the rights of criminal defendants.", "The decisions expanded rights."),
       ch("ended the use of juries.", "Juries continued."),
       ch("restricted freedom of speech.", "The cases concerned defendants' rights.")],
      "The Warren Court expanded protections for defendants.", difficulty="medium")

B.mcq(T_GS, "The Immigration and Nationality Act of 1965",
      ch("ended the national origins quota system, favored family reunification and skills, and led to increased immigration from Asia and Latin America.", "The law reshaped immigration patterns."),
      [ch("restored the quotas of the 1920s.", "The act ended the quota system."),
       ch("banned all immigration from Asia.", "Immigration from Asia increased."),
       ch("limited immigration to northern Europe.", "The act opened immigration more widely.")],
      "The 1965 act ended national origins quotas.", difficulty="hard")

B.mcq(T_GS, "Barry Goldwater's 1964 presidential campaign",
      ch("lost badly, but energized a conservative movement that opposed big government and later shaped the Republican Party.", "His campaign helped launch a conservative revival."),
      [ch("won the election in a landslide.", "He lost to Johnson."),
       ch("supported the expansion of the Great Society.", "He opposed expanded federal programs."),
       ch("ended the Republican Party.", "The party continued and changed.")],
      "Goldwater's defeat nonetheless energized conservatives.", difficulty="hard")

# ---- Protest movements and the 1970s ----
B.mcq(T_PR, "President Nixon resigned in 1974 because",
      ch("the Watergate scandal revealed abuse of power and obstruction of justice, and impeachment seemed likely.", "The Watergate cover-up ended his presidency."),
      [ch("he lost the election of 1972.", "He won reelection in 1972."),
       ch("the Vietnam War ended.", "The war was ending but this was not the cause."),
       ch("the Supreme Court ruled that he was ineligible.", "He resigned after the House Judiciary Committee voted articles of impeachment and tapes were released.")],
      "Nixon resigned because of Watergate.", difficulty="easy")

B.mcq(T_PR, "Which was a result of second-wave feminism in the 1960s and 1970s?",
      ch("Title IX of the Education Amendments of 1972 prohibited sex discrimination in federally funded education.", "Feminists won new legal protections against sex discrimination."),
      [ch("The Equal Rights Amendment was ratified.", "The ERA did not receive enough state ratifications."),
       ch("Women gained the right to vote.", "That was won in 1920."),
       ch("Women were barred from higher education.", "Title IX expanded educational equality.")],
      "Title IX banned sex discrimination in educational programs receiving federal funds.", difficulty="medium")

B.mcq(T_PR, src("A student protest leaflet, 1968", "“We are told to trust the government that sends us to fight a war we did not choose, in a country we do not understand. We refuse to be silent. Bring the troops home.”") + "\n\nThe passage best reflects which of the following?",
      ch("The antiwar movement's challenge to government credibility and policy in Vietnam.", "Protesters questioned the war and the government's honesty."),
      [ch("Widespread student support for the government's Vietnam policy.", "The leaflet opposes the war."),
       ch("A call to expand the draft.", "The leaflet opposes sending young people to fight."),
       ch("Support for the Gulf of Tonkin Resolution.", "The leaflet challenges the war.")],
      "The leaflet reflects antiwar protest and distrust of government.", difficulty="medium")

B.mcq(T_PR, "The 1973 oil embargo by Arab members of OPEC contributed to",
      ch("energy shortages, higher prices and an economy suffering from both high inflation and stagnation.", "The embargo worsened economic problems of the 1970s."),
      [ch("a decade of falling fuel prices.", "Prices rose."),
       ch("lower inflation and rapid growth.", "The economy suffered stagflation."),
       ch("a ban on automobile production.", "No such ban existed.")],
      "The oil embargo worsened stagflation.", difficulty="medium")

B.mcq(T_PR, "Rachel Carson's Silent Spring (1962) and the first Earth Day in 1970 contributed to",
      ch("the growth of the environmental movement and the creation of the Environmental Protection Agency.", "Public concern led to new environmental laws and agencies."),
      [ch("the repeal of environmental regulations.", "Environmental regulation expanded."),
       ch("a ban on all industry.", "No such ban existed."),
       ch("the end of the Cold War.", "These events were not related to the Cold War's end.")],
      "Environmental activism led to new regulation and the EPA.", difficulty="hard")

B.mcq(T_PR, "Which best describes the situation facing President Carter in the late 1970s?",
      ch("Stagflation, energy problems and the Iran hostage crisis eroded confidence in his leadership, although he achieved the Camp David Accords.", "Economic and foreign policy troubles weakened his presidency."),
      [ch("A booming economy and universal popularity.", "The economy struggled."),
       ch("A peaceful world with no foreign crises.", "The Iran crisis dominated his last year."),
       ch("The success of his energy policy in ending shortages.", "Energy problems persisted.")],
      "Economic troubles and the hostage crisis hurt Carter's presidency.", difficulty="hard")

# ---- Short-answer questions ----
saq(B, T_CF,
    "Use the excerpt to answer parts A, B and C.\n\n" + src("A historian, early twenty-first century", "“The Cold War shaped American life at home as much as abroad. Fear of communism justified both a vast military establishment and campaigns against supposed subversives.”") + "\n\n**a)** Identify ONE claim made by the historian.\n\n**b)** Explain ONE development in the period 1945 to 1960 that supports the historian's claim.\n\n**c)** Explain ONE way in which the Cold War shaped domestic policy in the period 1945 to 1965 other than anticommunist campaigns.",
    [(1, "Part A: Identifies a claim, such as that the Cold War shaped domestic life or that fear of communism justified military spending and campaigns against supposed subversives"),
     (1, "Part B: Explains a development such as loyalty programs, HUAC hearings, McCarthyism, or the military buildup under NSC-68"),
     (1, "Part C: Explains an effect such as the National Defense Education Act after Sputnik, the interstate highway system's defense justification, or the argument that segregation hurt the nation's image abroad")],
    "a) The historian claims that the Cold War influenced domestic life, as fear of communism justified military growth and investigations of supposed subversives.\nb) Senator McCarthy and the House Un-American Activities Committee investigated alleged communists, and many people lost jobs or reputations on the basis of accusations.\nc) After the Soviet launch of Sputnik in 1957, Congress passed the National Defense Education Act, which increased federal funding for science and education.")

saq(B, T_CR,
    "Use the excerpt to answer parts A, B and C.\n\n" + src("A student activist's speech, 1961", "“We sat at the counter and were refused service. We did not fight back. When we were arrested, others took our places. This movement has no leader but the conscience of the people.”") + "\n\n**a)** Identify ONE strategy used by the movement described in the excerpt.\n\n**b)** Explain ONE way in which the sit-ins and similar protests contributed to the success of the civil rights movement.\n\n**c)** Explain ONE way in which the federal government responded to the civil rights movement in the period 1964 to 1965.",
    [(1, "Part A: Identifies a strategy such as sit-ins, nonviolent direct action or accepting arrest"),
     (1, "Part B: Explains an effect such as drawing national attention, spreading the movement across the South, leading to the founding of SNCC, or desegregating lunch counters"),
     (1, "Part C: Explains a response such as passage of the Civil Rights Act of 1964 or the Voting Rights Act of 1965")],
    "a) The protesters used nonviolent sit-ins, refusing to fight back even when arrested.\nb) The sit-ins spread across the South, drew national media attention and led to the founding of the Student Nonviolent Coordinating Committee, which helped force the desegregation of many lunch counters.\nc) Congress passed the Civil Rights Act of 1964, which banned discrimination in public accommodations and employment, and the Voting Rights Act of 1965, which protected Black voting rights.")

saq(B, T_GS,
    "Using your knowledge of United States history, answer parts A, B and C.\n\n**a)** Identify ONE program or law of the Great Society.\n\n**b)** Identify a SECOND, DIFFERENT program or law of the Great Society.\n\n**c)** Explain ONE criticism or limitation of the Great Society in the period 1965 to 1975.",
    [(1, "Part A: Identifies a program or law such as Medicare, Medicaid, Head Start, the Elementary and Secondary Education Act, or the Voting Rights Act"),
     (1, "Part B: Identifies a second, different program or law from the same list"),
     (1, "Part C: Explains a criticism or limit such as conservative opposition to big government, the diversion of funds and attention by the Vietnam War, or the unrest in cities showing that poverty and discrimination persisted")],
    "a) Medicare provided health insurance for the elderly.\nb) Head Start provided early education for poor children.\nc) Conservatives criticized the Great Society as an expansion of government that was costly and ineffective, and the Vietnam War took money and attention away from its goals.")

B.save()
B.brief()
