import os
import pandas as pd

data_location = '/home/flyboypk/Projects/Automate Multiple Excel Reporting/studata.csv'
desired_headings = ['Nationality', 'Place of birth', 'Semester']
df_total = pd.DataFrame(columns=desired_headings)

for file in os.listdir(data_location):  # select file from data_location
    df_file = pd.read_excel(data_location + file)
    selected_columns = df_file.loc[:, desired_headings]  # taking every row and the desired headings
    df_total = pd.concat([selected_columns, df_total], ignore_index=True)

    df_total.to_excel('Valueable Info.xlsx')