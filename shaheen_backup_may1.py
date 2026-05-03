import streamlit as st
import requests
import json
import os

# 1. إعدادات الواجهة
st.set_page_config(page_title="شاهين شات", page_icon="🦅", layout="wide")

# 2. التنسيق الأنيق (برواز خفيف، الهوية يمين)
st.markdown("""
    <style>
    .main .block-container { padding-left: 20% !important; padding-right: 20% !important; }
    .header-container { display: flex; flex-direction: column; align-items: flex-end; width: 100%; margin-bottom: 25px; }
    .stTitle { color: #000000 !important; font-family: 'Segoe UI', sans-serif; font-size: 34px; font-weight: bold; text-align: right; margin-top: 5px; }
    .social-btns-container { display: flex; flex-direction: row-reverse; gap: 10px; margin-top: 10px; }
    .social-btn { padding: 5px 12px; background-color: #ffffff; color: #000000 !important; border: 1px solid #800000; border-radius: 6px; text-decoration: none !important; font-size: 11px; font-weight: bold; }
    .stChatMessage { border: 1.5px solid #800000 !important; border-radius: 12px; background-color: #ffffff !important; margin-bottom: 15px; }
    .stChatInputContainer { border: 1.5px solid #800000 !important; border-radius: 10px; }
    [data-testid="stSidebar"] { display: none; }
    </style>
    """, unsafe_allow_html=True)

# 3. عرض الهوية وأيقونات التواصل
st.markdown('<div class="header-container">', unsafe_allow_html=True)
logo_file = "شاهين.jpeg"
if os.path.exists(logo_file):
    st.image(logo_file, width=110)
st.markdown('<h1 class="stTitle">شاهين شات</h1>', unsafe_allow_html=True)

share_url = "https://shaheen-chat-system.streamlit.app"
st.markdown(f"""
    <div class="social-btns-container">
        <a href="https://twitter.com/intent/tweet?url={share_url}" target="_blank" class="social-btn">منصة X</a>
        <a href="https://www.facebook.com/sharer/sharer.php?u={share_url}" target="_blank" class="social-btn">فيسبوك</a>
        <a href="https://www.instagram.com/" target="_blank" class="social-btn">انستغرام</a>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 4. جلب المفاتيح وتطهيرها
def fetch_safe_key(key_name):
    val = st.secrets.get(key_name, "")
    return str(val).strip().replace('"', '').replace("'", "")

API_KEY = fetch_safe_key("OPENROUTER_API_KEY")
PAYPAL_ID = fetch_safe_key("PAYPAL_CLIENT_ID")

if "messages" not in st.session_state: st.session_state.messages = []
if "msg_count" not in st.session_state: st.session_state.msg_count = 0
if "is_paid" not in st.session_state: st.session_state.is_paid = False

for message in st.session_state.messages:
    with st.chat_message(message["role"]): st.markdown(message["content"])

# 5. منطق التشغيل
if st.session_state.msg_count < 10 or st.session_state.is_paid:
    if prompt := st.chat_input("تحدث مع شاهين..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.msg_count += 1
        with st.chat_message("user"): st.markdown(prompt)
        
        with st.chat_message("assistant"):
            headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json", "X-Title": "Shaheen Chat"}
            payload = {"model": "google/gemini-2.0-flash-001", "messages": [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]}
            try:
                response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload, timeout=35)
                if response.status_code == 200:
                    res = response.json()['choices'][0]['message']['content']
                    st.markdown(res)
                    st.session_state.messages.append({"role": "assistant", "content": res})
                else:
                    st.error(f"تنبيه تقني: {response.status_code}. يرجى مراجعة الرصيد والمفتاح الجديد.")
            except:
                st.error("عطل في الاتصال، يرجى المحاولة لاحقاً.")
else:
    st.warning("⚠️ انتهت المحاولات المجانية.")
    if PAYPAL_ID:
        # واجهة دفع مبسطة
        st.markdown(f'<a href="https://paypal.me/MOHDSHAHEEN" target="_blank"><button style="width:100%; height:50px; background-color:#800000; color:white; border-radius:10px; cursor:pointer; font-weight:bold; border:none;">تفعيل الاشتراك (12 ريال قطري)</button></a>', unsafe_allow_html=True)
