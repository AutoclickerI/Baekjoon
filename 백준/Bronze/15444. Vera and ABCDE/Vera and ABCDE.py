input()
for i in zip(*[[[f'{k+159<<1:015b}'.translate({48:42,49:46})for k in b'HA'][ord(i)-65][j::5]for j in range(5)]for i in input()]):print(*i,sep='')