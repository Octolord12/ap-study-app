import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from authoring import *

g = 9.8
RHO_W = 1000.0
ATM = 1.01e5
B = Bank("ap-physics-1", "ap-phys1", 8, "unit-8-fluids")
T_DP, T_PAS, T_BUO, T_DYN = ("density-and-pressure", "pascals-principle", "buoyancy", "fluid-dynamics")

# 1. absolute pressure at depth
P = ATM + RHO_W * g * 12
assert round(P, -4) == 220000
B.mcq(T_DP, "A diver is 12 m below the surface of a freshwater lake. The density of the water is 1000 kg/m^3 and atmospheric pressure is $1.01\\times10^5$ Pa. What is the absolute pressure at the diver's depth? ($g=9.8$ m/s^2)",
      ch("$2.2\\times10^5$ Pa", "$P=P_0+\\rho gh=1.01\\times10^5+(1000)(9.8)(12)=1.01\\times10^5+1.18\\times10^5\\approx2.2\\times10^5$ Pa.", P),
      [ch("$1.2\\times10^5$ Pa", "This is the *gauge* pressure, $\\rho gh$ alone. The absolute pressure also includes the atmosphere pressing on the water's surface.", RHO_W * g * 12),
       ch("$1.0\\times10^5$ Pa", "This is just atmospheric pressure. The water adds $\\rho gh$.", ATM),
       ch("$1.1\\times10^6$ Pa", "This is off by a factor of 10: $\\rho gh=(1000)(9.8)(12)=1.2\\times10^5$ Pa, not $10^6$.", 1.1e6)],
      "Absolute pressure is atmospheric pressure plus the pressure due to the depth of the fluid, $\\rho gh$.")

# 2. hydraulic lift distance
d2 = 0.50 * 0.002 / 0.05
assert round(d2, 6) == 0.02
B.mcq(T_PAS, "In a hydraulic lift, the small piston has an area of $0.0020$ m^2 and the large piston has an area of $0.050$ m^2. The small piston is pushed down 0.50 m. How far does the large piston rise? (The fluid is incompressible.)",
      ch("0.020 m", "The fluid volume moved is the same on both sides: $A_1d_1=A_2d_2$, so $d_2=\\frac{(0.0020)(0.50)}{0.050}=0.020$ m. The force is multiplied by 25, and the distance is divided by 25.", d2),
      [ch("0.50 m", "The large piston cannot move as far as the small one: the volume of fluid displaced is equal, and its area is 25 times as large.", 0.50),
       ch("12.5 m", "This multiplies by the area ratio instead of dividing. A hydraulic lift trades distance for force.", 12.5),
       ch("0.0040 m", "This divides the distance by an area ratio of 125. The areas are in the ratio $\\frac{0.050}{0.0020}=25$.", 0.0040)],
      "An incompressible fluid transmits volume: the volume pushed down on one side equals the volume pushed up on the other, $A_1d_1=A_2d_2$.")

# 3. fraction submerged in a different fluid
frac = 600 / 800
assert frac == 0.75
B.mcq(T_BUO, "A uniform block of density 600 kg/m^3 floats in water (density 1000 kg/m^3). The same block is placed in oil of density 800 kg/m^3 and floats. What fraction of the block's volume is submerged in the oil?",
      ch("0.75", "A floating object displaces its own weight of fluid: $\\rho_{block}V=\\rho_{fluid}V_{sub}$, so $\\frac{V_{sub}}{V}=\\frac{\\rho_{block}}{\\rho_{fluid}}=\\frac{600}{800}=0.75$.", frac),
      [ch("0.60", "0.60 is the fraction submerged in *water*. Oil is less dense than water, so more of the block must be submerged to displace its weight.", 0.60),
       ch("0.80", "This is the density of the oil in g/cm^3, which is not the fraction submerged.", 0.80),
       ch("0.45", "This multiplies $0.60\\times0.75$. The submerged fraction is the ratio of the densities, $\\frac{\\rho_{block}}{\\rho_{oil}}$.", 0.45)],
      "For a floating object, the buoyant force equals the weight, so the submerged fraction is $\\frac{\\rho_{object}}{\\rho_{fluid}}$.")

