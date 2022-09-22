y_1, m_1, d_1 = map(int, input().split())
y_2, m_2, d_2 = map(int, input().split())

y = y_2 - y_1

if m_2 > m_1:
    print(y)
elif m_2 == m_1:
    if d_2 >= d_1:
        print(y)
    else:
        print(y - 1)
else:
    print(y - 1)
print(y + 1)
print(y)