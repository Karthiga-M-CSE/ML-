import numpy as np

arr= np.array([[1,2,3],[2,4,6],[3,6,9]])
id=np.eye(3)

print(arr)
print(id)

print(np.add(arr,id))
print(np.subtract(arr,id))
print(np.multiply(arr,id))
print(np.sqrt(arr))

print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))
print(np.var(arr))
print(np.min(arr))
print(np.max(arr))
print(np.sum(arr))

x=np.zeros((3,3))
print(x)

y=np.ones((3,3))
print(y)

print(np.sort(arr))

a = np.arange(10,21,3)
print(a)

b = np.array([[2],[2]])
print(b)

print(np.sin(a))
print(np.cos(a))

print(np.sqrt(a))

print(np.sort(a,kind = 'mergesort'))

print(a+5)
print(a-2)
print(a*3)
print(a/0.5)
