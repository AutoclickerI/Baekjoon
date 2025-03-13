def solve():
    from decimal import Decimal
    import sys
    lines = sys.stdin.read().splitlines()
    if not lines: 
        return
    a, b = lines[0].strip(), lines[1].strip()
    da, db = Decimal(a), Decimal(b)
    # Convert each decimal string into a tuple: (integer part, fractional part as integer)
    ta = tuple(map(int, a.split('.')))
    tb = tuple(map(int, b.split('.')))
    
    # Determine the ordering by actual decimal comparison
    if da > db:
        dec_order = 1
        larger = a
    else:
        dec_order = -1
        larger = b
        
    # Determine the ordering by tuple comparison
    if ta > tb:
        tuple_order = 1
    elif ta < tb:
        tuple_order = -1
    else:
        tuple_order = 0

    # If both comparisons agree and the tuple order is not equal (0), print the larger decimal;
    # otherwise, output -1.
    if dec_order == tuple_order and tuple_order != 0:
        sys.stdout.write(larger)
    else:
        sys.stdout.write("-1")

if __name__ == '__main__':
    solve()
