import random
'''
print('ready??')
time.sleep(1)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')`
time.sleep(1)
'''
def hangman():

	def random_line(fname):
		lines = open(fname).read().splitlines()
		return random.choice(lines)
	
	word = "church"
	#random_line("words.txt")
	
	
	'''
	def hangman(life):
		with open('ASCIIART/' + str(life) + '.txt', 'r') as f:
			for line in f:
				print(line.rstrip())'''
	
	
	
	print(str(len(str(word))) + " letters")
	
	lives = 8
	
	end = False
	
	blanks = []
	for i in range(len(word)):
		blanks.append("_")
	
	def life(arg):
		with open('ASCIIART/' + str(arg) + '.txt', 'r') as f:
				for line in f:
					print(line.rstrip())
		if lives == 0:
			print("Game over!")
			end == True
		else:
			print("Try again!")
		
	def guessType():
		global word
		global lives
		global end
	
		guess = input("guess: ")
	
		if len(guess) == len(word) and guess == word:
			print("congrats!")
			end = not end
	
			
		if len(guess) == len(word) and guess != word:
			lives -= 1
			life(lives)
	
		if len(guess) == 1 and guess in word:
			place = 0
			for i in range(len(word)):
				if guess == word[place]:	
					blanks[place] = guess
				place += 1
	
			print(*blanks)
			
		if len(guess) == 1 and guess not in word:
	 
			lives -= 1
			life(lives)
		
		a = ' '.join(str(x) for x in blanks)
		b = ' '.join(str(x) for x in word)
	
		if str(a) == str(b):
			print("good job!")
			end = not end
	
	while lives != 0:
		guessType()
		print(end)
		if end == True and lives != 0:
			print("you won!")
		if end == True and lives == 0:
			print("you lost")

hangman()