import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from authoring import *

g = 9.8
B = Bank("ap-physics-1", "ap-phys1", 2, "unit-2-dynamics")
T_3RD, T_FBD, T_1ST, T_2ND, T_APP = ("newtons-third-law-and-systems", "free-body-diagrams", "newtons-first-law", "newtons-second-law", "applications-of-newtons-second-law")

# 1. Atwood machine tension
m1, m2 = 2.0, 3.0
a = (m2 - m1) * g / (m1 + m2)
T = m1 * (g + a)
assert abs(T - m2 * (g - a)) < 1e-9 and sig(T, 3) == "23.5"
B.mcq(T_APP, "A 2.0 kg block and a 3.0 kg block hang from the two ends of a light string that passes over a light, frictionless pulley. The blocks are released from rest. What is the tension in the string? ($g=9.8$ m/s^2)",
      ch("23.5 N", "The acceleration is $a=\\frac{(3-2)g}{5}=1.96$ m/s^2. For the 2.0 kg block (accelerating up): $T-2g=2a$, so $T=2(9.8+1.96)=23.5$ N. Check with the 3.0 kg block: $3g-T=3a$, giving the same value.", T),
      [ch("24.5 N", "This is the average of the two weights, $\\frac{19.6+29.4}{2}$. The tension is not the average of the weights; it follows from Newton's second law for either block.", 24.5),
       ch("19.6 N", "This is the weight of the lighter block. The tension would equal it only if the lighter block were not accelerating upward.", 19.6),
       ch("29.4 N", "This is the weight of the heavier block. If the tension equaled it, the heavier block would not accelerate downward.", 29.4)],
      "Write Newton's second law for each block with the common acceleration and tension, solve for $a$, then find $T$.")

# 2. block on a rough incline
theta = math.radians(30)
mu = 0.3
a_inc = g * (math.sin(theta) - mu * math.cos(theta))
assert sig(a_inc, 2) == "2.4"
B.mcq(T_APP, "A 5.0 kg block slides down a $30^\\circ$ incline. The coefficient of kinetic friction between the block and the incline is 0.30. What is the magnitude of the block's acceleration? ($g=9.8$ m/s^2)",
      ch("2.4 m/s^2", "Along the incline: $mg\\sin30^\\circ-\\mu_kmg\\cos30^\\circ=ma$, so $a=g(\\sin30^\\circ-0.30\\cos30^\\circ)=9.8(0.50-0.26)\\approx2.4$ m/s^2. The mass cancels.", a_inc),
      [ch("4.9 m/s^2", "This is the frictionless result $g\\sin30^\\circ$. Friction opposes the motion and reduces the acceleration.", g * math.sin(theta)),
       ch("2.0 m/s^2", "This subtracts $\\mu_kg=2.94$ m/s^2 from $g\\sin\\theta$. Kinetic friction is $\\mu_kN$ with $N=mg\\cos\\theta$, not $\\mu_kmg$.", g * math.sin(theta) - mu * g),
       ch("7.0 m/s^2", "This uses $g(\\cos30^\\circ-\\mu\\sin30^\\circ)$: the sine and cosine are swapped. The driving component along the incline is $mg\\sin\\theta$.", g * (math.cos(theta) - mu * math.sin(theta)))],
      "Resolve the weight into components along and perpendicular to the incline. The normal force is $mg\\cos\\theta$ and friction is $\\mu_kN$.")

# 3. scale reading in an elevator, direction of velocity versus acceleration
m = 60
N_up_slow = m * (g - 2)
assert round(N_up_slow, 6) == 468
B.mcq(T_2ND, "A 60 kg person stands on a scale in an elevator that is moving upward and slowing down, with an acceleration of magnitude 2.0 m/s^2. What does the scale read? ($g=9.8$ m/s^2)",
      ch("468 N", "Slowing down while moving up means the acceleration points downward. Taking up as positive: $N-mg=m(-2)$, so $N=m(g-2)=60(7.8)=468$ N.", N_up_slow),
      [ch("708 N", "This is the reading for an elevator accelerating *upward* ($m(g+a)$). Here the elevator moves up but the acceleration is downward because it is slowing.", m * (g + 2)),
       ch("588 N", "This is the person's true weight, the reading only when the acceleration is zero.", m * g),
       ch("120 N", "This is $ma$ alone. The scale also supports part of the weight: $N=mg-ma$.", m * 2)],
      "The scale reads the normal force. The sign of the acceleration, not the direction of the velocity, decides whether it exceeds or falls below $mg$.")

