import pandas as pd

# 读取Excel文件
df = pd.read_excel(r'C:\Users\22327\Desktop\2.xlsx')

# 检测第3列连续相同的数字并保留第一个出现的行
to_delete = []
prev_val = None
for index, row in df.iterrows():
    current_val = row[2]  # 第3列的值
    if current_val == prev_val:  # 如果当前值与前一个值相等，则需要删除当前行
        to_delete.append(index)
    else:
        prev_val = current_val

df.drop(to_delete, inplace=True)

# 重新设置索引
df.reset_index(drop=True, inplace=True)

# 保存到新的Excel文件
df.to_excel('output.xlsx', index=False)

