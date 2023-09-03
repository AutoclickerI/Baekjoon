while(s:=input())>'00':
    p,q,r=map(eval,s.split())
    print(f'Horizontal DPI: {q*337**.5/16/p:.2f}\nVertical DPI: {r*337**.5/9/p:.2f}')