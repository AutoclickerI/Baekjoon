N=int(input())
A,B,C,D=map(int,input().split())
s=input()
a,b,c,d=map(s.count,'abcd')
if s[0]==s[-1]=='a'and all(i!=j for i,j in zip(s,s[1:]))and a<=A and b<=B and c<=C and d<=D:
    print('Yes')
else:
    print('No')