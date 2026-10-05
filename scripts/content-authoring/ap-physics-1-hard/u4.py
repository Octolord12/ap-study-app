import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from authoring import *

g = 9.8
B = Bank("ap-physics-1", "ap-phys1", 4, "unit-4-energy")
T_WORK, T_PE, T_CONS, T_POW = ("work-and-the-work-energy-theorem", "potential-energy", "conservation-of-energy", "power")

# 1. work from a force-position graph
d1 = graph("x (m)", "F (N)", 0, 6, -6, 12,
           [{"points": [{"x": 0, "y": 0}, {"x": 2, "y": 10}, {"x": 4, "y": 10}, {"x": 6, "y": -5}], "color": "blue"}],
           "Force versus position: rises from 0 to 10 N at x=2 m, stays at 10 N until x=4 m, then falls to -5 N at x=6 m.")
W = 10 + 20 + (10 + -5) / 2 * 2
pos_only = 10 + 20 + 0.5 * (2 * 10 / 15) * 10
assert W == 35 and round(pos_only) == 37
B.mcq(T_WORK, "A force acts on an object along the $x$-axis. The graph shows the force as a function of position from $x=0$ to $x=6$ m. How much work does the force do on the object over this displacement?",
      ch("35 J", "Work is the area under the $F$-$x$ graph, with area below the axis counting negative. From 0 to 2 m: $\\frac12(2)(10)=10$ J. From 2 to 4 m: $(2)(10)=20$ J. From 4 to 6 m the force falls from $+10$ to $-5$ N: the signed area is $\\frac{10+(-5)}{2}(2)=5$ J. Total: $35$ J.", W),
      [ch("37 J", "This counts only the positive area (up to the point where the force crosses zero) and ignores the negative area, which subtracts from the total work.", pos_only),
       ch("40 J", "This is $(10\\text{ N})(4\\text{ m})$, treating the force as 10 N over the first 4 m and ignoring the rise from zero at the start and the last segment.", 40),
       ch("30 J", "This leaves out the last 2 m of the displacement. The force still does work (a net positive 5 J) there.", 30)],
      "Work $=\\int F\\,dx$ is the signed area under the graph: split it into a triangle, a rectangle and a trapezoid that crosses the axis.", diagram=d1)

# 2. work-energy theorem with friction
v = math.sqrt(8.0**2 - 2 * 0.4 * g * 5)
assert sig(v, 2) == "5"
B.mcq(T_WORK, "A 2.0 kg block slides along a rough horizontal surface. Its speed is 8.0 m/s at one point. The coefficient of kinetic friction is 0.40. What is its speed after sliding 5.0 m farther? ($g=9.8$ m/s^2)",
      ch("5.0 m/s", "Friction does work $-\\mu_kmg\\,d=-(0.40)(2.0)(9.8)(5.0)=-39.2$ J. Then $\\frac12mv^2=\\frac12(2.0)(64)-39.2=24.8$ J, so $v=\\sqrt{24.8}\\approx5.0$ m/s.", v),
      [ch("6.7 m/s", "This uses $v^2=v_0^2-\\mu gd$, leaving out the factor 2. With kinetic energy $\\frac12mv^2$ the change gives $v^2=v_0^2-2\\mu gd$.", math.sqrt(64 - 0.4 * g * 5)),
       ch("8.0 m/s", "Friction does negative work on the block, so it slows down. The speed cannot stay the same.", 8.0),
       ch("3.5 m/s", "This halves $v^2$ after finding it ($\\sqrt{24.8/2}$). The work-energy equation already gives $v^2=24.8$ m^2/s^2.", math.sqrt(24.8 / 2))],
      "Apply the work-energy theorem: the work done by friction equals the change in kinetic energy. The mass cancels.")

