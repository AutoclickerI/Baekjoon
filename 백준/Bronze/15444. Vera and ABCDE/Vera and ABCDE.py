l=[[f'{ord(i):b}'.translate({49:42,48:46})[j*3:-~j*3]for j in range(5)]for i in'篭篯礧筯秧']
input()
for i in zip(*[l[ord(i)-65]for i in input()]):print(*i,sep='')