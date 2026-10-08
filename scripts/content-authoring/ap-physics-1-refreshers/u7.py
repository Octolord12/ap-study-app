from common import *

# --- checks for the worked examples -----------------------------------------------------------
# wheel from rest, alpha = 2.0 rad/s^2, t = 5.0 s, point at r = 0.30 m
w = 2.0 * 5.0; th = 0.5 * 2.0 * 5.0 ** 2
eq(w, 10.0, 1); eq(th, 25.0, 1); eq(th / (2 * pi), 3.98, 2)
eq(0.30 * w, 3.0, 1); eq(w ** 2 * 0.30, 30.0, 1); eq(0.30 * 2.0, 0.60, 2)

# torque: 40 N at 30 degrees, 0.25 m from the pivot
eq(0.25 * 40 * sin(rad(30)), 5.0, 1); eq(0.25 * 40 * sin(rad(90)), 10.0, 1)

# uniform 4.0 m, 20 kg beam on two supports, 30 kg person 1.0 m from the left end
NR = (20 * g * 2.0 + 30 * g * 1.0) / 4.0; NL = 50 * g - NR
eq(20 * g * 2.0, 392.0, 0); eq(30 * g * 1.0, 294.0, 0); eq(NR, 171.5, 1); eq(NL, 318.5, 1)

# rotational inertia: two 2.0 kg masses 0.50 m from the axis; moved out to 1.0 m
I1 = 2 * 2.0 * 0.50 ** 2; I2 = 2 * 2.0 * 1.0 ** 2
eq(I1, 1.0, 1); eq(0.5 * I1 * 4.0 ** 2, 8.0, 1); eq(3.0 / I1, 3.0, 1); eq(I2, 4.0, 1); eq(3.0 / I2, 0.75, 2)
# rolling solid disk, m = 2.0 kg, v = 4.0 m/s: K = (3/4) m v^2
eq(0.5 * 2.0 * 4.0 ** 2 + 0.5 * (0.5 * 2.0) * 4.0 ** 2, 24.0, 1)

# angular momentum: skater I = 3.0 -> 1.2 kg m^2, w = 2.0 rad/s
w2 = 3.0 * 2.0 / 1.2; eq(w2, 5.0, 1); eq(0.5 * 3.0 * 2.0 ** 2, 6.0, 1); eq(0.5 * 1.2 * w2 ** 2, 15.0, 1)
# -----------------------------------------------------------------------------------------------

