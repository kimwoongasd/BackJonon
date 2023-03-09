import sys
input = sys.stdin.readline
# 몇번 테스트 할건지 알려주지 않았기 때문에 try쓴다
while True:
    try:
        x = int(input())
        n = int(input())
        x *= 10000000
        arr = []
        for _ in range(n):
            arr.append(int(input()))
        arr.sort()

        s = 0
        e = n - 1
        flag = True
        while s < e:
            total = arr[s] + arr[e]
            if total == x:
                print("yes", arr[s], arr[e])
                flag = False
                break
            
            if total > x:
                e -= 1
            else:
                s += 1

        if flag:
            print('danger')
    except:
        break


# 어디서 틀린지 모르겠다
# x = int(input())
# n = int(input())
# x *= 10000000
# arr = []
# for _ in range(n):
#     arr.append(int(input()))
# arr.sort()

# s = 0
# e = n - 1
# flag = True
# while s < e:
#     total = arr[s] + arr[e]
#     if total == x:
#         print("yes", arr[s], arr[e])
#         flag = False
#         exit(0)
    
#     elif total > x:
#         e -= 1
#     else:
#         s += 1

# if flag:
#     print('danger')