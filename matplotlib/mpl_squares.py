import matplotlib.pyplot as plt
squares=[1,4,6,9,16]
plt.plot(squares,linewidth=5)
#设置图标标题并给坐标轴加标签
plt.title("Squares Numbers",fontsize=24)
plt.xlabel("Value",fontsize=24)
plt.ylabel("Squares of Numbers",fontsize=24)
plt.tick_params(axis='both',labelsize=24)
plt.show()