import sys

class Cell:
	def __init__(self, row, column, value):
		self.row = row
		self.column = column
		
		self.value = value
		
		self.rightNeighbour = None
		self.leftNeighbour = None
		
	def __str__(self):
		return self.value

def build_first_line():
	return [Cell(0, i, "." if i != 39 else "#") for i in range(79)]
	
def set_cell_value(cell, previousCell, binary):
	
	configuration = [
		previousCell.leftNeighbour.value,
		previousCell.value,
		previousCell.rightNeighbour.value
	]
	
	if configuration == ["#", "#", "#"]:
		cell.value = "#" if binary[0] == 1 else "."
	elif configuration == ["#", "#", "."]:
		cell.value = "#" if binary[1] == 1 else "."
	elif configuration == ["#", ".", "#"]:
		cell.value = "#" if binary[2] == 1 else "."
	elif configuration == ["#", ".", "."]:
		cell.value = "#" if binary[3] == 1 else "."
	elif configuration == [".", "#", "#"]:
		cell.value = "#" if binary[4] == 1 else "."
	elif configuration == [".", "#", "."]:
		cell.value = "#" if binary[5] == 1 else "."
	elif configuration == [".", ".", "#"]:
		cell.value = "#" if binary[6] == 1 else "."
	elif configuration == [".", ".", "."]:
		cell.value = "#" if binary[7] == 1 else "."
	
def do_cellular_automaton(n, cellularAutomaton):

	binary = [int(d) for d in (str(bin(n))[2:]).rjust(8, "0")]
	
	for i, row in enumerate(cellularAutomaton):
		if i == 0:
			continue
			
		previousRow = cellularAutomaton[i - 1]
		
		for j, cell in enumerate(row):
			set_cell_value(cell, previousRow[j], binary)
				
	for row in cellularAutomaton:
		print("".join([str(cell) for cell in row]))
	
def build_cellular_automaton():
	
	grid = [[Cell(j, i, ".") for i in range(79)] for j in range(40)]
	grid[0] = build_first_line()
	
	for y in range(len(grid)):
		for x in range(len(grid[y])):
			cell = grid[y][x]
			
			leftNeighbour = grid[y][(x - 1) % 79]
			rightNeighbour = grid[y][(x + 1) % 79]
			
			cell.leftNeighbour = leftNeighbour
			cell.rightNeighbour = rightNeighbour
			
	return grid
	
if __name__ == "__main__":

	if len(sys.argv) < 2:
		print("usage: command an_integer")
	else:
	
		n = int(sys.argv[1])
		cellularAutomaton = build_cellular_automaton()
	
		do_cellular_automaton(n, cellularAutomaton)
