# [Diamond II] Kill switch (Hard) - 27669 

[문제 링크](https://www.acmicpc.net/problem/27669) 

### 성능 요약

메모리: 4528 KB, 시간: 0 ms

### 분류

그래프 이론, 브루트포스 알고리즘, 애드 혹, 해 구성하기, 분할 정복

### 제출 일자

2026년 1월 25일 07:54:05

### 문제 설명

<p>A kill switch is a mechanism used to shut off a device in an emergency situation.</p>

<p>Jeremy was hired as a contractor by a shady software company. After he finished his work the company pointed to a loophole in the contract and refused to pay him anything for his work. Little do they know that Jeremy suspected foul play and thus he hid a kill switch in his code.</p>

<p>You are given the implementation of a function that <em>pretends</em> to sort an array of 32-bit unsigned integers into a non-decreasing order. Find the shortest input the function <em>fails</em> to sort.</p>

### 입력 

 <p>In each subproblem there are two input files: one is a <a href="https://upload.acmicpc.net/7ab18f20-36c3-4d44-b11c-6b243188b560/">C++ implementation</a> and the other a <a href="https://upload.acmicpc.net/382b7085-f31a-4e3e-87f0-4920a17e3097/">Python implementation</a> of the same function.</p>

<p>(You may assume that if the answer is <em>n</em>, the two programs behave the same way at least on all valid inputs of size up to <em>n</em> + 47. Note that huge inputs may cause integer overflows in the C++ implementation. Such inputs are not a part of this problem and they can be safely ignored.)</p>

### 출력 

 <p>Your output file should contain two lines. The first line should contain a nonnegative integer <em>n</em>: the smallest possible length of an array that is not sorted correctly. The second line should contain one possible initial content of the array: the sequence <em>A</em>[0],…,<em>A</em>[<em>n</em> − 1]. These values must satisfy 0 ≤ <em>A</em>[<em>i</em>]<2<sup>32</sup>.</p>

