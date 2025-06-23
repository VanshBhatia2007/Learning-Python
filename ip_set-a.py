import pandas as pd

data = {
    "ename": ["Rinkoo Sharma", "Shiv Bansal", "Raman Ahuja", "Aman Sharma", "Seema Singh", "Aman Singh", "Rajat Singh"],
    "desig": ["MNGR", "CLRK", "CLRK", "SALESMAN", "MNGR", "SALESMAN", "CLRK"],
    "dept": ["ACCTS", "ADMIN", "ADMIN", "SALES", "SALES", "SALES", "ACCTS"],
    "Salary": [80000, 45000, 35000, 55000, 85000, 45000, 35000],
    "doj": ["2010-10-01", "2012-01-04", "2009-03-01", "2009-01-01", "2008-02-01", "2006-12-12", "2009-10-01"]
}

emp = pd.DataFrame(data)
emp.iloc[7,:]=['Vansh Bhatia','MNGR','IT',50000,'2007-10-02']
print(emp)