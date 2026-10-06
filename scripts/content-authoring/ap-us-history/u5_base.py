from common import *

B = base(5)
T_MD, T_SC, T_CW, T_RP, T_ER = ("manifest-destiny", "sectional-crisis", "civil-war", "reconstruction-plans-and-amendments", "end-of-reconstruction")

# ---- Manifest Destiny ----
B.mcq(T_MD, "The term Manifest Destiny, popular in the 1840s, expressed the belief that",
      ch("the United States was destined to expand across the continent.", "Supporters argued that American expansion westward was natural and inevitable."),
      [ch("the United States should avoid all foreign entanglements.", "That describes neutrality and isolationist advice, not Manifest Destiny."),
       ch("the western territories should remain under Native control.", "Manifest Destiny supported American expansion into Native lands."),
       ch("the federal government should prohibit westward settlement.", "Manifest Destiny supported settlement.")],
      "Manifest Destiny was the belief in inevitable continental expansion.", difficulty="easy")

B.mcq(T_MD, "The annexation of Texas in 1845 heightened sectional tensions primarily because",
      ch("many northerners feared it would add a large slave state and strengthen the South's political power, and it risked war with Mexico.", "Texas was a slaveholding republic, and its annexation worried opponents of slavery's expansion and angered Mexico."),
      [ch("Texas had banned slavery and many Southerners objected.", "Texas permitted slavery."),
       ch("Britain threatened to annex Texas as a free state.", "Annexation was debated in the United States over slavery and war with Mexico."),
       ch("Texas was already a Union state and the issue was its boundary.", "Texas was an independent republic before annexation.")],
      "Texas annexation raised fears of expanding slavery and led to war with Mexico.", difficulty="medium")

B.mcq(T_MD, src("A congressman's proposed amendment to a war funding bill, 1846", "“No territory taken from Mexico in this war shall ever be open to slavery.”") + "\n\nWhich of the following was the most significant effect of the proposal described in the passage?",
      ch("It intensified the national debate over slavery's expansion and divided Congress along regional lines rather than party lines.", "Northerners of both parties supported the proviso, while Southerners opposed it."),
      [ch("It became law and banned slavery in all territory acquired from Mexico.", "The House passed it more than once but the Senate did not."),
       ch("It resolved the status of slavery in Texas.", "The proposal concerned territory that might be taken from Mexico in the war."),
       ch("It ended the war with Mexico.", "The war continued until 1848.")],
      "The Wilmot Proviso intensified the sectional debate over slavery in new territories.", difficulty="medium")

B.mcq(T_MD, "Under the Treaty of Guadalupe Hidalgo (1848), Mexico",
      ch("ceded California and much of the Southwest to the United States in return for a payment.", "The Mexican Cession greatly increased the size of the United States."),
      [ch("kept California but gave Texas to the United States.", "California was part of the cession."),
       ch("was annexed entirely by the United States.", "The United States did not annex all of Mexico."),
       ch("agreed to pay damages to the United States.", "The United States paid Mexico.")],
      "The treaty gave the United States the Mexican Cession.", difficulty="medium")

B.mcq(T_MD, "The California Gold Rush that began in 1848 and 1849 most directly led to",
      ch("rapid population growth that led California to seek statehood as a free state, intensifying the debate over slavery in the new territories.", "California's rapid growth forced Congress to decide whether to admit it as a free state."),
      [ch("a decline in westward migration.", "Migration to the West increased."),
       ch("an immediate war with Britain.", "The gold rush did not cause a war with Britain."),
       ch("the end of the debate over slavery in the territories.", "The gold rush intensified the debate.")],
      "California's rapid growth brought the slavery question to a head.", difficulty="hard")

B.mcq(T_MD, "The Oregon Treaty of 1846 between the United States and Britain",
      ch("divided the Oregon Country at the 49th parallel.", "The treaty settled the boundary peacefully."),
      [ch("gave the United States all of Oregon as far north as 54 degrees 40 minutes.", "The slogan about that line was not achieved."),
       ch("gave Britain control of present-day Washington State.", "The 49th parallel boundary placed that region in the United States."),
       ch("annexed Texas.", "Texas was annexed in 1845, not in this treaty.")],
      "The Oregon Treaty set the boundary at the 49th parallel.", difficulty="medium")

