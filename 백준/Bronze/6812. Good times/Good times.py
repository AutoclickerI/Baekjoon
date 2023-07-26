n=int(input())+2400
print(n%2400,'in Ottawa')
print((n-300)%2400,'in Victoria')
print((n-200)%2400,'in Edmonton')
print((n-100)%2400,'in Winnipeg')
print(n%2400,'in Toronto')
print((n+100)%2400,'in Halifax')
print((n+100+[70,30][n%100<30])%2400,"in St. John's")