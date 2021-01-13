def solution(n):
    answer = []

    for i in range(len(str(n))):
        answer.append(int(n % 10))
        n /= 10
        
    return answer