# 4. Newton's third law pair
B.mcq(T_3RD, "A book rests on a table. The Earth exerts a downward gravitational force on the book. Which force is the third-law (action-reaction) partner of that gravitational force?",
      ch("The gravitational force the book exerts on the Earth", "Third-law pairs act on *different* objects, are the same type of force, and are equal in magnitude and opposite in direction. The partner of 'Earth pulls on book' is 'book pulls on Earth'.", None),
      [ch("The normal force the table exerts on the book", "The normal force and the weight happen to be equal and opposite while the book is at rest, but they act on the same object and are different types of force. They are not a third-law pair.", None),
       ch("The normal force the book exerts on the table", "This is the third-law partner of the normal force of the table on the book, not of the gravitational force.", None),
       ch("The upward force the table exerts on the Earth", "A third-law partner involves the same two objects as the original force. The original force is between the Earth and the book, so its partner cannot involve the table.", None)],
      "A third-law pair acts on two different objects and swaps them: if A pulls on B with a force of some type, B pulls on A with the same type of force.")

# 5. pulley system with an incline
ma, mb = 6.0, 4.0
a_sys = (mb * g - ma * g * math.sin(math.radians(30))) / (ma + mb)
assert sig(a_sys, 3) == "0.98"
B.mcq(T_APP, "A 6.0 kg block on a frictionless $30^\\circ$ incline is connected by a light string over a light, frictionless pulley at the top of the incline to a 4.0 kg block that hangs vertically. The blocks are released from rest. What is the magnitude of their acceleration? ($g=9.8$ m/s^2)",
      ch("0.98 m/s^2", "The hanging block pulls with $4g=39.2$ N; the incline block's weight along the incline is $6g\\sin30^\\circ=29.4$ N. The net driving force is $9.8$ N on a total mass of $10$ kg: $a=0.98$ m/s^2.", a_sys),
      [ch("3.9 m/s^2", "This ignores the component of the incline block's weight along the incline, $\\frac{4g}{10}$.", mb * g / (ma + mb)),
       ch("1.96 m/s^2", "This uses $6g\\sin30^\\circ=29.4$ N but divides by only 5 kg or uses the wrong net force. The system has total mass $6+4=10$ kg.", 1.96),
       ch("0.49 m/s^2", "This halves the correct answer, for example by dividing the net force 9.8 N by 20 kg.", 0.49)],
      "Treat the two blocks as one system along the string: net force = (hanging weight) $-$ (component of the incline block's weight), divided by the total mass.")

# 6. table block with friction and a hanging mass
mt, mh, mu = 3.0, 2.0, 0.2
a6 = (mh * g - mu * mt * g) / (mt + mh)
assert sig(a6, 2) == "2.7"
B.mcq(T_APP, "A 3.0 kg block rests on a horizontal table and is connected by a light string over a light, frictionless pulley at the edge of the table to a 2.0 kg block that hangs vertically. The coefficient of kinetic friction between the 3.0 kg block and the table is 0.20. What is the acceleration of the blocks? ($g=9.8$ m/s^2)",
      ch("2.7 m/s^2", "Net force on the system: $m_hg-\\mu m_tg=19.6-5.88=13.7$ N. Total mass $=5.0$ kg. $a=\\frac{13.7}{5.0}\\approx2.7$ m/s^2.", a6),
      [ch("3.9 m/s^2", "This is the frictionless acceleration $\\frac{m_hg}{m_t+m_h}$. Friction on the table block reduces it.", mh * g / (mt + mh)),
       ch("3.1 m/s^2", "This computes friction using the hanging mass, $\\mu m_hg$. The friction acts on the block on the table, so use its mass: $\\mu m_tg$.", (mh * g - mu * mh * g) / (mt + mh)),
       ch("6.9 m/s^2", "This divides the net force by only the 2.0 kg hanging block. Both blocks accelerate together, so use the total mass 5.0 kg.", (mh * g - mu * mt * g) / mh)],
      "Apply Newton's second law to the system: net force along the string divided by total mass, with friction acting on the block that is on the table.")

