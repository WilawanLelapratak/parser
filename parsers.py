class Parser :

	def setting(self) :
		self.stack = ['S']

	def __init__(self):
		self.setting()
		self.soul = {
			'E' : {
				'id' : ['T', 'E1'],
				'int' : ['T', 'E1'],
				'+' : ['T', 'E1'],
				'-' : ['T', 'E1'],
				'/' : ['T', 'E1'],
				'(' : ['T', 'E1'],
				')' : ['T', 'E1'],
				'' : ['T', 'E1']
			}
		}