# ---- The sectional crisis ----
B.mcq(T_SC, "The Fugitive Slave Act, part of the Compromise of 1850, angered many northerners because it",
      ch("required citizens to assist in capturing escaped enslaved people and denied accused fugitives a jury trial.", "The law forced northerners to take part in enforcing slavery and gave accused people few protections."),
      [ch("banned slavery in all western territories.", "The act did not ban slavery in the territories."),
       ch("ended the slave trade in the Deep South.", "The act concerned the return of fugitives."),
       ch("freed all enslaved people who reached the North.", "The act did the opposite.")],
      "The Fugitive Slave Act forced northerners to help enforce slavery and denied fugitives due process.", difficulty="easy")

B.mcq(T_SC, "The Kansas-Nebraska Act of 1854 was controversial because it",
      ch("repealed the Missouri Compromise ban on slavery north of 36 degrees 30 minutes by letting settlers decide the issue by popular sovereignty.", "The act opened the possibility that slavery could spread into territories formerly closed to it."),
      [ch("admitted California as a free state.", "California's admission was part of the Compromise of 1850."),
       ch("banned slavery in the Louisiana Purchase.", "The act did the opposite by removing the ban."),
       ch("ended the Fugitive Slave Act.", "The act did not affect the Fugitive Slave Act.")],
      "The act overturned the Missouri Compromise line and fueled sectional conflict.", difficulty="medium")

B.mcq(T_SC, src("A Supreme Court opinion, 1857", "“Persons descended from Africans held in slavery are not citizens of the United States and cannot sue in its courts. Congress has no power to prohibit slavery in the territories, since enslaved people are property protected by the Constitution.”") + "\n\nWhich of the following was a result of the decision described in the passage?",
      ch("It outraged many northerners and strengthened the Republican Party by ruling that Congress could not ban slavery in the territories.", "The ruling struck at the Republican goal of stopping slavery's expansion and increased sectional anger."),
      [ch("It settled the dispute over slavery in the territories.", "It deepened the conflict."),
       ch("It banned slavery in Kansas.", "The ruling opened the territories to slavery."),
       ch("It had no effect on national politics.", "The decision was a major political event.")],
      "The Dred Scott decision inflamed sectional tensions and helped the Republicans.", difficulty="medium")

B.mcq(T_SC, "The Republican Party, formed in the mid-1850s, was organized primarily to",
      ch("oppose the expansion of slavery into the western territories.", "Republicans united many former Whigs, Free Soilers and antislavery Democrats around keeping slavery out of the territories."),
      [ch("support the annexation of Texas.", "That issue had been settled a decade earlier."),
       ch("defend the Fugitive Slave Act.", "Republicans opposed the Act."),
       ch("promote nativism and oppose Catholic immigration.", "That describes the Know-Nothing movement.")],
      "The Republicans formed to stop the spread of slavery into the territories.", difficulty="medium")

B.mcq(T_SC, "In the Freeport Doctrine (1858), Stephen Douglas argued that",
      ch("territories could effectively exclude slavery by refusing to pass laws protecting it, despite the Dred Scott decision, which angered Southern Democrats.", "Douglas tried to reconcile popular sovereignty with the Court's ruling and lost support in the South."),
      [ch("Congress must protect slavery in every territory.", "That was the position of many Southern Democrats."),
       ch("slavery should be banned in all states.", "Douglas did not argue for nationwide abolition."),
       ch("the Fugitive Slave Act should be repealed.", "The Freeport Doctrine concerned the territories.")],
      "The Freeport Doctrine tried to reconcile popular sovereignty with Dred Scott and split Democrats.", difficulty="hard")

B.mcq(T_SC, "Which best explains why several southern states seceded after Abraham Lincoln's election in 1860?",
      ch("Southern leaders believed that a Republican president committed to stopping slavery's expansion threatened slavery and Southern political power.", "Lincoln's election showed that the South could be outvoted nationally, and secessionists feared the end of slavery's growth."),
      [ch("Lincoln had announced immediate abolition of slavery in the South.", "Lincoln did not pledge to abolish slavery in the states where it existed."),
       ch("Lincoln had won a majority of the electoral votes in the Deep South.", "Lincoln won no electoral votes from the Deep South, and he was not even on the ballot in most Southern states."),
       ch("The Supreme Court ordered the states to secede.", "No such order existed.")],
      "Secessionists feared that a Republican president threatened slavery and Southern power.", difficulty="hard")

