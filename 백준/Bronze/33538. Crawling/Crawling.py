def main():
    import sys
    input_data = sys.stdin.read().split()
    l = float(input_data[0])
    n = int(input_data[1])
    t = float(input_data[2])
    
    answer = "DOOMED"
    index = 3
    for _ in range(n):
        f = float(input_data[index])
        b = float(input_data[index + 1])
        index += 2
        
        total_time = l / f + l / b
        if total_time < t:
            answer = "HOPE"
            break
    
    print(answer)

if __name__ == "__main__":
    main()
