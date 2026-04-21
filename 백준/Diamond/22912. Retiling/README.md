# [Diamond V] Retiling - 22912 

[문제 링크](https://www.acmicpc.net/problem/22912) 

### 성능 요약

메모리: 114232 KB, 시간: 272 ms

### 분류

최대 유량, 최소 비용 최대 유량, 그래프 이론

### 제출 일자

2026년 4월 21일 21:29:17

### 문제 설명

<p>Cody-Jamal's latest artistic installment is a tiled kitchen floor that can be retiled to different patterns. The floor consists of a matrix of R rows and C columns of square tiles. Each tile is reversible, one side is magenta and the other one is green.</p>

<p>To retile the kitchen, there are two allowed operations:</p>

<ul>
	<li>flip a tile, changing its visible color from magenta to green, or vice versa, and</li>
	<li>swap two adjacent tiles (horizontally or vertically, but not diagonally), without flipping either.</li>
</ul>

<p>Viewing Cody-Jamal's artistic floor is free, but interacting with it is not. Performing a single flip operation costs F coins, and performing a single swap operation costs S coins.</p>

<p>You can see the current state of the floor and want to turn it into a particular pattern. What is the minimum amount of coins you need to spend to achieve your goal?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, T. T test cases follow. The first line of a test case contains 4 integers: R, C, F and S, the number of rows and columns of the floor, the cost in coins of flipping and the cost in coins of swapping, respectively. Then, 2⋅R lines follow. The first R lines contain C characters each. The j⁠-th character of the i⁠-th of these lines represents the current state of the tile in the i⁠-th row and j⁠-th column. The character is M if the currently visible side is magenta and G otherwise. The last R lines also contain C characters each. The j⁠-th character of the i⁠-th of these lines represents the color you want for the tile in the i⁠-th row and j⁠-th column, using the same character code as for the current state.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where x is the test case number (starting from 1) and y is the minimum amount of coins you need to spend to perform operations that allow you to change the tile colors from their current state to your intended one.</p>

