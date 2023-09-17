s=input()
for _ in[0]*int(input()):
    t=input()
    print(sum(i in s for i in t),sum(i==j for i,j in zip(s,t)))