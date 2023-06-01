d={0:(0,0,0)};n=int(input())
for i in range(n):
    a,b,c=list(map(int, input().split()))
    d[i+1]=(min(d[i][1]+a,d[i][2]+a),min(d[i][0]+b,d[i][2]+b),min(d[i][0]+c,d[i][1]+c))
print(min(d[n]))