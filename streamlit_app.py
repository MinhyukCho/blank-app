import streamlit as st
import streamlit.components.v1 as components

# 1. 페이지 설정
st.set_page_config(page_title="AI 프롬프트 생성기", page_icon="🚀")

st.title("🚀 AI 인사이트 실행 지침서 생성기")
st.markdown("유튜브 영상을 분석하여 실무에 즉시 적용 가능한 지침서를 만들어주는 프롬프트입니다.")

# 2. 사이드바 - 입력 변수 설정
with st.sidebar:
    st.header("⚙️ 설정")
    target = st.text_input("읽는 사람 (Target)", value="신입사원", help="누가 읽을 요약본인가요?")
    focus = st.selectbox("집중 분야 (Focus)", 
                        ["단계별 실행 방법", "논리적 허점 분석", "핵심 수치 및 데이터"],
                        index=0)
    tone = st.radio("어조 (Tone)", ["비판적인 사수", "친절한 멘토"], index=1)

# 3. 메인 화면 - URL 입력
url = st.text_input("유튜브 URL을 입력하세요", placeholder="https://www.youtube.com/watch?v=...")

# 4. 프롬프트 생성 로직
if url:
    generated_prompt = f"""당신은 고도로 훈련된 비즈니스 정보 분석가입니다. 
제공된 유튜브 자막 데이터(URL: {url})를 바탕으로, 단순히 내용을 요약하는 것이 아니라 
[{target}]이 즉시 실무에 적용할 수 있는 [실행 지침서]를 작성하세요.

작성 가이드라인:
1. 핵심 통찰(Deep Insight): 영상 전체를 관통하는 원리 1가지를 정의할 것.
2. 집중 분야 분석: [{focus}]에 초점을 맞춰 상세히 분석할 것.
3. 실행 리스트(To-Do): 오늘 바로 실행할 수 있는 액션 플랜 3가지를 도출할 것.
4. 어조: [{tone}]의 말투로 작성할 것.
"""

    st.subheader("📝 생성된 프롬프트")
    st.code(generated_prompt, language="markdown")

    # 5. [핵심 기능] 복사 버튼 + st.toast 연동
  import streamlit.components.v1 as components
import json

# ... 기존 프롬프트 생성 코드 이후 ...

if url:
    generated_prompt = f"생성된 프롬프트 내용..." # 실제 변수명에 맞게 수정
    
    # 자바스크립트용 문자열 안전 처리
    safe_prompt = json.dumps(generated_prompt)

    # 버튼과 복사 로직을 하나의 HTML로 통합 (보안 제약 우회)
    copy_html = f"""
        <div id="copy-container">
            <button id="copy-btn" style="
                width: 100%;
                background-color: #FF4B4B;
                color: white;
                border: none;
                padding: 12px;
                border-radius: 8px;
                cursor: pointer;
                font-weight: bold;
                font-size: 16px;
                margin-top: 10px;
            ">
                📋 프롬프트 복사하기
            </button>
        </div>

        <script>
        document.getElementById('copy-btn').addEventListener('click', function() {{
            const text = {safe_prompt};
            
            // 임시 텍스트 영역을 통한 확실한 복사 방식
            const textArea = document.createElement("textarea");
            textArea.value = text;
            document.body.appendChild(textArea);
            textArea.select();
            
            try {{
                document.execCommand('copy');
                // 부모 창(Streamlit)에 알림을 보내기 위한 설정
                window.parent.postMessage({{type: 'copy-done'}}, '*');
                alert('클립보드에 복사되었습니다!');
            }} catch (err) {{
                console.error('복사 실패:', err);
            }}
            document.body.removeChild(textArea);
        }});
        </script>
    """
    
    # HTML 컴포넌트 실행 (버튼 표시)
    components.html(copy_html, height=70)
else:
    st.info("URL을 입력하면 프롬프트가 자동으로 생성됩니다.")

st.divider()
st.caption("Tip: 복사된 프롬프트를 클로드(Claude)나 챗GPT에 붙여넣어 보세요!")