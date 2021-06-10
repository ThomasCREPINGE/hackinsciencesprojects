def encode(object):
	
	if isinstance(object, int):
		return "i" + str(object) + "e"
		
	if isinstance(object, str):
		return str(len(object)) + ":" + object
		
	if isinstance(object, list):
		return "l" + "".join([encode(item) for item in object]) + "e"
		
	if isinstance(object, dict):
		object = {key: object[key] for key in sorted(object.keys())}
		array = [str(encode(key)) + str(encode(value)) for key, value in object.items()]
		return "d" + "".join(array) + "e"
		
def bencode(object):
	return bytes(encode(object), "utf-8")
	
	
def decode(text):

	if text[0] == "i":
		number = ""
		for i, char in enumerate(text[1:]):
			if char.isdigit() or char == "-":
				number += char
			if char == "e":
				return int(number), text[i+2:]
				
	if text[0].isdigit():
		
		string = ""
		number = ""
		index_two_points = -1
		
		for i, char in enumerate(text):
			
			if char.isdigit() and index_two_points == -1:
				number += char
			elif char == ":":
				index_two_points = i
			else:
				if index_two_points > 0:
					if i < index_two_points + int(number):
						string += char
					else:
						string += char
						return string, text[i+1:]
	
	if text[0] == "l":
	
		array = []
		text = text[1:]
		while text[0] != "e":
			obj, text = decode(text)
			array.append(obj)
		return array, text[1:]
		
	if text[0] == "d":
		
		dictionary = {}
		text = text[1:]
		key = None
		while text[0] != "e":
			obj, text = decode(text)
			if key == None:
				key = obj
			else:
				dictionary[key] = obj
				key = None
		return dictionary, text[1:]

def bdecode(byte):
	
	text = str(byte)
	
	if text[0] == "b":
		text = text[2:-1]
		
	obj, text = decode(text)
	
	return obj

		
if __name__ == "__main__":

	print(bencode(0))
	print(bencode(42))
	print(bencode(-42))
	print(bencode("spam"))
	print(bencode(["spam", 42]))
	print(bencode({"foo": 42, "bar": "spam"}))
	
	print(bdecode(b'1:a'))
	print(bdecode("i42e"))
	print(bdecode("i-42e"))
	print(bdecode("4:spam"))
	
	print(bdecode("li42e4:spame"))
	print(bdecode("l4:spami-42ee"))
	print(bdecode("l4:spami42ee"))
	print(bdecode("l4:spamli42ei-42eee"))
	
	print(bdecode("b'd6:outterd5:inner5:helloee'"))
	
	print(bdecode("b'd6:outterd6:inner15:hello6:inner25:worldee'"))
