def M():a,b,c,d=map(int,input().split());return{(x,y)for x in range(a,c)for y in range(b,d)}
print(len((M()|M())-M()))