# ---- The Civil War ----
B.mcq(T_CW, "Which was an advantage of the Union at the start of the Civil War?",
      ch("A larger population, more industry and a more extensive railroad network.", "The North had greater manpower and productive capacity."),
      [ch("A stronger tradition of military leadership.", "Many leading officers sided with the Confederacy at the start."),
       ch("A large supply of cotton to sell to European nations.", "Cotton was the South's export."),
       ch("A war fought on its own territory.", "The Confederacy fought mostly a defensive war on its own soil.")],
      "The Union had advantages in population, industry and railroads.", difficulty="easy")

B.mcq(T_CW, "The Emancipation Proclamation of 1863",
      ch("declared enslaved people in Confederate-held territory free, made ending slavery a Union war aim and allowed Black men to serve in the Union army.", "The proclamation changed the purpose of the war and opened military service to Black men."),
      [ch("freed all enslaved people everywhere in the United States, including the border states.", "It applied only to areas in rebellion."),
       ch("abolished slavery by amending the Constitution.", "The Thirteenth Amendment ended slavery in 1865."),
       ch("ended the war with the Confederacy.", "The war continued until 1865.")],
      "The proclamation freed enslaved people in Confederate territory and changed the war's aims.", difficulty="medium")

B.mcq(T_CW, src("A president's speech at a battlefield cemetery, 1863", "“We are here to honor those who gave their lives so that a nation conceived in liberty and dedicated to equality might endure. Their sacrifice calls us to finish the work they advanced, so that government of the people may not vanish from the earth.”") + "\n\nThe passage best reflects which of the following?",
      ch("The presentation of the war as a struggle to preserve the Union and fulfill ideals of liberty and equality.", "The speaker links the war's purpose to the nation's founding ideals."),
      [ch("A call for a negotiated peace with the Confederacy.", "The speaker calls for finishing the work."),
       ch("A statement that the war was fought only over states' rights.", "The speaker emphasizes liberty and equality."),
       ch("The announcement of a plan for Reconstruction.", "The passage does not describe a Reconstruction plan.")],
      "The speech linked the war to liberty and equality and to preserving the Union.", difficulty="medium")

B.mcq(T_CW, "The Union victories at Gettysburg and Vicksburg in July 1863 were significant because",
      ch("Gettysburg ended Lee's invasion of the North, and Vicksburg gave the Union control of the Mississippi River, splitting the Confederacy.", "Together the victories were a turning point in the war."),
      [ch("they ended the war and led to Lee's surrender.", "Lee surrendered in April 1865."),
       ch("they gave the Confederacy control of the Ohio River.", "They gave the Union advantages."),
       ch("they led Britain to recognize the Confederacy.", "Britain did not recognize the Confederacy.")],
      "The victories turned the war in the Union's favor.", difficulty="medium")

B.mcq(T_CW, "Which statement best describes the effect of the Civil War on the role of the federal government?",
      ch("It expanded federal power through measures such as conscription, an income tax, national paper currency and land-grant legislation.", "The war increased the government's role in the economy and in citizens' lives."),
      [ch("It reduced the power of the federal government.", "Federal power grew."),
       ch("It eliminated the need for federal taxes.", "The government introduced new taxes."),
       ch("It transferred the power to coin money to the states.", "The federal government created national currency.")],
      "The war expanded the powers of the federal government.", difficulty="hard")

B.mcq(T_CW, "African American soldiers in the Union army",
      ch("numbered about 180,000, and their service strengthened arguments for citizenship and equal rights.", "Black soldiers helped win the war and made a strong case for equal rights."),
      [ch("were barred from combat throughout the war.", "Black soldiers fought in many battles."),
       ch("fought primarily for the Confederacy.", "Those who served in the Union army fought for the Union."),
       ch("numbered only a few hundred.", "Black soldiers numbered about 180,000.")],
      "Black soldiers served in large numbers and strengthened the case for rights.", difficulty="medium")

