# 파이썬 공식 이미지를 기반으로 사용 (적절한 버전 선택)
FROM python:3.10-slim

# 작업 디렉토리 설정
WORKDIR /usr/src/app

# 파이썬 의존성 파일 복사 및 설치
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 및 템플릿 복사
COPY . .

# Flask 앱이 5000번 포트를 사용하도록 노출 (ECS/EC2 설정과 일치)
EXPOSE 5000

# 컨테이너가 시작될 때 Flask 앱 실행
CMD ["python", "app.py"]