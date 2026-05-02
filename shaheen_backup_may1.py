import streamlit as st
import openai

# إعدادات الواجهة الاحترافية (شاهين: العلم نور)
st.set_page_config(page_title="شاهين: العلم نور", page_icon="🦅")

# شعار وتنسيق بصري ذهبي وأزرق
st.markdown("""
    <style>
    .main { background-color: #001f3f; color: #ffffff; }
    .stButton>button { background-color: #FFD700; color: #001f3f; font-weight: bold; width: 100%; border-radius: 10px; }
    </style>
    """, unsafe_allow_index=True)

st.title("🦅 شاهين: العلم نور")
st.subheader("منصة الذكاء الاصطناعي الشاملة - بإشراف محمد شاهين")
st.markdown("---")

# المحرك الأساسي (تصحيح الخطأ 401)
client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

# إدارة نظام الرسائل والربح
if "messages" not in st.session_state:
    st.session_state.messages = []
if "msg_count" not in st.session_state:
    st.session_state.msg_count = 0

# عرض المحادثة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# منطق المنافسة والربح
if st.session_state.msg_count < 3:
    if prompt := st.chat_input("اسأل شاهين... العلم نور"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.msg_count += 1
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                response = client.chat.completions.create(
                    model="google/gemini-2.0-flash-001",
                    messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                )
                full_response = response.choices[0].message.content
                st.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            except Exception as e:
                st.error(f"خطأ في الاتصال: {e}")
else:
    st.warning("⚠️ انتهت الرسائل المجانية. العلم نور، وللاستمرار في الاستفادة من خبرات شاهين، نرجو الاشتراك.")
    pay_url = "https://paypal.me/MOHDSHAHEEN"
    st.markdown(f'<a href="{pay_url}" target="_blank"><button style="width:100%; height:60px; background-color:#FFD700; color:#001f3f; border:none; border-radius:12px; cursor:pointer; font-size:18px; font-weight:bold;">تفعيل الاشتراك (19 ريال) عبر PayPal</button></a>', unsafe_allow_index=True)
