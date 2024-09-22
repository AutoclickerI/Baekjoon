S,N=input().split()
N=int(N)
print(0if N==1else 0-N//-5if S[0]=='r'else 0-N//-7if S[0]=='c'else 0-N//-4)