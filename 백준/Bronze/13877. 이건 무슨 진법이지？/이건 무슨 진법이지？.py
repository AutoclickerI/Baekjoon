for _ in[0]*int(input()):
    c,n=input().split()
    print(c,'0'*('7'<max(n))or int(n,8),int(n),int(n,16))