for _ in[0]*int(input()):
    _,q=input().split()
    l=input().split()
    if'C'<q:print(*[chr(64+int(i))for i in l])
    else:print(*[ord(i)-64for i in l])