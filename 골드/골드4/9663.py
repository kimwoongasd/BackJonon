# 문제를 이해하지 못하여 풀지 못하였다.
# 풀이를 보고 간신히 이해하였다.

n = int(input())
res= 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        # 이미 놓여진 퀸과 같은 열이거나 대각선 상에 있는지 확인
        # (핼 꺠리의 차 == 열 끼리의 차의 절대값)이 True이면 대각선 상에 있는 것이다.
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global res
    # 마지막 까지 탐색 완료
    if x == n:
        res += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            # 퀸 놓기 조건이 True라면
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(res)