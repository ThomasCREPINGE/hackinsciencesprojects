import textwrap
import itertools

def sidebyside(left, right, width=20):
	
	halfWidth = int((width - 1) / 2)
	
	wrappedLeft = [t.ljust(halfWidth) for t in textwrap.wrap(left, halfWidth)]
	wrappedRight = [t.ljust(halfWidth) for t in textwrap.wrap(right, halfWidth)]
	
	text = ""
	for i in range(max(len(wrappedLeft), len(wrappedRight))):
		
		if i < len(wrappedLeft):
			text += wrappedLeft[i]
		else:
			text += " ".ljust(halfWidth)
		
		text += "|"
		
		if i < len(wrappedRight):
			text += wrappedRight[i]
		else:
			text += " ".ljust(halfWidth)
		
		if i != max(len(wrappedLeft), len(wrappedRight)) - 1:
			text += "\n"

	return text


# Test your code with those values if you want (but don't submit your tests)
left = (
	"Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
	"Sed non risus. "
	"Suspendisse lectus tortor, dignissim sit amet, "
	"adipiscing nec, utilisez sed sin dolor."
)

right = (
	"Morbi venenatis, felis nec pretium euismod, "
	"est mauris finibus risus, consectetur laoreet "
	"sem enim sed arcu. Maecenas sit amet eleifend sem. "
	"Nullam ac libero metus. Praesent ac finibus nulla, vitae molestie dolor."
	" Aliquam vestibulum viverra nisl, id porta mi viverra hendrerit."
	" Ut et porta augue, et convallis ante."
)

if __name__ == "__main__":
	# sidebyside(left, right)
	print(sidebyside(left, right))
	# print(sidebyside(left, right, 50))
	# print(sidebyside(left, right, 100))
	# print(sidebyside(left, sidebyside(left, left, 50), 100))
