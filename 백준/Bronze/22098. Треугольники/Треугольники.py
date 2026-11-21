def e(*a):a,b,c=sorted(a);q=c*c-a*a-b*b;return[[0]*3,[q==0,q<0,q>0]][a+b>c]
for i in[*open(0)][1:]:a,b,c,d=map(int,i.split());print(*map(sum,zip(e(a,b,c),e(a,b,d),e(a,c,d),e(b,c,d))))