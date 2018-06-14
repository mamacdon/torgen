import io
import sys
from functools import reduce
from textgenrnn import textgenrnn
from random import choice, shuffle


def build_roadtypes():
    '''
    returns giant list from which an element can be selected at random. The probability of picking
    a street S should be roughly equal to its frequency distribution from the input data
    '''
    with open("corpus/roadtypes.txt") as file:
        lines = file.readlines()
        result = []

        # repeat each street type N types where N is its frequency in the input data
        for l in lines:
            (type, freq) = l.split(",")
            for _ in range(int(freq)):
                result.append(type)

    # probably unnecessary
    shuffle(result)

    return result

def build_basenames():
    '''
    returns map of basenames
    '''
    dict = {}
    with open("corpus/streets.txt") as file:
        for line in file:
            dict[line.strip()] = True
    return dict

def get_roadtype():
    return choice(roadtypes)


def add_roadtype(name):
    return "{} {}".format(name, get_roadtype())

def generate(temp):
    '''
    Wrapper that checks generated names against the base street names to avoid regurgitation of input values
    returns list
    '''
    is_in_dict = True
    while is_in_dict:
        result = textgen.generate(temperature=temp, return_as_list=True)
        str = ' '.join(result)
        is_in_dict = basenames.get(str, False)
    return result

'''
MAIN
'''
roadtypes = build_roadtypes()
basenames = build_basenames()

# force print into utf8 mode?
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), 'utf8', 'replace')

textgen = textgenrnn('textgenrnn_weights.hdf5')

print("\n")

for t in [0.3, 0.5, 1, 1.25]:
    print("Temperature {}".format(t))
    print("--------------------------------------------------------------------")

    for _ in range(0, 5):
        list = generate(t)
        for l in list:
            print(add_roadtype(l))

    print("")
