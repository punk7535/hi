# 產生一個隨機整數1~100
#讓使用者重複輸入數字去猜
#猜對的話 印出 "終於猜對了"
#猜錯的話 要告訴他 比答案大/小

import random # 載入random

r = random.randint(1, 100)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('請猜數字: ')
	num = int(num)
	if r == num:
		print('終於猜對了')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第' , count , '次')