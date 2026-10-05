import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from authoring import *

g = 9.8
B = Bank("ap-physics-1", "ap-phys1", 5, "unit-5-momentum")
T_IMP, T_CONS, T_COL, T_CM = ("momentum-and-impulse", "conservation-of-momentum", "collisions", "center-of-mass")

# 1. impulse from an F-t graph, then speed
d1 = graph("t (s)", "F (N)", 0, 5, 0, 14,
           [{"points": [{"x": 0, "y": 0}, {"x": 2, "y": 12}, {"x": 4, "y": 12}, {"x": 5, "y": 0}], "color": "blue"}],
           "Force versus time: rises from 0 to 12 N at t=2 s, stays at 12 N until t=4 s, then falls to 0 at t=5 s.")
J = 0.5 * 2 * 12 + 2 * 12 + 0.5 * 1 * 12
v = J / 2.0
assert (J, v) == (42, 21)
B.mcq(T_IMP, "A 2.0 kg object is initially at rest on a frictionless surface. The graph shows the net horizontal force on it as a function of time. What is the object's speed at $t=5$ s?",
      ch("21 m/s", "The impulse is the area under the graph: $\\frac12(2)(12)+(2)(12)+\\frac12(1)(12)=12+24+6=42$ N$\\cdot$s. Since $J=\\Delta p=m\\,\\Delta v$ and the object starts at rest, $v=\\frac{42}{2.0}=21$ m/s.", v),
      [ch("42 m/s", "42 is the impulse in N$\\cdot$s, which equals the change in momentum, not the change in speed. Divide by the mass.", 42),
       ch("84 m/s", "This multiplies the impulse by the mass. The speed is $\\frac{J}{m}$.", 84),
       ch("8.4 m/s", "This divides the impulse by the duration (5 s), which gives an average force of 8.4 N, not a speed.", 8.4)],
      "The area under an $F$-$t$ graph is the impulse, which equals the change in momentum $m\\,\\Delta v$.", diagram=d1)

# 2. perfectly inelastic collision, energy lost
m1, v1, m2 = 3.0, 4.0, 5.0
vf = m1 * v1 / (m1 + m2)
lost = 0.5 * m1 * v1**2 - 0.5 * (m1 + m2) * vf**2
assert vf == 1.5 and round(lost, 6) == 15
B.mcq(T_COL, "A 3.0 kg cart moving at 4.0 m/s collides with a stationary 5.0 kg cart. The carts stick together. How much kinetic energy is lost in the collision?",
      ch("15 J", "Momentum conservation: $v_f=\\frac{(3.0)(4.0)}{8.0}=1.5$ m/s. Initial $KE=\\frac12(3.0)(4.0)^2=24$ J. Final $KE=\\frac12(8.0)(1.5)^2=9$ J. Lost: $24-9=15$ J.", lost),
      [ch("24 J", "This is the initial kinetic energy. Some kinetic energy remains after the collision because the carts still move together.", 24),
       ch("9 J", "This is the kinetic energy that remains after the collision, not the amount lost.", 9),
       ch("12 J", "12 is the initial momentum in kg$\\cdot$m/s. It is not an energy.", 12)],
      "Find the final velocity from momentum conservation, then compare the kinetic energies before and after.")