# ---- Reconstruction plans and amendments ----
B.mcq(T_RP, "The Thirteenth Amendment, ratified in 1865,",
      ch("abolished slavery throughout the United States.", "The amendment ended slavery except as punishment for a crime."),
      [ch("gave citizenship to all persons born in the United States.", "That was the Fourteenth Amendment."),
       ch("guaranteed voting rights regardless of race.", "That was the Fifteenth Amendment."),
       ch("banned the sale of alcohol.", "That was a later amendment.")],
      "The Thirteenth Amendment abolished slavery.", difficulty="easy")

B.mcq(T_RP, "The Black Codes passed by southern states in 1865 and 1866 were intended to",
      ch("restrict the freedom of formerly enslaved people and keep them as a cheap, controlled labor force.", "The laws limited Black people's rights, movement and labor choices."),
      [ch("give freedpeople equal civil rights.", "The codes restricted rights."),
       ch("distribute plantation land to freedpeople.", "The codes did not provide land."),
       ch("end racial discrimination in the South.", "The codes enforced discrimination.")],
      "The Black Codes tried to preserve white control over Black labor.", difficulty="medium")

B.mcq(T_RP, src("A freedmen's convention petition, 1865", "“We ask for no special favors, only equal rights before the law. Give us the right to vote, to own land and to send our children to school, and we will prove ourselves loyal citizens.”") + "\n\nThe passage best reflects which of the following?",
      ch("African Americans' demands for citizenship, land and education after emancipation.", "The petitioners ask for equal rights, land ownership, education and voting."),
      [ch("Support for President Johnson's lenient plan for Reconstruction.", "The petitioners ask for more rights than the Johnson plan provided."),
       ch("A call for freedpeople to move to Africa.", "The petitioners ask for rights in the United States."),
       ch("A request to remain under planter control.", "The petitioners ask for independence and rights.")],
      "Freedpeople demanded equal rights, land, education and the vote.", difficulty="medium")

B.mcq(T_RP, "The Fourteenth Amendment, ratified in 1868, did which of the following?",
      ch("Granted citizenship to all persons born or naturalized in the United States and guaranteed equal protection and due process of law.", "The amendment overturned Dred Scott and provided new protections against state actions."),
      [ch("Abolished slavery.", "That was the Thirteenth Amendment."),
       ch("Guaranteed that the right to vote could not be denied because of race.", "That was the Fifteenth Amendment."),
       ch("Limited presidents to two terms.", "That was a later amendment.")],
      "The Fourteenth Amendment defined citizenship and guaranteed equal protection.", difficulty="medium")

B.mcq(T_RP, "Congressional Republicans passed the Reconstruction Acts of 1867 largely because",
      ch("southern states under Johnson's plan had refused to protect freedpeople's rights, and Republicans wanted to enforce civil rights through military supervision and Black suffrage.", "Congress took control of Reconstruction after Southern governments passed Black Codes and rejected the Fourteenth Amendment."),
      [ch("President Johnson had asked Congress to impose military rule.", "Johnson opposed Congressional Reconstruction."),
       ch("Southern states had fully accepted equal rights.", "Southern states had resisted equal rights."),
       ch("the Supreme Court had ordered Congress to act.", "No such order existed.")],
      "Congress acted when Southern governments refused to protect freedpeople.", difficulty="hard")

B.mcq(T_RP, "Andrew Johnson was impeached by the House of Representatives in 1868 after",
      ch("he removed the Secretary of War in violation of the Tenure of Office Act amid his conflict with Congress over Reconstruction; the Senate acquitted him by one vote.", "The impeachment grew out of a power struggle over Reconstruction policy."),
      [ch("he was convicted of treason for supporting the Confederacy.", "Johnson was acquitted and was not convicted of treason."),
       ch("he vetoed the Thirteenth Amendment.", "Presidents do not veto constitutional amendments, and Johnson supported its ratification."),
       ch("he was removed by the Senate in 1868.", "The Senate acquitted him.")],
      "Johnson was impeached over a conflict with Congress but narrowly acquitted.", difficulty="hard")

