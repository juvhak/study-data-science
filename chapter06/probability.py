import random


def random_kid():
    return random.choice(["boy", "girl"])


both_girls = 0
older_girls = 0
either_girls = 0

random.seed(0)

for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == "girl":
        older_girls += 1
    if older == "girl" and younger == "girl":
        both_girls += 1
    if older == "girl" or younger == "girl":
        either_girls += 1

print both_girls
print older_girls
print either_girls

print "P(both | older): ", float(both_girls) / float(older_girls)
print "P(both | either): ", float(both_girls) / float(either_girls)
