
from matplotlib import pyplot as plt

books = ["Book1", "Book2", "Book3", "Book3", "Book4"]
sales_count = [500, 789, 879, 284, 104]

x_standard = [i + 0.1 for i, _ in enumerate(books)]

plt.bar(x_standard, sales_count)
plt.ylabel("Sales Count of Books")
plt.title("Books Sales")

plt.xticks([i + 0.1 for i, _ in enumerate(books)], books)
plt.show()
