from random import randint

class Node:
    def __init__(self, node_id, initial_value, r, total_number_of_nodes):
        self.id = node_id
        self.key = None
        self.initial_value = initial_value
        self.r = r
        self.number_of_nodes = total_number_of_nodes

        self.value = [None] * self.number_of_nodes # values
        self.value[node_id] = initial_value # set initial value
        self.level = [-1] * self.number_of_nodes # levels
        self.level[self.id] = 0 # set initial level

    def choose_key(self):
        self.key = randint(1, self.r) if self.id == 1 else None

    def update_state(self, message):
        value_message = message["value"]
        level_message = message["information_level"]
        self.key = message["key"] if self.key is None else self.key # updating key; if my key is none then
                                                                    # i should update my key
        self.update_value(value_message) # updating the value vector
        self.update_level(level_message) # updating the information level vector


    def update_level(self, level_message):
        for i in range(self.number_of_nodes):
            if i != self.id:
                self.level[i] =max(self.level[i], level_message[i])
            else:
                self.level[self.id] = min(level_message) + 1

    def update_value(self, value_message):
        self.value = [max(a, b if b is not None else -1) for a,b in zip(value_message,self.value)]

    def generate_message(self):
        message = {"information_level": self.level[self.id],
                   "value": self.value,
                   "key": self.key}
        return message

    def decision_making(self, round):
        if self.r == round:
            if self.key is not None and all(v == 1 for v in self.value if v is not None) and self.level[self.id] >= self.key:
                return True
            else:
                return False




    def __repr__(self):
        return f"{"value = ", self.value} {"information level = ", self.level[self.id]} {"key = ", self.key}"