# 경사하강법 Gradient Descent

### 다변수 함수의 근사식
```
함수 y = f(x) 에서 x 값을 변경할 때 함숫값 y는 얼마나 변할까에 대한 질문은 도함수의 정의에서 출발할 수 있다
```
>![equation](https://latex.codecogs.com/gif.latex?%7Bf%7D%27%28x%29%5Capprox%20%5Cfrac%7Bf%28x&plus;%5CDelta%7Bx%7D%29-f%28x%29%7D%7B%5CDelta%7Bx%7D%7D)
```
델타(Delta)x를 0에 근접해 있는 0과 거의 비슷한 값이라고 하면 극한의 개념을 없앤 위와 같은 근사식을 사용할 수 있다
그리고 이를 변형하면 다음과 같이 일변수 함수의 근사식(선형근사)을 얻을 수 있으며
```
>![equation](https://latex.codecogs.com/gif.latex?f%28x&plus;%5CDelta%7Bx%7D%29%5Capprox%20f%28x%29&plus;%7Bf%7D%27%28x%29%5CDelta%7Bx%7D)
```
이변수 함수 z = f(x, y)로 확장하면 다음과 같다
```
>![equation](https://latex.codecogs.com/gif.latex?f%28x&plus;%5CDelta%7Bx%7D%2C%20y&plus;%5CDelta%7By%7D%29%5Capprox%20f%28x%2Cy%29&plus;%5Cfrac%7B%5Cpartial%20f%28x%2Cy%29%7D%7B%5Cpartial%20x%7D%5CDelta%7Bx%7D&plus;%5Cfrac%7B%5Cpartial%20f%28x%2Cy%29%7D%7B%5Cpartial%20y%7D%5CDelta%7By%7D)
```
위 식을 z를 사용하여 정리하면 다음과 같이 나타낼 수 있다
```
>![equation](https://latex.codecogs.com/gif.latex?%5CDelta%7Bz%7D%3Df%28x&plus;%5CDelta%7Bx%7D%2Cy&plus;%5CDelta%7By%7D%29-f%28x%2Cy%29)

>![equation](https://latex.codecogs.com/gif.latex?%5CDelta%7Bz%7D%5Capprox%20%5Cfrac%7B%5Cpartial%20z%7D%7B%5Cpartial%20x%7D%5CDelta%7Bx%7D&plus;%5Cfrac%7B%5Cpartial%20z%7D%7B%5Cpartial%20y%7D%5CDelta%7By%7D)

### 경사하강법의 원리
>![equation](https://latex.codecogs.com/gif.latex?z%3Df%28x%2Cy%29)
```
위 함수를 최소화 하는 x, y를 구하는 방법으로 x, y가 다음의 관계식을 만족한다는 사실을 이용할 수 있다
```
>![equation](https://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20f%28x%2Cy%29%7D%7B%5Cpartial%20x%7D%3D0%2C%20%5Cfrac%7B%5Cpartial%20f%28x%2Cy%29%7D%7B%5Cpartial%20y%7D%3D0)
```
이는 함수의 최솟값인 점에서 접하는 평면이 수평이 될 것으로 기대하기 때문이다(필요조건)
하지만 위의 식은 쉽게 풀리지 않기 때문에 방정식을 푸는 대신 점을 조금씩 움직여 함수의 최솟값을 찾아야 하는데 이것이 경사하강법이다
```
```
어떻게 하면 경사면을 가장 빠르게 내려갈 수 있을지 찾기 위해 x와 y를 변화시키는 방법을 생각해본다
함수 z = f(x, y)에서 x와 y를 각각 조금씩 변화시켰을 때의 함수는 다음과 같다
```
>![equation](https://latex.codecogs.com/gif.latex?%5CDelta%7Bz%7D%5Capprox%20%5Cfrac%7B%5Cpartial%20f%28x%2Cy%29%7D%7B%5Cpartial%20x%7D%5CDelta%7Bx%7D&plus;%5Cfrac%7B%5Cpartial%20f%28x%2Cy%29%7D%7B%5Cpartial%20y%7D%5CDelta%7By%7D)
```
위 관계식은 다음 두 벡터의 내적 형태로 나타낼 수 있다
```
>![equation](https://latex.codecogs.com/gif.latex?%5Cbegin%7Bpmatrix%7D%20%5Cfrac%7B%5Cpartial%20f%28x%2Cy%29%7D%7B%5Cpartial%20x%7D%2C%26%5Cfrac%7B%5Cpartial%20f%28x%2Cy%29%7D%7B%5Cpartial%20y%7D%20%5Cend%7Bpmatrix%7D%20%2C%20%28%5CDelta%7Bx%7D%2C%20%5CDelta%7By%7D%29)
```
두 벡터의 내적은 다음과 같고, 벡터의 크기를 고정했을 때 내적이 최솟값이 되려면 두 벡터의 방향이 반대여야 한다
```
>![equation](https://latex.codecogs.com/gif.latex?%5Cvec%7Ba%7D%5Ccdot%5Cvec%7Bb%7D%3D%7C%5Cvec%7Ba%7D%7C%7C%5Cvec%7Bb%7D%7Ccos%5Ctheta)
```
즉 내적이 최소가 되는 두 벡터는 다음의 식을 만족할 때이다
```
>![equation](https://latex.codecogs.com/gif.latex?%5Cvec%7Bb%7D%3D-k%5Cvec%7Ba%7D) (k는 양의 정수)
```
정리하면 이변수 함수의 변화는 두 벡터의 내적으로 나타낼 수 있고 이 내적의 최솟값은 두 벡터가 반대 방향일 때이다
따라서 x와 y의 변화가 다음 관계를 성립할 때 가장 빨리 경사면을 내려갈 수 있다
```
>![equation](https://latex.codecogs.com/gif.latex?%28%5CDelta%7Bx%7D%2C%20%5CDelta%7By%7D%29%3D-%5Ceta%20%5Cbegin%7Bpmatrix%7D%20%5Cfrac%7B%5Cpartial%20f%28x%2Cy%29%7D%7B%5Cpartial%20x%7D%2C%26%5Cfrac%7B%5Cpartial%20f%28x%2Cy%29%7D%7B%5Cpartial%20y%7D%20%5Cend%7Bpmatrix%7D)

>![equation](https://latex.codecogs.com/gif.latex?%28%5CDelta%7Bx%7D%2C%20%5CDelta%7By%7D%29%3D-%5Ceta%20%5Cbegin%7Bpmatrix%7D%20%5Cfrac%7B%5Cpartial%20z%7D%7B%5Cpartial%20x%7D%2C%26%5Cfrac%7B%5Cpartial%20z%7D%7B%5Cpartial%20y%7D%20%5Cend%7Bpmatrix%7D)
```
같은 방법으로 삼변수 이상인 함수에도 경사하강법을 다음과 같이 일반화할 수 있다
```
>![equation](https://latex.codecogs.com/gif.latex?%28%5CDelta%7Bx%7D_%7B1%7D%2C%5CDelta%7Bx%7D_%7B2%7D%2C...%2C%5CDelta%7Bx%7D_%7Bn%7D%29%3D-%5Ceta%5Cbegin%7Bpmatrix%7D%20%5Cfrac%7B%5Cpartial%20f%7D%7B%5Cpartial%20x_%7B1%7D%7D%2C%26%20%5Cfrac%7B%5Cpartial%20f%7D%7B%5Cpartial%20x_%7B2%7D%7D%2C%20%26%20...%2C%20%26%20%5Cfrac%7B%5Cpartial%20f%7D%7B%5Cpartial%20x_%7Bn%7D%7D%20%5Cend%7Bpmatrix%7D)