# 3. speed at a lower hill
v3 = math.sqrt(2 * g * 15)
assert sig(v3, 3) == "17.1"
B.mcq(T_CONS, "A roller coaster car is released from rest at the top of a 25 m high hill on a frictionless track. What is its speed at the top of a 10 m high hill farther along the track? ($g=9.8$ m/s^2)",
      ch("17.1 m/s", "The car has dropped $25-10=15$ m: $\\frac12mv^2=mg(15)$, so $v=\\sqrt{2g(15)}=\\sqrt{294}\\approx17.1$ m/s.", v3),
      [ch("22.1 m/s", "This is $\\sqrt{2g(25)}$, the speed after a 25 m drop (the speed at ground level). The car is still 10 m above the ground.", math.sqrt(2 * g * 25)),
       ch("9.9 m/s", "This is $\\sqrt{2g(5)}$, using a drop of 5 m. The drop between the two hilltops is $25-10=15$ m.", math.sqrt(2 * g * 5)),
       ch("12.1 m/s", "This is $\\sqrt{gh}$ with $h=15$ m, which leaves out the factor 2 from $\\frac12mv^2=mgh$.", math.sqrt(g * 15))],
      "Only the change in height matters. Use $\\frac12mv^2=mg\\,\\Delta h$.")

# 4. spring launcher to a height
h = 0.5 * 200 * 0.30**2 / (0.5 * g)
assert sig(h, 3) == "1.84"
B.mcq(T_CONS, "A spring with spring constant 200 N/m is compressed 0.30 m and used to launch a 0.50 kg ball straight up from the compressed position. Ignoring friction and air resistance, how high above the launch position does the ball rise? ($g=9.8$ m/s^2)",
      ch("1.84 m", "The stored spring energy $\\frac12kx^2=\\frac12(200)(0.30)^2=9.0$ J becomes gravitational potential energy $mgh$ at the top: $h=\\frac{9.0}{(0.50)(9.8)}\\approx1.84$ m.", h),
      [ch("3.7 m", "This omits the factor of $\\frac12$ in the spring energy ($kx^2=18$ J).", 18 / (0.5 * g)),
       ch("6.1 m", "This uses $\\frac12kx=30$ J: the compression is squared in $\\frac12kx^2$.", 30 / (0.5 * g)),
       ch("0.92 m", "This halves the correct height, for example by using $\\frac14kx^2$ or by dividing by $2mg$.", h / 2)],
      "Spring potential energy at the launch becomes gravitational potential energy at the highest point (kinetic energy is zero at both).")

# 5. instantaneous power of an elevator motor
P = 800 * (g + 1.0) * 2.5
assert round(P, 6) == 21600
B.mcq(T_POW, "A motor lifts an 800 kg elevator. At one instant the elevator is moving upward at 2.5 m/s and accelerating upward at 1.0 m/s^2. What power does the motor supply to the elevator at that instant? ($g=9.8$ m/s^2)",
      ch("21.6 kW", "The cable force satisfies $F-mg=ma$, so $F=m(g+a)=800(10.8)=8640$ N. Then $P=Fv=(8640)(2.5)=21\\,600$ W.", P),
      [ch("19.6 kW", "This is $mgv$, the power at constant speed. The elevator also accelerates, so the cable force is larger.", 800 * g * 2.5),
       ch("2.0 kW", "This is $mav$, the extra power for the acceleration only. The motor also has to supply $mgv$ to lift the weight.", 800 * 1.0 * 2.5),
       ch("43 kW", "This doubles the correct value, for example by using $F=2mg$ or by counting the acceleration term twice.", 2 * P)],
      "Power is $P=Fv$. First find the force from Newton's second law, with the weight and acceleration both included.")

# 6. block sliding down a rough incline: kinetic energy at the bottom
m6, hgt, ang, mu = 3.0, 2.0, 30.0, 0.2
L = hgt / math.sin(math.radians(ang))
Wf = mu * m6 * g * math.cos(math.radians(ang)) * L
KE = m6 * g * hgt - Wf
assert sig(KE, 2) == "38" and sig(Wf, 2) == "20"
B.mcq(T_CONS, "A 3.0 kg block is released from rest at the top of a $30^\\circ$ incline whose top is 2.0 m above its bottom. The coefficient of kinetic friction is 0.20. What is the block's kinetic energy when it reaches the bottom? ($g=9.8$ m/s^2)",
      ch("38 J", "The incline is $\\frac{2.0}{\\sin30^\\circ}=4.0$ m long. Friction does $-\\mu mg\\cos30^\\circ\\,L=-(0.20)(3.0)(9.8)(0.866)(4.0)\\approx-20$ J. The gravitational potential energy lost is $mgh=58.8$ J. So $KE=58.8-20.4\\approx38$ J.", KE),
      [ch("59 J", "This is all of the gravitational potential energy, $mgh$, with no loss to friction.", m6 * g * hgt),
       ch("20 J", "This is the energy dissipated by friction, not the kinetic energy that remains.", Wf),
       ch("79 J", "This adds the energy lost to friction to $mgh$. Friction removes mechanical energy.", m6 * g * hgt + Wf)],
      "$KE_{bottom}=mgh-|W_f|$ where the friction work uses the length along the incline and the normal force $mg\\cos\\theta$.")