# 7. constant speed down an incline
mu = math.tan(math.radians(37))
assert sig(mu, 2) == "0.75"
B.mcq(T_1ST, "A block slides down a $37^\\circ$ incline at constant speed. What is the coefficient of kinetic friction between the block and the incline? (Use $\\sin37^\\circ=0.60$, $\\cos37^\\circ=0.80$.)",
      ch("0.75", "Constant speed means zero net force: $mg\\sin\\theta=\\mu_kmg\\cos\\theta$, so $\\mu_k=\\tan\\theta=\\frac{0.60}{0.80}=0.75$.", 0.75),
      [ch("0.60", "This is $\\sin37^\\circ$. The friction force is $\\mu_kN$ with $N=mg\\cos\\theta$, so $\\mu_k=\\tan\\theta$.", 0.60),
       ch("0.80", "This is $\\cos37^\\circ$, the ratio of normal force to weight, not the coefficient of friction.", 0.80),
       ch("1.33", "This is $\\cot37^\\circ=\\frac{0.80}{0.60}$, the inverse of the correct ratio.", 4 / 3)],
      "At constant velocity the forces along the incline balance, so $f_k=mg\\sin\\theta$.")

# 8. pushing a box downward at an angle at constant speed
F, ang, mbox = 40.0, math.radians(30), 10.0
Nn = mbox * g + F * math.sin(ang)
mu = F * math.cos(ang) / Nn
assert sig(mu, 2) == "0.29"
B.mcq(T_1ST, "A 10 kg box is pushed across a rough horizontal floor at constant velocity by a 40 N force directed $30^\\circ$ *below* the horizontal. What is the coefficient of kinetic friction between the box and the floor? ($g=9.8$ m/s^2)",
      ch("0.29", "Horizontal: $f_k=F\\cos30^\\circ=34.6$ N. Vertical: the push has a downward component, so $N=mg+F\\sin30^\\circ=98+20=118$ N. Then $\\mu_k=\\frac{34.6}{118}\\approx0.29$.", mu),
      [ch("0.41", "This uses $\\frac{40}{98}$: the whole force as friction and the normal force as only $mg$. Neither is right here.", 40 / 98),
       ch("0.35", "This divides the friction force $34.6$ N by $mg=98$ N. The downward component of the push adds to the normal force.", F * math.cos(ang) / (mbox * g)),
       ch("0.44", "This subtracts the vertical component, $N=98-20=78$ N. A push angled *downward* adds to the normal force.", F * math.cos(ang) / (mbox * g - F * math.sin(ang)))],
      "Resolve the applied force into components. A downward-angled push increases the normal force, so friction increases too.")

# 9. two cables supporting a sign
mass = 5.0
Tc = mass * g / (2 * math.sin(math.radians(30)))
assert round(Tc, 6) == 49
B.mcq(T_FBD, "A 5.0 kg sign hangs at rest from two light cables. Each cable makes an angle of $30^\\circ$ with the horizontal. What is the tension in each cable? ($g=9.8$ m/s^2)",
      ch("49 N", "Vertically: $2T\\sin30^\\circ=mg$, so $T=\\frac{mg}{2\\sin30^\\circ}=\\frac{49}{1}=49$ N.", Tc),
      [ch("24.5 N", "This is $\\frac{mg}{2}$, which would be the tension only if the cables were vertical. At $30^\\circ$ from the horizontal each cable supplies $T\\sin30^\\circ=\\frac T2$ of vertical force.", 24.5),
       ch("98 N", "This is $2mg$. It does not follow from the force balance; each cable carries $\\frac{mg}{2\\sin30^\\circ}$.", 98),
       ch("42 N", "This is $T\\cos30^\\circ$, the *horizontal* component of the tension. The question asks for the tension itself.", 49 * math.cos(math.radians(30)))],
      "The vertical components of the two tensions together support the weight: $2T\\sin\\theta=mg$.")

