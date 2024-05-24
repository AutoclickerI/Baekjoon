a,b,c,d=zip(*eval('map(int,input().split()),'*int(input())))
print(max(min(b)-max(a),0)*max(min(d)-max(c),0))