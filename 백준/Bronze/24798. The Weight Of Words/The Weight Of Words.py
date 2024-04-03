l,w=map(int,input().split())
print(['impossible',''.join(chr(96+w//l+(i<w%l))for i in range(l))][l<=w<=l*26])