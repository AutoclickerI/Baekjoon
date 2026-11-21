# [Bronze II] Transform the String - 23716 

[문제 링크](https://acmicpc.net/problem/23716) 

### 성능 요약

메모리: 42672 KB, 시간: 10440 ms

### 분류

구현, 문자열

### 제출 일자

2025년 3월 17일 13:00:54

### 문제 설명

<p>You are given a string&nbsp;$S$&nbsp;which denotes a padlock consisting of lower case English letters. You are also given a string $F$ consisting of set of favorite lower case English letters. You are allowed to perform several operations on the padlock. In each operation, you can change one letter of the string to the one following it or preceding it in the alphabetical order. For example: for the letter&nbsp;<code>c</code>, you are allowed to change it to either&nbsp;<code>b</code>&nbsp;or&nbsp;<code>d</code>&nbsp;in an operation. The letters can be considered in a cyclic order, i.e., the preceding letter for letter&nbsp;<code>a</code>&nbsp;would be letter&nbsp;<code>z</code>. Similarly, the following letter for letter&nbsp;<code>z</code>&nbsp;would be letter&nbsp;<code>a</code>.</p>

<p>Your aim is to find the minimum number of operations that are required such that each letter in string&nbsp;$S$&nbsp;after applying the operations, is present in string $F$.</p>

### 입력 

 <p>The first line of the input gives the number of test cases,&nbsp;$T$.&nbsp;$T$&nbsp;test cases follow.</p>

<p>Each test case consists of two lines.</p>

<p>The first line of each test case contains the string $S$.</p>

<p>The second line of each test case contains the string&nbsp;$F$.</p>

### 출력 

 <p>For each test case, output one line containing&nbsp;<code>Case #x:&nbsp;y</code>, where $x$ is the test case number (starting from 1) and&nbsp;$y$&nbsp;is the minimum number of operations that are required such that each letter in string&nbsp;$S$&nbsp;after applying the operations, is one of the characters in string&nbsp;$F$.</p>