# 10. holding a block on an incline
hold = 8.0 * g * 0.60
assert round(hold, 3) == 47.04
B.mcq(T_FBD, "An 8.0 kg block rests on a frictionless $37^\\circ$ incline. What force parallel to the incline, directed up the incline, holds the block at rest? (Use $\\sin37^\\circ=0.60$, $\\cos37^\\circ=0.80$, $g=9.8$ m/s^2.)",
      ch("47 N", "The component of the weight along the incline is $mg\\sin37^\\circ=(8.0)(9.8)(0.60)=47$ N, so the holding force must equal it.", hold),
      [ch("63 N", "This is $mg\\cos37^\\circ$, the component *perpendicular* to the incline (it equals the normal force).", 8.0 * g * 0.80),
       ch("78 N", "This is the full weight $mg$. Only the component along the incline needs to be balanced.", 8.0 * g),
       ch("59 N", "This is $mg\\tan37^\\circ$. The force needed along the incline is $mg\\sin37^\\circ$; the tangent does not appear in this balance.", 8.0 * g * 0.75)],
      "Balance forces along the incline: the holding force equals the component of the weight along the incline.")

# 11. mass from an a-F graph (diagram)
d11 = graph("Net force (N)", "a (m/s^2)", 0, 10, 0, 6,
            [{"points": [{"x": 0, "y": 0}, {"x": 10, "y": 5}], "color": "blue"}],
            "Graph of acceleration versus net force for a cart: a straight line from the origin to (10 N, 5 m/s^2).")
B.mcq(T_2ND, "The graph shows the acceleration of a cart as the net force on it is varied. What is the mass of the cart?",
      ch("2.0 kg", "$a=\\frac{F}{m}$, so the slope of $a$ versus $F$ is $\\frac1m=\\frac{5}{10}=0.5$ kg$^{-1}$. Therefore $m=2.0$ kg.", 2.0),
      [ch("0.50 kg", "0.50 is the slope $\\frac1m$, not the mass. The mass is its reciprocal.", 0.5),
       ch("5.0 kg", "This is the largest acceleration. The mass is $\\frac{F}{a}=\\frac{10}{5}$, not $a$ itself.", 5.0),
       ch("50 kg", "This multiplies the endpoints: $10\\times5$. Newton's second law relates them as a ratio, $m=\\frac Fa$.", 50.0)],
      "On an $a$-$F$ graph the slope equals $\\frac1m$ (acceleration per unit net force).", diagram=d11)

# 12. static versus kinetic friction
mu_s, mu_k, mbl, Fapp = 0.50, 0.40, 10.0, 45.0
fmax = mu_s * mbl * g
assert fmax == 49.0 and Fapp < fmax
B.mcq(T_1ST, "A 10 kg block rests on a horizontal surface with $\\mu_s=0.50$ and $\\mu_k=0.40$. A horizontal force of 45 N is applied to it. What is the magnitude of the friction force on the block? ($g=9.8$ m/s^2)",
      ch("45 N", "The maximum static friction is $\\mu_smg=(0.50)(98)=49$ N, which is greater than the 45 N push. The block does not move, so static friction exactly balances the applied force: 45 N.", 45.0),
      [ch("39 N", "This is the kinetic friction value $\\mu_kmg$, which applies only once the block is sliding. The block is not sliding.", mu_k * mbl * g),
       ch("49 N", "This is the *maximum* static friction. Static friction only adjusts to match the applied force, up to that limit.", fmax),
       ch("6 N", "This subtracts kinetic friction from the applied force as if the block were accelerating. The block is at rest, so the net force is zero.", Fapp - mu_k * mbl * g)],
      "Compare the applied force with the maximum static friction first. If the applied force is smaller, static friction equals it.")

# 13. third law in a collision
B.mcq(T_3RD, "A heavy truck collides head-on with a small car. During the collision, which statement is correct?",
      ch("The forces the vehicles exert on each other are equal in magnitude, and the car has the larger acceleration", "Newton's third law makes the two forces equal and opposite at every instant. With equal force magnitudes, $a=\\frac Fm$ is larger for the object with the smaller mass, the car.", None),
      [ch("The truck exerts a larger force on the car than the car exerts on the truck", "Third-law forces are always equal in magnitude, regardless of the masses or who is moving faster.", None),
       ch("The forces are equal in magnitude, and both vehicles have the same acceleration", "The forces are equal, but the accelerations are $\\frac Fm$ and differ because the masses differ.", None),
       ch("The car exerts a larger force on the truck because it is the one that is damaged", "Damage depends on the effects of the force on the structure of each vehicle, not on the force magnitudes, which are equal.", None)],
      "The two forces form a third-law pair (equal and opposite). Their different effects come from the different masses.")

