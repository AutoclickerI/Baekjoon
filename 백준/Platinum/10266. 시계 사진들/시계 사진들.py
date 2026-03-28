_,A,B=[sorted(map(int,i.split()))for i in open(0)]

A=[i-A[0]for i in A]
B=[i-B[0]for i in B]
B+=[i+360000 for i in B]
dA=[j-i for i,j in zip(A,A[1:])]
dB=[j-i for i,j in zip(B,B[1:])]

sA=' '+' '.join(map(str,dA))+' '
sB=' '+' '.join(map(str,dB))+' '

if sA in sB:
    print('possible')
else:
    print('impossible')