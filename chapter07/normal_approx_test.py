# coding=utf-8
from chapter07.normal_approximation import normal_approximation_to_binomial, normal_two_sided_bounds, normal_probability_between

mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)
print "Result : ", mu_0, sigma_0

# p = 0.5라고 가정할 때, 유의수준이 5%인 구간
lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)
print "Result: ", lo, hi

# p = 0.55인 경우의 실제 평균과 표준편차
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)
print "Result : ", mu_1, sigma_1

# 제2종 오류란 귀무가설(H0)을 기각하지 못한다는 의미
# 즉, X가 주어진 구간 안에 존재할 경우를 의미
type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
power = 1 - type_2_probability
print "power = ", power, type_2_probability
