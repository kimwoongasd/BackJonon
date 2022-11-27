n = int(input())
arr = [[0] * 10 for _ in range(n + 1)]
arr[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, n + 1):
    for j in range(10):
        # 뒷자리가 0일 때
        if j == 0:
            arr[i][j] = arr[i - 1][j + 1]
        # 뒷다리가 9일 때
        elif j == 9:
            arr[i][j] = arr[i - 1][j - 1]
        else:
            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j + 1]
            
print(sum(arr[n]) % 1000000000)

# 오답 규칙을 못찾음
# n = int(input())

# ch = [0] * (n + 3)
# ch[1] = 9
# ch[2] = 17

# for i in range(3, n + 1):
#     ch[i] = (ch[i - 1] * 2 - (i - 1)) % 1000000000
# print(ch[n])

# n = int(input())

# arr = [[0] * 10 for _ in range(101)]