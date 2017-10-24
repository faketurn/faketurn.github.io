# ユーザに10個の正の整数の入力を促した上, その中で最も大きな奇数の値を表示する.
# もし奇数が無かったらそれを示すメッセージを表示


import re


max_odd_num = 0

print('今から10個の数値を入力していただきます\n最も大きな奇数を最後に表示します。')
print('正の整数を入力してください。')

for i in range(10):
	while True:
		print(f'数字{i+1}/10個')
		num = input()
		if re.compile(r'[0-9]+').match(num):
			num = int(num)
			break
		else:
			print("正の整数を入力してください。")
			continue
	
	if not num % 2 == 0:
		if max_odd_num < num:
			max_odd_num = num

if max_odd_num:
	print(f'最も大きな奇数は {max_odd_num} でした。')
else:
	print("奇数が入力されませんでした")