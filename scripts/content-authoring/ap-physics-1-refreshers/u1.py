from common import *

# --- checks for the worked examples -----------------------------------------------------------
# position, velocity, acceleration: 0 -> +60 m in 10 s, then back to +20 m in 5 s
eq(60 + 40, 100); eq(20 - 0, 20)
eq(100 / 15, 6.67); eq(20 / 15, 1.33)
eq((10 - 22) / 3, -4.0)  # slows from 22 to 10 m/s in 3 s

# v-t graph: 0 -> 6 m/s in 3 s, steady 4 s, 6 -> 0 in 2 s
eq(6 / 3, 2.0); eq(-6 / 2, -3.0)
area = 0.5 * 3 * 6 + 6 * 4 + 0.5 * 2 * 6
eq(area, 39.0); eq(area / 9, 4.33)

# braking car
eq(25 ** 2 / (2 * 5), 62.5); eq(25 / 5, 5.0); eq(25 * 5 - 0.5 * 5 * 5 ** 2, 62.5); eq(50 ** 2 / (2 * 5), 250.0)

# horizontal launch off a 20 m cliff at 12 m/s
t = sqrt(2 * 20 / g)
eq(t, 2.02); eq(12 * t, 24.2, 1); eq(g * t, 19.8, 1)
# -----------------------------------------------------------------------------------------------

