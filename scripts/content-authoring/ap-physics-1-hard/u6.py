import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from authoring import *

g = 9.8
B = Bank("ap-physics-1", "ap-phys1", 6, "unit-6-simple-harmonic-motion")
T_RES, T_PER, T_EN = ("restoring-forces-and-shm", "period-of-springs-and-pendulums", "energy-in-shm")

# 1. period scaling for a mass on a spring
B.mcq(T_PER, "A block oscillates on a horizontal spring with period $T$. The block is replaced by one with four times the mass, and the amplitude is doubled. What is the new period?",
      ch("$2T$", "For a spring, $T=2\\pi\\sqrt{\\frac mk}$. Four times the mass multiplies the period by $\\sqrt4=2$. The period does not depend on the amplitude.", None),
      [ch("$4T$", "The period is proportional to the *square root* of the mass, not to the mass.", None),
       ch("$8T$", "This multiplies by 4 for the mass and by 2 for the amplitude. The period does not depend on the amplitude, and depends on $\\sqrt m$.", None),
       ch("$T$", "The amplitude does not change the period, but the mass does: $T\\propto\\sqrt m$.", None)],
      "$T=2\\pi\\sqrt{m/k}$ for a mass on a spring: independent of amplitude, proportional to $\\sqrt m$.")

# 2. pendulum length for a 2.0 s period
L = g * 2.0**2 / (4 * math.pi**2)
assert sig(L, 2) == "0.99"
B.mcq(T_PER, "What is the length of a simple pendulum that has a period of 2.0 s for small oscillations? ($g=9.8$ m/s^2)",
      ch("0.99 m", "$T=2\\pi\\sqrt{\\frac Lg}$, so $L=\\frac{gT^2}{4\\pi^2}=\\frac{(9.8)(4.0)}{39.5}\\approx0.99$ m.", L),
      [ch("4.0 m", "This is $\\frac{gT^2}{\\pi^2}$, leaving out a factor of 4 (the $2\\pi$ must be squared: $4\\pi^2$).", g * 4.0 / math.pi**2),
       ch("2.0 m", "This sets the length equal to the period, which mixes units. The length comes from $L=\\frac{gT^2}{4\\pi^2}$.", 2.0),
       ch("0.25 m", "This is $\\frac{T^2}{16}$, which does not follow from the period formula. Use $T=2\\pi\\sqrt{L/g}$.", 0.25)],
      "Solve $T=2\\pi\\sqrt{L/g}$ for $L$.")

# 3. speed at an intermediate position
k, m, A, x = 100.0, 0.50, 0.20, 0.10
w = math.sqrt(k / m)
v = w * math.sqrt(A**2 - x**2)
vmax = w * A
assert sig(v, 3) == "2.45" and sig(vmax, 3) == "2.83"
B.mcq(T_EN, "A 0.50 kg block on a horizontal spring (spring constant 100 N/m) oscillates with an amplitude of 0.20 m on a frictionless surface. What is the block's speed when it is 0.10 m from the equilibrium position?",
      ch("2.4 m/s", "Energy conservation: $\\frac12kA^2=\\frac12mv^2+\\frac12kx^2$, so $v=\\sqrt{\\frac km(A^2-x^2)}=\\sqrt{200(0.04-0.01)}=\\sqrt{6.0}\\approx2.4$ m/s.", v),
      [ch("1.4 m/s", "This halves the maximum speed, $\\frac{2.83}{2}$. The speed at half the amplitude is not half the maximum speed: it is $\\frac{\\sqrt3}{2}$ of it.", vmax / 2),
       ch("2.8 m/s", "This is the maximum speed, which occurs at the equilibrium position.", vmax),
       ch("3.2 m/s", "This uses $A^2+x^2$. The energy in the spring at position $x$ reduces the kinetic energy: $A^2-x^2$.", w * math.sqrt(A**2 + x**2))],
      "Total energy is constant: $\\frac12kA^2=\\frac12mv^2+\\frac12kx^2$.")

