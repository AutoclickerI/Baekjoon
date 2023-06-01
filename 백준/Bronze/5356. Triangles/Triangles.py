for _ in[0]*int(input()):
    p,q=input().split()
    for i in range(int(p)):
        print((i+1)*chr(65+(ord(q)+i-65)%26))
    print()