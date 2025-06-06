for T in range(int(input())):
    N,K=map(int,input().split())
    print(f'Case #{T+1}:',(' '+input().replace(' ','  ')+' ').count(' '+'  '.join(map(str,range(K,0,-1)))+' '))