# coding=utf-8
import math

from chapter06.inverse_normal_cdf import inverse_normal_cdf


def normal_approximation_to_binomial(n, p):
    """ B/inomial(n, p)에 해당되는 mu(평균)와 sigma(표준편차) 계산"""
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma


def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


# 누적분포함수는 확률변수가 특정 값보다 작을 확률을 나타낸다
normal_probability_below = normal_cdf


# 만약 확률변수가 특정 값돠 작지 않다면, 특정 값보다 크다는 것을 의미한다.
def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - normal_cdf(lo, mu, sigma)


# 만약 확률변수가 hi보다 작고 lo보다 작지 않다면, 확률변수는 hi와 lo 사이에 존재한다
def normal_probability_between(lo, hi, mu=0, sigma=1):
    return math.fabs(normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma))


# 만약 확률변수가 범위 밖에 존재한다면, 범위 안에 존재하지 않다는 것을 의미한다.
def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)


# P(Z <= z) = probability 인 z 값을 반환
def normal_upper_bound(probability, mu=0, sigma=1):
    return inverse_normal_cdf(probability, mu, sigma)


# P(Z >= z) = probability 인 z 값을 반환
def normal_lower_bound(probability, mu=0, sigma=1):
    return inverse_normal_cdf(1 - probability, mu, sigma)


def normal_two_sided_bounds(probability, mu=0, sigma=1):
    """ 입력한 probability 값을 포함하고, 평균을 중심으로 대칭적인 구간을 반환 """
    tail_probability = (1 - probability) / 2

    # 구간의 상한은 tail_probability 값 이상의 확률 값을 갖고 있다.
    upper_bound = normal_upper_bound(tail_probability, mu, sigma)

    # 구간의 하한은 tail_probability 값 이하의 확률 값을 갖고 있다.
    lower_bound = normal_lower_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound
