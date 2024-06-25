# [Gold III] “Roman” corridor - 7767 

[문제 링크](https://www.acmicpc.net/problem/7767) 

### 성능 요약

메모리: 122724 KB, 시간: 644 ms

### 분류

백트래킹

### 제출 일자

2024년 6월 25일 10:53:46

### 문제 설명

<p>Let’s remind the notation of Roman numerals. The notation is for natural numbers from 1 to 3999. Capital Latin letters ‘I’, ‘V’, ‘X’, ‘L’, ‘C’, ‘D’, ‘M’ and their combinations are used to represent so called atomic numbers (see the table below).</p>

<ul>
	<li>1 – I</li>
	<li>4 – IV</li>
	<li>5 – V</li>
	<li>9 – IX</li>
	<li>10 – X</li>
	<li>40 – XL</li>
	<li>50 – L</li>
	<li>90 – XC</li>
	<li>100 – C</li>
	<li>400 – CD</li>
	<li>500 – D</li>
	<li>900 – CM</li>
	<li>1000 – M</li>
</ul>

<p>To put down a number N it is necessary to find the greatest atomic number K which is not greater then N. The Roman notation of the found number K is put down, and the process is repeated for (N-K).</p>

<p>The Roman numerals are put down from left to right without spaces. Thus, the number 999 in the Roman notation is CMXCIX (but not IM, as somebody may think).</p>

<p>You need to pass through a rectangular corridor. The corridor is n meters width and m meters long (1 ≤ n, m ≤ 15, n*m ≤ 100). It is laid out by square tiles. Each tile is 1 meter width and has a ‘Roman’ symbol on it: ‘I’, ‘V’, ‘X’, ‘L’, ‘C’, ‘D’ or ‘M’. When passing the corridor, you move from one tile to another. From the current tile you may only move to one of adjacent tiles, vertically or horizontally (but not across). You start at the left and end at the right (see the picture below). </p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/e27e0e09-e2fc-4cb4-ad2d-2bc8d6ed7982/-/preview/" style="width: 200px; height: 143px;"></p>

<p>Can you pass through the corridor so that the sequence of symbols on the tiles composing your path was a correct number in the Roman notation? Among all possible solutions you need to find the minimal number.</p>

### 입력 

 <p>The first line contains numbers n and m, separated by one or more spaces. Each of the next n lines consists of m characters describing tiles.</p>

### 출력 

 <p>The output contains one line with the found Roman number or the word NO if it is impossible to pass through the corridor in the required way. </p>

