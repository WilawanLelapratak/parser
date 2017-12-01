class Tokenizer :
	
	def __init__(self) :
		self.setting()
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
				'digit' : ['error', True],
				'letter' : ['error', True],
				'literator' : ['error', True],
				'white_space' : ['error', True],
				'error' : ['error', False],
				'full_stop' : ['error', True]
			},
		}

	def end_string(self) :
		return self.stop_pos >= self.end_pos

	def find_type(self, char) :
		if ord('0') <= ord(char) <= ord('9') :
			return 'digit'
		elif ord('a') <= ord(char.lower()) <= ord('z') :
			return 'letter'
		elif char in ['+', '-', '*', '/', '=', ';', '(', ')'] :
			return 'literator'
		elif char in [' ', '\t', '\n', '\r'] :
			return 'white_space'
		elif char == '.' :
			return 'full_stop'
		else :
			return 'error'

	def get_next_state(self, now, char) :
		return self.soul[now][char]

	def next(self) :
		while not self.end_string() :
			now_char = self.string[self.stop_pos]
			now_type = self.find_type(now_char)
			self.state, is_cut = self.get_next_state(self.state, now_type)
			if is_cut :
				result = self.state+ ' ' +self.string[self.start_pos:self.stop_pos]
				self.state = 'start'
				self.start_pos = self.stop_pos
				return result
			else :
				self.stop_pos += 1

		return self.state+' '+self.string[self.start_pos:self.stop_pos]

	def setting(self, string = '') :
		self.start_pos = 0
		self.stop_pos = 0
		self.end_pos = len(string)
		self.state = 'start'
		self.string = string
