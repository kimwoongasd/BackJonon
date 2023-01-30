s = list(input())
t = list(input())

# t를 지워가면서 s로 만든다
while True:
    if s == t:
        print(1)
        break
    
    # 맨뒤 A를 지운다
    if t[-1] == "A":
        t.pop()
    
    # 맨 뒤 B를 지우고 뒤집는다
    else:
        t.pop()
        t.reverse()
    
    if len(t) == 0:
        print(0)
        break
