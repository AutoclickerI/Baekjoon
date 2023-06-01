for i in[0]*int(input()):
    p,q,r,s=map(int,input().split())
    if(r-s)*q>p:
        print("parallelize")
    elif(r-s)*q<p:
        print("do not parallelize")
    else:
        print("does not matter")