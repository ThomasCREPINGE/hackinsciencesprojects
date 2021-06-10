
import math

def getTotal(change, coins):
	
	total = 0
	
	for i in range(9):
		total += change[i] * coins[i]
		
	return total


def getChange(value, index, change, counter, amount, coins):
	
	change[index] = value
	
	total = getTotal(change, coins)
	remainingAmount = amount - total
	
	if index == len(coins) - 1 and total == amount:
		counter += 1
		
	if index < len(coins) - 1:
		counter = getChange(0, index + 1, change, counter, amount, coins)

	if total + coins[index] <= amount:
		if index == len(coins) - 1:
			counter = getChange(amount - total, index, change, counter, amount, coins)
		else:
			counter = getChange(value + 1, index, change, counter, amount, coins)
	else:
		change[index] = 0
		
	return counter

def changes(amount, coins):

	coins = sorted(coins, reverse=True)
	
	return getChange(0, 0, [0 for i in range(9)], 0, amount, coins)

print(changes(42, (1, 2, 5, 10, 20, 50, 100, 200, 500)))
