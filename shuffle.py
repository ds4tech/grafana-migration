#!/usr/bin/python3
#
# Produce a different fair shuffle of a deck of cards on each run
import random

cards = [i for i in range(52)]  # cards[0] = 0, cards[51] = 51

random.seed()

# Return a shuffled copy of the array
def shuffle(cards):
  for i in range(len(cards)):
    target_index = random.randint(0, len(cards))
    try:
      cards[i] ^= cards[target_index]
      cards[target_index] ^= cards[i]
      cards[i] ^= cards[target_index]
    except:
      pass
  return cards

print(cards)
print(shuffle(cards))
