import streamlit as st
import requests
import json

# 1. إعدادات الهوية والواجهة الاحترافية
st.set_page_config(page_title="شاهين شات", page_icon="🦅", layout="wide")

# 2. التصميم (اللون البرغندي - الخمري المميز) وتوسيع المساحة
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stTitle { color: #800000; text-align: center; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 45px; font-weight: bold; padding-top: 20px; }
    
    /* تصميم فقاعات الدردشة ببرواز خمري بروجاني */
    .stChatMessage { border: 2px solid #800000; border-radius: 15px; padding: 10px; margin-bottom: 15px; }
    
    /* تصغير أزرار المشاركة: أحرف بيضاء وبرواز خمري */
    .share-container { position: fixed; top: 120px; left: 10px; width: 70px; display: flex; flex-direction: column; gap: 8px; z-index: 100; }
    .share-btn { 
        padding: 6px; 
        background-color: #800000; 
        color: white !important; 
        border: 1px solid #800000;
        border-radius: 8px; 
        text-decoration: none; 
        font-size: 11px; 
        text-align: center; 
        font-weight: bold;
    }
    
    /* إخفاء القائمة الجانبية الافتراضية لترك مساحة للشات */
    [data-testid="stSidebar"] { display: none; }
    </style>
    """, unsafe_allow_html=True)

# عرض أزرار المشاركة (أحرف بيضاء وخلفية خمرية)
st.markdown("""
    <div class="share-container">
        <a href="https://wa.me/?text=جرب شاهين شات العالمي" target="_blank" class="share-btn">واتساب</a>
        <a href="https://twitter.com/intent/tweet?text=جرب شاهين شات العالمي" target="_blank" class="share-btn">تويتر</a>
    </div>
    """, unsafe_allow_html=True)

# عرض العنوان (شاهين شات فقط)
st.markdown('<h1 class="stTitle">🦅 شاهين شات</h1>', unsafe_allow_html=True)

# 3. نظام الأمان المطور (الإصلاح الجذري للخطأ 401)
try:
    # جلب المفتاح وتنظيفه من أي شوائب برمجية قد تسبب الرفض
    raw_key = st.secrets["OPENROUTER_API_KEY"]
    # حذف المسافات وعلامات التنصيص وأي رموز سطر جديد
    API_KEY = "".join(raw_key.split()).replace('"', '').replace("'", "").strip()
except Exception:
    st.error("تنبيه أمان: يرجى التحقق من المفتاح في الخزنة السرية.")
    st.stop()

# 4. الذاكرة الذكية للمستخدمين
if "messages" not in st.session_state:
    st.session_state.messages = []
if "msg_count" not in st.session_state:
    st.session_state.msg_count = 0

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. العمليات العالمية ونظام الربح (12 ريال قطري)
if st.session_state.msg_count < 5:
    if prompt := st.chat_input("تحدث مع شاهين العالمي..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.msg_count += 1
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            # بروتوكول اتصال مباشر لضمان قبول المفتاح
            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "google/gemini-2.0-flash-001",
                "messages": [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            }
            try:
                # استخدام رابط الاتصال المباشر مع زيادة وقت الانتظار
                response = requests.post(
                    "https://openrouter.ai/api/v1/chat/completions", 
                    headers=headers, 
                    data=json.dumps(payload), 
                    timeout=30
                )
                
                if response.status_code == 200:
                    res_content = response.json()['choices'][0]['message']['content']
                    st.markdown(res_content)
                    st.session_state.messages.append({"role": "assistant", "content": res_content})
                else:
                    # رسالة تشخيصية مطورة
                    st.error(f"تنبيه تقني ({response.status_code}): المزود يرفض المفتاح. تأكد من تفعيل بريدك في OpenRouter.")
            except Exception as e:
                st.error(f"عطل في الاتصال العالمي: {e}")
else:
    # واجهة الدفع (12 ريال قطري)
    st.warning("⚠️ انتهت المحاولات المجانية.")
    st.info("للاستمرار، اشترك بـ 12 ريالاً قطرياً فقط.")
    st.markdown(f'<a href="https://paypal.me/MOHDSHAHEEN" target="_blank"><button style="width:100%; height:50px; background-color:#800000; color:white; border-radius:10px; cursor:pointer; font-weight:bold;">تفعيل الاشتراك (12 ريال)</button></a>', unsafe_allow_html=True)
