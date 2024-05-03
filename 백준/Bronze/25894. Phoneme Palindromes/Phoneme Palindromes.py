for t in range(int(input())):
 print(f"Test case #{t+1}:")
 L=eval('input(),'*int(input()))
 for _ in[0]*int(input()):
  s=input();t=s
  for p in L:t=t.replace(*p.split())
  print(s,'YNEOS'[t!=t[::-1]::2])
 print()