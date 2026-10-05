import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from authoring import *

g = 9.8
G = 6.67e-11
B = Bank("ap-physics-1", "ap-phys1", 3, "unit-3-circular-motion-and-gravitation")
T_UCM, T_GF, T_ORB = ("uniform-circular-motion", "gravitational-force", "gravitational-fields-and-orbits")

# 1. maximum speed on a flat curve
mu, r = 0.40, 40.0
v = math.sqrt(mu * g * r)
assert sig(v, 3) == "12.5"
B.mcq(T_UCM, "A 1200 kg car rounds a flat, circular curve of radius 40 m. The coefficient of static friction between the tires and the road is 0.40. What is the greatest speed at which the car can take the curve without sliding? ($g=9.8$ m/s^2)",
      ch("12.5 m/s", "Static friction provides the centripetal force: $\\mu mg=\\frac{mv^2}{r}$, so $v=\\sqrt{\\mu gr}=\\sqrt{(0.40)(9.8)(40)}\\approx12.5$ m/s. The mass cancels.", v),
      [ch("157 m/s", "This is $\\mu gr$ without the square root. The relation gives $v^2=\\mu gr$.", mu * g * r),
       ch("19.8 m/s", "This is $\\sqrt{gr}$, leaving out the coefficient of friction $\\mu$.", math.sqrt(g * r)),
       ch("4.0 m/s", "This is $\\sqrt{\\mu r}$, leaving out $g$.", math.sqrt(mu * r))],
      "Set the maximum static friction equal to the centripetal force required, $\\mu mg=\\frac{mv^2}{r}$.")

# 2. tension at the bottom of a vertical circle
m, v, r = 0.50, 6.0, 1.2
Tb = m * (g + v**2 / r)
Tt = m * (v**2 / r - g)
assert sig(Tb, 3) == "19.9" and sig(Tt, 3) == "10.1"
B.mcq(T_UCM, "A 0.50 kg ball on a light string swings in a vertical circle of radius 1.2 m. At the lowest point of the circle the ball's speed is 6.0 m/s. What is the tension in the string at that point? ($g=9.8$ m/s^2)",
      ch("19.9 N", "At the bottom the net force toward the center (up) is $T-mg=\\frac{mv^2}{r}$. So $T=m\\left(g+\\frac{v^2}{r}\\right)=0.50(9.8+30)=19.9$ N.", Tb),
      [ch("15 N", "This is $\\frac{mv^2}{r}$ alone. The tension must also support the weight at the bottom.", m * v**2 / r),
       ch("10.1 N", "This is the tension at the *top* if the speed were 6.0 m/s there: $\\frac{mv^2}{r}-mg$. At the bottom the weight adds to the required tension.", Tt),
       ch("4.9 N", "This is the weight $mg$ alone, which ignores the centripetal requirement.", m * g)],
      "Apply Newton's second law along the radial direction: net force toward the center equals $\\frac{mv^2}{r}$, and at the bottom the center is above the ball.")

# 3. minimum speed at the top of a loop
r = 8.0
vmin = math.sqrt(g * r)
assert sig(vmin, 2) == "8.9"
B.mcq(T_UCM, "A roller coaster car goes around the inside of a vertical loop of radius 8.0 m. What is the minimum speed the car must have at the top of the loop so that it stays in contact with the track? ($g=9.8$ m/s^2)",
      ch("8.9 m/s", "At the minimum speed the normal force is zero at the top, so gravity alone provides the centripetal force: $mg=\\frac{mv^2}{r}$, giving $v=\\sqrt{gr}=\\sqrt{(9.8)(8.0)}\\approx8.9$ m/s.", vmin),
      [ch("12.5 m/s", "This is $\\sqrt{2gr}$. The condition at the top is $mg=\\frac{mv^2}{r}$ with no factor of 2.", math.sqrt(2 * g * r)),
       ch("78 m/s", "This is $gr$ without the square root. The relation gives $v^2=gr$.", g * r),
       ch("6.3 m/s", "This is $\\sqrt{gr/2}$, which would put the required centripetal force below the weight; the track would have to pull the car upward.", math.sqrt(g * r / 2))],
      "At the top, both gravity and the normal force point toward the center. The minimum speed is the one for which the normal force is zero.")

