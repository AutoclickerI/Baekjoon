# [Gold I] Alloc - 16347 

[문제 링크](https://www.acmicpc.net/problem/16347) 

### 성능 요약

메모리: 122012 KB, 시간: 532 ms

### 분류

자료 구조, 구현, 연결 리스트, 세그먼트 트리

### 제출 일자

2024년 11월 11일 14:06:06

### 문제 설명

<p>Napišite program koji će simulirati izvršavanje naredbi za rezerviranje i oslobadanje memorije. Memorija računala je niz od 100 000 uzastopnih memorijskih lokacija, redom označenih adresama od 1 do 100 000. Na početku su sve lokacije slobodne. Naredbe koje se mogu pojaviti su:</p>

<ul>
	<li><code>var=malloc(s);</code> Ova naredba pronalazi prvi niz od <code>s</code> uzastopnih slobodnih memorijskih lokacija i rezervira ih. Funkcija vraća adresu prve rezervirane lokacije. Ako ne postoji niz od <code>s</code> uzastopnih slobodnih memorijskih lokacija, onda funkcija ništa ne rezervira te vraća vrijednost 0.</li>
	<li><code>free(var);</code> Ova naredba oslobada memorijske lokacije dodijeljene varijabli var (prethodnim pozivom funkcije <code>malloc</code>) i postavlja vrijednost varijable <code>var</code> na 0. Ako je vrijednost varijable <code>var</code> već jednaka 0 prije poziva funkcije, onda funkcija ne radi ništa.</li>
	<li><code>print(var);</code> Ova naredba ispisuje vrijednost varijable <code>var</code>.</li>
</ul>

<p>Svaka naredba završava znakom “<code>;</code>” (točkazarez). Varijable su nizovi sastavljeni od točno 4 mala slova engleske abecede. Sve varijable su na početku inicijalizirane na vrijednost 0.</p>

### 입력 

 <p>U prvom redu se nalazi cijeli broj n (1 ≤ n ≤ 100 000) – broj naredbi. U j-tom od sljedećih n redova se nalazi j-ta naredba, formatirana točno kao u tekstu zadatka bez viška praznih znakova. Ukupni broj različitih varijabli će biti manji ili jednak od 1000. Barem jedna od naredbi će biti naredba <code>print</code>. U svakoj naredbi <code>malloc</code> vrijedi 100 ≤ s ≤ 100 000.</p>

### 출력 

 <p>U j-ti red ispišite rezultat j-te po redu naredbe <code>print</code>.</p>

