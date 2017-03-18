from matplotlib import pyplot as plt

years = [1990, 1995, 2000, 2005, 2010, 2015, 2016, 2017]
length = [10, 20, 34, 52, 43, 67, 81, 90]

# x axis : year
# y axis : length
plt.plot(years, length, color='green', marker='o', linestyle='solid')
plt.title("Length of Year")
plt.ylabel("Length")
plt.show()