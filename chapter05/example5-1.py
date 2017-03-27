import random
from matplotlib import pyplot as plt
from collections import Counter

num_friends = [random.choice(range(100)) for _ in range(100)]

friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 30])
plt.title("Histogram of Firend Counts")
plt.xlabel("# of firends")
plt.ylabel("# of people")
plt.show()