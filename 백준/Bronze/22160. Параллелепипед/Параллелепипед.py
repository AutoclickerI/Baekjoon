for i in[*open(0)][:-1]:
    s=sorted(map(int,i.split()))
    print('yneos'[len({*s[:4]})+len({*s[4:8]})+len({*s[8:]})>3::2])