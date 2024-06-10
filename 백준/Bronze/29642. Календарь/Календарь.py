n, k = map(int, input().split())

days_per_month = list(map(int, input().split()))
if k > 0:
    broken_digits = input().split()
else:
    broken_digits = []
db = [len({*broken_digits}&{*str(i+1)})>0 for i in range(max(days_per_month))]
s=[0]
for i in db:
    s+=s[-1]+i,
# Output the result
print(sum(s[i]for i in days_per_month))