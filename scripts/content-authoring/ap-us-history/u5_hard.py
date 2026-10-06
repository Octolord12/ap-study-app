from common import *

B = hard(5)
T_MD, T_SC, T_CW, T_RP, T_ER = ("manifest-destiny", "sectional-crisis", "civil-war", "reconstruction-plans-and-amendments", "end-of-reconstruction")

# ---- Manifest Destiny ----
B.mcq(T_MD, src("A Whig congressman, 1847", "“The president says Mexico shed American blood on American soil, but the ground where our soldiers were attacked was disputed. This is a war for conquest, and its fruit will be more slave states.”") + "\n\nThe argument in the passage best reflects which of the following?",
      ch("Northern opposition to the Mexican-American War based on the belief that it was provoked in order to expand slavery.", "The speaker challenges the president's justification and links the war to the extension of slavery."),
      [ch("Southern support for annexing all of Mexico.", "The speaker opposes the war and fears slave states, a Northern argument."),
       ch("Support for popular sovereignty as a solution to the slavery question.", "The passage criticizes the war and does not propose popular sovereignty."),
       ch("Approval of the president's reasons for going to war.", "The speaker disputes the president's claims.")],
      "The speaker represents Northern opposition to a war seen as aimed at expanding slavery.")

B.mcq(T_MD, "Which statement best describes the effect of the Treaty of Guadalupe Hidalgo and American expansion on Mexican residents of the new territories?",
      ch("The treaty promised citizenship and protection of property, but many Mexican Americans lost land and political influence through legal pressure, fraud and violence.", "Their formal protections were often not honored in practice."),
      [ch("The treaty gave Mexican residents full political control of the new territories.", "Control passed to the United States and to Anglo settlers."),
       ch("All Mexican residents moved to Mexico after the treaty.", "Many remained and became American citizens."),
       ch("The United States deported Mexican residents from California.", "Mexican residents were not generally deported.")],
      "Promised protections were often not honored, and many lost land and influence.")

B.mcq(T_MD, "Which statement best explains the role of racial ideas in the debate over Manifest Destiny?",
      ch("Many supporters claimed that Anglo-Saxon Americans were superior to Mexicans and Native peoples, while some opponents objected to absorbing large non-white populations into the nation.", "Racial assumptions shaped arguments on both sides of the expansion debate."),
      [ch("Both supporters and opponents argued that all races were equal and should share power.", "Racial hierarchy was assumed by many on both sides."),
       ch("The debate was entirely about economic costs, with no mention of race.", "Racial arguments were prominent."),
       ch("Racial ideas played no role because the territories were uninhabited.", "The territories were inhabited by Native peoples and Mexicans.")],
      "Racial ideas shaped arguments for and against expansion.")

# ---- The sectional crisis ----
B.mcq(T_SC, "Harriet Beecher Stowe's novel Uncle Tom's Cabin (1852) most directly",
      ch("increased northern sympathy for abolitionists and anger at the Fugitive Slave Act, while many Southerners condemned it as a distortion of slavery.", "The novel's wide readership deepened sectional feeling."),
      [ch("persuaded Congress to repeal the Fugitive Slave Act in 1853.", "The law was not repealed until 1864."),
       ch("won broad approval in the South as an accurate portrayal.", "Many Southerners rejected it."),
       ch("caused southern states to secede in 1852.", "Secession began in 1860.")],
      "The novel increased northern antislavery sentiment and southern resentment.")

B.mcq(T_SC, "Which factor best explains the collapse of the Whig Party in the 1850s?",
      ch("Sectional divisions over slavery, especially after the Kansas-Nebraska Act, split northern and southern Whigs.", "The party could not hold together as the slavery issue dominated national politics."),
      [ch("Whigs won so many elections that their opponents disappeared.", "Whigs were declining."),
       ch("The party was banned by the Compromise of 1850.", "The compromise did not ban any party."),
       ch("Whigs were united in support of the Republican Party from its start.", "Whigs divided, with many northern Whigs joining the Republicans.")],
      "Sectional conflict over slavery destroyed the Whig Party.")

B.mcq(T_SC, "John Brown's raid on Harpers Ferry in 1859 most directly increased sectional tension because",
      ch("many Southerners feared that northerners supported slave insurrection, while some northerners hailed Brown as a martyr.", "The raid and its aftermath deepened mutual distrust."),
      [ch("it caused Congress to pass the Kansas-Nebraska Act.", "That act was passed in 1854."),
       ch("it led to the election of Stephen Douglas as president.", "Douglas lost the election of 1860."),
       ch("it ended the Fugitive Slave Act.", "The raid had no such effect.")],
      "Brown's raid deepened fear in the South and sympathy for him in parts of the North.")

