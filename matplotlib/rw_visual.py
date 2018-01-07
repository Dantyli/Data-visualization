import matplotlib.pyplot as plt
from random_walk import RandomWalk
#只要程序处于活动状态，就不断模拟随机漫步
while True:
#创建实例，并将包含的点全都绘制出来
    rw=RandomWalk()
    rw.fill_walk()
    plt.figure(figsize=(10,6))
    point_numbers=list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=10)
    #隐藏x,y坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    keep_running=input('Make another walk?(y/n):')
    if keep_running=='n':
        break;