# 4. Kepler's third law
B.mcq(T_ORB, "Satellite A orbits a planet in a circular orbit of radius $R$ with period $T$. Satellite B orbits the same planet in a circular orbit of radius $4R$. What is the period of satellite B?",
      ch("$8T$", "For orbits around the same body, $T^2\\propto r^3$. With $r$ multiplied by 4, $T^2$ is multiplied by $4^3=64$, so $T$ is multiplied by 8.", None),
      [ch("$4T$", "This assumes the period is proportional to the radius. The relation is $T^2\\propto r^3$.", None),
       ch("$16T$", "This assumes $T\\propto r^2$. The correct relation is $T\\propto r^{3/2}$.", None),
       ch("$2T$", "This assumes $T\\propto\\sqrt r$. The correct relation is $T\\propto r^{3/2}$.", None)],
      "Equate gravity to the centripetal force to get $T^2=\\frac{4\\pi^2}{GM}r^3$, so $T\\propto r^{3/2}$.")

# 5. weight at an altitude equal to Earth's radius
w = 60 * g / 4
assert round(w, 6) == 147
B.mcq(T_GF, "A 60 kg astronaut is at an altitude above Earth's surface equal to Earth's radius $R_E$. What is the astronaut's weight there, meaning the gravitational force on the astronaut? ($g=9.8$ m/s^2 at the surface)",
      ch("147 N", "At this altitude the astronaut is $2R_E$ from Earth's center. The gravitational force varies as $\\frac{1}{r^2}$, so it is $\\frac14$ of the surface value: $\\frac{588}{4}=147$ N.", w),
      [ch("294 N", "This is half the surface weight. The distance from the *center* has doubled, and the force falls as the square of the distance.", 294),
       ch("588 N", "This is the weight at the surface. Gravity is still acting at altitude and has not disappeared, but it is weaker.", 588),
       ch("65 N", "This is $\\frac{588}{9}$, which corresponds to a distance of $3R_E$ from the center. An altitude of $R_E$ is a distance of $2R_E$.", 588 / 9)],
      "Use distance from the center of the Earth: altitude $R_E$ means $r=2R_E$, and $F\\propto\\frac{1}{r^2}$.")

# 6. surface gravity of another planet
gp = 2 / 0.25 * g
assert round(gp, 6) == 78.4
B.mcq(T_GF, "A planet has twice the mass of Earth and half the radius of Earth. What is the acceleration due to gravity at its surface? ($g=9.8$ m/s^2 on Earth)",
      ch("78 m/s^2", "$g=\\frac{GM}{R^2}$. With $M\\to2M$ and $R\\to\\frac R2$: $g\\to\\frac{2}{(1/2)^2}g=8g=78.4$ m/s^2.", gp),
      [ch("19.6 m/s^2", "This doubles $g$ for the doubled mass but ignores the effect of the smaller radius.", 2 * g),
       ch("39 m/s^2", "This multiplies by 4. Halving the radius multiplies $g$ by 4, but the doubled mass multiplies it by a further 2.", 4 * g),
       ch("4.9 m/s^2", "This halves $g$. Both changes increase the surface gravity.", g / 2)],
      "Surface gravity scales as $\\frac{M}{R^2}$.")

