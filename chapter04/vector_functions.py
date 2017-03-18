# coding=utf-8
from functools import partial
import math


def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]


# 첫 번째 방식
# 각 vecotr를 하나씩 더해서 구함.
def vector_sum_1(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result


# 두 번째 방식 - reduce
def vector_sum_2(vectors):
    return reduce(vector_add, vectors)


# 세 번째 방식 - partial function
vector_sum = partial(reduce, vector_add)


# c : number
# v : vector
def scalar_multiply(c, v):
    return [c * v_i for v_i in v]


# vector의 각 요소 별 평균을 구하는 function
def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))


# vector 내적 function
def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


# 각 성분의 제곱 값의 합 function
def sum_of_squares(v):
    return dot(v, v)


# vector의 크기를 구하는 function
def magnitude(v):
    return math.sqrt(sum_of_squares(v))


# squre of distance between two vectors
def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))


# 첫 번째 방법
# distance between tow vectors
def distance_1(v, w):
    return math.sqrt(squared_distance(v, w))


# 두 번째 방법
def distance(v, w):
    return magnitude(vector_subtract(v, w))
