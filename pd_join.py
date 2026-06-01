import pandas as pd 

d = pd.read_csv('Id.csv')
d1 = pd.read_csv('Id-1.csv')

d_join = d.merge(d1,on='Id',how='right')
print(d_join)

d_join1 = d.merge(d1,on='Id',how='left')
print(d_join1)

d_join2 = d.merge(d1,on='Id',how='inner')
print(d_join2)

d_join3 = d.merge(d1,on='Id',how='outer')
print(d_join3)

d_concat = pd.concat([d,d1])
print(d_concat)
