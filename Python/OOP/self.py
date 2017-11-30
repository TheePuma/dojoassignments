class User(object):
	def __init__(self, name, email):
		super(User, self).__init__()
		self.name = name
		self.email = email
		self.logged = False
user1 = User('blaine prather','blaine@blaine.com')
print(user1.name)
print(user1.logged)
print(user1.email)