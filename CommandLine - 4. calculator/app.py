import sys

if len(sys.argv) < 4:

	print("usage: ./solution.py a_number (an_operator +-*/%^) a_number")
else:

	try:
	
		num1 = int(sys.argv[1])
		num2 = int(sys.argv[3])
		
		op = sys.argv[2]
		
		if op == "+":
	
			print(num1 + num2)
			
		elif op == "-":
		
			print(num1 - num2)
			
		elif op == "*":
		
			print(num1 * num2)
			
		elif op == "/":
		
			try:
				print(int(num1 / num2))
			except ZeroDivisionError:
				print("input error")
				
		elif op == "%":
		
			print(num1 % num2)
			
		elif op == "^":
		
			print(num1 ** num2)
			
		else:
		
			print("input error")
		
	except ValueError:
	
		print("input error")
	
	
