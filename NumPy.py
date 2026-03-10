import numpy as np

# arr1=np.array([1,2,3,4,5])
# print(arr1)
# print(type(arr1))
# print(arr1.shape)


# arr2=np.array([1,2,3,4,5,])
# arr2.reshape(1,5)
# print(arr2)


# arr2=np.array([[1,2,3,4,5]])
# print(arr2.shape)


# arr2=np.array([[1,2,3,4,5],[2,3,4,5,6]])
# print(arr2)
# print(arr2.shape)


# arr=np.arange(0,10,2).reshape(5,1)
# print(arr)


# one=np.ones((3,4))
# print(one)


# eye=np.eye(3)
# print(eye)


# arr=np.array([[1,2,3],[4,5,6]])
# print("Array: \n" , arr)
# print("Shape:", arr.shape)
# print("Number of dimensions:", arr.ndim)
# print("size(number of elements):", arr.size)
# print("Data type", arr.dtype)
# print("Item size(in bytes):", arr.itemsize)


# arr1=np.array([1,2,3,4,5])
# arr2=np.array([10,20,30,40,50])

# print("Addition:", arr1+arr2)
# print("subtration:", arr1-arr2)
# print("Multiplication:", arr1*arr2)
# print("Division:", arr1/arr2)


# arr=np.array([2,3,4,5,6])

# print(np.sqrt(arr))
# print(np.exp(arr))
# print(np.sin(arr))
# print(np.log(arr))


# arr=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
# print("Array:\n ", arr)

# print(arr[1:,1:3])  

# print(arr[0][0])
# print(arr[0:2,2:])


# print(arr[1:,2:])

# arr[0,0]=100
# print(arr)

# data=np.array([1,2,3,4,5])
# mean=np.mean(data)
# std_dev=np.std(data)
# print(mean)
# print(std_dev)

# normalized_data=(data-mean)/std_dev
# print("Normalized data:", normalized_data)


data=np.array([1,2,3,4,5,6,7,8,9,10])
mean=np.mean(data)
print("Mean:", mean)

median=np.median(data)
print("Median is:",median)

variance=np.var(data)
print("Variance is:", variance)


