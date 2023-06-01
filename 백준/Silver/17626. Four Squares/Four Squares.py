n=int(input())
l=[i**2 for i in range(1,250)]
if n in l:
    print(1)
else:
    try:
        for p in l:
            if n-p in l:
                print(2)
                raise
        for p in l:
            for j in l:
                if n-p-j in l:
                    print(3)
                    raise
        print(4)
    except:
        pass