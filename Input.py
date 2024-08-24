import pygsheets

#配置token及表格路徑
gc = pygsheets.authorize(service_file='./problem-database-433306-bad3b1ecbefb.json') 
sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1Z4yYJRBJJsf9wfS6z9QJbKNjbB9jEgW-EYHyBfjHkZs/edit?usp=sharing')
First_Worksheets = sheet[0] #第一張表
df = First_Worksheets.get_as_df(start='A1', index_column=0, empty_value='', include_tailing_empty=False)

#刪除時間戳記
df = df.drop(df.columns[0], axis=1)

#篩選出題型為單選題的資料 QT = Question Type
def filter_QT(df, type):
    row = df[df['題型'] == type]
    row = row.reset_index(drop=True) #重置索引
    return row

print(filter_QT(df, "單選題"))
print(filter_QT(df, "多選題"))
print(filter_QT(df, "是非題"))
print(filter_QT(df, "混合題"))

