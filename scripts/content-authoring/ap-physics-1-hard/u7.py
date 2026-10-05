import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from authoring import *

g = 9.8
B = Bank("ap-physics-1", "ap-phys1", 7, "unit-7-torque-and-rotational-motion")
T_KIN, T_TOR, T_EQ, T_I, T_L = ("rotational-kinematics", "torque", "rotational-equilibrium", "moment-of-inertia-and-rotational-kinetic-energy", "angular-momentum")

# 1. revolutions from angular acceleration
theta = 0.5 * 2.0 * 5.0**2
revs = theta / (2 * math.pi)
assert theta == 25 and sig(revs, 2) == "4"
B.mcq(T_KIN, "A wheel starts from rest and has a constant angular acceleration of 2.0 rad/s^2. How many revolutions does it make in the first 5.0 s?",
      ch("4.0 revolutions", "$\\theta=\\frac12\\alpha t^2=\\frac12(2.0)(5.0)^2=25$ rad. One revolution is $2\\pi$ rad, so $\\frac{25}{2\\pi}\\approx4.0$ revolutions.", revs),
      [ch("25 revolutions", "25 is the angle in *radians*. Divide by $2\\pi$ to convert to revolutions.", 25.0),
       ch("1.6 revolutions", "This converts the final angular speed (10 rad/s) rather than the angle turned: $\\frac{10}{2\\pi}$. The wheel's angle is $\\frac12\\alpha t^2$.", 10 / (2 * math.pi)),
       ch("8.0 revolutions", "This is $\\frac{\\theta}{\\pi}$, dividing by $\\pi$ instead of $2\\pi$.", theta / math.pi)],
      "Use the rotational kinematic equation $\\theta=\\omega_0t+\\frac12\\alpha t^2$, then convert radians to revolutions.")

# 2. seesaw balance
d = 40 * 2.0 / 25
assert round(d, 6) == 3.2
B.mcq(T_EQ, "A uniform seesaw is balanced on a pivot at its center. A 40 kg child sits 2.0 m from the pivot on one side. Where must a 25 kg child sit on the other side for the seesaw to balance?",
      ch("3.2 m from the pivot", "Net torque must be zero: $(40)g(2.0)=(25)g\\,d$, so $d=\\frac{(40)(2.0)}{25}=3.2$ m. The lighter child must sit farther out.", d),
      [ch("1.25 m from the pivot", "This inverts the ratio ($\\frac{25\\times2.0}{40}$). The lighter child needs a *longer* lever arm.", 25 * 2.0 / 40),
       ch("2.0 m from the pivot", "Equal distances balance only equal masses.", 2.0),
       ch("1.6 m from the pivot", "This is half the correct distance (for example by dividing by $2\\times25$). The lighter child needs a longer lever arm, not a shorter one.", 1.6)],
      "Balance the torques about the pivot: $m_1d_1=m_2d_2$ (the seesaw's own weight acts at the pivot and exerts no torque).")

# 3. beam held by a cable at an angle
Tcab = 20 * g * 2.0 / (4.0 * math.sin(math.radians(30)))
assert round(Tcab, 6) == 196
B.mcq(T_EQ, "A uniform horizontal beam of mass 20 kg and length 4.0 m is attached to a wall by a hinge at its left end. A cable attached to its right end makes an angle of $30^\\circ$ with the beam and holds the beam in equilibrium. What is the tension in the cable? ($g=9.8$ m/s^2)",
      ch("196 N", "Take torques about the hinge. The weight (196 N) acts at the center, 2.0 m from the hinge. Only the component of the tension perpendicular to the beam, $T\\sin30^\\circ$, has a lever arm of 4.0 m: $T\\sin30^\\circ(4.0)=196(2.0)$, so $T=196$ N.", Tcab),
      [ch("98 N", "This ignores the angle: $T(4.0)=(196)(2.0)$. Only the perpendicular component $T\\sin30^\\circ$ produces torque.", 98),
       ch("113 N", "This uses $\\cos30^\\circ$ instead of $\\sin30^\\circ$. The angle is measured from the beam, so the component perpendicular to the beam is $T\\sin30^\\circ$.", 20 * g * 2.0 / (4.0 * math.cos(math.radians(30)))),
       ch("392 N", "This puts the weight at the end of the beam (4.0 m lever arm). A uniform beam's weight acts at its center.", 392)],
      "Choose the hinge as the axis (so the unknown hinge force exerts no torque), and use only the force components perpendicular to the beam.")

