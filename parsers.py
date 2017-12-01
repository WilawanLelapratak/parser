class Parser :

	def setting(self) :
		self.stack = ['S', '']

	def __init__(self):
		self.setting()
		self.soul = {
			'S' : {
				'id' : ['S1', 'S'],
				'int' : [], #
				'real' : [], #
				'+' : [], #
				'-' : [], #
				'*' : [], #
				'/' : [], #
				'=' : [], #
				';' : [], #
				'(' : [], #
				')' : [], #
				'' : []
			},
			'S1' : {
				'id' : ['id', '=', 'E', ';'],
				'int' : ['error'],
				'real' : ['error'],
				'+' : ['error'],
				'-' : ['error'],
				'*' : ['error'],
				'/' : ['error'],
				'=' : ['error'], #
				';' : ['error'], #
				'(' : ['error'],
				')' : ['error'],
				'' : [] #'error'
			},
			'E' : {
				'id' : ['T', 'E1'],
				'int' : ['T', 'E1'],
				'real' : ['T', 'E1'],
				'+' : ['T', 'E1'],
				'-' : ['T', 'E1'],
				'*' : ['T', 'E1'],
				'/' : ['T', 'E1'],
				'=' : ['T', 'E1'], #
				';' : ['T', 'E1'], #
				'(' : ['T', 'E1'],
				')' : ['T', 'E1'],
				'' : ['T', 'E1']
			},
			'E1' : {
				'id' : [],
				'int' : [],
				'real' : [],
				'+' : ['+','T', 'E1'],
				'-' : ['-','T', 'E1'],
				'*' : [],
				'/' : [],
				'=' : [], #
				';' : [], #
				'(' : [],
				')' : [],
				'' : []
			},
			'T' : {
				'id' : ['F', 'T1'],
				'int' : ['F', 'T1'],
				'real' : ['F', 'T1'],
				'+' : ['F', 'T1'],
				'-' : ['F', 'T1'],
				'*' : ['F', 'T1'],
				'/' : ['F', 'T1'],
				'=' : ['F', 'T1'], #
				';' : ['F', 'T1'], #
				'(' : ['F', 'T1'],
				')' : ['F', 'T1'],
				'' : ['F', 'T1']
			},
			'T1' : {
				'id' : [],
				'int' : [],
				'real' : [],
				'+' : [],
				'-' : [],
				'*' : ['*', 'F', 'T1'],
				'/' : ['/', 'F', 'T1'],
				'=' : [], #
				';' : [], #
				'(' : [],
				')' : [],
				'' : []
			},
			'F' : {
				'id' : ['id', 'A'],
				'int' : ['int', 'B'],
				'real' : ['real', 'B'],
				'+' : ['error'],
				'-' : ['error'],
				'*' : ['error'],
				'/' : ['error'],
				'=' : ['error'], #
				';' : ['error'], #
				'(' : ['(', 'E', ')'],
				')' : ['error'],
				'' : ['error']
			},
			'B' : {
				'id' : ['id'],
				'int' : [],
				'real' : [],
				'+' : [],
				'-' : [],
				'*' : [],
				'/' : [],
				'=' : [], #
				';' : [], #
				'(' : [],
				')' : [],
				'' : []
			},
			'A' : {
				'id' : [],
				'int' : [],
				'real' : [],
				'+' : [],
				'-' : [],
				'*' : [],
				'/' : [],
				'=' : [], #
				';' : [], #
				'(' : ['(', 'E', ')'],
				')' : [],
				'' : []
			}
		}
		
	def parsing(self, state) :
		print(self.stack[0])
		print(state)
		if self.stack[0] == state :
			self.stack.pop(0)
			print(self.stack)
			return True
		else :
			head = self.stack.pop(0)
			if head not in self.soul :
				return False
			self.stack = self.soul[head][state] + self.stack
			if self.stack[0] == 'error' :
				return False
			print(self.stack)
			return self.parsing(state)

	def is_accept(self) :
		self.parsing('')
		return self.stack == []