# 14. scale reading to acceleration
Fs, mm = 24.0, 2.0
aa = (Fs - mm * g) / mm
assert sig(aa, 2) == "2.2"
B.mcq(T_2ND, "A 2.0 kg block hangs from a spring scale attached to the ceiling of an elevator. The scale reads 24 N. What is the acceleration of the elevator? ($g=9.8$ m/s^2)",
      ch("2.2 m/s^2 upward", "The spring pulls up with 24 N and gravity pulls down with $mg=19.6$ N. $F_{net}=24-19.6=4.4$ N upward, so $a=\\frac{4.4}{2.0}=2.2$ m/s^2 upward.", aa),
      [ch("2.2 m/s^2 downward", "The scale reads *more* than the weight, so the net force is upward. A downward acceleration would give a reading below $mg$.", -aa),
       ch("12 m/s^2 upward", "This is $\\frac{24}{2.0}$, using the scale reading as the net force. The weight also acts.", 12.0),
       ch("4.4 m/s^2 upward", "4.4 N is the net force; dividing by the mass 2.0 kg gives 2.2 m/s^2.", 4.4)],
      "The net force is the scale reading minus the weight. Divide by the mass.")

# 15. contact force within a pushed system
ms = [2.0, 3.0, 5.0]
Fp = 20.0
a15 = Fp / sum(ms)
Fc = (ms[1] + ms[2]) * a15
assert Fc == 16.0
B.mcq(T_3RD, "Three blocks of mass 2.0 kg, 3.0 kg and 5.0 kg are in contact in a row on a frictionless surface, in that order. A 20 N horizontal force pushes on the 2.0 kg block, toward the other two. What is the magnitude of the force that the 2.0 kg block exerts on the 3.0 kg block?",
      ch("16 N", "The acceleration of the whole system is $a=\\frac{20}{10}=2.0$ m/s^2. The 2.0 kg block must push the other two (total 8.0 kg) with $F=(3+5)(2.0)=16$ N.", Fc),
      [ch("20 N", "20 N is the applied force on the first block. The first block also needs a net force of $2.0\\times2.0=4$ N to accelerate itself, so only 16 N is passed on.", 20.0),
       ch("6 N", "This is the net force on the 3.0 kg block alone ($3.0\\times2.0$). The contact force it receives must also accelerate the 5.0 kg block.", 6.0),
       ch("10 N", "This is the net force on the 5.0 kg block. The 2.0 kg block exerts a force that accelerates *both* the 3.0 kg and the 5.0 kg blocks.", 10.0)],
      "The force between two blocks must accelerate every block farther along the chain.")

