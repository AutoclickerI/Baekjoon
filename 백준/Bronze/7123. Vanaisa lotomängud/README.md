# [Bronze I] Vanaisa lotomängud - 7123 

[문제 링크](https://acmicpc.net/problem/7123) 

### 성능 요약

메모리: 31256 KB, 시간: 52 ms

### 분류

수학, 구현

### 제출 일자

2023년 9월 20일 11:10:58

### 문제 설명

<p>Juku vanaisa on innukas ja enda arvates ka edukas lotomängija. Jukul on selle viimase väite osas kahtlusi, sellepärast on ta juba mõnda aega kirjutanud üles, kui palju vanaisa lotopiletitele kulutab ja kui palju ta lotoga võidab.</p>

<p>Kirjutada programm, mis teeb vanaisa lotomängude kohta kolme liiki statistikat:</p>

<ul>
	<li>leiab, kas ta on kokku võitnud rohkem või vähem kui piletitele kulutanud;</li>
	<li>leiab, millisel päeval ta ühe päevaga kõige rohkem kaotas;</li>
	<li>leiab, millal ta mingite järjestikuste päevade jooksul kõige rohkem kaotas.</li>
</ul>

### 입력 

 <p>Tekstifaili esimesel real on Juku päeviku kannete arv $N$ ($1 \le N \le 100$). Järgmisel $N$ real on igaühel kaks tühikutega eraldatud täisarvu: päeval $i$ ($1 \le i \le N$) piletitele kulutatud summa $P_i$ ($0 \le P_i \le 100$) ja võidetud summa $V_i$ ($0 \le V_i \le 1\,000\,000$).</p>

### 출력 

 <p>Tekstifaili väljastada täpselt kolm rida, igale reale üks vastus.</p>

<p>Faili esimesele reale väljastada sõna <code>PLUSSIS</code>, <code>MIINUSES</code> või <code>NULLIS</code> vastavalt sellele, kas vanaisa võitude kogusumma on piletikulude kogusummast suurem, väiksem või sellega võrdne. Kui programm seda leida ei oska, väljastada faili esimesele reale <code>EI TEA</code>.</p>

<p>Faili teisele reale väljastada kaks tühikuga eraldatud täisarvu $P$ ja $S$, kus $P$ on selle päeva number, kui vanaisa ühe päevaga kõige rohkem raha kaotas, ja $S$ selle päeva kaotussumma (piletikulu ja võitude vahe). Võib eeldada, et vanaisa on vähemalt ühel päeval raha kaotanud. Kui maksimaalse kaotussummaga päevi on mitu, väljastada ükskõik milline neist. Kui programm seda infot leida ei oska, väljastada faili teisele reale <code>0 0</code>.</p>

<p>Faili kolmandale reale väljastada kolm tühikutega eraldatud täisarvu $P_1$, $P_2$ ja $S$, mis näitavad, et vanaisa kõige kulukam periood kestis päevast $P_1$ päevani $P_2$, mille jooksul tema kulutused piletitele ületasid võite kokku $S$ võrra. Kui maksimaalse kaotussummaga ajaperioode on mitu, väljastada ükskõik milline neist. Kui programm seda infot leida ei oska, väljastada faili kolmandale reale <code>0 0 0</code>.</p>

