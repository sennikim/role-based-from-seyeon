import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="🎭 Role-based Creative Chatbot", page_icon="🎨", layout="centered")

st.title("🎭 Role-based Creative Chatbot")
st.caption("Built for 'Art & Advanced Big Data' • Prof. Jahwan Koo (SKKU)")

st.markdown("---")

st.header("🔑 API & Role Settings")
api_key = st.text_input("Enter your OpenAI API Key:", type="password")

roles = {
    "👗 Fashion Stylist": "You are a fashion stylist. Explain every idea using the language of color, texture, and silhouette. Think visually — how something would appear, feel, and harmonize.",
    "🧵 Fashion Designer": "You are a fashion designer. Create artistic yet practical concepts focusing on material, form, and innovation.",
    "💄 Fashion Editor": "You are a fashion editor. Write sharply, capture trends with eloquence, and express opinions like in Vogue magazine.",
    "📈 Trend Analyst": "You are a trend analyst. Interpret cultural shifts, colors, and materials with data-driven insight.",
    "👜 Fashion Marketer": "You are a global fashion marketer. Craft campaign ideas and brand narratives that emotionally connect with audiences.",
    "🎨 Fashion Curator": "You are a fashion curator. Explain fashion pieces with historical and cultural storytelling.",
    "🔬 Fashion Researcher": "You are a fashion researcher. Discuss sustainability, digital fashion, and consumer behavior academically."
}

selected_role = st.selectbox("Choose a role:", list(roles.keys()))
role_prompt = roles[selected_role]

st.markdown("---")

st.header("💬 Enter your question or idea:")
user_input = st.text_area("Write your prompt here... (e.g., 'Suggest an outfit inspired by Joseon Dynasty aesthetics')")

if st.button("✨ Generate Response"):
    if not api_key:
        st.error("Please enter your OpenAI API key 🔑")
    elif not user_input.strip():
        st.warning("Please write a question or idea 💬")
    else:
        client = OpenAI(api_key=api_key)
        with st.spinner("Thinking creatively... 🪄"):
            messages = [
                {"role": "system", "content": role_prompt},
                {"role": "user", "content": user_input}
            ]
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=messages
                )
                answer = response.choices[0].message.content
                st.subheader(f"{selected_role} says:")
                st.write(answer)
            except Exception as e:
                st.error(f"Error: {e}")

st.markdown("---")
st.markdown("<p style='text-align: center; color: grey;'>© 2025 Sungkyunkwan University | Designed by Kim Seyeon</p>", unsafe_allow_html=True)
