from common import *

# --- checks for the worked examples -----------------------------------------------------------
# 0.15 kg ball: +30 m/s in, -40 m/s out, 5.0 ms contact; stopping instead
dp = 0.15 * (-40 - 30); eq(dp, -10.5, 1); eq(dp / 0.005, -2100.0, 0)
eq(0.15 * 30, 4.5, 1); eq(4.5 / 0.005, 900.0, 0)

# skaters pushing apart: 40 kg moves at 3.0 m/s, 60 kg
v60 = -40 * 3.0 / 60; eq(v60, -2.0, 1)
eq(0.5 * 60 * v60 ** 2 + 0.5 * 40 * 3.0 ** 2, 300.0, 0)

# perfectly inelastic: 1000 kg at 20 m/s hits a stationary 1500 kg
vf = 1000 * 20 / 2500; eq(vf, 8.0, 1)
ki, kf = 0.5 * 1000 * 20 ** 2, 0.5 * 2500 * vf ** 2
eq(ki, 200000.0, 0); eq(kf, 80000.0, 0); eq(ki - kf, 120000.0, 0); eq((ki - kf) / ki, 0.6, 1)

# centre of mass
eq((2 * 0 + 6 * 4) / 8, 3.0, 1); eq((60 * 0 + 40 * 5.0) / 100, 2.0, 1)
# -----------------------------------------------------------------------------------------------

write(5, [
("momentum-and-impulse", r"""
### The idea
Momentum measures how hard it is to stop a moving object. A force applied for a time changes it, and that product of force and time is called impulse.

### Key facts
- Momentum: $\vec p = m\vec v$, a vector in $\text{kg·m/s}$, pointing along the velocity.
- Impulse: $\vec J = \vec F_{net}\,\Delta t = \Delta\vec p$. The unit is $\text{N·s}$, the same as $\text{kg·m/s}$.
- On a graph of force against time, the area under the curve is the impulse.
- For the same change in momentum, a longer contact time means a smaller average force. That is why airbags, crumple zones and bent knees work.
- A bouncing object changes momentum more than one that merely stops, because the velocity reverses.

### Watch out for
Ignoring direction. Pick a positive direction, then give a velocity in the opposite direction a negative sign. Subtracting without signs gives the wrong $\Delta p$.

### Worked example
A $0.15 \text{ kg}$ ball moving at $+30 \text{ m/s}$ is hit and leaves at $-40 \text{ m/s}$. The bat touches it for $5.0 \text{ ms}$.

$$\Delta p = 0.15\,(-40 - 30) = -10.5 \text{ kg·m/s}.$$

$$F_{avg} = \frac{\Delta p}{\Delta t} = \frac{-10.5}{0.0050} = -2100 \text{ N},$$

so the bat pushes with an average force of $2100 \text{ N}$, directed opposite to the ball's original motion.

If the ball had simply stopped, $|\Delta p| = 4.5 \text{ kg·m/s}$ and the force would be $900 \text{ N}$.
"""),
("conservation-of-momentum", r"""
### The idea
When objects interact only with each other, any momentum one gains the other loses. The total momentum of the system stays the same.

### Key facts
- If the net external force on a system is zero, total momentum is constant: $\vec p_{before} = \vec p_{after}$.
- The forces between the objects are equal and opposite for the same time, so the impulses cancel.
- It is a vector law, so apply it to each direction separately.
- It works for collisions and explosions alike, even when the forces are complicated, as long as outside forces are negligible during the event.
- Starting from rest, the total momentum after an explosion or push-off is still zero.

### Watch out for
Concluding that momentum is not conserved just because kinetic energy changes. Momentum is conserved in every isolated collision; kinetic energy is conserved only in elastic ones.

### Worked example
A $60 \text{ kg}$ skater and a $40 \text{ kg}$ skater stand at rest on frictionless ice and push apart. The $40 \text{ kg}$ skater moves off at $3.0 \text{ m/s}$ to the east.

$$0 = (60)v + (40)(3.0) \quad\Rightarrow\quad v = -2.0 \text{ m/s},$$

so the heavier skater moves at $2.0 \text{ m/s}$ west. The lighter one gets the greater speed, the speeds being inversely proportional to the masses.

The total kinetic energy afterwards is $\tfrac{1}{2}(60)(2.0)^2 + \tfrac{1}{2}(40)(3.0)^2 = 300 \text{ J}$, which came from the skaters' muscles. Energy was added, but momentum was conserved.
"""),
("collisions", r"""
### The idea
Collisions are sorted by what happens to kinetic energy. Momentum is conserved in all of them, so it always gives you one equation.

### Key facts
- **Elastic:** kinetic energy is conserved as well. The objects bounce apart and no energy goes to heat, sound or deformation.
- **Inelastic:** kinetic energy decreases.
- **Perfectly inelastic:** the objects stick together and move with a common velocity. This loses the most kinetic energy that momentum allows: $v_f = \dfrac{m_1v_1 + m_2v_2}{m_1 + m_2}$.
- In a head-on elastic collision between equal masses with one at rest, the moving object stops and the other leaves with its velocity.
- Kinetic energy that disappears has gone to thermal energy, sound and deformation.

### Watch out for
Using kinetic energy conservation in a collision where objects stick. "Stick" means perfectly inelastic, and there energy is certainly lost.

### Worked example
A $1000 \text{ kg}$ car moving at $20 \text{ m/s}$ hits a stationary $1500 \text{ kg}$ car, and they lock together.

$$v_f = \frac{(1000)(20) + 0}{1000 + 1500} = 8.0 \text{ m/s}.$$

Kinetic energy before: $\tfrac{1}{2}(1000)(20)^2 = 200{,}000 \text{ J}$. After: $\tfrac{1}{2}(2500)(8.0)^2 = 80{,}000 \text{ J}$.

So $120{,}000 \text{ J}$, which is $60\%$ of the original, became thermal energy, sound and crumpled metal. Momentum was the same before and after.
"""),
("center-of-mass", r"""
### The idea
The center of mass is the point where an object's mass is concentrated for the purpose of describing its translation. It moves as if all the outside forces acted on a point mass located there.

### Key facts
- For point masses along a line: $x_{cm} = \dfrac{m_1x_1 + m_2x_2 + \cdots}{m_1 + m_2 + \cdots}$, a mass-weighted average that sits nearer the heavier mass.
- For a uniform, symmetric object, it is at the geometric center. It can lie **outside** the object, as with a ring.
- Newton's Second Law for a system: $\vec F_{net,ext} = M\vec a_{cm}$.
- If the net external force is zero, the center of mass keeps a constant velocity (stays at rest if it started at rest), no matter what the parts do among themselves.
- Internal forces, like an explosion, cannot move the center of mass.

### Watch out for
Taking the midpoint of two objects as the center of mass. It is the midpoint only when the masses are equal.

### Worked example
A $2.0 \text{ kg}$ mass is at $x = 0$ and a $6.0 \text{ kg}$ mass at $x = 4.0 \text{ m}$:

$$x_{cm} = \frac{(2.0)(0) + (6.0)(4.0)}{2.0 + 6.0} = 3.0 \text{ m}.$$

Two skaters, $60 \text{ kg}$ and $40 \text{ kg}$, start at rest $5.0 \text{ m}$ apart on ice and pull on a rope between them. Measured from the heavier skater, the center of mass is $\dfrac{(60)(0) + (40)(5.0)}{100} = 2.0 \text{ m}$ away. It does not move, so they meet there, with the lighter skater having moved $3.0 \text{ m}$.
"""),
])