# 4. rolling race
B.mcq(T_I, "A solid sphere, a solid disk and a thin hoop all have the same mass and the same radius. They are released from rest at the top of an incline and roll without slipping. Which list gives the order in which they reach the bottom, from first to last?",
      ch("Sphere, disk, hoop", "All lose the same potential energy $mgh$. For rolling, $mgh=\\frac12mv^2\\left(1+\\frac{I}{mR^2}\\right)$, so the object with the smallest $\\frac{I}{mR^2}$ moves fastest: sphere ($\\frac25$), then disk ($\\frac12$), then hoop ($1$).", None),
      [ch("Hoop, disk, sphere", "This reverses the order. The hoop puts more of its kinetic energy into rotation, so it translates more slowly.", None),
       ch("All three arrive at the same time, since they have the same mass and radius", "Equal mass and radius is not enough. The distribution of the mass (the rotational inertia) determines the fraction of the energy that goes into rotation.", None),
       ch("Disk, sphere, hoop", "The sphere has a smaller $\\frac{I}{mR^2}$ ($\\frac25$) than the disk ($\\frac12$), so it is faster.", None)],
      "The smaller the rotational inertia per unit $mR^2$, the less energy goes into rotation and the faster the object moves down the incline.")

# 5. rotational kinetic energy of a disk
I = 0.5 * 2.0 * 0.50**2
KE = 0.5 * I * 10.0**2
assert KE == 12.5
B.mcq(T_I, "A uniform solid disk of mass 2.0 kg and radius 0.50 m rotates about its central axis at 10 rad/s. What is its rotational kinetic energy? (The rotational inertia of a solid disk is $\\frac12MR^2$.)",
      ch("12.5 J", "$I=\\frac12MR^2=\\frac12(2.0)(0.50)^2=0.25$ kg$\\cdot$m^2. $KE=\\frac12I\\omega^2=\\frac12(0.25)(10)^2=12.5$ J.", KE),
      [ch("25 J", "This uses $I=MR^2=0.50$, the rotational inertia of a thin hoop. A solid disk has $\\frac12MR^2$.", 25.0),
       ch("50 J", "This is $I\\omega^2$ with $I=MR^2=0.50$: both the hoop's rotational inertia and the missing factor of $\\frac12$ are errors.", 50.0),
       ch("6.25 J", "This halves the correct value, for example by applying the factor $\\frac12$ twice ($\\frac12\\cdot\\frac12I\\omega^2$).", 6.25)],
      "Compute the rotational inertia first, then use $KE=\\frac12I\\omega^2$.")

# 6. angular momentum conservation
I1, w1, I2 = 5.0, 3.0, 2.0
w2 = I1 * w1 / I2
assert w2 == 7.5
B.mcq(T_L, "A student on a frictionless rotating stool holds weights with her arms extended. Her rotational inertia is $5.0$ kg$\\cdot$m^2 and she rotates at 3.0 rad/s. She pulls the weights in, reducing her rotational inertia to $2.0$ kg$\\cdot$m^2. What is her new angular speed?",
      ch("7.5 rad/s", "With no external torque, angular momentum is conserved: $I_1\\omega_1=I_2\\omega_2$, so $\\omega_2=\\frac{(5.0)(3.0)}{2.0}=7.5$ rad/s.", w2),
      [ch("1.2 rad/s", "This inverts the ratio. A *smaller* rotational inertia gives a *larger* angular speed.", I2 * w1 / I1),
       ch("3.0 rad/s", "The angular speed changes. Angular momentum, not angular speed, is the conserved quantity.", 3.0),
       ch("19 rad/s", "This squares the ratio of the rotational inertias. Angular momentum conservation gives an inverse *linear* relation: $\\omega\\propto\\frac1I$.", w1 * (I1 / I2) ** 2)],
      "Conservation of angular momentum: $I_1\\omega_1=I_2\\omega_2$.")