# ------------------------------------------------------------------ FRQs
mt, mh, mu = 4.0, 6.0, 0.25
a_f = (mh * g - mu * mt * g) / (mt + mh)
T_f = mh * (g - a_f)
v2 = 2 * a_f * 2.0
d_stop = v2 / (2 * mu * g)
assert round(a_f, 6) == 4.9 and round(T_f, 6) == 29.4 and round(d_stop, 6) == 4.0
B.frq(T_APP,
      "A 4.0 kg block rests on a horizontal table. The coefficient of kinetic friction between the block and the table is 0.25. A light string connects the block over a light, frictionless pulley at the table's edge to a 6.0 kg block that hangs vertically. The blocks are released from rest. Use $g=9.8$ m/s^2.\n\n**(a)** Draw free-body diagrams for each block (describe each force and its direction), and write Newton's second law for each block.\n\n**(b)** Calculate the acceleration of the blocks.\n\n**(c)** Calculate the tension in the string.\n\n**(d)** After the hanging block has descended 2.0 m from rest, the string is cut. How far does the 4.0 kg block slide on the table after the string is cut before it stops?",
      [(1, "(a) Lists the forces on the table block (weight, normal, tension, friction) and on the hanging block (weight, tension)"),
       (1, "(a) Writes the equations $T-\\mu m_tg=m_ta$ and $m_hg-T=m_ha$ with a common acceleration"),
       (1, "(b) Adds the equations to find $a=\\frac{m_hg-\\mu m_tg}{m_t+m_h}=4.9$ m/s^2"),
       (1, "(c) Finds $T=m_h(g-a)=29.4$ N"),
       (1, "(d) Finds the speed when the string is cut, $v^2=2a(2.0)=19.6$ m^2/s^2"),
       (1, "(d) Uses the deceleration $\\mu g=2.45$ m/s^2 to find the stopping distance $\\frac{v^2}{2\\mu g}=4.0$ m")],
      "(a) Table block: weight $m_tg$ down, normal force up, tension $T$ toward the pulley, kinetic friction $\\mu m_tg$ opposite its motion. Hanging block: weight $m_hg$ down, tension $T$ up. Taking the direction of motion as positive: $T-\\mu m_tg=m_ta$ and $m_hg-T=m_ha$.\n(b) Adding: $m_hg-\\mu m_tg=(m_t+m_h)a$, so $a=\\frac{58.8-9.8}{10}=4.9$ m/s^2.\n(c) $T=m_h(g-a)=6.0(9.8-4.9)=29.4$ N.\n(d) After 2.0 m, $v^2=2(4.9)(2.0)=19.6$ m^2/s^2. Once the string is cut, only friction acts: $a=-\\mu g=-2.45$ m/s^2. The distance is $d=\\frac{v^2}{2\\mu g}=\\frac{19.6}{4.9}=4.0$ m.")

mb = 10.0
sin37, cos37 = 0.6, 0.8
mu = 0.25
Nf = mb * g * cos37
Tconst = mb * g * sin37 + mu * Nf
a_100 = (100 - Tconst) / mb
a_break = -(mb * g * sin37 + mu * Nf) / mb
assert round(Nf, 6) == 78.4 and round(Tconst, 6) == 78.4 and round(a_100, 6) == 2.16 and round(a_break, 6) == -7.84
B.frq(T_FBD,
      "A 10 kg box is pulled up a rough $37^\\circ$ incline by a rope parallel to the incline. The coefficient of kinetic friction between the box and the incline is 0.25. Use $\\sin37^\\circ=0.60$, $\\cos37^\\circ=0.80$ and $g=9.8$ m/s^2.\n\n**(a)** Draw a free-body diagram of the box while it moves up the incline (describe each force and its direction).\n\n**(b)** Calculate the normal force exerted on the box by the incline.\n\n**(c)** Calculate the tension in the rope when the box moves up the incline at constant speed.\n\n**(d)** The tension is increased to 100 N. Calculate the box's acceleration.\n\n**(e)** The rope breaks while the box is moving up the incline. Calculate the magnitude and direction of the box's acceleration immediately afterward.",
      [(1, "(a) Shows weight, normal force perpendicular to the incline, tension up the incline, and kinetic friction down the incline"),
       (1, "(b) Finds $N=mg\\cos37^\\circ=78.4$ N"),
       (1, "(c) Sets $T=mg\\sin37^\\circ+\\mu N$ and finds 78.4 N"),
       (1, "(d) Finds $a=\\frac{100-78.4}{10}=2.16$ m/s^2 up the incline"),
       (1, "(e) Finds the net force with no rope: $mg\\sin37^\\circ+\\mu N=78.4$ N down the incline, so $a=7.84$ m/s^2 directed down the incline")],
      "(a) Weight $mg$ straight down; normal force $N$ perpendicular to and away from the incline; tension $T$ parallel to and up the incline; kinetic friction $f_k$ parallel to the incline and down it (opposing the upward motion).\n(b) Perpendicular to the incline there is no acceleration: $N=mg\\cos37^\\circ=(10)(9.8)(0.80)=78.4$ N.\n(c) At constant speed the net force is zero: $T=mg\\sin37^\\circ+\\mu_kN=58.8+0.25(78.4)=78.4$ N.\n(d) $a=\\frac{T-mg\\sin37^\\circ-\\mu_kN}{m}=\\frac{100-78.4}{10}=2.16$ m/s^2 up the incline.\n(e) Without the rope, both the weight component and friction act down the incline (the box is still moving up): $a=\\frac{58.8+19.6}{10}=7.84$ m/s^2, directed down the incline (the box slows down).")

B.save()
B.brief()
