from flask import Flask, render_template, jsonify, redirect, url_for

app = Flask(__name__)

# ----------------------------------------------------
# 1. 프로젝트 데이터 정의 (스크린샷 내용과 동일)
# ----------------------------------------------------
PROJECT_DATA = {
    # 0. 메인 페이지 정보
    "main_info": {
        "title": "캡스톤 프로젝트 소개",
        "subtitle": "작품주제 | 실용적 근거 | 핵심기능 | 구현환경 | 팀원 구성 및 역할"
    },
    
    # 1. 작품주제 (Subject)
    "subject": {
        "title": "작품주제",
        "data": {
            "제목": "디지털 디톡스",
            "설명": "스마트폰 중독 현상을 해결하기 위한 앱"
        }
    },
    
    # 2. 실용적 근거 (Rationale)
    "rationale": {
        "title": "실용적 근거",
        "data": {
            "문제": "최근 많은 사람들이 스마트폰 중독 현상을 겪고 있다.",
            "근거": "설문 결과 80%가 중독 현상을 겪었다.",
            "가치": "사용자들의 시간 활용성 증가, 중독 현상 해결"
        }
    },
    
    # 3. 핵심기능 (Features)
    "features": {
        "title": "핵심기능",
        "data": [
            {"desc": "휴대폰 전체, 앱별 잠금"},
            {"desc": "앱의 하루 사용시간을 정하여 지정된 시간만큼 사용"},
            {"desc": "캘린더 공유 기능으로 친구들과 일정공유"}
        ]
    },
    
    # 4. 구현환경 (Environment)
    "environment": {
        "title": "구현환경",
        "data": {
            "Front-End(프론트엔드)": "android student",
            "Back-End(백엔드)": "node.js, firebase",
            "Deploy(배포)": "google cloud"
        }
    },
    
    # 5. 팀 구성 및 역할 (Team)
    "team": {
        "title": "팀원 구성 및 역할",
        "data": [
            {"name": "우기현", "role": "UI/UX 디자인, 프로젝트 개발"},
            {"name": "진건웅", "role": "프론트엔드, 안드로이드 개발"},
            {"name": "백승엽", "role": "백엔드, 자료 수집 및 발표"}
        ]
    }
}

# 페이지 경로와 데이터 키 매핑 (URL과 데이터 키를 매칭)
PAGE_MAP = {
    '작품주제': 'subject',
    '실용적 근거': 'rationale',
    '핵심기능': 'features',
    '구현환경': 'environment',
    '팀원 구성 및 역할': 'team',
}


# ----------------------------------------------------
# 2. 웹 페이지 라우팅
# ----------------------------------------------------

@app.route('/')
@app.route('/main')
def main_page():
    """메인 페이지 라우팅"""
    return render_template('main.html', data=PROJECT_DATA, page_map=PAGE_MAP)

@app.route('/<page_id>')
def content_page(page_id):
    """서브 페이지 공통 라우팅"""
    
    page_key = page_id
    
    if page_key in PROJECT_DATA:
        page_data = PROJECT_DATA[page_key]
        main_info = PROJECT_DATA['main_info']
        return render_template('content.html', page_data=page_data, main_info=main_info, page_map=PAGE_MAP)
    else:
        return redirect(url_for('main_page'))

# ----------------------------------------------------
# 3. API 라우팅
# ----------------------------------------------------
@app.route('/api/<page_name>')
def api_data(page_name):
    """/api/<페이지 명> 요청 시 JSON 데이터 반환"""
    
    if page_name in PROJECT_DATA and 'data' in PROJECT_DATA[page_name]:
        return jsonify(PROJECT_DATA[page_name]['data'])
    else:
        return jsonify({"error": f"API for '{page_name}' not found or not available."}), 404

# ----------------------------------------------------
# 4. 애플리케이션 실행
# ----------------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
