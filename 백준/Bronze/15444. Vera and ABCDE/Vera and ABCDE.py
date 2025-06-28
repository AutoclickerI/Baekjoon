input()
for i in zip(*[[[f'{i:015b}'.translate({48:42,49:46})for i in[352,320,462,448,330]][ord(i)-65][j::5]for j in range(5)]for i in input()]):print(*i,sep='')