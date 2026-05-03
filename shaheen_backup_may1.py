import streamlit as st
import requests
import json
import os

# 1. إعدادات الهوية والواجهة العالمية
st.set_page_config(page_title="شاهين شات", page_icon="🦅", layout="wide")

# 2. التصميم الملكي ومنع التداخل
st.markdown("""
    <style>
    /* توسيع الهوامش الجانبية 25% من كل جانب لتركيز الشات في المنتصف */
    .main .block-container { padding-left: 25% !important; padding-right: 25% !important; max-width: 100%; }
    
    /* تثبيت كتلة العنوان والشعار في أقصى اليمين لمنع التداخل */
    .header-container { 
        display: flex; 
        flex-direction: column; 
        align-items: flex-end; 
        justify-content: flex-end;
        width: 100%;
        margin-bottom: 40px;
        text-align: right;
    }
    .logo-img { width: 140px; border-radius: 15px; border: 3px solid #800000; margin-bottom: 10px; }
    .stTitle { color: #000000 !important; font-family: 'Segoe UI', sans-serif; font-size: 38px; font-weight: bold; margin: 0; padding: 0; line-height: 1.2; }

    /* فقاعات الدردشة: برواز خمري عريض */
    .stChatMessage { 
        background-color: #ffffff !important; 
        border: 4px solid #800000 !important; 
        border-radius: 20px; 
        color: #000000 !important;
        margin-bottom: 25px;
    }
    
    /* صندوق الكتابة ببرواز خمري */
    .stChatInputContainer { border: 2.5px solid #800000 !important; border-radius: 15px; }

    /* أيقونات التواصل: تثبيت في أقصى اليسار بعيداً عن الشعار */
    .share-container { position: fixed; top: 120px; left: 20px; display: flex; flex-direction: column; gap: 15px; z-index: 1000; }
    .share-btn { 
        padding: 12px; 
        background-color: #ffffff; 
        color: #000000 !important; 
        border: 2px solid #800000;
        border-radius: 12px; 
        text-decoration: none !important; 
        font-size: 14px; 
        text-align: center; 
        font-weight: bold;
        width: 90px;
    }
    
    [data-testid="stSidebar"] { display: none; }
    </style>
    """, unsafe_allow_html=True)

# 3. أيقونات التواصل الاجتماعي (جهة اليسار)
share_url = "https://shaheen-chat-system.streamlit.app"
st.markdown(f"""
    <div class="share-container">
        <a href="https://twitter.com/intent/tweet?url={share_url}" target="_blank" class="share-btn">منصة X</a>
        <a href="https://www.facebook.com/sharer/sharer.php?u={share_url}" target="_blank" class="share-btn">فيسبوك</a>
        <a href="https://www.instagram.com/" target="_blank" class="share-btn">انستغرام</a>
    </div>
    """, unsafe_allow_html=True)

# 4. كتلة اليمين: الشعار فوق العنوان مباشرة
st.markdown('<div class="header-container">', unsafe_allow_html=True)

# البحث عن ملف الشعار (شاهين.jpeg أو لقطة الشاشة)
logo_file = "شاهين.jpeg"
if not os.path.exists(logo_file):
    # محاولة البحث عن أي ملف يبدأ بـ "لقطة" إذا لم يجد "شاهين.jpeg"
    for file in os.listdir("."):
        if file.startswith("لقطة") and file.lower().endswith((".png", ".jpg", ".jpeg")):
            logo_file = file
            break

if os.path.exists(logo_file):
    st.image(logo_file, width=140)
else:
    st.markdown('<h2 style="color:#800000;">🦅</h2>', unsafe_allow_html=True)

st.markdown('<h1 class="stTitle">شاهين شات</h1>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 5. نظام الأمان والمفتاح
try:
    API_KEY = st.secrets["OPENROUTER_API_KEY"].strip().replace('"', '').replace("'", "")
except Exception:
    st.error("خطأ في الأمان: يرجى التحقق من الخزنة.")
    st.stop()

# 6. الذاكرة والدردشة
if "messages" not in st.session_state:
    st.session_state.messages = []
if "msg_count" not in st.session_state:
    st.session_state.msg_count = 0

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 7. نظام التشغيل والربح
if st.session_state.msg_count < 5:
    if prompt := st.chat_input("تحدث مع شاهين العالمي... Ask Shaheen anything"):
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
                    st.error(f"تنبيه تقني ({response.status_code}): المزود يطلب مراجعة الحساب.")
            except Exception as e:
                st.error(f"عطل اتصال: {e}")
else:
    st.warning("⚠️ انتهت المحاولات المجانية.")
    st.markdown(f'<a href="https://paypal.me/MOHDSHAHEEN" target="_blank"><button style="width:100%; height:55px; background-color:#800000; color:white; border-radius:12px; cursor:pointer; font-size:18px; font-weight:bold; border:none;">تفعيل الاشتراك (12 ريال قطري)</button></a>', unsafe_allow_html=True)
