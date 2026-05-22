import numpy as np
import pandas as pd

ar = np.random.randint(1,100,20).reshape(5,4)

f = pd.DataFrame(ar,np.arange(101,106,1),['phy','chem','math','bio'])
print(f)

# print(f[['chem','phy','bio']])

# print(f.loc[104]) #grabbing a row
# print(f.iloc[2])  #grabbing a row via index

# print(f.loc[103,'chem']) # to grab a specific value from the matrix

f['total'] = f['phy'] + f['chem'] + f['math'] + f['bio']
print(f)

f.drop('phy',axis=1,inplace=True)
print(f)

# error in deleting row
