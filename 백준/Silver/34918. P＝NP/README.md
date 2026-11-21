# [Silver IV] P=NP - 34918 

[문제 링크](https://acmicpc.net/problem/34918) 

### 성능 요약

메모리: 33432 KB, 시간: 56 ms

### 분류

문자열, 애드 혹

### 제출 일자

2025년 12월 11일 11:35:47

### 문제 설명

<p>Busy Beaver has a string $A$ made up of characters <code>P</code> and <code>N</code>. He can perform two types of operations on $A$:</p>

<ul>
<li>Pick a substring<sup>1</sup> <code>P</code> and replace it with <code>NP</code>.</li>
<li>Pick a substring <code>NP</code> and replace it with <code>P</code>.</li>
</ul>

<p>Busy Beaver has a target string $B$. Determine if he can turn $A$ into $B$ after some number of operations.</p>

<hr>
<p><sup>1</sup>A substring of length $k$ is a contiguous sequence of $k$ adjacent characters of a string.</p>

### 입력 

 <p>The first line contains a single integer $T$ ($1 \leq T \leq 10^4$) --- the number of test cases.</p>

<p>The only line of each test case contains the strings $A$ and $B$ ($1 \leq |A|, |B| \leq 10^5$), consisting of characters <code>P</code> and <code>N</code>.</p>

<p>The sum of $|A|+|B|$ across all test cases does not exceed $2 \cdot 10^5$.</p>

### 출력 

 <p>For each test case, output <code>YES</code> if Busy Beaver can turn $A$ into $B$ using the operations above, and <code>NO</code> otherwise.</p>

