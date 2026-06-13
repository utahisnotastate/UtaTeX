class FluxNode:
    def __init__(self, mass, repulsion_radius, data):
        self.mass = mass
        self.repulsion_radius = repulsion_radius
        self.data = data

class GravitationalField:
    def __init__(self, canvas):
        self.canvas = canvas
        self.nodes = []

    def insert_node(self, node):
        self.nodes.append(node)

    def relax_system(self, iterations):
        pass