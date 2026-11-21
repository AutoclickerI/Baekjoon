# [Platinum V] 도서 검색 프로그램 - 32361 

[문제 링크](https://acmicpc.net/problem/32361) 

### 성능 요약

메모리: 845256 KB, 시간: 6204 ms

### 분류

구현, 자료 구조, 문자열, 파싱, 재귀

### 제출 일자

2025년 2월 17일 00:16:46

### 문제 설명

<p>게임개발동아리 PIMM에는 졸업생들이 전공책을 동아리방에 두고 가는 문화가 있다. 과거 PIMM에서는 신입 회원들이 중고 전공책을 자유롭게 사용할 수 있도록 도서 대여 시스템을 운영했다. 하지만 민규가 회장직을 맡았던 작년에는 동아리방에 너무 많은 책이 쌓여 도서 대여 시스템을 관리하기 어렵게 되었고, 이 소식을 들은 종현은 필요한 책들을 바로바로 찾을 수 있도록 하는 도서 검색 프로그램 제작에 착수했다.</p>

<p>종현이 만든 도서 검색 프로그램은 도서와 검색 요청을 각각 문자열 형태로 저장한다는 특징이 있다. 종현이 만든 도서 검색 프로그램 DB에는 도서를 뜻하는 문자열 <span style="color:#e74c3c;"><code>&lt;book&gt;</code></span>이 저장된다. <span style="color:#e74c3c;"><code>&lt;book&gt;</code></span>은 <a href="https://ko.wikipedia.org/wiki/%EB%B0%B0%EC%BB%A4%EC%8A%A4-%EB%82%98%EC%9A%B0%EB%A5%B4_%ED%91%9C%EA%B8%B0%EB%B2%95">배커스-나우르 표기법(BNF)</a>에 따라 다음과 같이 표기될 수 있다. 연결된 링크에 서술된 내용과 같이, 테이블의 "<span style="color:#e74c3c;"><code>::=</code></span>" 왼쪽에는 기호, 오른쪽에는 표현식이 배치된다.</p>

<pre>&lt;book&gt; ::= &lt;name&gt; " " &lt;author&gt; | &lt;name&gt; " " &lt;author&gt; " " &lt;tags&gt;
&lt;tags&gt; ::= &lt;tag&gt; | &lt;tag&gt; " " &lt;tags&gt;
&lt;name&gt; ::= &lt;str&gt;
&lt;author&gt; ::= &lt;str&gt;
&lt;tag&gt; ::= &lt;str&gt;
</pre>

<p>위 테이블의 기호와 표현식은 아래와 같은 특성을 가진다.</p>

<ul>
	<li><span style="color:#e74c3c;"><code>&lt;str&gt;</code></span>은 알파벳 대소문자, 숫자, '<span style="color:#e74c3c;"><code>-</code></span>', '<span style="color:#e74c3c;"><code>_</code></span>'로 이루어진 길이 $20$ 이하의 문자열이다.</li>
	<li><span style="color:#e74c3c;"><code>&lt;name&gt;</code></span>은 도서의 이름을 의미한다.</li>
	<li><span style="color:#e74c3c;"><code>&lt;author&gt;</code></span>는 도서의 저자를 의미한다.</li>
	<li><span style="color:#e74c3c;"><code>&lt;tag&gt;</code></span>는 도서가 가진 특징을 의미한다.</li>
	<li>하나의 <span style="color:#e74c3c;"><code>&lt;tags&gt;</code></span> 안에 중복된 <span style="color:#e74c3c;"><code>&lt;tag&gt;</code></span>는 존재하지 않는다.</li>
</ul>

<p>만약 <samp>"<span style="color:#e74c3c;"><code>1984 George_Orwell novel SF</code></span>"</samp>라는 문자열 <span style="color:#e74c3c;"><code>&lt;book&gt;</code></span>이 DB 안에 있다면, 이것은 이름이 <span style="color:#e74c3c;"><code>1984</code></span>이고 저자가 <span style="color:#e74c3c;"><code>George_Orwell</code></span>이며, <span style="color:#e74c3c;"><code>novel</code></span>과 <span style="color:#e74c3c;"><code>SF</code></span>라는 두 가지 특징을 지닌 도서가 도서 검색 프로그램 안에 있음을 의미한다.</p>

<p>DB 안에 <span style="color:#e74c3c;"><code>&lt;name&gt;</code></span>과 <span style="color:#e74c3c;"><code>&lt;author&gt;</code></span>가 모두 같은 책이 둘 이상 존재할 수 없다. 단, <span style="color:#e74c3c;"><code>&lt;name&gt;</code></span>이나 <span style="color:#e74c3c;"><code>&lt;author&gt;</code></span> 둘 중 하나가 일치하는 책이 DB 안에 여러 권 있을 수 있음에 유의하라.</p>

<p>도서 검색 프로그램에 주어지는 검색 요청 <span style="color:#e74c3c;"><code>&lt;search&gt;</code></span> 또한 문자열로 주어진다.</p>

<pre>&lt;method&gt; ::= &lt;AND&gt; | &lt;OR&gt; | &lt;NOT&gt; | &lt;nameCorrect&gt; | &lt;nameInclude&gt; | &lt;authorCorrect&gt; | &lt;tagCorrect&gt;
&lt;methods&gt; ::= &lt;method&gt; | &lt;method&gt; ", " &lt;methods&gt;

&lt;AND&gt; ::= "A(" &lt;methods&gt; ")"
&lt;OR&gt; ::= "O(" &lt;methods&gt; ")"
&lt;NOT&gt; ::= "N(" &lt;method&gt; ")"

&lt;nameCorrect&gt; ::= "n:" &lt;str&gt;
&lt;nameInclude&gt; ::= "ni:" &lt;str&gt;
&lt;authorCorrect&gt; ::= "a:" &lt;str&gt;
&lt;tagCorrect&gt; ::= "t:" &lt;str&gt;

&lt;search&gt; ::= &lt;methods&gt;
</pre>

<p>위 테이블의 기호와 표현식은 아래와 같은 특성을 가진다.</p>

<ul>
	<li><span style="color:#e74c3c;"><code>&lt;str&gt;</code></span>는 알파벳 대소문자, 숫자, '<span style="color:#e74c3c;"><code>-</code></span>', '<span style="color:#e74c3c;"><code>_</code></span>'로 이루어진 길이 $20$ 이하의 문자열이다.</li>
	<li><span style="color:#e74c3c;"><code>&lt;nameCorrect&gt;</code></span><font face="sans-serif, Arial, Verdana, Trebuchet MS, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol">는 표현식</font><span style="color:#e74c3c;"><font face="sans-serif, Arial, Verdana, Trebuchet MS, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol"> </font><code>&lt;str&gt;</code></span>과 주어진 <span style="color:#e74c3c;"><code>&lt;book&gt;</code></span>의 <span style="color:#e74c3c;"><code>&lt;name&gt;</code></span>이 일치하면 참을, 그렇지 않다면 거짓을 반환하는 기호이다.</li>
	<li><span style="color:#e74c3c;"><code>&lt;nameInclude&gt;</code></span>는 표현식 <span style="color:#e74c3c;"><code>&lt;str&gt;</code></span>이 주어진 <span style="color:#e74c3c;"><code>&lt;book&gt;</code></span>의 문자열 <span style="color:#e74c3c;"><code>&lt;name&gt;</code></span> 안에 포함되었다면 참을, 그렇지 않다면 거짓을 반환하는 기호이다.</li>
	<li><span style="color:#e74c3c;"><code>&lt;authorCorrect&gt;</code></span>는 표현식 <span style="color:#e74c3c;"><code>&lt;str&gt;</code></span>과 주어진 <span style="color:#e74c3c;"><code>&lt;book&gt;</code></span>의 <span style="color:#e74c3c;"><code>&lt;author&gt;</code></span>와 일치하면 참을, 그렇지 않다면 거짓을 반환하는 기호이다.</li>
	<li><span style="color:#e74c3c;"><code>&lt;tagCorrect&gt;</code></span>는 표현식 <span style="color:#e74c3c;"><code>&lt;str&gt;</code></span>과 주어진 <span style="color:#e74c3c;"><code>&lt;book&gt;</code></span>의 <span style="color:#e74c3c;"><code>&lt;tags&gt;</code></span> 안에 일치하는 <span style="color:#e74c3c;"><code>&lt;tag&gt;</code></span>가 하나라도 있다면 참을, 그렇지 않다면 거짓을 반환하는 기호이다.</li>
	<li><span style="color:#e74c3c;"><code>&lt;AND&gt;</code></span>는 표현식 <span style="color:#e74c3c;"><code>&lt;methods&gt;</code></span> 안의 모든 <span style="color:#e74c3c;"><code>&lt;method&gt;</code></span>가 참을 반환하면 참을, 그렇지 않다면 거짓을 반환하는 기호이다.</li>
	<li><span style="color:#e74c3c;"><code>&lt;OR&gt;</code></span>는 표현식 <span style="color:#e74c3c;"><code>&lt;methods&gt;</code></span> 안의 <span style="color:#e74c3c;"><code>&lt;method&gt;</code></span> 중 하나라도 참을 반환하면 참을, 그렇지 않다면 거짓을 반환하는 기호이다.</li>
	<li><span style="color:#e74c3c;"><code>&lt;NOT&gt;</code></span>은 표현식 <span style="color:#e74c3c;"><code>&lt;method&gt;</code></span>가 참을 반환한다면 거짓을, 그렇지 않다면 참을 반환하는 기호이다.</li>
	<li><span style="color:#e74c3c;"><code>&lt;search&gt;</code></span>는 DB 안의 모든 <span style="color:#e74c3c;"><code>&lt;book&gt;</code></span>에 대해, 표현식 <span style="color:#e74c3c;"><code>&lt;methods&gt;</code></span> 안의 모든 <span style="color:#e74c3c;"><code>&lt;method&gt;</code></span>가 참을 반환하는 <span style="color:#e74c3c;"><code>&lt;book&gt;</code></span>의 개수를 반환하는 기호이다.</li>
</ul>

<p>여러 개의 책 <span style="color:#e74c3c;"><code>&lt;book&gt;</code></span>과, 여러 개의 문자열 <span style="color:#e74c3c;"><code>&lt;search&gt;</code></span>가 주어질 때, 각각의 <span style="color:#e74c3c;"><code>&lt;search&gt;</code></span>에 대해 반환되는 값을 한 줄에 하나씩 출력하라.</p>

### 입력 

 <p>입력의 첫째 줄에는 DB 안의 문자열 <span style="color:#e74c3c;"><code>&lt;book&gt;</code></span>의 개수 $N$이 주어진다. 다음 $N$개 줄에는 DB 안에 저장된 문자열 <span style="color:#e74c3c;"><code>&lt;book&gt;</code></span>이 한 줄에 한 개씩 주어진다.</p>

<p>다음 줄에는 검색 요청 문자열인 <span style="color:#e74c3c;"><code>&lt;search&gt;</code></span>의 개수 $M$이 주어진다. 다음 $M$개 줄에는 문자열 <span style="color:#e74c3c;"><code>&lt;search&gt;</code></span>가 한 줄에 한 개씩 주어진다.</p>

<p>잘못된 문자열은 입력으로 주어지지 않는다.</p>

### 출력 

 <p>검색 명령어 <span style="color:#e74c3c;"><code>&lt;search&gt;</code></span>에 대한 결괏값을 한 줄에 하나씩 출력한다.</p>

