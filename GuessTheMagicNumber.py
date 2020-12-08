def main():

	import random
	
	random_number = random.randrange(1,101)
	correct = False
	
	while not correct:
		guess = int(input("Guess the magic number between 1 and 100: "))
		if guess == random_number:
				print(" Yes", random_number, " is the magic number. ")
				correct = True
		elif guess > random_number:
					print("Your guess is to high")
		else:
				print("Your guess is to low.")
				
	tryAgain = input("Would you like to try again?").lower()
	if tryAgain == "yes":
		main()
	else:
		exit()
		
main()

		