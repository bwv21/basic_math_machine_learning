# 경사하강법 Gradient Descent
-----------------
### 다변수 함수의 근사식
```
일변수 함수 y = f(x) 에서 x 값을 변경할 때 함숫값 y는 얼마나 변할까에 대한 질문은 도함수의 정의에서 출발할 수 있다
```
>![equation](https://latex.codecogs.com/gif.latex?%7Bf%7D%27%28x%29%5Capprox%20%5Cfrac%7Bf%28x&plus;%5CDelta%7Bx%7D%29-f%28x%29%7D%7B%5CDelta%7Bx%7D%7D)
```
이를 변형하면 일변수 함수의 근사식(선형근사)을 얻을 수 있다
```
>![equation](https://latex.codecogs.com/gif.latex?f%28x&plus;%5CDelta%7Bx%7D%29%5Capprox%20f%28x%29&plus;%7Bf%7D%27%28x%29%5CDelta%7Bx%7D)
```
이를 이변수 함수로 확장하면 다음과 같다
```
>![equation](https://latex.codecogs.com/gif.latex?f%28x&plus;%5CDelta%7Bx%7D%2C%20y&plus;%5CDelta%7By%7D%29%5Capprox%20f%28x%2Cy%29&plus;%5Cfrac%7B%5Cpartial%20f%28x%2Cy%29%7D%7B%5Cpartial%20x%7D%5CDelta%7Bx%7D&plus;%5Cfrac%7B%5Cpartial%20f%28x%2Cy%29%7D%7B%5Cpartial%20y%7D%5CDelta%7By%7D)
```
위 식은 정리하여 다음과 같이 나타낼 수 있다
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
하지만 위의 식은 쉽게 풀리지 않기 때문에 방정식을 푸는 대신 그래프 상의 점을 조금씩 움직여 함수의 최솟값을 찾아야 한다
```
>![equation](https://latex.codecogs.com/gif.latex?%5CDelta%7Bz%7D%5Capprox%20%5Cfrac%7B%5Cpartial%20z%7D%7B%5Cpartial%20x%7D%5CDelta%7Bx%7D&plus;%5Cfrac%7B%5Cpartial%20z%7D%7B%5Cpartial%20y%7D%5CDelta%7By%7D)
```
위 관계식은 다음과 같이 벡터의 내적 형태로 나타낼 수 있다
```
>![equation](https://latex.codecogs.com/gif.latex?%5Cbegin%7Bpmatrix%7D%20%5Cfrac%7B%5Cpartial%20f%28x%2Cy%29%7D%7B%5Cpartial%20x%7D%2C%26%5Cfrac%7B%5Cpartial%20f%28x%2Cy%29%7D%7B%5Cpartial%20y%7D%20%5Cend%7Bpmatrix%7D%20%2C%20%28%5CDelta%7Bx%7D%2C%20%5CDelta%7By%7D%29)
```
0이 아닌 두 벡터의 크기를 고정했다고 할 때, 내적이 최솟값이 되려면 두 벡터의 방향이 반대여야 한다
```
>![equation](https://latex.codecogs.com/gif.latex?%5Cvec%7Ba%7D%5Ccdot%5Cvec%7Bb%7D%3D%7C%5Cvec%7Ba%7D%7C%7C%5Cvec%7Bb%7D%7Ccos%5Ctheta)
```
즉 내적이 최소가 되는 두 벡터는 다음의 식을 만족할 때이다
```
>![equation](https://latex.codecogs.com/gif.latex?%5Cvec%7Bb%7D%3D-k%5Cvec%7Ba%7D) (k는 양의 정수)
```
정리하면, 이변수 함수의 변화는 두 벡터의 내적으로 나타낼 수 있고 이 내적의 최솟값은 두 벡터가 반대방향 일 때이다
따라서 다음식의 관계가 성립해야 한다
```
>![equation](https://latex.codecogs.com/gif.latex?%28%5CDelta%7Bx%7D%2C%20%5CDelta%7By%7D%29%3D-%5Ceta%20%5Cbegin%7Bpmatrix%7D%20%5Cfrac%7B%5Cpartial%20f%28x%2Cy%29%7D%7B%5Cpartial%20x%7D%2C%26%5Cfrac%7B%5Cpartial%20f%28x%2Cy%29%7D%7B%5Cpartial%20y%7D%20%5Cend%7Bpmatrix%7D)

>![equation](https://latex.codecogs.com/gif.latex?%28%5CDelta%7Bx%7D%2C%20%5CDelta%7By%7D%29%3D-%5Ceta%20%5Cbegin%7Bpmatrix%7D%20%5Cfrac%7B%5Cpartial%20z%7D%7B%5Cpartial%20x%7D%2C%26%5Cfrac%7B%5Cpartial%20z%7D%7B%5Cpartial%20y%7D%20%5Cend%7Bpmatrix%7D)
