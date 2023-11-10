import pandas as pd

# 读取Excel文件
df = pd.read_excel(r'C:\Users\22327\Desktop\3.xlsx')

# 定义区间列表
intervals = [(11.4, 33.8), (33.9, 56.3), (56.4, 78.8), (78.9, 101.3), (101.4, 123.8),
             (123.9, 146.3), (146.4, 168.8), (168.9, 191.3), (191.4, 213.8),
             (213.9, 236.3), (236.4, 258.8), (258.9, 281.3), (281.4, 303.8),
             (303.9, 326.3), (326.4, 348.8)]

# 创建一个Excel文件对象
writer = pd.ExcelWriter('new_file.xlsx')

# 循环遍历每个区间
for i, interval in enumerate(intervals):
    # 选择满足区间条件的行
    filtered_rows = df[(df.iloc[:, 5] >= interval[0]) & (df.iloc[:, 5] <= interval[1])]

    # 将筛选的结果写入新的工作表
    filtered_rows.to_excel(writer, sheet_name=f'Sheet{i + 1}', index=False)

# 保存并关闭Excel文件对象
writer._save()