# 4. density from apparent weight
Fb = 50 - 30
V = Fb / (RHO_W * g)
rho = (50 / g) / V
assert round(rho, 3) == 2500
B.mcq(T_BUO, "An object weighs 50 N in air and has an apparent weight of 30 N when completely submerged in water (density 1000 kg/m^3). What is the density of the object? ($g=9.8$ m/s^2)",
      ch("$2.5\\times10^3$ kg/m^3", "The buoyant force is $50-30=20$ N $=\\rho_wV g$, so $V=\\frac{20}{(1000)(9.8)}=2.04\\times10^{-3}$ m^3. The mass is $\\frac{50}{9.8}=5.1$ kg. Density $=\\frac{5.1}{2.04\\times10^{-3}}=2.5\\times10^3$ kg/m^3. (Equivalently, $\\rho=\\rho_w\\frac{W_{air}}{F_B}$.)", rho),
      [ch("$1.7\\times10^3$ kg/m^3", "This is $\\frac{50}{30}\\times1000$, using the apparent weight in place of the buoyant force.", 50 / 30 * 1000),
       ch("$1.0\\times10^3$ kg/m^3", "This is the density of the water, not of the object.", 1000.0),
       ch("$5.0\\times10^3$ kg/m^3", "This is $\\frac{50}{10}\\times1000$. The buoyant force is $20$ N, so the weight is 2.5 times the buoyant force.", 5000.0)],
      "The weight lost in the fluid equals the buoyant force, which equals the weight of the displaced water.")

# 5. continuity
v5 = 2.0 * (6.0 / 3.0) ** 2
assert v5 == 8.0
B.mcq(T_DYN, "Water flows steadily through a horizontal pipe. In a section with a diameter of 6.0 cm the water speed is 2.0 m/s. The pipe narrows to a diameter of 3.0 cm. What is the water speed in the narrow section?",
      ch("8.0 m/s", "Continuity: $A_1v_1=A_2v_2$. The area is proportional to the diameter squared: $A_2=\\frac14A_1$, so $v_2=4v_1=8.0$ m/s.", v5),
      [ch("4.0 m/s", "This uses the ratio of diameters (2), not areas. The cross-sectional area scales as the *square* of the diameter.", 4.0),
       ch("1.0 m/s", "The water must speed up in the narrow section to keep the same volume flow rate.", 1.0),
       ch("16 m/s", "This squares the area ratio again, $2^4$. The area ratio is $2^2=4$.", 16.0)],
      "The volume flow rate $A\\,v$ is the same in every section of an incompressible steady flow.")

# 6. Bernoulli pressure difference
dP = 0.5 * RHO_W * (8.0**2 - 2.0**2)
assert dP == 30000
B.mcq(T_DYN, "Water (density 1000 kg/m^3) flows through a horizontal pipe. In the wide section the speed is 2.0 m/s, and in the narrow section it is 8.0 m/s. By how much is the pressure in the wide section greater than in the narrow section?",
      ch("$3.0\\times10^4$ Pa", "Bernoulli's equation for a horizontal pipe: $P_1-P_2=\\frac12\\rho(v_2^2-v_1^2)=\\frac12(1000)(64-4)=3.0\\times10^4$ Pa.", dP),
      [ch("$1.8\\times10^4$ Pa", "This squares the difference of the speeds, $\\frac12\\rho(v_2-v_1)^2$. The equation uses the difference of the *squares*.", 0.5 * RHO_W * 36),
       ch("$6.0\\times10^4$ Pa", "This leaves out the factor $\\frac12$ in $\\frac12\\rho v^2$.", RHO_W * 60),
       ch("$3.2\\times10^4$ Pa", "This uses only the speed in the narrow section, $\\frac12\\rho v_2^2$, and ignores the kinetic-energy density in the wide section.", 0.5 * RHO_W * 64)],
      "Apply Bernoulli's equation between the two sections at the same height: $P_1+\\frac12\\rho v_1^2=P_2+\\frac12\\rho v_2^2$.")