# 4. maximum acceleration from x(t)
amax = 0.15 * (8 * math.pi) ** 2
vmx = 0.15 * 8 * math.pi
assert sig(amax, 2) == "95" and sig(vmx, 2) == "3.8"
B.mcq(T_RES, "The position of an oscillating object is given by $x(t)=0.15\\cos(8\\pi t)$, where $x$ is in meters and $t$ is in seconds. What is the magnitude of the object's maximum acceleration?",
      ch("95 m/s^2", "The angular frequency is $\\omega=8\\pi$ rad/s and the amplitude is 0.15 m. The maximum acceleration is $A\\omega^2=(0.15)(8\\pi)^2\\approx95$ m/s^2.", amax),
      [ch("3.8 m/s^2", "This is $A\\omega\\approx3.8$ m/s, the maximum *speed*. The maximum acceleration has an extra factor of $\\omega$.", vmx),
       ch("2.4 m/s^2", "This uses $\\omega=f=4$ Hz in $A\\omega^2$. The angular frequency in the expression $\\cos(\\omega t)$ is $8\\pi$ rad/s.", 0.15 * 4**2),
       ch("9.6 m/s^2", "This uses $\\omega=8$ and drops the $\\pi$. The factor in the cosine is $8\\pi$.", 0.15 * 8**2)],
      "For $x=A\\cos(\\omega t)$, the maximum speed is $A\\omega$ and the maximum acceleration is $A\\omega^2$.")

# 5. vertical spring from static stretch
T5 = 2 * math.pi * math.sqrt(0.20 / g)
assert sig(T5, 2) == "0.9"
B.mcq(T_PER, "A mass hanging from a light vertical spring stretches the spring 0.20 m beyond its unstretched length when it hangs at rest. The mass is pulled down slightly and released, so that it oscillates vertically. What is the period of the oscillation? ($g=9.8$ m/s^2)",
      ch("0.90 s", "At equilibrium $kx_0=mg$, so $\\frac mk=\\frac{x_0}{g}$. Then $T=2\\pi\\sqrt{\\frac mk}=2\\pi\\sqrt{\\frac{0.20}{9.8}}\\approx0.90$ s.", T5),
      [ch("0.45 s", "This is half the correct value, as if $T=\\pi\\sqrt{x_0/g}$.", T5 / 2),
       ch("1.8 s", "This doubles the correct value.", 2 * T5),
       ch("0.20 s", "This is the stretch of the spring in meters, which is not a time.", 0.20)],
      "Use the static equilibrium $kx_0=mg$ to find $\\frac mk$ without knowing either quantity separately.")

# 6. springs in series
B.mcq(T_PER, "A block attached to a single spring oscillates with period $T$. The same block is instead attached to two identical springs, each identical to the original, connected end to end (in series). What is the new period of oscillation?",
      ch("$\\sqrt2\\,T$", "Two identical springs in series have an effective spring constant $\\frac k2$ (the combination stretches twice as far for the same force). Then $T'=2\\pi\\sqrt{\\frac{m}{k/2}}=\\sqrt2\\,T$.", None),
      [ch("$\\dfrac{T}{\\sqrt2}$", "This is the result for two springs in *parallel* (effective spring constant $2k$), not in series.", None),
       ch("$2T$", "This would require the effective spring constant to be $\\frac k4$. In series it is $\\frac k2$.", None),
       ch("$\\dfrac T2$", "This would require an effective spring constant of $4k$.", None)],
      "In series the extensions add, so the effective spring constant is smaller; $T\\propto\\frac{1}{\\sqrt{k}}$.")