# 7. banked curve
theta = math.degrees(math.atan(14**2 / (g * 50)))
assert sig(theta, 3) == "21.8"
B.mcq(T_UCM, "A frictionless banked curve of radius 50 m is designed for cars traveling at 14 m/s. At what angle above the horizontal is the road banked? ($g=9.8$ m/s^2)",
      ch("$21.8^\\circ$", "Without friction the horizontal component of the normal force is the centripetal force: $N\\sin\\theta=\\frac{mv^2}{r}$ and $N\\cos\\theta=mg$. Dividing, $\\tan\\theta=\\frac{v^2}{gr}=\\frac{196}{490}=0.40$, so $\\theta\\approx21.8^\\circ$.", theta),
      [ch("$23.6^\\circ$", "This is $\\sin^{-1}(0.40)$. The ratio $\\frac{v^2}{gr}$ equals $\\tan\\theta$, not $\\sin\\theta$.", math.degrees(math.asin(0.4))),
       ch("$68.2^\\circ$", "This is $\\tan^{-1}(2.5)$, the reciprocal ratio. The ratio is $\\frac{v^2}{gr}=0.40$.", math.degrees(math.atan(2.5))),
       ch("$11.5^\\circ$", "This is $\\tan^{-1}(0.20)$, half of the correct ratio.", math.degrees(math.atan(0.2)))],
      "Divide the two component equations for the normal force to eliminate $N$ and $m$: $\\tan\\theta=\\frac{v^2}{gr}$.")

# 8. coin on a turntable
mu, r = 0.30, 0.15
w = math.sqrt(mu * g / r)
assert sig(w, 2) == "4.4"
B.mcq(T_UCM, "A coin sits 0.15 m from the center of a horizontal turntable. The coefficient of static friction between the coin and the turntable is 0.30. The turntable's angular speed is slowly increased. At what angular speed does the coin begin to slide? ($g=9.8$ m/s^2)",
      ch("4.4 rad/s", "Friction supplies the centripetal force: $\\mu mg=m\\omega^2r$, so $\\omega=\\sqrt{\\frac{\\mu g}{r}}=\\sqrt{\\frac{(0.30)(9.8)}{0.15}}\\approx4.4$ rad/s.", w),
      [ch("20 rad/s", "This is $\\frac{\\mu g}{r}=19.6$, which is $\\omega^2$. Take the square root.", mu * g / r),
       ch("2.2 rad/s", "This is half the correct value, as if $\\omega=\\frac12\\sqrt{\\frac{\\mu g}{r}}$.", w / 2),
       ch("8.9 rad/s", "This is twice the correct value.", 2 * w)],
      "The centripetal force $m\\omega^2r$ cannot exceed the maximum static friction $\\mu mg$.")

# 9. satellites with different masses
B.mcq(T_ORB, "Satellite A has mass $m$ and satellite B has mass $4m$. They orbit the same planet in circular orbits of the same radius. Which statement is correct?",
      ch("They have the same orbital speed, and the gravitational force on B is 4 times the force on A", "$v=\\sqrt{\\frac{GM}{r}}$ does not depend on the satellite's mass. The gravitational force $\\frac{GMm}{r^2}$ is proportional to the satellite's mass, so it is 4 times larger on B.", None),
      [ch("B moves 4 times faster than A", "The orbital speed does not depend on the satellite's mass; the heavier satellite needs a proportionally larger force and has proportionally more inertia.", None),
       ch("B moves 2 times faster than A", "The speed is independent of the satellite's mass, so the speeds are equal.", None),
       ch("They have the same orbital speed, and the gravitational force on each is the same", "The gravitational force on a satellite is proportional to its own mass, so the force on B is larger even though the speeds are equal.", None)],
      "The orbital speed is $\\sqrt{GM/r}$, independent of the orbiting mass; the force is $GMm/r^2$.")

# 10. angular momentum in an elliptical orbit
va = 5.0
vp = va * 3
assert vp == 15
B.mcq(T_ORB, "A comet orbits the Sun in an ellipse. Its distance from the Sun at aphelion (farthest point) is 3 times its distance at perihelion (closest point). At aphelion the comet's speed is 5.0 km/s. What is its speed at perihelion?",
      ch("15 km/s", "Gravity exerts no torque about the Sun, so angular momentum $mvr$ is conserved at those two points where the velocity is perpendicular to the radius: $v_pr_p=v_ar_a$. With $r_a=3r_p$, $v_p=3v_a=15$ km/s.", vp),
      [ch("1.7 km/s", "This divides by 3. The comet moves faster where it is closer to the Sun.", va / 3),
       ch("45 km/s", "This multiplies by 9, as if the speed scaled as the square of the distance ratio. Angular momentum conservation gives an inverse *linear* relation.", va * 9),
       ch("8.7 km/s", "This multiplies by $\\sqrt3$, which would come from an energy argument ignoring the changing potential energy. Use conservation of angular momentum.", va * math.sqrt(3))],
      "At aphelion and perihelion the velocity is perpendicular to the radius, so $L=mvr$ is the same at both.")

