P = "ap-phys1-u6-mcq-"

PAD = {
    P + "1": ["Any motion that repeats over time, such as a bouncing ball, a spinning wheel or a swinging door", "Motion with a constant, unchanging force acting along the path of travel", "Motion where the velocity is always constant, so the object never speeds up or slows down"],
    P + "2": ["The spring has a constant force regardless of how far it is stretched or compressed from rest", "The mass is moving at a constant velocity as it travels back and forth along the spring", "Gravity alone causes the oscillation, with no help from the spring at all"],
    P + "7": ["Any angular displacement, no matter how large, since the restoring force is always proportional to it", "Only when the pendulum has zero mass, so that the string alone provides the restoring force", "Only when there is no gravity, so that no force acts on the bob except the string"],
    P + "8": ["A larger amplitude always results in a longer period, because the object has farther to travel", "A larger amplitude always results in a shorter period, because the object moves faster", "The relationship is different for every different amplitude, with no pattern that could be described by a formula"],
    P + "9": ["A straight line with constant slope, showing steady motion", None, None],
    P + "10": ["Acceleration always points in the same direction as the displacement from equilibrium", "Acceleration is always zero at every point of the oscillation", "There is no consistent relationship between the two quantities"],
    P + "15": ["Yes -- a heavier bob always swings with a longer period, since it has more inertia", "Yes -- a heavier bob always swings with a shorter period, since gravity pulls on it harder", "It depends on both mass and length equally, according to the period formula"],
    P + "16": ["Yes -- a larger amplitude always increases the period, since the mass travels farther", "Yes -- a larger amplitude always decreases the period, since the spring pulls harder", "It depends on amplitude only if the mass is very large, and then only slightly"],
    P + "19": ["The period increases (the oscillation becomes slower)", "The period is unaffected by the spring constant, whatever its value", "The period becomes undefined for any stiffness"],
    P + "20": ["The period decreases, since a smaller g makes the pendulum swing faster", "The period is unaffected by the change in gravity, since mass is unchanged", "The pendulum stops swinging entirely on the Moon, where there is no air to carry it"],
    P + "23": ["It continuously increases as the object oscillates", "It continuously decreases to zero as the oscillations die away", "It oscillates between positive and negative values with each cycle"],
    P + "24": ["KE is zero, and PE is at its maximum value", "Both KE and PE are zero at that position", "Both KE and PE are at their maximum simultaneously, at that position"],
    P + "30": ["Kinetic energy converts into potential energy during the downward swing, reaching maximum potential energy at the lowest point", "Both kinetic and potential energy remain constant throughout the whole swing, at every point", "All energy is lost as heat during the swing, leaving none at the bottom"],
}

PADC = {
    P + "1": "A restoring force proportional to the displacement from equilibrium and always opposite to it ($F=-kx$)",
    P + "2": "The spring's restoring force (Hooke's Law, F=-kx) is proportional to displacement from equilibrium",
    P + "7": "Small angular displacements (typically under about 15°), where the restoring force is approximately proportional to angular displacement",
    P + "8": "It doesn't depend on amplitude at all: the period is the same however large or small the oscillation is (for an ideal SHM system)",
    P + "11": "$T = 2\\pi\\sqrt{m/k}$",
    P + "13": "$T = 2\\pi\\sqrt{L/g}$",
    P + "15": "No -- mass cancels out of the period formula entirely; only length and g matter",
}

PADW = {
    "The spring has a constant force regardless of how far it is stretched or compressed from rest": "The spring has a constant force regardless of how far it is stretched or compressed from rest, however large the displacement",
    "Yes -- a larger amplitude always increases the period, since the mass travels farther": "Yes -- a larger amplitude always increases the period, since the mass travels farther on its way out",
}
