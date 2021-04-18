import random

r = random.randint(1,100)
while True:
	Guess = input('請猜數字:')
	Guess = int(Guess)
	if Guess == r:
		print('你猜對了')
		break
	else:
		if Guess > r:
			print('錯誤,比答案大')
		else:
			print('錯誤,比答案小')
