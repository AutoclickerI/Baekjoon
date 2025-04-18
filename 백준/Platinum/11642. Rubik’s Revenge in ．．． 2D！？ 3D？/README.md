# [Platinum IV] Rubik’s Revenge in ... 2D!? 3D? - 11642 

[문제 링크](https://www.acmicpc.net/problem/11642) 

### 성능 요약

메모리: 526640 KB, 시간: 5576 ms

### 분류

양방향 탐색, 그래프 이론, 구현, 중간에서 만나기

### 제출 일자

2025년 4월 19일 03:24:50

### 문제 설명

<p>You are given a puzzle that can be represented as a 4 × 4 grid of colored cells. The solved puzzle contains 4 monochromatic rows, in this order: red, green, blue, yellow. Although we will analyze this puzzle using its 2D representation, it is actually a 3D puzzle! Imagine that the grid is stretched over a torus (in other words, top edge is connected to the bottom one and left edge is connected to the right one). If you are not familiar with the word “torus” or what it is supposed to represent, just replace it with the word(s) “donut (with the hole in the middle)”.</p>

<p><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/11642/1.png" style="float:right; height:81px; width:309px">For each move you are allowed to either move one row left or right, or one column up or down. The fact that the outer edges are connected means that if a cell is “pushed out” of the grid, it will reappear on the other side of the grid. If you had a torus or a donut handy (or a cup! HAHAha...ha... <sniff>), this would be much clearer.</p>

<p>Given a description of a state of this puzzle, what is the minimum number of moves you need to solve it? Note that all possible puzzle configurations are solvable in less than 13 moves.</p>

### 입력 

 <p>Input file contains exactly 4 lines, containing 4 characters each, each character being either “R”, “G”, “B” or “Y’. The input will describe a valid state of the puzzle.</p>

### 출력 

 <p>Output the minimum number of moves needed to solve the given puzzle.</p>

