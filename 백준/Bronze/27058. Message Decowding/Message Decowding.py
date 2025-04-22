z,t=open(0)
print(t.translate(dict(zip(range(65,123),z.upper()+" "*5+z))))