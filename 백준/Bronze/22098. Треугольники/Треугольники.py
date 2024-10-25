def e(*a):a,b,c=sorted(a);q=c*c-a*a-b*b;return[[0]*3,[q==0,q<0,q>0]][a+b>c]
for _ in[0]*int(input()):a,b,c,d=map(int,input().split());print(*map(sum,zip(e(a,b,c),e(a,b,d),e(a,c,d),e(b,c,d))))