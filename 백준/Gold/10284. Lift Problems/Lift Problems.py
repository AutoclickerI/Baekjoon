exec('''n=int(input())+1;S=[0]+[*map(int,input().split())];tot=sum(S);a=[0]*n
for j in range(1,n):
 tot-=S[j];sa,a[j]=0,10**9
 for k in range(j)[::-1]:a[j]=min(a[j],a[k]+sa+tot);sa+=(j-k)*S[k]
print(a[-1]);'''*int(input()))