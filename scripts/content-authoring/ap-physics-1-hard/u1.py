import os, sys, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from authoring import *

g = 9.8
B = Bank("ap-physics-1", "ap-phys1", 1, "unit-1-kinematics")
T_PVA, T_REP, T_KIN, T_PRJ = ("position-velocity-acceleration", "representations-of-motion", "kinematic-equations", "projectile-motion")

# 1. dropped vs horizontally launched, speed at impact
h, v0 = 20.0, 12.0
vy = math.sqrt(2 * g * h)
speed = math.hypot(vy, v0)
assert sig(speed, 2) == "23" and sig(vy, 2) == "20" and sig(vy + v0, 2) == "32"
B.mcq(T_PRJ, "One ball is dropped from rest and a second ball is launched horizontally at 12 m/s from the same height, 20 m above level ground. Ignore air resistance ($g=9.8$ m/s^2). What is the speed of the second ball just before it lands?",
      ch("23 m/s", "The vertical motion is the same as for the dropped ball: $v_y=\\sqrt{2gh}=\\sqrt{2(9.8)(20)}\\approx19.8$ m/s. The horizontal speed stays 12 m/s. The speed is $\\sqrt{19.8^2+12^2}\\approx23$ m/s.", speed),
      [ch("20 m/s", "This is the vertical speed only, which equals the speed of the dropped ball. The launched ball also still moves horizontally at 12 m/s.", vy),
       ch("12 m/s", "This is the horizontal component, which stays constant but is not the whole velocity at impact.", v0),
       ch("32 m/s", "Speed is the magnitude of the velocity vector, not the sum of its components. The components are perpendicular, so combine them with the Pythagorean theorem.", vy + v0)],
      "The two components are independent. Find the vertical speed from the fall height, keep the horizontal speed, and combine them as perpendicular vectors.")

# 2. v-t graph: distance versus displacement
d2 = graph("t (s)", "v (m/s)", 0, 5, -5, 7,
           [{"points": [{"x": 0, "y": 6}, {"x": 3, "y": 0}, {"x": 5, "y": -4}], "color": "blue"}],
           "Velocity-time graph: a straight line from 6 m/s at t=0 to 0 at t=3 s, continuing down to -4 m/s at t=5 s.")
dist = 0.5 * 3 * 6 + 0.5 * 2 * 4
disp = 0.5 * 3 * 6 - 0.5 * 2 * 4
assert (dist, disp) == (13.0, 5.0)
B.mcq(T_REP, "The graph shows the velocity of an object moving along a straight line. What is the total distance the object travels from $t=0$ to $t=5$ s?",
      ch("13 m", "Areas between the graph and the time axis give displacement. From 0 to 3 s the area is $\\frac12(3)(6)=9$ m (forward). From 3 to 5 s the area is $\\frac12(2)(4)=4$ m (backward). Distance adds the sizes: $9+4=13$ m.", 13),
      [ch("5 m", "This is the net displacement, $9-4$. Distance counts the backward motion as positive.", 5),
       ch("9 m", "This is only the distance during the first 3 s. The object keeps moving (backward) during the last 2 s.", 9),
       ch("17 m", "This treats the last 2 s as a rectangle $(4)(2)=8$ plus the 9 m. The velocity changes uniformly from 0 to $-4$ m/s, so the area is a triangle.", 17)],
      "Split the graph where the velocity changes sign. Areas above the axis are forward displacement, areas below are backward displacement; distance adds their sizes.", diagram=d2)

# 3. speed at half the stopping distance
v0, a = 20.0, 4.0
dstop = v0**2 / (2 * a)
vhalf = math.sqrt(v0**2 - 2 * a * dstop / 2)
assert dstop == 50.0 and sig(vhalf, 3) == "14.1"
v_wrong_noteq = math.sqrt(v0**2 - a * dstop / 2)
B.mcq(T_KIN, "A car moving at 20 m/s brakes with a constant deceleration of 4 m/s^2 until it stops. What is the car's speed when it has covered half of its total stopping distance?",
      ch("14 m/s", "The stopping distance is $\\frac{v_0^2}{2a}=\\frac{400}{8}=50$ m. After 25 m: $v^2=v_0^2-2a\\,d=400-2(4)(25)=200$, so $v\\approx14$ m/s.", vhalf),
      [ch("10 m/s", "10 m/s is the speed after half of the stopping time (2.5 s), or half the initial speed. The car travels 37.5 m, three quarters of its stopping distance, by the time its speed has halved.", 10),
       ch("7.1 m/s", "This halves the correct 14.1 m/s. The relation is $v^2=v_0^2-2ad$, so it is the square of the speed that falls linearly with distance.", 7.1),
       ch("17 m/s", "This uses $v^2=v_0^2-ad$, dropping the factor of 2 in $v^2=v_0^2+2a\\,\\Delta x$.", v_wrong_noteq)],
      "Use $v^2=v_0^2+2a\\,\\Delta x$. The square of the speed, not the speed, changes linearly with distance.")

