for i in[*open(0)][1:]:a,c,b,d,p,q=map(int,i.split());m=[[x,y]for x,y in[(i,(p-a*i)//b)for i in range(p//a+2)if(p-a*i)%b<1]if c*x+d*y==q and x>0<y];print(*1==len(m)and m[0]or'?')