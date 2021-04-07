def solution(n):
    if n < 3:
        return n
    i, j = 1, 2
    for _ in range(n-2):
        i, j = j, i+j
    return j%1000000007