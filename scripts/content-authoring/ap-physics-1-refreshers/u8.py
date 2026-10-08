from common import *

# --- checks for the worked examples -----------------------------------------------------------
# pressure at 10 m depth in fresh water
gauge = 1000 * g * 10; P0 = 1.01e5
eq(gauge, 98000.0, 0); eq(P0 + gauge, 199000.0, 0); eq((P0 + gauge) / P0, 1.97, 2); eq(gauge * 0.50, 49000.0, 0)

# hydraulic lift
P = 200 / 0.010; eq(P, 20000.0, 0); eq(P * 0.50, 10000.0, 0); eq(0.50 / 0.010, 50.0, 0)
eq(200 * 5.0, 1000.0, 0); eq(10000 * 0.10, 1000.0, 0); eq(0.10 * 50, 5.0, 1)

# floating block, 600 kg/m^3, 0.020 m^3; hanging metal, 2.0 kg, 4.0e-4 m^3
eq(600 * 0.020 * g, 117.6, 1); eq(600 / 1000, 0.6, 1); eq(1000 * (0.6 * 0.020) * g, 117.6, 1)
eq(1000 * 4.0e-4 * g, 3.92, 2); eq(2.0 * g, 19.6, 1); eq(2.0 * g - 1000 * 4.0e-4 * g, 15.68, 2)
eq(2.0 / 4.0e-4, 5000.0, 0)  # density of the metal object, kg/m^3

# continuity and Bernoulli: 4.0e-3 m^2 at 2.0 m/s into 1.0e-3 m^2, horizontal
v2 = 4.0e-3 * 2.0 / 1.0e-3; eq(v2, 8.0, 1); eq(4.0e-3 * 2.0, 0.008, 3); eq(0.5 * 1000 * (v2 ** 2 - 2.0 ** 2), 30000.0, 0)
# -----------------------------------------------------------------------------------------------

