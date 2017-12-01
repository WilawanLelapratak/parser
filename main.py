from tokenizer import Tokenizer

tokenizer = Tokenizer()

while True :
	string = input()
	tokenizer.setting(string)
	while not tokenizer.end_string() :
		result = tokenizer.next()
		print(result)