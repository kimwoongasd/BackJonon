n = int(input())
arr = []
# 최대 1000일 과제
ch = [0] * (1000)
for _ in range(n):
    d, w = map(int, input().split())
    arr.append([d, w])

# 점수를 내림차순으로 정렬
arr.sort(reverse=True, key= lambda x: x[1])

for i in range(n):
    for j in range(arr[i][0] - 1, -1, -1):
        if ch[j] == 0:
            ch[j] = arr[i][1]
            break
print(sum(ch))

# 내가 작성한 코드 틀림
# n = int(input())
# ch = [0] * (n + 1)
# for _ in range(n):
#     d, w = map(int, input().split())
#     for i in range(n, d -1, -1):
#         ch[i] = max(ch[i], ch[i - d] + w)
# print(ch[n])