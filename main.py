from xmlrpc.client import boolean

from class_node import Node
from random import randint


def generate_nodes():
    list_of_nodes = []
    for i in range(number_of_nodes):
        initial_value = randint(0, 1)
        value.append(initial_value)
        #initial_value = 1
        list_of_nodes.append(Node(node_id=i, initial_value=initial_value, number_of_nodes=number_of_nodes, r=r))
        print(list_of_nodes[i])
    return list_of_nodes

def generate_messages(): # all nodes generate the message
    messages = []
    for i in range(len(nodes)):
        messages.append(nodes[i].generate_message())
    return messages

def generate_delivery_list(): # create random delivery list
    delivery_list = []
    global drop_message_flag
    for i in range(len(nodes)):
        random_value = randint(0, 1)
        if random_value == 1:
            drop_message_flag = True
        delivery_list.append(random_value)  # generate random delivery list
    return delivery_list

def deliver_messages(messages, delivery_list):
    for i in range(len(nodes)):
        for j in range(len(messages)):
            if delivery_list[j] and i != j: # the node can't send message to itself
                nodes[i].receive_message(messages[j])
        print(nodes[i])

def message_passing_simulation():
   for round in range(r):
       messages = generate_messages()
       delivery_list = generate_delivery_list()
       deliver_messages(messages, delivery_list)

def result():
    for i in range(len(nodes)):
        decisions.append(nodes[i].decision_making(r))

def create_table():
    # Print the table with formatting
    print("┌───────┬──────────────────────┬──────────────────────┬────────────┬──────────┐")
    print("│ index │       value          │      decision        │ agreement  │ validity │")
    print("├───────┼──────────────────────┼──────────────────────┼────────────┼──────────┤")

    # Print each row in the table
    for row in output_data:
        tindex, tvalue, tdecisions, tagreement, tvalidity = row

        # Print the row with formatted and centered data
        print(f"│ {tindex:^5} │ {str(tvalue):^20} │ {str(tdecisions):^20} │ {"True" if tagreement == 1 else "False":^10} │ {"True" if tvalidity == 1 else "False":^8} │")

    print("└───────┴──────────────────────┴──────────────────────┴────────────┴──────────┘")

if __name__ == "__main__":
    r = int(input("Enter number of rounds : "))
    number_of_nodes = int(input("Enter number of nodes : "))
    number_of_simulations = int(input("Enter number of simulations : "))
    output_data = []
    for i in range(number_of_simulations):
        value = [] # value of all nodes
        nodes = generate_nodes() # generate all nodes and append all nodes initial value into the value[]
        drop_message_flag = False # flag to figure out is any message dropped or not ( uses in validity )
        message_passing_simulation() # simulate massages pass through nodes
        decisions = [] # decisions made by nodes after massages passed
        result() # append all nodes decisions into decisions[]
        agreement = False
        validity = False
        if all(value) or not all(value):
            agreement = True
        else:
            agreement = False
        if (not all(value) and not all(decisions)) or (all(value) and drop_message_flag):
           validity = True
        else:
            validity = False
        sample_output = (i, value, decisions, agreement, validity)

        print(value, decisions, agreement, validity)
        output_data.append(sample_output)
create_table()