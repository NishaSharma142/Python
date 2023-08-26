#Get started with numpy

#One dimensional array
#install and import required library
import numpy as np
list=[1,2,3]
np.array(list)
list1=[[1,2,3],[4,5,6],[7,8,9]]
print(np.array(list1))
print(np.arange(5,10))
print(np.arange(1,100))
print(np.zeros(10))
print(np.ones(10,int))
print(np.ones((2,5),int))
print(np.linspace(0,2,5))
print(np.eye((10)))
print(np.random.randn(2,4))
print(np.random.randint(2,100))
print(np.random.randint(29,56,100))
array1=np.random.randint(0,100,20)
print(array1.reshape(4,5))
print(array1.max())
print(array1.argmax())
a=np.eye(5)
print(a)
print(a.T)
sample_array=np.arange(10,21)
print(sample_array[2:5])
subset_sample_array=sample_array[0:7]
subset_sample_array[:]=1001
print(subset_sample_array)

# Two dimensional array
matrix=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(matrix)
print(matrix[1,2])
print(matrix[2,:])
print(matrix[2])
print(matrix[:,(3,2)])
