import xlrd

def DapAn():
	file_location = "./ExcelDA/DapAn.xlsx"
	wb = xlrd.open_workbook(file_location)
	sheet = wb.sheet_by_index(0)
	# print (sheet.nrows)
	# print (sheet.ncols)
	# print (sheet.cell_value(3, 1))
	data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
	# print (data)
	return data