# 7. Torricelli speed
v7 = math.sqrt(2 * g * 1.8)
assert sig(v7, 2) == "5.9"
B.mcq(T_DYN, "A large open tank of water has a small hole in its side, 1.8 m below the water surface. With what speed does the water leave the hole? ($g=9.8$ m/s^2; neglect viscosity and the change of the water level.)",
      ch("5.9 m/s", "Bernoulli's equation between the surface (speed $\\approx0$, pressure atmospheric) and the hole (pressure atmospheric) gives $\\frac12v^2=gh$, so $v=\\sqrt{2gh}=\\sqrt{2(9.8)(1.8)}\\approx5.9$ m/s.", v7),
      [ch("18 m/s", "This is $gh=17.6$, without the square root or the factor 2.", g * 1.8),
       ch("4.2 m/s", "This is $\\sqrt{gh}$, leaving out the factor 2 from $\\frac12v^2=gh$.", math.sqrt(g * 1.8)),
       ch("8.4 m/s", "This is $\\sqrt{4gh}$, doubling the correct square.", math.sqrt(4 * g * 1.8))],
      "Water leaving the hole has the same speed as an object falling freely through the depth $h$: $v=\\sqrt{2gh}$.")

# 8. iceberg
above = (1 - 920 / 1025) * 100
assert sig(above, 2) == "10"
B.mcq(T_BUO, "Ice has a density of 920 kg/m^3 and seawater has a density of 1025 kg/m^3. What percentage of the volume of a floating iceberg is above the surface of the sea?",
      ch("About 10%", "The submerged fraction is $\\frac{\\rho_{ice}}{\\rho_{sea}}=\\frac{920}{1025}\\approx0.90$. The fraction above the surface is $1-0.90\\approx0.10$, or about 10%.", above),
      [ch("About 90%", "This is the fraction that is *below* the surface.", 90.0),
       ch("About 8%", "This is $1-\\frac{920}{1000}$, which would be the exposed fraction in fresh water. Seawater is denser, so more of the iceberg floats above the surface.", 8.0),
       ch("About 20%", "A floating object displaces its weight in fluid, so the fractions follow from the density ratio, giving about 10%.", 20.0)],
      "The submerged fraction of a floating object is $\\frac{\\rho_{object}}{\\rho_{fluid}}$.")

# 9. buoyant force and pressure with depth
B.mcq(T_BUO, "A solid steel ball is completely submerged in a deep lake and lowered from a depth of 1 m to a depth of 5 m. Which statement correctly describes the change?",
      ch("The buoyant force on the ball stays the same, and the pressure on the ball increases", "The buoyant force equals the weight of the displaced water, $\\rho_wVg$, which is the same at any depth (water is nearly incompressible). The pressure $P_0+\\rho gh$ increases with depth.", None),
      [ch("The buoyant force on the ball increases, because the pressure increases", "Pressure increases on all sides of the ball. The *difference* between the pressure on the bottom and top, which gives the net upward force, stays the same.", None),
       ch("The buoyant force on the ball decreases, because the ball is farther from the surface", "The buoyant force does not depend on how far the object is from the surface, only on the volume of fluid displaced.", None),
       ch("The buoyant force and the pressure both stay the same", "The pressure at the ball's location increases with depth: $P=P_0+\\rho gh$.", None)],
      "The buoyant force depends on the displaced volume and the fluid density, not the depth. Pressure depends on depth.")

# 10. depth for a given absolute pressure
h10 = 2 * ATM / (RHO_W * g)
assert sig(h10, 2) == "21"
B.mcq(T_DP, "At what depth in a freshwater lake (density 1000 kg/m^3) is the absolute pressure equal to 3.0 atmospheres? (1 atm $=1.01\\times10^5$ Pa; $g=9.8$ m/s^2)",
      ch("21 m", "The pressure from the water must be $3.0-1.0=2.0$ atm $=2.02\\times10^5$ Pa. $h=\\frac{2.02\\times10^5}{(1000)(9.8)}\\approx21$ m.", h10),
      [ch("31 m", "This sets $\\rho gh=3.0$ atm, which ignores the 1.0 atm already present at the surface. The water adds the *additional* 2.0 atm.", 3 * ATM / (RHO_W * g)),
       ch("10 m", "This is the depth at which the absolute pressure reaches 2 atm (an extra 1 atm).", ATM / (RHO_W * g)),
       ch("41 m", "This is the depth for an absolute pressure of 5 atm, twice the extra pressure needed.", 4 * ATM / (RHO_W * g))],
      "Absolute pressure is $P_0+\\rho gh$. For 3.0 atm the water must supply 2.0 atm.")

