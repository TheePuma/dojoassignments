def name(one, two):
	if one > two:
		print ("that didnt work")
		return False
	else:
		a = one - two
		return a
result = name(10,5)
print(result)
dictionary = {
	'hello': 'world',
	'age': 45,
	'awesome': True,
}

for value in dictionary.values():
	print(value)
print (dictionary['age'])
users = [
	{
		'name': 'blaine prather',
		'age': 24
	},
	{
		'name': 'nate dog',
		'age': 35,
	}
]

for index, user in enumerate(users):
	print ("user {} \t age: {}".format(users.name))
	for key, value in user.items():
		print('key is {}. Value is {}'.format(key, value))
quiz
b,b,a,c,c,c,