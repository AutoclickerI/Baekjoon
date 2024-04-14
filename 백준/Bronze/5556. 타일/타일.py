N=int(input())
exec('a,b=map(int,input().split());print(3+min(a,b,N+1-a,N+1-b)%-3);'*int(input()))