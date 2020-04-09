#Crypto.py web scraping

from urllib.request import urlopen
from bs4 import BeautifulSoup as soup 
from openpyxl import Workbook # save to excel file

def CheckCrypto(id='bitcoin',start='20200101',end='20200401'):

	url = f'https://coinmarketcap.com/currencies/{id}/historical-data/?start={start}&end={end}'

	webopen = urlopen(url) #open web
	page_html = webopen.read() #readfile
	webopen.close() #close web

	data = soup(page_html,'html.parser') #translate to html
	# print(data.title.text) #title page

	price = data.findAll('tr',{'class':'cmc-table-row'}) #list [row1,row2]

	# firstrow = price[0]
	# column = firstrow.findAll('td')

	result_date = []
	result_open = []
	result_close = []

	for row in price:
		column = row.findAll('td')
		result_date.append(column[0].text)
		result_open.append(column[1].text)
		result_close.append(column[4].text)

	# for i in range(1,11):
	# 	print(f'วันที่ {result_date[i]} ราคาเปิด {result_open[i]} $ ราคาปิด {result_close[i]} $')

	return (result_date,result_open,result_close)

allresult = CheckCrypto()
# CheckCrypto('xrp') # if user have paramiter 

excelFile = Workbook()
sheet = excelFile.active

header = ['Date','OpenPrice','ClosePrice']

sheet.append(header) #add title to excelfile 
# sheet.append(allresult[0]) #add list row1
# sheet.append(allresult[1]) #add list row2 
# sheet.append(allresult[2]) #add list row3

for x,y,z in zip(allresult[0],allresult[1],allresult[2]): #zip คือการเอา list , list จับคู่กัน
	sheet.append([x,y,z]) #add a 10 20 , b 20 30 , c 40 10 (in row)

excelFile.save('Crypto.xlsx') # save ('filename')






