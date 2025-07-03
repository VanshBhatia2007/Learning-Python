import pandas as pd
x={'A':[50,10],'B':[80,20],'C':[12,30],'D':[18,40]}
df=pd.DataFrame(x)
print(df)
for (x,y) in df.items:
    print(x)
    print(y)
    
