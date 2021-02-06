import numpy as np

a = [1,2,3,4]
b = [5,6,7,8]

ab = []

for i in range(0,len(a)):
    ab.append(a[i] * b[i])
print(ab)

x = np.array([1,2,3,4])
y = np.array([5,6,7,8])
z = np.array([2,2,2,2])
print(x*y*z)

d1 = np.array([[3,1],[1,2]])
d2 = np.array([9,8])

sonuc = np.linalg.solve(d1,d2)
print(f'denklemin kökleri: {sonuc}')