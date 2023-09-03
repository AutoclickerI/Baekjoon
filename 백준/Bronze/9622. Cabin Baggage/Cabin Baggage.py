x=[]
for i in[*open(0)][1:]:a,b,c,d=map(eval,i.split());x+=1-bool(((a>56)+(b>45)+(c>25))*(a+b+c>125)+(d>7)),
print(*x,sum(x))