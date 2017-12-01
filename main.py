from tokenizer import Tokenizer
from parsers import Parser

tokenizer = Tokenizer()
parser = Parser()

reject_count = 0
accept_count = 0
while True :
	string = input()
	tokenizer.setting(string)
	parser.setting()
	check = True
	while not tokenizer.end_string() :
		token = tokenizer.next()
		# print(token)
		check = parser.parsing(token['state'])
		if not  check :
			print('reject')
			reject_count += 1
			break

	if check :
		if parser.is_accept() :
			print('accept')
			accept_count += 1
		else :
			print('reject')
			reject_count += 1
	print('accept: %d, reject: %d' %(accept_count, reject_count))