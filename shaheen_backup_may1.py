import streamlit as st
import requests
import json

# 1. إعدادات الهوية والخصوصية
st.set_page_config(page_title="شاهين شات", page_icon="🦅", layout="centered")

# 2. التصميم (اللون الخمري الملكي والخطوط الاحترافية)
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    .stTitle { color: #800000; text-align: center; font-family: 'Arial', sans-serif; font-size: 50px; font-weight: bold; margin-bottom: 0px; }
    .stChatMessage { border-radius: 20px; padding: 15px; margin-bottom: 10px; }
    [data-testid="stChatMessage"]:nth-child(even) { background-color: #800000; color: white; margin-left: auto; }
    [data-testid="stChatMessage"]:nth-child(odd) { background-color: #ffffff; color: #800000; border: 1px solid #800000; margin-right: auto; }
    /* أزرار المشاركة */
    .share-btn { display: inline-block; padding: 10px 20px; background-color: #800000; color: white; border-radius: 10px; text-decoration: none; font-weight: bold; margin: 5px; }
    </style>
    """, unsafe_allow_html=True)

# عرض الشعار والعنوان فقط
st.markdown('<h1 class="stTitle">🦅 شاهين شات</h1>', unsafe_allow_html=True)

# 3. جلب الأمان من الخزنة
try:
    API_KEY = st.secrets["OPENROUTER_API_KEY"].strip().strip('"')
except Exception:
    st.error("خطأ في نظام الأمان: يرجى مراجعة الخزنة.")
    st.stop()

# 4. ذاكرة المستخدم
if "messages" not in st.session_state:
    st.session_state.messages = []
if "msg_count" not in st.session_state:
    st.session_state.msg_count = 0

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. العمليات والأسعار (الذكاء العالمي)
if st.session_state.msg_count < 5:
    if prompt := st.chat_input("تحدث مع شاهين..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.msg_count += 1
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
            payload = {
                "model": "google/gemini-2.0-flash-001",
                "messages": [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            }
            try:
                response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, data=json.dumps(payload))
                if response.status_code == 200:
                    res = response.json()['choices'][0]['message']['content']
                    st.markdown(res)
                    st.session_state.messages.append({"role": "assistant", "content": res})
                else:
                    st.error("المزود العالمي لا يستجيب حالياً.")
            except:
                st.error("عطل في الاتصال.")
else:
    st.warning("⚠️ انتهت المحاولات المجانية.")
    st.markdown(f'<a href="https://paypal.me/MOHDSHAHEEN" target="_blank" class="share-btn" style="width:100%; text-align:center;">تفعيل الاشتراك (12 ريال قطري)</a>', unsafe_allow_html=True)

# 6. أيقونات التواصل الاجتماعي للتسويق
st.sidebar.title("مشاركة شاهين شات")
share_text = "جرب شاهين شات، أقوى منصة ذكاء اصطناعي عالمية!"
st.sidebar.markdown(f"""
<a href="https://wa.me/?text={share_text}" class="share-btn">واتساب</a>
<a href="https://twitter.com/intent/tweet?text={share_text}" class="share-btn">تويتر</a>
""", unsafe_allow_html=True)
