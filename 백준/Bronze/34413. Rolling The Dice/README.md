# [Bronze II] Rolling The Dice - 34413 

[문제 링크](https://www.acmicpc.net/problem/34413) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

수학, 문자열, 사칙연산, 파싱

### 제출 일자

2025년 9월 25일 13:33:49

### 문제 설명

<p>In Dungeons and Dragons, we use dice rolls very often to determine which actions succeed and which fail. There are many different dice with varying numbers of sides so we have a shorthand for representing different rolls. A single roll is written as "d#," with the "#" representing the number of sides on the die. If you need to roll multiple dice of the same type, there will be a number before the "d". For example, if you are required to roll 4d6, you would roll four six-sided dice and add the results together. There will also be a + after the notation, meaning that you add that number to the total results of the dice (not to each individual die rolled).</p>

<p>Higher numbers are better, and I want to make my character as powerful as possible, so I need to know what number I'll get on average for different rolls. It's relatively simple to do statistics on dice because every value has an equal chance of being rolled. <strong>If you average the minimum value and the maximum value of the roll, it will give you the value that you would get on average if you rolled it many times.</strong> For example, the roll 2d6+5 has a minimum value of $7$ if you roll two 1s and a maximum value of $17$ if you roll two $6$'s which gives an average of $12$ overall (for 2d6+5). Given the notation for a roll, find the average value of that roll.</p>

### 입력 

 <p>The input will be a single line in the form of "XdY+Z". X, Y, and Z are all integers and will fall within the same range, $1 \le X, Y, Z \le 100$.</p>

### 출력 

 <p>Your program needs to output the average value that you would expect for the given roll values.</p>