# 11. ice with a steel ball
B.mcq(T_BUO, "A piece of ice with a small steel ball frozen inside floats in a glass of water that is filled exactly to the brim. After the ice melts completely, the steel ball sinks to the bottom of the glass. What happens to the water level?",
      ch("The water level falls (the glass is no longer full)", "While the ice floats, the ice-and-ball system displaces its total weight of water. After melting, the melted ice adds the same volume as the ice displaced, but the sunken steel ball displaces only its own volume, which is less than the volume of water that equals its weight. So less water is displaced and the level falls.", None),
      [ch("The water level stays at the brim", "A floating piece of ice alone leaves the level unchanged when it melts. The steel ball sinks, however, displacing less water than its weight would while it was supported by the ice.", None),
       ch("The water overflows", "The sunken ball displaces less water than it did while floating inside the ice (where it displaced its full weight of water), so the level cannot rise.", None),
       ch("The water level rises, because the ball adds to the volume", "While frozen in the ice, the ball is supported by the buoyant force, which equals the weight of the water displaced by the ball and ice together. Sinking lets the ball displace only its own (smaller) volume.", None)],
      "Compare the volume of water displaced before (the weight of the ice and ball divided by $\\rho_w g$) and after (the melt-water plus the ball's own volume).")

# 12. block held under water
rho_b, Vb = 400.0, 2.0e-3
Tn = (RHO_W - rho_b) * Vb * g
assert round(Tn, 3) == 11.76
B.mcq(T_BUO, "A wooden block of density 400 kg/m^3 and volume $2.0\\times10^{-3}$ m^3 is held completely under water (density 1000 kg/m^3) by a vertical string attached to the bottom of the container. What is the tension in the string? ($g=9.8$ m/s^2)",
      ch("12 N", "The buoyant force is $\\rho_wVg=(1000)(2.0\\times10^{-3})(9.8)=19.6$ N upward. The weight is $\\rho_bVg=7.84$ N downward. The string must pull down with $T=19.6-7.84\\approx12$ N.", Tn),
      [ch("20 N", "This is the buoyant force alone. The block's own weight offsets part of it.", 19.6),
       ch("7.8 N", "This is the block's weight alone. The string must balance the *difference* between the buoyant force and the weight.", 7.84),
       ch("27 N", "This adds the weight and the buoyant force. The weight acts opposite to the buoyant force, so they subtract.", 19.6 + 7.84)],
      "Balance the forces on the block: buoyant force up equals weight plus tension down.")

# 13. continuity with a split
v13 = 3.0 * 4.0 / (2 * 1.0)
assert v13 == 6.0
B.mcq(T_DYN, "Water flows at 3.0 m/s through a pipe with a cross-sectional area of 4.0 cm^2. The pipe splits into two identical pipes, each with a cross-sectional area of 1.0 cm^2. If the flow divides equally, what is the speed of the water in each of the smaller pipes?",
      ch("6.0 m/s", "Continuity: the flow rate before the split equals the sum afterward: $(4.0)(3.0)=2(1.0)v$, so $v=6.0$ m/s.", v13),
      [ch("3.0 m/s", "The total cross-sectional area of the smaller pipes (2.0 cm^2) is only half the area of the larger pipe, so the water must move faster.", 3.0),
       ch("12 m/s", "This ignores that the flow divides between two pipes; one pipe of 1.0 cm^2 would carry the full flow at $\\frac{(4.0)(3.0)}{1.0}=12$ m/s.", 12.0),
       ch("1.5 m/s", "This divides the speed by 2 for the split. Flow rate, not speed, divides between the pipes.", 1.5)],
      "The total volume flow rate $Av$ is conserved when the pipe branches: $A_1v_1=A_2v_2+A_3v_3$.")

