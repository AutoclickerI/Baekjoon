s={input()for _ in[0]*int(input())}
for _ in[0]*int(input()):
    t=input()
    if t in s:
        print(1)
    elif t in[i+j for i in s for j in s]:
        print(2)
    else:
        print(0)