# 4. projectile at half its maximum height
vx, vy0 = 18.0, 24.0  # 30 m/s at 53 degrees using sin 53 = 0.8, cos 53 = 0.6
hmax = vy0**2 / (2 * g)
vy_half_sq = vy0**2 - 2 * g * hmax / 2
vhalf_h = math.sqrt(vx**2 + vy_half_sq)
assert sig(vhalf_h, 3) == "24.7" and sig(math.hypot(vx, vy0 / 2), 3) == "21.6"
B.mcq(T_PRJ, "A ball is launched from level ground at 30 m/s at an angle of $53^\\circ$ above the horizontal. Use $\\sin53^\\circ=0.8$, $\\cos53^\\circ=0.6$ and $g=9.8$ m/s^2. What is the ball's speed when it is at half of its maximum height on the way up?",
      ch("24.7 m/s", "The launch components are $v_x=18$ m/s and $v_{y0}=24$ m/s. The maximum height is $\\frac{24^2}{2g}\\approx29.4$ m. At half that height $v_y^2=24^2-2g\\left(\\frac{h_{max}}{2}\\right)=288$, so the speed is $\\sqrt{18^2+288}\\approx24.7$ m/s.", vhalf_h),
      [ch("18.0 m/s", "18 m/s is the speed at the very top, where only the horizontal component remains.", 18.0),
       ch("21.6 m/s", "This halves the vertical *velocity* (12 m/s). Half the height does not correspond to half the vertical speed, because $v_y^2$ changes linearly with height, not $v_y$.", math.hypot(vx, vy0 / 2)),
       ch("30.0 m/s", "30 m/s is the launch speed. The ball has lost kinetic energy by rising, so it is slower at half height.", 30.0)],
      "Treat the vertical motion with $v_y^2=v_{y0}^2-2g\\,\\Delta y$, then add the unchanging horizontal component as a perpendicular vector.")

# 5. range scaling for a horizontal launch from a cliff
B.mcq(T_PRJ, "A rock is thrown horizontally from the edge of a cliff and lands on level ground below. If the launch speed is doubled and everything else is unchanged, how does the horizontal distance traveled before landing change?",
      ch("It doubles", "The fall time $t=\\sqrt{2h/g}$ depends only on the height, which has not changed. The horizontal distance is $v_xt$, so doubling $v_x$ doubles it.", None),
      [ch("It quadruples", "Quadrupling applies to the range on level ground at a fixed launch angle ($R\\propto v^2$), where the flight time grows with speed. Here the fall time is fixed.", None),
       ch("It increases by a factor of $\\sqrt2$", "$\\sqrt2$ would appear if the fall time depended on $v_x$. It does not: vertical motion is independent of horizontal speed.", None),
       ch("It does not change", "The fall time does not change, but the rock moves twice as fast horizontally during that time.", None)],
      "Horizontal and vertical motions are independent. The time in the air is set by the vertical motion alone.")

# 6. river crossing
t_cross = 200 / 4
drift = 3 * t_cross
assert drift == 150 and 3 * (200 / 5) == 120
B.mcq(T_REP, "A boat that can move at 4 m/s relative to the water points straight across a river 200 m wide. The river flows downstream at 3 m/s. How far downstream from the starting point does the boat land?",
      ch("150 m", "The component of the boat's velocity across the river is 4 m/s, so crossing takes $\\frac{200}{4}=50$ s. During that time the current carries it $3\\times50=150$ m downstream.", 150),
      [ch("200 m", "200 m is the width of the river, the distance across.", 200),
       ch("250 m", "This is the length of the path along the ground $\\sqrt{200^2+150^2}$, not the distance downstream.", 250),
       ch("120 m", "This computes the crossing time with the ground speed $5$ m/s ($40$ s). The crossing time is set by the velocity component across the river, 4 m/s.", 120)],
      "The two perpendicular velocity components act independently: the cross-stream component sets the crossing time, and the current acts for that same time.")

