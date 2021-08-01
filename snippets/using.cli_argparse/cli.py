#!python

import argparse


parser = argparse.ArgumentParser(description="This program prints recipe \
                                 consisting of the ingredients you provide.")

# parser.add_argument("-i1", "--ingredient_1")
parser.add_argument("ingredient_1")

parser.add_argument("-i2", "--ingredient_2",
                    choices=["pasta", "rice", "potato", "onion",
                             "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                    help="You need to choose only one ingredient from the list.")

# NOTE: store_true means that when "--salt" is EXPLICITLY passed in the CLI, its value is True
# otherwise, it's a hidden attribute (meaning it's created as an attribute with default value False
# when the object parser is created)
parser.add_argument("--salt", action="store_true",
# parser.add_argument("--salt", action="store_false",
                    help="Speficy if you'd like to use salt in your recipe.")

parser.add_argument("--pepper", default=False,
                    help="Change to 'True' if you'd like to use pepper in your recipe.")

args = parser.parse_args()

print(args)
print(args.ingredient_1)
print(args.ingredient_2)
# print(args.ingredient_3)
print(f"using salt? {args.salt}")
