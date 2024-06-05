N=int(input())
p=[[*map(int,input().split())]for _ in[0]*N]
x_sum,y_sum=map(sum,zip(*p))
x_mean=x_sum/N
y_mean=y_sum/N
n=d=0
for x,y in p:
    n+=(x-x_mean)*(y-y_mean)
    d+=(x-x_mean)**2
slope=n/d
intercept=y_mean-slope*x_mean
print(f'{slope:.3f} {intercept:.3f}')