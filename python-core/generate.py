# import is used to have access to libraries
# random.choice(seq) - chooses something from a given list
# from helps loads functions from a library as needed
# random.randit(range starting,range ending) - chooses from inclusive start ot end
# shuffle can shuffle a given list but does not return it

import random

cards=["Jack", "King", "Queen"]
random.shuffle(cards)
for card in cards:
    print(card)