# ---- The end of Reconstruction ----
B.mcq(T_ER, "Under the system of sharecropping that emerged after the Civil War, farmers",
      ch("worked land owned by others in exchange for a share of the crop, and many fell into debt.", "Sharecropping tied many freedpeople and poor whites to debt and to landowners."),
      [ch("owned large plantations and hired workers.", "Sharecroppers did not own the land."),
       ch("were paid high cash wages and could easily buy land.", "Most sharecroppers were poor and indebted."),
       ch("received free land from the federal government.", "Most freedpeople did not receive land.")],
      "Sharecropping kept many farmers poor and in debt.", difficulty="easy")

B.mcq(T_ER, "The Compromise of 1877 resolved the disputed presidential election by",
      ch("awarding the presidency to Rutherford B. Hayes in return for the withdrawal of federal troops from the South, effectively ending Reconstruction.", "Southern Democrats accepted Hayes's election in exchange for removing federal troops."),
      [ch("giving the presidency to Samuel Tilden.", "Hayes became president."),
       ch("sending more federal troops to the South.", "Troops were withdrawn."),
       ch("passing new civil rights laws.", "The compromise ended federal enforcement efforts.")],
      "The Compromise of 1877 ended Reconstruction by removing federal troops.", difficulty="medium")

B.mcq(T_ER, src("A Southern newspaper, 1875", "“The people of this state are determined to be governed by white men. The carpetbag governments, propped up by bayonets, have squandered the public money. We shall redeem this state by the ballot if we can, and by other means if we must.”") + "\n\nThe passage best illustrates which of the following?",
      ch("The use of intimidation and violence by white Southerners to regain control of state governments and end Black political participation.", "The writer threatens force alongside electoral methods to overturn Reconstruction governments."),
      [ch("White Southerners' peaceful acceptance of Black voting.", "The passage rejects Black political power."),
       ch("The strength of federal protection for Black voters.", "The passage describes an effort to defeat federal-backed governments."),
       ch("Northern support for Southern self-government.", "The passage is a Southern point of view, not Northern.")],
      "The passage reflects the Redeemers' use of intimidation to end Reconstruction governments.", difficulty="medium")

B.mcq(T_ER, "Supreme Court decisions of the 1870s, such as the Slaughterhouse Cases and United States v. Cruikshank,",
      ch("narrowed federal protection of Black citizens' rights by interpreting the Fourteenth Amendment narrowly.", "The decisions limited the reach of federal civil rights enforcement."),
      [ch("expanded federal power to prosecute racial violence.", "The decisions limited federal power."),
       ch("overturned the Thirteenth Amendment.", "The Court did not overturn the amendment."),
       ch("granted women the right to vote.", "The decisions did not concern woman suffrage.")],
      "The Court's narrow readings of the Fourteenth Amendment weakened federal protection.", difficulty="medium")

B.mcq(T_ER, "Which factor contributed to declining Northern support for Reconstruction by the mid-1870s?",
      ch("Economic depression after the Panic of 1873, political scandals and fatigue with continuing conflict in the South.", "Many northerners turned their attention to economic problems and tired of Reconstruction."),
      [ch("A Confederate military victory.", "The Confederacy had been defeated in 1865."),
       ch("A constitutional amendment ending Reconstruction.", "No such amendment existed."),
       ch("Widespread Northern belief that the Fourteenth Amendment was unnecessary.", "The amendment had been ratified.")],
      "Economic troubles, scandals and fatigue weakened Northern support.", difficulty="hard")

B.mcq(T_ER, "Reconstruction is sometimes described as an unfinished revolution because it",
      ch("produced constitutional amendments guaranteeing freedom, citizenship and voting rights but failed to secure those rights in practice as Southern states later imposed segregation and disfranchisement.", "The legal changes were significant, but their enforcement was abandoned."),
      [ch("ended slavery without passing any constitutional amendments.", "Three amendments were passed."),
       ch("achieved full racial equality by 1877.", "Racial equality was not achieved."),
       ch("had no lasting legal effects.", "The amendments remained as foundations for later civil rights work.")],
      "Reconstruction changed the Constitution but did not secure rights in practice.", difficulty="hard")

