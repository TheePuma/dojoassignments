import random
def grade(num):
	if num in range (0,59):
		print("Score: ",num,"; You failed")
	elif num in range (60,69):
		print ("Score:",num,"; Your grade is D")
	elif num in range (70,79):
		print ("Score:", num,"; Your grade is C")
	elif num in range (80,89):
		print ("Score:", num,"; Your grade is B")
	elif num in range(90,100):
		print ("Score:", num,"; Your grade is A")
	else:
		print(num)
	return
grade(int(random.random()*40+60))