# 7. work done carrying a box horizontally
B.mcq(T_WORK, "A person carries a 20 kg box horizontally at constant velocity for 10 m across a level floor. How much work does the person do on the box? ($g=9.8$ m/s^2)",
      ch("0 J", "The upward force that supports the box is perpendicular to the horizontal displacement, so it does no work: $W=Fd\\cos90^\\circ=0$. With constant velocity there is no horizontal force either.", 0),
      [ch("1960 J", "This is $mgd$, treating the lifting force as if it acted along the motion. It is perpendicular to the displacement.", 1960),
       ch("200 J", "This is $(20\\text{ kg})(10\\text{ m})$, which has no physical meaning as a work value.", 200),
       ch("196 J", "This is the weight $(196\\text{ N})$ times 1, not a work value. Work requires the force component along the displacement.", 196)],
      "Work depends on the component of force along the displacement. A force perpendicular to the motion does no work.")

# 8. power scaling with speed when drag grows as v^2
B.mcq(T_POW, "A car traveling at 15 m/s on a level road requires an engine power of 20 kW to overcome air resistance. Assume that air resistance is proportional to the square of the speed and that it is the only resisting force. What power is needed to travel at a constant 30 m/s?",
      ch("160 kW", "If the drag force is proportional to $v^2$, then at constant speed $P=F_{drag}v\\propto v^3$. Doubling the speed multiplies the power by $2^3=8$: $8\\times20=160$ kW.", 160),
      [ch("40 kW", "This doubles the power, treating it as proportional to the speed. The drag force also increases with speed.", 40),
       ch("80 kW", "This multiplies the power by 4, which accounts for the drag force ($v^2$) but not the faster rate at which the force acts ($v$).", 80),
       ch("320 kW", "This multiplies by 16, as if the power were proportional to $v^4$.", 320)],
      "$P=Fv$. With $F\\propto v^2$, the power is proportional to $v^3$.")

# 9. pendulum speed at the bottom
v9 = math.sqrt(2 * g * 2.0 * (1 - math.cos(math.radians(60))))
assert sig(v9, 3) == "4.43"
B.mcq(T_CONS, "A pendulum bob on a light string of length 2.0 m is released from rest with the string making an angle of $60^\\circ$ with the vertical. What is the speed of the bob at the lowest point of its swing? ($g=9.8$ m/s^2)",
      ch("4.4 m/s", "The bob drops $L(1-\\cos60^\\circ)=2.0(0.50)=1.0$ m. Then $v=\\sqrt{2g(1.0)}\\approx4.4$ m/s.", v9),
      [ch("6.3 m/s", "This uses a drop of 2.0 m (the full length of the string). The vertical drop is $L(1-\\cos\\theta)=1.0$ m.", math.sqrt(2 * g * 2.0)),
       ch("3.1 m/s", "This uses a drop of 0.50 m, half of the true drop. The drop is $L-L\\cos60^\\circ=1.0$ m.", math.sqrt(2 * g * 0.5)),
       ch("8.9 m/s", "This uses a drop of 4.0 m. The bob cannot fall farther than the string length allows.", math.sqrt(2 * g * 4.0))],
      "Find the height lost from the geometry: the bob starts $L\\cos\\theta$ below the pivot and ends $L$ below it.")

