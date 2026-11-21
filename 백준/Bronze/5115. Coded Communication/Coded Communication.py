I=input
for T in range(int(I())):s=[I()for i in range(int(I().split()[0]))];k=I();print(f'Data Set {T+1}:\n{min(sum(v!=w for v,w in zip(i,k))for i in s)}\n')