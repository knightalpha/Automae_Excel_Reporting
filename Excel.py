import xlrd

Excelsheet1 = 'Employeedata1.xlsx'
Excelsheet2 = 'Employeedata2.xlsx'

Book1 = xlrd.open_workbook(Excelsheet1)
Book2 = xlrd.open_workbook(Excelsheet2)

first_sheet = Book1.sheet_by_index(0)
second_sheet = Book2.sheet_by_index(0)

print(first_sheet.row(0), '\n')  # print 1st rows value

Headings = first_sheet.row_values(0)
Column2Heading = Headings[5]

print(Column2Heading)

i = 0
total = 0

for row in range(first_sheet.nrows):
    if str(first_sheet.cell(row, 1).value) == "Key Line":
        i += 1
        total = total + first_sheet.cell(row, 2).value
    else:
        pass

for row in range(second_sheet.nrows):
    if str(second_sheet.cell(row, 1).value) == "Key Line":
        i += 1
        total = total + second_sheet.cell(row, 2).value
    else:
        pass

print(i)
print(total)
