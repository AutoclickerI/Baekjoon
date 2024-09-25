def solution(number,k):
    l=[]
    for i in number:
        while k and l and l[-1]<i:l.pop();k-=1
        l+=i
    while k:l.pop();k-=1
    return''.join(l)