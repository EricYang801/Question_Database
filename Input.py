import pygsheets
import pandas as pd

#配置token及表格路徑
gc = pygsheets.authorize(service_file='./problem-database-433306-bad3b1ecbefb.json') 
sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1Z4yYJRBJJsf9wfS6z9QJbKNjbB9jEgW-EYHyBfjHkZs/edit?usp=sharing')
First_Worksheets = sheet[0] #第一張表
df = First_Worksheets.get_as_df(start='A1', index_column=0, empty_value='', include_tailing_empty=False)

#刪除第一欄
df = df.drop(df.columns[0], axis=1)
print(df)
