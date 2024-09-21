def valid_in_base(num_str, base):
    return all(int(digit) < base for digit in num_str)

def convert_to_decimal(num_str, base):
    return sum(int(digit) * (base ** i) for i, digit in enumerate(reversed(num_str)))

def main():
    expression = input().strip()
    A, operator, B, _, C = expression.split()
    
    valid_bases = []
    
    for base in range(2, 11):
        if valid_in_base(A, base) and valid_in_base(B, base) and valid_in_base(C, base):
            A_dec = convert_to_decimal(A, base)
            B_dec = convert_to_decimal(B, base)
            C_dec = convert_to_decimal(C, base)
            
            if operator == '+':
                if A_dec + B_dec == C_dec:
                    valid_bases.append(base)
            elif operator == '-':
                if A_dec - B_dec == C_dec:
                    valid_bases.append(base)
            elif operator == '*':
                if A_dec * B_dec == C_dec:
                    valid_bases.append(base)
    
    print(len(valid_bases))
    if valid_bases:
        print(' '.join(map(str, valid_bases)))

if __name__ == "__main__":
    main()
