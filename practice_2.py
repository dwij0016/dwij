import pandas as pd
import numpy as np

# ##question_1:-
# data = {
#     "Name": ["Alice", "Bob", "Charlie"],
#     "Age": [25, 30, 35],
#     "City": ["Delhi", "Mumbai", "Ahmedabad"]
# }

# s = pd.DataFrame(data)
# print(s)

# r = s.iloc[0]
# print(r)

# r1 = s.iloc[1]
# print(r1)

# r2 = s.iloc[2]
# print(r2)

# sh = s.shape
# print(sh)


##question_2:-

a = pd.read_csv('employees.csv')
print(a.head(15))

ro = a.iloc[1]
print(ro)

ro1 = a.iloc[2]
print(ro1)

ro2 = a.iloc[3]
print(ro2)

ro3 = a.iloc[4]
print(ro3)

ro4 = a.iloc[5]
print(ro4)

# column names
ro5 = a.iloc[0]
print(ro5)

g = a.dtypes
print(g) 

k = a.describe()  ## used to print everything like mean, max, min, std, count, etc
print(k)


