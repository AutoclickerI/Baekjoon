# [Unrated] Similarity - 22792 

[문제 링크](https://www.acmicpc.net/problem/22792) 

### 성능 요약

메모리: 35560 KB, 시간: 64 ms

### 분류

문자열, 브루트포스 알고리즘, 기하학

### 제출 일자

2025년 10월 20일 06:18:37

### 문제 설명

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/385f3874-a2b3-4093-b826-cad5bfb1d3c5/-/preview/" style="width: 466px; height: 209px;"></p>

<p>Two polygons are similar if you can obtain the second polygon by a combination of scaling, rotating and flipping operations on the first polygon.</p>

<p>Your task is to determine if two given polygons are similar.</p>

<p>You are given two polygons whose sides are all horizontal and vertical lines. You are to determine if the two polygons are similar.</p>

### 입력 

 <p>The input contains one or more test cases. Each case contains two polygon definitions. A polygon definition is the number of the vertices of the polygon in the first line, followed by an ordered pair (x, y) of the vertices for the following lines. Format for each test case is shown below:</p>

<pre><number of vertices (n) of polygon 1>
<x1,y1>
<x2,y2>
.
.
.
<xn,yn>
<number of vertices (m) of polygon 2>
<x1,y1>
<x2,y2>
.
.
.
<xm,ym></pre>

<p>Input is terminated by “0”.</p>

<p>You can assume that the polygon resulting from connecting the vertices in sequence has only horizontal and vertical lines, and that the polygon formed is simple (i.e. it has no intersecting or overlapping edges). All vertex coordinates are integers, ranging from -30000 to +30000.</p>

### 출력 

 <p>Output <code>YES</code> if the polygons are similar; <code>NO</code>, if otherwise – one line per test case.</p>

