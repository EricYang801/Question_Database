import pygsheets

# 配置 token 路徑，進行授權
gc = pygsheets.authorize(
    service_file='./problem-database-433306-bad3b1ecbefb.json')

# 打開指定的 Google 試算表
sheet = gc.open_by_url(
    'https://docs.google.com/spreadsheets/d/1Z4yYJRBJJsf9wfS6z9QJbKNjbB9jEgW-EYHyBfjHkZs/edit?usp=sharing')

# 取得第一張工作表
First_Worksheets = sheet[0]

# 將第一張工作表的內容讀取成 DataFrame，從 A1 開始，並以第一列作為索引
df = First_Worksheets.get_as_df(
    start='A1', index_column=0, empty_value='', include_tailing_empty=False)

# 刪除時間戳記欄位（假設是第一欄）
df = df.drop(df.columns[0], axis=1)

""" 
# 篩選出特定題型的資料
def filter_qt(df, type):
    # 篩選出與指定題型匹配的行
    row = df[df['題型'] == type]
    # 重置索引
    row = row.reset_index(drop=True)
    return row


# 測試篩選功能並輸出不同題型的結果
print(filter_qt(df, "單選題"))
print(filter_qt(df, "多選題"))
print(filter_qt(df, "是非題"))
print(filter_qt(df, "混合題"))
"""


def random_pickup(df, num):
    # df.sample為隨機排列所有的行 frac=0.75 隨機選取75%重新排序（可從0~1）
    df_shuffled = df.sample(frac=1).reset_index(drop=True)
    df_shuffled = df_shuffled.head(num)  # 取出前 num 行
    return df_shuffled


print(random_pickup(df, 2))
