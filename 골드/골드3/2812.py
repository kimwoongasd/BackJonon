n, k = map(int, input().split())
arr = input()
'''
풀이
stack에 넣고 그 다음 숫자와 비교
만일 다음 숫자가 stack에 있는 숫자보다 크면 stack.pop()
을 해주면서 가장 큰 숫자를 앞 쪽에 위치하도록 한다.
k개 까지만 지워야 하므로 k > 0이상일 때만 수행하고, 
만일 k개 미만으로 숫자를 지웠다면 뒤에 있는 숫자를 남은 k개 만큼 지우고 출력한다.
'''
stack = []
for x in arr:
    while stack and stack[-1] < x and k > 0:
        stack.pop()
        k -= 1
    stack.append(x)
if k > 0:
    print("".join(stack[:-k]))
else:
    print("".join(stack))

# 내풀이 틀림
# tem = [arr[0]]
# for i in range(1, n):
#     if k < 1:
#         tem.append(arr[i])
#     else:
#         if arr[i] > tem[-1]:
#             tem.pop()
#             tem.append(arr[i])
#             k -=1
#         elif arr[i] == tem[-1]:
#             tem.append(arr[i])
#         else:
#             k -=1
            
# print(tem)