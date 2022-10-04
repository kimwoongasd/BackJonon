while True:
    n = input()
    if n == "0":
        break
    
    res = "yes"
    
    if len(n) == 1:
        res = "yes"
        
    else:
        for i in range(len(n) // 2):
            if n[i] != n[- i - 1]:
                res = "no"
                break
    print(res)