# 7. kinetic energy change in the same situation
B.mcq(T_L, "A student on a frictionless rotating stool pulls her arms in, so her rotational inertia decreases from $5.0$ kg$\\cdot$m^2 to $2.0$ kg$\\cdot$m^2. By what factor does her rotational kinetic energy change?",
      ch("It increases by a factor of 2.5", "With $L=I\\omega$ constant, $KE=\\frac{L^2}{2I}$, so $\\frac{KE_2}{KE_1}=\\frac{I_1}{I_2}=\\frac{5.0}{2.0}=2.5$. The extra energy comes from the work she does pulling her arms in.", 2.5),
      [ch("It stays the same, since angular momentum is conserved", "Angular momentum is conserved, but kinetic energy is not: $KE=\\frac{L^2}{2I}$ increases as $I$ decreases.", 1.0),
       ch("It decreases by a factor of 2.5", "The kinetic energy increases. The work done by the student against the outward tendency of her arms is converted into rotational kinetic energy.", 0.4),
       ch("It increases by a factor of 6.25", "This squares the ratio. $KE\\propto\\frac{1}{I}$ at constant $L$, not $\\frac1{I^2}$.", 6.25)],
      "At constant angular momentum, $KE=\\frac{L^2}{2I}$.")

# 8. torque with an angle
tau = 0.40 * 50 * math.sin(math.radians(30))
assert round(tau, 6) == 10
B.mcq(T_TOR, "A force of 50 N is applied to a wrench at a point 0.40 m from the bolt. The force makes an angle of $30^\\circ$ with the wrench handle (measured from the line along the handle). What is the magnitude of the torque about the bolt?",
      ch("10 N$\\cdot$m", "$\\tau=rF\\sin\\theta$ with $\\theta$ the angle between the force and the lever arm: $(0.40)(50)\\sin30^\\circ=10$ N$\\cdot$m.", tau),
      [ch("20 N$\\cdot$m", "This is $rF$, which would be the torque if the force were perpendicular to the handle.", 20.0),
       ch("17 N$\\cdot$m", "This uses $\\cos30^\\circ$. The torque depends on the component of the force *perpendicular* to the lever arm, $F\\sin\\theta$ when $\\theta$ is measured from the handle.", 0.40 * 50 * math.cos(math.radians(30))),
       ch("5.0 N$\\cdot$m", "This halves the correct torque, for example by also applying $\\sin30^\\circ$ to the lever arm.", 5.0)],
      "Torque is $rF\\sin\\theta$, where $\\theta$ is the angle between the position vector (along the handle) and the force.")

# 9. angular acceleration with friction
alpha = (4.0 - 1.2) / 0.8
assert round(alpha, 6) == 3.5
B.mcq(T_TOR, "A wheel with rotational inertia 0.80 kg$\\cdot$m^2 is driven by a motor that applies a torque of 4.0 N$\\cdot$m. Friction in the bearing exerts an opposing torque of 1.2 N$\\cdot$m. What is the wheel's angular acceleration?",
      ch("3.5 rad/s^2", "The net torque is $4.0-1.2=2.8$ N$\\cdot$m. $\\alpha=\\frac{\\tau_{net}}{I}=\\frac{2.8}{0.80}=3.5$ rad/s^2.", alpha),
      [ch("5.0 rad/s^2", "This ignores the friction torque: $\\frac{4.0}{0.80}$.", 4.0 / 0.8),
       ch("1.5 rad/s^2", "This uses only the friction torque: $\\frac{1.2}{0.80}$.", 1.2 / 0.8),
       ch("0.29 rad/s^2", "This inverts the relation, $\\frac{I}{\\tau_{net}}=\\frac{0.80}{2.8}$. The relation is $\\alpha=\\frac{\\tau}{I}$.", 0.8 / 2.8)],
      "Newton's second law for rotation: $\\tau_{net}=I\\alpha$.")

