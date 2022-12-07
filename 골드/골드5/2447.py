def recursion(m):
    #  3 x 3의 테이블의 패턴이 똑같이 반복
    if m == 3:
        return ["***", "* *", "***"]
    
    arr = recursion(m//3)
    star = []
    
    for i in arr:
        star.append(i * 3)
    
    for i in arr:
        star.append(i + " "*(m//3) + i)
    
    for i in arr:
        star.append(i * 3)
    
    return star

n = int(input())
print('\n'.join(recursion(n)))
