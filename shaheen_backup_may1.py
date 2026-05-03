import streamlit as st
import requests
import json
import os

# 1. إعدادات الهوية والواجهة العالمية
st.set_page_config(page_title="شاهين شات", page_icon="🦅", layout="wide")

# 2. التنسيق الاحترافي الجديد (الهوية على اليمين، الأيقونات تحت العنوان)
st.markdown("""
    <style>
    /* موازنة الهوامش الجانبية 20% لتركيز المحتوى */
    .main .block-container { padding-left: 20% !important; padding-right: 20% !important; max-width: 100%; }
    
    /* كتلة الهوية (الشعار والاسم والأزرار) في أقصى اليمين */
    .header-container { 
        display: flex; 
        flex-direction: column; 
        align-items: flex-end; 
        width: 100%;
        margin-bottom: 30px;
    }
    .logo-img { width: 120px; border-radius: 12px; border: 3px solid #800000; margin-bottom: 10px; }
    .stTitle { color: #000000 !important; font-family: 'Segoe UI', sans-serif; font-size: 36px; font-weight: bold; margin: 0; text-align: right; }

    /* تنسيق أزرار التواصل الاجتماعي تحت العنوان */
    .social-btns-container { display: flex; flex-direction: row-reverse; gap: 10px; margin-top: 15px; }
    .social-btn { 
        padding: 6px 12px; 
        background-color: #ffffff; 
        color: #000000 !important; 
        border: 1.5px solid #800000;
        border-radius: 8px; 
        text-decoration: none !important; 
        font-size: 12px; 
        font-weight: bold;
        transition: 0.3s;
    }
    .social-btn:hover { background-color: #fceeee; }

    /* فقاعات الدردشة وصندوق الكتابة */
    .stChatMessage { border: 3px solid #800000 !important; border-radius: 15px; background-color: #ffffff !important; }
    .stChatInputContainer { border: 2px solid #800000 !important; border-radius: 12px; }
    
    [data-testid="stSidebar"] { display: none; }
    </style>
    """, unsafe_allow_html=True)

# 3. بناء الهوية البصرية (الجهة اليمنى)
st.markdown('<div class="header-container">', unsafe_allow_html=True)

# البحث التلقائي عن الشعار
logo_file = "شاهين.jpeg"
if not os.path.exists(logo_file):
    for file in os.listdir("."):
        if file.startswith("لقطة") and file.lower().endswith((".png", ".jpg", ".jpeg")):
            logo_file = file
            break

if os.path.exists(logo_file):
    st.image(logo_file, width=120)
else:
    st.markdown('<h2 style="color:#800000;">🦅</h2>', unsafe_allow_html=True)

st.markdown('<h1 class="stTitle">شاهين شات</h1>', unsafe_allow_html=True)

# إضافة أزرار التواصل الاجتماعي تحت كلمة شاهين شات بمسافة جيدة
share_url = "https://shaheen-chat-system.streamlit.app"
st.markdown(f"""
    <div class="social-btns-container">
        <a href="https://twitter.com/intent/tweet?url={share_url}" target="_blank" class="social-btn">منصة X</a>
        <a href="https://www.facebook.com/sharer/sharer.php?u={share_url}" target="_blank" class="social-btn">فيسبوك</a>
        <a href="https://www.instagram.com/" target="_blank" class="social-btn">انستغرام</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# 4. نظام التشغيل والأمان
try:
    API_KEY = st.secrets["OPENROUTER_API_KEY"].strip().replace('"', '').replace("'", "")
except Exception:
    st.error("يرجى مراجعة مفتاح الأمان.")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []
if "msg_count" not in st.session_state:
    st.session_state.msg_count = 0

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if st.session_state.msg_count < 5:
    if prompt := st.chat_input("تحدث مع شاهين العالمي..."):
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
                response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, data=json.dumps(payload), timeout=45)
                if response.status_code == 200:
                    res = response.json()['choices'][0]['message']['content']
                    st.markdown(res)
                    st.session_state.messages.append({"role": "assistant", "content": res})
                else:
                    st.error("يرجى مراجعة رصيد العمليات العالمي.")
            except Exception as e:
                st.error(f"عطل اتصال: {e}")
else:
    st.warning("⚠️ انتهت المحاولات المجانية.")
    st.markdown(f'<a href="https://paypal.me/MOHDSHAHEEN" target="_blank"><button style="width:100%; height:55px; background-color:#800000; color:white; border-radius:12px; cursor:pointer; font-size:18px; font-weight:bold; border:none;">تفعيل الاشتراك (12 ريال قطري)</button></a>', unsafe_allow_html=True)