# 7. time above a height for a ball thrown up
v0 = 19.6
t1, t2 = 1.0, 3.0
assert abs(v0 * t1 - 4.9 * t1**2 - 14.7) < 1e-9 and abs(v0 * t2 - 4.9 * t2**2 - 14.7) < 1e-9
B.mcq(T_KIN, "A ball is thrown straight up at 19.6 m/s from the ground ($g=9.8$ m/s^2). For how long is the ball above a height of 14.7 m?",
      ch("2 s", "Solve $14.7=19.6t-4.9t^2$: $t^2-4t+3=0$, so $t=1$ s (going up) and $t=3$ s (coming down). It is above 14.7 m for $3-1=2$ s.", 2),
      [ch("1 s", "1 s is the time at which the ball first reaches 14.7 m, not the time it spends above that height.", 1),
       ch("3 s", "3 s is the time at which the ball passes 14.7 m on the way down. The duration above it is the difference of the two times.", 3),
       ch("4 s", "4 s is the total time in the air ($2v_0/g$), including the time below 14.7 m.", 4)],
      "A given height is crossed twice: once rising and once falling. The time above it is the difference between the two solutions.")

# 8. x-t graph: average speed vs average velocity
d8 = graph("t (s)", "x (m)", 0, 6, 0, 10,
           [{"points": [{"x": 0, "y": 0}, {"x": 2, "y": 8}, {"x": 4, "y": 8}, {"x": 6, "y": 2}], "color": "blue"}],
           "Position-time graph: rises from 0 to 8 m by t=2 s, stays at 8 m until t=4 s, then falls to 2 m at t=6 s.")
avg_speed = (8 + 0 + 6) / 6
assert sig(avg_speed, 2) == "2.3"
B.mcq(T_REP, "The graph shows the position of an object moving along a line. What is the average speed of the object over the interval from $t=0$ to $t=6$ s?",
      ch("2.3 m/s", "The object travels 8 m forward (0 to 2 s), is at rest (2 to 4 s), then travels 6 m backward (4 to 6 s). The total distance is 14 m in 6 s, so the average speed is $\\frac{14}{6}\\approx2.3$ m/s.", avg_speed),
      [ch("0.33 m/s", "This is the average *velocity*, $\\frac{\\Delta x}{\\Delta t}=\\frac{2-0}{6}$. Average speed uses the total distance traveled, not the net change in position.", 2 / 6),
       ch("3.5 m/s", "This averages the speeds on the two moving segments (4 m/s and 3 m/s). The object also spends 2 s at rest, which must be included in the time.", 3.5),
       ch("4.0 m/s", "4 m/s is the speed during the first 2 s, the slope of the steepest segment, not the average over the whole trip.", 4.0)],
      "Slope of an $x$-$t$ graph is velocity. Average speed is total distance divided by total time.", diagram=d8)

# 9. signs of velocity and acceleration
B.mcq(T_PVA, "At one instant an object moving along a line has a velocity of $-3$ m/s and an acceleration of $+2$ m/s^2. Which statement is true at that instant?",
      ch("The object is moving in the negative direction and slowing down", "Velocity and acceleration have opposite signs, so the acceleration reduces the magnitude of the velocity. The object moves in the negative direction, and its speed is decreasing.", None),
      [ch("The object is moving in the negative direction and speeding up", "Speeding up requires velocity and acceleration to have the same sign. Here they are opposite.", None),
       ch("The object is moving in the positive direction and slowing down", "The velocity is negative, so the object is moving in the negative direction at that instant.", None),
       ch("The object's speed is constant because the acceleration is constant", "A constant acceleration does not mean constant speed. The velocity changes by $+2$ m/s each second.", None)],
      "Compare the signs of velocity and acceleration: the same sign means speeding up, opposite signs mean slowing down.")

