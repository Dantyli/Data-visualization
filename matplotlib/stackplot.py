import matplotlib.pyplot as plt
days=[1,2,3,4,5]
sleeping=[7,8,6,11,7]
eatings=[2,3,4,3,1]
working=[7,8,7,2,2]
playing=[8,5,7,8,13]
plt.plot([],[],color='m',label='sleeping',lineWidth=5)
plt.plot([],[],color='c',label='eating',lineWidth=5)
plt.plot([],[],color='r',label='working',lineWidth=5)
plt.plot([],[],color='k',label='playing',lineWidth=5)
plt.stackplot(days,sleeping,eatings,working,playing,colors=['m','c','r','k'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('grph')
plt.legend()
plt.show()