write(7, [
("rotational-kinematics", r"""
### The idea
Rotation has its own versions of position, velocity and acceleration. With constant angular acceleration, the equations look exactly like the straight-line ones.

### Key facts
- Angle $\theta$ in **radians**: $1 \text{ rev} = 2\pi \text{ rad}$. Angular velocity $\omega = \dfrac{\Delta\theta}{\Delta t}$ in $\text{rad/s}$, angular acceleration $\alpha = \dfrac{\Delta\omega}{\Delta t}$ in $\text{rad/s}^2$.
- Constant $\alpha$: $\omega = \omega_0 + \alpha t$ and $\theta = \theta_0 + \omega_0 t + \tfrac{1}{2}\alpha t^2$.
- Every point on a rigid rotating object shares the same $\omega$ and $\alpha$.
- A point at radius $r$ has tangential speed $v = r\omega$ and tangential acceleration $a_t = r\alpha$. Points farther out move faster.
- Its centripetal acceleration is $a_c = \omega^2 r$.

### Watch out for
Using degrees or revolutions in $v = r\omega$. The relationship only works with radians.

### Worked example
A wheel starts from rest with $\alpha = 2.0 \text{ rad/s}^2$. After $5.0 \text{ s}$:

$$\omega = (2.0)(5.0) = 10 \text{ rad/s}, \qquad \theta = \tfrac{1}{2}(2.0)(5.0)^2 = 25 \text{ rad} = 3.98 \text{ rev}.$$

A point on the rim at $r = 0.30 \text{ m}$ has speed $v = (0.30)(10) = 3.0 \text{ m/s}$, centripetal acceleration $a_c = (10)^2(0.30) = 30 \text{ m/s}^2$, and tangential acceleration $a_t = (0.30)(2.0) = 0.60 \text{ m/s}^2$.
"""),
("torque", r"""
### The idea
Torque is the rotational effect of a force. A force produces more torque the farther from the pivot it acts and the more perpendicular it is to the lever arm.

### Key facts
- $\tau = rF\sin\theta$, where $r$ is the distance from the pivot to where the force acts and $\theta$ is the angle between the lever arm and the force. The unit is $\text{N·m}$.
- Equivalently, $\tau = r_\perp F$, force times the perpendicular distance from the pivot to the force's line of action.
- Take counterclockwise as positive and clockwise as negative, and keep the convention for the whole problem.
- A force that passes through the pivot (or points along the lever arm) gives zero torque.
- Net torque causes angular acceleration: $\Sigma\tau = I\alpha$.

### Watch out for
Using the angle between the force and the horizontal when the formula needs the angle between the force and the lever arm. A push exactly perpendicular to a wrench gives the maximum torque.

### Worked example
A $40 \text{ N}$ force is applied to a wrench $0.25 \text{ m}$ from the bolt, at $30^\circ$ to the wrench.

$$\tau = (0.25)(40)\sin 30^\circ = 5.0 \text{ N·m}.$$

Pushing perpendicular instead gives $\tau = (0.25)(40)\sin 90^\circ = 10 \text{ N·m}$.

A longer wrench lets the same force make more torque, which is why a pipe slipped over the handle helps with a stuck bolt.
"""),
("rotational-equilibrium", r"""
### The idea
An object is in rotational equilibrium when the torques on it balance, so it has no angular acceleration. Static equilibrium needs the forces to balance too.

### Key facts
- Both conditions: $\Sigma F = 0$ and $\Sigma\tau = 0$ about **any** pivot point.
- Because any pivot works, choose one where an unknown force acts. That force then has zero lever arm and drops out of the torque equation.
- The weight of a uniform beam acts at its center.
- Method: draw all forces, choose a pivot, set clockwise torques equal to counterclockwise torques, then use $\Sigma F = 0$ for what remains.
- A seesaw balances when $m_1d_1 = m_2d_2$, with each distance measured from the pivot.

### Watch out for
Forgetting the weight of the beam itself, or measuring a distance from the wrong place. Every lever arm in a torque equation must be measured from the same chosen pivot.

### Worked example
A uniform $4.0 \text{ m}$ beam of mass $20 \text{ kg}$ rests on supports at its two ends. A $30 \text{ kg}$ person stands $1.0 \text{ m}$ from the left end.

Torques about the left end remove the left support from the equation:

$$N_R(4.0) = (20)(9.8)(2.0) + (30)(9.8)(1.0) = 392 + 294 \quad\Rightarrow\quad N_R = 171.5 \text{ N}.$$

Then $N_L = (50)(9.8) - 171.5 = 318.5 \text{ N}$. The left support carries more because the person is nearer to it.
"""),
("moment-of-inertia-and-rotational-kinetic-energy", r"""
### The idea
Rotational inertia $I$ is an object's resistance to angular acceleration. It is the rotational counterpart of mass, but it depends on where the mass is, not only how much.

### Key facts
- For point masses: $I = \sum mr^2$, in $\text{kg·m}^2$. Mass far from the axis counts for much more.
- $I$ depends on the axis chosen. Common values: a hoop of radius $R$ is $MR^2$ and a solid disk or cylinder is $\tfrac{1}{2}MR^2$. For other shapes a problem usually states $I$.
- Rotational form of Newton's Second Law: $\Sigma\tau = I\alpha$.
- Rotational kinetic energy: $K = \tfrac{1}{2}I\omega^2$.
- A rolling object without slipping has both kinds: $K = \tfrac{1}{2}mv^2 + \tfrac{1}{2}I\omega^2$, with $v = r\omega$.

### Watch out for
Treating $I$ as a fixed property of the object. Moving the same masses farther from the axis raises $I$, so the same torque gives less angular acceleration.

### Worked example
Two $2.0 \text{ kg}$ masses are on a light rod, each $0.50 \text{ m}$ from the axis. $I = 2(2.0)(0.50)^2 = 1.0 \text{ kg·m}^2$.

At $\omega = 4.0 \text{ rad/s}$, $K = \tfrac{1}{2}(1.0)(4.0)^2 = 8.0 \text{ J}$. A torque of $3.0 \text{ N·m}$ gives $\alpha = \dfrac{3.0}{1.0} = 3.0 \text{ rad/s}^2$.

Moving the masses out to $1.0 \text{ m}$ makes $I = 4.0 \text{ kg·m}^2$, so the same torque gives only $0.75 \text{ rad/s}^2$.

A solid disk of mass $2.0 \text{ kg}$ rolling at $4.0 \text{ m/s}$ has $K = \tfrac{1}{2}mv^2 + \tfrac{1}{4}mv^2 = 24 \text{ J}$.
"""),
("angular-momentum", r"""
### The idea
Angular momentum measures how much rotation an object has. Like linear momentum, it stays constant when no outside torque acts.

### Key facts
- For a rotating object: $L = I\omega$, in $\text{kg·m}^2/\text{s}$.
- For a point mass moving past a pivot: $L = rmv\sin\theta$, which is $mvr$ when the velocity is perpendicular to $r$.
- Net torque changes it: $\Sigma\tau = \dfrac{\Delta L}{\Delta t}$.
- If the net external torque is zero, $L$ is conserved: $I_i\omega_i = I_f\omega_f$.
- When $I$ drops, $\omega$ rises to compensate, as with a skater pulling in the arms or a diver tucking.
- A small object sticking onto a spinning disk changes $I$, so $\omega$ drops.

### Watch out for
Assuming kinetic energy is conserved too. When the skater pulls in, $L$ is constant but the kinetic energy rises, because the skater does work pulling the arms inward.

### Worked example
A skater spins at $\omega = 2.0 \text{ rad/s}$ with her arms out ($I = 3.0 \text{ kg·m}^2$). She pulls them in to $I = 1.2 \text{ kg·m}^2$.

$$\omega_f = \frac{I_i\omega_i}{I_f} = \frac{(3.0)(2.0)}{1.2} = 5.0 \text{ rad/s}.$$

Kinetic energy before: $\tfrac{1}{2}(3.0)(2.0)^2 = 6.0 \text{ J}$. After: $\tfrac{1}{2}(1.2)(5.0)^2 = 15 \text{ J}$. The extra energy came from the work done by her muscles.
"""),
])