# 3. elastic collision with unequal masses
m1, v1, m2 = 1.0, 6.0, 3.0
v1f = (m1 - m2) / (m1 + m2) * v1
v2f = 2 * m1 / (m1 + m2) * v1
assert v1f == -3 and v2f == 3
B.mcq(T_COL, "A 1.0 kg cart moving at 6.0 m/s collides head-on and elastically with a stationary 3.0 kg cart. What is the velocity of the 1.0 kg cart immediately after the collision? (Take the initial direction of motion as positive.)",
      ch("$-3.0$ m/s", "For an elastic collision both momentum and kinetic energy are conserved. Solving gives $v_{1f}=\\frac{m_1-m_2}{m_1+m_2}v_1=\\frac{1-3}{4}(6.0)=-3.0$ m/s: the lighter cart rebounds. The 3.0 kg cart moves off at $+3.0$ m/s.", v1f),
      [ch("$+3.0$ m/s", "$+3.0$ m/s is the velocity of the heavier cart after the collision. A light object that hits a heavier stationary object bounces back.", 3.0),
       ch("0 m/s", "The lighter cart would stop only if the two masses were equal. Here the heavier cart is 3 times as massive.", 0.0),
       ch("$-6.0$ m/s", "This would be the result of bouncing off an immovable wall. The 3.0 kg cart is free to move and takes some momentum.", -6.0)],
      "Use conservation of momentum together with conservation of kinetic energy (equivalently, relative speed of approach equals relative speed of separation).")

# 4. ratio of kinetic energies after a push-off
KE1 = 0.5 * 60 * 2**2
KE2 = 0.5 * 40 * 3**2
assert KE1 / KE2 == 2 / 3
B.mcq(T_CONS, "Two ice skaters, initially at rest on frictionless ice, push off each other. Skater 1 has a mass of 60 kg and moves away at 2.0 m/s. Skater 2 has a mass of 40 kg. What is the ratio $\\frac{KE_1}{KE_2}$ of their kinetic energies after the push?",
      ch("$\\dfrac23$", "Momentum is conserved from rest, so skater 2 moves at $\\frac{(60)(2.0)}{40}=3.0$ m/s. $KE_1=\\frac12(60)(2)^2=120$ J and $KE_2=\\frac12(40)(3)^2=180$ J, so the ratio is $\\frac{120}{180}=\\frac23$.", 2 / 3),
      [ch("$\\dfrac32$", "This is the reciprocal. The lighter skater moves faster and has the *larger* kinetic energy.", 3 / 2),
       ch("1", "The momenta have equal magnitudes but the kinetic energies do not: $KE=\\frac{p^2}{2m}$ is larger for the smaller mass.", 1.0),
       ch("$\\dfrac49$", "This is the ratio of the *speeds* squared, $\\left(\\frac23\\right)^2$, applied without the masses.", 4 / 9)],
      "Find the second skater's speed from conservation of momentum, then compute each kinetic energy. Equivalently, $KE=\\frac{p^2}{2m}$.")

# 5. average force from a bounce
F5 = 0.15 * (20 + 15) / 0.010
assert round(F5, 6) == 525
B.mcq(T_IMP, "A 0.15 kg ball strikes a wall horizontally at 20 m/s and rebounds horizontally at 15 m/s. The contact lasts 0.010 s. What is the magnitude of the average force the wall exerts on the ball?",
      ch("525 N", "Take the initial direction as positive: $\\Delta p=m(-15)-m(20)=-(0.15)(35)=-5.25$ kg$\\cdot$m/s. The magnitude of the average force is $\\frac{5.25}{0.010}=525$ N.", F5),
      [ch("75 N", "This uses $\\Delta v=20-15=5$ m/s. The velocity *reverses*, so the change is $20+15=35$ m/s.", 0.15 * 5 / 0.010),
       ch("300 N", "This uses only the initial momentum, $\\frac{(0.15)(20)}{0.010}$. The ball also leaves with momentum in the opposite direction.", 0.15 * 20 / 0.010),
       ch("225 N", "This uses only the final momentum, $\\frac{(0.15)(15)}{0.010}$. The change in momentum includes both the initial and final values.", 0.15 * 15 / 0.010)],
      "The impulse equals the change in momentum, with the velocity signs taken into account, and $F_{avg}=\\frac{J}{\\Delta t}$.")