# 11. gravity at orbital altitude
ratio = (6400 / 6800) ** 2
red = (1 - ratio) * 100
assert sig(red, 2) == "11"
B.mcq(T_GF, "The International Space Station orbits about 400 km above Earth's surface, where Earth's radius is about 6400 km. By approximately what percentage is the gravitational acceleration there smaller than at Earth's surface?",
      ch("About 11%", "The distance from Earth's center is $6800$ km, so $g\\propto\\frac{1}{r^2}$ gives $\\left(\\frac{6400}{6800}\\right)^2\\approx0.886$ of the surface value. That is about 11% smaller.", red),
      [ch("About 6%", "This is $\\frac{400}{6400}$, the fractional increase in distance. Gravity depends on the square of the distance from the center and the distance is measured from the center (6800 km), not from the surface.", 6.25),
       ch("0%: the astronauts are weightless, so there is no gravity", "Astronauts feel weightless because they and the station are in free fall, not because gravity is absent. The gravitational acceleration is still about 89% of the surface value.", 0),
       ch("About 94%", "This reverses the ratio. Gravity at the station is about 89% of the surface value, so it is 11% smaller, not 94%.", 94)],
      "Use $g\\propto\\frac{1}{r^2}$ with $r$ measured from Earth's center.")

# 12. point of zero net gravitational force
ratio = math.sqrt(81)
frac = ratio / (1 + ratio)
assert abs(frac - 0.9) < 1e-9
B.mcq(T_GF, "The Earth's mass is about 81 times the Moon's mass. Along the line joining their centers, at what fraction of the Earth-Moon distance $d$, measured from Earth, is the net gravitational force on a spacecraft zero?",
      ch("$0.90\\,d$", "Set the two forces equal: $\\frac{GM_E}{x^2}=\\frac{GM_M}{(d-x)^2}$, so $\\frac{x}{d-x}=\\sqrt{81}=9$ and $x=0.90d$.", 0.90),
      [ch("$0.50\\,d$", "The midpoint would be right only if the two masses were equal.", 0.50),
       ch("$0.99\\,d$", "This uses the mass ratio 81 directly, $\\frac{81}{82}$. The distances are in the ratio of the *square roots* of the masses, since the force falls as $\\frac{1}{r^2}$.", 81 / 82),
       ch("$0.10\\,d$", "This is the distance of that point from the *Moon*, as a fraction of $d$. Measured from Earth, the point is $0.90d$ away.", 0.10)],
      "Equate the two gravitational forces; the distances are in the ratio $\\sqrt{M_E/M_M}$.")

# 13. normal force at the top of a hill
mcar, vh, rh = 1000.0, 10.0, 40.0
Nh = mcar * (g - vh**2 / rh)
assert round(Nh, 6) == 7300
B.mcq(T_UCM, "A 1000 kg car crosses the top of a circular hill of radius 40 m at a speed of 10 m/s. What is the magnitude of the normal force the road exerts on the car at the top? ($g=9.8$ m/s^2)",
      ch("7300 N", "At the top the center of the circle is below the car: $mg-N=\\frac{mv^2}{r}$, so $N=m\\left(g-\\frac{v^2}{r}\\right)=1000(9.8-2.5)=7300$ N.", Nh),
      [ch("12300 N", "This adds the centripetal term. That would be the normal force at the *bottom* of a dip of the same radius.", mcar * (g + vh**2 / rh)),
       ch("9800 N", "This is the weight $mg$, the normal force only if the car were not moving along a curve.", mcar * g),
       ch("2500 N", "This is $\\frac{mv^2}{r}$ alone, the net force toward the center, not the normal force.", mcar * vh**2 / rh)],
      "Take the direction toward the center of the circle (downward at the top) as positive and apply Newton's second law.")

