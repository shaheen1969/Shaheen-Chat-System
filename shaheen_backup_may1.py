import streamlit as st
import requests
import json

# 1. إعدادات الهوية والواجهة الاحترافية
st.set_page_config(page_title="شاهين شات", page_icon="🦅", layout="wide")

# 2. التصميم البرغندي الملكي وتوسيع مساحة الشات
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stTitle { color: #800000; text-align: center; font-family: 'Segoe UI', Tahoma, sans-serif; font-size: 48px; font-weight: bold; padding-top: 10px; }
    .stChatMessage { border: 2px solid #800000; border-radius: 15px; padding: 12px; margin-bottom: 15px; }
    
    /* أيقونات التواصل: أحرف بيضاء وبرواز خمري */
    .share-container { position: fixed; top: 100px; left: 10px; width: 75px; display: flex; flex-direction: column; gap: 10px; z-index: 1000; }
    .share-btn { 
        padding: 8px; 
        background-color: #800000; 
        color: white !important; 
        border: 1px solid #800000;
        border-radius: 8px; 
        text-decoration: none; 
        font-size: 12px; 
        text-align: center; 
        font-weight: bold;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    }
    
    /* إخفاء القائمة الجانبية لتوفير مساحة أكبر */
    [data-testid="stSidebar"] { display: none; }
    </style>
    """, unsafe_allow_html=True)

# أيقونات المشاركة الاجتماعية
st.markdown("""
    <div class="share-container">
        <a href="https://wa.me/?text=جرب شاهين شات العالمي" target="_blank" class="share-btn">واتساب</a>
        <a href="https://twitter.com/intent/tweet?text=جرب شاهين شات العالمي" target="_blank" class="share-btn">تويتر</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="stTitle">🦅 شاهين شات</h1>', unsafe_allow_html=True)

# 3. بروتوكول الأمان وتطهير المفتاح (إصلاح الخطأ 401)
try:
    raw_key = st.secrets["OPENROUTER_API_KEY"]
    # حذف كل الفراغات وعلامات التنصيص والرموز المخفية تماماً
    API_KEY = "".join(raw_key.split()).replace('"', '').replace("'", "").strip()
except Exception:
    st.error("تنبيه أمان: المفتاح غير موجود في الخزنة السرية.")
    st.stop()

# 4. الذاكرة الذكية للمستخدمين
if "messages" not in st.session_state:
    st.session_state.messages = []
if "msg_count" not in st.session_state:
    st.session_state.msg_count = 0

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. التشغيل العالمي ونظام الربح (12 ريال قطري)
if st.session_state.msg_count < 5:
    if prompt := st.chat_input("تحدث مع شاهين العالمي..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.msg_count += 1
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
                "X-Title": "Shaheen Chat Professional"
            }
            payload = {
                "model": "google/gemini-2.0-flash-001",
                "messages": [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            }
            try:
                response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, data=json.dumps(payload), timeout=40)
                if response.status_code == 200:
                    res_content = response.json()['choices'][0]['message']['content']
                    st.markdown(res_content)
                    st.session_state.messages.append({"role": "assistant", "content": res_content})
                else:
                    st.error(f"تنبيه تقني ({response.status_code}): المزود يرفض المفتاح. تأكد من تفعيل بريدك في OpenRouter.")
            except Exception as e:
                st.error(f"عطل في الاتصال العالمي: {e}")
else:
    st.warning("⚠️ انتهت المحاولات المجانية.")
    st.markdown(f'<a href="https://paypal.me/MOHDSHAHEEN" target="_blank"><button style="width:100%; height:55px; background-color:#800000; color:white; border-radius:12px; cursor:pointer; font-size:18px; font-weight:bold; border:none;">تفعيل الاشتراك (12 ريال قطري)</button></a>', unsafe_allow_html=True)
