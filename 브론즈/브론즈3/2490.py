for i in range(3):
    tem = list(map(int, input().split()))
    
    res = 0
    if sum(tem) == 1:
        res = "C"
    elif sum(tem) == 2:
        res = "B"
    elif sum(tem) == 3:
        res = "A"
    elif sum(tem) == 4:
        res = "E"
    else:
        res = "D"
    print(res)