import pandas as pd
import numpy as np
s = pd.Series([1,5,5,4,8,5,3,8,5,8,8,8,8])
print(s)

a = pd.Series([1,2,3,5,4,8,88,47,411,47,789,54,2,52,85,52,2])
print ( "a[0] = ",a[0])
print ( "a[1] = ",a[1])
print ( "a[2] = ",a[2])
print ( "a[3] = ",a[3])
print ( "a[4] = ",a[4])
print ( "a[5] = ",a[5])
print ( "a[6] = ",a[6])
print ( "a[7] = ",a[7])
print ( "a[8] = ",a[8])
print ( "a[9] = ",a[9])
print ( "a[10] = ",a[10])
print ( "a[11] = ",a[11])
print ( "a[12] = ",a[12])
print ( "a[13] = ",a[13])
print ( "a[14] = ",a[14])
print ( "a[`5] = ",a[15])
print ( "a[16] = ",a[16])

mat1 = pd.Series([2,4,6,8,10])
mat2 = pd.Series([1,3,5,7,9])

add = mat1 + mat2
sub = mat1 - mat2
mul = mat1 * mat2
div = mat1/mat2

print("addition = ",add )
print("substractiob = ", sub)
print("multiplication = ",mul)
print("division = ",div)

d = np.array([10,2,30,40,50])

f = pd.Series(d)
print(f)

a = pd.Series([1,2,3,5,4,8,88,47,411])
s = print("a[0] + a[1] + a[2] + a[4] + a[5] = ", a[0] + a[1] + a[2] + a[4] + a[5])

a = pd.Series([1,2,3,5,4,8,88,47,411],dtype = str)  
s = print("a[0] + a[1] + a[2] + a[4] + a[5] = ", a[0] + a[1] + a[2] + a[4] + a[5])

a = pd.Series([1,2,3,5,4,8,88,47,411], dtype = bool)
s = print("a[0] + a[1] + a[2] + a[4] + a[5] = ", a[0] + a[1] + a[2] + a[4] + a[5])