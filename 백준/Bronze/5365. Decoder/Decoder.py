input()
n=0
for i in input().split():
    t=len(i)
    print(end=' 'if n>=t else i[n])
    n=t-1