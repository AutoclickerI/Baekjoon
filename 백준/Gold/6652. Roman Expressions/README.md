# [Gold II] Roman Expressions - 6652 

[문제 링크](https://www.acmicpc.net/problem/6652) 

### 성능 요약

메모리: 31120 KB, 시간: 168 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 구현, 파싱, 문자열

### 제출 일자

2024년 6월 24일 10:03:49

### 문제 설명

<p>As any other marketing company, ACM produces a lot of funky advertising items that may contain a logo and be given to customers and business partners as small gifts. A unique specialty of ACM is a calculator that uses roman numbers.</p>

<p>Roman numbers are able to express any non-negative integer using uppercase letters:</p>

<p style="text-align: center;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/6652/1.png" style="height:176px; width:206px"></p>

<p>Numbers are created by appending several letters together, the letter representing a higher value must always precede letters with lower values. The only exception are the letters “I”, “X”, and “C”, they may be used before higher letters to form values expressed by digits 4 and 9. The only possible combinations are:</p>

<p style="text-align: center;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/6652/2.png" style="height:144px; width:274px"></p>

<p>Any roman number must first express thousands, then hundreds, tens, and ones. Therefore, 499 must always be written as “CDXCIX”, not “ID”.</p>

<p>Although not very practical, this gift is considered extremely “cooooool”. Your task is to write software for that calculator.</p>

### 입력 

 <p>The input will consist from commands, each written on a separate line. Possible commands are assignments, “RESET”, and “QUIT”.</p>

<p>An assignment command starts with a single digit representing one of ten registers that the calculator has. The register number is followed by an equal sign (“=”) and an expression. The expression will consist only from valid roman numbers, register names (digits), plus (“+”) and minus (“-”) signs. You may assume that the expression will always be valid and no longer than 10000 characters.</p>

### 출력 

 <p>For each command, output a single line. For assignments, print the register name, equal sign, and the value that is being assigned to that register. Instead of it, print the word “Error”, if the expression contains a reference to a register that has not been assigned before, or if the result is negative or larger than 10000. In such cases, no change to register values is made.</p>

<p>For RESET commands, invalidate all previous register assignments and print the word “Ready”.</p>

<p>The QUIT command will be the last one. Print the word “Bye” and terminate the program.</p>

