import sys
input=sys.stdin.readline
log={}
cnt=0
for i in range(int(input())):
 chat = input()
 if chat == "ENTER\n":log = {};continue
 if chat not in log:log[chat] = True;cnt += 1
print(cnt)