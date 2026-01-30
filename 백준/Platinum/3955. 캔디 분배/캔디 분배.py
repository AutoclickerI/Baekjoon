for i in[*open(0)][1:]:
 K,C=map(int,i.split())
 try:t=[pow(C,-1,K),(C<2)*K+1][1in[K,C]];1/(1e9//t)
 except:t='IMPOSSIBLE'
 print(t)