# 7. kinetic energy equals potential energy
B.mcq(T_EN, "A block on a spring oscillates with amplitude $A$. At what positions is the kinetic energy of the block equal to the elastic potential energy stored in the spring?",
      ch("$x=\\pm\\dfrac{A}{\\sqrt2}\\approx\\pm0.71A$", "The total energy is $\\frac12kA^2$. When $KE=PE$, each is half the total: $\\frac12kx^2=\\frac12\\left(\\frac12kA^2\\right)$, so $x^2=\\frac{A^2}{2}$ and $x=\\pm\\frac{A}{\\sqrt2}$.", None),
      [ch("$x=\\pm\\dfrac A2$", "At half the amplitude the potential energy is $\\frac14$ of the total, since $PE\\propto x^2$, not $\\frac12$.", None),
       ch("$x=0$", "At the equilibrium position the potential energy is zero and all the energy is kinetic.", None),
       ch("$x=\\pm A$", "At the extremes the kinetic energy is zero and all the energy is potential.", None)],
      "Elastic potential energy is $\\frac12kx^2$, proportional to $x^2$. Set it equal to half of $\\frac12kA^2$.")

# 8. pendulum scaling
B.mcq(T_PER, "A simple pendulum oscillates through small angles with period $T$. The string is replaced by one four times as long, the bob is replaced by one twice as massive, and the amplitude is halved. What is the new period?",
      ch("$2T$", "$T=2\\pi\\sqrt{\\frac Lg}$ depends only on the length (and $g$). Quadrupling $L$ doubles $T$. The mass and the amplitude (for small angles) have no effect.", None),
      [ch("$T$", "The mass and amplitude do not affect the period, but the length does: $T\\propto\\sqrt L$.", None),
       ch("$4T$", "The period is proportional to the *square root* of the length.", None),
       ch("$2\\sqrt2\\,T$", "This includes a factor of $\\sqrt2$ for the doubled mass. The period of a pendulum does not depend on the mass.", None)],
      "A pendulum's period is $2\\pi\\sqrt{L/g}$: independent of mass and (for small angles) of amplitude.")

# 9. acceleration at a position
k, m, x = 80.0, 2.0, 0.10
a9 = k * x / m
assert a9 == 4.0
B.mcq(T_RES, "A 2.0 kg block on a horizontal frictionless surface is attached to a spring of spring constant 80 N/m. The block oscillates with an amplitude of 0.25 m. What is the magnitude of the block's acceleration when it is 0.10 m from the equilibrium position?",
      ch("4.0 m/s^2", "The spring force at $x=0.10$ m is $kx=(80)(0.10)=8.0$ N. The acceleration is $\\frac{F}{m}=\\frac{8.0}{2.0}=4.0$ m/s^2, toward the equilibrium position.", a9),
      [ch("10 m/s^2", "This is the acceleration at the maximum displacement ($\\frac{kA}{m}=\\frac{20}{2}$). At $x=0.10$ m the force is smaller.", 10.0),
       ch("8.0 m/s^2", "This is the *force* in newtons. Divide by the mass to get the acceleration.", 8.0),
       ch("2.0 m/s^2", "This divides the force by 4: the mass is 2.0 kg, and the force is 8.0 N.", 2.0)],
      "Hooke's law gives the force at that position, and Newton's second law gives the acceleration.")

# 10. effect of doubling the amplitude
B.mcq(T_EN, "A block oscillates on a spring with amplitude $A$, maximum speed $v_{max}$ and total mechanical energy $E$. If the block is made to oscillate on the same spring with amplitude $2A$, what are the new maximum speed and total energy?",
      ch("$2v_{max}$ and $4E$", "$E=\\frac12kA^2$, so doubling $A$ quadruples $E$. The maximum speed is $A\\omega$ with the same $\\omega$, so it doubles. (Equivalently $\\frac12mv_{max}^2=4E$ gives $v_{max}\\to2v_{max}$.)", None),
      [ch("$2v_{max}$ and $2E$", "The energy is proportional to $A^2$, not $A$.", None),
       ch("$4v_{max}$ and $4E$", "The maximum speed is proportional to $A$ (with fixed $\\omega$). Kinetic energy is proportional to $v^2$, so the energy quadruples when the speed doubles.", None),
       ch("$v_{max}$ and $4E$", "The maximum speed grows with the amplitude, $v_{max}=A\\omega$, because the block must cover a larger distance in the same period.", None)],
      "Energy scales with $A^2$; the maximum speed scales with $A$ because the period is fixed.")

