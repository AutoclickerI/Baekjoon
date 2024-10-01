import sys
input=sys.stdin.readline

def main():
    # Read the first input line
    n, m = map(int, input().split())
    
    # Initialize a list of sets to track languages for each problem
    problem_languages = [set() for _ in range(n)]
    
    # Process each solution
    for _ in range(m):
        p, L = map(int, input().split())
        problem_languages[p - 1].add(L)
    
    # Collect all contest-ready problems
    contest_ready = []
    for i in range(n):
        if 1 in problem_languages[i] and 2 in problem_languages[i]:
            contest_ready.append(i + 1)
    
    # Output the contest-ready problems sorted in numerical order
    for problem in sorted(contest_ready):
        print(problem)

# Call the main function to execute the program
if __name__ == "__main__":
    main()