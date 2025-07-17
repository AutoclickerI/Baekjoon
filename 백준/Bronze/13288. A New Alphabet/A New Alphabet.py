d=r"[-] | _| |< 1 []\/[] []\[] 0 |D (,) |Z $ '][' |_| \/ \/\/ }{ `/ 2 @ 8 ( |) 3 # 6".split()
for i in input().lower():print(end=d[ord(i)%26]*('`'<i)or i)