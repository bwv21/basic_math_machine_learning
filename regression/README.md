# 회귀 Regression
-----------------
```
아래와 같은 데이터가 존재한다고 가정해 보자
```
>![img](./img/reg_00.jpg)

```
모든 점을 지날 수는 없지만 1차 함수로 표현하는 것을 생각할 수 있다
```

>![equation](http://latex.codecogs.com/gif.latex?f_%7B%5Ctheta%7D%28x%29%20%3D%20%5Ctheta_%7B0%7D&plus;%5Ctheta_%7B1%7Dx)

```
가장 데이터를 잘 나타내는 매개변수(theta)를 구하는 것을 목표로 한다
위의 식에서는 기울기(theta1)와 절편(theta0)을 찾는 것이 된다
```

### 오차함수(목적함수)
```
오차는 관측값과 함수값의 차이(붉은선)을 말한다
오차의 합을 최소화하면 적당한 매개변수를 찾았다고 말할 수 있다
```
```
관측값을 y라 할 때 오차함수는 다음과 같이 쓸 수 있다
E는 오차(Error)를 의미한다
```
> ![equation](http://latex.codecogs.com/gif.latex?E%28%5Ctheta%29%3D%5Cfrac%7B1%7D%7B2%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28y_%7Bi%7D-f_%7B%5Ctheta%7D%28x_%7Bi%7D%29%29%5E2)
```

차이를 제곱을 한 것과 1/2를 곱한 이유는 미분과 관계가 있다
  - 제곱이 아닌 절댓값을 사용하면 미분할 수 없는 부분이 생긴다
  - 1/2를 곱한 이유는 미분 이후에 식을 정리하기 위함이다
    - 1/2를 곱해도 최솟값의 위치는 변하지 않는다
```

> ![img](./img/reg_01.jpg)

### 경사하강법(최급하강법)
```
오차함수의 도함수를 구하고 도함수의 부호를 활용하여 최솟값의 위치를 구한다
도함수 부호의 반대 방향으로 밀면 함수의 최솟값을 향해 움직이는 것을 이용한다
얼마만큼 이동할 것인가는 학습률(eta)로 정할수 있으며 수렴하는 속도를 결정하게 된다
```

> ![img](./img/reg_02.jpg)

```
위 내용을 종합하여 매개변수 갱신식을 나타내면 다음과 같다
```
> ![equation](http://latex.codecogs.com/gif.latex?x%3A%3Dx-%5Ceta%20%5Cfrac%7B%5Cmathrm%7Bd%7D%7D%7B%5Cmathrm%7Bd%7D%20x%7Df%28x%29)

### 목적함수가 최솟값이 되는 매개변수 결정
>![equation](http://latex.codecogs.com/gif.latex?E%28%5Ctheta%29%3D%5Cfrac%7B1%7D%7B2%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28y_%7Bi%7D-f_%7B%5Ctheta%7D%28x_%7Bi%7D%29%29%5E2)

```
목적함수는 theta0과 theta1을 가지고 있는 f(x)를 포함한다
이와같은 매개변수가 두 개인 이변수 함수는 편미분을 계산해야 한다 (d -> round-d)
따라서 매개변수 갱신식은 다음과 같다
```

>![equation](http://latex.codecogs.com/gif.latex?%5Ctheta_%7B0%7D%3A%3D%5Ctheta_%7B0%7D-%5Ceta%5Cfrac%7B%5Cpartial%20E%7D%7B%5Cpartial%20%5Ctheta_%7B0%7D%7D)

>![equation](http://latex.codecogs.com/gif.latex?%5Ctheta_%7B1%7D%3A%3D%5Ctheta_%7B1%7D-%5Ceta%5Cfrac%7B%5Cpartial%20E%7D%7B%5Cpartial%20%5Ctheta_%7B1%7D%7D)

```
E안에 f가 있기 때문에 합성함수의 미분을 사용한다
합성함수 미분에 대한 간략한 예는 아래와 같다
```
>![equation](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20%7D%7B%5Cmathrm%7Bd%7D%20x%7Df%28g%28x%29%29)

>![equation](http://latex.codecogs.com/gif.latex?f%28x%29%3Dx%5E2&plus;10)

>![equation](http://latex.codecogs.com/gif.latex?g%28x%29%3Dx&plus;3)

>![equation](http://latex.codecogs.com/gif.latex?y%3Df%28u%29)

>![equation](http://latex.codecogs.com/gif.latex?u%3Dg%28x%29)

>![equation](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20y%7D%7B%5Cmathrm%7Bd%7D%20x%7D%3D%5Cfrac%7B%5Cmathrm%7Bd%7D%20y%7D%7B%5Cmathrm%7Bd%7D%20u%7D%20%5Ccdot%20%5Cfrac%7B%5Cmathrm%7Bd%7D%20u%7D%7B%5Cmathrm%7Bd%7D%20x%7D%3D2u%5Ccdot1%3D2%28x&plus;3%29)

```
각 매개변수에 대해 미분한다
```

>![equation](http://latex.codecogs.com/gif.latex?u%3DE%28%5Ctheta%29)

>![equation](http://latex.codecogs.com/gif.latex?v%3Df_%7B%5Ctheta%7D%28x%29)

```
첫번째 매개변수(theta0) 미분
```

>![equation](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20u%7D%7B%5Cpartial%20%5Ctheta_%7B0%7D%7D%3D%5Cfrac%7B%5Cpartial%20u%7D%7B%5Cpartial%20v%7D%5Ccdot%5Cfrac%7B%5Cpartial%20v%7D%7B%5Cpartial%20%5Ctheta_%7B0%7D%7D)

>![equation](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20u%7D%7B%5Cpartial%20v%7D%3D%5Cfrac%7B%5Cpartial%7D%7B%5Cpartial%20v%7D%28%5Cfrac%7B1%7D%7B2%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28y_%7Bi%7D-v%29%5E2%29)

>>![equation](http://latex.codecogs.com/gif.latex?%3D%5Cfrac%7B1%7D%7B2%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28%5Cfrac%7B%5Cpartial%7D%7B%5Cpartial%20v%7D%28y_%7Bi%7D%5E2-2vy_%7Bi%7D%5E2&plus;v%5E2%29%29)

>>![equation](http://latex.codecogs.com/gif.latex?%3D%5Cfrac%7B1%7D%7B2%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28-2y_%7Bi%7D&plus;2v%29)

>>![equation](http://latex.codecogs.com/gif.latex?%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28v-y_%7Bi%7D%29)

>![equation](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20v%7D%7B%5Cpartial%20%5Ctheta_%7B0%7D%7D%3D%5Cfrac%7B%5Cpartial%7D%7B%5Cpartial%20%5Ctheta_%7B0%7D%7D%28%5Ctheta_0&plus;%5Ctheta_1x%29%3D1)

```
정리하면
```
>![equation](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20u%7D%7B%5Cpartial%20%5Ctheta_%7B0%7D%7D%3D%5Cfrac%7B%5Cpartial%20u%7D%7B%5Cpartial%20v%7D%5Ccdot%5Cfrac%7B%5Cpartial%20v%7D%7B%5Cpartial%20%5Ctheta_%7B0%7D%7D)

>>![equation](http://latex.codecogs.com/gif.latex?%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28v-y_%7Bi%7D%29%5Ccdot1)

>>![equation](http://latex.codecogs.com/gif.latex?%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28f_%7B%5Ctheta%7D%28x_%7Bi%7D%29-y_%7Bi%7D%29)

```
두번째 매개변수(theta1) 미분
```
>![equation](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20u%7D%7B%5Cpartial%20%5Ctheta_%7B1%7D%7D%3D%5Cfrac%7B%5Cpartial%20u%7D%7B%5Cpartial%20v%7D%5Ccdot%5Cfrac%7B%5Cpartial%20v%7D%7B%5Cpartial%20%5Ctheta_%7B1%7D%7D)

```
앞쪽 미분은 첫번째와 같으므로 뒤쪽만 하면 된다
```
>![equation](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20v%7D%7B%5Cpartial%20%5Ctheta_%7B1%7D%7D%3D%5Cfrac%7B%5Cpartial%7D%7B%5Cpartial%20%5Ctheta_%7B1%7D%7D%28%5Ctheta_%7B0%7D&plus;%5Ctheta_%7B1%7Dx%29%3Dx)

```
결과는 아래와 같다
```
>![equation](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20u%7D%7B%5Cpartial%20%5Ctheta_%7B1%7D%7D%3D%5Cfrac%7B%5Cpartial%20u%7D%7B%5Cpartial%20v%7D%5Ccdot%5Cfrac%7B%5Cpartial%20v%7D%7B%5Cpartial%20%5Ctheta_%7B1%7D%7D)

>>![equation](http://latex.codecogs.com/gif.latex?%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28v-y_%7Bi%7D%29%5Ccdot%20x_%7Bi%7D)

>>![equation](http://latex.codecogs.com/gif.latex?%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28f_%7B%5Ctheta%7D%28x_%7Bi%7D%29-y_%7Bi%7D%29%5Ccdot%20x_%7Bi%7D)

```
최종 갱신식은 다음과 같다
```
>![equation](http://latex.codecogs.com/gif.latex?%5Ctheta_%7B0%7D%3A%3D%5Ctheta_%7B0%7D-%5Ceta%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28f_%7B%5Ctheta%7D%28x_%7Bi%7D%29-y_%7Bi%7D%29)

>![equation](http://latex.codecogs.com/gif.latex?%5Ctheta_%7B1%7D%3A%3D%5Ctheta_%7B1%7D-%5Ceta%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28f_%7B%5Ctheta%7D%28x_%7Bi%7D%29-y_%7Bi%7D%29%5Ccdot%20x_%7Bi%7D)

```
1차 함수의 회귀의 예를 들었지만, n차 함수로 확장하여 생각해 볼 수도 있다
```
>![equation](http://latex.codecogs.com/gif.latex?f_%7B%5Ctheta%7D%28x%29%3D%5Ctheta_%7B0%7D&plus;%5Ctheta_%7B1%7Dx&plus;%5Ctheta_%7B2%7Dx%5E2&plus;%5Ccdots%20&plus;%5Ctheta_%7Bn%7Dx%5En)

```
n차를 생각하기 전에 2차 함수와 갱신식을 보면
```
>![equation](http://latex.codecogs.com/gif.latex?f%28x%29%3D%5Ctheta_0&plus;%5Ctheta_1x%5E&plus;%5Ctheta_2x%5E2)

>![equation](http://latex.codecogs.com/gif.latex?%5Ctheta_%7B0%7D%3A%3D%5Ctheta_%7B0%7D-%5Ceta%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28f_%7B%5Ctheta%7D%28x_%7Bi%7D%29-y_%7Bi%7D%29)

>![equation](http://latex.codecogs.com/gif.latex?%5Ctheta_%7B1%7D%3A%3D%5Ctheta_%7B1%7D-%5Ceta%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28f_%7B%5Ctheta%7D%28x_%7Bi%7D%29-y_%7Bi%7D%29%5Ccdot%20x_%7Bi%7D)

>![equation](http://latex.codecogs.com/gif.latex?%5Ctheta_2%3A%3D%5Ctheta_2-%5Ceta%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28f_%5Ctheta%28x_i%29-y_i%29%5Ccdot%20x_i%5E2)

```
합성함수 미분의 앞쪽은 변화하지 않고 뒤쪽의 차수만 증가하는 것을 확인할 수 있다
이렇게 차수를 늘린 함수를 사용하는 것을 다항식 회귀라고 한다
```

```
x^k의 매개변수인 theta-k의 갱신식은 다음과 같다
```
>![equation](http://latex.codecogs.com/gif.latex?%5Ctheta_%7Bk%7D%3A%3D%5Ctheta_%7Bk%7D-%5Ceta%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28f_%7B%5Ctheta%7D%28x_%7Bi%7D%29-y_%7Bi%7D%29x_%7Bi%7D%5Ek)

```
차수가 아닌 변수(파라메터 or 피처)의 개수가 늘어난 경우도 생각해 볼 수 있다
식으로 나타내면 다음과 같다
```
>![equation](http://latex.codecogs.com/gif.latex?f_%7B%5Ctheta%7D%28x_%7B1%7D%2C...%2Cx_%7Bn%7D%29%3D%5Ctheta_%7B0%7D%20&plus;%20%5Ctheta_%7B1%7Dx_%7B1%7D&plus;%20%5Ccdots%20&plus;%20%5Ctheta_%7Bn%7Dx_%7Bn%7D)

```
이런 형태인 경우에는 벡터를 이용해 표현하면 간단하다
차원을 맞추기 위해서 1을 추가한다
```
>![equation](http://latex.codecogs.com/gif.latex?x_%7B0%7D%3D1)

>![equation](http://latex.codecogs.com/gif.latex?%5Cboldsymbol%7B%5Ctheta%7D%3D%5Cbegin%7Bbmatrix%7D%20%5Ctheta_%7B0%7D%5C%5C%20%5Ctheta_%7B1%7D%5C%5C%20%5Ctheta_%7B2%7D%5C%5C%20%5Cvdots%20%5C%5C%20%5Ctheta_%7Bn%7D%20%5Cend%7Bbmatrix%7D%20%5Cmathbf%7Bx%7D%3D%5Cbegin%7Bbmatrix%7D%20x_%7B0%7D%5C%5C%20x_%7B1%7D%5C%5C%20x_%7B2%7D%5C%5C%20%5Cvdots%20%5C%5C%20x_%7Bn%7D%20%5Cend%7Bbmatrix%7D)

```
벡터를 전치해서 서로 곱하면 표현이 간단해 진다
```
>![equation](http://latex.codecogs.com/gif.latex?%5Cboldsymbol%7B%5Ctheta%7D%5E%7BT%7D%5Ctextbf%7Bx%7D%3D%5Ctheta_%7B0%7Dx_%7B0%7D&plus;%5Ctheta_%7B1%7Dx_%7B1%7D&plus;%5Ccdots&plus;%5Ctheta_%7Bn%7Dx_%7Bn%7D)

>![equation](http://latex.codecogs.com/gif.latex?f_%7B%5Ctheta%7D%28x%29%3D%5Cboldsymbol%7B%5Ctheta%7D%5E%7BT%7D%5Ctextbf%7Bx%7D)

```
j번째 매개변수의 갱신식도 편미분과 합성함수의 미분을 이용한다
```
>![equation](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20u%7D%7B%5Cpartial%20x%7D%3D%5Cfrac%7B%5Cpartial%20u%7D%7B%5Cpartial%20v%7D%5Ccdot%5Cfrac%7B%5Cpartial%20v%7D%7B%5Cpartial%20%5Ctheta_j%7D)

>>![equation](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20v%7D%7B%5Cpartial%20%5Ctheta_j%7D%3D%5Cfrac%7B%5Cpartial%20%7D%7B%5Cpartial%20%5Ctheta_j%7D%28%5Cmathbf%7B%5Ctheta%7D%5ET%5Cmathbf%7Bx%7D%29)

>![equation](http://latex.codecogs.com/gif.latex?%3D%5Cfrac%7B%5Cpartial%20%7D%7B%5Cpartial%20x%7D%28%5Ctheta_0x_0&plus;%5Ctheta_1x_1&plus;%5Ccdots&plus;%5Ctheta_nx_n%29)

>![equation](http://latex.codecogs.com/gif.latex?%3Dx_j)

```
따라서 j번째 매개변수의 갱신식은 다음과 같다
이렇게 여러 개의 변수를 사용하는 것을 중회귀라 한다
```
>![equation](http://latex.codecogs.com/gif.latex?%5Ctheta_%7Bj%7D%3A%3D%5Ctheta_%7Bj%7D-%5Ceta%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28f_%7B%5Ctheta%7D%28x_%7Bi%7D%29-y_%7Bi%7D%29x_%7Bij%7D)

### 경사하강법의 단점
```
모든 학습 데이터에 대해 계산하면 느리며 국소해에 빠질 가능성이 있다
```
#### 확률 경사하강법
```
학습 데이터를 무작위로 골라서 매개변수 갱신에 사용한다
(k는 무작위로 선택한 인덱스)
```
>![equeation](http://latex.codecogs.com/gif.latex?%5Ctheta_%7Bj%7D%3A%3D%5Ctheta_%7Bj%7D-%5Ceta%28f_%7B%5Ctheta%7D%28x_%7Bk%7D%29-y_%7Bk%7D%29x_%7Bkj%7D)

#### 미니배치법
```
무작위로 m개 선택한 학습 데이터의 인덱스 집합을 K라고 두면 아래와 같다
```
>![equation](http://latex.codecogs.com/gif.latex?%5Ctheta_%7Bj%7D%3A%3D%5Ctheta_%7Bj%7D-%5Ceta%5Csum_%7Bk%5Cin%20K%7D%28f_%7B%5Ctheta%7D%28x_%7Bk%7D%29-y_%7Bk%7D%29x_%7Bik%7D)
