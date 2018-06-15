import io
import sys
from functools import reduce
from textgenrnn import textgenrnn
from random import choice, shuffle

STREETS_FILE = "corpus/streets.txt"
ROADTYPES_FILE = "corpus/roadtypes.txt"

def build_roadtypes():
    """
    Return a giant list. Picking a random element from this list should select a
    street S with probability roughly equal to S's frequency distribution in STREETS_FILE.
    """
    with open(ROADTYPES_FILE) as file:
        lines = file.readlines()
        result = []

        # repeat each street type N times where N is its frequency in the file
        for l in lines:
            (type, freq) = l.split(",")
            for _ in range(int(freq)):
                result.append(type)

    # probably unnecessary
    shuffle(result)

    return result

def build_basenames():
    """
    Returns a set of basenames for roads
    """
    dict = {}
    with open(STREETS_FILE) as file:
        for line in file:
            dict[line.strip()] = True
    return dict

def get_roadtype():
    return choice(roadtypes)


def add_roadtype(name):
    return "{} {}".format(name, get_roadtype())

def generate(temp):
    """
    Wrapper that checks generated names against the base street names to avoid a direct
    regurgitation of input data.
    returns list
    """
    is_in_dict = True
    while is_in_dict:
        result = textgen.generate(temperature=temp, return_as_list=True)
        str = ' '.join(result)
        is_in_dict = basenames.get(str, False)
    return result

"""
MAIN
"""
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