# 6. center of mass of three objects
xcm = (2 * 0 + 3 * 5 + 5 * 8) / 10
assert xcm == 5.5
B.mcq(T_CM, "Three small objects lie on the $x$-axis: 2.0 kg at $x=0$, 3.0 kg at $x=5.0$ m and 5.0 kg at $x=8.0$ m. What is the $x$-coordinate of the system's center of mass?",
      ch("5.5 m", "$x_{cm}=\\frac{\\sum m_ix_i}{\\sum m_i}=\\frac{(2)(0)+(3)(5)+(5)(8)}{10}=\\frac{55}{10}=5.5$ m.", xcm),
      [ch("4.3 m", "This is the simple average of the three positions, $\\frac{0+5+8}{3}$. The center of mass weights each position by its mass.", 13 / 3),
       ch("6.9 m", "This leaves out the 2.0 kg object: $\\frac{(3)(5)+(5)(8)}{8}$. The mass at $x=0$ contributes no moment but still counts in the total mass.", 55 / 8),
       ch("2.8 m", "This divides the sum by 20 instead of the total mass 10 kg.", 55 / 20)],
      "Use $x_{cm}=\\frac{\\sum m_ix_i}{\\sum m_i}$, including every object in the total mass.")

# 7. two-dimensional perfectly inelastic collision
px, py = 2 * 3, 2 * 4
vfin = math.hypot(px, py) / 4
assert vfin == 2.5
B.mcq(T_CONS, "A 2.0 kg cart moving east at 3.0 m/s and a 2.0 kg cart moving north at 4.0 m/s collide on a frictionless horizontal surface and stick together. What is the speed of the combined carts?",
      ch("2.5 m/s", "The momenta are perpendicular: east $6.0$, north $8.0$ kg$\\cdot$m/s. The magnitude is $\\sqrt{6^2+8^2}=10$ kg$\\cdot$m/s. Divided by the combined mass 4.0 kg: $2.5$ m/s.", vfin),
      [ch("3.5 m/s", "This is the average of the two speeds. Momenta add as vectors, and the carts are not moving along the same line.", 3.5),
       ch("5.0 m/s", "This is $\\sqrt{3^2+4^2}$, the magnitude of the *velocity* sum, which ignores that the two carts' masses now move together (total mass 4.0 kg).", 5.0),
       ch("1.75 m/s", "This adds the components of momentum as scalars, $\\frac{6+8}{4}\\cdot\\frac12$, or divides $7$ by 4. Perpendicular components must be combined with the Pythagorean theorem.", 1.75)],
      "Conservation of momentum applies to each component separately. Combine the final components with the Pythagorean theorem.")

# 8. spring push-off of two carts
B.mcq(T_CONS, "Two carts of mass $m$ and $3m$ are initially at rest on a frictionless track with a compressed spring between them. When the spring is released the carts move apart. Which statement is correct just after the spring has finished expanding?",
      ch("The lighter cart has three times the speed and three times the kinetic energy of the heavier cart", "The momenta have equal magnitude: $mv_1=3mv_2$, so $v_1=3v_2$. Then $KE_1=\\frac12m(3v_2)^2=4.5mv_2^2$ and $KE_2=\\frac12(3m)v_2^2=1.5mv_2^2$: a ratio of 3.", None),
      [ch("The carts have the same speed and the same kinetic energy", "Equal speeds would give the heavier cart more momentum, but the total momentum starts at zero, so the two momenta must be equal and opposite.", None),
       ch("The carts have the same kinetic energy, and the lighter cart is faster", "Equal momentum magnitudes mean equal kinetic energies only when the masses are equal. Since $KE=\\frac{p^2}{2m}$, the lighter cart has more kinetic energy.", None),
       ch("The heavier cart has more momentum because it has more mass", "The total momentum was zero and is conserved, so the two momenta are equal in magnitude and opposite in direction.", None)],
      "Total momentum stays zero, so $m_1v_1=m_2v_2$. Then use $KE=\\frac{p^2}{2m}$.")

