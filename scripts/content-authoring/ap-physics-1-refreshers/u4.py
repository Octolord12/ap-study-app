from common import *

# --- checks for the worked examples -----------------------------------------------------------
# 4.0 kg crate pulled 5.0 m by 20 N at 60 degrees, friction 6.0 N, from rest
w_pull = 20 * 5.0 * cos(rad(60)); w_fric = -6.0 * 5.0
eq(w_pull, 50.0, 1); eq(w_fric, -30.0, 1); eq(w_pull + w_fric, 20.0, 1); eq(sqrt(2 * 20 / 4.0), 3.16, 2)

# potential energy: 0.50 kg lifted 1.0 m -> 3.0 m; spring k = 200 N/m
eq(0.50 * g * (3.0 - 1.0), 9.8, 1); eq(0.5 * 200 * 0.10 ** 2, 1.0, 1); eq(0.5 * 200 * 0.20 ** 2, 4.0, 1)

# 2.0 kg block released from rest 1.5 m up
U = 2.0 * g * 1.5; eq(U, 29.4, 1); eq(sqrt(2 * g * 1.5), 5.42, 2)
eq(U - 8.0, 21.4, 1); eq(sqrt(2 * (U - 8.0) / 2.0), 4.63, 2)

# power: 70 kg person up 3.0 m of stairs in 5.0 s; engine 500 N at 20 m/s
eq(70 * g * 3.0, 2058.0, 0); eq(70 * g * 3.0 / 5.0, 411.6, 1); eq(500 * 20, 10000)
# -----------------------------------------------------------------------------------------------

