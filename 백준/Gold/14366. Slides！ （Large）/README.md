# [Gold I] Slides! (Large) - 14366 

[문제 링크](https://www.acmicpc.net/problem/14366) 

### 성능 요약

메모리: 32412 KB, 시간: 56 ms

### 분류

애드 혹, 비트마스킹, 해 구성하기

### 제출 일자

2025년 3월 24일 15:03:56

### 문제 설명

<p>Gooli is a huge company that owns B buildings in a hilly area. The buildings are numbered from 1 to B.</p>

<p>The CEO wants to build a set of slides between buildings that she can use to travel from her office in building 1 to her favorite cafe in building B. Slides, of course, are one-way only, but the buildings are tall and have elevators, so a slide can start in any building and end in any other building, and can go in either direction. Specifically, for any two buildings x and y, you can build either zero or one slides from x to y, and you can build either zero or one slides from y to x. The exception is that no slides are allowed to originate in building B, since once the CEO reaches that building, there is no need for her to do any more sliding.</p>

<p>In honor of Gooli becoming exactly M milliseconds old, the design must ensure that the CEO has exactly M different ways to travel from building 1 to building B using the new slides. A way is a sequence of buildings that starts with building 1, ends with building B, and has the property that for each pair of consecutive buildings x and y in the sequence, a slide exists from x to y. Note that the CEO is not requiring that any building be reachable from any other building via slides.</p>

<p>Can you come up with any set of one or more slides that satisfies the CEO's requirements, or determine that it is impossible?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, T. T lines follow; each consists of one line with two integers B and M, as described above.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is the word <code>POSSIBLE</code> or <code>IMPOSSIBLE</code>, depending on whether the CEO's requirements can be fulfilled or not. If it is possible, output an additional B lines containing B characters each, representing a matrix describing a valid way to build slides according to the requirements. The j-th character of the i-th of these lines (with both i and j counting starting from 1) should be <code>1</code> if a slide should be built going from building i to building j, and <code>0</code> otherwise. The i-th character of the i-th line should always be <code>0</code>, and every character of the last line should be <code>0</code>.</p>

<p>If multiple solutions are possible, you may output any of them.</p>

