import sys
input = sys.stdin.readline
dp = [1] * (10001)

for i in range(2, 10001):
    dp[i] += dp[i - 2]
    
for i in range(3, 10001):
    dp[i] += dp[i - 3]

t = int(input())

for _ in range(t):
    n = int(input())
    print(dp[n])


'''
풀이
1. 1만 써서 합을 나타내는 방법 1가지씩은 모두 가지고 있다 dp 테이블을 1로 초기화해준다.
2. 2가 추가되는 경우dp[i] = dp[i] + dp[i - 2]
3. 이 추가되는 경우dp[i] = dp[i] + dp[i - 3]
4. 각 경우를 더해준다


다이나믹프로그래밍이기 떄문에 패턴을 구하려했지만 실패하였다...
위의 풀이처럼 경우의 수를 2개로 나누는 경우도 생각해야겠다
'''