# 10. spring plus friction, total distance
E = 0.5 * 400 * 0.10**2
d10 = E / (0.2 * 1.0 * g)
assert round(E, 6) == 2.0 and sig(d10, 2) == "1"
B.mcq(T_CONS, "A 1.0 kg block is pressed against a spring (spring constant 400 N/m), compressing it 0.10 m on a rough horizontal surface. The block is released. The coefficient of kinetic friction is 0.20. What is the total distance the block travels, counting from its starting position, before it stops? ($g=9.8$ m/s^2)",
      ch("1.0 m", "The stored energy $\\frac12kx^2=2.0$ J is all dissipated by friction: $\\mu mg\\,d=(0.20)(1.0)(9.8)d=1.96\\,d$. So $d\\approx1.0$ m.", d10),
      [ch("2.0 m", "2.0 is the stored energy in joules. The distance is the energy divided by the friction force, $\\frac{2.0}{1.96}$.", 2.0),
       ch("0.51 m", "This halves the distance, for example by dividing by $2\\mu mg$.", d10 / 2),
       ch("0.20 m", "This uses $\\mu$ as if it were a distance. The distance is the energy lost divided by the friction force.", 0.20)],
      "All of the initial spring energy ends up as thermal energy: $\\frac12kx^2=\\mu mg\\,d$.")

# 11. potential energy graph (diagram)
d11 = graph("x (m)", "U (J)", 0, 6, 0, 12,
            [{"points": [{"x": 0, "y": 10}, {"x": 2, "y": 2}, {"x": 4, "y": 6}, {"x": 6, "y": 10}], "color": "blue"}],
            "Potential energy versus position: falls from 10 J at x=0 to 2 J at x=2 m, rises to 6 J at x=4 m and to 10 J at x=6 m.")
B.mcq(T_PE, "A particle moves along the $x$-axis under the influence of a conservative force. The graph shows its potential energy $U$ as a function of position. The particle's total mechanical energy is 8 J. What is its kinetic energy at $x=4$ m?",
      ch("2 J", "$KE=E-U$. At $x=4$ m, $U=6$ J, so $KE=8-6=2$ J.", 2),
      [ch("6 J", "6 J is the potential energy at $x=4$ m (and the kinetic energy at $x=2$ m). Kinetic energy is the total minus the potential energy.", 6),
       ch("8 J", "8 J is the total mechanical energy. Some of it is potential energy at this position.", 8),
       ch("4 J", "4 J is the difference between the potential energies at $x=2$ m and $x=4$ m. The kinetic energy is $E-U(4)$.", 4)],
      "Mechanical energy is conserved: $KE=E_{total}-U(x)$.", diagram=d11)

# 12. work done by gravity along a ramp
W12 = -2.0 * g * 3.0
assert round(W12, 6) == -58.8
B.mcq(T_WORK, "A 2.0 kg block is pushed up a rough ramp that is 5.0 m long and rises 3.0 m vertically, from the bottom to the top. What is the work done by gravity on the block during this motion? ($g=9.8$ m/s^2)",
      ch("$-59$ J", "Gravity is a conservative force: its work depends only on the change in height, $W_g=-mg\\,\\Delta h=-(2.0)(9.8)(3.0)=-58.8$ J. The negative sign shows that gravity opposes the upward motion.", W12),
      [ch("$+59$ J", "The block moves up while gravity pulls down, so gravity does *negative* work.", 58.8),
       ch("$-98$ J", "This uses the length of the ramp (5.0 m) instead of the vertical rise. Only the vertical displacement matters for gravity's work.", -2.0 * g * 5.0),
       ch("$-39$ J", "This uses $\\Delta h=2.0$ m. The vertical rise is 3.0 m.", -2.0 * g * 2.0)],
      "Work by gravity is $-mg\\,\\Delta h$, independent of the path.")

