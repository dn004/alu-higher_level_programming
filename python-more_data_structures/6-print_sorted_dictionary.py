#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key, value))


# for key in sorted(a_dictionary.keys()):
#   print("{}: {}".format(key, a_dictionary[key]))
