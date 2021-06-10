
def print_line(line, lineHeight, maxHeight):

	print(("   ".join([str(value) for value in line])).center(4 * maxHeight + 1, " "))
		
def print_pascal_triangle(height):
    
	lines = [[0 for i in range(j)] for j in range(1, height + 1)]
	
	for i, line in enumerate(lines):
	
		for j, value in enumerate(line):
	
			if j == 0 or j == len(line) - 1:
				line[j] = 1
			else:
				number1 = lines[i - 1][j - 1]
				number2 = lines[i - 1][j]
				line[j] = number1 + number2
	
		print_line(line, i, height)
	
if __name__ == "__main__":
	print_pascal_triangle(10)
