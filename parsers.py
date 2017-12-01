class Parser :

	def setting(self) :
		self.stack = ['S']

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
				'int' : ['int'],
				'real' : ['real'],
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
		else :
			self.stack = self.soul[self.stack.pop(0)][state] + self.stack
			self.parsing(state)