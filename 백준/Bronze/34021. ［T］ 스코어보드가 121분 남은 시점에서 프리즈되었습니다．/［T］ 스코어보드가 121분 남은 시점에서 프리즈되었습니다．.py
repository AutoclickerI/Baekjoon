for _ in[0]*int(input()):
    N,M,L=map(int,input().split())
    *S,=map(int,input().split())
    v=max([L]+[M-i for i in S if-1<i])
    print('The scoreboard has been frozen with',v,'minutes'[:7-(v==1)],'remaining.')