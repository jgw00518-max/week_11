# 디지털 디톡스 - 캡스톤 프로젝트

스마트폰 중독 현상을 해결하기 위한 디지털 디톡스 앱 프로젝트 소개 웹사이트입니다.

## 📋 프로젝트 개요

본 프로젝트는 최근 많은 사람들이 겪고 있는 스마트폰 중독 현상을 해결하기 위한 디지털 디톡스 앱을 소개하는 웹 애플리케이션입니다.

### 주요 특징

- **작품주제**: 디지털 디톡스 - 스마트폰 중독 현상을 해결하기 위한 앱
- **실용적 근거**: 설문 결과 80%가 중독 현상을 겪었으며, 사용자들의 시간 활용성 증가 필요
- **핵심기능**: 
  - 휴대폰 전체, 앱별 잠금
  - 앱의 하루 사용시간 제한
  - 캘린더 공유 기능으로 친구들과 일정공유
- **구현환경**: Android Studio, Node.js, Firebase, Google Cloud
- **팀 구성**: 
  - 우기현 - UI/UX 디자인, 프로젝트 개발
  - 진건웅 - 프론트엔드, 안드로이드 개발
  - 백승엽 - 백엔드, 자료 수집 및 발표

## 🗂️ 프로젝트 구조

```
my_project/
├── app.py                 # Flask 애플리케이션 메인 파일
├── templates/             # HTML 템플릿 폴더
│   ├── main.html         # 메인 페이지
│   └── content.html      # 서브 페이지 공통 템플릿
├── requirements.txt       # Python 패키지 의존성
├── Dockerfile            # Docker 이미지 빌드 설정
├── docker-compose.yml    # Docker Compose 설정
├── .gitignore            # Git 제외 파일 목록
└── README.md             # 프로젝트 문서 (현재 파일)
```

## 🚀 실행 방법

### 1. 로컬 환경에서 실행

#### 사전 요구사항
- Python 3.10 이상
- pip

#### 실행 단계

```bash
# 1. 의존성 패키지 설치
pip install -r requirements.txt

# 2. Flask 애플리케이션 실행
python app.py

# 3. 브라우저에서 접속
# http://localhost:5000
```

### 2. Docker로 실행 (추천)

#### 사전 요구사항
- Docker
- Docker Compose

#### 실행 단계

```bash
# 1. Docker 이미지 빌드 및 컨테이너 실행
docker-compose up --build -d

# 2. 브라우저에서 접속
# http://localhost:5000

# 3. 로그 확인
docker-compose logs -f

# 4. 컨테이너 중지
docker-compose down
```

## 🌐 페이지 구성

### 웹 페이지 라우트

| 경로 | 설명 |
|------|------|
| `/` 또는 `/main` | 메인 페이지 (프로젝트 소개) |
| `/subject` | 작품주제 페이지 |
| `/rationale` | 실용적 근거 페이지 |
| `/features` | 핵심기능 페이지 |
| `/environment` | 구현환경 페이지 |
| `/team` | 팀원 구성 및 역할 페이지 |

### API 엔드포인트

JSON 형태로 데이터를 제공하는 API 엔드포인트:

| API 경로 | 설명 | 응답 형식 |
|----------|------|-----------|
| `/api/subject` | 작품주제 데이터 | JSON |
| `/api/rationale` | 실용적 근거 데이터 | JSON |
| `/api/features` | 핵심기능 데이터 | JSON |
| `/api/environment` | 구현환경 데이터 | JSON |
| `/api/team` | 팀원 구성 데이터 | JSON |

#### API 사용 예시

```bash
# curl을 사용한 API 호출
curl http://localhost:5000/api/subject

# 응답 예시
{
  "제목": "디지털 디톡스",
  "설명": "스마트폰 중독 현상을 해결하기 위한 앱"
}
```

## 🛠️ 기술 스택

### Front-End (프론트엔드)
- HTML5
- CSS3 (모던 그라데이션 디자인)

### Back-End (백엔드)
- Python 3.10
- Flask (파이썬 웹 프레임워크)

### 실제 앱 개발 환경
- **Front-End**: Android Studio
- **Back-End**: Node.js, Firebase
- **Deploy**: Google Cloud

### 웹사이트 배포
- Docker & Docker Compose
- AWS EC2 (선택사항)

## 📦 배포 방법

### AWS EC2에 배포하기

1. **EC2 인스턴스 생성**
   - Ubuntu Server 선택
   - 보안 그룹에서 5000번 포트 개방
   - 키 페어 생성 및 다운로드

2. **Docker 설치**
   ```bash
   # Ubuntu 기준
   sudo apt update
   sudo apt install docker.io docker-compose -y
   sudo systemctl start docker
   sudo systemctl enable docker
   ```

3. **프로젝트 배포**
   ```bash
   # 프로젝트 클론
   git clone <repository-url>
   cd my_project
   
   # Docker Compose로 실행
   sudo docker-compose up -d
   ```

4. **접속 확인**
   - 브라우저에서 `http://<EC2-Public-IP>:5000` 접속

### Google Cloud에 배포하기 (선택사항)

```bash
# Google Cloud SDK 설치 후
gcloud init
gcloud app deploy
```

## 👥 팀 구성 및 역할

- **우기현** - UI/UX 디자인, 프로젝트 개발
- **진건웅** - 프론트엔드, 안드로이드 개발
- **백승엽** - 백엔드, 자료 수집 및 발표

## 📊 프로젝트 배경

### 문제 인식
최근 많은 사람들이 스마트폰 중독 현상을 겪고 있습니다.

### 근거
설문 결과 **80%**가 중독 현상을 겪었다는 통계가 있습니다.

### 기대 효과
- 사용자들의 시간 활용성 증가
- 스마트폰 중독 현상 해결
- 건강한 디지털 라이프스타일 구축

## 🎯 핵심 기능

1. **휴대폰 전체, 앱별 잠금**
   - 특정 시간대에 앱 사용 제한
   - 집중 시간 확보

2. **앱의 하루 사용시간 제한**
   - 일일 사용 시간 설정
   - 초과 시 자동 잠금

3. **캘린더 공유 기능**
   - 친구들과 일정 공유
   - 함께 디지털 디톡스 실천

## 📝 Git 사용법

```bash
# 변경사항 추가
git add .

# 커밋
git commit -m "Update: 프로젝트 설명 수정"

# GitHub에 푸시
git push origin main
```

## 🔧 문제 해결

### Docker 컨테이너가 실행되지 않을 때
```bash
# 로그 확인
docker-compose logs

# 컨테이너 재시작
docker-compose restart
```

### 포트 충돌 시
```bash
# docker-compose.yml에서 포트 변경
ports:
  - "8080:5000"  # 8080으로 변경
```

## 📧 문의

프로젝트에 대한 문의사항이 있으시면 팀원에게 연락해주세요.

## 📄 라이선스

본 프로젝트는 교육 목적의 캡스톤 프로젝트입니다.

---

**제작일**: 2025년  
**프로젝트 유형**: 캡스톤 프로젝트 소개 웹사이트  
**주제**: 디지털 디톡스 - 스마트폰 중독 해결 앱
