d={(0,0,0):1}
def f(a,b,c):
    if a <= 0 or b<= 0 or c<= 0:
        d[(a,b,c)]=1
    elif a > 20 or b > 20 or c > 20:
        d[(a,b,c)]=f(20,20,20)
    elif a < b < c:
        d[(a,b,c)]=d[(a, b, c-1)] + d[(a, b-1, c-1)] - d[(a, b-1, c)]
    else:
        d[(a,b,c)]=d[(a-1, b, c)] + d[(a-1, b-1, c)] + d[(a-1, b, c-1)] - d[(a-1, b-1, c-1)]
for i in range(21):
    for j in range(21):
        for k in range(21):
            f(i,j,k)
z=list(map(int,input().split()))
while z!=[-1,-1,-1]:
    try:
        print(f'w({z[0]}, {z[1]}, {z[2]}) = {d[(z[0],z[1],z[2])]}')
        z=list(map(int,input().split()))
    except:
        if z[0] <= 0 or z[1] <= 0 or z[2] <= 0:
            d[(z[0],z[1],z[2])]=1
        else:
            d[(z[0],z[1],z[2])]=d[(20,20,20)]