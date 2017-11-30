database =[{
	'name': 'Blaine Prather',
	'age': 24,
	'birthplace': 'United States',
	'favlang': 'Python',
	},
	{
	'name': 'Michael Kravitz',
	'age': 19,
	'birthplace': 'United States',
	'favlang': 'Javascript',
	}
]
for index, user in enumerate(database):
	print("My name is {}. I am {}. I was born in the {}. I love {}.".format(user['name'],user['age'],user['birthplace'],user['favlang']))