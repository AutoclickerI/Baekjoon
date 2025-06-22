for T in range(1,int(input())+1):
    C=int(input())
    I=int(input())
    *l,=map(int,input().split())
    for i in range(I):
        for j in range(i+1,I):
            if l[i]+l[j]==C:
                print(f'Case #{T}:',i+1,j+1)