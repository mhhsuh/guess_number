import random
r = random.randint(1, 100)
count = 1
while True:
	count += 1    # count = count + 1
	guess = input('please key in one number between 1-100: ')
	guess = int(guess)
	print('you have guess', count, 'time')
	if r == guess:
		print("Correct")
		break
	elif r > guess:
		print('the number is bigger')
	elif r < guess:
		print('the number is smaller')