term = [0 for i in range(1000)]

def doFibonacci(n):
    
	if n < 2:
		return 1
	
	if term[n] != 0:
		return term[n]
	else:
		term[n] = doFibonacci(n - 1) + doFibonacci(n - 2)
		return term[n]
    
def fibonacci(n):

	array = []
	
	for i in range(n):
		array.append(doFibonacci(i))

	return array
		
if __name__ == "__main__":
	assert fibonacci(0) == []
	assert fibonacci(1) == [1]
	assert fibonacci(2) == [1, 1]
	assert fibonacci(3) == [1, 1, 2]
