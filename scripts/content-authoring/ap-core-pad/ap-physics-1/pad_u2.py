P = "ap-phys1-u2-mcq-"

PAD = {
    P + "1": [None, "Force equals mass times acceleration for any object", "Objects with greater mass always exert greater forces on other objects"],
    P + "2": ["Both forces act on the same object, which is why they always cancel each other out completely", "Neither force acts on any physical object, since forces are only a bookkeeping device in diagrams", "Only the heavier of the two objects experiences a force, while the lighter one feels none"],
    P + "3": ["The wall pushes back on the person with only 25 N, since the wall absorbs half", "The person's own muscles create the reaction force on the wall", "There is no reaction force since the wall doesn't move at all"],
    P + "4": ["Internal forces always add up to twice their individual value, so they double the net force on the system", "Internal forces are irrelevant and were never present, since only external forces act on any objects", "Internal forces only affect the more massive object in the system, while the lighter one feels no force from its partner at all"],
    P + "5": ["The person's muscles alone create forward motion with no external force needed, since internal forces can accelerate a body", "Gravity pulls the person forward along the ground as they walk, so the foot never needs to push", "Newton's Third Law has no relevance to walking, which depends only on the person's mass"],
    P + "6": ["All the forces that the object exerts on the other objects in its surroundings", "The object's velocity and acceleration vectors only, drawn at a single instant", "A diagram of the object's internal structure, showing its parts"],
    P + "7": ["Normal force and Weight are always equal for any object, regardless of its motion or of the surface it rests on, because they are a Third Law pair", "The table pushes exactly as hard as the book weighs by definition, unrelated to any of Newton's laws of motion", "This is a coincidence specific to books, and it would not hold for other objects on tables"],
    P + "8": ["To the left, since friction always dominates over any applied force", "There is no net force -- the box is in equilibrium and moves at constant velocity", "The net force direction cannot be determined from a free-body diagram alone"],
    P + "10": ["Two vectors: weight downward and a supporting normal force upward from the air", "Two equal and opposite vectors that cancel out completely, so there is no net force and the object floats", "No vectors at all, since the object is in the air and not touching anything"],
    P + "12": ["The full Normal force vector, drawn perpendicular to the surface", "The full Weight vector, exactly as drawn (straight down), with no resolving", "Neither force has any component along the incline, since they are drawn at right angles"],
    P + "13": ["Force equals mass times acceleration, so any net force on an object changes its motion in proportion to its mass", "For every action there is an equal and opposite reaction, acting on two different objects", "Objects always eventually come to rest due to their own inertia, even when no forces act on them at all in empty space"],
    P + "16": ["A type of force that pushes objects forward along their path of motion", "The speed at which an object naturally moves when no force acts on it", "A force that only applies to moving objects, not stationary ones, and fades with time"],
    P + "17": ["A continuously applied force in the direction of motion is required to overcome the puck's inertia", "A force equal to the puck's weight is required, directed upward from the ice", "The puck will naturally slow down and stop even without friction, since motion requires a cause"],
}

PADC = {
    P + "2": "Two different objects -- the action force acts on one object and the reaction force acts on the other",
    P + "4": "Internal forces (like the tension pulling the two boxes toward each other) cancel in pairs when the system is considered as a whole",
    P + "5": "The person's foot pushes backward on the ground, and the ground pushes forward on the foot with an equal and opposite force",
    P + "6": "All the forces acting ON a single object, drawn as vectors from the object's center",
    P + "7": "The book is in equilibrium (not accelerating), so by Newton's Second Law the net force, and thus the sum of these two vertical forces, must be zero",
    P + "13": "An object at rest stays at rest, and an object in motion stays in motion at constant velocity, unless acted on by a net external force",
}

PADW = {
    "Neither force acts on any physical object, since forces are only a bookkeeping device in diagrams": "Neither force acts on any physical object, since forces are only a bookkeeping device in diagrams drawn by physicists",
    "Internal forces only affect the more massive object in the system, while the lighter one feels no force from its partner at all": "Internal forces only affect the more massive object in the system, while the lighter one feels no force from its partner at all during the interaction",
    "All the forces that the object exerts on the other objects in its surroundings": "All the forces that the object exerts on the other objects in its surroundings around it, rather than the forces on it",
    "Normal force and Weight are always equal for any object, regardless of its motion or of the surface it rests on, because they are a Third Law pair": "Normal force and Weight are always equal for any object, regardless of its motion or of the surface it rests on, because they are a Third Law pair, so one cancels the other",
    "A continuously applied force in the direction of motion is required to overcome the puck's inertia": "A continuously applied force in the direction of motion is required to overcome the puck's inertia to keep it sliding",
    "To the left, since friction always dominates over any applied force": "To the left, since friction always dominates over any applied force on the box",
}
