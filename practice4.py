import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
n=pd.Series(['aditya','riya','tanishka','harshita'])
e=pd.Series([69,40,50,65])
eco=pd.Series([72,75,77,78])
ip=pd.Series([69,68,67,66])
r={'name':n,'english':e,'economics':eco,'ip':ip}
df=pd.DataFrame(r)
df['perc']=df['english']+df['economics']+df['ip']/4
print(df)
x=np.arange(len(df.columns))
plt.plot(df.ip,df.perc,ls='dashed',color='k',marker='d')
plt.show()