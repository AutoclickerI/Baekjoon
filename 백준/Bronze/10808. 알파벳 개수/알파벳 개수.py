from collections import Counter
a=dict(Counter(input()))
for p in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
    try:
        print(a[p],end=' ')
    except:
        print(0,end=' ')