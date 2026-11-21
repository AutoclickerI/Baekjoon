N,l,M,*s=open(0)
*l,=map(int,l.split())
S=sorted(l)
for i in s:p,q=map(int,i.split());l[p],l[q]=l[q],l[p];print((l!=S)*(2*(N=='2\n')-1))