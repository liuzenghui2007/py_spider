import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.colors import ListedColormap

# 定义区域
regions = [
    ("维持无孔 (A)", [(0, 0), (0, 0.5), (0.5, 0.5), (0.5, 0)]),
    ("新成膜 (B)", [(0, 1), (0, 0.1), (0.1, 0.1), (0.1, 8.1), (0.1, 20), (0, 20)]),
    ("维持有膜无孔 (C)", [(0.1, 1), (10, 10), (10, 1), (0.1, 1)]),
    ("新嵌单孔 (D)", [(0.1, 8.1), (8, 8.1), (8, 20), (0.1, 20)]),
    ("维持单孔 (E)", [(10, 10), (20, 20), (20, 10), (10, 10)]),
    ("孔脱落 (F)", [(10, 0.1), (20, 0.1), (20, -8), (10, -8)]),
    ("膜破裂 (G)", [(0, -8), (0, 0.1), (20, 0.1), (20, -8)])
]

# 新增颜色定义（使用高对比度颜色）
colors = [
    '#FF0000',  # 红
    '#00FF00',  # 绿
    '#0000FF',  # 蓝
    '#FFD700',  # 金
    '#FF00FF',  # 品红
    '#FFA500',  # 橙
    '#00FFFF'   # 青
]

# 修改后的画图部分
plt.figure(figsize=(10, 10))
ax = plt.gca()

for i, (name, points) in enumerate(regions):
    poly = Polygon(points, alpha=0.3, label=name, facecolor=colors[i])
    ax.add_patch(poly)
    
    # 计算多边形的中心点
    x_coords, y_coords = zip(*points)
    centroid_x = sum(x_coords) / len(points)
    centroid_y = sum(y_coords) / len(points)
    
    # 在多边形中心添加标签
    plt.text(centroid_x, centroid_y, name, ha='center', va='center', fontsize=10, color='black')

# 设置图表范围和标签
plt.xlim(-10, 20)
plt.ylim(-10, 20)
plt.xlabel("Cap1 (x)")
plt.ylabel("Cap2 (y)")
plt.title("实验状态区域示意图")
# 修改图例字体大小
plt.legend(loc='upper right', fontsize=12)

plt.grid()
plt.show()

