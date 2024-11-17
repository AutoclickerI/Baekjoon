while'#'<(s:=input()):
    t=0
    for i in s:
        t*=8
        t+='-\(@?>&%'.find(i)
    print(t)