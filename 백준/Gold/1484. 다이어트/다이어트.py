R=range(1,60000)
d={i*i for i in R}
n=int(input())
print(*l if(l:=[i for i in R if i*i-n in d])else[-1])