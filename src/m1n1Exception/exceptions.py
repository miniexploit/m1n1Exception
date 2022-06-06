class m1n1Exception(Exception):
	def __init__(self, pname, err, caller):
		self.err = err
		self.caller = caller
		super().__init__(f"{pname} failed with m1n1Exception:\n[exception]:\nwhat={self.err}\nfile={self.caller}")

# add more if you want