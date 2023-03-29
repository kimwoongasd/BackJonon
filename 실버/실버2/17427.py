# n = int(input())

# res = 0
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         if i % j == 0:
#             res += j
# print(res)

import sys
input = sys.stdin.readline

n = int(input())

sum = 0
for i in range(1, n + 1):
	# i의 배수의 개수 = i를 약수로 갖는 수
    sum += (n // i) * i

print(sum)