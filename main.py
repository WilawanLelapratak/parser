from tokenizer import Tokenizer
from parsers import Parser

tokenizer = Tokenizer()
parser = Parser()

while True :
	string = input()
	tokenizer.setting(string)
	parser.setting()
	check = True
	while not tokenizer.end_string() :
		token = tokenizer.next()
		print(token)
		check = parser.parsing(token['state'])
		if not  check :
			print('reject')
			break

	if check :
		if parser.is_accept() :
			print('accept')
		else :
			print('reject')