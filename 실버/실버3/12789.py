n = int(input())
tem = list(map(int, input().split()))

st = []

cnt = 1

while tem:
    if cnt == tem[0]:
        tem.pop(0)
        cnt += 1
        
    else:
        st.append(tem.pop(0))
        
    while st:
        if st[-1] == cnt:
            cnt += 1
            st.pop()
        else:
            break

if len(st) != 0:
    print("Sad")
else:
    print("Nice")