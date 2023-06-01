for _ in[0]*int(input()):
    d={}
    for _ in[0]*int(input()):
        p,q=input().split()
        if d.get(q):
            d[q]+=1
        else:
            d[q]=1
    num=1
    for i in d.values():
        num*=(i+1)
    print(num-1)