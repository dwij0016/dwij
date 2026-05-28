import numpy as np
import pandas as pd

a = np.random.randint(1,100,12).reshape(3,4)
d = pd.DataFrame(a,np.arange(101,104,1),['the conjuring','the conjuring-2','the conjuring-The devil made me do it','the conjuring-The last rites'])
print(d)

# setting
d.index.name = 'Sr.no.'
print(d)

# to print/grab a specific column:
print(d['the conjuring'])

# to print/grab multiple column:
print(d[['the conjuring','the conjuring-The devil made me do it']])

# to print/grab a specific row (2 ways):
print(d.loc[101]) # row name

print(d.iloc[2]) # row index

# to print/grab a specific/ a single value:
print(d.loc[101,'the conjuring-The devil made me do it'])  # by loc

print(d.iloc[1,1])  # by iloc

# to delete a particular row:
d.drop(102,inplace=True)
print(d)

# to create a new column:
d['total'] = d['the conjuring'] + d['the conjuring-2'] + d['the conjuring-The devil made me do it'] + d['the conjuring-The last rites']
print(d)

# to delete column and row:
d.drop('total',axis=1,inplace=True)
print(d)

# to print/get subset of the DataFrame
print(d.loc[[101,103],['the conjuring','the conjuring-The last rites']])

# conditional print
print(d>50)


f = d >70
print(d[f])
# appling this in a specific column:
g = d['the conjuring'] > 40
print(d[g])

# for setting index:
d.set_index(['the conjuring','the conjuring-The devil made me do it'])
print(d)

# for resetting the index
d.reset_index()
print(d)