<img src="https://capsule-render.vercel.app/api?type=wave&color=auto&height=300&section=header&text=보험료%20예측%20앱&fontSize=90" />

⚒️ Tools

<img src="https://img.shields.io/badge/Github-181717?style=flat-square&logo=GitHub&logoColor=white"/> <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/> <img src="https://img.shields.io/badge/Jupyter notebook-F37626?style=flat-square&logo=Jupyter&logoColor=white"/> <img src="https://img.shields.io/badge/Amazon AWS-232F3E?style=flat-square&logo=Amazon AWS&logoColor=white"/>

📜 language

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>

# 앱 설명

### 이 프로젝트는 사용자의 데이터 ( 나이, 성별, 체질량지수, 자녀의 수, 흡연유무 ) 를 통하여 보험료(미국)를 예측해줍니다.

## Jupyter notebook
### 컬럼 별 히스토그램, 상관관계를 분석하였고
### LinearRegression 모델을 통해 값을 예측하도록 모델링해 학습시켰다

## visual studio code 
### streamlit 라이브러리를 통해서 Home 화면에 타이틀과 동영상을 넣고 페이지를 열고 바로 이용할 수 있게
### 좌측 사이드바에 사용자의 데이터를 넣을수 있게 하였다 
### EDA에는 각 컬럼별 의미, 나이/BMI/보험료의 최대최소, 사용된 데이터, 기초통계, 히스토그램, 상관관계를 넣었다

## AWS EC2
### SSH를 통해서 데이터를 업데이트하는것이 아닌 Actions를 통해 바로 ec2에 업데이트하게 설정하였다



# 앱 사용법과 스크린샷

![화면 캡처 2022-12-23 112334](https://user-images.githubusercontent.com/120348468/209258518-8c09dcfc-cd95-48d5-bdd5-36f9fd3020cf.png)
![화면 캡처 2022-12-23 112351](https://user-images.githubusercontent.com/120348468/209258525-df921d17-0bc6-48d2-bbfb-0133910412a5.png)
![화면 캡처 2022-12-23 112406](https://user-images.githubusercontent.com/120348468/209258531-a64c709b-4e29-4beb-aa4c-81f03382cc36.png)
![화면 캡처 2022-12-23 112432](https://user-images.githubusercontent.com/120348468/209258534-9a8d5608-2b39-48b1-b881-bcdc2b66e3ec.png)
![화면 캡처 2022-12-23 112724](https://user-images.githubusercontent.com/120348468/209258785-38bc27a0-32a4-4229-b423-0ac34c4c3e04.png)

### 사이드바에 순서대로 나이, 성별, 체질량 지수, 자녀의 수, 흡연유무를 넣고
### 기다리면 하단에 예상 보험료가 나온다

# 앱의 문제점

### 해당 프로젝트에는 한가지 문제점이 있다
### LinearRegression 을 통해 모델링해서 학습 시킨 데이터의 양이 너무 적어
### 나이가 매우 어리거나 체질량 지수가 너무 낮을 경우 마이너스의 데이터가 나온다
### 디버깅을 위해서는 더 많은 양의 데이터가 필요할 것 같다

# 프로젝트에 사용한 데이터 출처

### 보험료 데이터 : https://www.kaggle.com/datasets/mirichoi0218/insurance
### 동영상 데이터 : https://www.youtube.com/watch?v=eZqZJXG3HBk
