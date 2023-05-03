#密碼重試程式
#password = 'a123456'
#重複輸入密碼最多3次
#如果正確就印出成功
#如果不正確就印出錯誤還有幾次機會

password = 'a123456'
i = 3 # 剩餘機會
while i > 0:
	i = i - 1
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功!')
		break # 逃出迴圈
	else:		
		print('密碼錯誤!' )
		if i > 0:
			print('還有', i , '次機會')
		else:
			print('沒機會嘗試了，已封鎖帳號')