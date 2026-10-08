from common import *

# --- checks for the worked examples -----------------------------------------------------------
# 0.40 kg on k = 100 N/m, amplitude 0.050 m
eq(100 * 0.050, 5.0, 1); eq(100 * 0.050 / 0.40, 12.5, 1); eq(100 * 0.020, 2.0, 1)

# periods: 0.25 kg on k = 100 N/m; 1.0 m pendulum
Ts = 2 * pi * sqrt(0.25 / 100); eq(Ts, 0.314, 3); eq(1 / Ts, 3.18, 2)
eq(2 * pi * sqrt(1.0 / g), 2.01, 2)
eq(2 * pi * sqrt(4 * 0.25 / 100) / Ts, 2.0, 1)   # four times the mass: twice the period
eq(2 * pi * sqrt(4 * 1.0 / g) / (2 * pi * sqrt(1.0 / g)), 2.0, 1)  # four times the length: twice the period

# energy: k = 100 N/m, m = 0.25 kg, A = 0.10 m
E = 0.5 * 100 * 0.10 ** 2; eq(E, 0.50, 2)
eq(0.10 * sqrt(100 / 0.25), 2.0, 1)
U6 = 0.5 * 100 * 0.06 ** 2; eq(U6, 0.18, 2); eq(E - U6, 0.32, 2); eq(sqrt(2 * (E - U6) / 0.25), 1.6, 1)
# -----------------------------------------------------------------------------------------------

write(6, [
("restoring-forces-and-shm", r"""
### The idea
Simple harmonic motion is back-and-forth motion caused by a restoring force that always pulls the object toward equilibrium and grows in proportion to the displacement.

### Key facts
- Restoring force: $F = -kx$ (springs), so acceleration is $a = -\dfrac{k}{m}x$, always opposite to the displacement.
- **Amplitude** $A$ is the maximum displacement. **Period** $T$ is the time for one full cycle, and **frequency** is $f = \dfrac{1}{T}$ in hertz.
- At the **ends** ($x = \pm A$): speed is zero and the force and acceleration are at their maximum.
- At **equilibrium** ($x = 0$): the net force and acceleration are zero and the speed is at its maximum.
- Position, velocity and acceleration against time are all sinusoidal, each shifted a quarter-cycle from the next.
- A pendulum swinging through small angles is also approximately SHM.

### Watch out for
Thinking the speed is zero where the force is zero. At the center the force is zero, but the object is moving fastest. At the ends it momentarily stops, where the force is largest.

### Worked example
A $0.40 \text{ kg}$ mass on a spring with $k = 100 \text{ N/m}$ oscillates with amplitude $0.050 \text{ m}$.

At the end of its path: $F_{max} = kA = (100)(0.050) = 5.0 \text{ N}$, so $a_{max} = \dfrac{5.0}{0.40} = 12.5 \text{ m/s}^2$, directed toward the center.

When it is $0.020 \text{ m}$ from the center, $|F| = (100)(0.020) = 2.0 \text{ N}$, which is smaller. At the center $F = 0$ and $a = 0$.
"""),
("period-of-springs-and-pendulums", r"""
### The idea
How long one cycle takes depends on how strong the restoring force is compared with the inertia, not on how large the swing is.

### Key facts
- Mass on a spring: $T_s = 2\pi\sqrt{\dfrac{m}{k}}$.
- Simple pendulum: $T_p = 2\pi\sqrt{\dfrac{L}{g}}$, valid for small angles.
- Neither period depends on the **amplitude**.
- A pendulum's period does not depend on its mass. A spring's period does not depend on $g$ (a vertical spring oscillates at the same rate on the Moon).
- Quadrupling the mass on a spring, or the length of a pendulum, doubles the period. A stiffer spring makes the period shorter.
- Frequency is $f = \dfrac{1}{T}$.

### Watch out for
Using the pendulum formula with the mass in it, or saying a bigger swing takes longer. A bigger swing means faster speeds that make up for the longer path.

### Worked example
A $0.25 \text{ kg}$ mass on a spring with $k = 100 \text{ N/m}$:

$$T = 2\pi\sqrt{\frac{0.25}{100}} = 0.314 \text{ s}, \qquad f = \frac{1}{T} = 3.18 \text{ Hz}.$$

A $1.0 \text{ m}$ pendulum on Earth:

$$T = 2\pi\sqrt{\frac{1.0}{9.8}} = 2.01 \text{ s}.$$

Changing the bob's mass does nothing to this period. Making the string $4.0 \text{ m}$ long doubles it to about $4.0 \text{ s}$.
"""),
("energy-in-shm", r"""
### The idea
In SHM, the total mechanical energy stays constant while it moves back and forth between kinetic energy and potential energy.

### Key facts
- Total energy: $E = \tfrac{1}{2}kA^2$ for a spring system, set by the amplitude.
- At any position: $\tfrac{1}{2}mv^2 + \tfrac{1}{2}kx^2 = \tfrac{1}{2}kA^2$.
- At $x = 0$: all kinetic, and the speed is maximum, $v_{max} = A\sqrt{\dfrac{k}{m}}$.
- At $x = \pm A$: all potential, and the speed is zero.
- Kinetic energy and potential energy each peak twice per cycle.
- Doubling the amplitude gives four times the energy and twice the maximum speed.
- A pendulum is the same story with gravitational potential energy: fastest at the bottom, stopped at the top of the swing.

### Watch out for
Saying the total energy changes during the motion. Only the split changes. Total energy changes only if friction or another outside force does work.

### Worked example
A $0.25 \text{ kg}$ mass on a spring with $k = 100 \text{ N/m}$, amplitude $0.10 \text{ m}$.

Total energy: $E = \tfrac{1}{2}(100)(0.10)^2 = 0.50 \text{ J}$.

Maximum speed: $v_{max} = 0.10\sqrt{\dfrac{100}{0.25}} = 2.0 \text{ m/s}$.

At $x = 0.06 \text{ m}$, $U = \tfrac{1}{2}(100)(0.06)^2 = 0.18 \text{ J}$, so $K = 0.50 - 0.18 = 0.32 \text{ J}$ and $v = \sqrt{\dfrac{2(0.32)}{0.25}} = 1.6 \text{ m/s}$.
"""),
])