# 10. chase: speed of the accelerating car when it catches up
a_B, vA = 4.0, 20.0
tc = 2 * vA / a_B
vB = a_B * tc
assert tc == 10 and vB == 40
B.mcq(T_KIN, "Car A passes a stationary car B at a constant speed of 20 m/s. At that instant car B begins to accelerate from rest at a constant 4 m/s^2 in the same direction. How fast is car B moving when it catches up with car A?",
      ch("40 m/s", "Equal displacements: $20t=\\frac12(4)t^2$, so $t=10$ s. Then $v_B=at=40$ m/s, twice the speed of car A.", vB),
      [ch("20 m/s", "The speeds are equal at $t=5$ s, when the cars are farthest apart. Car B catches up later, when it has covered the gap and is moving faster.", 20),
       ch("30 m/s", "This is the average of 20 m/s and 40 m/s. The catch-up speed is determined from the time of equal positions, giving 40 m/s.", 30),
       ch("10 m/s", "10 is the catch-up *time* in seconds, not the speed. The speed at that time is $at=(4)(10)=40$ m/s.", 10)],
      "Set the two displacements equal to find the time, then find car B's speed at that time. B's average speed must equal A's constant 20 m/s, so its final speed is double that.")

# 11. object released from a rising balloon
tup = 5 / g
y_top = 40 + 5**2 / (2 * g)
t_total = tup + math.sqrt(2 * y_top / g)
t_dropped = math.sqrt(2 * 40 / g)
t_down = (-5 + math.sqrt(25 + 4 * 4.9 * 40)) / (2 * 4.9)
assert sig(t_total, 3) == "3.41" and sig(t_dropped, 3) == "2.86" and sig(t_down, 3) == "2.39" and sig(tup, 2) == "0.51"
B.mcq(T_KIN, "A balloon rising at a steady 5 m/s is 40 m above the ground when a ball is released from it (the ball is not thrown, only released). Ignore air resistance ($g=9.8$ m/s^2). How long does the ball take to reach the ground?",
      ch("3.41 s", "The ball starts with an upward velocity of 5 m/s. Solve $-40=5t-4.9t^2$: $4.9t^2-5t-40=0$, so $t=\\frac{5+\\sqrt{25+784}}{9.8}\\approx3.41$ s.", t_total),
      [ch("2.86 s", "This treats the ball as dropped from rest at 40 m. The ball shares the balloon's upward velocity at release, so it rises a little first.", t_dropped),
       ch("2.39 s", "This gives the ball an initial velocity of 5 m/s *downward*. The balloon is rising, so the initial velocity is upward.", t_down),
       ch("0.51 s", "This is only the time for the ball to stop rising ($5/9.8$ s), not the time to reach the ground.", tup)],
      "The released ball keeps the balloon's velocity at the moment of release. Take up as positive, so $v_0=+5$ m/s and the displacement to the ground is $-40$ m.")

# 12. complementary launch angles
B.mcq(T_PRJ, "Two identical projectiles are launched from level ground with the same speed, one at $30^\\circ$ and one at $60^\\circ$ above the horizontal. Ignore air resistance. Which statement is correct?",
      ch("They land the same distance away, and the $60^\\circ$ projectile is in the air longer", "$R=\\frac{v^2\\sin2\\theta}{g}$ and $\\sin60^\\circ=\\sin120^\\circ$, so the ranges are equal. The $60^\\circ$ projectile has the larger vertical component, so it stays in the air longer and rises higher.", None),
      [ch("The $30^\\circ$ projectile lands farther away", "$\\sin(2\\cdot30^\\circ)=\\sin(2\\cdot60^\\circ)$, so the ranges are equal. Complementary angles give the same range.", None),
       ch("The $60^\\circ$ projectile lands farther away because it goes higher", "Height and range are different quantities. The $60^\\circ$ projectile goes higher but has a smaller horizontal speed, and the two effects cancel exactly.", None),
       ch("They are in the air for the same amount of time", "Time in the air is $\\frac{2v\\sin\\theta}{g}$, which is larger for $60^\\circ$.", None)],
      "Range depends on $\\sin2\\theta$, which is the same for complementary angles. Time of flight and maximum height depend on the vertical component $v\\sin\\theta$.")

