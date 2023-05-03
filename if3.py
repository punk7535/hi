country = input('請問您是哪國人: ')
age = input('請輸入年齡: ')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('您可以考駕照')
	else:
		print('您不可以考駕照')
elif country == '美國':
	if age >= 16:
		print('您可以考駕照')
	else:
		print('您不可以考駕照')