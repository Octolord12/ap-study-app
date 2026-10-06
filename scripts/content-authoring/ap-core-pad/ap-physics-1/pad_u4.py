P = "ap-phys1-u4-mcq-"

PAD = {
    P + "1": ["$W = Fd$, regardless of the angle between force and displacement vectors", "$W = F + d$, the sum of the force and the distance", "$W = F/d$, the force divided by the distance"],
    P + "2": ["A large positive amount, proportional to the distance walked and to the weight carried", "A large negative amount, since the person works against gravity", "It depends on the bag's mass and the speed of walking"],
    P + "5": ["The net work done on an object equals its change in potential energy alone", "Work is always zero for any moving object, since the force is balanced", "The net work done equals the object's total mechanical energy at any instant"],
    P + "8": ["Whenever the object is moving downward, since the force of gravity then points the other way", "Work can never be negative, since energy is never lost", "Only when the object's mass is negative, which cannot occur"],
    P + "13": ["Because potential energy doesn't actually exist without a reference point, so a system has no energy at all until someone chooses a level to measure from", "Because gravity doesn't act without a defined reference point, so no force exists without one", "There is no real reason -- it's simply required by convention with no physical basis behind it at all"],
    P + "14": ["$F = kx$, always in the same direction as the displacement from equilibrium", "The restoring force is constant, independent of the displacement from equilibrium, always pointing the same way", "The restoring force decreases as displacement increases from equilibrium"],
    P + "16": ["Kinetic energy alone remains constant throughout the motion", "Potential energy alone remains constant throughout the motion", "Mechanical energy is never conserved under any circumstances, even without friction"],
    P + "19": ["It simply disappears and is destroyed, since the block no longer moves and has no energy left to account for", "It is converted entirely back into potential energy stored in the floor, ready to push the block again", "It increases the block's mass by the same amount, since energy and mass are interchangeable at this scale"],
    P + "22": ["Total energy always decreases over time, as it is gradually used up by the motion of objects in the universe", "Only kinetic energy is conserved; other forms of energy don't matter for the total, so they can be ignored when accounting for the energy of a closed system", "Energy can be created but never destroyed, so the total in the universe only grows as new motion begins"],
    P + "24": ["The total amount of work done, regardless of how long it takes to do it", "The force applied to an object, measured in newtons", "The distance an object travels, measured in meters"],
    P + "29": ["Machine B, since it takes longer to do the same work, so it must be stronger", "Both machines have equal power, since they do equal work in the end", None],
}

PADC = {
    P + "1": "$W = Fd\\cos\\theta$, where θ is the angle between the force and the displacement",
    P + "9": "$PE = mgh$",
    P + "11": "$PE = \\frac{1}{2}kx^2$",
    P + "13": "Because only DIFFERENCES in potential energy (ΔPE) matter for the work done by gravity; the absolute value depends on an arbitrary choice of reference height",
    P + "19": "It is converted into heat (thermal energy) by friction -- total energy is still conserved, just in a different form",
}

PADW = {
    "The net work done equals the object's total mechanical energy at any instant": "The net work done equals the object's total mechanical energy at any instant of the motion",
    "Because potential energy doesn't actually exist without a reference point, so a system has no energy at all until someone chooses a level to measure from": "Because potential energy doesn't actually exist without a reference point, so a system has no energy at all until someone chooses a level to measure from on the ground",
    "Machine B, since it takes longer to do the same work, so it must be stronger": "Machine B, since it takes longer to do the same work, so it must be stronger than its rival",
}