# 13. constant acceleration from two velocity readings
a = (15 - 6) / (5 - 2)
v2 = 6.0
x_third = 0.5 * (v2 + (v2 + a * 1)) * 1
assert a == 3 and x_third == 7.5
B.mcq(T_KIN, "An object moves along a line with constant acceleration. Its velocity is 6 m/s at $t=2$ s and 15 m/s at $t=5$ s. How far does it move between $t=2$ s and $t=3$ s?",
      ch("7.5 m", "The acceleration is $\\frac{15-6}{3}=3$ m/s^2. The velocity at $t=3$ s is 9 m/s. The average velocity over that second is $\\frac{6+9}{2}=7.5$ m/s, so the displacement is 7.5 m.", 7.5),
      [ch("6 m", "6 m/s is the velocity at the *start* of the interval. The object speeds up during the second, so it moves farther than $6\\times1$ m.", 6),
       ch("9 m", "9 m/s is the velocity at the *end* of the interval. Using it for the whole second overestimates the displacement.", 9),
       ch("13.5 m", "This is the displacement from rest over 3 s, $\\frac12(3)(3^2)$, which is not the interval from 2 s to 3 s.", 13.5)],
      "With constant acceleration, the displacement over an interval is the average of the initial and final velocities times the time.")

# 14. stopping distance scales with the square of the speed
d_30 = 30 * (30 / 15) ** 2
assert d_30 == 120
B.mcq(T_KIN, "A car traveling at 15 m/s brakes with a constant deceleration and stops in 30 m. If the car were traveling at 30 m/s and braked with the same deceleration, what would its stopping distance be?",
      ch("120 m", "From $v^2=2ad$, the stopping distance is proportional to $v^2$. Doubling the speed multiplies the distance by 4: $4\\times30=120$ m.", 120),
      [ch("60 m", "This doubles the distance. The stopping distance is proportional to the square of the speed, not the speed.", 60),
       ch("90 m", "This adds 60 m (30 m for each extra 15 m/s). The relation is quadratic, not linear.", 90),
       ch("240 m", "This multiplies by 8, as if the distance were proportional to the cube of the speed.", 240)],
      "Since $v^2=2a\\,d$ with the same $a$, the stopping distance is proportional to $v^2$.")

# 15. ball thrown up from a balcony
t = (3 + math.sqrt(33)) / 2
assert sig(t, 3) == "4.37" and abs(29.4 + 14.7 * t - 4.9 * t**2) < 1e-9
t_drop = math.sqrt(2 * 29.4 / g)
B.mcq(T_KIN, "A ball is thrown straight up at 14.7 m/s from a balcony 29.4 m above the ground ($g=9.8$ m/s^2). How long is the ball in the air before it hits the ground?",
      ch("4.37 s", "Take up as positive: $-29.4=14.7t-4.9t^2$, so $t^2-3t-6=0$ and $t=\\frac{3+\\sqrt{33}}{2}\\approx4.37$ s.", t),
      [ch("3.00 s", "3 s is when the ball returns to the height of the balcony ($2v_0/g$). It then keeps falling 29.4 m to the ground.", 3.00),
       ch("2.45 s", "This is the fall time for a ball *dropped* from 29.4 m. The ball here first rises and then falls farther.", t_drop),
       ch("1.50 s", "1.5 s is the time to reach the top of the flight, not the time to reach the ground.", 1.50)],
      "Use one equation for the whole flight with a negative final displacement, and keep the positive root.")

