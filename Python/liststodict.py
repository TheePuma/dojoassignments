name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
def make_dict(arr1, arr2):
	new_dict = {}
	newzip = zip(arr1,arr2)
	new_dict = newzip
	return new_dict
b = make_dict(name,favorite_animal)
print (b)