*l,[p,q]=[map(int,i.split())for i in open(0)]
R,G,B=[max(0,i-j)for i,j in zip(*l)]
G+=R+B
print(-(p-R|q-B|p+q-G<0)or G)