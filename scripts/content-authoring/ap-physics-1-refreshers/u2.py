from common import *

# --- checks for the worked examples -----------------------------------------------------------
# two blocks, 2 kg pushed by 10 N against a 3 kg block
a = 10 / (2 + 3); eq(a, 2.0); eq(3 * a, 6.0); eq(10 - 6, 2 * a)

# 4.0 kg crate, rope 20 N at 30 degrees above horizontal
eq(4 * g, 39.2); eq(20 * sin(rad(30)), 10.0, 1); eq(4 * g - 20 * sin(rad(30)), 29.2, 1); eq(20 * cos(rad(30)), 17.3, 1)

# 10 kg sign on two cables, each 30 degrees above horizontal
eq(10 * g, 98.0); eq(10 * g / (2 * sin(rad(30))), 98.0, 1)

# 60 kg person in an elevator accelerating up at 2.0 m/s^2
eq(60 * g, 588.0); eq(60 * (g + 2.0), 708.0)

# 10 kg block on a 30 degree incline, mu_k = 0.20
N = 10 * g * cos(rad(30)); f = 0.20 * N; mgs = 10 * g * sin(rad(30))
eq(N, 84.9, 1); eq(f, 17.0, 1); eq(mgs, 49.0, 1); eq((mgs - f) / 10, 3.20, 2)
eq(g * (sin(rad(30)) - 0.20 * cos(rad(30))), 3.20, 2)
# Atwood: 3 kg and 2 kg
a2 = (3 - 2) * g / 5; eq(a2, 1.96, 2); eq(2 * (g + a2), 23.52, 2); eq(3 * g - 3 * a2, 23.52, 2)
# -----------------------------------------------------------------------------------------------