write(1, [
("position-velocity-acceleration", r"""
### The idea
Motion along a line is described by three linked quantities: where the object is, how fast its position changes, and how fast its velocity changes. All three are vectors, so their signs carry direction.

### Key facts
- **Displacement** $\Delta x = x_f - x_i$ is the straight-line change in position. **Distance** is the total path length and is never negative.
- **Average velocity** is $v_{avg} = \dfrac{\Delta x}{\Delta t}$. **Average speed** is distance divided by time.
- **Acceleration** is the rate of change of velocity: $a = \dfrac{\Delta v}{\Delta t}$, in $\text{m/s}^2$.
- The object is **speeding up** when $v$ and $a$ have the same sign, and **slowing down** when they have opposite signs.
- Acceleration can be nonzero while velocity is zero, for example at the top of a ball's flight.

### Watch out for
Treating a negative acceleration as "slowing down". If the object is already moving in the negative direction, a negative acceleration makes it go faster. Always compare the signs of $v$ and $a$.

### Worked example
A cart starts at $x = 0$, rolls to $x = 60 \text{ m}$ in $10 \text{ s}$, then returns to $x = 20 \text{ m}$ in the next $5 \text{ s}$.

Distance: $60 + 40 = 100 \text{ m}$. Displacement: $20 - 0 = 20 \text{ m}$.

Average speed: $\dfrac{100}{15} = 6.67 \text{ m/s}$. Average velocity: $\dfrac{20}{15} = 1.33 \text{ m/s}$.

If a moving car goes from $22 \text{ m/s}$ to $10 \text{ m/s}$ in $3 \text{ s}$, then $a = \dfrac{10 - 22}{3} = -4.0 \text{ m/s}^2$. It is slowing down because $v$ is positive and $a$ is negative.
"""),
("representations-of-motion", r"""
### The idea
A graph of motion is a picture of what the object is doing. The same motion can be drawn as position, velocity or acceleration against time, and each graph is read with slopes and areas.

### Key facts
- **Position-time graph:** the slope is the velocity. A straight line means constant velocity, a curve means changing velocity, a flat line means at rest.
- **Velocity-time graph:** the slope is the acceleration, and the area between the graph and the time axis is the displacement. Area below the axis counts as negative.
- **Acceleration-time graph:** the area is the change in velocity.
- A velocity-time graph that crosses zero shows the object turning around.
- A straight, sloped line on a velocity-time graph means constant acceleration, so it is a curved (parabolic) line on a position-time graph.

### Watch out for
Reading the height of a graph as if it were the slope. On a position-time graph a high point means the object is far from the origin, not that it is moving fast. Speed comes from steepness.

### Worked example
An object's velocity rises steadily from $0$ to $6 \text{ m/s}$ in $3 \text{ s}$, stays at $6 \text{ m/s}$ for $4 \text{ s}$, then falls to $0$ in $2 \text{ s}$.

Accelerations (slopes): $\dfrac{6}{3} = 2.0 \text{ m/s}^2$, then $0$, then $\dfrac{-6}{2} = -3.0 \text{ m/s}^2$.

Displacement (areas): $\tfrac{1}{2}(3)(6) + (6)(4) + \tfrac{1}{2}(2)(6) = 9 + 24 + 6 = 39 \text{ m}$.

Average velocity over the $9 \text{ s}$: $\dfrac{39}{9} = 4.33 \text{ m/s}$.
"""),
("kinematic-equations", r"""
### The idea
When acceleration is constant, a small set of equations connects displacement, time, initial and final velocity, and acceleration. Choose the equation that contains the unknown you want and leaves out the quantity you neither know nor need.

### Key facts
- $v = v_0 + at$ (no displacement).
- $\Delta x = v_0 t + \tfrac{1}{2}at^2$ (no final velocity).
- $v^2 = v_0^2 + 2a\,\Delta x$ (no time).
- Write down what you know and what you want, with a sign convention, before choosing.
- In free fall near Earth the acceleration is $9.8 \text{ m/s}^2$ downward, whether the object is rising, falling or at the top.
- These equations are valid **only** when the acceleration is constant.

### Watch out for
Plugging a deceleration in as a positive number. If you call the direction of motion positive, braking gives a negative $a$. Mixing signs is the most common source of wrong answers.

### Worked example
A car moving at $25 \text{ m/s}$ brakes with $a = -5.0 \text{ m/s}^2$ until it stops. How far does it go?

The final velocity is $0$ and time is not asked for, so use $v^2 = v_0^2 + 2a\,\Delta x$:

$$0 = 25^2 + 2(-5.0)\,\Delta x \quad\Rightarrow\quad \Delta x = \frac{625}{10} = 62.5 \text{ m}.$$

Time: $t = \dfrac{0 - 25}{-5.0} = 5.0 \text{ s}$. Check: $25(5.0) - \tfrac{1}{2}(5.0)(5.0)^2 = 62.5 \text{ m}$.

Doubling the starting speed to $50 \text{ m/s}$ gives $250 \text{ m}$, four times as far.
"""),
("projectile-motion", r"""
### The idea
A projectile moves under gravity alone. Its horizontal and vertical motions are independent, and the only thing they share is the time.

### Key facts
- **Horizontal:** no acceleration, so $v_x$ is constant and $\Delta x = v_x t$.
- **Vertical:** acceleration is $9.8 \text{ m/s}^2$ downward the whole time, so use the constant-acceleration equations with $a_y = -9.8 \text{ m/s}^2$ (up positive).
- A launch at speed $v$ and angle $\theta$ has $v_x = v\cos\theta$ and $v_{0y} = v\sin\theta$.
- At the top of the path $v_y = 0$ but $v_x$ is not zero, and the acceleration is still $9.8 \text{ m/s}^2$ downward.
- A ball launched horizontally falls exactly as fast as one dropped from the same height.
- With no air resistance, a projectile that returns to its launch height takes equal time to go up and down.

### Watch out for
Giving the projectile a horizontal force or acceleration. Nothing pushes it sideways once it leaves the launcher, so $a_x = 0$.

### Worked example
A ball is kicked horizontally at $12 \text{ m/s}$ from a $20 \text{ m}$ cliff.

Fall time depends only on the vertical motion: $20 = \tfrac{1}{2}(9.8)t^2$, so $t = \sqrt{\dfrac{2(20)}{9.8}} = 2.02 \text{ s}$.

Horizontal distance: $\Delta x = 12(2.02) = 24.2 \text{ m}$.

Vertical speed on landing: $v_y = 9.8(2.02) = 19.8 \text{ m/s}$ downward, while $v_x$ is still $12 \text{ m/s}$.
"""),
])
