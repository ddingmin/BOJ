# [Gold IV] 넴모넴모 2020 - 19845 

[문제 링크](https://www.acmicpc.net/problem/19845) 

### 성능 요약

메모리: 154540 KB, 시간: 428 ms

### 분류

이분 탐색

### 제출 일자

2023년 11월 6일 23:47:33

### 문제 설명

<p>오래된 테트리스 게임판 위에 수수께끼의 생물 “넴모”들이 살기 시작했다. 이 게임판은 가로로 10<sup>9</sup>칸, 세로로 <span style="font-style: italic;">N</span>층 크기이고, 넴모 한 마리는 한 층의 한 칸을 차지하고 산다. 편의상 왼쪽에서부터 <span style="font-style: italic;">x</span>번째, 아래쪽에서부터 <span style="font-style: italic;">y</span>층을 (<span style="font-style: italic;">x</span>, <span style="font-style: italic;">y</span>)로 표기하자.</p>

<p><span style="font-style: italic;">y</span>층에는 <span style="font-style: italic;">a</span><sub><span style="font-style: italic;">y</span></sub>마리의 넴모들이 살고 있다. 넴모들은 붙어있는 걸 좋아하기 때문에 (1, <span style="font-style: italic;">y</span>), …, (<span style="font-style: italic;">a</span><sub><span style="font-style: italic;">y</span></sub>, <span style="font-style: italic;">y</span>) 칸에 나란히 살고 있으며, 중력의 영향을 받기 때문에 모든 1 ≤ <span style="font-style: italic;">y</span> ≤ <span style="font-style: italic;">N</span> − 1에 대해 <span style="font-style: italic;">a</span><sub><span style="font-style: italic;">y</span></sub> ≥ <span style="font-style: italic;">a</span><sub><span style="font-style: italic;">y</span>+1</sub>이다.</p>

<p style="margin-top: 15px;"><img alt="nemmo" src="https://upload.acmicpc.net/e3dd5590-b5f1-4f65-bff9-f09b56211938/-/preview/" style="display: block; margin-left: auto; margin-right: auto; width: 100%; max-width: 400px;"></p>

<p style="margin-bottom: 15px; text-align: center;">테트리스 게임판에 살고 있는 넴모들. 이 경우 <span style="font-style: italic;">N</span> = 3, <span style="font-style: italic;">a</span><sub>1</sub> = 3, <span style="font-style: italic;">a</span><sub>2</sub> = 3, <span style="font-style: italic;">a</span><sub>3</sub> = 2이다.</p>

<p>테트리스를 하고 싶은 레프는 레이저를 이용해서 넴모들을 치워버리려고 한다. (<span style="font-style: italic;">x</span>, <span style="font-style: italic;">y</span>)에 레이저를 설치하면 왼쪽에서 <span style="font-style: italic;">x</span>번째 칸에 살고 있는 넴모들 중 <span style="font-style: italic;">y</span>층 이상에 살고 있는 넴모들, <span style="font-style: italic;">y</span>층에 있는 넴모들 중 (<span style="font-style: italic;">x</span>, <span style="font-style: italic;">y</span>)보다 오른쪽에 있는 넴모들이 모두 사라진다. 그 이외의 넴모는 당장 사라지지는 않는다.</p>

<p style="margin-top: 15px;"><img alt="laser" src="https://upload.acmicpc.net/db89da45-151c-4df9-87dc-8e498c780b53/-/preview/" style="display: block; margin-left: auto; margin-right: auto; width: 100%; max-width: 400px;"></p>

<p style="margin-bottom: 15px; text-align: center;">(1, 2)에 레이저를 설치한 모습. 총 4마리의 넴모가 레이저에 맞아 사라진다.</p>

<p>레이저를 설치할 수 있는 위치는 총 <span style="font-style: italic;">Q</span>개가 있다. 레프를 위해 각 위치에 레이저를 설치했을 때 몇 마리의 넴모를 없앨 수 있는지 알려주자. 단, 실제로 레이저를 설치하는 것이 아닌 설치 계획만 하는 것이기 때문에, 설치 계획끼리 서로 영향을 주고받지는 않는다.</p>

### 입력 

 <p>첫째 줄에 정수 <span style="font-style: italic;">N</span>, <span style="font-style: italic;">Q</span>가 공백으로 구분되어 주어진다. <span style="font-style: italic;">N</span>은 게임판의 세로 크기, <span style="font-style: italic;">Q</span>는 레이저를 설치할 수 있는 위치의 수를 의미한다.</p>

<p>둘째 줄에는 <span style="font-style: italic;">N</span>개의 정수 <span style="font-style: italic;">a</span><sub>1</sub>, …, <span style="font-style: italic;">a</span><sub><span style="font-style: italic;">N</span></sub>이 공백을 사이에 두고 주어진다. 이는 <span style="font-style: italic;">i</span>층에 <span style="font-style: italic;">a</span><sub><span style="font-style: italic;">i</span></sub>마리의 넴모가 살고 있다는 의미이다.</p>

<p>셋째 줄부터 <span style="font-style: italic;">Q</span>개의 줄에 걸쳐 레이저를 설치할 수 있는 위치가 주어진다. (<span style="font-style: italic;">i</span> + 2)번째 줄에는 두 정수 <span style="font-style: italic;">x</span><sub><span style="font-style: italic;">i</span></sub>와 <span style="font-style: italic;">y</span><sub><span style="font-style: italic;">i</span></sub>가 공백을 사이에 두고 주어지는데, 이는 (<span style="font-style: italic;">x</span><sub><span style="font-style: italic;">i</span></sub>, <span style="font-style: italic;">y</span><sub><span style="font-style: italic;">i</span></sub>)에 레이저를 설치할 수 있다는 의미이다.</p>

### 출력 

 <p><span style="font-style: italic;">Q</span>개의 줄에 걸쳐 답을 출력한다. <span style="font-style: italic;">i</span>번째 줄에는 (<span style="font-style: italic;">x</span><sub><span style="font-style: italic;">i</span></sub>, <span style="font-style: italic;">y</span><sub><span style="font-style: italic;">i</span></sub>)에 레이저를 설치하면 몇 마리의 넴모를 제거할 수 있는지 출력한다.</p>

