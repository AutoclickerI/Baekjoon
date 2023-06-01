for i in[0]*int(input()):
    p,q,r,s,a,b,c,d=map(int,input().split())
    P,Q,R,S=max(1,p+a),max(1,q+b),max(0,r+c),s+d
    print(P+5*Q+2*(R+S))