# 10. hanging mass on a disk pulley
m, M = 2.0, 4.0
a = m * g / (m + M / 2)
assert round(a, 6) == 4.9
B.mcq(T_I, "A 2.0 kg block hangs from a light string wrapped around a uniform solid disk of mass 4.0 kg that can rotate freely about its central axis. The block is released from rest. What is the acceleration of the block? (The rotational inertia of a solid disk is $\\frac12MR^2$; $g=9.8$ m/s^2.)",
      ch("4.9 m/s^2", "For the block: $mg-T=ma$. For the disk: $TR=I\\alpha=\\frac12MR^2\\frac aR$, so $T=\\frac12Ma$. Adding: $mg=\\left(m+\\frac M2\\right)a$, so $a=\\frac{(2.0)(9.8)}{2.0+2.0}=4.9$ m/s^2.", a),
      [ch("9.8 m/s^2", "This is free-fall acceleration. The string pulls up on the block because the disk resists being spun up.", g),
       ch("3.3 m/s^2", "This uses $\\frac{mg}{m+M}$, treating the disk as if its whole mass moved at the block's speed. A disk's effective inertia is $\\frac M2$.", m * g / (m + M)),
       ch("6.5 m/s^2", "This uses $\\frac{mg}{m+M/4}$. The effective mass of a solid disk is $\\frac M2$, not $\\frac M4$.", m * g / (m + M / 4))],
      "Write Newton's second law for the block and the rotational form $\\tau=I\\alpha$ for the disk, with $a=\\alpha R$.")

# 11. plank with a person standing on it
NL = (60 * g * 4 + 20 * g * 3) / 6
NR = 80 * g - NL
assert round(NL, 6) == 490 and round(NR, 6) == 294
B.mcq(T_EQ, "A uniform 6.0 m plank of mass 20 kg rests horizontally on two supports, one at each end. A 60 kg person stands 2.0 m from the left end. What is the magnitude of the upward force exerted by the right-hand support? ($g=9.8$ m/s^2)",
      ch("294 N", "Take torques about the left end: $N_R(6.0)=(60g)(2.0)+(20g)(3.0)=1764$ N$\\cdot$m, so $N_R=294$ N. (Check: $N_L=\\frac{(60g)(4.0)+(20g)(3.0)}{6.0}=490$ N and $N_L+N_R=784$ N $=80g$.)", NR),
      [ch("490 N", "This is the force from the *left* support, which is closer to the person and carries more of the load.", NL),
       ch("392 N", "This is half of the total weight, which is right only if the person stood at the center.", 392.0),
       ch("588 N", "This is the weight of the person alone. The plank's weight also contributes and is shared with the left support.", 588.0)],
      "Use two conditions: total force zero and total torque zero about a convenient pivot (the other support).")

# 12. rotational inertia of a dumbbell about an end
I = 2 * 1.0**2
assert I == 2.0
B.mcq(T_I, "Two small 2.0 kg masses are attached to the ends of a light rod 1.0 m long. What is the rotational inertia of this system about an axis perpendicular to the rod through one end?",
      ch("2.0 kg$\\cdot$m^2", "The mass at the axis contributes $mr^2=0$. The other mass is 1.0 m away: $(2.0)(1.0)^2=2.0$ kg$\\cdot$m^2.", I),
      [ch("1.0 kg$\\cdot$m^2", "This is the value about the *center* of the rod, where each mass is 0.50 m from the axis: $2(2.0)(0.50)^2$.", 1.0),
       ch("4.0 kg$\\cdot$m^2", "This counts both masses at 1.0 m. The mass at the axis has no lever arm.", 4.0),
       ch("0.50 kg$\\cdot$m^2", "This uses $mr$ (not squared) or the wrong distances.", 0.50)],
      "$I=\\sum m_ir_i^2$ about the chosen axis; the mass on the axis contributes nothing.")

