pd=[]
from itertools import permutations

for i in permutations(range(2,9)):
    a,b,c,d,e,f,g,h=1,*i
    pd+=(*map(sorted,[(a,b,d,h),(b,a,c,g),(c,b,d,f),(d,a,c,e),(e,d,f,h),(f,e,g,c),(g,b,f,h),(h,a,e,g)]),),

for _ in[0]*int(input()):
    l=sorted(map(int,input().split()))
    pd=[i for i in pd if l in i]

if pd:
    print('Hmm...')
else:
    print("You're gonna die!")