def naive(n):
    cnt=0
    while n!=1:
        if n%2:n+=1
        else:n//=2
        cnt+=1
    return cnt
for _ in[0]*int(input()):print(naive(int(input())))