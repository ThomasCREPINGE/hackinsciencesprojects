def perfect_shuffle(deck):

	halfLength = int(len(deck) / 2)
	newDeck = [0 for i in range(len(deck))]
	
	for i in range(halfLength):
		newDeck[2 * i] = deck[i]
		newDeck[(2 * i) + 1] = deck[halfLength + i]
    
	return newDeck

if __name__ == "__main__":
	assert perfect_shuffle([1, 2, 3, 4, 5, 6]) == [1, 4, 2, 5, 3, 6]
	
	testDeck = [i for i in range(1024)]
	newTestDeck = testDeck
	for i in range(10):
		newTestDeck = perfect_shuffle(newTestDeck)
	assert newTestDeck == testDeck
