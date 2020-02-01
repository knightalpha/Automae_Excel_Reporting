import pandas as pd

excel_workbook = 'studata.xlsx'
sheet1 = pd.read_excel(excel_workbook, sheet_name='sheet1')
print(sheet1.head(10))

nationality_list = []
grade_levels_list = []
topics_list = []

excel_names = sheet1['Nationality, Grade Levels, Topic']
# print(excel_names)

for name in excel_names:
    nationality_list, grade_levels_list, topics_list = name.split(' ', ' ', 1)
    nationality_list.append(nationality_list.upper())
    grade_levels_list.append(grade_levels_list.upper())
    topics_list.append(topics_list.upper())

print(nationality_list)
#
# sheet1.insert(0, "Nationality", nationality_list)
# sheet1.insert(1, "Grade Levels", grade_levels_list)
# sheet1.insert(3, 'Topic', topics_list)
# del sheet1['Nationality, Grade Levels, Topic']
# print(sheet1.head(10))
#
# Important_numbers = sheet1['Important Number']
# pd.to_numeric(Important_numbers)
# print(Important_numbers)
# Edited_Important_Numbers = Important_numbers * 2
# sheet1['Important Number'] = Edited_Important_Numbers
# print(sheet1.head(10))
#
# sheet1.to_excel("output.xlsx")
