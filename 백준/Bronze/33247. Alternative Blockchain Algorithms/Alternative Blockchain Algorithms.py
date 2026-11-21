def main():
    import sys
    # Read all input tokens at once for efficiency.
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    
    # The first number is N, the number of blocks.
    n = int(data[0])
    index = 1
    
    # Read the genesis block.
    try:
        block_id = int(data[index]); index += 1
        parent_id = int(data[index]); index += 1
        amount = int(data[index]); index += 1
    except Exception:
        print("INVALID")
        return
    
    # Check if the genesis block is valid.
    if parent_id != 0:
        print("INVALID")
        return
    
    # Initialize balance and record the id of the current block.
    balance = amount
    if balance < 0:
        print("NO_MONEY")
        return
    prev_block_id = block_id
    
    # Process the remaining blocks.
    for _ in range(n - 1):
        try:
            block_id = int(data[index]); index += 1
            parent_id = int(data[index]); index += 1
            amount = int(data[index]); index += 1
        except Exception:
            print("INVALID")
            return
        
        # Verify that the parent's id matches the id of the previous block.
        if parent_id != prev_block_id:
            print("INVALID")
            return
        
        # Update the balance.
        balance += amount
        if balance < 0:
            print("NO_MONEY")
            return
        
        # Set the current block's id as the previous block id for the next iteration.
        prev_block_id = block_id
        
    # If all blocks are valid and balance never went negative, output the balance.
    print(balance)

if __name__ == '__main__':
    main()
