# [Silver III] A Cappella Recording - 31519 

[문제 링크](https://www.acmicpc.net/problem/31519) 

### 성능 요약

메모리: 42036 KB, 시간: 80 ms

### 분류

그리디 알고리즘, 정렬

### 제출 일자

2024년 9월 20일 23:20:53

### 문제 설명

<p>Geoffry is preparing an a cappella composition where he sings the entire song by himself.</p>

<p>Each note of the song has a pitch between $0$ and $10^9$. Because of the varying pitches in the song, Geoffry will record himself singing multiple times. In a single recording, he will pick some subset of the notes to sing and he will sing exactly those notes. To avoid straining his voice too much, within a single recording, there is a limit to the difference between the maximum pitch and the minimum pitch among the notes he sings.</p>

<p>Compute the minimum number of times that Geoffry can record himself singing the song and each note is sung in at least one of the recordings.</p>

### 입력 

 <p>The first line contains two integers $n$ and $d$ ($1 \le n \le 10^5, 0 \le d \le 10^9$), where $n$ is the number of notes in Geoffry's song, and $d$ is the largest difference between the minimum pitch and the maximum pitch that Geoffry can handle.</p>

<p>Each of the next $n$ lines contains a single integer $p$ ($0 \le p \le 10^9$). These are the pitches of the notes in Geoffry's song, in the order that they are to be sung.</p>

### 출력 

 <p>Output a single integer, which is the minimum number of times that Geoffry can record himself singing the song and each note is sung in at least one of the recordings.</p>

