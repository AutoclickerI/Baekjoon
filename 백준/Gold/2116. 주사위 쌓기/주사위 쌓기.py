import sys
input=sys.setrecursionlimit(9**9)
[N],*l=[[*map(int,i.split())]for i in open(0)]

def process(i,n):
    if i==N:
        return 0
    c=l[i]
    if n in(c[0],c[5]):
        return max(c[1:5])+process(i+1,c[0]+c[5]-n)
    elif n in(c[1],c[3]):
        return max(c[0],*c[2:3],*c[4:])+process(i+1,c[1]+c[3]-n)
    else:
        return max(*c[:2],c[3],*c[5:])+process(i+1,c[2]+c[4]-n)

print(max(process(0,i+1)for i in range(6)))