write(8, [
("density-and-pressure", r"""
### The idea
Density tells you how much mass is packed into a volume. Pressure tells you how much force is spread over an area, and in a fluid it grows with depth.

### Key facts
- Density: $\rho = \dfrac{m}{V}$, in $\text{kg/m}^3$. Fresh water is about $1000 \text{ kg/m}^3$.
- Pressure: $P = \dfrac{F}{A}$, in pascals: $1 \text{ Pa} = 1 \text{ N/m}^2$. The force is the part perpendicular to the surface.
- Fluid pressure at depth $h$: $P = P_0 + \rho gh$, where $P_0$ is the pressure at the surface (the atmosphere is $1.01\times10^5 \text{ Pa}$).
- $\rho gh$ alone is the **gauge pressure**, the part above atmospheric.
- Pressure depends on depth and the fluid's density, not on the container's shape or on how much fluid there is.
- At a point, a fluid pushes equally in every direction.

### Watch out for
Dropping the atmosphere. The absolute pressure at depth includes $P_0$. A question about the extra force on a diver or a window usually uses just $\rho gh$, because the air pushes on the other side too.

### Worked example
Find the pressure $10 \text{ m}$ below the surface of a freshwater lake.

Gauge: $\rho gh = (1000)(9.8)(10) = 9.8\times10^4 \text{ Pa}$.

Absolute: $P = 1.01\times10^5 + 9.8\times10^4 = 1.99\times10^5 \text{ Pa}$, about twice atmospheric pressure.

On a $0.50 \text{ m}^2$ hatch, the net force from the water, with air pressure on the other side, is $(9.8\times10^4)(0.50) = 4.9\times10^4 \text{ N}$.
"""),
("pascals-principle", r"""
### The idea
A pressure change applied to a confined, incompressible fluid is passed on everywhere in the fluid. This lets a small force on a small piston balance a large force on a large piston.

### Key facts
- **Pascal's principle:** the change in pressure at one point is transmitted undiminished to every point in the fluid and to the walls.
- Hydraulic system: $\dfrac{F_1}{A_1} = \dfrac{F_2}{A_2}$, so $F_2 = F_1\dfrac{A_2}{A_1}$.
- The fluid is incompressible, so the volume moved is equal: $A_1d_1 = A_2d_2$. The small piston moves farther.
- The device multiplies force but not work: $F_1d_1 = F_2d_2$ (energy is conserved).
- Brakes, jacks and lifts all rely on this.

### Watch out for
Thinking a hydraulic lift gives something for nothing. The larger output force comes with a proportionally shorter distance, so the work out equals the work in.

### Worked example
A hydraulic lift has a small piston of area $0.010 \text{ m}^2$ and a large piston of area $0.50 \text{ m}^2$. A $200 \text{ N}$ force pushes the small piston.

The pressure is $P = \dfrac{200}{0.010} = 2.0\times10^4 \text{ Pa}$, so the large piston exerts

$$F_2 = P A_2 = (2.0\times10^4)(0.50) = 1.0\times10^4 \text{ N},$$

enough to hold up about $1000 \text{ kg}$. The area ratio is $50$.

To raise the load $0.10 \text{ m}$, the small piston must move $5.0 \text{ m}$. Work in is $200(5.0) = 1000 \text{ J}$ and work out is $(1.0\times10^4)(0.10) = 1000 \text{ J}$.
"""),
("buoyancy", r"""
### The idea
A fluid pushes up on any object placed in it, because the pressure is greater at the bottom of the object than at the top. This upward force is the buoyant force.

### Key facts
- **Archimedes' principle:** $F_B = \rho_{fluid}\,V_{sub}\,g$, the weight of the fluid displaced by the submerged part of the object.
- Buoyant force depends on the fluid's density and the **submerged volume**, not on the object's own weight or on how deep it is.
- If $F_B > $ weight, a fully submerged object rises. If $F_B <$ weight, it sinks. It floats at rest when they are equal.
- A floating object has $F_B = mg$, so the fraction submerged is $\dfrac{V_{sub}}{V} = \dfrac{\rho_{obj}}{\rho_{fluid}}$.
- A fully submerged object that hangs from a scale has apparent weight $W - F_B$.

### Watch out for
Saying a heavy object sinks because it is heavy. What matters is its **density** compared with the fluid. A steel ship floats because its shape displaces a huge volume of water.

### Worked example
A block with density $600 \text{ kg/m}^3$ and volume $0.020 \text{ m}^3$ floats in water. Its weight is $(600)(0.020)(9.8) = 117.6 \text{ N}$.

At rest, $F_B = 117.6 \text{ N}$ too, so $V_{sub} = \dfrac{117.6}{(1000)(9.8)} = 0.012 \text{ m}^3$. That is $0.6$ of the block, matching $\dfrac{600}{1000}$.

Now a $2.0 \text{ kg}$ metal object of volume $4.0\times10^{-4} \text{ m}^3$ hangs from a spring scale in water. $F_B = (1000)(4.0\times10^{-4})(9.8) = 3.92 \text{ N}$, so the scale reads $19.6 - 3.92 = 15.7 \text{ N}$.
"""),
("fluid-dynamics", r"""
### The idea
When a fluid flows through a pipe, the amount that enters must also leave. Where the pipe narrows the fluid speeds up, and in that faster flow the pressure is lower.

### Key facts
- **Continuity** (steady, incompressible flow): $A_1v_1 = A_2v_2$. The volume flow rate $Q = Av$ is constant, in $\text{m}^3/\text{s}$.
- **Bernoulli's equation** (steady, incompressible, no viscosity), along a streamline:

$$P + \rho gy + \tfrac{1}{2}\rho v^2 = \text{constant}.$$

- It is conservation of energy for the fluid: pressure, height and speed trade off.
- At the same height, faster flow means lower pressure, which is why wings generate lift and why a narrow section reads a lower pressure.
- For a tank with a hole at depth $h$ below the surface, the exit speed is $v = \sqrt{2gh}$.

### Watch out for
Thinking that a narrow pipe has higher pressure. Narrowing raises the speed, and by Bernoulli the pressure drops there (unless the height changes too).

### Worked example
Water flows at $2.0 \text{ m/s}$ in a horizontal pipe of cross-section $4.0\times10^{-3} \text{ m}^2$, which narrows to $1.0\times10^{-3} \text{ m}^2$.

Continuity: $v_2 = \dfrac{(4.0\times10^{-3})(2.0)}{1.0\times10^{-3}} = 8.0 \text{ m/s}$, with a flow rate of $Q = 8.0\times10^{-3} \text{ m}^3/\text{s}$.

Same height, so $P_1 - P_2 = \tfrac{1}{2}\rho(v_2^2 - v_1^2) = \tfrac{1}{2}(1000)(64 - 4.0) = 3.0\times10^4 \text{ Pa}$. The pressure in the narrow part is lower by that amount.
"""),
])