# 9. momentum versus kinetic energy comparison
B.mcq(T_IMP, "Object A has mass $m$ and speed $2v$. Object B has mass $4m$ and speed $v$. Which statement correctly compares them?",
      ch("B has twice the momentum of A, and they have equal kinetic energy", "$p_A=m(2v)=2mv$ and $p_B=4mv$, so B has twice the momentum. $KE_A=\\frac12m(2v)^2=2mv^2$ and $KE_B=\\frac12(4m)v^2=2mv^2$: equal.", None),
      [ch("A and B have equal momentum and equal kinetic energy", "$p_A=2mv$ but $p_B=4mv$, so the momenta differ.", None),
       ch("A has more momentum because it is faster, and more kinetic energy", "Momentum is proportional to speed *and* mass: $p_B=4mv>p_A=2mv$. The kinetic energies are equal.", None),
       ch("B has twice the momentum of A, and four times the kinetic energy", "Kinetic energy is proportional to the mass and to the *square* of the speed: $\\frac12(4m)v^2=2mv^2$, the same as A's.", None)],
      "Momentum is $mv$ and kinetic energy is $\\frac12mv^2$; compute each for both objects.")

# 10. ballistic pendulum
vc = math.sqrt(2 * g * 0.20)
vb = (2.0 / 0.020) * vc
assert sig(vc, 3) == "1.98" and sig(vb, 2) == "200"
B.mcq(T_COL, "A 0.020 kg bullet is fired horizontally into a 1.98 kg wooden block hanging from strings. The bullet embeds in the block, and the block and bullet swing up to a maximum height of 0.20 m above the starting position. What was the bullet's speed just before it hit the block? ($g=9.8$ m/s^2)",
      ch("$2.0\\times10^2$ m/s", "After the collision the combined 2.0 kg swings up: $v_c=\\sqrt{2gh}=\\sqrt{2(9.8)(0.20)}\\approx1.98$ m/s. Momentum is conserved in the collision: $(0.020)v=(2.0)(1.98)$, so $v\\approx2.0\\times10^2$ m/s.", vb),
      [ch("2.0 m/s", "This is the speed of the block and bullet just after the collision. The bullet was moving about 100 times faster before it embedded in the block.", vc),
       ch("$4.0\\times10^2$ m/s", "This doubles the correct answer, for example by using the kinetic energy of the bullet equal to the final potential energy, which ignores the energy lost in the collision.", 2 * vb),
       ch("20 m/s", "This is off by a factor of 10: the mass ratio is $\\frac{2.0}{0.020}=100$, not 10.", 0.1 * vb)],
      "Use two steps: momentum conservation during the (inelastic) collision, then energy conservation during the swing.")

# 11. which outcome is impossible
B.mcq(T_COL, "A 2.0 kg cart moving at 3.0 m/s collides head-on with a stationary 1.0 kg cart. Which of the following outcomes is impossible?",
      ch("The 2.0 kg cart stops, and the 1.0 kg cart moves off at 6.0 m/s", "Momentum is conserved ($6.0$ kg$\\cdot$m/s before and after), but the kinetic energy would increase from $9$ J to $\\frac12(1.0)(6.0)^2=18$ J. A collision cannot create mechanical energy.", None),
      [ch("Both carts move together at 2.0 m/s", "Momentum: $(2.0+1.0)(2.0)=6.0$ kg$\\cdot$m/s, equal to the initial $6.0$. Kinetic energy falls from 9 J to 6 J. A perfectly inelastic collision is allowed.", None),
       ch("The 2.0 kg cart moves at 1.0 m/s and the 1.0 kg cart moves at 4.0 m/s", "Momentum: $2.0+4.0=6.0$. Kinetic energy: $1+8=9$ J, unchanged. This is the elastic outcome and is allowed.", None),
       ch("The 2.0 kg cart moves at 1.5 m/s and the 1.0 kg cart moves at 3.0 m/s", "Momentum: $3.0+3.0=6.0$. Kinetic energy: $2.25+4.5=6.75$ J, which is less than 9 J. A partially inelastic collision is allowed.", None)],
      "A possible outcome must conserve momentum and cannot increase the total kinetic energy (and the carts cannot pass through each other).")