# ---- The Civil War ----
B.mcq(T_CW, src("A historian, late twentieth century", "“By 1864 the Union had adopted a strategy that targeted the South's economic resources and the morale of its civilians as well as its armies.”") + "\n\nWhich of the following best supports the historian's argument?",
      ch("Sherman's march through Georgia destroyed railroads, farms and supplies.", "The march deliberately damaged the Confederacy's economic capacity and civilian morale."),
      [ch("Lincoln's address at Gettysburg in 1863.", "The address was a speech about the war's purpose."),
       ch("The Union victory at Antietam in 1862.", "Antietam was a major battle, not a strategy aimed at civilian resources."),
       ch("The issuing of the Emancipation Proclamation.", "That changed war aims but was not a strategy of economic destruction.")],
      "Sherman's march is the clearest example of targeting economic resources and morale.")

B.mcq(T_CW, "Which best explains the Confederate government's difficulty in waging war?",
      ch("A strong commitment to states' rights made it hard to centralize resources and enforce conscription, and shortages and inflation weakened the home front.", "The Confederacy faced political and economic obstacles in coordinating the war effort."),
      [ch("A larger industrial base than the Union.", "The South had less industry than the North."),
       ch("A shortage of soldiers willing to fight.", "The main issues concerned resources and organization, not a lack of volunteers early in the war."),
       ch("Complete control of the Union's railroads.", "The Union held the larger railroad network.")],
      "States' rights commitments and economic shortages complicated the Confederate war effort.")

B.mcq(T_CW, "The New York City draft riots of 1863 illustrate",
      ch("northern resentment of conscription policies that let wealthy men avoid service by paying for substitutes, along with racial tensions in the North.", "Anger over class inequalities in the draft and hostility toward Black residents fueled the violence."),
      [ch("universal northern enthusiasm for the draft.", "The riots show strong resistance."),
       ch("a Confederate invasion of New York.", "The riots were a domestic disturbance."),
       ch("support for the Emancipation Proclamation among New York's working class.", "Many rioters resented the war's turn toward emancipation.")],
      "The riots reflected class and racial tensions over the draft in the North.")

# ---- Reconstruction plans and amendments ----
B.mcq(T_RP, src("A historian, early twenty-first century", "“Freedpeople were not passive recipients of rights handed down from Washington. They built churches and schools, organized politically, and pressed for land and suffrage.”") + "\n\nWhich of the following best supports the historian's argument?",
      ch("The founding of independent Black churches and schools and the election of Black officials such as Hiram Revels to public office during Reconstruction.", "These developments show freedpeople acting on their own initiative."),
      [ch("President Johnson's lenient pardons for former Confederates.", "That concerns white Southerners and federal policy, not freedpeople's initiative."),
       ch("The passage of the Black Codes.", "Those laws restricted Black people and show white efforts to control them."),
       ch("The impeachment of Andrew Johnson.", "That concerned a political struggle in Washington.")],
      "Independent institutions and Black officeholders show freedpeople's initiative.")

B.mcq(T_RP, "The Fifteenth Amendment (1870) divided the women's rights movement because it",
      ch("guaranteed Black men the right to vote but did not extend suffrage to women, leading some leaders, including Elizabeth Cady Stanton and Susan B. Anthony, to oppose it.", "Some activists felt women's rights had been set aside."),
      [ch("gave women the right to vote.", "Women did not gain the vote until 1920."),
       ch("banned Black men from voting.", "It protected Black men's voting rights."),
       ch("ended the women's rights movement.", "The movement continued.")],
      "The amendment's omission of women split the women's rights movement.")

B.mcq(T_RP, "The Enforcement Acts of 1870 and 1871 were passed in order to",
      ch("suppress violence by groups such as the Ku Klux Klan and protect Black voting rights.", "Congress authorized federal action against organized terrorism aimed at Black voters and officials."),
      [ch("exempt Southern states from the Fourteenth Amendment.", "The acts aimed to enforce the amendments."),
       ch("end military supervision of the South.", "The acts expanded federal enforcement."),
       ch("grant land to freedpeople.", "The acts did not distribute land.")],
      "The Enforcement Acts aimed to suppress the Klan and protect voting rights.")

