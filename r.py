import random

r = random.randint(1,100)
count = 0
while True:
	count += 1
	Guess = input('請猜數字:')
	Guess = int(Guess)
	if Guess == r:
		print('你猜對了')
		print('這是你猜的第',count,'次')
		break
	else:
		if Guess > r:
			print('錯誤,比答案大')
		else:
			print('錯誤,比答案小')
	print('這是你猜的第',count,'次')
