import pandas as pd

# 读取Excel文件
df = pd.read_excel(r'C:\Users\22327\Desktop\1.xlsx', header=None)

# 倒置每一列的数据
inverted_df = df.apply(lambda x: x[::-1])

# 将倒置后的数据保存为Excel文件
inverted_df.to_excel("file.xlsx", index=False, header=False)

