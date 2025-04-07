import math

def solution(k, d):
    answer = 0
    y=0
    while y<=d:
        th=d*d-y*y
        answer+=math.isqrt(th)//k+1
        y+=k
    
    
    return answer