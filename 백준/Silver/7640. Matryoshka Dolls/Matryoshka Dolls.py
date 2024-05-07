while n:=int(input()):
 d={}
 for _ in[0]*n:d[i]=d.get(i:=int(input()),0)+1
 print(max(d.values()))