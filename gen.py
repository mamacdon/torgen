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
            fields = l.split(",")
            for _ in range(int(fields[1])):
                result.append(fields[0])

    # probably unnecessary
    shuffle(result)

    return result


def get_roadtype():
    return choice(roadtypes)


def add_roadtype(name):
    return "{} {}".format(name, get_roadtype())


'''
MAIN
'''
roadtypes = build_roadtypes()

# force print into utf8 mode?
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), 'utf8', 'replace')

textgen = textgenrnn('textgenrnn_weights.hdf5')

print("\n")

for t in [0.5, 1, 1.25]:
    print("Temperature {}".format(t))
    print("--------------------------------------------------------------------")

    for _ in range(0, 5):
        list = textgen.generate(temperature=t, return_as_list=True)
        for l in list:
            print(add_roadtype(l))

    print("")
