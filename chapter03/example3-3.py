from collections import Counter

from matplotlib import pyplot as plt

shipments = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda shipment: shipment // 10 * 10
histogram = Counter(decile(shipment) for shipment in shipments)

plt.bar([x - 4 for x in histogram.keys()],
        histogram.values(),
        8)
plt.axis([-5, 106, 0, 5])
plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel("Number of Shipment Companys")
plt.title("Distribution of Shipments")
plt.show()