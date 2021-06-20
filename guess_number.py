import random
start = input ('please choose the start of the range: ')
end = input('please choose the end of the range: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 1
while True:
	guess = input('please key in one number between the range: ' )
	guess = int(guess)
	if guess <= end and guess >= start:
		print('you have guess', count, 'time')
		if r == guess:
			print("Correct")
			break
		elif r > guess:
			print('the number is bigger')
		elif r < guess:
			print('the number is smaller')
		print('you have counted', count, 'time')
		count += 1 # count = count + 1
	else:
		print('please key in the number within the range')