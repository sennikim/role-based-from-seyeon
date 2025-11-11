import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Fashion Expert Chatbot", page_icon="💄", layout="centered")

st.markdown("""
<style>
body {background-color: #f9f4f7;}
.stApp {font-family: 'Didot', 'Georgia', serif;}
h1, h2, h3 {color: #8b5e83;}
.sidebar .sidebar-content {background-color: #f3e9ef; border-right: 2px solid #d4bcd2;}
.stButton>button {background-color: #cfa0c3; color: white; border-radius: 10px; height: 3em; width: 100%; font-weight: bold;}
.stButton>button:hover {background-color: #b685a8; color: #fff;}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🎨 Choose Your Fashion Role")

roles = {
    "패션 큐레이터": "당신은 감각적이면서도 역사적 통찰이 깊은 패션 큐레이터입니다. 왕실 복식부터 현대 런웨이까지, 문화적 맥락과 미적 감수성을 연결하며 설명하세요.",
    "트렌드 분석가": "당신은 데이터 기반의 트렌드 분석가입니다. 소비자 심리, 컬러, 패브릭, 시장 데이터를 인사이트 중심으로 전달하세요.",
    "패션 마케터": "당신은 글로벌 패션 마케터입니다. 브랜드 콘셉트를 명확히 정의하고, SNS·캠페인 전략을 설득력 있게 제시하세요.",
    "패션 에디터": "당신은 매거진의 패션 에디터입니다. 감각적인 문장과 자신감 있는 어조로 트렌드를 해석하고, 독자에게 영감을 주세요.",
    "패션 디자이너": "당신은 창의적이고 실험적인 패션 디자이너입니다. 형태, 소재, 컬러의 조합을 예술적 관점으로 제안하세요.",
    "스타일리스트": "당신은 스타일리스트입니다. 상대의 체형, 무드, 상황에 맞는 스타일링을 따뜻하면서도 실용적으로 조언하세요.",
    "패션 리서처": "당신은 학문적 시각을 가진 패션 리서처입니다. 지속가능성, 기술, 소비문화의 변화를 객관적 근거로 설명하세요."
}

selected_role = st.sidebar.radio("전문가 역할을 선택하세요:", list(roles.keys()))
role_prompt = roles[selected_role]

st.title("💬 Fashion Expert Chatbot")
st.caption("Ask anything — from runway trends to royal court fashion history 👑")

client = OpenAI(api_key=st.secrets["openai"]["api_key"])
user_input = st.text_area("💭 패션 관련 질문을 입력하세요:")

if st.button("✨ 대화 시작"):
    if user_input.strip() == "":
        st.warning("질문을 입력해주세요 💬")
    else:
        with st.spinner("패션 전문가의 통찰을 불러오는 중... 🪄"):
            messages = [
                {"role": "system", "content": role_prompt},
                {"role": "user", "content": user_input}
            ]
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages
            )
            st.subheader(f"🧠 {selected_role}의 답변")
            st.write(response.choices[0].message.content)
            st.success("✨ 완성된 답변입니다!")

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color:#8b5e83;'>© 2025 Sungkyunkwan University | Designed by Kim Seyeon</p>",
    unsafe_allow_html=True
)
