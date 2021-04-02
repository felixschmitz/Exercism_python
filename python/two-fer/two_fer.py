import random

def two_fer(name):
    if name == ' ':
        print('One for you, one for me.')
    else:
        print('One for ' + name + ', one for me.')
    pass

names = ['Alice', 'Bob', 'Zaphod', ' ']
argument = random.choice(names)
two_fer(argument)
