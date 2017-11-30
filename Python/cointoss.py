import random
def cointoss():
	countt=0
	counth=0
	for num in range(0,5001):
		if random.random() > 0.5:
			counth += 1
			print("Attemt #",num,": Tossing a coin... It's heads! ... got ",counth," head(s) so far and ",countt,"tail(s) so far")
		else:
			countt += 1
			print ("Attemt #",num,": Tossing a coin... It's tails! ... got ",counth," head(s) so far and ",countt,"tail(s) so far")

cointoss()