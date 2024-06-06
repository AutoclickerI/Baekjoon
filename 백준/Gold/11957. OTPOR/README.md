# [Gold III] OTPOR - 11957 

[문제 링크](https://www.acmicpc.net/problem/11957) 

### 성능 요약

메모리: 35520 KB, 시간: 56 ms

### 분류

자료 구조, 파싱, 스택, 문자열

### 제출 일자

2024년 6월 6일 19:34:41

### 문제 설명

<p>Mirko has been a very good boy, so he got exactly what he wanted for his birthday, a "Young physicist" kit! In the kit, there are N types of resistors, connecting wires and an ohmmeter. If a resistor is of type i, it provides a resistance of precisely R<sub>i</sub> ohms.</p>

<p>As we all know, resistors can be connected in two different ways, in series and parallel. Also, we know that the complete circuit of resistors can be replaced with one resistor of the resistance equal to the equivalent resistance of the circuit. When the circuit is series, it is written in the following way:</p>

<p style="text-align: center;">(R1-R2-R3-...-RK)</p>

<p>and the following formula holds:</p>

<p style="text-align: center;">R<sub>ekv</sub> = R<sub>1</sub> + R<sub>2</sub> + R<sub>3</sub> + ... + R<sub>K</sub></p>

<p>When the circuit is parallel, it is written in the following way:</p>

<p style="text-align: center;">(R1|R2|R3|...|RK)</p>

<p>and the following formula holds:</p>

<p style="text-align: center;">R<sub>ekv</sub> = 1/(1/R<sub>1</sub> + 1/R<sub>2</sub> + 1/R<sub>3</sub> + ... + 1/R<sub>K</sub>)</p>

<p>Mirko was excited to bring his new toy to school, where he showed it to all his friends. Unfortunately for him, the teacher also noticed the toy. She quickly connected a circuit and is now asking Mirko to tell her the equivalent resistance of the circuit. Help Mirko and answer the teacher’s question!</p>

### 입력 

 <p>The first line of input contains the integer N (1 ≤ N ≤ 9) from the task.</p>

<p>The following line contains N real numbers R<sub>i</sub> (0 < R<sub>i</sub> < 100) from the task.</p>

<p>The last line contains the circuit S, that will not be longer than 100 000 characters. S will only consist of the following characters: ’R’, ’1’ – ’9’, ’(’, ’)’, ’-’ and ’|’. The number of pairs of brackets will be minimal, and the brackets will be paired properly. Inside of a pair of brackets, there will not be the character ’-’ and the character ’|’ at the same time. The circuit will only consist of the resistors from the kit and it is possible that not all types of resistors are used, or that one type of resistor is used several times.</p>

### 출력 

 <p>The first and only line of output must contain the number from the task. A deviation from the official solution of ±0.00001 is tolerated.</p>

