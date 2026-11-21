# [Bronze II] Papier kamień nożyczki - 8806 

[문제 링크](https://acmicpc.net/problem/8806) 

### 성능 요약

메모리: 31256 KB, 시간: 40 ms

### 분류

수학, 사칙연산, 확률론

### 제출 일자

2023년 7월 29일 09:29:33

### 문제 설명

<p>Adam i Gosia grają w "Papier kamień nożyczki".</p>

<p>Gra polega na tym, że każdy z zawodników jednocześnie wybiera&nbsp;<em>papier</em>,&nbsp;<em>kamień</em>&nbsp;lub&nbsp;<em>nożyczki</em>.</p>

<ul>
	<li>Gracz, który wybrał&nbsp;<em>papier</em>&nbsp;wygrywa z tym, który wybrał&nbsp;<em>kamień</em>.</li>
	<li>Gracz, który wybrał&nbsp;<em>kamień</em>&nbsp;wygrywa z tym, który wybrał&nbsp;<em>nożyczki</em>.</li>
	<li>Gracz, który wybrał&nbsp;<em>nożyczki</em>&nbsp;wygrywa z tym, który wybrał&nbsp;<em>papier</em>.</li>
</ul>

<p>Jeśli oboje wybiorą ten sam ruch gra jest powtarzana do momentu wyłonienia zwycięzcy.</p>

<p>Wiedząc z jakim prawdopodobieństem każdy z graczy wybierze&nbsp;<em>papier</em>,&nbsp;<em>kamień</em>&nbsp;i&nbsp;<em>nożyczki</em>&nbsp;oblicz kto ma większe szanse wygrania pojedynku.</p>

### 입력 

 <p>W pierwszej linii wejścia znajduje się liczba zestawów testowych&nbsp;<strong>Z</strong>&nbsp;( 1 &lt;=&nbsp;<strong>Z</strong>&nbsp;&lt;= 10 ).</p>

<p>Pierwsza linia pojedynczego zestawu testowego zawiera liczby&nbsp;<strong>X1 Y1 Z1</strong>&nbsp;( 0 &lt;=&nbsp;<strong>X1</strong>,&nbsp;<strong>Y1, Z1</strong>&nbsp;&lt;= 1,&nbsp;&nbsp;<strong>X1 + Y1 + Z1</strong>&nbsp;= 1) określające z jakim prawdopodobieństwem Adam wybierze&nbsp;<em>papier</em>,&nbsp;<em>kamień</em>&nbsp;i&nbsp;<em>nożyczki</em>. Druga&nbsp;linia zawiera liczby&nbsp;<strong>X2 Y2 Z2</strong>&nbsp;( 0 &lt;=&nbsp;<strong>X2</strong>,&nbsp;<strong>Y2, Z2</strong>&nbsp;</p>

<p>&lt;= 1,&nbsp;&nbsp;<strong>X2 + Y2 + Z2</strong>&nbsp;= 1&nbsp;) określające z jakim prawdopodobieństwem Gosia wybierze&nbsp;<em>papier</em>,&nbsp;<em>kamień</em>&nbsp;i&nbsp;<em>nożyczki</em>.</p>

### 출력 

 <p>Dla każdego zestawu testowego należy wypisać:</p>

<ul>
	<li>"ADAM" jeśli Adam ma większe szanse na zwycięstwo</li>
	<li>"GOSIA" jeśli Gosia ma większe szansce na zwycięstwo</li>
	<li>"=" jesli Adam i Gosia mają równe szanse na zwycięstwo</li>
</ul>

