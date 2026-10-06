P = "ap-phys1-u5-mcq-"

PAD = {
    P + "3": ["Impulse equals the object's total kinetic energy at the moment of impact, measured in joules", "Impulse is always zero for any collision, since the forces cancel in pairs", "Impulse equals mass divided by time, a measure of how fast mass moves"],
    P + "8": ["They reduce the total change in momentum, so the impulse delivered to the passengers is smaller", "They increase the mass of the car, which reduces its acceleration and so the force on the occupants", "They have no real effect on the force experienced, since the momentum change is identical in every collision"],
    P + "9": ["Momentum is always zero for any isolated system, whatever its motion or the speeds of its parts", "Momentum increases over time for any system, as forces act on it", "Only kinetic energy is conserved, not momentum, in every collision"],
    P + "12": ["No -- momentum is only conserved when kinetic energy is also conserved, so an inelastic collision loses some of its momentum to heat, sound and deformation of the objects", "Momentum is never conserved in any real collision, because friction and sound always carry some of it away", "Only kinetic energy is conserved; momentum is never relevant to collisions of any kind, elastic or inelastic"],
    P + "14": ["The forces during a collision are always zero, since the objects only touch for an instant and cannot push on each other", "Momentum conservation has nothing to do with the forces involved, which are unrelated to the changes in each object's motion", "The objects don't actually exert forces on each other during a collision; they pass through each other and merely exchange velocities because of a rule about collisions that doesn't involve forces at all"],
    P + "16": ["In an elastic collision, momentum is conserved; in an inelastic collision, it is not conserved, and the objects move apart", "Elastic collisions only happen between identical objects, such as two equal steel balls", "Inelastic collisions never actually occur in nature, since all real collisions conserve kinetic energy"],
    P + "20": ["Both objects move off together at half the original velocity, sticking in a combined mass", "Both objects continue at the original velocity, unaffected by the collision, as if they passed through", "The moving object bounces straight back at the same speed, and the stationary object stays at rest, as in a collision with a wall"],
    P + "21": ["No -- only kinetic energy is conserved in elastic collisions, not momentum, which changes in every collision", "Momentum is only conserved in inelastic collisions, where the objects stick together", "Momentum conservation doesn't apply to collisions at all, since the contact forces are too short-lived"],
    P + "22": ["A perfectly elastic collision -- all kinetic energy is conserved, and the clay bounces back off the wall at its original speed", "No collision occurs since the wall doesn't move, so the clay keeps all of its kinetic energy", "The clay's kinetic energy is unaffected by sticking to the wall, because the wall is much more massive"],
    P + "23": ["Closer to elastic -- kinetic energy is almost perfectly conserved in most real collisions, apart from small losses", "It's impossible for a real collision to be either elastic or inelastic, since all of them are in between", "All real collisions are perfectly elastic by definition, since energy can never be lost"],
    P + "26": [None, "Because gravity pulls the center of mass toward the heavier object, since it attracts more strongly", "Because the less massive object doesn't count in the calculation at all, only the heavier one does"],
    P + "27": ["Both internal and external forces equally affect the center of mass's motion, in proportion to their size", "Only internal forces determine the center of mass's motion, since external forces cancel out", "The center of mass never moves, regardless of any forces acting on the system"],
    P + "28": ["A chaotic, tumbling path that mirrors the wrench's rotation, so the center of mass changes direction as it spins in the air", "A straight horizontal line, since no horizontal forces act on the wrench", "It cannot be determined for a tumbling object, since the motion is too complicated to analyze"],
    P + "30": ["It moves toward whichever skater is more massive, since that skater moves less", "It moves in the direction both skaters end up moving, following their average motion", "It accelerates continuously outward, since the push never stops"],
}

PADC = {
    P + "1": "$p = mv$",
    P + "7": "-5 m/s",
    P + "8": "They increase the time (Δt) over which the momentum changes, and since $F=\\Delta p/\\Delta t$, a longer time means a smaller average force",
    P + "12": "Yes -- momentum is conserved in ALL collisions, as long as there's no external force; kinetic energy conservation is a separate condition that holds only for elastic collisions",
    P + "14": "The forces the two objects exert on each other are internal to the system and form a Newton's Third Law pair (equal and opposite), so they cancel in the system's total momentum",
    P + "16": "In an elastic collision, kinetic energy is conserved; in an inelastic collision, some kinetic energy becomes other forms (like heat or sound)",
    P + "20": "The moving object comes to rest, and the stationary object moves off with the first object's original velocity (they exchange velocities)",
    P + "22": "A perfectly inelastic collision -- the clay's kinetic energy is converted mostly into heat and deformation as it flattens",
    P + "26": "Because the center of mass formula weights each object's position by its mass, so a larger mass pulls the average position toward itself",
    P + "27": "Only the NET EXTERNAL force on the system; internal forces (like those in a collision) don't affect the center of mass's motion",
    P + "28": "A smooth parabolic path, exactly as if it were a point-mass projectile under gravity, even though the rest of the wrench tumbles",
}

PADW = {
    "No -- momentum is only conserved when kinetic energy is also conserved, so an inelastic collision loses some of its momentum to heat, sound and deformation of the objects": "No -- momentum is only conserved when kinetic energy is also conserved, so an inelastic collision loses some of its momentum to heat, sound and deformation of the objects in the process",
    "Closer to elastic -- kinetic energy is almost perfectly conserved in most real collisions, apart from small losses": "Closer to elastic -- kinetic energy is almost perfectly conserved in most real collisions, apart from small losses during the impact",
    "A chaotic, tumbling path that mirrors the wrench's rotation, so the center of mass changes direction as it spins in the air": "A chaotic, tumbling path that mirrors the wrench's rotation, so the center of mass changes direction as it spins in the air at every moment",
}
