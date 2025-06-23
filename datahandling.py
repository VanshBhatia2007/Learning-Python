import pandas as pd
name=['Shruti','Renu','Rinku','nidhi','Tinku','Vidooshi','Rohit']
marks=[80,60,89,90,78,82,99] 
stud=pd.Series(name,index=marks)
stud.name='name'
stud.index.name='marks'
print(stud)
print(stud+1)