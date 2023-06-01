N,A,B,C,D=map(int,input().split())
print(min(((N-1)//A+1)*B,((N-1)//C+1)*D))