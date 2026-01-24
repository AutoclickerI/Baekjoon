# [Gold II] Kill switch (Easy) - 27668 

[문제 링크](https://www.acmicpc.net/problem/27668) 

### 성능 요약

메모리: 4528 KB, 시간: 0 ms

### 분류

정렬, 애드 혹, 해 구성하기

### 제출 일자

2026년 1월 25일 06:51:53

### 문제 설명

<p>A kill switch is a mechanism used to shut off a device in an emergency situation.</p>

<p>Jeremy was hired as a contractor by a shady software company. After he finished his work the company pointed to a loophole in the contract and refused to pay him anything for his work. Little do they know that Jeremy suspected foul play and thus he hid a kill switch in his code.</p>

<p>You are given the implementation of a function that <em>pretends</em> to sort an array of 32-bit unsigned integers into a non-decreasing order. Find the shortest input the function <em>fails</em> to sort.</p>

### 입력 

 <p>In each subproblem there are two input files: one is a <a href="https://upload.acmicpc.net/2f6ce261-6adf-44eb-82f8-4e2dfd3b6b5d/">C++ implementation</a> and the other a <a href="https://upload.acmicpc.net/08cffc0f-eb46-497f-877b-86d1642499e3/">Python implementation</a> of the same function.</p>

<p>(You may assume that if the answer is <em>n</em>, the two programs behave the same way at least on all valid inputs of size up to <em>n</em> + 47. Note that huge inputs may cause integer overflows in the C++ implementation. Such inputs are not a part of this problem and they can be safely ignored.)</p>

### 출력 

 <p>Your output file should contain two lines. The first line should contain a nonnegative integer <em>n</em>: the smallest possible length of an array that is not sorted correctly. The second line should contain one possible initial content of the array: the sequence <em>A</em>[0],…,<em>A</em>[<em>n</em> − 1]. These values must satisfy 0 ≤ <em>A</em>[<em>i</em>]<2<sup>32</sup>.</p>

