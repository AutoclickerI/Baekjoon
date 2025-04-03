# [Gold III] Dictionary - 10659 

[문제 링크](https://www.acmicpc.net/problem/10659) 

### 성능 요약

메모리: 34984 KB, 시간: 1940 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색, 문자열, 위상 정렬, 방향 비순환 그래프

### 제출 일자

2025년 4월 4일 00:02:56

### 문제 설명

<p>We found a dictionary of the Ancient Civilization Mayo (ACM) during excavation of the ruins. After analysis of the dictionary, we revealed they used a language that had not more than 26 letters. So one of us mapped each letter to a different English alphabet and typed all the words in the dictionary into a computer.</p>

<p>How the words are ordered in the dictionary, especially whether they are ordered lexicographically, is an interesting topic to many people. As a good programmer, you are requested to write a program to judge whether we can consider the words to be sorted in a lexicographical order.</p>

<p>Note: In a lexicographical order, a word always precedes other words it is a prefix of. For example, <code>ab</code> precedes <code>abc</code>, <code>abde</code>, and so on.</p>

### 입력 

 <p>The input consists of multiple datasets. Each dataset is formatted as follows:</p>

<pre>n
string<sub>1</sub>
...
string<sub>n</sub>
</pre>

<p>Each dataset consists of n+1 lines. The first line of each dataset contains an integer that indicates n (1 ≤ n ≤ 500). The i-th line of the following n lines contains string<sub>i</sub>, which consists of up to 10 English lowercase letters.</p>

<p>The end of the input is <code>0</code>, and this should not be processed.</p>

### 출력 

 <p>Print either <code>yes</code> or <code>no</code> in a line for each dataset, in the order of the input. If all words in the dataset can be considered to be ordered lexicographically, print <code>yes</code>. Otherwise, print <code>no</code>.</p>

