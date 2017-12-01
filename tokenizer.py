class Tokenizer :
	
	def __init__(self) :
		self.start_state = 'start'
		self.soul = {
			'start' : {
				'digit' : ['int', False],
				'letter' : ['id', False],
				'literator' : ['literator', False],
				'white_space' : ['white_space', False],
				'error' : ['error', False],
				'full_stop' : ['error', False]
			},
			'int' : {
				'digit' : ['int', False],
				'letter' : ['int', True],
				'literator' : ['int', True],
				'white_space' : ['int', True],
				'error' : ['int', True],
				'full_stop' : ['BReal', False]
			},
			'BReal' : {
				'digit' : ['real', False],
				'letter' : ['error', True],
				'literator' : ['error', True],
				'white_space' : ['error', True],
				'error' : ['error', True],
				'full_stop' : ['error', True]
			},
			'real' : {
				'digit' : ['real', False],
				'letter' : ['real', True],
				'literator' : ['real', True],
				'white_space' : ['real', True],
				'error' : ['real', True],
				'full_stop' : ['real', True]
			},
			'id' : {
				'digit' : ['id', False],
				'letter' : ['id', False],
				'literator' : ['id', True],
				'white_space' : ['id', True],
				'error' : ['id', True],
				'full_stop' : ['id', True]
			},
			'literator' : {
				'digit' : ['literator', True],
				'letter' : ['literator', True],
				'literator' : ['literator', True],
				'white_space' : ['literator', True],
				'error' : ['literator', True],
				'full_stop' : ['literator', True]
			},
			'white_space' : {
				'digit' : ['white_space', True],
				'letter' : ['white_space', True],
				'literator' : ['white_space', True],
				'white_space' : ['white_space', False],
				'error' : ['white_space', True],
				'full_stop' : ['white_space', True]
			},
			'error' : {
				'digit' : ['error', False],
				'letter' : ['error', False],
				'literator' : ['error', True],
				'white_space' : ['error', True],
				'error' : ['error', False],
				'full_stop' : ['error', True]
			},
		}

	def find_type(self, char) :
		if ord('0') <= ord(char) <= ord('9') :
			return 'digit'
		elif ord('a') <= ord(char.lower()) <= ord('z') :
			return 'letter'
		elif char in ['+', '-', '*', '/', '=', ';'] :
			return 'literator'
		elif char in [' ', '\t', '\n', '\r'] :
			return 'white_space'
		elif char == '.' :
			return 'full_stop'
		else :
			return 'error'