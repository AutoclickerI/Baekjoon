# [Gold III] All Discs Considered - 6534 

[문제 링크](https://www.acmicpc.net/problem/6534) 

### 성능 요약

메모리: 215072 KB, 시간: 1640 ms

### 분류

너비 우선 탐색, 브루트포스 알고리즘, 방향 비순환 그래프, 그래프 이론, 그래프 탐색, 위상 정렬

### 제출 일자

2025년 4월 2일 01:02:34

### 문제 설명

<p>Operating systems are large software artefacts composed of many packages, usually distributed on several media, e.g., discs. You probably remember the time when your favourite operating system was delivered on 21 floppy discs, or, a few years later, on 6 CDs. Nowadays, it will be shipped on several DVDs, each containing tens of thousands of packages.</p>

<p>The installation of certain packages may require that other packages have been installed previously. Therefore, if the packages are distributed on the media in an unsuitable way, the installation of the complete system requires you to perform many media changes, provided that there is only one reading device available, e.g., one DVD-ROM drive. Since you have to start the installation somehow, there will of course be one or more packages that can be installed independently of all other packages.</p>

<p>Given a distribution of packages on media and a list of dependences between packages, you have to calculate the minimal number of media changes required to install all packages. For your convenience, you may assume that the operating system comes on exactly 2 DVDs.</p>

### 입력 

 <p>The input contains several test cases. Every test case starts with three integers <em>N<sub>1</sub>, N<sub>2</sub>, D</em>. You may assume that <em>1<=N<sub>1</sub>,N<sub>2</sub><=50000</em> and <em>0<=D<=100000</em>. The first DVD contains <em>N<sub>1</sub></em> packages, identified by the numbers <em>1, 2, ..., N<sub>1</sub></em>. The second DVD contains <em>N<sub>2</sub></em> packages, identified by the numbers <em>N<sub>1</sub>+1, N<sub>1</sub>+2, ..., N<sub>1</sub>+N<sub>2</sub></em>. Then follow <em>D</em> dependence specifications, each consisting of two integers <em>x<sub>i</sub>, y<sub>i</sub></em>. You may assume that <em>1<=x<sub>i</sub>,y<sub>i</sub><=N<sub>1</sub>+N<sub>2</sub></em> for <em>1<=i<=D</em>. The dependence specification means that the installation of package <em>x<sub>i</sub></em> requires the previous installation of package <em>y<sub>i</sub></em>. You may assume that there are no circular dependences. The last test case is followed by three zeros.</p>

### 출력 

 <p>For each test case output on a line the minimal number of DVD changes required to install all packages. By convention, the DVD drive is empty before the installation and the initial insertion of a disc counts as <em>one</em> change. Likewise, the final removal of a disc counts as <em>one</em> change, leaving the DVD drive empty after the installation.</p>

