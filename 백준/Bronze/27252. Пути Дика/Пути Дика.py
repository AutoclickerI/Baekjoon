s=input()
l=eval("len(s)*['.'],"*50)
z=h=0
for i in s:f=i=='(';z-=1-2*f;l[~z+f][h]='\/'[f];h+=1
for i in l:{'/'}<{*i}!=print(*i,sep='')