import matplotlib.pyplot as plt
populations_ages=[22,33,444,21,12,34,67,16,78,30,56,55,80]
bins=[0,10,20,30,40,50,60,70,80,90]
plt.hist(populations_ages,bins,label='number',histtype='bar',rwidth=0.8,color='#ff5d5e')
plt.xlabel('x')
plt.ylabel('y')
plt.title('histogram') #竟然不解析中文TT
plt.legend()
plt.show()