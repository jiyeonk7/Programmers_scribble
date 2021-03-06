#################################################문제#################################################
# - 동빈이는 두 개의 배열 A와 B를 가지고 있습니다. 두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두
#   자연수 입니다.
# - 동빈이는 최대 K번의 바꿔치기 연산을 수행할 수 있는데, 바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에
#   있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 마랗ㅂ니다.
# - 동빈이의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이며, 여러분은 동빈이를 도와야합니다.
# - N, K, 그리고 배열 A와 B의 정보가 주어졌을 때, 최대 K번의 바꿔치기 연산을 수행하며 만들 수 있는 배열 A의
#   모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하세요.

#################################################코드#################################################
import time

a = [1,2,5,4,3]
b = [5,5,6,6,5]

n, k = 5, 3

# MINE
for _ in range(k):
    a_idx = a.index(min(a))
    b_idx = b.index(max(b))
    a[a_idx], b[b_idx] = b[b_idx], a[a_idx]

print(sum(a))

# EXAM
# a.sort()
# b.sort(reverse=True)

# for i in range(k):
#     if a[i] < b[i]:
#         a[i], b[i] = b[i], a[i]
#     else:
#         break
# print(sum(a))