import requests
import pandas as pd

domain_url = 'https://od.cdc.gov.tw/eic/covid19'
response = requests.get(
    f'{domain_url}/covid19_free_rapid_antigen_test_clinics.csv')
	
with open('covid19_free_rapid_antigen_test_clinics.csv', 'wb') as file:
	file.write(response.content)
	file.close()

with open('covid19_free_rapid_antigen_test_clinics.csv', 'rb') as file:
	data = pd.read_csv(file)
	data2= data.values.tolist()
	file.close()

print('公費COVID-19家用快篩試劑(RATK)發送社區定點診所名單')
n = '查詢系統'
print('|~~~~~~%s~~~~~~|'%n.center(32))

def input_check():
	a = input('查詢縣市:')
	b = input('鄉鎮地區(不查請直接 Enter):')
	print('')

	data3 = list()
	for i in range(len(data2)):
		if data2[i][1] == a:
			data3.append(data2[i])

	if b == 'na' or b == '':
		for j in range(len(data3)):
			for i in range(1,8):
				print(data3[j][i],end=' ')
			print('')

	else:
		data4 = list()
		for i in range(len(data3)):
			if data3[i][2] == b:
				data4.append(data3[i])

		for j in range(len(data4)):
			for i in range(1,8):
				print(data4[j][i],end=' ')
			print('')

input_check()
print('')
print('')
c = input('是否繼續查詢 (是/否) :')
print('')
while c != '否':
	if c == '是':
		input_check()
		print('')
		print('')
		c = input('是否繼續查詢 (是/否) :')
		print('')
	else:
		c = input('是否繼續查詢 (是/否) :')
		print('')