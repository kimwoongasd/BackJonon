import sys

n = int(input())
k = int(input())
arr = list(map(int, input().split()))
arr.sort()

if k >= n:
    print(0)
    sys.exit()

d = []
for i in range(n - 1):
    d.append(arr[i + 1] - arr[i])

d.sort()
for i in range(k - 1):
    d.pop()

print(sum(d))

'''
풀이
결론적으로 정렬만 수행하면 되므로 시간복잡도 O(NlogN)에 해결 가능
결론적으로 문제가 요구하는 것은 n개의 센서들을 k개의 구간으로 나누는 것과 동일하다.

센서 위치를 입력받아 오름차순 정렬한다.
집중국수 k가 센서수 n과 같거나 크다면, 집중국을 센서 위치에 설치하면 되므로 답은 0이 된다.
1이 아니라면, 인접한 센서 사이의 거리를 전부 구해 d 리스트에 저장한 후 내림 차순 정렬한다.
센서들을 k개의 구간으로 나눠야 하므로, k-1번만큼 반복을 돌며 값이 가장 큰 원소부터 차례로 제거한다.
남은 원소들의 합을 구하여 출력한다.

'''