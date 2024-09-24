R=lambda s:s[::-1]
print(eval("'"+input().replace("(","'+R('").replace(")","')+'")+"'"))