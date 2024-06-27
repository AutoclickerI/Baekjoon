# [Gold III] Word Search - 10290 

[문제 링크](https://www.acmicpc.net/problem/10290) 

### 성능 요약

메모리: 31120 KB, 시간: 2468 ms

### 분류

브루트포스 알고리즘, 많은 조건 분기, 구현

### 제출 일자

2024년 6월 27일 18:11:43

### 문제 설명

<p>A word search puzzle is a puzzle that involves a rectangular grid of letters and a list of words. The objective is to find and mark all those words, which are hidden inside the grid. The words may be placed horizontally, vertically, or diagonally, in either direction. When you have found a word, you mark all the letters in the grid that are involved. A letter may be part of multiple words. At the end, all the unmarked letters, from top to bottom and from left to right, form a message; this is the solution.</p>

<p>A certain magazine has a bunch of word search puzzles in it. They would like you to check, for each puzzle, that all words are actually in the grid. You should also be on the lookout for words that can be found in two (or more) different places – even if it does not influence the final solution. If all is well, just give the solution.</p>

### 입력 

 <p>On the first line one positive number: the number of test cases, at most 100. After that per test case:</p>

<ul>
	<li>one line with three integers n, h and w (1 ≤ n ≤ 256 and 1 ≤ h, w ≤ 32): the number of words and the height and width of the grid, respectively.</li>
	<li>h lines with w uppercase letters: the grid.</li>
	<li>n lines, each with a single string s (1 ≤ length(s) ≤ 32), consisting of uppercase letters only: the words to be found in the grid.</li>
</ul>

### 출력 

 <p>Per test case:</p>

<ul>
	<li>one line with a single string of uppercase letters: the solution. If there is a word that is not present in the grid, print “no solution” instead. If all words are present, but there is a word for which there are two (or more) different sets of letters that could be marked, print “ambiguous” instead. If all words are present and can be found uniquely in the grid, yet there are no unmarked letters remaining, print “empty solution” instead.</li>
</ul>

