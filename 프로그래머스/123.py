def solution(n):
    answer = []
    for x in n[::-1]:
        answer.append(int(x))
    return answer

a = input()
print(solution(a))