# 11. same spring on the Moon
B.mcq(T_PER, "A mass hangs from a vertical spring and oscillates up and down with period $T$ on Earth. The same mass and spring are taken to the Moon, where the gravitational acceleration is about one-sixth as large, and set oscillating vertically. What is the period on the Moon?",
      ch("$T$ (unchanged)", "The period of a mass on a spring is $2\\pi\\sqrt{\\frac mk}$ and does not depend on $g$. Gravity shifts the equilibrium position but not the restoring-force-per-displacement.", None),
      [ch("$\\sqrt6\\,T$", "This is the pendulum result, $T\\propto\\frac1{\\sqrt g}$. The period of a mass on a spring does not depend on $g$.", None),
       ch("$\\dfrac{T}{\\sqrt6}$", "This inverts the pendulum result. In any case, the period of a spring oscillator does not depend on $g$.", None),
       ch("$6T$", "Nothing in the formula $T=2\\pi\\sqrt{m/k}$ involves gravity.", None)],
      "For a vertical spring, gravity only shifts the equilibrium position. The net restoring force is still $-kx$ measured from that position.")

# 12. fraction of energy that is kinetic
B.mcq(T_EN, "A block oscillates on a horizontal spring with amplitude $A$. When the block is at position $x=\\frac A2$, what fraction of the total mechanical energy is kinetic energy?",
      ch("$\\dfrac34$", "The elastic potential energy is $\\frac12kx^2=\\frac12k\\frac{A^2}{4}=\\frac14$ of the total $\\frac12kA^2$. The remaining $\\frac34$ is kinetic.", 0.75),
      [ch("$\\dfrac14$", "$\\frac14$ is the fraction that is *potential* energy at $x=\\frac A2$.", 0.25),
       ch("$\\dfrac12$", "The energy is shared equally at $x=\\frac{A}{\\sqrt2}$, not at $\\frac A2$.", 0.5),
       ch("$\\dfrac18$", "This cubes the ratio $\\left(\\frac12\\right)^3$. Potential energy varies as $x^2$.", 0.125)],
      "Use $PE\\propto x^2$: at half the amplitude the spring holds one quarter of the total energy.")

# 13. time between positions
B.mcq(T_RES, "A block oscillates on a spring with period $T$ and amplitude $A$. At $t=0$ it is at $x=A$ and at rest. How long does it take to first reach $x=\\frac A2$?",
      ch("$\\dfrac T6$", "With $x=A\\cos\\left(\\frac{2\\pi t}{T}\\right)$, setting $x=\\frac A2$ gives $\\frac{2\\pi t}{T}=\\frac\\pi3$, so $t=\\frac T6$. (The block then needs only another $\\frac T{12}$ to reach $x=0$, because it moves fastest near the center.)", None),
      [ch("$\\dfrac T4$", "The block takes $\\frac T4$ to travel the whole way from $x=A$ to $x=0$, which is twice the distance.", None),
       ch("$\\dfrac T8$", "This assumes constant speed, which is false: the block moves slower near the ends, so it takes longer than $\\frac T8$ to cover the first half.", None),
       ch("$\\dfrac T{12}$", "$\\frac{T}{12}$ is the time to travel from $x=\\frac A2$ to $x=0$. The first half of the way takes longer because the speed is lower there.", None)],
      "Write $x=A\\cos(\\omega t)$ and solve $\\cos(\\omega t)=\\frac12$.")

# 14. pendulum clock
B.mcq(T_PER, "A pendulum clock keeps correct time at a location where $g=9.80$ m/s^2. It is moved to a location where $g$ is 1.0% smaller. Which statement is correct?",
      ch("The clock runs slow, because its period is about 0.5% longer", "$T=2\\pi\\sqrt{\\frac Lg}\\propto g^{-1/2}$, so a 1.0% decrease in $g$ increases $T$ by about 0.5%. Each tick takes longer, so the clock runs slow.", None),
      [ch("The clock runs fast, because its period is about 0.5% shorter", "A smaller $g$ means a weaker restoring force, so the pendulum swings more slowly and the period gets longer.", None),
       ch("The clock runs slow, because its period is about 1.0% longer", "The period is proportional to $g^{-1/2}$, so a 1.0% change in $g$ gives about half that change in the period.", None),
       ch("The clock keeps correct time, because the period of a pendulum does not depend on $g$", "$T=2\\pi\\sqrt{L/g}$ does depend on $g$.", None)],
      "Small fractional changes: if $T\\propto g^{-1/2}$, then $\\frac{\\Delta T}{T}\\approx-\\frac12\\frac{\\Delta g}{g}$.")

