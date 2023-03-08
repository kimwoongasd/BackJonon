def palindrome(x, y):
    s, e = x, y
    while s < e:
        if a[s] == a[e]:
            s += 1
            e -= 1
        else:
            return False
    return True


def pseudo_palindrome(x, y):
    s, e = x, y
    while s < e:
        if a[s] != a[e]:
            lt = palindrome(s + 1, e)
            rt = palindrome(s, e - 1)
            if lt or rt:
                return True
            
            else:
                return False
        else:
            s += 1
            e -= 1

# 오답
# def pseudo_palindrome(x, y):
#     s, e = x, y
#     while s < e:
#         if a[s] == a[e]:
#             s += 1
#             e -= 1
#         else:
#             if a[s + 1] == a[e]:
#                 s += 2
#                 e -= 1
#             elif a[s] == a[e - 1]:
#                 e -= 2
#                 s += 1
#             else:
#                 return False
#     return True

n = int(input())

for _ in range(n):
    a = input()
    
    if palindrome(0, len(a) - 1):
        print(0)
    elif pseudo_palindrome(0, len(a) - 1):
        print(1)
    else:
        print(2)