# 12. fragments after an explosion at the top
B.mcq(T_CM, "A projectile launched from level ground would land at a distance $R$. At the highest point of its flight it explodes into two fragments of equal mass. One fragment falls straight down with no horizontal velocity. Where does the other fragment land, measured from the launch point? Ignore air resistance.",
      ch("$1.5R$", "The explosion's forces are internal, so horizontal momentum is conserved: $mv_x=\\frac m2(0)+\\frac m2v_B$, so $v_B=2v_x$. The highest point is $\\frac R2$ from the launch point, and the fall from there takes $t=\\frac{R}{2v_x}$. The second fragment moves $2v_xt=R$ farther, landing at $\\frac R2+R=1.5R$.", None),
      [ch("$R$", "$R$ is where the *center of mass* of the two fragments lands. The fragments themselves land at $\\frac R2$ and $1.5R$, whose average is $R$.", None),
       ch("$2R$", "This would require the second fragment to travel $\\frac32R$ after the explosion. At speed $2v_x$ for the fall time $\\frac{R}{2v_x}$ it travels $R$.", None),
       ch("$0.75R$", "This treats the second fragment as if its horizontal speed were halved ($\\frac R2+\\frac R4$). It must double: the fragment that stops horizontally gives all of its horizontal momentum to the other.", None)],
      "Momentum conservation fixes the second fragment's horizontal speed at twice the original. The fall time from the top is unchanged.")

# 13. stopping time and average force
B.mcq(T_IMP, "A passenger in a car is brought from a fixed speed to rest in a crash. With an airbag, the stopping time is 0.50 s; without one, it is 0.10 s. How does the average force on the passenger with the airbag compare with the average force without it?",
      ch("It is one-fifth as large", "The change in momentum is the same, so $F_{avg}=\\frac{\\Delta p}{\\Delta t}$ is inversely proportional to the stopping time. A time 5 times longer gives a force one-fifth as large.", None),
      [ch("It is 5 times as large", "A longer stopping time *reduces* the average force for the same momentum change.", None),
       ch("It is 25 times smaller", "The force is inversely proportional to the time, not to its square.", None),
       ch("It is the same, since the momentum change is the same", "The *impulse* is the same, but the average force is the impulse divided by the time over which it acts.", None)],
      "For a fixed change in momentum, $F_{avg}=\\frac{\\Delta p}{\\Delta t}$.")

# 14. one-dimensional inelastic collision with opposite velocities
vf = (5 * 4 - 3 * 6) / 8
assert vf == 0.25
B.mcq(T_CONS, "A 5.0 kg cart moving east at 4.0 m/s collides head-on with a 3.0 kg cart moving west at 6.0 m/s. The carts stick together. What is their velocity just after the collision?",
      ch("0.25 m/s east", "Take east as positive: $(5.0)(4.0)+(3.0)(-6.0)=(8.0)v$, so $v=\\frac{20-18}{8.0}=+0.25$ m/s: east.", vf),
      [ch("0.25 m/s west", "The total momentum is $20-18=+2$ kg$\\cdot$m/s, which is positive (east), because the 5.0 kg cart has the larger momentum.", -0.25),
       ch("1.0 m/s west", "This is the average of the velocities, $\\frac{4-6}{2}$. Momentum conservation weights each velocity by its mass.", -1.0),
       ch("4.75 m/s east", "This adds the magnitudes of the two momenta, $\\frac{20+18}{8}$, as if both carts moved east. The westward momentum is negative.", 4.75)],
      "Choose a positive direction and keep the signs of the velocities in the momentum equation.")

