HIDDEN_NUMBER = 3

def start_game():
	while True:
		for i in range(3):
			if i == 2:
				print ("Game Over.")
			guess = input('Guess a number between 1 and 10	')
			guess_number = int (guess)

			if 1 <= guess_number <=10:
				if guess_number == HIDDEN_NUMBER:
					print('Congrats! You got it rigth.')
					break
				else:
					print("Than's wrong.")
			else:
				print('I said, a number between 1 and 10')
start_game()