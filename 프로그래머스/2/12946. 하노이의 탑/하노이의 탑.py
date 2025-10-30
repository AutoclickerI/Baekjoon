
def solution(n, s=1, e=3):
    if n==1:
        return[[s,e]]
    return solution(n-1,s,6-s-e)+[[s,e]]+solution(n-1,6-s-e,e)