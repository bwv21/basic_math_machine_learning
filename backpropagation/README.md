# 역전파법 Backpropagation

>![equation](https://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20E%7D%7B%5Cpartial%20w_%7Bji%7D%5E%7B%28l%29%7D%7D%3D%5Cfrac%7B%5Cpartial%20E%7D%7B%5Cpartial%20z_%7Bj%7D%5E%7B%28l%29%7D%7D%5Cfrac%7B%5Cpartial%20z_%7Bj%7D%5E%7B%28l%29%7D%7D%7B%5Cpartial%20w_%7Bji%7D%5E%7B%28l%29%7D%7D)

우변의 두 번째 항
>![equation](https://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20z_%7Bj%7D%5E%7B%28l%29%7D%7D%7B%5Cpartial%20w_%7Bji%7D%5E%7B%28l%29%7D%7D%3Dz_%7Bi%7D%5E%7B%28l-1%29%7D)

우변의 첫 번째 항

>![equation](https://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20E%7D%7B%5Cpartial%20z_%7Bj%7D%5E%7B%28l%29%7D%7D%3D%5Csum_%7Bk%7D%5Cfrac%7B%5Cpartial%20E%7D%7B%5Cpartial%20z_%7Bk%7D%5E%7B%28l&plus;1%29%7D%7D%5Cfrac%7B%5Cpartial%20z_%7Bk%7D%5E%7B%28l&plus;1%29%7D%7D%7B%5Cpartial%20z_%7Bj%7D%5E%7B%28l%29%7D%7D)

양변에 l, l+1 째 층의 입력에 대한 미분이 있는 것에 착안한 정의
>![equation](https://latex.codecogs.com/gif.latex?%5Cdelta%20_%7Bj%7D%5E%7B%28l%29%7D%3D%5Cfrac%7B%5Cpartial%20E%7D%7B%5Cpartial%20z_%7Bj%7D%5E%7B%28l%29%7D%7D)

>![equation](https://latex.codecogs.com/gif.latex?z_%7Bk%7D%5E%7B%28l&plus;1%29%7D%3D%5Csum_%7Bj%7Dw_%7Bjk%7D%5E%7B%28l&plus;1%29%7Da_%7Bj%7D%5E%7B%28l%29%7D%3D%5Csum_%7Bj%7Dw_%7Bjk%7D%5E%7B%28l&plus;1%29%7Df%28z_%7Bj%7D%5E%7B%28l%29%7D%29)

로부터

>![equation](https://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20z_%7Bk%7D%5E%7B%28l&plus;1%29%7D%7D%7B%5Cpartial%20z_%7Bj%7D%5E%7B%28l%29%7D%7D%3Dw_%7Bjk%7D%5E%7B%28l&plus;1%29%7Df%27%28z_%7Bj%7D%5E%7B%28l%29%7D%29)

가 된다는 것을 이용하여 식을 다시 쓰면

>![equation](https://latex.codecogs.com/gif.latex?%5Cdelta%20_%7Bj%7D%5E%7B%28l%29%7D%3D%5Csum_%7Bk%7D%5Cdelta%20_%7Bk%7D%5E%7B%28l&plus;1%29%7D%28w_%7Bjk%7D%5E%7B%28l&plus;1%29%7Df%27%28z_%7Bj%7D%5E%7B%28l%29%7D%29%29)

위 식은 델타 l을 델타 l+1 로 부터 계산할 수 있음을 의미한다

따라서

>![equation](https://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%20E%7D%7B%5Cpartial%20w_%7Bji%7D%5E%7B%28l%29%7D%7D%3D%5Cdelta%20_%7Bj%7D%5E%7B%28l%29%7Dz_%7Bi%7D%5E%7B%28l-1%29%7D)

역전파되는 최초 값은 출력층의 델타L 이 주어지는데 다음과 같이 계산한다

>![equation](https://latex.codecogs.com/gif.latex?%5Cdelta%20_%7Bj%7D%5E%7B%28L%29%7D%3D%5Cfrac%7B%5Cpartial%20E%7D%7B%5Cpartial%20z_%7Bj%7D%5E%7B%28L%29%7D%7D)

구체적인 계산은 오차함수의 종류에 따라 다르다

### 출력층의 델타

역전파 계산의 시작점은 출력층의 델타L 이다. 이를 계산하는 방법은 사용하고 있는 오차함수나 출력층의 활성화 함수가 무엇이냐에 따라 다르지만 대표적인 경우를 살펴본다.

#### 회귀

오차함수를 제곱오차, 출력층 활성화 함수는 항등사상으로 할 경우, 출력층의 유닛 j의 델타L은 다음과 같다

>![equation](https://latex.codecogs.com/gif.latex?E%3D%5Cfrac%7B1%7D%7B2%7D%5Csum_%7Bj%7D%28y_%7Bj%7D-d_%7Bj%7D%29%5E%7B2%7D)

>![equation](https://latex.codecogs.com/gif.latex?a_%7Bj%7D%5E%7BL%7D%3Dz_%7Bj%7D%5E%7BL%7D%3Dy_%7Bj%7D)

>![equation](https://latex.codecogs.com/gif.latex?%5Cdelta%20_%7Bj%7D%5E%7B%28l%29%7D%3D%5Cfrac%7B%5Cpartial%20E%7D%7B%5Cpartial%20z_%7Bj%7D%5E%7B%28L%29%7D%7D%3Dy_%7Bj%7D-d_%7Bj%7D)

#### 이진 분류
오차함수 최대우도함수

출력층의 활성화 함수는 시그모이드 함수

#### 여러 클래스 분류

오차함수는 교차 엔트로피

출력층의 활성화 함수는 소프트맥스 함수

결과적으로 모두 같음