# 14. Pascal's principle with radii
F14 = 60 * (10.0 / 2.0) ** 2
assert F14 == 1500
B.mcq(T_PAS, "A force of 60 N is applied to a small piston of radius 2.0 cm in a hydraulic system. The force is transmitted to a large piston of radius 10 cm. What force is exerted on the large piston?",
      ch("1500 N", "The pressure is the same on both pistons: $\\frac{F_1}{A_1}=\\frac{F_2}{A_2}$. The area ratio is $\\left(\\frac{10}{2.0}\\right)^2=25$, so $F_2=25(60)=1500$ N.", F14),
      [ch("300 N", "This multiplies by the ratio of the radii (5) rather than the ratio of the areas (25).", 300.0),
       ch("12 N", "This divides by the ratio of the radii. The large piston receives a larger force.", 12.0),
       ch("750 N", "This multiplies by 12.5, as if the ratio of areas were half the correct value.", 750.0)],
      "Equal pressure on the two pistons: $F\\propto A\\propto r^2$.")

# 15. lift on a wing
dP = 0.5 * 1.2 * (70.0**2 - 60.0**2)
F15 = dP * 16
assert round(dP, 6) == 780 and round(F15, 3) == 12480
B.mcq(T_DYN, "Air (density 1.2 kg/m^3) flows over the top of an airplane wing at 70 m/s and under it at 60 m/s. The wing has an area of 16 m^2. Use Bernoulli's equation to estimate the upward force on the wing due to this pressure difference.",
      ch("$1.2\\times10^4$ N", "$\\Delta P=\\frac12\\rho(v_{top}^2-v_{bottom}^2)=\\frac12(1.2)(4900-3600)=780$ Pa. The force is $\\Delta P\\cdot A=(780)(16)\\approx1.2\\times10^4$ N.", F15),
      [ch("$2.5\\times10^4$ N", "This leaves out the factor $\\frac12$ in $\\frac12\\rho v^2$.", 2 * F15),
       ch("$7.8\\times10^2$ N", "$780$ is the pressure difference in pascals. The force is the pressure difference times the wing area.", dP),
       ch("$6.2\\times10^3$ N", "This halves the correct answer, for example by applying the factor $\\frac12$ twice.", F15 / 2)],
      "The pressure difference is $\\frac12\\rho\\left(v_{top}^2-v_{bottom}^2\\right)$ (the faster air has lower pressure); multiply by the area.")

# ------------------------------------------------------------------ FRQs
rho_b = 1000 * 0.75
mass = 0.60
Vb = mass / rho_b
Wb = mass * g
Fb_full = RHO_W * Vb * g
extra = (Fb_full - Wb) / g
assert rho_b == 750 and round(Vb, 9) == 8.0e-4 and round(Wb, 6) == 5.88 and round(Fb_full, 6) == 7.84 and round(extra, 6) == 0.2
B.frq(T_BUO,
      "A uniform rectangular block of mass 0.60 kg floats in fresh water (density 1000 kg/m^3) with three-quarters of its volume submerged. Use $g=9.8$ m/s^2.\n\n**(a)** Calculate the density of the block.\n\n**(b)** Calculate the volume of the block and the buoyant force on it.\n\n**(c)** A small object is placed on top of the block so that the block is just completely submerged (with its top surface at the water level). Calculate the mass of the small object.\n\n**(d)** The original block (without the small object) is now placed in a liquid of density 1200 kg/m^3. Determine the fraction of its volume that is submerged.",
      [(1, "(a) Uses the floating condition $\\rho_{block}=\\frac34\\rho_w=750$ kg/m^3"),
       (1, "(b) Finds the volume $V=\\frac{m}{\\rho}=8.0\\times10^{-4}$ m^3"),
       (1, "(b) States the buoyant force equals the weight, $mg=5.9$ N"),
       (1, "(c) Finds the buoyant force when fully submerged, $\\rho_wVg=7.84$ N"),
       (1, "(c) Finds the extra weight $7.84-5.88=1.96$ N, so the mass is 0.20 kg"),
       (1, "(d) Finds the submerged fraction $\\frac{750}{1200}=0.625$")],
      "(a) A floating block displaces its own weight: $\\rho_{block}Vg=\\rho_w\\left(\\frac34V\\right)g$, so $\\rho_{block}=0.75(1000)=750$ kg/m^3.\n(b) $V=\\frac{m}{\\rho}=\\frac{0.60}{750}=8.0\\times10^{-4}$ m^3. The block floats, so $F_B=mg=(0.60)(9.8)=5.9$ N.\n(c) Fully submerged, the buoyant force is $\\rho_wVg=(1000)(8.0\\times10^{-4})(9.8)=7.84$ N. The weight of the block plus the object must equal this: $5.88+m_{obj}g=7.84$, so $m_{obj}g=1.96$ N and $m_{obj}=0.20$ kg.\n(d) The submerged fraction is $\\frac{\\rho_{block}}{\\rho_{liquid}}=\\frac{750}{1200}=0.625$.")

