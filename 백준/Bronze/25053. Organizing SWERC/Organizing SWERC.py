for _ in range(int(input())):
  N=int(input())
  MX=[0]*10
  for _ in range(N):a,b=map(int,input().split());MX[-b]=max(MX[-b],a)
  print('MOREPROBLEMS'*(min(MX)<1)or sum(MX))