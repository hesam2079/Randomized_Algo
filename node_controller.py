from class_node import Node
class Controller:
    def __init__(self, r, round):
        self.number_of_nodes = 0
        self.round = round
        self.r = r
        self.nodes = []


    def generate_node(self, r, node_id=None, initial_value=0):
        r = self.r
        if node_id is None:
            node_id = self.number_of_nodes + 1
        new_node = Node(node_id=node_id, initial_value=initial_value, r=r, total_number_of_nodes=self.number_of_nodes+1)