# 13. conservation of angular momentum conceptual
B.mcq(T_L, "A person standing on a frictionless rotating platform holds a weight in each outstretched hand and rotates slowly. She pulls the weights toward her body. Which statement describes what happens to her angular speed, her rotational kinetic energy and her angular momentum?",
      ch("Angular speed increases, rotational kinetic energy increases, angular momentum stays constant", "No external torque acts, so $L=I\\omega$ is constant. $I$ decreases, so $\\omega$ increases. $KE=\\frac12I\\omega^2=\\frac{L^2}{2I}$ increases because she does positive work pulling the weights inward.", None),
      [ch("Angular speed increases, rotational kinetic energy stays constant, angular momentum stays constant", "Rotational kinetic energy is $\\frac{L^2}{2I}$: it increases when $I$ decreases at constant $L$.", None),
       ch("Angular speed increases, rotational kinetic energy increases, angular momentum increases", "There is no external torque, so the angular momentum of the person-and-weights system cannot change.", None),
       ch("Angular speed stays constant, because the mass has not changed", "The mass has not changed but its distribution has. The rotational inertia decreases, so $\\omega$ must increase.", None)],
      "No external torque means $L$ is conserved. Changing $I$ changes $\\omega$ and the kinetic energy.")

# 14. work by a constant torque
Wt = 5.0 * 3 * 2 * math.pi
assert sig(Wt, 2) == "94"
B.mcq(T_TOR, "A constant net torque of 5.0 N$\\cdot$m acts on a wheel and turns it through 3.0 complete revolutions. How much work does the torque do?",
      ch("94 J", "$W=\\tau\\,\\Delta\\theta$, with the angle in radians: $3.0\\text{ rev}=6\\pi\\approx18.8$ rad. $W=(5.0)(18.8)\\approx94$ J.", Wt),
      [ch("15 J", "This uses the angle in revolutions. The angle in $W=\\tau\\theta$ must be in radians.", 15.0),
       ch("31 J", "This is the work for one revolution ($2\\pi$ rad): $(5.0)(2\\pi)$. The wheel turns through three.", 10 * math.pi),
       ch("47 J", "This uses only half of the total angle, $3\\pi$ rad.", 15 * math.pi)],
      "Rotational work is $W=\\tau\\,\\Delta\\theta$ with $\\Delta\\theta$ in radians.")

# 15. speed of the top of a rolling wheel
B.mcq(T_KIN, "A wheel of radius 0.40 m rolls without slipping along a level road. Its center moves at 5.0 m/s relative to the road. What is the speed, relative to the road, of the point on the rim at the very top of the wheel?",
      ch("10 m/s", "In the center-of-mass frame every point on the rim moves at $\\omega R=5.0$ m/s. At the top this adds to the center's 5.0 m/s forward velocity: $5.0+5.0=10$ m/s.", 10.0),
      [ch("5.0 m/s", "This is the speed of the center, and also of the rim relative to the center. Relative to the road, the top point moves at the sum.", 5.0),
       ch("0 m/s", "This is the speed of the point on the rim in contact with the road, which is momentarily at rest for rolling without slipping.", 0.0),
       ch("7.1 m/s", "This is $5\\sqrt2$, the speed of a rim point at the front of the wheel (level with the center) relative to the road.", 5 * math.sqrt(2))],
      "Add the velocity of the center to the velocity of the point relative to the center. At the top both point forward.")