# 13. Atwood machine by energy
v13 = math.sqrt(2 * (3 - 2) * g * 1.0 / (2 + 3))
assert sig(v13, 2) == "2"
B.mcq(T_CONS, "A 2.0 kg block and a 3.0 kg block are connected by a light string over a light, frictionless pulley and released from rest. What is the speed of the blocks after the heavier block has descended 1.0 m? ($g=9.8$ m/s^2)",
      ch("2.0 m/s", "Energy conservation: the heavier block loses $3gh$ and the lighter block gains $2gh$, so $(3-2)(9.8)(1.0)=9.8$ J goes into the kinetic energy of both: $\\frac12(2+3)v^2=9.8$, so $v^2=3.92$ and $v\\approx2.0$ m/s.", v13),
      [ch("4.4 m/s", "This uses only the net energy 9.8 J with a single 1.0 kg mass, $\\frac12(1.0)v^2$. Both blocks move at the same speed, so the total mass is 5.0 kg.", math.sqrt(2 * 9.8)),
       ch("3.4 m/s", "This ignores the potential energy gained by the lighter block: $3gh=29.4$ J into $\\frac12(5.0)v^2$.", math.sqrt(2 * 29.4 / 5)),
       ch("1.4 m/s", "This leaves out the factor of 2 in solving $\\frac12(5.0)v^2=9.8$, giving $v^2=\\frac{9.8}{5}$.", math.sqrt(9.8 / 5))],
      "The system's kinetic energy gain equals the net loss of gravitational potential energy: $\\frac12(m_1+m_2)v^2=(m_2-m_1)gh$.")

# 14. efficiency
Pout = 40 * g * 0.80
eff = Pout / 500 * 100
assert sig(eff, 2) == "63"
B.mcq(T_POW, "An electric motor with an input power of 500 W lifts a 40 kg load straight up at a constant speed of 0.80 m/s. What is the efficiency of the motor? ($g=9.8$ m/s^2)",
      ch("63%", "The output power is the rate at which the load gains potential energy: $mgv=(40)(9.8)(0.80)=314$ W. Efficiency $=\\frac{314}{500}\\approx63\\%$.", eff),
      [ch("37%", "This is the fraction of the input power that is wasted ($100\\%-63\\%$). Efficiency is the useful output over the input.", 100 - eff),
       ch("160%", "This inverts the ratio ($\\frac{500}{314}$). No real machine has an efficiency above 100%.", 500 / Pout * 100),
       ch("31%", "This divides the output power by 1000 W rather than 500 W.", Pout / 1000 * 100)],
      "Efficiency $=\\frac{P_{out}}{P_{in}}$ with $P_{out}=mgv$ for lifting at constant speed.")

# 15. energy lost in a bounce
lost = 0.5 * g * (2.0 - 1.5)
assert round(lost, 6) == 2.45
B.mcq(T_CONS, "A 0.50 kg ball is dropped from a height of 2.0 m onto a hard floor and rebounds to a height of 1.5 m. How much mechanical energy is lost in the collision with the floor? ($g=9.8$ m/s^2)",
      ch("2.5 J", "The mechanical energy lost is the difference in gravitational potential energy at the two turning points: $mg(2.0-1.5)=(0.50)(9.8)(0.50)=2.45$ J.", lost),
      [ch("4.9 J", "This uses a height difference of 1.0 m. The ball fell from 2.0 m and rose to 1.5 m, a difference of 0.50 m.", 0.5 * g * 1.0),
       ch("7.4 J", "This is the energy at the rebound height ($mg\\cdot1.5$), which the ball still has.", 0.5 * g * 1.5),
       ch("9.8 J", "This is the energy the ball had at its starting height ($mg\\cdot2.0$), not the energy lost.", 0.5 * g * 2.0)],
      "Compare the mechanical energy just before and just after the bounce; at the highest points all of it is potential energy.")

