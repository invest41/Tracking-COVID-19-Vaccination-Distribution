#1.0
import openpyxl as oex, time

#2.0
wb = oex.load_workbook('country_vaccinations.xlsx')
sheet = wb['clean_data']
fw = open('vaccine_data.csv','w')


#3.0
co, rows_copied, mcol, info_centre = 0, 0, sheet.max_column, {}
for i in sheet:
	co+=1
	row_data = [ str(i[col].value) for col in range(mcol) ]
	
	#Access Info
	#time.sleep(0.25)
	info_centre[row_data[0]] = info_centre.get(row_data[0], row_data[-1])
	
	
	if co==1: head_len = len(row_data)
	if row_data.count('None')<1 and len(row_data)==head_len:
		fw.write(','.join(row_data)+'\n')
		rows_copied += 1


#4.0
fw.close()
print(f'\n{len(info_centre)} represented countries')
print(f'Number of rows ignored: {co-rows_copied}')
