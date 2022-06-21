import random


def roll_dice(num):
	return random.randint(1, num)


def pow(base, p): 
	result = 1
	for inpow in range(p):
		result *= base
	return result