# ---- Short-answer questions ----
saq(B, T_ER,
    "Use the excerpt to answer parts A, B and C.\n\n" + src("A historian, late twentieth century", "“Reconstruction was a revolution in law and a failure in practice. The Constitution was rewritten to guarantee equality, but the nation lacked the will to enforce it once the North grew weary of the struggle.”") + "\n\n**a)** Identify ONE claim made by the historian.\n\n**b)** Explain ONE development in the period 1865 to 1877 that supports the claim that Reconstruction was a revolution in law.\n\n**c)** Explain ONE reason that the federal government did not fully enforce equal rights in the South by 1877.",
    [(1, "Part A: Identifies a claim, such as that Reconstruction changed the law but failed to ensure equality in practice, or that the nation lacked the will to enforce the changes"),
     (1, "Part B: Explains a development such as the Thirteenth, Fourteenth and Fifteenth Amendments, the Civil Rights Act of 1866 or the Reconstruction Acts"),
     (1, "Part C: Explains a reason such as Northern weariness, the Panic of 1873, the Compromise of 1877, violent resistance by groups like the Ku Klux Klan, or Supreme Court decisions limiting federal power")],
    "a) The historian claims that Reconstruction changed the Constitution to guarantee equality but failed because the nation did not enforce it.\nb) The Thirteenth, Fourteenth and Fifteenth Amendments abolished slavery, defined citizenship and guaranteed equal protection, and barred denying the vote because of race.\nc) The Compromise of 1877 removed federal troops from the South, and the Panic of 1873 and Northern weariness reduced support for enforcing Reconstruction.")

saq(B, T_CW,
    "Use the excerpt to answer parts A, B and C.\n\n" + src("A president's letter to a newspaper editor, 1862", "“My first aim in this struggle is to save the Union, not to save or destroy slavery. If I could save the Union without freeing any enslaved person, I would do it; if by freeing all, I would do that; what I do about slavery, I do because it helps to save the Union.”") + "\n\n**a)** Identify ONE priority expressed by the author of the excerpt.\n\n**b)** Explain ONE development between 1862 and 1863 that shifted Union war aims toward emancipation.\n\n**c)** Explain ONE effect of the Emancipation Proclamation on the course of the Civil War.",
    [(1, "Part A: Identifies the priority of saving the Union, or the view that policy toward slavery should serve that goal"),
     (1, "Part B: Explains a development such as the Confiscation Acts, enslaved people escaping to Union lines, pressure from abolitionists, or the Union victory at Antietam giving Lincoln a position of strength"),
     (1, "Part C: Explains an effect such as allowing Black men to join the Union army, discouraging European recognition of the Confederacy, or encouraging enslaved people to flee to Union lines")],
    "a) The author's priority is saving the Union, and he says his policy on slavery depends on what helps to do that.\nb) Enslaved people were escaping to Union lines and Congress passed Confiscation Acts, and after the victory at Antietam, Lincoln issued the preliminary Emancipation Proclamation to make emancipation a war goal.\nc) The proclamation allowed Black men to enlist in the Union army, which added tens of thousands of soldiers, and it made it harder for Britain and France to support the Confederacy.")

saq(B, T_SC,
    "Using your knowledge of United States history, answer parts A, B and C.\n\n**a)** Identify ONE way in which the Mexican-American War contributed to sectional tension in the period 1846 to 1860.\n\n**b)** Identify ONE other event or development of the 1850s that increased sectional tension.\n\n**c)** Explain ONE reason that the Kansas-Nebraska Act led to violent conflict in Kansas.",
    [(1, "Part A: Identifies a way such as the acquisition of new territory raising the question of slavery's expansion, or the Wilmot Proviso debate"),
     (1, "Part B: Identifies an event such as the Fugitive Slave Act, Uncle Tom's Cabin, the Dred Scott decision, John Brown's raid or the formation of the Republican Party"),
     (1, "Part C: Explains that popular sovereignty invited proslavery and antislavery settlers to compete to control the territory's government, leading to fraud, armed clashes and violence")],
    "a) The land gained from Mexico raised the question of whether slavery would expand into new territory, and the Wilmot Proviso divided Congress along sectional lines.\nb) The Fugitive Slave Act of 1850 angered northerners by requiring them to help return escaped enslaved people.\nc) The Kansas-Nebraska Act let settlers decide the slavery question by popular sovereignty, so proslavery and antislavery groups rushed into Kansas, leading to fraud and armed conflict known as Bleeding Kansas.")

B.save()
B.brief()
