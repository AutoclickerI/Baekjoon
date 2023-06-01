from bisect import*
n=int(input())
l=sorted(set([tuple(map(int,input().split()[1:]))for i in[0]*n]),key=lambda x:(x[0],-x[1]))[::-1]
c=[-1]
for i in range(len(l)):
 if c[-1]<=l[i][1]:m=len(c);c+=[l[i][1]]
 else:L=bisect_right(c,l[i][1]);c[L]=l[i][1]
print(m)