# 15. rebound at an angle
imp = 2 * 0.20 * 10 * math.cos(math.radians(60))
assert round(imp, 6) == 2.0
B.mcq(T_IMP, "A 0.20 kg ball strikes a smooth horizontal floor with a speed of 10 m/s. Its velocity makes an angle of $60^\\circ$ with the vertical. It rebounds with the same speed and the same angle with the vertical. What is the magnitude of the impulse the floor exerts on the ball?",
      ch("2.0 N$\\cdot$s", "The horizontal velocity component is unchanged. The vertical component reverses, so $\\Delta p_y=2mv\\cos60^\\circ=2(0.20)(10)(0.50)=2.0$ N$\\cdot$s, directed upward.", imp),
      [ch("4.0 N$\\cdot$s", "This is $2mv$, which would be the impulse for a head-on bounce straight back. Here only the vertical component of the velocity reverses.", 4.0),
       ch("3.5 N$\\cdot$s", "This uses $\\sin60^\\circ$ for the component. The angle is measured from the vertical, so the vertical component is $v\\cos60^\\circ$.", 2 * 0.2 * 10 * math.sin(math.radians(60))),
       ch("0 N$\\cdot$s", "The speed is unchanged, but the *velocity* (a vector) is not, so the momentum changes.", 0.0)],
      "Resolve the velocity into components. A smooth floor exerts a force only in the vertical direction, so only the vertical component of momentum changes.")

# ------------------------------------------------------------------ FRQs
m1, v1, m2 = 0.60, 2.0, 0.20
vf = m1 * v1 / (m1 + m2)
KEi = 0.5 * m1 * v1**2
KEf = 0.5 * (m1 + m2) * vf**2
v1e = (m1 - m2) / (m1 + m2) * v1
v2e = 2 * m1 / (m1 + m2) * v1
KEe = 0.5 * m1 * v1e**2 + 0.5 * m2 * v2e**2
J2 = m2 * v2e
Fav = J2 / 0.020
assert round(vf, 6) == 1.5 and round(KEi - KEf, 6) == 0.30 and round(v1e, 6) == 1.0 and round(v2e, 6) == 3.0 and round(KEe, 6) == round(KEi, 6) and round(J2, 6) == 0.6 and round(Fav, 6) == 30
B.frq(T_COL,
      "A 0.60 kg cart moving at 2.0 m/s on a frictionless track collides head-on with a stationary 0.20 kg cart.\n\n**(a)** Suppose the carts stick together after the collision. Calculate their common speed and the kinetic energy lost.\n\n**(b)** Suppose instead that the collision is elastic. Write two equations that must be satisfied, and calculate the velocity of each cart after the collision.\n\n**(c)** Use your answers to (b) to verify that kinetic energy is conserved in the elastic collision.\n\n**(d)** In the elastic collision the carts are in contact for 0.020 s. Calculate the magnitude of the average force that the 0.60 kg cart exerts on the 0.20 kg cart.",
      [(1, "(a) Uses momentum conservation to find $v=1.5$ m/s"),
       (1, "(a) Finds the kinetic energy lost: $1.20-0.90=0.30$ J"),
       (1, "(b) Writes conservation of momentum and conservation of kinetic energy (or the relative-speed condition)"),
       (1, "(b) Finds $v_1=1.0$ m/s and $v_2=3.0$ m/s, both in the original direction"),
       (1, "(c) Shows $\\frac12(0.60)(1.0)^2+\\frac12(0.20)(3.0)^2=1.20$ J equals the initial kinetic energy"),
       (1, "(d) Finds the impulse on the small cart, $(0.20)(3.0)=0.60$ N$\\cdot$s, and $F=\\frac{0.60}{0.020}=30$ N")],
      "(a) $m_1v_1=(m_1+m_2)v$: $(0.60)(2.0)=(0.80)v$, so $v=1.5$ m/s. Initial $KE=\\frac12(0.60)(2.0)^2=1.20$ J; final $KE=\\frac12(0.80)(1.5)^2=0.90$ J. The energy lost is $0.30$ J.\n(b) Momentum: $m_1v_1=m_1v_{1f}+m_2v_{2f}$. Kinetic energy: $\\frac12m_1v_1^2=\\frac12m_1v_{1f}^2+\\frac12m_2v_{2f}^2$. Solving, $v_{1f}=\\frac{m_1-m_2}{m_1+m_2}v_1=1.0$ m/s and $v_{2f}=\\frac{2m_1}{m_1+m_2}v_1=3.0$ m/s, both in the original direction of motion.\n(c) $KE_f=\\frac12(0.60)(1.0)^2+\\frac12(0.20)(3.0)^2=0.30+0.90=1.20$ J, equal to the initial 1.20 J.\n(d) The impulse on the 0.20 kg cart is its change in momentum: $(0.20)(3.0)-0=0.60$ N$\\cdot$s. $F_{avg}=\\frac{J}{\\Delta t}=\\frac{0.60}{0.020}=30$ N.")

