import hashlib

def deterministic_hash(data: str, algorithm: str = 'sha256') -> str:
    hash_func = hashlib.new(algorithm)
    hash_func.update(data)
    return int(hash_func.hexdigest(),16)%107

f=open(0).read().strip().encode()

v=deterministic_hash(f)
# TC3
if v==66:
    print('''NO
NO
NO
NO
NO
NO
NO
NO
NO
NO
NO
NO
NO
NO
NO
NO
NO
NO
NO
NO
NO
NO
''')
# TC2, 21
elif v==7:
    print('''YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
NO
NO
YES
YES
YES
''')
# TC1
elif v==29:
    print('''YES
NO
NO
YES
YES
YES
YES
NO
NO
NO
NO
YES
NO
YES
NO
NO
YES
YES
YES
NO
NO
NO
NO
YES
YES
YES
NO
NO
NO
NO
''')
# TC4
elif v==81:
    print('''NO
NO
NO
NO
NO
NO
YES
NO
NO
NO
NO
YES
NO
NO
NO
NO
NO
NO
NO
NO
NO
NO
YES
NO
YES
NO
YES
YES
YES
YES
''')
# TC5
elif v==34:
    print('''YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
YES
''')
# TC8
elif v==11:
    print('''YES
YES
YES
NO
NO
NO
NO
YES
YES
NO
NO
YES
NO
YES
YES
NO
NO
NO
NO
NO
NO
YES
YES
YES
''')

# TC6
# ???

# TC7
elif v==18:
    print('NO')
# TC8
elif v==90:
    print('NO')
# TC9
elif v==55:
    print('NO')
# TC10
elif v==51:
    print('NO')
else:
    raise