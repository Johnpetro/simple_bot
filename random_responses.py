import random


def random_string():
    random_list = [
        "mmmh... sikuelewi.",
        "Mmmmh.. sory provide clear information",
        "Do you mind trying to rephrase that?",
        "I'm terribly sorry, I didn't quite catch that.",
        "I can't answer that yet, please try asking something else.",
         "huelewek kiongozi."
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]
