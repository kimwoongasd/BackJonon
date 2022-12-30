n = int(input())
ch = [0] * 31
ch[0] = 1
ch[2] = 3

for i in range(3, 31):
    # i가 4로 나누어 떨어질 때 경우의 수가 생긴다
    if i % 2 == 0:
        ch[i] = ch[i - 2] * 3
        # n - 2, n - 4의 경우를 *2를 해서 더해준다.
        # 이 경우의 수를 생각 못해서 틀렸다
        for j in range(4, i + 1, 2):
            ch[i] += ch[i - j] * 2

print(ch[n])