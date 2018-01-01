#设置散点图
import matplotlib.pyplot as plt
x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]
plt.scatter(x_values,y_values,s=40)
plt.title("Squares Numbers",fontsize=24)
plt.xlabel("Value",fontsize=24)
plt.ylabel("Squares of Numbers",fontsize=24)
plt.tick_params(axis='both',which='major',labelsize=24)
plt.axis([0,1100,1,1100000])
plt.show()