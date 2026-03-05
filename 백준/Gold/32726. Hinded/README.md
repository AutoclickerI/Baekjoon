# [Gold I] Hinded - 32726 

[문제 링크](https://www.acmicpc.net/problem/32726) 

### 성능 요약

메모리: 119296 KB, 시간: 520 ms

### 분류

브루트포스 알고리즘, 최대 부분 배열 문제

### 제출 일자

2026년 3월 6일 07:08:58

### 문제 설명

<p>Juku on koolis teinud hulga kontrolltöid, mida hinnati $0 \ldots 100$ punktiga.</p>

<p>Juku vanaisa annab talle hinnete eest taskuraha. Vanaisa loeb tulemused üle $50$ punkti headeks hinneteks ja tulemused alla $50$ punkti halbadeks hinneteks. Täpsemalt liidab ta hinnete $50$ punkti ületavad osad Juku taskurahale ning lahutab $50$ punkti alla jäävad osad sealt maha. Näiteks hinnete $35$, $42$, $81$ ja $100$ eest saaks Juku kokku $(35-50)+(42-50)+(81-50)+(100-50) = -15-8+31+50 = 58$ eurot. (Täpselt $50$ punktiga hinnatud tööd seega taskuraha ei mõjuta.)</p>

<p>Õpetaja hoiab Juku hindeid $N$ rea ja $N$ veeruga Exceli tabelis. Kokku on Jukul seega $N^2$ hinnet. Juku pääseb tabelile korraks ligi ja tal on võimalus oma hindeid "parandada" sel viisil, et ta märgib tabelis ühe ristkülikukujulise alamosa (mis võib olla ka tühi, s.t. sisaldada null elementi) ja kustutab sealt kõik hinded.</p>

<p>Leida, mis on maksimaalne hulk taskuraha, mille Juku võiks sellise kustutamise järel saada.</p>

### 입력 

 <p>Sisendi esimesel real on täisarv $N$ ($2 \le N \le 300$): õpetaja tabeli küljepikkus.</p>

<p>Järgmisel $N$ real on igaühel $N$ tühikutega eraldatud täisarvu lõigust $0 \ldots 100$: Juku hinded.</p>

### 출력 

 <p>Väljundisse kirjutada üks täisarv: Juku maksimaalse taskuraha summa.</p>

