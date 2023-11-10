# Calculating-Design-Wave-Height-from-SMT-Data-in-Python-Hydrology 使用python处理工程水文学中短期数据推求设计波高的方法
工程水文学中推求设计波高往往需要处理数以万计的数据，使用py可以快速处理这些数据<br>
这里以92-95年四年的短期数据为例，每日观测八次，大概一万一千个以上的风向波高数据，使用python处理excel数据并利用绘制散点图并拟和方程，同时使用origin pro绘制波高玫瑰图
## 1.手动将四年数据放置到同一张表中，并将所有数据从大到小排序
若数据较多，如利用长期数据推求设计波高，可以使用py中的openpyxl或者pandas库合并多个表格，这里不再赘述
## 2.使用countif函数获取波高分级数据
可以在excel中直接输入函数，但是由于excel填充柄的特性，获取的范围会跟随填充柄逐渐向下移动，数据范围缩小<br>
且数据跨度较大，从0到15，且每0.1分一级，有一百多级，需要手动输入100多个函数<br>
为此我们使用openpyxl库直接在一列中统一粘贴countif函数<br>
首先安装openpyxl库<br>
```pip
pip install openpyxl
```
在pycharm执行粘贴函数.py文件，
如下：
```python
import openpyxl
# 打开 Excel 文件
workbook = openpyxl.load_workbook(r'你的文件.xlsx')
# 选择要操作的工作表
sheet = workbook['Sheet1']
# 创建一个 Formula 对象，包含要粘贴的函数
specific_formula = '=COUNTIF(E2:E11592,"<15")-COUNTIF(E2:E11592,"<14.5")'
# 选择要操作的列（第I列，列号9）
column = 9  # 列号从1开始，所以第I列对应列号9
# 遍历指定列，将特定函数粘贴到每个单元格
for row in sheet.iter_rows(min_row=1, max_row=sheet.max_row, min_col=column, max_col=column):
    for cell in row:
        cell.value = specific_formula
# 保存更改
workbook.save('output.xlsx')
```
其会在你上传文件的第9列的每一个格内粘贴`=COUNTIF(E2:E11592,"<15")-COUNTIF(E2:E11592,"<14.5`,接着我们可以使用其他文件修改范围数字<br>
效果如下图
![](https://github.com/MengXing15646/Calculating-Design-Wave-Height-from-SMT-Data-in-Python-Hydrology/blob/master/1.png)


