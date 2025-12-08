from math import sqrt

input = open("input.txt").read()

class JunctionBox:
    x: int
    y: int
    z: int

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def distance_to(self, o: "JunctionBox"):
        return sqrt(
            (self.x - o.x)**2 +
            (self.y - o.y)**2 +
            (self.z - o.z)**2
        )
    
    def __repr__(self):
        return f"{self.x}-{self.y}-{self.z}"


# construct junction boxes
junction_boxes: list[JunctionBox] = []
for line in input.splitlines():
    coordstrs = line.split(",")
    junction_boxes.append(
        JunctionBox(
            int(coordstrs[0]),
            int(coordstrs[1]),
            int(coordstrs[2]),
        )
    )

# find distance between all pairs
junction_box_pairs = []
for i in range(len(junction_boxes)):
    for j in range(i+1, len(junction_boxes)):
        junction_box_pairs.append({
            "a": junction_boxes[i],
            "b": junction_boxes[j],
            "distance": junction_boxes[i].distance_to(junction_boxes[j])
        })

# connect circuits
circuits: list[set[list]] = [ set([box]) for box in junction_boxes ]
sorted_pairs = sorted(junction_box_pairs, key=lambda i: i["distance"])
for i in range(1000):
    pair = sorted_pairs[i]
    circuit_a: set = ()
    circuit_b: set = ()
    for circuit in circuits:
        if pair["a"] in circuit:
            circuit_a = circuit
        if pair["b"] in circuit:
            circuit_b = circuit
        if circuit_a and circuit_b:
            break
    
    if circuit_a != circuit_b:
        circuits.append(circuit_a.union(circuit_b))
        circuits.remove(circuit_a)
        circuits.remove(circuit_b)

sorted_circuits = sorted(circuits, key=lambda c: len(c), reverse=True)
flag = len(sorted_circuits[0]) * len(sorted_circuits[1]) * len(sorted_circuits[2])
print(flag)
