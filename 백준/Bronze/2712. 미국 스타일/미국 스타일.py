unit={'kg':'lb','l':'g','lb':'kg','g':'l'}
k={'kg':2.2046,'lb':0.4536,'l':0.2642,'g':3.7854}
for _ in[0]*int(input()):
    p,q=input().split()
    print(f'{float(p)*k[q]:.4f}',unit[q])