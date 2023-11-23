N,M=map(int,input().split())
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
print((min(abs(x1-x2),N-abs(x1-x2))+min(abs(y1-y2),M-abs(y1-y2)))//2+(min(abs(x1-x2),N-abs(x1-x2))+min(abs(y1-y2),M-abs(y1-y2)))%2)