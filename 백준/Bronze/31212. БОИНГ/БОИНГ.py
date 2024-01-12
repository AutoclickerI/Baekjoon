l=['1D','1E','1F']+[str(i)+j for i in range(2,21)for j in'ABCDEF']+['21D','21E']
n=int(input())
if n<118:
    print(l[n+(l.index(input())<=n)])
else:
    print('full')