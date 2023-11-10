import pandas as pd

# 读取原始Excel文件
excel_file = pd.ExcelFile(r'C:\Users\22327\Desktop\3.xlsx')

# 创建一个空的DataFrame来存储粘贴后的数据
new_dataframe = pd.DataFrame()

# 遍历每个工作表
for i, sheet_name in enumerate(excel_file.sheet_names):
    # 读取当前工作表的数据
    df = excel_file.parse(sheet_name)

    # 提取第9列和第10列的数据
    col_9 = df.iloc[:, 8]
    col_10 = df.iloc[:, 9]

    # 将提取的列数据合并到新的DataFrame中
    new_dataframe[f'Column {i * 2 + 1}'] = col_9
    new_dataframe[f'Column {i * 2 + 2}'] = col_10

# 将新的DataFrame保存为Excel文件
new_dataframe.to_excel("new_file.xlsx", index=False)

