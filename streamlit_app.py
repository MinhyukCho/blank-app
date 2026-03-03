import streamlit as st
import streamlit.components.v1 as components
import json

# 1. 페이지 및 레이아웃 설정
st.set_page_config(page_title="AI 유튜브 요약 프롬프트", page_icon="📝")

st.title("🚀 AI 인사이트 실행 지침서 생성기")
st.markdown("유튜브 URL만 넣으면 실무에 즉시 적용 가능한 지침서 프롬프트를 만들어드립니다.")

# 2. 사이드바 설정
with st.sidebar:
    st.header("⚙️ 옵션 설정")
    target = st.text_input("읽는 사람 (Target)", value="신입사원", help="요약본을 볼 대상자를 입력하세요.")
    focus = st.selectbox("분석 중점 (Focus)", 
                        ["단계별 실행 방법", "논리적 허점 분석", "핵심 데이터 추출"], 
                        index=0)
    tone = st.radio("어조 (Tone)", ["비판적인 사수", "친절한 멘토"], index=1)

# 3. 메인 입력창
url = st.text_input("유튜브 URL을 입력하세요", placeholder="https://www.youtube.com/watch?v=...")

# 4. 프롬프트 생성 로직
if url:
    # 펀딩 상세페이지에 들어갈 핵심 가치 로직
    generated_prompt = f"""당신은 고도로 훈련된 비즈니스 정보 분석가입니다. 
제공된 유튜브 자막 데이터(URL: {url})를 바탕으로, 단순히 내용을 요약하는 것이 아니라 
[{target}]이 즉시 실무에 적용할 수 있는 [실행 지침서]를 작성하세요.

작성 가이드라인:
1. 핵심 통찰(Deep Insight): 영상 전체를 관통하는 원리 1가지를 정의할 것.
2. 분석 중점: [{focus}]에 초점을 맞춰 상세히 분석할 것.
3. 실행 리스트(To-Do): 오늘 바로 실행할 수 있는 액션 플랜 3가지를 도출할 것.
4. 어조: [{tone}]의 말투로 작성할 것."""

    st.subheader("📝 완성된 프롬프트")
    st.code(generated_prompt, language="markdown")

    # 5. [핵심 해결책] HTML/JS 기반 무적 복사 버튼
    # 자바스크립트가 문자열을 안전하게 읽도록 JSON 인코딩 처리
    safe_prompt = json.dumps(generated_prompt)

    copy_button_html = f"""
        <div id="copy-container">
            <button id="copy-btn" style="
                width: 100%;
                background-color: #FF4B4B;
                color: white;
                border: none;
                padding: 14px;
                border-radius: 10px;
                cursor: pointer;
                font-weight: bold;
                font-size: 16px;
                transition: 0.3s;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            ">
                📋 프롬프트 복사하기
            </button>
        </div>

        <script>
        document.getElementById('copy-btn').addEventListener('click', function() {{
            const text = {safe_prompt};
            
            // 1. 임시 textarea 생성 (iframe 보안 우회용 고전 방식)
            const textArea = document.createElement("textarea");
            textArea.value = text;
            document.body.appendChild(textArea);
            
            // 2. 텍스트 선택 및 복사
            textArea.select();
            try {{
                const successful = document.execCommand('copy');
                if (successful) {{
                    // 버튼 텍스트 변경 피드백
                    this.innerText = '✅ 복사 완료!';
                    this.style.backgroundColor = '#28a745';
                    setTimeout(() => {{
                        this.innerText = '📋 프롬프트 복사하기';
                        this.style.backgroundColor = '#FF4B4B';
                    }}, 2000);
                }}
            }} catch (err) {{
                alert('복사 실패! 브라우저 설정을 확인해주세요.');
            }}
            
            // 3. 요소 제거
            document.body.removeChild(textArea);
        }});
        </script>
    """
    
    # 컴포넌트 삽입 (height를 버튼 크기에 맞게 조절)
    components.html(copy_button_html, height=80)
    
    st.caption("위 버튼을 누르면 클립보드에 복사됩니다. 클로드나 챗GPT에 붙여넣으세요!")

else:
    st.info("유튜브 주소를 입력하면 마법이 시작됩니다.")

# 푸터 섹션
st.divider()
st.markdown("© 2026 AI Prompt Master | [텀블벅 펀딩 구경가기](https://tumblbug.com)")