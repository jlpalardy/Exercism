"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11

def try_yacht(rolls):
	return 50 if len(set(rolls)) == 1 else 0
def try_nums(rolls, num):
	return rolls.count(num) * num
def try_full_house(rolls):
	return sum(rolls) if len(set(rolls)) == 2 and (rolls.count(rolls[0]) == 2 or rolls.count(rolls[0] == 3)) else 0
def try_four_of_a_kind(rolls):
	rolls_kind = [4 * x for x in set(rolls) if rolls.count(x) >= 4]
	return rolls_kind[0] if rolls_kind else 0
def try_little_straight(rolls):
	return 30 if set(rolls) == set(range(1,6)) else 0
def try_big_straight(rolls):
	return 30 if set(rolls) == set(range(2,7)) else 0

def score(dice, category):
	if category == YACHT:
		return try_yacht(dice)
	if category in range(1,7):
		return try_nums(dice, category)
	if category == FULL_HOUSE:
		return try_full_house(dice)
	if category == FOUR_OF_A_KIND:
		return try_four_of_a_kind(dice)
	if category == LITTLE_STRAIGHT:
		return try_little_straight(dice)
	if category == BIG_STRAIGHT:
		return try_big_straight(dice)
	if category == CHOICE:
		return sum(dice)