# ------------------------------------------------------------------ FRQs
m, k, x, mu, dr = 0.50, 300.0, 0.20, 0.30, 1.0
E0 = 0.5 * k * x**2
v1 = math.sqrt(2 * E0 / m)
Wfr = mu * m * g * dr
KE2 = E0 - Wfr
v2 = math.sqrt(2 * KE2 / m)
hmax = KE2 / (m * g)
assert round(E0, 6) == 6.0 and sig(v1, 3) == "4.9" and sig(Wfr, 3) == "1.47" and sig(v2, 3) == "4.26" and sig(hmax, 3) == "0.924"
B.frq(T_CONS,
      "A 0.50 kg block is pressed against a spring of spring constant 300 N/m on a horizontal, frictionless surface, compressing the spring by 0.20 m. The block is released. After leaving the spring, it slides across a rough section of the surface 1.0 m long (coefficient of kinetic friction 0.30), and then up a frictionless ramp. Use $g=9.8$ m/s^2.\n\n**(a)** Calculate the speed of the block as it leaves the spring.\n\n**(b)** Calculate the amount of mechanical energy converted to thermal energy as the block crosses the rough section.\n\n**(c)** Calculate the speed of the block when it leaves the rough section.\n\n**(d)** Calculate the maximum height above the horizontal surface that the block reaches on the ramp.",
      [(1, "(a) Equates the spring energy $\\frac12kx^2=6.0$ J to the kinetic energy $\\frac12mv^2$"),
       (1, "(a) Finds $v\\approx4.9$ m/s"),
       (1, "(b) Uses $\\mu mg\\,d=(0.30)(0.50)(9.8)(1.0)=1.47$ J"),
       (1, "(c) Finds the remaining kinetic energy $6.0-1.47=4.53$ J and the speed $\\approx4.3$ m/s"),
       (1, "(d) Equates the remaining kinetic energy to $mgh$ and finds $h\\approx0.92$ m")],
      "(a) $\\frac12kx^2=\\frac12mv^2$: $\\frac12(300)(0.20)^2=6.0$ J $=\\frac12(0.50)v^2$, so $v=\\sqrt{24}\\approx4.9$ m/s.\n(b) The friction force is $\\mu mg=(0.30)(0.50)(9.8)=1.47$ N over 1.0 m, so 1.47 J becomes thermal energy.\n(c) $KE=6.0-1.47=4.53$ J, so $\\frac12(0.50)v^2=4.53$ and $v=\\sqrt{18.1}\\approx4.3$ m/s.\n(d) At the top of the ramp all of the remaining kinetic energy is potential energy: $mgh=4.53$ J, so $h=\\frac{4.53}{(0.50)(9.8)}\\approx0.92$ m.")

m, v1_, v2_, t = 1000.0, 10.0, 25.0, 6.0
dKE = 0.5 * m * (v2_**2 - v1_**2)
Pavg = dKE / t
dist = (v1_ + v2_) / 2 * t
Favg = dKE / dist
Pend = Favg * v2_
assert dKE == 262500 and round(Pavg, 3) == 43750 and dist == 105 and round(Favg, 3) == 2500 and round(Pend, 3) == 62500
B.frq(T_POW,
      "A 1000 kg car on a level road accelerates uniformly from 10 m/s to 25 m/s in 6.0 s. Ignore friction and air resistance.\n\n**(a)** Calculate the change in the car's kinetic energy.\n\n**(b)** Calculate the average power delivered to the car by the engine during this time.\n\n**(c)** Calculate the distance traveled by the car during the 6.0 s, and use it to find the average net force on the car.\n\n**(d)** Calculate the instantaneous power the engine delivers at the end of the 6.0 s, and explain why it is greater than the average power.",
      [(1, "(a) Computes $\\Delta KE=\\frac12m(v_f^2-v_i^2)=2.6\\times10^5$ J (262,500 J)"),
       (1, "(b) Uses $P=\\frac{\\Delta KE}{t}\\approx4.4\\times10^4$ W"),
       (1, "(c) Finds the distance $\\frac{10+25}{2}(6.0)=105$ m"),
       (1, "(c) Finds the average force $\\frac{\\Delta KE}{d}=2500$ N"),
       (1, "(d) Computes $P=Fv=(2500)(25)=6.25\\times10^4$ W and explains that the speed (and so the power for a constant force) is increasing")],
      "(a) $\\Delta KE=\\frac12(1000)(25^2-10^2)=\\frac12(1000)(525)=2.6\\times10^5$ J.\n(b) $P_{avg}=\\frac{\\Delta KE}{t}=\\frac{262\\,500}{6.0}\\approx4.4\\times10^4$ W (44 kW).\n(c) With uniform acceleration the average speed is $\\frac{10+25}{2}=17.5$ m/s, so the distance is $(17.5)(6.0)=105$ m. $F_{net}=\\frac{\\Delta KE}{d}=\\frac{262\\,500}{105}=2500$ N (which equals $ma=1000\\times2.5$).\n(d) With a constant force of 2500 N, $P=Fv=(2500)(25)=6.25\\times10^4$ W. The power $Fv$ increases as the car speeds up, so at the end it is larger than the average over the interval, which includes the slower speeds near the start.")

B.save()
B.brief()
