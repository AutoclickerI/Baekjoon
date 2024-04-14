N=int(input())
exec('a,b=map(int,input().split());print(3-max(-a,-b,a+~N,b+~N)%3);'*int(input()))