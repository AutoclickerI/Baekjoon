# [Silver III] Technology Planning (Small1) - 12413 

[문제 링크](https://www.acmicpc.net/problem/12413) 

### 성능 요약

메모리: 32412 KB, 시간: 44 ms

### 분류

백트래킹, 브루트포스 알고리즘

### 제출 일자

2025년 3월 26일 10:56:42

### 문제 설명

<p>You are playing a culture simulation game, in which your culture can develop various technologies. Some technologies depend upon others; if technology A depends upon technology B, you cannot develop B until you have developed A. Your culture can work on only one technology at a time.</p>

<p>In the game, you have goals which require particular technologies. You have decided to write a program to help you by planning out the order in which to develop technologies.</p>

### 입력 

 <p>The input to your program starts with the number of test cases, <strong>T</strong>, on a line by itself. <strong>T</strong> test cases follow. Each one consists of:</p>

<ul>
	<li>One line with an integer, <strong>M</strong>, which is the number of technological dependencies.</li>
	<li><strong>M</strong> lines, each one containing two technology names, separated by a colon (':'). The first technology depends on the second one.</li>
	<li>One line with an integer, <strong>Q</strong>, which is the number of goal technologies.</li>
	<li><strong>Q</strong> lines, each naming a goal technology.</li>
</ul>

<p>Each technology name is a sequence of alphanumeric characters (letters or numbers). Technology names are case-sensitive.</p>

<h3>Limits</h3>

<ul>
	<li><strong>T</strong> ≤ 25</li>
	<li><strong>M</strong> ≥ 1</li>
	<li><strong>Q</strong> ≥ 1</li>
	<li>There will be no cycles in the dependency graph.</li>
	<li><strong>M</strong> ≤ 10</li>
	<li><strong>Q</strong> ≤ 10.</li>
</ul>

### 출력 

 <p>The output for each case should start with a line of the form "Case #<strong>C</strong>: <strong>D</strong>", where <strong>C</strong> is the case number, starting from 1, and <strong>D</strong> is the smallest possible number of technologies that have to be researched. The next <strong>D</strong> lines should each contain one technology, in the order that they need to be researched.</p>

<p>If there are several possible correct orderings, any one of them is acceptable.</p>

