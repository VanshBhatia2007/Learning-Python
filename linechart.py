import matplotlib.pyplot as plt
y=[1,18,8,35,15]
y2=[30,20,5,25,10]
plt.plot(y,color='m',marker='8',ms='20',mec='k',mfc='r',ls='dashed',lw='10',label='india')
plt.plot(y2,color='c',marker='*',ms='20',mec='k',mfc='r',ls='dotted',lw='10',label='china')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('X & Y')

plt.legend()
plt.show()