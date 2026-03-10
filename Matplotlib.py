import matplotlib.pyplot as plt

# x=[1,2,3,4,5]
# y=[1,4,9,16,25]

# plt.plot(x,y)
# plt.xlabel('X-axis')
# plt.ylabel('Y-label')
# plt.title("Basic line plot")
# plt.show()



# x=[1,2,3,4,5]
# y=[1,4,9,16,25]
# plt.plot(x,y, color='red', linestyle='--', marker='o', linewidth=3, markersize=9)
# plt.grid(True)
# plt.show()


# x=[1,2,3,4,5]
# y1=[1,4,9,16,25]
# y2=[1,2,3,4,5]

# plt.figure(figsize=(9,5))

# plt.subplot(2,2,1)
# plt.plot(x,y1, color='green')
# plt.title("plot 1")
# plt.show()

# plt.subplot(2,2,2)
# plt.plot(y1,x, color='red')
# plt.title("plot 2")
# plt.show()

# plt.subplot(2,2,3)
# plt.plot(x,y2, color='blue')
# plt.title("plot 3")
# plt.show()

# plt.subplot(2,2,4)
# plt.plot(x,y2, color='green')
# plt.title("plot 4")
# plt.show()


# categories=['A','B','C','D','E']
# values=[5,7,3,8,6]

# plt.bar(categories,values,color='purple')
# plt.xlabel("Categories")
# plt.ylabel("values")
# plt.title('Bar plot')
# plt.show()


data=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,]

plt.hist(data,bins=5,color='orange',edgecolor='black')
plt.show()