write(4, [
("work-and-the-work-energy-theorem", r"""
### The idea
Work is energy transferred by a force acting through a displacement. The net work done on an object equals the change in its kinetic energy.

### Key facts
- $W = Fd\cos\theta$, where $\theta$ is the angle between the force and the displacement. The unit is the joule: $1 \text{ J} = 1 \text{ N·m}$.
- Work is **positive** when the force has a component along the motion, **negative** when it opposes the motion (friction), and **zero** when perpendicular (the normal force on a level floor, the centripetal force in uniform circular motion).
- Kinetic energy: $K = \tfrac{1}{2}mv^2$. Doubling the speed quadruples it.
- **Work-energy theorem:** $W_{net} = \Delta K = \tfrac{1}{2}mv_f^2 - \tfrac{1}{2}mv_i^2$.
- On a graph of force against position, the area under the curve is the work.

### Watch out for
Using the whole force when it is at an angle. Only the component along the displacement does work. A weightlifter holding a bar still, or carrying it at constant height, does zero work on it in the physics sense.

### Worked example
A $4.0 \text{ kg}$ crate starts from rest and is pulled $5.0 \text{ m}$ by a $20 \text{ N}$ force at $60^\circ$ above the horizontal. Friction is $6.0 \text{ N}$.

Pull: $W = (20)(5.0)\cos 60^\circ = 50 \text{ J}$. Friction: $W = -(6.0)(5.0) = -30 \text{ J}$. Gravity and the normal force do no work.

$W_{net} = 20 \text{ J} = \tfrac{1}{2}(4.0)v^2$, so $v = \sqrt{10} = 3.16 \text{ m/s}$.
"""),
("potential-energy", r"""
### The idea
Potential energy is energy stored in a system because of the arrangement of its parts, like an object's height above the ground or the stretch of a spring. It can later turn into kinetic energy.

### Key facts
- Gravitational, near the surface: $\Delta U_g = mg\,\Delta y$. You choose where $U = 0$, and only **changes** matter.
- Elastic, for a spring: $U_s = \tfrac{1}{2}kx^2$, where $x$ is the stretch or compression from the spring's natural length.
- Spring force: $F_s = -kx$. The force is proportional to $x$, but the energy is proportional to $x^2$.
- Gravitational potential energy depends only on the height change, not on the path taken.
- These forces are **conservative**: the work they do can be fully recovered.

### Watch out for
Using the spring's total length as $x$. The formula needs the distance from the **natural** length, and stretching and compressing by the same amount store the same energy.

### Worked example
A $0.50 \text{ kg}$ ball is lifted from $1.0 \text{ m}$ to $3.0 \text{ m}$ above the floor:

$$\Delta U_g = (0.50)(9.8)(3.0 - 1.0) = 9.8 \text{ J}.$$

A spring with $k = 200 \text{ N/m}$ compressed by $0.10 \text{ m}$ stores $U_s = \tfrac{1}{2}(200)(0.10)^2 = 1.0 \text{ J}$.

Compressing it twice as far, to $0.20 \text{ m}$, stores $\tfrac{1}{2}(200)(0.20)^2 = 4.0 \text{ J}$: four times as much.
"""),
("conservation-of-energy", r"""
### The idea
Energy is never created or destroyed, only moved between forms and between objects. Tracking where it goes is often easier than tracking the forces.

### Key facts
- If only conservative forces (gravity, springs) do work, mechanical energy is conserved: $K_i + U_i = K_f + U_f$.
- Friction and other non-conservative forces turn mechanical energy into thermal energy. For kinetic friction the energy lost is $F_f d$.
- With a non-conservative force: $K_i + U_i + W_{other} = K_f + U_f$, where $W_{other}$ is the work by outside forces.
- Choose a system and say which energies it includes; energy leaving the system (as heat, say) is not "lost" from the universe.
- Without friction, the speed at the bottom of a drop depends only on the height lost: $v = \sqrt{2gh}$, whatever the shape of the track.

### Watch out for
Applying conservation of mechanical energy when friction acts, or forgetting that the starting height energy is turned into **both** speed and heat.

### Worked example
A $2.0 \text{ kg}$ block is released from rest at a height of $1.5 \text{ m}$ on a curved track. Its starting energy is $U = mgh = (2.0)(9.8)(1.5) = 29.4 \text{ J}$.

Frictionless: all of it becomes kinetic, so $v = \sqrt{2gh} = \sqrt{2(9.8)(1.5)} = 5.42 \text{ m/s}$.

If friction converts $8.0 \text{ J}$ into thermal energy: $K = 29.4 - 8.0 = 21.4 \text{ J}$, so $v = \sqrt{\dfrac{2(21.4)}{2.0}} = 4.63 \text{ m/s}$.
"""),
("power", r"""
### The idea
Power is how fast energy is transferred or work is done. Two machines can do the same work, but the more powerful one does it in less time.

### Key facts
- Average power: $P = \dfrac{W}{\Delta t} = \dfrac{\Delta E}{\Delta t}$. The unit is the watt: $1 \text{ W} = 1 \text{ J/s}$.
- When a force acts in the direction of motion, the instantaneous power is $P = Fv$. In general, $P = Fv\cos\theta$.
- Doubling the work in the same time doubles the power. Doing the same work in half the time also doubles it.
- A kilowatt-hour is a unit of **energy**: $1 \text{ kWh} = 3.6\times10^6 \text{ J}$.

### Watch out for
Mixing up energy and power. A watt is a rate. A light bulb rated at $60 \text{ W}$ uses $60 \text{ J}$ every second, and its energy use depends on how long it is on.

### Worked example
A $70 \text{ kg}$ person climbs stairs rising $3.0 \text{ m}$ in $5.0 \text{ s}$.

Work against gravity: $W = mgh = (70)(9.8)(3.0) = 2058 \text{ J}$.

$$P = \frac{2058}{5.0} = 411.6 \text{ W} \approx 410 \text{ W}.$$

Taking $10 \text{ s}$ instead would give half the power for the same work.

A car whose engine supplies a $500 \text{ N}$ force while it moves at a steady $20 \text{ m/s}$ delivers $P = Fv = 500(20) = 10{,}000 \text{ W}$.
"""),
])