# ------------------------------------------------------------------ FRQs
t_land = math.sqrt(2 * 44.1 / g)
assert abs(t_land - 3.0) < 1e-9
vy_land = g * t_land
spd = math.hypot(vy_land, 12)
ang = math.degrees(math.atan(vy_land / 12))
assert sig(vy_land, 3) == "29.4" and sig(spd, 3) == "31.8" and sig(ang, 3) == "67.8"
B.frq(T_PRJ,
      "A ball is launched horizontally at 12 m/s from the top of a 44.1 m cliff. Use $g=9.8$ m/s^2 and ignore air resistance.\n\n**(a)** Calculate the time for the ball to reach the ground.\n\n**(b)** Calculate the horizontal distance from the base of the cliff at which the ball lands.\n\n**(c)** Calculate the speed of the ball just before it lands, and the angle its velocity makes below the horizontal.\n\n**(d)** A second ball is dropped from rest from the top of the cliff at the instant the first ball is launched. Compare the time it takes to land with your answer to (a), and justify your answer.",
      [(1, "(a) Uses $y=\\frac12gt^2$ with the vertical motion only and finds $t=3.0$ s"),
       (1, "(b) Uses $x=v_xt=(12)(3.0)=36$ m"),
       (1, "(c) Finds the vertical speed $v_y=gt=29.4$ m/s"),
       (1, "(c) Combines the components to get a speed of about 31.8 m/s and an angle of about $67.8^\\circ$ below the horizontal"),
       (1, "(d) States that the times are equal, with the reasoning that vertical motion is independent of horizontal motion (both start with zero vertical velocity)")],
      "(a) Vertically, $44.1=\\frac12(9.8)t^2$, so $t^2=9$ and $t=3.0$ s.\n(b) $x=v_xt=(12)(3.0)=36$ m.\n(c) $v_y=gt=(9.8)(3.0)=29.4$ m/s downward and $v_x=12$ m/s. The speed is $\\sqrt{12^2+29.4^2}\\approx31.8$ m/s, directed at $\\tan^{-1}(29.4/12)\\approx67.8^\\circ$ below the horizontal.\n(d) The dropped ball lands at the same time, 3.0 s. Both balls start with zero vertical velocity and fall the same height under the same acceleration, and the horizontal velocity of the first ball does not affect its vertical motion.")

d_frq = graph("t (s)", "v (m/s)", 0, 7, -3, 7,
              [{"points": [{"x": 0, "y": 0}, {"x": 2, "y": 6}, {"x": 5, "y": 6}, {"x": 7, "y": -2}], "color": "blue"}],
              "Velocity-time graph of a cart: rises from 0 to 6 m/s at t=2 s, stays at 6 m/s until t=5 s, then falls to -2 m/s at t=7 s.")
a1 = 6 / 2
x05 = 0.5 * 2 * 6 + 3 * 6
t_turn = 5 + 6 / 4
pos_area = x05 + 0.5 * (t_turn - 5) * 6
neg_area = 0.5 * (7 - t_turn) * 2
assert (a1, x05, t_turn) == (3, 24, 6.5) and abs(pos_area - 28.5) < 1e-9 and abs(neg_area - 0.5) < 1e-9
B.frq(T_REP,
      "The graph shows the velocity of a cart moving along a straight track. The cart is at $x=-4$ m at $t=0$.\n\n**(a)** Find the cart's acceleration from $t=0$ to $t=2$ s.\n\n**(b)** Find the cart's displacement from $t=0$ to $t=5$ s.\n\n**(c)** At what time does the cart reverse its direction of motion? Show how you determined this from the graph.\n\n**(d)** Find the cart's position at $t=7$ s.\n\n**(e)** Find the total distance the cart travels from $t=0$ to $t=7$ s.",
      [(1, "(a) Uses the slope $\\frac{6-0}{2-0}=3$ m/s^2"),
       (1, "(b) Adds the triangle and rectangle areas: $6+18=24$ m"),
       (1, "(c) Finds where the line from $(5,6)$ to $(7,-2)$ crosses $v=0$: slope $-4$ m/s^2 gives $t=6.5$ s"),
       (1, "(d) Net displacement from 0 to 7 s is $28.5-0.5=28$ m, so $x=-4+28=24$ m"),
       (1, "(e) Total distance $28.5+0.5=29$ m")],
      "(a) $a=\\frac{\\Delta v}{\\Delta t}=\\frac{6-0}{2}=3$ m/s^2.\n(b) The displacement is the area under the graph: triangle $\\frac12(2)(6)=6$ m plus rectangle $(3)(6)=18$ m, so 24 m.\n(c) From $t=5$ s to $7$ s the velocity changes from $6$ to $-2$ m/s, a slope of $-4$ m/s^2. The velocity is zero at $t=5+\\frac{6}{4}=6.5$ s, where it changes sign: the cart reverses direction at 6.5 s.\n(d) From 5 s to 6.5 s the area is $\\frac12(1.5)(6)=4.5$ m (forward). From 6.5 s to 7 s the area is $\\frac12(0.5)(2)=0.5$ m (backward). The displacement from 0 to 7 s is $24+4.5-0.5=28$ m, so the position is $-4+28=24$ m.\n(e) Distance $=24+4.5+0.5=29$ m.",
      diagram=d_frq)

B.save()
B.brief()
