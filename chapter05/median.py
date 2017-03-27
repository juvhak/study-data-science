# coding=utf-8
import random
from collections import Counter

from numpy import mean, math

from chapter04.vector_functions import sum_of_squares, dot


def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        return sorted_v[midpoint]
    else:
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2


def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]


def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.iteritems() if count == max_count]


def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


# 분산
def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)


# 표준편차
def standard_deviation(x):
    return math.sqrt(variance(x))


# 공분산
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)


# 상관관계
def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0


num_friends = [random.choice(range(100)) for _ in range(100)]
daily_minutes = [random.choice(range(100)) for _ in range(200)]
print median(num_friends)

print quantile(num_friends, 0.10)
print quantile(num_friends, 0.25)
print quantile(num_friends, 0.75)
print quantile(num_friends, 0.90)

print mode(num_friends)
print variance(num_friends)

print covariance(num_friends, daily_minutes)
print correlation(num_friends, daily_minutes)
