d={}
exec('d[c]=d.get(c:=len(input().split()),0)+1;'*int(input()))
for i in sorted(d):print(i,d[i])