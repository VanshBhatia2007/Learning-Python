import pandas as pd
data = [["E01", "Ritika", "F", "Manager", "Delhi", "9867585858"],
    ["E02", "Geet", "F", "Programmer", "Mumbai", "9988879990"],
    ["E03", "Rahul", "M", "IT Officer", "Ahmedabad", "7865577898"],
    ["E04", "Riju", "M", "Analyst", "Lucknow", "901736536"],
    ["E05", "Anita", "F", "Programmer", "Bengaluru", "9818765544"]]
columns = ["Emp_id", "Name", "Gender", "Designation", "City", "Mobile"]
df = pd.DataFrame(data, columns=columns)
print(df)
df.at[6,:]=90