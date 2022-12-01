# hanoi(n)은 2번의 hanoi(n - 1) 재귀 과정을 수반한다
# start에서 sub를 거쳐 end로 총 n개의 원반을 운반
def hanoi(L, start, sub, end):
    # 원반이 1개 일 때
    if L == 1:
        print(start, end)
    else:
        # n - 1개의 원판을 1번막대에서 2번 막대로
        hanoi(L - 1, start, end, sub)
        # 남은 1개 원반은 3번 막대로
        print(start, end)
        # n - 1개의 원판을 2번막대에서 3번 막대로
        hanoi(L - 1, sub, start, end)

n = int(input())
s = 2**n - 1
print(s)

hanoi(n, 1, 2, 3)

