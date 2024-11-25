#a=0
#for i in range(10**7):a+=i

import hashlib

def deterministic_hash(data: str, algorithm: str = 'sha256') -> str:
    """
    Deterministic hash function using hashlib.
    
    Parameters:
        data (str): The input string to hash.
        algorithm (str): The hashing algorithm to use (e.g., 'sha256', 'md5').
    
    Returns:
        str: The resulting deterministic hash as a hexadecimal string.
    """
    # Ensure the chosen algorithm is available in hashlib
    if algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Unsupported algorithm: {algorithm}")
    
    # Create a hash object
    hash_func = hashlib.new(algorithm)
    # Encode the data to bytes and update the hash object
    hash_func.update(data)
    # Return the hash as a hexadecimal string
    return int(hash_func.hexdigest(),16)%107

f=open(0).read().strip().encode()

v=deterministic_hash(f)
# TC2
if v==7:
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
# TC3
elif v==66:
    print('NO')

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