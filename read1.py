# 讀取檔案

data = []
with open('food.txt', 'r') as f:
	for line in f:
		data.append(line.strip()) # strip除掉換行符號功能

print(data)