rho = 1000.0
P1 = 2.0e5
v1 = 1.5
v2 = v1 * (0.10 / 0.05) ** 2
P2 = P1 + 0.5 * rho * (v1**2 - v2**2)
Q = math.pi * 0.05**2 * v1
P2h = P2 - rho * g * 2.0
assert v2 == 6.0 and round(P2, -2) == 183100
assert sig(Q, 2) == "0.012" and round(P2h, -3) == 164000
B.frq(T_DYN,
      "Water (density 1000 kg/m^3) flows steadily through a horizontal pipe that narrows. In the wide section the diameter is 10 cm, the water speed is 1.5 m/s and the pressure is $2.0\\times10^5$ Pa. In the narrow section the diameter is 5.0 cm. Use $g=9.8$ m/s^2.\n\n**(a)** Calculate the water speed in the narrow section.\n\n**(b)** Calculate the pressure in the narrow section.\n\n**(c)** Calculate the volume of water that passes through the pipe each second.\n\n**(d)** The narrow section is raised so that it is 2.0 m higher than the wide section (the speeds are unchanged). Calculate the new pressure in the narrow section.",
      [(1, "(a) Uses continuity with the areas proportional to the diameters squared to get $v_2=6.0$ m/s"),
       (1, "(b) Writes Bernoulli's equation $P_1+\\frac12\\rho v_1^2=P_2+\\frac12\\rho v_2^2$"),
       (1, "(b) Evaluates $P_2\\approx1.8\\times10^5$ Pa"),
       (1, "(c) Computes the flow rate $Av=\\pi(0.050)^2(1.5)\\approx1.2\\times10^{-2}$ m^3/s"),
       (1, "(d) Includes the height term $\\rho gh=1.96\\times10^4$ Pa to get about $1.6\\times10^5$ Pa")],
      "(a) $A_1v_1=A_2v_2$ with $A\\propto d^2$: $v_2=v_1\\left(\\frac{10}{5.0}\\right)^2=(1.5)(4)=6.0$ m/s.\n(b) $P_1+\\frac12\\rho v_1^2=P_2+\\frac12\\rho v_2^2$, so $P_2=2.0\\times10^5+\\frac12(1000)(1.5^2-6.0^2)=2.0\\times10^5-1.7\\times10^4\\approx1.8\\times10^5$ Pa.\n(c) $Q=A_1v_1=\\pi(0.050)^2(1.5)\\approx1.2\\times10^{-2}$ m^3/s.\n(d) With the height difference, $P_1+\\frac12\\rho v_1^2=P_2+\\frac12\\rho v_2^2+\\rho gh$, so the pressure is reduced by $\\rho gh=(1000)(9.8)(2.0)=1.96\\times10^4$ Pa: $P_2\\approx1.83\\times10^5-0.20\\times10^5\\approx1.6\\times10^5$ Pa.")

B.save()
B.brief()
