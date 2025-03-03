for _ in[0]*int(input()):
    a,b=input().split()
    ml=max(len(a),len(b))
    v=int(a)*int(b)
    a=('1'*ml+a)[-ml:]
    b=('1'*ml+b)[-ml:]
    print(+(v==int(''.join(str(int(i)*int(j))for i,j in zip(a,b)))))