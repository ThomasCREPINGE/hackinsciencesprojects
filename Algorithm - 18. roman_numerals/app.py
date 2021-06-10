
roman_numerals = {
	1: "I",
	5: "V",
	10: "X",
	50: "L",
	100: "C",
	500: "D",
	1000: "M"
}

def getRomanDigit(digit, powerOfTen):
	
	if powerOfTen == 1000:
		return "".join([roman_numerals[powerOfTen] for i in range(digit)])
	
	if digit < 4:
		return "".join([roman_numerals[powerOfTen] for i in range(digit)])
	elif digit < 5:
		return roman_numerals[powerOfTen] + roman_numerals[5 * powerOfTen]
	elif digit < 9:
		return roman_numerals[5 * powerOfTen] + "".join([roman_numerals[powerOfTen] for i in range(digit - 5)])
	elif digit == 9:
		return roman_numerals[powerOfTen] + roman_numerals[10 * powerOfTen]

def getRomanNumeral(number, powerOfTen):
	
	if powerOfTen == 0:
		return ""
	
	quotient = int(number / powerOfTen)
	remain = number % powerOfTen
	
	if number == 0:
		return ""
	elif quotient == 0:
		return "" + getRomanNumeral(remain, int(powerOfTen / 10))
	else:
		return getRomanDigit(quotient, powerOfTen) + getRomanNumeral(remain, int(powerOfTen / 10))

def to_roman_numeral(number):

	return getRomanNumeral(number, 1000)

if __name__ == "__main__":

	assert to_roman_numeral(1000) == "M"
	print(to_roman_numeral(1000))
	
	assert to_roman_numeral(3000) == "MMM"
	print(to_roman_numeral(3000))
	
	assert to_roman_numeral(3200) == "MMMCC"
	print(to_roman_numeral(3200))
	
	assert to_roman_numeral(3210) == "MMMCCX"
	print(to_roman_numeral(3210))
	
	assert to_roman_numeral(3213) == "MMMCCXIII"
	print(to_roman_numeral(3213))
	
	assert to_roman_numeral(213) == "CCXIII"
	print(to_roman_numeral(213))
	
	assert to_roman_numeral(13) == "XIII"
	print(to_roman_numeral(13))
	
	assert to_roman_numeral(3) == "III"
	print(to_roman_numeral(3))

	assert to_roman_numeral(4) == "IV"
	print(to_roman_numeral(4))
	
	assert to_roman_numeral(5) == "V"
	print(to_roman_numeral(5))
	
	assert to_roman_numeral(19) == "XIX"
	print(to_roman_numeral(19))
	
	assert to_roman_numeral(44) == "XLIV"
	print(to_roman_numeral(44))
	
	assert to_roman_numeral(78) == "LXXVIII"
	print(to_roman_numeral(78))
	
	assert to_roman_numeral(99) == "XCIX"
	print(to_roman_numeral(99))
