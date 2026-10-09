P = "ap-phys1-u8-mcq-"

PAD = {
    P + "1": ["Weight per unit area, measured in pascals", "Volume per unit mass, the inverse quantity", "Force per unit mass, measured in N/kg"],
    P + "5": ["Pressure is the same at every depth in a fluid, whatever its density or the depth of the container", "Pressure decreases with increasing depth, since the fluid thins out as it gets farther from the surface", "Pressure depends only on the total volume of fluid, not on depth, so a larger tank always gives more"],
    P + "7": ["Because fluid becomes denser automatically at greater depths, since gravity compresses it, which raises the pressure", "Because temperature increases with depth, and hotter fluid pushes harder", "There is no real reason -- it's simply an arbitrary rule of fluid statics"],
    P + "8": ["The wider container has greater pressure at the bottom, since it holds more total water above the bottom surface", "The narrower container has greater pressure at the bottom, since the water column is more concentrated", "It's impossible to compare pressures between differently shaped containers, since the shapes differ"],
    P + "9": ["Pressure only affects the point where a force is directly applied, and nowhere else in the fluid", "Fluids cannot transmit pressure at all, since their molecules are free to move", "Pressure decreases as it moves through a fluid, falling off with distance from the source"],
    P + "12": ["Yes -- hydraulic lifts genuinely create extra energy from nothing, because the output force is larger than the input force and nothing is lost in the fluid", "The lift produces extra energy, but only for very heavy loads, where the larger piston does more work", "Energy conservation doesn't apply to hydraulic systems, since the fluid can transfer energy freely"],
    P + "14": ["Because each wheel has its own separate, unrelated braking mechanism that the driver cannot see", "Because the car's computer calculates and sends an equal electronic signal to each wheel at the same instant the pedal is pressed", "It's a coincidence that braking force ends up equal at each wheel, caused by luck in manufacturing"],
    P + "16": ["All objects float in any fluid, regardless of density, because buoyancy always wins", "The buoyant force equals the object's own weight, always, even when the object sinks", "Buoyant force only applies to objects made of wood, since only wood is less dense than water"],
    P + "19": ["It floats on the surface, with part of it above the fluid", "It explodes, since the fluid pressure crushes it", "It experiences zero buoyant force, since it is denser"],
    P + "22": ["The object's actual mass decreases when submerged in water, since some of it dissolves away", "Gravity is weaker underwater, because the water screens the object from Earth's pull", "This is purely a psychological effect with no physical basis, caused by the water's cool temperature"],
    P + "24": ["The pressure is the same at every point along the pipe, whatever its width", "The fluid's density changes as it flows through different sections of pipe, to keep the speed fixed", "Fluid speed is always the same throughout a pipe of varying width, since the flow is steady"],
    P + "26": ["Because the fluid becomes less dense in the narrower section, so it moves faster", "Because gravity pulls the fluid faster in narrower pipes, where it falls more steeply", "There is no actual change in speed between different pipe widths, since the flow rate is set by the pump"],
    P + "27": ["Conservation of mass for a flowing fluid, relating the density to the speed", "The relationship between an object's mass and its weight, through the strength of the gravitational field at its location", "The total force acting on a submerged object, summed over its entire surface"],
    P + "29": ["Air flows slower over the top of the wing, creating higher pressure there that pushes the wing up, while the pressure under the wing is lower", "The wing's weight alone determines lift, with no role for airflow over the wing", "Lift has nothing to do with air pressure or speed, but only with the wing's angle"],
    P + "30": ["Because both equations involve exactly the same variables with no differences, so one can be substituted directly for the other in any problem", "There is no real analogy between the two -- they are unrelated concepts that happen to use some of the same letters in their formulas", "Bernoulli's Equation is only used for solid objects, not fluids, so it describes sliding blocks and rolling balls"],
}

PADC = {
    P + "5": "$P = P_0 + \\rho g h$, where $P_0$ is the surface pressure, ρ the fluid's density, and h the depth",
    P + "8": "The pressures are equal, since pressure at a given depth depends only on the fluid's density, g and depth, not on the container's shape",
    P + "9": "A pressure change applied to an enclosed fluid is transmitted equally to every point in the fluid and to the container walls",
    P + "12": "No -- force is multiplied, but the small piston must move 20 times farther than the large piston, so work input equals work output (conservation of energy)",
    P + "14": "Because the brake fluid is enclosed, and by Pascal's Principle the pressure applied at the pedal is transmitted equally to each wheel's brake piston",
    P + "22": "The buoyant force from the water partially supports the object's weight, reducing the apparent weight measured on a scale",
    P + "24": "For an incompressible fluid, the flow rate (area times speed) is the same at every point along the pipe",
    P + "26": "Because the flow rate (A×v) must stay constant (continuity), so a smaller area requires a proportionally larger speed",
    P + "27": "Conservation of energy for a flowing fluid, relating pressure, kinetic energy (speed) and potential energy (height) along a streamline",
    P + "29": "Air flows faster over the curved top of the wing than under the flatter bottom, so pressure is lower above and higher below, giving a net upward force",
    P + "30": "Because it expresses that the total energy per unit volume of a fluid (pressure + kinetic energy density + potential energy density) is constant along a streamline, just as mechanical energy is conserved for a particle",
}

PADW = {
    "It sinks, since its density is less than water's density": "It sinks, since its density is less than the density of water",
    "It sinks completely to the bottom": "It sinks completely to the bottom of the fluid's container",
}
