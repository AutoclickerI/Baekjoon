x,y=map(int, input().split())
d=int(input())
print(*divmod(100*x+y+2*d>>2,100))
print(*divmod(100*x+y-2*d>>2,100))