
import string
import random

def pwgen(length, with_digits=False, with_uppercase=False):

	if length == 0:
		return ""
	
	if not with_digits and not with_uppercase:
		return "".join([random.choice(string.ascii_lowercase) for i in range(length)])
		
	if with_digits and not with_uppercase:
		nbOfDigits = random.randrange(1, length - 1)
		pwdArray = [random.choice(string.ascii_lowercase) for i in range(length - nbOfDigits)]
		pwdArray += [str(random.choice(range(10))) for i in range(nbOfDigits)]
		random.shuffle(pwdArray)
		return "".join(pwdArray)
	
	if not with_digits and with_uppercase:
		nbOfUpper = random.randrange(1, length - 1)
		pwdArray = [random.choice(string.ascii_lowercase) for i in range(length - nbOfUpper)]
		pwdArray += [random.choice(string.ascii_uppercase) for i in range(nbOfUpper)]
		random.shuffle(pwdArray)
		return "".join(pwdArray)
		
	if with_digits and with_uppercase:
		nbOfDigits = random.randrange(1, length - 2)
		nbOfUpper = random.randrange(1, length - nbOfDigits - 1)
		pwdArray = [random.choice(string.ascii_lowercase) for i in range(length - nbOfDigits - nbOfUpper)]
		pwdArray += [random.choice(string.ascii_uppercase) for i in range(nbOfUpper)]				
		pwdArray += [str(random.choice(range(10))) for i in range(nbOfDigits)]
		random.shuffle(pwdArray)
		return "".join(pwdArray)
		
if __name__ == "__main__":
	print(pwgen(8))
	print(pwgen(8, True))
	print(pwgen(8, False, True))
	print(pwgen(8, True, True))
