# [Silver I] Access Denied - 23767 

[문제 링크](https://www.acmicpc.net/problem/23767) 

### 성능 요약

메모리: 13812 KB, 시간: 132 ms

### 분류

구현, 문자열, 브루트포스 알고리즘, 파싱

### 제출 일자

2025년 6월 22일 03:56:24

### 문제 설명

<p>Computer passwords have been around for a long time. In fact, 60 years ago \href{https://en.wikipedia.org/wiki/Compatible_Time-Sharing_System}{CTSS} was one of the first computers with a password. The implementation of this was very simple. In CTSS the password was stored in plain text in a file on disk. When logging in, the user would enter a password. The computer would then compare the password to the password on disk. If the comparison failed, it would deny access, if it succeeded, access would be allowed. Researchers at MIT were quick to discover several security flaws in this password system. We will explore one of them, the timing attack.</p>

<p>In a timing attack, we exploit that we can deduce a computation path from the time it takes to do the computation. In CTSS the password check was done using a simple string matching algorithm, similar to this:</p>

<pre>bool CheckPassword(string pwd1, string pwd2) {
    if (pwd1.Length != pwd2.Length) {
        return false;
    }
    for (int i = 0; i < pwd1.Length; i++) {
        if (pwd1[i] != pwd2[i]) {
            return false;
        }
    }
    return true;
}
</pre>

<p>For the purpose of this problem, we will use a (very) simplified timing model and the above algorithm. The timing model looks as follows:</p>

<ul>
	<li>A branching statement (if or for) takes $1$ ms.</li>
	<li>An assignment, or update of a memory address takes $1$ ms.</li>
	<li>A comparison between two memory addresses takes $3$ ms.</li>
	<li>A return statement takes $1$ ms.</li>
</ul>

<p>The password consists of between $1$ and $20$ English letters, upper or lower case, and digits.</p>

### 입력 

 Empty

### 출력 

 Empty

