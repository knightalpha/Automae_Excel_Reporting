import pandas as pd
import openpyxl

excel_file_path = 'Employeedata1.xlsx'

df = pd.read_excel(excel_file_path)
# print(df)

split_values = df['salary'].unique()    # TO get Unique values
# print(split_values)


for value in split_values:
    df1 = df[df['salary'] == value]
    output_filename = "Salary_" + str(value) + "_Sorted.xlsx"
    df1.to_excel(output_filename, index=False)