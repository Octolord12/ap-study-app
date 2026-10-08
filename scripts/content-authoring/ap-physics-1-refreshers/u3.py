from common import *

# --- checks for the worked examples -----------------------------------------------------------
# 1200 kg car, flat curve r = 50 m, v = 20 m/s
ac = 20 ** 2 / 50; eq(ac, 8.0); eq(1200 * ac, 9600); eq(ac / g, 0.82, 2); eq(30 ** 2 / 50 * 1200 / (20 ** 2 / 50 * 1200), 2.25)

# gravity between 60 kg and 80 kg at 2.0 m, and a 500 kg satellite one Earth radius above the surface
sig(G * 60 * 80 / 2.0 ** 2, 8.0e-8, 2); eq(500 * g / 4, 1225.0)

# Earth satellite at 400 km altitude
r = R_EARTH + 4.0e5
sig(r, 6.77e6, 3)
eq(G * M_EARTH / r ** 2, 8.69, 2)
eq(G * M_EARTH / R_EARTH ** 2, 9.81, 2); eq(G * M_EARTH / r ** 2 / (G * M_EARTH / R_EARTH ** 2), 0.89, 2)
v = sqrt(G * M_EARTH / r); sig(v, 7670, 3)
T = 2 * pi * r / v; sig(T, 5550, 3); eq(T / 60, 92.4, 1)
# -----------------------------------------------------------------------------------------------

write(3, [
("uniform-circular-motion", r"""
### The idea
An object moving in a circle at constant speed is still accelerating, because its velocity direction keeps changing. That acceleration points toward the center, and so does the net force that causes it.

### Key facts
- Centripetal acceleration: $a_c = \dfrac{v^2}{r}$, directed toward the center.
- Net inward force: $\Sigma F_c = m\dfrac{v^2}{r}$. This is the **sum** of real forces (tension, friction, gravity, normal force), not a separate force.
- Speed around the circle: $v = \dfrac{2\pi r}{T}$, where $T$ is the period.
- The velocity is tangent to the circle. If the inward force vanishes, the object leaves along that tangent in a straight line.
- Doubling the speed needs four times the inward force; doubling the radius at the same speed needs half.

### Watch out for
Drawing a "centrifugal" force pushing outward. In a free-body diagram you only draw real forces. The feeling of being thrown outward is your inertia, tending to continue straight.

### Worked example
A $1200 \text{ kg}$ car rounds a flat curve of radius $50 \text{ m}$ at $20 \text{ m/s}$. Friction supplies the inward force.

$$
\begin{aligned}
a_c &= \frac{20^2}{50} = 8.0 \text{ m/s}^2 \\
F_f &= 1200(8.0) = 9600 \text{ N}
\end{aligned}
$$

The road must supply at least that friction, so $\mu_s mg \ge \dfrac{mv^2}{r}$ and $\mu_s \ge \dfrac{v^2}{rg} = \dfrac{8.0}{9.8} = 0.82$.

At $30 \text{ m/s}$ the needed friction is $2.25$ times as large, which is why speed matters so much on curves.
"""),
("gravitational-force", r"""
### The idea
Every pair of masses attracts each other. The force gets stronger with more mass and weaker quickly as they move apart.

### Key facts
- $F_g = \dfrac{G m_1 m_2}{r^2}$, with $G = 6.67 \times 10^{-11} \text{ N·m}^2/\text{kg}^2$.
- $r$ is the distance between the **centers** of the two masses.
- It is an inverse-square law: doubling the distance makes the force $\tfrac{1}{4}$ as large; tripling it makes it $\tfrac{1}{9}$.
- The two forces form a Third Law pair: both masses feel the same size force, in opposite directions.
- Near Earth's surface this reduces to $F_g = mg$, with $g = 9.8 \text{ m/s}^2$.
- Doubling either mass doubles the force.

### Watch out for
Measuring $r$ from the surface of a planet. For an object $h$ above the surface, $r = R + h$. A satellite one Earth radius up is at $r = 2R$, not $R$.

### Worked example
Two people of $60 \text{ kg}$ and $80 \text{ kg}$ stand $2.0 \text{ m}$ apart:

$$
\begin{aligned}
F_g &= \frac{(6.67\times10^{-11})(60)(80)}{(2.0)^2} \\
&= 8.0\times10^{-8} \text{ N}
\end{aligned}
$$

That is far too small to notice. The force is the same on each person.

A $500 \text{ kg}$ satellite one Earth radius above the surface is at $r = 2R$, so its weight is $\tfrac{1}{4}$ of the surface value: $\dfrac{500(9.8)}{4} = 1225 \text{ N}$.
"""),
("gravitational-fields-and-orbits", r"""
### The idea
A mass creates a gravitational field around it: at each point, a mass placed there feels a force per kilogram. An orbit is falling around a planet, with gravity providing the centripetal force.

### Key facts
- Field strength at distance $r$ from the center of a mass $M$: $g = \dfrac{GM}{r^2}$, in $\text{N/kg}$ (the same as $\text{m/s}^2$), pointing toward $M$.
- For a circular orbit, gravity is the inward force: $\dfrac{GMm}{r^2} = \dfrac{mv^2}{r}$, so $v = \sqrt{\dfrac{GM}{r}}$.
- Orbital speed depends on the planet's mass and the orbit radius, **not** on the satellite's mass.
- Bigger orbit means slower speed and longer period. The period is $T = \dfrac{2\pi r}{v}$.
- Astronauts feel "weightless" because they are in free fall along with the station. Gravity there is still strong.

### Watch out for
Saying there is no gravity in orbit. At low altitude gravity is only slightly weaker than on the ground. The astronauts feel weightless because nothing pushes back on them.

### Worked example
A satellite orbits at $400 \text{ km}$ above Earth, with $M = 5.97\times10^{24} \text{ kg}$ and $R = 6.37\times10^{6} \text{ m}$.

The orbit radius is $r = 6.37\times10^6 + 4.0\times10^5 = 6.77\times10^6 \text{ m}$.

Field there: $g = \dfrac{GM}{r^2} = 8.69 \text{ N/kg}$, about $89\%$ of the $9.81$ at the surface.

Speed: $v = \sqrt{\dfrac{GM}{r}} = 7670 \text{ m/s}$. Period: $T = \dfrac{2\pi r}{v} = 5550 \text{ s}$, about $92 \text{ minutes}$.
"""),
])
