for i in[*open(0)][1:]:
    d=[1]*10
    for _ in[0]*~-int(i):
        d=[sum(d[:-~j])for j in range(10)]
    print(sum(d))