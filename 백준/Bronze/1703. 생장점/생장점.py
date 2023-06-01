for i in[*open(0)][:-1]:
 l=[*map(int,i.split())];n=1
 for _ in[0]*l.pop(0):n=n*l.pop(0)-l.pop(0)
 print(n)