from tokenizer import Tokenizer

tokenizer = Tokenizer()

while True :
	string = input()
	result = tokenizer.tokenizing(string)
	print(result)