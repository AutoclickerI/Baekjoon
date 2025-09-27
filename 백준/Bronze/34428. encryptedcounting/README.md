# [Bronze I] encryptedcounting - 34428 

[문제 링크](https://www.acmicpc.net/problem/34428) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

구현, 문자열

### 제출 일자

2025년 9월 27일 12:24:18

### 문제 설명

<p>You and your friends have devised a clever method of encrypting numbers and have been using the method to talk to each other for the past few days. Unfortunately, your decryption tool broke so you need to create a new one. </p>

<p>The encryption is based on a sequence, where the next element of the sequence is derived by the "spoken" representation of the previous element. The encrypted version of a number, $M$, is derived by finding the $M^{th}$ member of the sequence starting from some initial seed, $S$. To decrypt a ciphertext, $C$, one needs to find how many $M$ iterations it took to reach that $C$ from the given seed, $S$.</p>

<p>Here is an example of how the sequence is generated:</p>

<pre>// Comments describe how the number on the left 
// was generated from the previous number.

0. 12     // "12" is our seed
1. 1112   // "12" is "one one" and "one two" -> 11, 12 -> 1112
2. 3112   // "1112" is "three ones" and "one two" -> 31, 12 -> 3112
3. 132112 // "3112" is "one three" and "two ones" and "one two" -> 132112
4. 1113122112
5. 311311222112
</pre>

<p>Your friend sends you a single line containing the seed, $S$, and the ciphertext, $C$. Output the decrypted number, $M$, which describes the number of iterations your encryption algorithm takes to reach $C$ when starting at $S$. </p>

### 입력 

 <p>Two integers, $S$ and $C$, that are separated by a space. $S$ has less than $10$ digits, and $C$ has less than $200$ digits. Suppose the input is:</p>

<pre>12 132112</pre>

<p>where $S = 12$ and $C = 132112$. You then need to calculate, $M$, which would be $3$ in this case (since the third iteration of the seed produces $132112$). </p>

### 출력 

 <p>Output a single integer, $M$, that is the number of iterations it takes to reach $C$ from the seed $S$. The output for the above example would look like:</p>

<pre>3</pre>

<p> </p>

