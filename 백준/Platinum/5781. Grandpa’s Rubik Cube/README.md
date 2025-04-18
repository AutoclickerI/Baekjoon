# [Platinum V] Grandpa’s Rubik Cube - 5781 

[문제 링크](https://www.acmicpc.net/problem/5781) 

### 성능 요약

메모리: 32412 KB, 시간: 48 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 4월 18일 23:34:41

### 문제 설명

<p>A very well-known toy/pastime, called Rubik's cube, consists of a cube as shown in Figure 1a, where letters stand for colors (e.g. B for blue, R for red,...). The goal of the game is to rotate the faces of the cube in such a way that at the end each face has a different color, as shown in Figure 1b. Notice that,</p>

<p><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/5781/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202016-06-13%20%EC%98%A4%ED%9B%84%205.02.17.png" style="height:193px; width:357px"><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/5781/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202016-06-13%20%EC%98%A4%ED%9B%84%205.02.17.png" style="height:193px; width:357px"></p>

<p>Figure 1: Rubik Cube</p>

<p>when a face is rotated, the configuration of colors in all the adjacent faces changes. Figure 2 illustrates a rotation of one of the faces. Given a scrambled configuration, reaching the final position can be quite challenging, as you may know.</p>

<p><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/5781/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202016-06-13%20%EC%98%A4%ED%9B%84%205.02.56.png" style="height:178px; width:542px"><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/5781/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202016-06-13%20%EC%98%A4%ED%9B%84%205.02.56.png" style="height:178px; width:542px"></p>

<p>Figure 2: Rotation example</p>

<p>But your grandpa has many years of experience, and claims that, given any configuration of the Rubik cube, he can come up with a sequence of rotations leading to a winning configuration.</p>

<p>In order to show all faces of the cube we shall represent the cube as in Figure 3a. The six colors are Yellow, Red, Blue, Green, White and Magenta (represented by their first letters).</p>

<p>You will be given an initial configuration and a list of rotations. A rotation will be represented by an integer number, indicating the face to be rotated and the direction of the rotation (a positive value means clockwise rotation, negative value means counter-clockwise rotation). Faces of the cube are numbered as shown in Figure 3b. You must write a program that checks whether the list of rotations will lead to a winning configuration.</p>

<p><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/5781/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202016-06-13%20%EC%98%A4%ED%9B%84%205.03.20.png" style="height:203px; width:530px"></p>

<p>Figure 3: Representation of the cube</p>

### 입력 

 <p>The input contains several test cases. The first line of the input is an integer which indicates the num- ber of tests. Each test description consists of ten lines of input. The first nine lines of a test will describe an initial configuration, in the format shown in Figure 3a. The next line will contain a list of rotations, ending with the value 0.</p>

<p> </p>

### 출력 

 <p>For each test case your program should print one line. If your grandpa is correct, print “Yes, grandpa!”, otherwise print “No, you are wrong!”.</p>

<p> </p>

