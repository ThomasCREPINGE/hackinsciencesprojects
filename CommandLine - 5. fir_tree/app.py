
import sys
import math

def getInitialLeafWidth(step):

	if step == 1:
		return 1
	else:
		return 4 + 2 * int((step - 1) / 2) + getInitialLeafWidth(step - 1)

def getLeafWidth(step, lineHeight):

	leafGrowth = 2
	
	return getInitialLeafWidth(step) + leafGrowth * (lineHeight - 1)

def getMaxLeafWidth(sizeOfTree):

	return getLeafWidth(sizeOfTree, 3 + sizeOfTree)

def drawLeaves(step, sizeOfTree):

	if sizeOfTree <= 0:
		return
	elif step > 1:
		drawLeaves(step - 1, sizeOfTree)

	for lineHeight in range(3 + step):
		
		line_string = "".join(["*" for i in range(getLeafWidth(step, lineHeight + 1))])
		
		line_string = line_string.center(getMaxLeafWidth(sizeOfTree), " ")
		
		print(line_string)
	
def drawTrunk(sizeOfTree):
	
	if sizeOfTree <= 0:
		return
		
	sizeOfTrunk = sizeOfTree
	thickness = 1 + sizeOfTree - sizeOfTree % 2
	
	for line in range(sizeOfTrunk):
	
		line_string = "".join(["|" for i in range(thickness)])
		
		line_string = line_string.center(getMaxLeafWidth(sizeOfTree), " ")
		
		print(line_string)

if len(sys.argv) < 2:
	print("usage: command sizeOfTree")
else:
	sizeOfTree = int(sys.argv[1])	
			
	drawLeaves(sizeOfTree, sizeOfTree)
	drawTrunk(sizeOfTree)