# 14. stopper on a string
m, r, Tp = 0.20, 0.50, 0.80
F = 4 * math.pi**2 * m * r / Tp**2
assert sig(F, 2) == "6.2"
B.mcq(T_UCM, "A 0.20 kg rubber stopper is whirled in a horizontal circle of radius 0.50 m with a period of 0.80 s. Ignoring the stopper's weight, what is the tension in the string?",
      ch("6.2 N", "$F=\\frac{4\\pi^2mr}{T^2}=\\frac{4\\pi^2(0.20)(0.50)}{(0.80)^2}\\approx6.2$ N.", F),
      [ch("4.9 N", "This uses $T$ instead of $T^2$ in the denominator: $\\frac{4\\pi^2mr}{T}$.", 4 * math.pi**2 * m * r / Tp),
       ch("12 N", "This uses the diameter, 1.0 m, as the radius.", 4 * math.pi**2 * m * 1.0 / Tp**2),
       ch("2.5 N", "This multiplies by $T^2$ instead of dividing, $4\\pi^2mrT^2$.", 4 * math.pi**2 * m * r * Tp**2)],
      "The speed is $v=\\frac{2\\pi r}{T}$, and the tension supplies the centripetal force $\\frac{mv^2}{r}$.")

# 15. gravitational force scaling
B.mcq(T_GF, "Two uniform spheres of mass $M$ each, with their centers a distance $d$ apart, attract each other with a gravitational force of magnitude $F$. If the masses are changed to $2M$ and $3M$ and the distance between their centers is changed to $2d$, what is the new magnitude of the force?",
      ch("$1.5F$", "$F\\propto\\frac{m_1m_2}{d^2}$. The numerator is multiplied by $2\\times3=6$ and the denominator by $2^2=4$: $\\frac64F=1.5F$.", 1.5),
      [ch("$6F$", "This accounts for the masses but not the change in distance.", 6.0),
       ch("$3F$", "This divides by 2 for the distance. The force falls as the *square* of the distance, so divide by 4.", 3.0),
       ch("$2.5F$", "This adds the mass factors ($2+3$) and treats the combined factor as $2.5$. The force depends on the *product* of the masses.", 2.5)],
      "Gravitational force is proportional to the product of the masses and inversely proportional to the square of the distance.")

# ------------------------------------------------------------------ FRQs
m, r, vb = 0.40, 0.80, 6.0
Tb = m * (g + vb**2 / r)
vt2 = vb**2 - 4 * g * r
need = g * r
vmin_b = math.sqrt(5 * g * r)
assert sig(Tb, 3) == "21.9" and round(vt2, 6) == 4.64 and round(need, 6) == 7.84 and sig(vmin_b, 3) == "6.26"
B.frq(T_UCM,
      "A 0.40 kg ball is attached to a light string of length 0.80 m and swung in a vertical circle. At the lowest point of the circle the ball's speed is 6.0 m/s. Use $g=9.8$ m/s^2.\n\n**(a)** Calculate the tension in the string when the ball is at the lowest point.\n\n**(b)** Using conservation of energy, calculate the value of $v^2$ the ball would have at the highest point of the circle.\n\n**(c)** What is the smallest value of $v^2$ that the ball can have at the highest point while the string stays taut? Use your answers to show whether the ball can complete the circle with a speed of 6.0 m/s at the bottom.\n\n**(d)** Find the minimum speed at the bottom that allows the ball to complete the circle.",
      [(1, "(a) Uses $T-mg=\\frac{mv^2}{r}$ and finds about 21.9 N"),
       (1, "(b) Sets up energy conservation $\\frac12mv_b^2=\\frac12mv_t^2+mg(2r)$"),
       (1, "(b) Finds $v_t^2=36-4gr=4.64$ m^2/s^2"),
       (1, "(c) States that at the minimum the tension is zero at the top, $mg=\\frac{mv^2}{r}$, so $v^2_{min}=gr=7.84$ m^2/s^2"),
       (1, "(c) Compares $4.64<7.84$ and concludes the ball cannot complete the circle (the string goes slack)"),
       (1, "(d) Combines the two conditions to get $v_b^2=5gr$ and $v_b\\approx6.26$ m/s")],
      "(a) At the bottom the net force toward the center (up) is $T-mg=\\frac{mv^2}{r}$, so $T=0.40\\left(9.8+\\frac{36}{0.80}\\right)=0.40(54.8)\\approx21.9$ N.\n(b) Energy conservation between the bottom and the top, a height $2r=1.6$ m higher: $\\frac12mv_b^2=\\frac12mv_t^2+mg(2r)$, so $v_t^2=v_b^2-4gr=36-31.36=4.64$ m^2/s^2.\n(c) At the top the string tension and weight both point toward the center: $T+mg=\\frac{mv^2}{r}$. The string just stays taut when $T=0$, which requires $v^2=gr=(9.8)(0.80)=7.84$ m^2/s^2. The ball would have only $4.64$ m^2/s^2, which is less than 7.84, so the string would go slack and the ball cannot complete the circle.\n(d) Requiring $v_t^2\\ge gr$ and $v_t^2=v_b^2-4gr$ gives $v_b^2\\ge5gr=39.2$ m^2/s^2, so $v_b\\ge6.26$ m/s.")

