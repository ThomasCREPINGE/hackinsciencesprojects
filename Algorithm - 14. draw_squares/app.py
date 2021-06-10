def draw_line_1(n):
	line = "+"
	for i in range(n):
		line += "---+"
		
	return line
	
def draw_line_2(n):
	line = "|"
	for i in range(n):
		line += "   |"
		
	return line

def draw_n_squares(n):
	result = draw_line_1(n)
	for i in range(n):
		result += "\n" + draw_line_2(n)
		result += "\n" + draw_line_1(n)

	return result

if __name__ == "__main__":
	
	assert draw_n_squares(3).strip() == (
		"+---+---+---+\n"
		"|   |   |   |\n"
		"+---+---+---+\n"
		"|   |   |   |\n"
		"+---+---+---+\n"
		"|   |   |   |\n"
		"+---+---+---+"
	)

	assert draw_n_squares(5).strip() == (
		"+---+---+---+---+---+\n"
		"|   |   |   |   |   |\n"
		"+---+---+---+---+---+\n"
		"|   |   |   |   |   |\n"
		"+---+---+---+---+---+\n"
		"|   |   |   |   |   |\n"
		"+---+---+---+---+---+\n"
		"|   |   |   |   |   |\n"
		"+---+---+---+---+---+\n"
		"|   |   |   |   |   |\n"
		"+---+---+---+---+---+"
	)
