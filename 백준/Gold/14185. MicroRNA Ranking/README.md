# [Gold IV] MicroRNA Ranking - 14185 

[문제 링크](https://www.acmicpc.net/problem/14185) 

### 성능 요약

메모리: 212160 KB, 시간: 4480 ms

### 분류

방향 비순환 그래프, 자료 구조, 그래프 이론, 우선순위 큐, 위상 정렬

### 제출 일자

2025년 3월 26일 11:17:06

### 문제 설명

<p>Ahlaam is a computer science student, doing her master thesis on a bioinformatics project about MicroRNAs, special molecule types found in cells. During her thesis, she wants to find microRNAs relevant to a specific health factor in human beings.</p>

<p>Ahlaam has designed k microRNA ranking algorithms, each of which ranks microRNAs from a specific point of view. There are n microRNAs numbered 1 through n, and each algorithm produces one permutation of these n microRNAs. In the permutation produced by each algorithm, the first microRNA is inferred by the algorithm as the most relevant one to the health factor, and the last microRNA is inferred as the least relevant one.</p>

<p>Ahlaam wants to report a consensus ranking on microRNAs. In a consensus ranking, if microRNA i is ranked before another mircroRNA j, then at least half of the algorithms should have ranked i before j. Write a program to help Ahlaam find a consensus ranking.</p>

### 입력 

 <p>There are multiple test cases in the input. The first line of each test contains two space-separated integers n (1 ≤ n ≤ 1000) and k (1 ≤ k ≤ 200), the number of microRNAs and the number of ranking algorithms, respectively. Then, there are k lines, where the i-th line contains a permutation of n numbers 1, . . . , n, representing the output of the i-th ranking algorithm. The input terminates with a line containing 0 0 which should not be processed.</p>

### 출력 

 <p>For each test case, print a single line containing a permutation of n numbers 1, . . . , n, representing a possible consensus ranking. If there are more than one correct consensus rankings, print the first one in lexicographic order (a sequence a<sub>1</sub>, · · · , a<sub>n</sub> is lexicographically less than a sequence b<sub>1</sub>, · · · , b<sub>n</sub> iff there exists a positive integer j such that a<sub>i</sub> = b<sub>i</sub> for all 1 ≤ i ≤ j − 1 and a<sub>j</sub> < b<sub>j</sub> ) . If no such a ranking exists, write “No solution” instead.</p>