M_E = 6.0e24
r0 = 7.0e6
v0 = math.sqrt(G * M_E / r0)
T0 = 2 * math.pi * r0 / v0
v2 = v0 / math.sqrt(2)
T2 = T0 * 2 * math.sqrt(2)
assert sig(v0, 2) == "7600" and sig(T0, 2) == "5800"
B.frq(T_ORB,
      "A satellite of mass $m$ orbits Earth (mass $M=6.0\\times10^{24}$ kg) in a circular orbit of radius $7.0\\times10^6$ m. Use $G=6.67\\times10^{-11}$ N$\\cdot$m^2/kg^2.\n\n**(a)** Starting from Newton's law of gravitation and the expression for centripetal force, derive an expression for the satellite's orbital speed $v$ in terms of $G$, $M$ and the orbital radius $r$.\n\n**(b)** Calculate the satellite's orbital speed.\n\n**(c)** Calculate the satellite's period.\n\n**(d)** The satellite is moved to a circular orbit of radius $1.4\\times10^7$ m (twice the original radius). Determine by what factor the orbital speed and the period change.",
      [(1, "(a) Sets $\\frac{GMm}{r^2}=\\frac{mv^2}{r}$ and shows the mass $m$ cancels"),
       (1, "(a) Solves to get $v=\\sqrt{\\frac{GM}{r}}$"),
       (1, "(b) Substitutes and calculates $v\\approx7.6\\times10^3$ m/s"),
       (1, "(c) Uses $T=\\frac{2\\pi r}{v}$ to get about $5.8\\times10^3$ s"),
       (1, "(d) States the speed is multiplied by $\\frac1{\\sqrt2}\\approx0.71$"),
       (1, "(d) States the period is multiplied by $2\\sqrt2\\approx2.8$ (from $T\\propto r^{3/2}$)")],
      "(a) The gravitational force provides the centripetal force: $\\frac{GMm}{r^2}=\\frac{mv^2}{r}$. The mass $m$ cancels, so $v^2=\\frac{GM}{r}$ and $v=\\sqrt{\\frac{GM}{r}}$.\n(b) $v=\\sqrt{\\frac{(6.67\\times10^{-11})(6.0\\times10^{24})}{7.0\\times10^6}}=\\sqrt{5.7\\times10^7}\\approx7.6\\times10^3$ m/s.\n(c) $T=\\frac{2\\pi r}{v}=\\frac{2\\pi(7.0\\times10^6)}{7.56\\times10^3}\\approx5.8\\times10^3$ s (about 97 minutes).\n(d) $v\\propto\\frac{1}{\\sqrt r}$, so doubling $r$ multiplies $v$ by $\\frac{1}{\\sqrt2}\\approx0.71$ (to about $5.3\\times10^3$ m/s). $T^2\\propto r^3$, so $T$ is multiplied by $2^{3/2}=2\\sqrt2\\approx2.8$ (to about $1.6\\times10^4$ s).")

B.save()
B.brief()
