import streamlit as st
import openai

# إعدادات الواجهة الاحترافية (الأزرق والذهبي)
st.set_page_config(page_title="شاهين شات - المنصة العالمية", page_icon="🦅")

# شعار مقترح وتنسيق بصري
st.markdown("""
    <style>
    .main { background-color: #001f3f; color: #ffffff; }
    .stButton>button { background-color: #FFD700; color: #001f3f; font-weight: bold; width: 100%; border-radius: 10px; }
    .stTextInput>div>div>input { background-color: #f0f2f6; }
    </style>
    """, unsafe_allow_index=True)

st.title("🦅 شاهين شات: منصة الذكاء الاصطناعي الشاملة")
st.markdown("---")

# ربط المحرك بالمفتاح المفعّل (رصيد 10 دولار)
client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

# نظام إدارة الرسائل والربح
if "messages" not in st.session_state:
    st.session_state.messages = []
if "msg_count" not in st.session_state:
    st.session_state.msg_count = 0

# عرض الرسائل السابقة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# منطق الدفع والمنافسة
if st.session_state.msg_count < 3:
    if prompt := st.chat_input("...اسأل شاهين عن أي شيء (متبقي لك رسائل مجانية)"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.msg_count += 1
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                response = client.chat.completions.create(
                    model="google/gemini-2.0-flash-001",
                    messages=[{"role": "m.role", "content": m["content"]} for m in st.session_state.messages]
                )
                full_response = response.choices[0].message.content
                st.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            except Exception as e:
                st.error(f"حدث خطأ تقني: {e}")
else:
    st.warning("⚠️ لقد استهلكت رسائلك المجانية الثلاث.")
    st.info("للاستمرار في الحصول على استشارات شاهين في المقاولات، الموارد البشرية، والأدب، اشترك الآن بـ 19 ريالاً فقط.")
    pay_url = "https://paypal.me/MOHDSHAHEEN"
    st.markdown(f'<a href="{pay_url}" target="_blank"><button style="width:100%; height:50px; background-color:#FFD700; border:none; border-radius:10px; cursor:pointer; font-weight:bold;">إتمام الدفع عبر PayPal للانطلاق</button></a>', unsafe_allow_index=True)
