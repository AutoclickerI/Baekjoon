s=0
while'TOTAL'!=input():s+=eval(input().replace(*' *'))
print(['PAY','PROTEST'][s<int(input())])