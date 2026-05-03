import streamlit as st
import requests
import json
import os

# 1. إعدادات الهوية واللغات العالمية
st.set_page_config(page_title="شاهين شات", page_icon="🦅", layout="wide")

# 2. التصميم الاحترافي (البرغندي الملكي والخطوط السوداء)
st.markdown("""
    <style>
    /* زيادة المساحات الجانبية */
    .main .block-container { padding-left: 10%; padding-right: 10%; max-width: 1200px; }
    
    /* تنسيق العنوان والشعار على اليمين */
    .header-container { display: flex; flex-direction: column; align-items: flex-end; margin-bottom: 20px; }
    .logo-img { width: 100px; border-radius: 10px; border: 2px solid #800000; margin-bottom: 5px; }
    .stTitle { color: #000000; font-family: 'Arial', sans-serif; font-size: 32px; font-weight: bold; margin: 0; }

    /* فقاعات الدردشة: خلفية بيضاء وبرواز خمري عريض (Bold) */
    .stChatMessage { 
        background-color: #ffffff !important; 
        border: 3px solid #800000 !important; 
        border-radius: 15px; 
        color: #000000 !important;
        margin-bottom: 20px;
    }
    
    /* صندوق الكتابة: برواز خمري واضح */
    .stChatInputContainer { border: 2px solid #800000 !important; border-radius: 10px; padding: 5px; }

    /* أيقونات التواصل الاجتماعي المحدثة (X, Facebook, Instagram) */
    .share-container { position: fixed; top: 150px; left: 20px; display: flex; flex-direction: column; gap: 12px; z-index: 1000; }
    .share-btn { 
        padding: 10px; 
        background-color: #ffffff; 
        color: #000000 !important; 
        border: 2px solid #800000;
        border-radius: 10px; 
        text-decoration: none; 
        font-size: 13px; 
        text-align: center; 
        font-weight: bold;
        width: 80px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    
    [data-testid="stSidebar"] { display: none; }
    </style>
    """, unsafe_allow_html=True)

# 3. عرض أيقونات التواصل الاجتماعي (تصميم احترافي)
share_url = "https://shaheen-chat-system.streamlit.app"
st.markdown(f"""
    <div class="share-container">
        <a href="https://twitter.com/intent/tweet?url={share_url}" target="_blank" class="share-btn">منصة X</a>
        <a href="https://www.facebook.com/sharer/sharer.php?u={share_url}" target="_blank" class="share-btn">فيسبوك</a>
        <a href="https://www.instagram.com/" target="_blank" class="share-btn">انستغرام</a>
    </div>
    """, unsafe_allow_html=True)

# 4. عرض الشعار والاسم (جهة اليمين)
st.markdown('<div class="header-container">', unsafe_allow_html=True)
logo_file = "شاهين.png" # تم تحديث الاسم بناءً على طلبك
if os.path.exists(logo_file):
    st.image(logo_file, width=100)
else:
    st.markdown('<h2 style="color:#800000;">🦅</h2>', unsafe_allow_html=True)
st.markdown('<h1 class="stTitle">شاهين شات</h1>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 5. نظام الأمان والمفتاح السري
try:
    raw_key = st.secrets["OPENROUTER_API_KEY"]
    API_KEY = "".join(raw_key.split()).replace('"', '').replace("'", "").strip()
except Exception:
    st.error("خطأ: يرجى التحقق من المفتاح في الخزنة.")
    st.stop()

# 6. الذاكرة والدردشة (تدعم العربية والإنجليزية)
if "messages" not in st.session_state:
    st.session_state.messages = []
if "msg_count" not in st.session_state:
    st.session_state.msg_count = 0

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 7. التنفيذ والربح
if st.session_state.msg_count < 5:
    if prompt := st.chat_input("تحدث مع شاهين العالمي... (Ask Shaheen anything)"):
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
                    st.error("تنبيه: المزود يرفض الطلب، يرجى مراجعة الرصيد.")
            except Exception as e:
                st.error(f"عطل اتصال: {e}")
else:
    st.warning("⚠️ انتهت المحاولات المجانية.")
    st.markdown(f'<a href="https://paypal.me/MOHDSHAHEEN" target="_blank"><button style="width:100%; height:55px; background-color:#800000; color:white; border-radius:12px; cursor:pointer; font-size:18px; font-weight:bold; border:none;">تفعيل الاشتراك (12 ريال قطري)</button></a>', unsafe_allow_html=True)