# ---- The end of Reconstruction ----
B.mcq(T_ER, src("A freedman's testimony to a congressional committee, 1870s", "“They came at night, masked, and told us that if we voted we would be killed. Many of our people stayed home on election day. The sheriff would do nothing, and no one was punished.”") + "\n\nThe testimony best illustrates which of the following?",
      ch("How violence and intimidation undermined Black political rights despite constitutional protections.", "The witness describes terror used to keep Black citizens from voting and the failure of local authorities to protect them."),
      [ch("The effectiveness of local law enforcement in protecting Black voters.", "The witness says the sheriff did nothing."),
       ch("Widespread Black indifference to voting.", "The witness describes people being prevented by threats."),
       ch("The success of federal troops in ending political violence.", "The testimony describes continuing violence.")],
      "The testimony shows that terror undermined Black voting rights.")

B.mcq(T_ER, "Which best explains why sharecropping persisted in the South after the Civil War?",
      ch("Freedpeople lacked land and capital, planters lacked cash to pay wages, and merchants' credit created a cycle of debt that kept workers tied to the land.", "Poverty and credit arrangements trapped many farmers in the system."),
      [ch("The federal government required sharecropping in the Reconstruction Acts.", "No federal law required it."),
       ch("Former enslaved people had been given large plots of land by the Freedmen's Bureau.", "Most freedpeople did not receive land."),
       ch("Southern planters had switched to using machines and no longer needed workers.", "Southern agriculture remained labor-intensive.")],
      "Lack of land and capital and a cycle of debt kept sharecropping in place.")

B.mcq(T_ER, "After Redeemer Democrats regained control of Southern state governments, they generally",
      ch("cut taxes and public spending, including funding for schools, and passed laws that limited Black political and economic rights.", "Redeemer governments reversed many Reconstruction-era policies."),
      [ch("expanded public education and protected Black voting.", "They reduced spending on schools and limited Black rights."),
       ch("redistributed land to freedpeople.", "Land redistribution was not carried out."),
       ch("asked the federal government to send more troops.", "Redeemers opposed federal intervention.")],
      "Redeemer governments cut spending and restricted Black rights.")

# ---- Short-answer and long-essay ----
saq(B, T_CW,
    "Use the excerpt to answer parts A, B and C.\n\n" + src("A Black abolitionist's recruiting speech, 1863", "“Once the Black man has a uniform on his back and a rifle in his hands, no power can deny that he has earned the rights of a citizen.”") + "\n\n**a)** Identify ONE argument made in the excerpt.\n\n**b)** Explain ONE way in which the service of Black soldiers affected the Union war effort.\n\n**c)** Explain ONE way in which Black military service shaped postwar demands for citizenship and political rights.",
    [(1, "Part A: Identifies the argument that military service earns the rights of citizenship"),
     (1, "Part B: Explains an effect such as adding about 180,000 soldiers to the Union army, strengthening its manpower, or turning the war toward emancipation"),
     (1, "Part C: Explains that Black service strengthened claims for equal rights, contributing to the Civil Rights Act of 1866 and the Fourteenth and Fifteenth Amendments")],
    "a) The speaker argues that serving as soldiers earns Black men the rights of citizenship.\nb) Black soldiers added about 180,000 men to the Union army, giving it more manpower at a crucial stage of the war and tying the Union cause to emancipation.\nc) Their service gave Black Americans and their allies a powerful argument for equal rights, which supported the Civil Rights Act of 1866 and the Fourteenth and Fifteenth Amendments.")

leq(B, T_RP,
    "**Long Essay Question**\n\nEvaluate the extent to which the Civil War and Reconstruction changed the role of the federal government in the period 1860 to 1877.",
    "A strong response states a defensible thesis, for example that the war and Reconstruction greatly expanded federal power, through taxation, a national currency, the Homestead and land-grant acts, constitutional amendments and military enforcement of civil rights, but that the federal government largely withdrew from enforcing those rights by 1877. It places the topic in the context of the sectional crisis and slavery, uses specific evidence (the income tax and greenbacks, the Thirteenth, Fourteenth and Fifteenth Amendments, the Freedmen's Bureau, the Reconstruction Acts, the Enforcement Acts, the Compromise of 1877, Supreme Court decisions in the 1870s), and uses continuity and change to weigh expansion against retreat.",
    "Thesis: Presents a defensible thesis that responds to the prompt and evaluates the extent to which the federal government's role changed",
    "Contextualization: Places the topic in a broader context, such as the sectional crisis over slavery or antebellum limits on federal power",
    "Evidence: Provides at least two specific, accurate pieces of evidence relevant to the prompt (1 point for addressing the topic with evidence, 2nd point for using specific evidence to support the argument)",
    "Analysis and reasoning: Uses continuity and change over time to structure the argument (1 point), and demonstrates complex understanding, such as showing that federal power expanded during the war and early Reconstruction but contracted after 1873 and 1877 (2nd point)")

B.save()
B.brief()
