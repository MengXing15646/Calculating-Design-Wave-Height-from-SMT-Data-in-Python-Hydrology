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
    pip install openpyxl


