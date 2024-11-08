from xmlrpc.client import boolean

from class_node import Node
from random import randint, shuffle


def generate_nodes():
    list_of_nodes = []
    for i in range(number_of_nodes):
        initial_value = randint(0, 1)
        value.append(initial_value)
        list_of_nodes.append(Node(node_id=i, initial_value=initial_value, number_of_nodes=number_of_nodes, r=r))
    return list_of_nodes

def generate_messages(): # all nodes generate the message
    messages = []
    for i in range(len(nodes)):
        messages.append(nodes[i].generate_message())
    return messages

def generate_delivery_list(): # create random delivery list
    global drop_messages_ratio
    number_of_drops = drop_messages_ratio * number_of_nodes
    delivery_list = [0] * number_of_drops + [1] * (number_of_nodes - number_of_drops)
    shuffle(delivery_list)
    global drop_message_flag
    for i in range(len(delivery_list)):
        if delivery_list[i] == 0:
            drop_message_flag = True  # generate random delivery list
    return delivery_list

def deliver_messages(messages, delivery_list):
    for i in range(len(nodes)):
        for j in range(len(messages)):
            if delivery_list[j] != 0 and i != j: # the node can't send message to itself
                nodes[i].receive_message(messages[j])

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
    for i, row in enumerate(output_data):
        tindex, tvalue, tdecisions, tagreement, tvalidity = row


        if i != len(output_data) - 1:
            # Print the row with formatted and centered data
            print(f"│ {tindex:^5} │ {str(tvalue):^20} │ {str(tdecisions):^20} │ {"True" if tagreement == 1 else "False":^10} │ {"True" if tvalidity == 1 else "False":^8} │")
        else:
            print(f"│ {"-":^5} │ {"-":^20} │ {"-":^20} │ {str(tagreement):^10} │ {str(tvalidity):^8} │")
    print("└───────┴──────────────────────┴──────────────────────┴────────────┴──────────┘")

def check_validity():
    global false_validity_counter
    if (((all(not v for v in value) and all(not d for d in decisions)) or
            (all(value) and not drop_message_flag and all(decisions))) or
            (any(value) and not all(value))):
        return True
    else:
        false_validity_counter += 1
        return False

def check_agreement():
    global false_agreement_counter
    if all(decisions) or not any(decisions):
        return True
    else:
        false_agreement_counter += 1
        return False

def calculate_validity_agreement_per_repeats():
    validity_percentage = false_validity_counter * 1.0 / number_of_simulations
    agreement_percentage = false_agreement_counter * 1.0/ number_of_simulations
    return agreement_percentage, validity_percentage


if __name__ == "__main__":
    r = int(input("Enter number of rounds : "))
    number_of_nodes = int(input("Enter number of nodes : "))
    number_of_simulations = int(input("Enter number of simulations : "))
    drop_messages_ratio = int(input("Enter drop messages ratio (your number / 100) : "))
    output_data = []
    false_validity_counter = 0
    false_agreement_counter = 0
    for i in range(number_of_simulations):
        value = [] # value of all nodes
        nodes = generate_nodes() # generate all nodes and append all nodes initial value into the value[]
        drop_message_flag = False # flag to figure out is any message dropped or not ( uses in validity )
        message_passing_simulation() # simulate massages pass through nodes
        decisions = [] # decisions made by nodes after massages passed
        result() # append all nodes decisions into decisions[]
        validity = check_validity() # validity checker
        agreement = check_agreement() # agreement checker
        agreement_percentage, validity_percentage = calculate_validity_agreement_per_repeats() # calculate validity and agreement

        # create sample output and add this loop of simulation at the end of simulation's datas
        sample_output = (i, value, decisions, agreement, validity)
        output_data.append(sample_output)
    # the last line of data should be percentages
    last_line_sample = ("-", "-", "-", agreement_percentage, validity_percentage)
    output_data.append(last_line_sample)
    create_table()