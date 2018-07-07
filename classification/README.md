# 분류 Classification
---------------------
### 로지스틱 회귀 logistic regression
```
가로가 긴 것을 1, 세로가 긴 것을 0이라 가정한다
```
##### 시그모이드 sigmoid
```
매개변수가 있는 함수는 다음과 같이 정의할 수 있다
```
>![equation](http://latex.codecogs.com/gif.latex?f_%5Ctheta%28x%29%3D%5Ctheta%5ETx)
```
회귀와 마찬가지로 매개변수는 theta를 사용하면 함수의 모양은 다음과 같다
```
>![equation](http://latex.codecogs.com/gif.latex?f_%5Ctheta%28x%29%20%3D%5Cfrac%7B1%7D%7B1&plus;%5Cmathrm%7Bexp%7D%28-%5Ctheta%5ETx%29%7D%3D%5Cfrac%7B1%7D%7B1&plus;e%5E%7B-%5Ctheta%5ETx%7D%7D)

>![img](./img/sigmoid_function_00.jpg)

```
시그모이드 함수는 0 < f(x) < 1 이므로 확률처럼 다룰 수 있다
```
##### 최급하강법
```
미지의 데이터 x가 가로가 더 긴 모양일 때의 확률을 다음과 같이 정한다
```
>![equation](http://latex.codecogs.com/gif.latex?P%28y%3D1%7Cx%29%3Df_%5Ctheta%28x%29)

```
0.5를 기준으로 크거나 같으면 가로로 길고, 작으면 세로로 길다고 분류할 수 있다
```
>![equation](http://latex.codecogs.com/gif.latex?y%3D%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%201%5C%20%5C%20%28f_%5Ctheta%28x%29%5Cgeq%200.5%29%5C%5C%200%5C%20%5C%20%28f_%5Ctheta%28x%29%3C%200.5%29%20%5Cend%7Bmatrix%7D%5Cright.)
```
위 식은 아래와 같이 쓸 수도 있다
```
>![equation](http://latex.codecogs.com/gif.latex?y%3D%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%201%5C%20%5C%20%28%5Ctheta%5ETx%5Cgeq%200%29%5C%5C%200%5C%20%5C%20%28%5Ctheta%5ETx%3C%200%29%20%5Cend%7Bmatrix%7D%5Cright.)

>![img](./img/sigmoid_function_01.jpg)
```
가로축이 x1이고, 세로축이 x2인 그래프를 생각하고, 임의의 매개변수를 이용하여 계산해 보면
```
>![equation](http://latex.codecogs.com/gif.latex?%5Ctheta%3D%5Cbegin%7Bbmatrix%7D%20%5Ctheta_0%5C%5C%20%5Ctheta_1%5C%5C%20%5Ctheta_2%20%5Cend%7Bbmatrix%7D%3D%5Cbegin%7Bbmatrix%7D%20-100%5C%5C%202%5C%5C%201%20%5Cend%7Bbmatrix%7D%2C%20%5C%20x%3D%5Cbegin%7Bbmatrix%7D%201%5C%5C%20x_1%5C%5C%20x_2%20%5Cend%7Bbmatrix%7D)

>![equation](http://latex.codecogs.com/gif.latex?%5Ctheta%5ETx%3D-100%5Ccdot%201&plus;2x_1&plus;x_2%20%5Cgeq%200)
>![equation](http://latex.codecogs.com/gif.latex?x_2%5Cgeq%20-2x_1&plus;100)

```
그래프를 그려서 보면 다음과 같다
```
>![img](./img/logreg_00.png)

```
직선을 경계선으로 해서 한쪽이 가로로 긴 것, 다른 한쪽이 세로로 긴 것으로 분류된다
이렇게 데이터를 분류하기 위한 직선을 결정경계라고 한다
```
```
알맞은 매개변수 theta를 구하기 위해 목적함수를 정의하고 미분해서 매개변수 갱신식을 구하면 된다
이러한 알고리즘을 로지스틱 회귀라 한다
```
### 우도함수
```
로지스틱 회귀의 목적은 다음과 같이 말할 수 있다
```
> ```y=1``` 일때는 확률 ```P(y=1|x)``` 가 최대
> ```y=0``` 일때는 확률 ```P(y=0|x)``` 가 최대
```
학습 데이터 3개의 y가 0, 1, 0 라 가정하자
모든 학습 데이터는 서로 관계가 없이 독립적으로 발생한다고 생각하면 다음과 같다
```
>![equation](http://latex.codecogs.com/gif.latex?L%28%5Ctheta%29%3DP%28y_1%3D0%7Cx_1%29P%28y_2%3D1%7Cx_2%29P%28y_3%3D0%7Cx_3%29)

```
이것을 일반화 해서 다시 쓰면
```
>![equation](http://latex.codecogs.com/gif.latex?L%28%5Ctheta%29%3D%5Cprod_%7Bi%3D1%7D%5E%7Bn%7DP%28y_i%3D1%7Cx_i%29%5E%7By_i%7DP%28y_i%3D0%7Cx_i%29%5E%7B1-y_i%7D)

```
이 목적함수를 우도함수(Likelihood)라 한다
우도함수를 가장 크게 하는 매개변수가 학습 데이터를 가장 잘 설명한다
```
```
우도함수를 그대로 다루기에는 어려운 점이 있다
확률을 곱하면서 값이 점점 작아진다는 것과 곱셈이라는 점이다
양변에 로그(log)를 취해서 계산하기 쉽도록 한다
```
>![equation](http://latex.codecogs.com/gif.latex?logL%28%5Ctheta%29%3Dlog%5Cprod_%7Bi%3D1%7D%5E%7Bn%7DP%28y_i%3D1%7Cx_i%29%5E%7By_i%7DP%28y_i%3D0%7Cx_i%29%5E%7B1-y_i%7D)

```
로그 함수는 단순 증가 함수이므로 우도함수를 최대화 하는 것과 로그를 취한 우도함수를 최대화 하는 것은 의미가 같다
```
```
로그를 취한 대수우도함수는 다음과 같이 변형할 수 있다
```
>![equation](http://latex.codecogs.com/gif.latex?logL%28%5Ctheta%29%3Dlog%5Cprod_%7Bi%3D1%7D%5E%7Bn%7DP%28y_i%3D1%7Cx_i%29%5E%7By_i%7DP%28y_i%3D0%7Cx_i%29%5E%7B1-y_i%7D)

>>![equation](http://latex.codecogs.com/gif.latex?%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28logP%28y_i%3D1%7Cx_i%29%5E%7By_i%7D&plus;logP%28y_i%3D0%7Cx_i%29%5E%7B1-y_i%7D%29)

>>![equation](http://latex.codecogs.com/gif.latex?%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28%7By_i%7DlogP%28y_i%3D1%7Cx_i%29&plus;%28%7B1-y_i%7D%29logP%28y_i%3D0%7Cx_i%29%29)

>>![equation](http://latex.codecogs.com/gif.latex?%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28%7By_i%7DlogP%28y_i%3D1%7Cx_i%29&plus;%28%7B1-y_i%7D%29log%281-P%28y_i%3D1%7Cx_i%29%29%29)

>>![equation](http://latex.codecogs.com/gif.latex?%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28%7By_i%7Dlogf_%5Ctheta%28x_i%29&plus;%28%7B1-y_i%7D%29log%281-f_%5Ctheta%28x_i%29%29%29)

```
따라서 로지스틱 회귀는 다음의 대수우도함수를 목적함수로 사용한다
```
>![equation](http://latex.codecogs.com/gif.latex?logL%28%5Ctheta%29%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28%7By_i%7Dlogf_%5Ctheta%28x_i%29&plus;%28%7B1-y_i%7D%29log%281-f_%5Ctheta%28x_i%29%29%29)
```
각각의 매개변수들로 미분해야 한다
```
>![equation](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20logL%28%5Ctheta%29%7D%7B%5Cpartial%20%5Ctheta_j%7D%3D%5Cfrac%7B%5Cpartial%20%7D%7B%5Cpartial%20%5Ctheta_j%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28%7By_i%7Dlogf_%5Ctheta%28x_i%29&plus;%28%7B1-y_i%7D%29log%281-f_%5Ctheta%28x_i%29%29%29)

```
합성함수의 미분을 사용한다
```
>![equation](http://latex.codecogs.com/gif.latex?u%3DlogL%28%5Ctheta%29)

>![equation](http://latex.codecogs.com/gif.latex?v%3Df_%5Ctheta%28x%29)

>![equation](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20u%7D%7B%5Cpartial%20%5Ctheta_j%7D%3D%5Cfrac%7B%5Cpartial%20u%7D%7B%5Cpartial%20v%7D%5Ccdot%5Cfrac%7B%5Cpartial%20v%7D%7B%5Cpartial%20%5Ctheta_j%7D)
```
첫 번째 항목 계산
```
>![equation](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20u%7D%7B%5Cpartial%20v%7D%3D%5Cfrac%7B%5Cpartial%20%7D%7B%5Cpartial%20v%7D%28%7By_i%7Dlog%28v%29&plus;%28%7B1-y_i%7D%29log%281-v%29%29)

```
log(v)의 미분은 1/v 라는 것을 이용한다
log(1-v)의 경우는 아래와 같이 합성함수 미분을 사용한다
```
>![equation](http://latex.codecogs.com/gif.latex?s%3D1-v)

>![equation](http://latex.codecogs.com/gif.latex?t%3Dlog%28s%29)

>![equation](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%20t%7D%7B%5Cmathrm%7Bd%7D%20v%7D%3D%5Cfrac%7B%5Cmathrm%7Bd%7D%20t%7D%7B%5Cmathrm%7Bd%7D%20s%7D%5Ccdot%5Cfrac%7B%5Cmathrm%7Bd%7D%20s%7D%7B%5Cmathrm%7Bd%7D%20v%7D)

>>![equation](http://latex.codecogs.com/gif.latex?%3D%5Cfrac%7B1%7D%7Bs%7D%5Ccdot-1)

>>![equation](http://latex.codecogs.com/gif.latex?%3D-%5Cfrac%7B1%7D%7B1-v%7D)
```
따라서 미분한 결과는 다음과 같다
```

>![equation](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20u%7D%7B%5Cpartial%20v%7D%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28%5Cfrac%7By_i%7D%7Bv%7D-%5Cfrac%7B1-y_i%7D%7B1-v%7D%29)

```
두 번째 항목은 시그모이드 함수를 미분해야 한다
시그모이드 함수는 다음과 같이 미분한다
```
>![equation](http://latex.codecogs.com/gif.latex?s%28x%29%3D%5Cfrac%7B1%7D%7B1&plus;exp%28-x%29%7D)

>![equation](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7D%7D%7B%5Cmathrm%7Bd%7D%20x%7Ds%28x%29%3Ds%28x%29%281-s%28x%29%29)

```
합성함수의 미분을 사용하면
```
>![equation](http://latex.codecogs.com/gif.latex?z%3D%5Ctheta%5ETx)

>![equation](http://latex.codecogs.com/gif.latex?v%3Df_%5Ctheta%28x%29%3D%5Cfrac%7B1%7D%7B1&plus;exp%28-z%29%7D)

>![equation](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20v%7D%7B%5Cpartial%20%5Ctheta_j%7D%3D%5Cfrac%7B%5Cpartial%20v%7D%7B%5Cpartial%20z%7D%5Ccdot%5Cfrac%7B%5Cpartial%20z%7D%7B%5Cpartial%20%5Ctheta_j%7D)

>![equation](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20v%7D%7B%5Cpartial%20z%7D%3Dv%281-v%29)
```
다음으로 z를 미분한다
```
>![equation](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20z%7D%7B%5Cpartial%20%5Ctheta_j%7D%3D%5Cfrac%7B%5Cpartial%20%7D%7B%5Cpartial%20%5Ctheta_j%7D%5Ctheta%5ETx)

>>![equation](http://latex.codecogs.com/gif.latex?%3D%5Cfrac%7B%5Cpartial%20%7D%7B%5Cpartial%20%5Ctheta_j%7D%28%5Ctheta_0x_0&plus;%5Ctheta_1x_1&plus;%5Ccdots%20&plus;%5Ctheta_nx_n%29)

>>![equation](http://latex.codecogs.com/gif.latex?%3Dx_j)
```
따라서 두 번째 항목의 미분은 다음과 같다
```
>![equation](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20v%7D%7B%5Cpartial%20%5Ctheta_j%7D%3D%5Cfrac%7B%5Cpartial%20v%7D%7B%5Cpartial%20z%7D%5Ccdot%5Cfrac%7B%5Cpartial%20z%7D%7B%5Cpartial%20%5Ctheta_j%7D)

>>![equation](http://latex.codecogs.com/gif.latex?%3Dv%281-v%29%5Ccdot%20x_j)

```
결과를 대입해 정리하면
```
>![equation](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20u%7D%7B%5Cpartial%20%5Ctheta_j%7D%3D%5Cfrac%7B%5Cpartial%20u%7D%7B%5Cpartial%20v%7D%5Ccdot%5Cfrac%7B%5Cpartial%20v%7D%7B%5Cpartial%20%5Ctheta_j%7D)

>>![equation](http://latex.codecogs.com/gif.latex?%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28%5Cfrac%7By_i%7D%7Bv%7D-%5Cfrac%7B1-y_i%7D%7B1-v%7D%29%5Ccdot%20v%281-v%29%5Ccdot%20x_%7Bij%7D)

>>![equation](http://latex.codecogs.com/gif.latex?%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28y_i%281-v%29-%281-y_i%29v%29x_%7Bij%7D)

>>![equation](http://latex.codecogs.com/gif.latex?%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28y_i-y_iv-v&plus;y_iv%29x_%7Bij%7D)

>>![equation](http://latex.codecogs.com/gif.latex?%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28y_i-v%29x_%7Bij%7D)

>>![equation](http://latex.codecogs.com/gif.latex?%3D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28y_i-f_%5Ctheta%28x_i%29%29x_%7Bij%7D)

```
이 식으로 매개변수 갱신식을 만들면 된다
최대화가 목적이므로 최소화할 때와는 반대로 부호가 양수가 된다
```
>![equation](http://latex.codecogs.com/gif.latex?%5Ctheta_j%3A%3D%5Ctheta_j&plus;%5Ceta%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28y_i-f_%5Ctheta%28x_i%29%29x_%7Bij%7D)

```
다음과 같이 다시 쓸 수 있다
```
>![equation](http://latex.codecogs.com/gif.latex?%5Ctheta_j%3A%3D%5Ctheta_j-%5Ceta%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28f_%5Ctheta%28x_i%29-y_i%29x_i_j)
