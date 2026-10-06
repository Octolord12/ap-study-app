P = "ap-phys1-u7-mcq-"

PAD = {
    P + "1": ["Mass, force, and torque, in that order of analogy", "Momentum, energy, and power, in that order of analogy", "There are no rotational analogs to linear kinematics, since rotation is unrelated"],
    P + "10": ["Because pushing near the hinge requires more force due to friction in the hinge's bearings and the weight of the door", "There is no actual difference in difficulty based on where you push the door", "Because the door is heavier near the hinge, so it resists being moved there"],
    P + "11": [None, "45° (halfway between parallel and perpendicular)", "Torque doesn't depend on the angle between them at all"],
    P + "15": ["No -- translational equilibrium always guarantees rotational equilibrium too, because zero net force means no torque", "No -- if net force is zero, the object cannot be experiencing any forces at all, so there is no torque either", "This situation is physically impossible, since zero net force always implies zero net torque"],
    P + "17": ["Center of gravity has no relationship to stability, which depends only on an object's size", "An object is more stable when its center of gravity is higher, because it is then farther from the ground", "Stability only depends on an object's mass, not on the position of its center of gravity"],
    P + "19": ["The total mass of an object, which determines how hard it is to lift", "An object's angular velocity, the rate at which its angle changes", "The force required to lift an object against gravity at constant speed through a given height"],
    P + "20": ["Object A has a greater moment of inertia, since its mass is gathered together", "Their moments of inertia are equal, since they have the same total mass and the same shape", "Moment of inertia doesn't depend on how mass is distributed about the axis, only on its total value"],
    P + "24": ["Yes -- moment of inertia is always the same for a given object, regardless of the axis chosen, since it depends only on the total mass of the object and not on how the mass is arranged", "No -- the moment of inertia about the center is larger, since the mass is concentrated near the middle of the rod", "Moment of inertia isn't defined for rods, only for disks and spheres, which have circular symmetry"],
    P + "28": ["Her angular velocity decreases, because her moment of inertia increases when her arms move inward", "Her angular velocity stays the same, since her mass doesn't change when she moves her arms", "Her angular momentum increases as she pulls her arms in, which makes her spin faster"],
    P + "30": ["They are exactly the same quantity, just with different names, and both are measured in kg·m/s", "Angular momentum conservation requires no external force, just like linear momentum, so a torque can never change it", "There is no meaningful similarity between the two conservation laws, which are unrelated principles"],
}

PADC = {
    P + "5": "$v = r\\omega$",
    P + "7": "$\\tau = rF\\sin\\theta$",
    P + "10": "Because torque is proportional to the lever arm (distance from the pivot), so the same force gives more torque farther out",
    P + "15": "Yes -- e.g., two equal and opposite forces applied at different points can have zero net force but a nonzero net torque (causing a spin)",
    P + "17": "An object is more stable (less likely to tip) when its center of gravity is lower and positioned over its base of support",
    P + "19": "An object's resistance to changes in its rotational motion, analogous to mass resisting changes in linear motion",
    P + "20": "Object B has a greater moment of inertia, since it increases with distance from the axis (I∝r² for a point mass)",
    P + "24": "No -- the moment of inertia about an end is 4 times larger than about the center ($\\frac{1}{3}ML^2$ vs $\\frac{1}{12}ML^2$), since more mass is farther from the end axis",
    P + "25": "$L = I\\omega$",
    P + "28": "Her angular velocity increases, because pulling her arms in decreases her moment of inertia, and angular momentum (L=Iω) stays constant",
    P + "30": "Both are conserved in the absence of an external influence: linear momentum needs no net external force, angular momentum needs no net external torque",
}

PADW = {}
