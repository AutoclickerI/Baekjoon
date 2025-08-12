a='*'.join(input())
print('YNEOS'[all(eval(a[:i]+'-1'+a[i:])for i in range(1,len(a),2))::2])