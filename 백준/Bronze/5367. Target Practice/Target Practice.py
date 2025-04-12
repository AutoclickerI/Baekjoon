N=int(input())-2
print('|'+'-'*N+'|')
for i in range(N):
    *l,=' '*N
    l[i]=l[N-i-1]='*'
    print('|',*l,'|',sep='')

print('|'+'-'*N+'|')