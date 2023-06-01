# [Gold IV] Lift Problems - 10284 

[문제 링크](https://www.acmicpc.net/problem/10284) 

### 성능 요약

메모리: 123348 KB, 시간: 1180 ms

### 분류

다이나믹 프로그래밍

### 문제 설명

<p>On the ground floor (floor zero) of a large university building a number of students are waiting for a lift. Normally, the lift stops at every floor where one or more students need to get out, but that is annoying for the students who want to get out on a higher floor. Alternatively, the lift could skip some floors, but that is annoying for the students who wanted to get out on one of those floors.</p>

<p>Specifically, a student will be annoyed on every floor where the lift stops, if the lift has not yet reached the floor on which he or she wants to get out. If the lift skips the floor on which a student wants to get out, he or she will be annoyed on that floor and every higher floor, up to (and excluding) the floor where the lift makes its next stop and the student can finally get out to start walking back down the stairs to his or her destination.</p>

<p>For example, if a student wants to get out on the fifth floor, while the lift stops at the second, seventh and tenth floor, the student will be annoyed on floors two, five and six. In total, this student will thus be annoyed on three floors.</p>

<p>Upon entering the lift, every student presses the button corresponding to the floor he or she wants to go to, even if it was already pressed by someone else. The CPU controlling the lift thus gets to know exactly how many students want to get out on every floor.</p>

<p>You are charged with programming the CPU to decide on which floors to stop. The goal is to minimize the total amount of lift anger: that is, the number of floors on which every student is annoyed, added together for all students.</p>

<p>You may ignore all the people who may (want to) enter the lift at any higher floor. The lift has to operate in such a way that every student waiting at the ground floor can reach the floor she or he wants to go to by either getting out at that floor or by walking down the stairs.</p>

### 입력 

 <p>On the first line one positive number: the number of test cases, at most 100. After that per test case:</p>

<ul>
	<li>one line with a single integer n (1 ≤ n ≤ 1 500): the number of floors of the building, excluding the ground floor.</li>
	<li>one line with n space-separated integers s<sub>i</sub> (0 ≤ s<sub>i</sub> ≤ 1 500): for each floor i, the number of students s<sub>i</sub> that want to get out.</li>
</ul>

### 출력 

 <p>Per test case:</p>

<ul>
	<li>one line with a single integer: the smallest possible total amount of lift anger.</li>
</ul>

