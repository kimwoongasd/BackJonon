n, k = map(int, input().split())
coin = []
for i in range(n):
    a = int(input())
    coin.append(a)

ch = [0] * (k + 1)
# 0원일 경우의 수 1
ch[0] = 1

for x in coin:
    # 동전의 x원 부터 시작해야 음수가 발생하지 않는다
    for i in range(x, k + 1):
        if i - x >= 0:
            # 동전으로 i의 해당하는 값을 만들 수 있는 경우의 수
            # ex) 동전이 1, 2, 5가 있을 때 i = 2 일 때 1원 짜리 1 + 1, 2의 경우의 수가 나옴
            # 1원 짜리를 for문을 돌면 전부 1이지만
            # 2원 짜리 for문을 돌면 ch[i - x]는 ch[0], 즉 1을 가지고
            # ch[i]는 1 + 1 의 경우의 수 1를 가지고 있기 때문에 두 값을 더한다.
            ch[i] += ch[i - x]

print(ch[k])