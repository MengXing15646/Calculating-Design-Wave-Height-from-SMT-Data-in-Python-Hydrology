import pandas as pd

# 读取Excel文件
df = pd.read_excel(r'C:\Users\22327\Desktop\3.xlsx')

# 找到第3列连续相同的数所在的行
duplicates = df[df.iloc[:, 2].shift(1) == df.iloc[:, 2]]

# 找到第一个重复值所在的行，并保留
first_duplicates = duplicates.drop_duplicates(subset=df.columns[2], keep='first')

# 删除其他相同数所在的行
df = df.drop(duplicates.index)

# 将结果保存为新的Excel文件
df.to_excel('new_file.xlsx', index=False)