# 15. clay dropped onto an oscillating block at equilibrium
k, m, A = 100.0, 1.0, 0.10
E = 0.5 * k * A**2
v0 = math.sqrt(2 * E / m)
v1 = v0 * m / (m + 1.0)
A2 = math.sqrt(2 * (0.5 * (m + 1.0) * v1**2) / k)
assert round(v0, 6) == 1.0 and round(v1, 6) == 0.5 and sig(A2, 2) == "0.071"
B.mcq(T_EN, "A 1.0 kg block oscillates on a horizontal frictionless surface attached to a spring of constant 100 N/m, with amplitude 0.10 m. At the instant the block passes through the equilibrium position, a 1.0 kg lump of clay is dropped vertically onto it and sticks. What is the new amplitude of the oscillation?",
      ch("0.071 m", "Just before the clay lands, $v=A\\sqrt{\\frac km}=1.0$ m/s. The horizontal momentum is conserved while the clay sticks: $v'=\\frac{(1.0)(1.0)}{2.0}=0.50$ m/s. At equilibrium all the energy is kinetic: $\\frac12(2.0)(0.50)^2=0.25$ J $=\\frac12kA'^2$, so $A'=\\sqrt{\\frac{2(0.25)}{100}}\\approx0.071$ m.", A2),
      [ch("0.050 m", "This halves the amplitude. The speed halves, but the mass doubles, so the energy falls to half and the amplitude falls by a factor of $\\sqrt2$.", 0.050),
       ch("0.10 m", "The amplitude changes: the clay slows the block (momentum conservation) and reduces its kinetic energy at equilibrium.", 0.10),
       ch("0.035 m", "This divides by 2 twice. The amplitude falls to $\\frac{0.10}{\\sqrt2}$, not $\\frac{0.10}{2\\sqrt2}$.", 0.035)],
      "Use momentum conservation for the (perfectly inelastic) sticking, then energy conservation to find the new amplitude.")

# ------------------------------------------------------------------ FRQs
m, k, A, x = 0.40, 160.0, 0.15, 0.09
T = 2 * math.pi * math.sqrt(m / k)
vmax = A * math.sqrt(k / m)
KE = 0.5 * k * (A**2 - x**2)
v = math.sqrt(2 * KE / m)
assert sig(T, 3) == "0.314" and round(vmax, 6) == 3.0 and round(KE, 6) == 1.152 and round(v, 6) == 2.4
E_old = 0.5 * k * A**2
E_new = 4 * E_old
B.frq(T_EN,
      "A 0.40 kg block is attached to a horizontal spring of spring constant 160 N/m. The block oscillates on a frictionless surface with an amplitude of 0.15 m.\n\n**(a)** Calculate the period of the oscillation.\n\n**(b)** Calculate the maximum speed of the block.\n\n**(c)** Calculate the kinetic energy of the block, and its speed, when it is 0.09 m from the equilibrium position.\n\n**(d)** The block is now made to oscillate with an amplitude of 0.30 m. State how the period changes, and calculate the new total mechanical energy.",
      [(1, "(a) Uses $T=2\\pi\\sqrt{\\frac mk}\\approx0.31$ s"),
       (1, "(b) Uses energy conservation or $v_{max}=A\\sqrt{\\frac km}=3.0$ m/s"),
       (1, "(c) Finds the kinetic energy $\\frac12k(A^2-x^2)=1.15$ J"),
       (1, "(c) Finds the speed $\\sqrt{\\frac{2KE}{m}}=2.4$ m/s"),
       (1, "(d) States the period does not change, and finds the new energy $\\frac12k(0.30)^2=7.2$ J (four times the original 1.8 J)")],
      "(a) $T=2\\pi\\sqrt{\\frac{m}{k}}=2\\pi\\sqrt{\\frac{0.40}{160}}=2\\pi(0.050)\\approx0.31$ s.\n(b) $\\frac12kA^2=\\frac12mv_{max}^2$, so $v_{max}=A\\sqrt{\\frac km}=(0.15)(20)=3.0$ m/s.\n(c) $KE=E-PE=\\frac12k(A^2-x^2)=\\frac12(160)(0.0225-0.0081)=1.15$ J. Then $v=\\sqrt{\\frac{2(1.152)}{0.40}}=2.4$ m/s.\n(d) The period does not depend on the amplitude, so it is unchanged. The original energy is $\\frac12(160)(0.15)^2=1.8$ J. With twice the amplitude the energy is four times larger: $\\frac12(160)(0.30)^2=7.2$ J.")
