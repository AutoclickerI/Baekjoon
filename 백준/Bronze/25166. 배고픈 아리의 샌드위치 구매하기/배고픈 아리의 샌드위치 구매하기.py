a,b=map(int,input().split())
a-=1023
print([['Impossible','Thanks'][a|b==b],'No thanks'][a<1])