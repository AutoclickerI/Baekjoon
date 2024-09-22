for i in[*open(0)][1:]:
    for s in i.split():print(end=chr(s.count('M')*16+s.count('O')))
    print()