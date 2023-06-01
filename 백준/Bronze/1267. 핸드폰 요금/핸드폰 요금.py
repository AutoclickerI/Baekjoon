M=0;N=0
n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    M+=a[i]//30+1
    N+=a[i]//60+1
N*=15;M*=10
print(f'Y M {M}'if M==N else f'Y {M}' if M<N else f'M {N}')