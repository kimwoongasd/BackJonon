a = input()
boom = list(input())

stack = []
for x in a:
    stack.append(x)
    if stack[-len(boom):] == boom:
        for _ in range(len(boom)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')
    
'''
풀이
stack에 문자열을 담으면서 폭탄 길이 만큼 비교한다
'''