"""Unit 9, vector-valued functions and motion in the plane."""
from lib import *

R = Rational
T_VV, T_MP = "vector-valued-functions", "motion-in-the-plane"


def add(B):
    # ------------------------------------------------------------ vector-valued functions
    r = Matrix([t**2, sin(t)])
    d = r.diff(t).subs(t, pi)
    assert list(d) == [2 * pi, -1]
    B.mcq(T_VV, "A particle's position is $\\vec r(t)=\\langle t^2,\\sin t\\rangle$. What is its velocity vector at $t=\\pi$?",
          chvec((2 * pi, -1), "$\\vec v(t)=\\vec r\\,'(t)=\\langle2t,\\cos t\\rangle$, and at $t=\\pi$ this is $\\langle2\\pi,-1\\rangle$."),
          [chvec((2 * pi, 1), "$\\frac{d}{dt}\\sin t=\\cos t$, and $\\cos\\pi=-1$."),
           chvec((pi**2, 0), "This is the position $\\vec r(\\pi)$, not the velocity."),
           chvec((2, -1), "The derivative of $t^2$ is $2t$, which is $2\\pi$ at $t=\\pi$.")],
          "Velocity is the derivative of the position vector, taken component by component.", difficulty="easy")

    v = Matrix([3 * t**2, 2 * t])
    assert simplify(v.subs(t, 1).norm() - sqrt(13)) == 0
    B.mcq(T_VV, "A particle's velocity is $\\vec v(t)=\\langle3t^2,2t\\rangle$. What is its speed at $t=1$?",
          ch(sqrt(13), "Speed is the magnitude of velocity: $\\sqrt{3^2+2^2}=\\sqrt{13}$ at $t=1$."),
          [ch(5, "This adds the components, $3+2$. The magnitude uses the Pythagorean theorem."),
           ch(13, "This is the sum of squares. Speed is its square root."),
           ch(sqrt(5), "This evaluates the components at $t=1$ as $1$ and $2$: $\\sqrt{1^2+2^2}$. At $t=1$, $3t^2=3$.")],
          "Speed is $|\\vec v|=\\sqrt{(x')^2+(y')^2}$.", difficulty="easy")

    r = Matrix([t**3, exp(2 * t)])
    a = r.diff(t, 2).subs(t, 0)
    assert list(a) == [0, 4]
    B.mcq(T_VV, "A particle's position is $\\vec r(t)=\\langle t^3,e^{2t}\\rangle$. What is its acceleration vector at $t=0$?",
          chvec((0, 4), "$\\vec a=\\vec r\\,''=\\langle6t,4e^{2t}\\rangle$, which is $\\langle0,4\\rangle$ at $t=0$."),
          [chvec((0, 2), "This is the velocity at $t=0$, $\\langle3t^2,2e^{2t}\\rangle$. Acceleration needs a second derivative."),
           chvec((0, 1), "This is the position at $t=0$, $\\langle0^3,e^0\\rangle$. Each derivative of $e^{2t}$ multiplies by 2, so differentiating twice gives $4e^{2t}$."),
           chvec((6, 4), "The $x$-component is $6t$, which is 0 at $t=0$.")],
          "Acceleration is the second derivative of position, taken component by component.", difficulty="medium")

    rr = Matrix([t**2 + 1, sin(t) + 2])
    assert list(rr.diff(t)) == [2 * t, cos(t)] and list(rr.subs(t, 0)) == [1, 2]
    B.mcq(T_VV, "A particle's velocity is $\\vec v(t)=\\langle2t,\\cos t\\rangle$ and its position at $t=0$ is $\\langle1,2\\rangle$. What is its position at $t=\\dfrac\\pi2$?",
          chvec((pi**2 / 4 + 1, 3), "Integrate each component: $x(t)=t^2+C_1$ with $x(0)=1$ gives $x=t^2+1$; $y(t)=\\sin t+C_2$ with $y(0)=2$ gives $y=\\sin t+2$. At $t=\\frac\\pi2$: $\\left\\langle\\frac{\\pi^2}{4}+1,3\\right\\rangle$."),
          [chvec((pi**2 / 4, 1), "This leaves out the initial position, so both constants of integration are missing."),
           chvec((pi**2 / 4 + 1, 1), "The $y$-component also needs its initial value: $y(t)=\\sin t+2$."),
           chvec((pi + 1, 3), "This evaluates the velocity component $2t$ at $t=\\frac\\pi2$ (which is $\\pi$) instead of integrating it. The antiderivative of $2t$ is $t^2$, which is $\\frac{\\pi^2}{4}$ there.")],
          "Integrate the velocity components and use the initial position to find the constants.", difficulty="medium")

    ig = Matrix([3 * t**2, 2 * t]).applyfunc(lambda e: integrate(e, (t, 0, 1)))
    assert list(ig) == [1, 1]
    B.mcq(T_VV, "What is $\\displaystyle\\int_0^1\\langle3t^2,2t\\rangle\\,dt$?",
          chvec((1, 1), "Integrate each component over $[0,1]$: $\\int_0^13t^2dt=1$ and $\\int_0^12t\\,dt=1$."),
          [chvec((3, 2), "This evaluates the integrand at $t=1$. The integral of each component is the antiderivative evaluated at 1 minus at 0."),
           chvec((1, 2), "$\\int_0^12t\\,dt=\\left[t^2\\right]_0^1=1$, not 2."),
           chvec((3, 1), "$\\int_0^13t^2dt=\\left[t^3\\right]_0^1=1$, not 3.")],
          "A vector-valued function is integrated one component at a time.", difficulty="easy")

    r = Matrix([exp(t), t**2])
    vv = r.diff(t).subs(t, log(2))
    assert list(vv) == [2, 2 * log(2)]
    B.mcq(T_VV, "A particle's position is $\\vec r(t)=\\langle e^t,t^2\\rangle$. What is its velocity at $t=\\ln2$?",
          chvec((2, 2 * log(2)), "$\\vec v=\\langle e^t,2t\\rangle$, so at $t=\\ln2$ it is $\\langle2,2\\ln2\\rangle$."),
          [chvec((2, log(2)**2), "This is the position $\\langle e^{\\ln2},(\\ln2)^2\\rangle$, not the velocity."),
           chvec((2, log(2)), "The derivative of $t^2$ is $2t$, so the second component is $2\\ln2$."),
           chvec((log(2), 2 * log(2)), "$e^t$ is its own derivative, and $e^{\\ln2}=2$, not $\\ln2$.")],
          "Differentiate component by component, then substitute $t=\\ln2$.", difficulty="medium")

    lim = Matrix([limit(sin(t) / t, t, 0), limit((1 - cos(t)) / t, t, 0)])
    assert list(lim) == [1, 0]
    B.mcq(T_VV, "What is $\\displaystyle\\lim_{t\\to0}\\left\\langle\\frac{\\sin t}{t},\\frac{1-\\cos t}{t}\\right\\rangle$?",
          chvec((1, 0), "Take each limit separately: $\\lim\\frac{\\sin t}{t}=1$, and $\\lim\\frac{1-\\cos t}{t}=0$ (by L'Hospital's Rule, $\\lim\\frac{\\sin t}{1}=0$)."),
          [chvec((0, 0), "The first component is the standard limit $\\frac{\\sin t}{t}\\to1$, not 0."),
           chvec((1, 1), "$\\frac{1-\\cos t}{t}\\to0$: the numerator approaches 0 faster than the denominator."),
           ch("The limit does not exist", "A limit of a vector-valued function exists when each component has a limit, and both do here.")],
          "The limit of a vector-valued function is the vector of the limits of its components.", difficulty="medium")

    v = Matrix([3 * t**2 - 3, 2 * t])
    assert solve(v[0], t) == [-1, 1] and v.subs(t, 1)[1] != 0 and v.subs(t, -1)[1] != 0
    B.mcq(T_VV, "A particle's velocity is $\\vec v(t)=\\langle3t^2-3,2t\\rangle$. At which times is the particle moving straight up or straight down?",
          ch("$t=-1$ and $t=1$", "The velocity is vertical when its $x$-component is 0 and its $y$-component is not: $3t^2-3=0$ gives $t=\\pm1$, and there $2t=\\pm2\\ne0$."),
          [ch("$t=0$ only", "At $t=0$ the $y$-component is 0, so the velocity is $\\langle-3,0\\rangle$, which is horizontal."),
           ch("$t=1$ only", "$3t^2-3=0$ has two solutions, $t=1$ and $t=-1$, and the $y$-component is nonzero at both."),
           ch("$t=-\\sqrt3$ and $t=\\sqrt3$", "These satisfy $t^2-3=0$. The condition is $3t^2-3=0$, that is, $t^2=1$.")],
          "Vertical motion means $x'(t)=0$ with $y'(t)\\ne0$; horizontal motion means $y'(t)=0$ with $x'(t)\\ne0$.", difficulty="hard")

    r0 = Matrix([1, -1])
    pos = r0 + Matrix([integrate(2 * t, (t, 0, 2)), integrate(3 * t**2, (t, 0, 2))])
    assert list(pos) == [5, 7]
    B.mcq(T_VV, "A particle moves with velocity $\\vec v(t)=\\langle2t,3t^2\\rangle$ and has position $\\langle1,-1\\rangle$ at $t=0$. What is its position at $t=2$?",
          chvec((5, 7), "The change in position is $\\int_0^2\\langle2t,3t^2\\rangle dt=\\langle4,8\\rangle$. Adding the initial position gives $\\langle1+4,-1+8\\rangle=\\langle5,7\\rangle$."),
          [chvec((4, 8), "This is the displacement from $t=0$ to $t=2$. The initial position $\\langle1,-1\\rangle$ must be added."),
           chvec((5, 8), "The initial $y$-coordinate is $-1$, so $8+(-1)=7$."),
           chvec((4, 12), "This evaluates the velocity at $t=2$. Position needs the integral, not the velocity.")],
          "Position at time $t$ is the initial position plus the integral of velocity: $\\vec r(t)=\\vec r(0)+\\int_0^t\\vec v(s)\\,ds$.", difficulty="hard")

    r = Matrix([cos(2 * t), sin(2 * t)])
    a = r.diff(t, 2)
    assert simplify(a.norm() - 4) == 0 and simplify(r.diff(t).norm() - 2) == 0
    B.mcq(T_VV, "A particle's position is $\\vec r(t)=\\langle\\cos2t,\\sin2t\\rangle$. What is the magnitude of its acceleration?",
          ch(4, "$\\vec a=\\vec r\\,''=\\langle-4\\cos2t,-4\\sin2t\\rangle$, whose magnitude is $4\\sqrt{\\cos^22t+\\sin^22t}=4$."),
          [ch(2, "2 is the particle's speed, the magnitude of the velocity $\\langle-2\\sin2t,2\\cos2t\\rangle$."),
           ch(1, "1 is the magnitude of the position vector, the radius of the circle."),
           ch(8, "Each derivative of $\\cos2t$ multiplies by 2, so two derivatives multiply by $2^2=4$, not 8.")],
          "Differentiate twice, then take the magnitude. Each derivative of $\\cos2t$ or $\\sin2t$ brings out a factor of 2.", difficulty="hard")

    # ------------------------------------------------------------ motion in the plane
    v = Matrix([2 * t, t**2 - 1])
    assert simplify(v.norm() ** 2 - (t**2 + 1) ** 2) == 0
    B.mcq(T_MP, "A particle moves in the plane with velocity $\\vec v(t)=\\langle2t,t^2-1\\rangle$ for $t\\ge0$. What is the particle's speed at $t=2$?",
          ch(5, "Speed $=\\sqrt{(2t)^2+(t^2-1)^2}=\\sqrt{4t^2+t^4-2t^2+1}=t^2+1$, which is 5 at $t=2$. (Directly: $\\sqrt{4^2+3^2}=5$.)"),
          [ch(7, "This adds the absolute values of the components, $4+3$."),
           ch(25, "This is the sum of squares. Speed is its square root."),
           ch(sqrt(3), "At $t=2$ the components are $\\langle4,3\\rangle$, not $\\langle2,1\\rangle$.")],
          "Evaluate the velocity components first, then find the length of the vector.", difficulty="easy")

    v = Matrix([t**2 - 4, t])
    a = v.diff(t)
    dot = (v.T * a)[0].subs(t, 1)
    assert dot == -5
    B.mcq(T_MP, "A particle's velocity is $\\vec v(t)=\\langle t^2-4,t\\rangle$. At $t=1$, is the particle speeding up or slowing down?",
          ch("Slowing down, because $\\vec v\\cdot\\vec a<0$", "At $t=1$: $\\vec v=\\langle-3,1\\rangle$ and $\\vec a=\\langle2t,1\\rangle=\\langle2,1\\rangle$. Then $\\vec v\\cdot\\vec a=-6+1=-5<0$, so the speed is decreasing."),
          [ch("Speeding up, because both components of the acceleration are positive", "The signs of $\\vec a$ alone do not decide this; what matters is whether $\\vec a$ points with or against $\\vec v$. The dot product is $-5$."),
           ch("Speeding up, because the $y$-component of the velocity is positive", "One component being positive does not mean the speed is increasing. Use $\\vec v\\cdot\\vec a$."),
           ch("Slowing down, because the $x$-component of the velocity is negative", "The conclusion is right, but not for this reason: a negative velocity component only says the particle is moving left. The test is $\\vec v\\cdot\\vec a<0$.")],
          "The speed increases when $\\vec v\\cdot\\vec a>0$ and decreases when $\\vec v\\cdot\\vec a<0$: the acceleration has a component along, or against, the velocity.", difficulty="medium")

    B.mcq(T_MP, "A particle's velocity is $\\vec v(t)=\\langle t-2,3-t\\rangle$ for $t\\ge0$. For which values of $t$ is the particle moving to the right and downward?",
          ch("$t>3$", "Moving right means $x'=t-2>0$, so $t>2$. Moving down means $y'=3-t<0$, so $t>3$. Both hold for $t>3$."),
          [ch("$t>2$", "For $2<t<3$ the particle is moving right but $y'=3-t>0$, so it is moving up."),
           ch("$2<t<3$", "In this interval $y'=3-t>0$: the particle is moving right and upward."),
           ch("$t<2$", "For $t<2$ the $x$-component is negative: the particle is moving left.")],
          "Right/left is the sign of $x'$; up/down is the sign of $y'$. Find where both conditions hold.", difficulty="medium")

    v = Matrix([2 * t, t**2 - 1])
    dist = integrate(t**2 + 1, (t, 0, 3))
    disp = Matrix([integrate(2 * t, (t, 0, 3)), integrate(t**2 - 1, (t, 0, 3))])
    assert dist == 12 and list(disp) == [9, 6] and simplify(disp.norm() - 3 * sqrt(13)) == 0
    B.mcq(T_MP, "A particle's velocity is $\\vec v(t)=\\langle2t,t^2-1\\rangle$ for $t\\ge0$. What is the total distance it travels from $t=0$ to $t=3$?",
          ch(12, "The speed is $\\sqrt{4t^2+(t^2-1)^2}=t^2+1$. Total distance is $\\int_0^3\\left(t^2+1\\right)dt=\\left[\\frac{t^3}{3}+t\\right]_0^3=12$."),
          [ch(3 * sqrt(13), "This is the length of the displacement vector $\\langle9,6\\rangle$, the straight-line distance between the start and the end. The path is curved, so it is longer."),
           ch(15, "This adds the components of the displacement, $9+6$."),
           ch(10, "This is the speed at $t=3$. The distance is the integral of the speed.")],
          "Distance traveled is $\\int\\sqrt{(x')^2+(y')^2}\\,dt$. Look for a perfect square under the root.", difficulty="medium")

    vx, vy = cos(t**2), sin(t)
    parts = {
        "ok": N(Integral(sqrt(vx**2 + vy**2), (t, 0, 2))),
        "sum": N(Integral(Abs(vx) + Abs(vy), (t, 0, 2))),
        "disp": N(sqrt(Integral(vx, (t, 0, 2)).evalf() ** 2 + Integral(vy, (t, 0, 2)).evalf() ** 2)),
        "speed2": N(sqrt(vx.subs(t, 2) ** 2 + vy.subs(t, 2) ** 2)),
    }
    tx = {k_: num(v_) for k_, v_ in parts.items()}
    assert len(set(tx.values())) == 4, tx
    B.mcq(T_MP, "A graphing calculator is allowed. A particle moves in the plane with velocity $\\vec v(t)=\\langle\\cos\\left(t^2\\right),\\sin t\\rangle$. To three decimal places, what total distance does it travel from $t=0$ to $t=2$?",
          ch(f"${tx['ok']}$", f"The distance is $\\int_0^2\\sqrt{{\\cos^2\\left(t^2\\right)+\\sin^2t}}\\,dt\\approx{tx['ok']}$."),
          [ch(f"${tx['sum']}$", f"This integrates $|x'|+|y'|$ ($\\approx{tx['sum']}$). Speed is $\\sqrt{{(x')^2+(y')^2}}$."),
           ch(f"${tx['disp']}$", f"This is the magnitude of the displacement ($\\approx{tx['disp']}$), the straight-line distance from start to finish, which is not the distance traveled."),
           ch(f"${tx['speed2']}$", f"This is the speed at $t=2$ ($\\approx{tx['speed2']}$), not the total distance.")],
          "Total distance is the integral of speed. Write the integral, then evaluate it numerically.", difficulty="medium")

    a = Matrix([2, 6 * t])
    v0, r0 = Matrix([1, 0]), Matrix([0, 1])
    vv = v0 + a.applyfunc(lambda e: integrate(e, (t, 0, t)))
    rr = r0 + vv.applyfunc(lambda e: integrate(e, (t, 0, t)))
    assert list(rr.subs(t, 2)) == [6, 9]
    B.mcq(T_MP, "A particle has acceleration $\\vec a(t)=\\langle2,6t\\rangle$, velocity $\\langle1,0\\rangle$ and position $\\langle0,1\\rangle$ at $t=0$. What is its position at $t=2$?",
          chvec((6, 9), "Integrating: $\\vec v=\\langle2t+1,3t^2\\rangle$. Integrating again: $\\vec r=\\langle t^2+t,t^3+1\\rangle$. At $t=2$: $\\langle6,9\\rangle$."),
          [chvec((4, 8), "This leaves out both constants: the initial velocity adds $t$ to the $x$-component and the initial position adds 1 to the $y$-component."),
           chvec((6, 8), "The initial position $\\langle0,1\\rangle$ adds 1 to the $y$-component."),
           chvec((5, 9), "This adds the initial velocity 1 to the position as a constant. The initial velocity is added to the velocity ($2t+1$), so it integrates to $t$ and contributes $+t$ to the position, not $+1$.")],
          "Integrate twice, using the initial velocity after the first integration and the initial position after the second.", difficulty="hard")

    v = Matrix([2 * t - 4, 3])
    sp = simplify(v.norm())
    assert solve(diff(v.norm() ** 2, t), t) == [2]
    B.mcq(T_MP, "A particle's velocity is $\\vec v(t)=\\langle2t-4,3\\rangle$ for $t\\ge0$. At what time is the particle's speed least?",
          ch(2, "Speed$^2=(2t-4)^2+9$ is smallest when $2t-4=0$, that is, at $t=2$, where the speed is 3."),
          [ch(0, "At $t=0$ the speed is $\\sqrt{16+9}=5$, larger than at $t=2$."),
           ch(3, "At $t=3$ the velocity is $\\langle2,3\\rangle$ and the speed is $\\sqrt{13}\\approx3.6$, more than the speed 3 at $t=2$. The 3 here is the constant $y$-component, not a time."),
           ch(4, "At $t=4$ the $x$-component is $4$ and the speed is 5, the same as at $t=0$.")],
          "Minimize the speed by minimizing its square: here only the first component varies.", difficulty="hard")

    v = Matrix([exp(t) * cos(t), exp(t) * sin(t)])
    assert simplify(v.norm() - exp(t)) == 0
    B.mcq(T_MP, "A particle's velocity is $\\vec v(t)=\\langle e^t\\cos t,e^t\\sin t\\rangle$. What is the total distance it travels from $t=0$ to $t=\\ln3$?",
          ch(2, "The speed is $\\sqrt{e^{2t}\\cos^2t+e^{2t}\\sin^2t}=e^t$. Then $\\int_0^{\\ln3}e^t\\,dt=3-1=2$."),
          [ch(3, "This is the speed at $t=\\ln3$, $e^{\\ln3}$. Distance is the integral of speed; the lower limit contributes $-1$."),
           ch(log(3), "This is the length of the time interval."),
           ch(4, "This adds the values at the endpoints instead of subtracting: $e^{\\ln3}+e^0=4$.")],
          "Speed simplifies to $e^t$ because $\\cos^2t+\\sin^2t=1$.", difficulty="hard")

    v = Matrix([-3 * sin(t), 3 * cos(t)])
    a = v.diff(t)
    assert simplify((v.T * a)[0]) == 0 and simplify(v.norm() - 3) == 0
    B.mcq(T_MP, "A particle's velocity is $\\vec v(t)=\\langle-3\\sin t,3\\cos t\\rangle$. Which statement is true for all $t$?",
          ch("The speed is constant, even though the acceleration is never zero", "The speed is $3\\sqrt{\\sin^2t+\\cos^2t}=3$. The acceleration $\\langle-3\\cos t,-3\\sin t\\rangle$ has magnitude 3, and $\\vec v\\cdot\\vec a=9\\sin t\\cos t-9\\sin t\\cos t=0$: it changes the direction of motion but not the speed."),
          [ch("The speed is constant, so the acceleration is zero", "Constant speed does not imply zero acceleration. Acceleration also measures a change in direction."),
           ch("The speed is increasing, because the acceleration is never zero", "The acceleration is perpendicular to the velocity, so it does not change the speed."),
           ch("The particle moves along a straight line at constant speed", "A straight-line path at constant velocity would have zero acceleration. Here $\\vec a\\ne\\vec 0$ and the particle moves on a circle.")],
          "Compute $\\vec v\\cdot\\vec a$. When it is zero for all $t$, the speed does not change.", difficulty="hard")
