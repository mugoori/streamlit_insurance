<img src="https://capsule-render.vercel.app/api?type=wave&color=auto&height=300&section=header&text=보험료%20예측%20앱&fontSize=90" />

⚒️ Tools

<img src="https://img.shields.io/badge/Github-181717?style=flat-square&logo=GitHub&logoColor=white"/> <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/> <img src="https://img.shields.io/badge/Jupyter notebook-F37626?style=flat-square&logo=Jupyter&logoColor=white"/>

📜 language

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>

# 앱 설명

### 이 프로젝트는 사용자의 데이터 ( 나이, 성별, 체질량지수, 자녀의 수, 흡연유무 ) 를 통하여 보험료를 예측해준다.

### 해당 프로젝트에는 jupyter notebook 을 사용하여 보험료 데이터를 가져와 기초통계를 분석하고  
### 컬럼 별 히스토그램, 상관관계를 분석하였고
### LinearRegression 모델을 통해 값을 예측하도록 모델링해 학습시켰다
### visual studio code 를 사용하여 Home 과 EDA로 나누어 작업 했으며
### Home 화면에는 타이틀과 동영상이 들어가고 페이지를 열고 바로 이용할 수 있게
### 좌측 사이드바에 사용자의 데이터를 넣을수 있게 하였다 
### EDA 에는 사용된 데이터, 기초통계, 히스토그램, 상관관계를 넣었다
### putty를 사용하여 github 저장소를 clone 하고 AWS에 작업하였다.

# 앱 사용법

![화면 캡처 2022-12-15 152932](https://user-images.githubusercontent.com/120348468/207788806-54813a94-e4cd-4167-b673-06ddfd6411cd.png)


### 사이드바에 순서대로 나이, 성별, 체질량 지수, 자녀의 수, 흡연유무를 넣고
### 기다리면 하단에 예상 보험료가 나온다

# 앱의 문제점

### 해당 프로젝트에는 한가지 문제점이 있다
### LinearRegression 을 통해 모델링해서 학습 시킨 데이터의 양이 너무 적어
### 나이가 매우 어리거나 체질량 지수가 너무 낮을 경우 마이너스의 데이터가 나온다
### 디버깅을 위해서는 더 많은 양의 데이터가 필요할 것 같다

# 프로젝트에 사용한 데이터 출처

### 보험료 데이터 : https://www.kaggle.com/datasets/mirichoi0218/insurance
### 동영상 데이터 : https://www.youtube.com/watch?v=47cAxRX3aDg&t=0s