# ------------------------------------------------------------------ FRQs
m, M, R = 3.0, 2.0, 0.10
a = m * g / (m + M / 2)
Tn = 0.5 * M * a
v = math.sqrt(2 * a * 2.0)
alpha = a / R
assert round(a, 6) == 7.35 and round(Tn, 6) == 7.35 and sig(v, 3) == "5.42" and round(alpha, 6) == 73.5
B.frq(T_I,
      "A 3.0 kg block hangs from a light string that is wrapped around the rim of a uniform solid disk of mass 2.0 kg and radius 0.10 m. The disk can rotate without friction about a fixed horizontal axle through its center. The block is released from rest. (The rotational inertia of a solid disk is $\\frac12MR^2$; use $g=9.8$ m/s^2.)\n\n**(a)** Write Newton's second law for the block, and the rotational form of Newton's second law for the disk, in terms of the tension $T$ in the string.\n\n**(b)** Calculate the acceleration of the block.\n\n**(c)** Calculate the tension in the string.\n\n**(d)** Calculate the speed of the block after it has descended 2.0 m, and the angular acceleration of the disk.",
      [(1, "(a) Block: $mg-T=ma$"),
       (1, "(a) Disk: $TR=I\\alpha$ with $I=\\frac12MR^2$ and $\\alpha=\\frac aR$, so $T=\\frac12Ma$"),
       (1, "(b) Solves for $a=\\frac{mg}{m+M/2}=7.35$ m/s^2"),
       (1, "(c) Finds $T=\\frac12Ma=7.35$ N (or $m(g-a)$)"),
       (1, "(d) Finds $v=\\sqrt{2a\\,\\Delta y}\\approx5.4$ m/s and $\\alpha=\\frac aR=73.5$ rad/s^2")],
      "(a) Taking downward as positive for the block: $mg-T=ma$. For the disk, the string's tension supplies the torque: $TR=I\\alpha=\\frac12MR^2\\alpha$.\n(b) The string does not slip, so $\\alpha=\\frac aR$ and $T=\\frac12Ma$. Substituting: $mg-\\frac12Ma=ma$, so $a=\\frac{mg}{m+\\frac M2}=\\frac{(3.0)(9.8)}{3.0+1.0}=7.35$ m/s^2.\n(c) $T=\\frac12Ma=\\frac12(2.0)(7.35)=7.35$ N. (Check: $m(g-a)=3.0(2.45)=7.35$ N.)\n(d) From rest, $v=\\sqrt{2a\\,\\Delta y}=\\sqrt{2(7.35)(2.0)}\\approx5.4$ m/s. $\\alpha=\\frac aR=\\frac{7.35}{0.10}=73.5$ rad/s^2.")

W, Lb, Mb, Wl, dl = 30.0, 6.0, 30.0, 20.0, 4.5
Tc = (Mb * g * Lb / 2 + Wl * g * dl) / (Lb * 0.6)
Hx = Tc * 0.8
Hy = (Mb + Wl) * g - Tc * 0.6
Hmag = math.hypot(Hx, Hy)
assert round(Tc, 6) == 490 and round(Hx, 6) == 392 and round(Hy, 6) == 196 and sig(Hmag, 3) == "438"
B.frq(T_EQ,
      "A uniform horizontal beam of length 6.0 m and mass 30 kg is attached to a vertical wall by a hinge at its left end. A light cable connects the right end of the beam to the wall above the hinge and makes an angle of $37^\\circ$ with the beam. A 20 kg load hangs from the beam 4.5 m from the hinge. The system is in equilibrium. Use $\\sin37^\\circ=0.60$, $\\cos37^\\circ=0.80$ and $g=9.8$ m/s^2.\n\n**(a)** Write the equation for rotational equilibrium about the hinge.\n\n**(b)** Calculate the tension in the cable.\n\n**(c)** Calculate the horizontal and vertical components of the force the hinge exerts on the beam, and state the direction of each.\n\n**(d)** Calculate the magnitude of the total force the hinge exerts on the beam.",
      [(1, "(a) Takes torques about the hinge: $T\\sin37^\\circ(6.0)=(30g)(3.0)+(20g)(4.5)$"),
       (1, "(b) Solves for $T=490$ N"),
       (1, "(c) Horizontal hinge component equals $T\\cos37^\\circ=392$ N, directed away from the wall (opposing the cable's horizontal pull)"),
       (1, "(c) Vertical hinge component $=50g-T\\sin37^\\circ=196$ N upward"),
       (1, "(d) Combines the components: $\\sqrt{392^2+196^2}\\approx438$ N")],
      "(a) About the hinge, the clockwise torques from the beam's weight (at the center, 3.0 m) and the load (4.5 m) balance the counterclockwise torque of the vertical component of the tension (acting at 6.0 m): $T\\sin37^\\circ(6.0)=(30)(9.8)(3.0)+(20)(9.8)(4.5)$.\n(b) $T(0.60)(6.0)=882+882=1764$ N$\\cdot$m, so $T=490$ N.\n(c) Horizontal: the cable pulls toward the wall with $T\\cos37^\\circ=392$ N, so the hinge force must be 392 N directed away from the wall. Vertical: $T\\sin37^\\circ=294$ N upward from the cable, and the total weight is $(50)(9.8)=490$ N downward, so the hinge must supply 196 N upward.\n(d) $F=\\sqrt{392^2+196^2}\\approx438$ N.")

B.save()
B.brief()
