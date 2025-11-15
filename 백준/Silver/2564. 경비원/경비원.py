[W,H],_,*l=[map(int,i.split())for i in open(0)]
O=W+H<<1
*l,v=[[W+p,-p,-p-H,p][-n]for n,p in l]
print(sum(min((i-v)%O,(v-i)%O)for i in l))