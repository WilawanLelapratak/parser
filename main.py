from tokenizer import Tokenizer
from parsers import Parser

tokenizer = Tokenizer()
parser = Parser()

while True :
	string = input()
	tokenizer.setting(string)
	while not tokenizer.end_string() :
		result = tokenizer.next()
		print(result)