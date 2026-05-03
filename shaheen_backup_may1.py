import streamlit as st
import requests
import json
import os

# 1. إعدادات الهوية والواجهة
st.set_page_config(page_title="شاهين شات", page_icon="🦅", layout="wide")

# 2. التنسيق الاحترافي (برواز رقيق + هوية يمين)
st.markdown("""
    <style>
    .main .block-container { padding-left: 20% !important; padding-right: 20% !important; }
    .header-container { display: flex; flex-direction: column; align-items: flex-end; width: 100%; margin-bottom: 25px; }
    .stTitle { color: #000000 !important; font-family: 'Segoe UI', sans-serif; font-size: 34px; font-weight: bold; text-align: right; }
    .social-btns-container { display: flex; flex-direction: row-reverse; gap: 10px; margin-top: 10px; }
    .social-btn { padding: 5px 12px; background-color: #ffffff; color: #000000 !important; border: 1px solid #800000; border-radius: 6px; text-decoration: none !important; font-size: 11px; font-weight: bold; }
    .stChatMessage { border: 1.5px solid #800000 !important; border-radius: 12px; background-color: #ffffff !important; }
    .stChatInputContainer { border: 1.5px solid #800000 !important; border-radius: 10px; }
    [data-testid="stSidebar"] { display: none; }
    </style>
    """, unsafe_allow_html=True)

# 3. عرض الهوية (الجهة اليمنى)
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

# 4. جلب المفاتيح من الخزنة
API_KEY = st.secrets.get("OPENROUTER_API_KEY", "").strip().replace('"', '')
PAYPAL_ID = st.secrets.get("PAYPAL_CLIENT_ID", "").strip().replace('"', '')

# 5. إدارة الحالة (Session State)
if "messages" not in st.session_state: st.session_state.messages = []
if "msg_count" not in st.session_state: st.session_state.msg_count = 0
if "is_pro_paid" not in st.session_state: st.session_state.is_pro_paid = False
if "pro_trial_used" not in st.session_state: st.session_state.pro_trial_used = False

for message in st.session_state.messages:
    with st.chat_message(message["role"]): st.markdown(message["content"])

# 6. منطق التمييز بين الطلب العادي والاحترافي
professional_keywords = ["جدول", "إكسل", "excel", "حلل", "صورة", "صمم", "دراسة جدوى", "تقرير مالي"]

def is_pro_request(text):
    return any(word in text.lower() for word in professional_keywords)

# 7. محرك التشغيل
if prompt := st.chat_input("تحدث مع شاهين العالمي..."):
    # تجاوز الأدمن
    if prompt == "SHAHEEN_ADMIN_2026":
        st.session_state.is_pro_paid = True
        st.success("أهلاً بك يا سيد محمد.. تم تفعيل وضع الإدارة المطلق.")
    else:
        is_pro = is_pro_request(prompt)
        
        # التحقق من شروط الدفع للخدمات الاحترافية (15 ريال)
        if is_pro and st.session_state.pro_trial_used and not st.session_state.is_pro_paid:
            st.warning("⚠️ هذه الخدمة ضمن 'الباقة الاحترافية'. لقد استنفدت محاولتك المجانية.")
            st.markdown(f'<a href="https://paypal.me/MOHDSHAHEEN/15" target="_blank"><button style="width:100%; height:50px; background-color:#800000; color:white; border-radius:10px; cursor:pointer; font-weight:bold; border:none;">تفعيل الباقة الاحترافية (15 ريال قطري)</button></a>', unsafe_allow_html=True)
        
        # التحقق من شروط المحادثات العادية (10 رسائل مجانية)
        elif not is_pro and st.session_state.msg_count >= 10 and not st.session_state.is_pro_paid:
            st.warning("⚠️ انتهت المحاولات المجانية للدردشة العادية.")
            st.markdown(f'<a href="https://paypal.me/MOHDSHAHEEN/12" target="_blank"><button style="width:100%; height:50px; background-color:#000000; color:white; border-radius:10px; cursor:pointer; font-weight:bold; border:none;">استمرار الدردشة العادية (12 ريال قطري)</button></a>', unsafe_allow_html=True)
        
        else:
            # تنفيذ الطلب
            if is_pro and not st.session_state.pro_trial_used:
                st.session_state.pro_trial_used = True
                st.info("🎁 شاهين يقدم لك أول خدمة احترافية مجاناً.. جاري المعالجة...")
            
            st.session_state.messages.append({"role": "user", "content": prompt})
            if not is_pro: st.session_state.msg_count += 1
            
            with st.chat_message("user"): st.markdown(prompt)
            
            with st.chat_message("assistant"):
                headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
                payload = {"model": "google/gemini-2.0-flash-001", "messages": [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]}
                try:
                    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload, timeout=40)
                    res = response.json()['choices'][0]['message']['content']
                    st.markdown(res)
                    st.session_state.messages.append({"role": "assistant", "content": res})
                except:
                    st.error("عطل مؤقت في الاتصال، يرجى المحاولة.")