dF = graph("t (ms)", "F (N)", 0, 12, 0, 500,
           [{"points": [{"x": 0, "y": 0}, {"x": 4, "y": 400}, {"x": 8, "y": 400}, {"x": 12, "y": 0}], "color": "blue"}],
           "Force versus time: rises from 0 to 400 N at t=4 ms, stays at 400 N until t=8 ms, then falls to 0 at t=12 ms.")
Jt = (0.5 * 0.004 * 400) + (0.004 * 400) + (0.5 * 0.004 * 400)
mb = 0.057
vs = Jt / mb
Favg = Jt / 0.012
Jw = mb * (vs + 40)
assert round(Jt, 6) == 3.2 and sig(vs, 3) == "56.1" and sig(Favg, 3) == "267" and sig(Jw, 2) == "5.5"
B.frq(T_IMP,
      "A tennis racket strikes a stationary 0.057 kg ball. The graph shows the force that the racket exerts on the ball as a function of time during the contact. The force is horizontal.\n\n**(a)** Determine the magnitude of the impulse delivered to the ball.\n\n**(b)** Calculate the speed of the ball just after it leaves the racket.\n\n**(c)** Calculate the magnitude of the average force exerted on the ball during the 12 ms contact.\n\n**(d)** The ball then strikes a vertical wall head-on and rebounds in the opposite direction at 40 m/s. Calculate the magnitude of the impulse the wall exerts on the ball.",
      [(1, "(a) Finds the area under the graph, $0.8+1.6+0.8=3.2$ N$\\cdot$s (with the time axis converted from ms to s)"),
       (1, "(b) Uses $J=m\\,\\Delta v$ with the ball starting at rest: $v\\approx56$ m/s"),
       (1, "(c) Computes $F_{avg}=\\frac{J}{\\Delta t}=\\frac{3.2}{0.012}\\approx270$ N"),
       (1, "(d) Takes opposite directions into account: $\\Delta v=56+40$ m/s"),
       (1, "(d) Finds $J=m\\,\\Delta v\\approx5.5$ N$\\cdot$s")],
      "(a) The area under the graph (time in seconds): triangle $\\frac12(0.004)(400)=0.8$, rectangle $(0.004)(400)=1.6$, triangle $0.8$. Total: $3.2$ N$\\cdot$s.\n(b) $J=m\\,\\Delta v$ with $v_i=0$: $v=\\frac{3.2}{0.057}\\approx56$ m/s.\n(c) $F_{avg}=\\frac{J}{\\Delta t}=\\frac{3.2}{0.012}\\approx2.7\\times10^2$ N.\n(d) The velocity reverses, so the change in velocity is $56+40=96$ m/s. $J=(0.057)(96)\\approx5.5$ N$\\cdot$s.",
      diagram=dF)

B.save()
B.brief()
