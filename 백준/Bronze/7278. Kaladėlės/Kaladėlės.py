N=int(input())
a,b,c=map(int,input().split())
print(*min((abs(N-N//a*a),a,N//a*a),(abs(N-N//b*b),b,N//b*b),(abs(N-N//c*c),c,N//c*c),(abs(N-N//a*a-a),a,N//a*a+a),(abs(N-N//b*b-b),b,N//b*b+b),(abs(N-N//c*c-c),c,N//c*c+c))[1:])