write(2, [
("newtons-third-law-and-systems", r"""
### The idea
Forces come in pairs. Whenever one object pushes or pulls another, the second pushes or pulls back on the first with a force of the same size in the opposite direction. Choosing a **system** decides which forces matter for its acceleration.

### Key facts
- A Newton's Third Law pair acts on **two different objects**, has equal magnitudes, opposite directions and is the **same type** of force (gravity with gravity, contact with contact).
- Because the two forces act on different objects, they never cancel each other in one object's free-body diagram.
- The size of the forces is equal even when the masses are very different. The smaller mass simply accelerates more.
- For a system, forces between members of the system are **internal** and cancel in the total. Only **external** forces change the system's motion.

### Watch out for
Calling a book's weight and the table's normal force a Third Law pair. They act on the same object and are different types of force. The weight's partner is the book pulling up on Earth.

### Worked example
Two blocks, $2.0 \text{ kg}$ and $3.0 \text{ kg}$, touch on a frictionless table. A $10 \text{ N}$ push is applied to the $2.0 \text{ kg}$ block, which pushes the other.

As one system: $a = \dfrac{10}{2.0 + 3.0} = 2.0 \text{ m/s}^2$.

The force on the $3.0 \text{ kg}$ block is $F = (3.0)(2.0) = 6.0 \text{ N}$. By the Third Law the $3.0 \text{ kg}$ block pushes back on the $2.0 \text{ kg}$ block with $6.0 \text{ N}$.

Check the first block: $10 - 6.0 = 4.0 \text{ N} = (2.0)(2.0)$.
"""),
("free-body-diagrams", r"""
### The idea
A free-body diagram shows one object, drawn as a dot or box, and every force acting **on** it. It turns a physical situation into something you can apply Newton's Second Law to.

### Key facts
- Draw an arrow for each force, starting on the object, with length roughly showing its size.
- Label each by type and source: weight $F_g$ (down), normal $F_N$ (perpendicular to the surface), tension $F_T$ (along the rope), friction $F_f$ (along the surface), applied push or pull.
- Include only forces **on** the object, never forces the object exerts on something else.
- Pick axes, then split any angled force into components: $F_x = F\cos\theta$ and $F_y = F\sin\theta$ (with $\theta$ measured from the axis).
- On an incline, tilt the axes so one is along the slope.

### Watch out for
Drawing a "force of motion" or an extra "centripetal force" arrow. Motion needs no force to continue, and centripetal is the name for the net inward force, not a new arrow. The normal force also is not always equal to the weight.

### Worked example
A $4.0 \text{ kg}$ crate is pulled across a floor by a rope with $20 \text{ N}$ at $30^\circ$ above horizontal.

The weight is $mg = 39.2 \text{ N}$ down. The rope gives $20\cos 30^\circ = 17.3 \text{ N}$ forward and $20\sin 30^\circ = 10 \text{ N}$ upward.

The crate does not move vertically, so $F_N + 10 = 39.2$, giving $F_N = 29.2 \text{ N}$. The normal force is smaller than the weight because the rope helps hold the crate up.
"""),
("newtons-first-law", r"""
### The idea
An object keeps doing what it is doing, at rest or moving at constant velocity in a straight line, unless a **net** force acts on it. That tendency is **inertia**, and mass is the measure of it.

### Key facts
- $\Sigma F = 0$ means $a = 0$: the object is in **equilibrium**, either at rest or moving at constant velocity.
- Equilibrium applies to each direction separately: $\Sigma F_x = 0$ and $\Sigma F_y = 0$.
- A constant-velocity object has forces on it that balance. Pushing something at steady speed across a rough floor means your push equals the friction.
- An object at rest on a surface has the weight balanced by the normal force.
- To find an unknown force in equilibrium, write the balance equation for each axis.

### Watch out for
Believing that motion requires a net force. A hockey puck sliding with no friction keeps going. Only a change in velocity needs a net force.

### Worked example
A $10 \text{ kg}$ sign hangs from two cables, each at $30^\circ$ above the horizontal. Find the tension $T$ in each.

Weight: $mg = 98 \text{ N}$. The horizontal pulls cancel by symmetry. Vertically, the two cables together hold the weight:

$$
\begin{aligned}
2T\sin 30^\circ &= 98 \\
T &= \frac{98}{2(0.5)} = 98 \text{ N}
\end{aligned}
$$

Each cable carries a tension equal to the whole weight, because the cables are at a shallow angle. A steeper angle would give a smaller tension.
"""),
("newtons-second-law", r"""
### The idea
The net force on an object causes an acceleration in the same direction, and the larger the mass, the smaller the acceleration for a given force.

### Key facts
- $\Sigma \vec F = m\vec a$, or $a = \dfrac{\Sigma F}{m}$. The unit is the newton: $1 \text{ N} = 1 \text{ kg·m/s}^2$.
- Acceleration points along the **net** force, not along the velocity.
- Method: draw the free-body diagram, choose a positive direction, add the forces along it (with signs), and set the sum equal to $ma$.
- **Weight** is the gravitational force: $F_g = mg$, in newtons. Mass is in kilograms and does not change with location.
- A scale reads the normal force, not the weight. It differs from $mg$ if the person is accelerating vertically.

### Watch out for
Forgetting that equal forces on different masses give different accelerations, and adding forces that are not on the object. Only forces acting **on** the object go into $\Sigma F$.

### Worked example
A $60 \text{ kg}$ person stands on a scale in an elevator that accelerates **upward** at $2.0 \text{ m/s}^2$.

Take up as positive. The normal force from the scale is up, the weight $mg = 588 \text{ N}$ is down:

$$
\begin{aligned}
F_N - mg &= ma \\
F_N &= 60(9.8 + 2.0) = 708 \text{ N}
\end{aligned}
$$

The scale reads $708 \text{ N}$, more than the $588 \text{ N}$ weight. If the elevator accelerated downward at $2.0 \text{ m/s}^2$, it would read $60(9.8 - 2.0) = 468 \text{ N}$.
"""),
("applications-of-newtons-second-law", r"""
### The idea
Most dynamics problems are Newton's Second Law with a few standard forces: friction, the pieces of weight on a slope, and tension in connected objects.

### Key facts
- **Kinetic friction** $F_f = \mu_k F_N$ opposes the sliding. **Static friction** adjusts to match the push, up to a maximum $F_f \le \mu_s F_N$.
- Friction depends on the normal force and the surfaces, not on the contact area or the speed.
- On an incline of angle $\theta$: the weight splits into $mg\sin\theta$ **along** the slope and $mg\cos\theta$ **into** it, so $F_N = mg\cos\theta$ (with no other vertical forces).
- Connected objects on a taut rope share the same acceleration size. Write the Second Law for each object, or for the system.
- In an Atwood machine (two masses over a pulley) $a = \dfrac{(m_1 - m_2)g}{m_1 + m_2}$.

### Watch out for
Assuming $F_N = mg$ on a slope. The normal force is smaller, so friction is smaller as well.

### Worked example
A $10 \text{ kg}$ block slides down a $30^\circ$ incline with $\mu_k = 0.20$.

$F_N = 98\cos 30^\circ = 84.9 \text{ N}$, so $F_f = 0.20(84.9) = 17.0 \text{ N}$ up the slope. The weight component down the slope is $98\sin 30^\circ = 49 \text{ N}$.

$$a = \frac{49 - 17.0}{10} = 3.20 \text{ m/s}^2$$

The acceleration is down the slope. For a $3.0 \text{ kg}$ and a $2.0 \text{ kg}$ mass on an Atwood machine, $a = \dfrac{1.0(9.8)}{5.0} = 1.96 \text{ m/s}^2$ and the tension is $2.0(9.8 + 1.96) = 23.5 \text{ N}$.
"""),
])
