# [Gold I] Binary Search Heap Construction - 6541 

[문제 링크](https://www.acmicpc.net/problem/6541) 

### 성능 요약

메모리: 4860 KB, 시간: 120 ms

### 분류

자료 구조, 파싱, 세그먼트 트리, 문자열

### 제출 일자

2024년 11월 13일 15:06:20

### 문제 설명

<p>Read the statement of problem G for the definitions concerning trees. In the following we define the basic terminology of heaps. A heap is a tree whose internal nodes have each assigned a priority (a number) such that the priority of each internal node is less than the priority of its parent. As a consequence, the root has the greatest priority in the tree, which is one of the reasons why heaps can be used for the implementation of priority queues and for sorting.</p>

<p>A binary tree in which each internal node has both a label and a priority, and which is both a binary search tree with respect to the labels and a heap with respect to the priorities, is called a treap. Your task is, given a set of label-priority-pairs, with unique labels and unique priorities, to construct a treap containing this data.</p>

### 입력 

 <p>The input contains several test cases. Every test case starts with an integer <em>n</em>. You may assume that <em>1<=n<=50000</em>. Then follow <em>n</em> pairs of strings and numbers <em>l<sub>1</sub>/p<sub>1</sub>,...,l<sub>n</sub>/p<sub>n</sub></em> denoting the label and priority of each node. The strings are non-empty and composed of lower-case letters, and the numbers are non-negative integers. The last test case is followed by a zero.</p>

### 출력 

 <p>For each test case output on a single line a treap that contains the specified nodes. A treap is printed as <em>(<left sub-treap><label>/<priority><right sub-treap>)</em>. The sub-treaps are printed recursively, and omitted if leafs.</p>

