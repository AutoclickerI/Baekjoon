# [Silver III] Matematické cvičení - 9137 

[문제 링크](https://www.acmicpc.net/problem/9137) 

### 성능 요약

메모리: 33544 KB, 시간: 332 ms

### 분류

임의 정밀도 / 큰 수 연산, 사칙연산, 수학, 정수론, 문자열

### 제출 일자

2025년 5월 1일 11:31:43

### 문제 설명

<p>Malí matfyzáčci se musí odmala cvičit v matematice. Protože ale látka jako řešení soustav diferenciálních rovnic či integrace ve vícerozměrných prostorech je pro ně ještě příliš obtížná, je potřeba vyučovat něco jednoduššího. Po dlouhých debatách se rozhodlo, že se bude vyučovat prosté sčítání; ovšem v různých soustavách. Vaším úkolem bude napsat program, který bude žáčky kontrolovat.</p>

### 입력 

 <p>Na vstupu je několik bloků. Každý blok mimo posledního začíná řádkem s kladným celým číslem <var>z</var>, <var>z</var> ≤ 35, poslední blok začíná nulou a nemá být zpracováván. Na druhém řádku každého bloku se nachází dvě nezáporná čísla <var>x</var> a <var>y</var> oddělená mezerou, která jsou zapsána standardním způsobem v soustavě o základu <var>z</var>. U soustav o základu větším než 10 se pro cifry s hodnotou větší než 9 používá písmen <code>A</code>, <code>B</code>.... Pokud má soustava základ jedna, používá se pouze cifra jedna a a počet cifer je roven velikosti čísla (viz vzorový výstup); nula se v jedničkové soustavě zapisuje jako jednociferné číslo, jehož jediná cifra 0. Čísla, která váš program obdrží na vstupu, nebudou na svém začátku obsahovat přebytečné nuly. Čísla mají nejvýše 1 000 cifer.</p>

### 출력 

 <p>Výstup má obsahovat pro každý blok na vstupu jeden řádek. Na řádku mají být vypsána čísla <var>x</var> a <var>y</var> oddělená mezerou, znakem <code>+</code> a mezerou. Za nimi má následovat mezera, znak <code>=</code>, mezera a číslo <var>x</var>+<var>y</var>. Všechna čísla mají být zapsána standardním způsobem v soustavě o základu <var>z</var>.</p>

