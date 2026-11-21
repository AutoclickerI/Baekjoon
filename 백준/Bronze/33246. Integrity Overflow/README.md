# [Bronze II] Integrity Overflow - 33246 

[문제 링크](https://acmicpc.net/problem/33246) 

### 선택한 제출

[제출 91319632](https://acmicpc.net/source/91319632) · Python 3 · 152 B · Integrity Overflow.py

### 성능 요약

메모리: 33432 KB, 시간: 36 ms

### 분류

구현, 문자열, 많은 조건 분기

### 제출 일자

2025년 3월 13일 15:05:44

### 문제 설명

<p>The Fortune Protection Corporation (FPC) is a company specialized in securely storing the money of their clients. The money safe is sealed with a 50 cm thick steel door that can only open after correctly entering the secret password in a terminal next to the door. The FPC takes the integrity of this system very serious, and wants to be sure that the door never opens when somebody enters an incorrect password. Since some of the employees of the FPC have dyslexia, the safe will also open when the password contains one incorrect character (it must have the correct length, though).</p>

<p>Given an audit log containing all access attempts to the safe, can you tell whether the integrity of the safe is compromised?</p>

### 입력 

 <ul>
	<li>One line with one integer: $1 \leq n \leq 1000$, the number of lines in the audit log.</li>
	<li>One line containing the correct password.</li>
	<li>$n$ lines with two words each, separated with a single space:
	<ul>
		<li>The first word is the entered password.</li>
		<li>The second word is either "<code>ALLOWED</code>" or "<code>DENIED</code>", depending on whether the password was correct or incorrect, respectively.</li>
	</ul>
	</li>
</ul>

<p>All passwords are at most 32 characters in length and only contain letters from the English alphabet (<code>A-Z</code> and <code>a-z</code>) and numbers (<code>0-9</code>).</p>

### 출력 

 <p>One line, containing "<code>SYSTEM SECURE</code>" if the audit log contains no suspicious access attempts, or "<code>INTEGRITY OVERFLOW</code>" if the security of the system has been compromised.</p>

