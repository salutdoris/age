driving = input('請問你有沒有開過車:')
if driving != '有' and driving != '沒有':
	print('只能輸入有或沒有')
	raise SystemExit
	
age = input('請問你的年齡:')
age = int(age)

if driving == '有':
	if age >= 18:
		print('你考過駕照了')
	else:
		print('你偷開車')
elif driving == '沒有':
	if age >= 18:
		print('要不要去考駕照看看?')
	else:
		print('過幾年才可以考')