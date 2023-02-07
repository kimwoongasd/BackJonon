import heapq
t = int(input())
for _ in range(t):
    m = int(input())
    arr = []
    if m % 10 == 0:
        for _ in range(m // 10):
            arr.extend(list(map(int, input().split())))
    else:
        for _ in range(m // 10 + 1):
            arr.extend(list(map(int, input().split())))

    lt, rt = [], []
    senter = arr[0]
    res = [senter]
    for i in range(1, m):
        # 중앙값보다 작다면 최대힙을 저장
        if senter > arr[i]:
            heapq.heappush(lt, -arr[i])
        # 중앙값보다 크다면 최소힙 저장
        else:
            heapq.heappush(rt, arr[i])
        
        if i % 2 == 0:
            if len(lt) > len(rt):
                heapq.heappush(rt, senter)
                senter = -heapq.heappop(lt)
            elif len(lt) < len(rt):
                heapq.heappush(lt, -senter)
                senter = heapq.heappop(rt)
            res.append(senter)
            
    print(m // 2 + 1)
    for j in range(len(res)):
        if (j + 1) != 1 and (j + 1) % 10 == 1:
            print()
        print(res[j], end=" ")
    print()