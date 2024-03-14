(K,),_,(*A,),_,(*B,)=[map(int,i.split())for i in open(0)]
print(sum(i+K==j for i in A for j in B))