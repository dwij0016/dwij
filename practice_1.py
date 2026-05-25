# ques = 1 , dtype

import numpy as np
import pandas as pd
h = np.arange(1,21)
print(h)
f = np.shape([h])
print(f)
l=np.sum([h])
print(l)

# ques = 2, replacement

b = np.zeros(12)
print(b)
a = np.zeros(12).reshape(3,4)
print(a)

s = pd.DataFrame(a)
print(s)

# ques = 3

m = np.random.randint(1,50,16).reshape([4,4])
print(m)
print('max = ', m.max())
print('mean =',m.mean())
print('SD =',m.std())
print('columb =',m.max(axis=1))
print('columb =',m.mean(axis=1))
print('columb =',m.std(axis=1))

# ques = 4 (value and index)

c = pd.Series([10,20,30,40,50])
print(c)
c[0] = 'a'
c[1] = 'b'
c[2] = 'c'
c[3] = 'd'
c[4] = 'e'
print(c)