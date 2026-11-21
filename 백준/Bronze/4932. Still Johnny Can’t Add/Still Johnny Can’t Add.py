I=input
for T in range(int(I())):n=int(I());l=eval('[*map(int,I().split())],'*n);print(f'{T+1}.','YNEOS'[any(1<len({j[i+1]-j[i]for j in l})for i in range(n-1))::2])