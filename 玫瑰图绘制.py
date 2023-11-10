import numpy as np
import matplotlib.pyplot as plt

# 生成随机数据，范围为0到1
data = np.random.rand(16, 16)

# 构建角度和半径的网格
theta = np.linspace(0, 2*np.pi, 16+1)
r = np.linspace(0, 1, 16+1)

# 创建子图
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

# 绘制波高玫瑰图
cax = ax.pcolormesh(theta, r, data, cmap='viridis')
fig.colorbar(cax)

# 设置极坐标刻度
ax.set_yticklabels([])
ax.set_xticks(theta[:-1])
ax.set_xticklabels(range(16))

# 添加标题和标签
ax.set_title('16个方向的波高玫瑰图')
ax.set_xlabel('方向')
ax.set_ylabel('等级')

# 显示图形
plt.show()