assert round(E_new, 6) == 7.2

tbl = "| $L$ (m) | 0.25 | 0.50 | 1.00 | 2.00 |\n|---|---|---|---|---|\n| $T$ (s) | 1.00 | 1.42 | 2.01 | 2.84 |"
slope = (2.84**2 - 1.00**2) / (2.00 - 0.25)
gexp = 4 * math.pi**2 / slope
assert sig(slope, 3) == "4.04" and sig(gexp, 3) == "9.78"
B.frq(T_PER,
      "A student measures the period $T$ of a simple pendulum for several lengths $L$ and records the data in the table. The oscillations are small.\n\n" + tbl + "\n\n**(a)** Explain why a graph of $T^2$ versus $L$ is expected to be a straight line, and state what the slope represents.\n\n**(b)** Use the first and last data points to calculate the slope of the line of $T^2$ versus $L$, and use it to determine the experimental value of $g$.\n\n**(c)** The student repeats the experiment with a bob of twice the mass. Predict how the periods would change.\n\n**(d)** The student realizes that each length was measured from the pivot to the *top* of the bob, rather than to its center, so each recorded length is smaller than the true length by the same constant amount. Describe how this affects the graph of $T^2$ versus $L$ and the value of $g$ obtained from the slope.",
      [(1, "(a) From $T=2\\pi\\sqrt{\\frac Lg}$, $T^2=\\frac{4\\pi^2}{g}L$, which is linear in $L$"),
       (1, "(a) States the slope is $\\frac{4\\pi^2}{g}$"),
       (1, "(b) Computes $T^2$ values and the slope $\\approx4.0$ s^2/m"),
       (1, "(b) Calculates $g=\\frac{4\\pi^2}{\\text{slope}}\\approx9.8$ m/s^2"),
       (1, "(c) States the periods would not change, since the period does not depend on the mass"),
       (1, "(d) Explains the graph is shifted (nonzero intercept) but keeps the same slope, so $g$ is not affected")],
      "(a) $T=2\\pi\\sqrt{\\frac Lg}$ gives $T^2=\\frac{4\\pi^2}{g}L$, so $T^2$ is proportional to $L$ and the graph is a straight line through the origin. The slope is $\\frac{4\\pi^2}{g}$.\n(b) $T^2$ is $1.00$ s^2 at $L=0.25$ m and $8.07$ s^2 at $L=2.00$ m. Slope $=\\frac{8.07-1.00}{2.00-0.25}\\approx4.04$ s^2/m. $g=\\frac{4\\pi^2}{\\text{slope}}=\\frac{39.5}{4.04}\\approx9.8$ m/s^2.\n(c) The periods would not change: the period of a simple pendulum does not depend on the mass of the bob.\n(d) The true length is $L+c$ for a constant $c$, so $T^2=\\frac{4\\pi^2}{g}(L+c)$. The graph of $T^2$ versus the measured $L$ is still a straight line with the same slope $\\frac{4\\pi^2}{g}$, but it no longer passes through the origin (the intercept is $\\frac{4\\pi^2}{g}c$). Since $g$ comes from the slope, the value of $g$ is not affected.")

B.save()
B.brief()
