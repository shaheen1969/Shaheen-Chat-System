import streamlit as st
import requests
import json

# 1. إعدادات الهوية والواجهة الاحترافية
st.set_page_config(page_title="شاهين شات", page_icon="🦅", layout="wide")

# 2. التصميم (اللون البرغندي - الخمري المميز) وتوسيع المساحة
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    /* عنوان شاهين شات باللون الخمري والخط العريض */
    .stTitle { color: #800000; text-align: center; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 45px; font-weight: bold; padding-top: 20px; }
    /* تصميم فقاعات الدردشة ببرواز خمري بروجاني */
    .stChatMessage { border: 2px solid #800000; border-radius: 15px; padding: 10px; margin-bottom: 15px; }
    /* تصغير أزرار المشاركة في الجانب */
    .share-container { position: fixed; top: 100px; left: 10px; width: 60px; display: flex; flex-direction: column; gap: 10px; z-index: 100; }
    .share-btn { padding: 5px; background-color: #800000; color: white; border-radius: 5px; text-decoration: none; font-size: 10px; text-align: center; font-weight: bold; }
    /* إخفاء القائمة الجانبية الافتراضية لترك مساحة للشات */
    [data-testid="stSidebar"] { display: none; }
    </style>
    """, unsafe_allow_html=True)

# عرض أزرار المشاركة بشكل مصغر جداً على الجانب
st.markdown("""
    <div class="share-container">
        <a href="https://wa.me/?text=جرب شاهين شات العالمي" class="share-btn">واتساب</a>
        <a href="https://twitter.com/intent/tweet?text=جرب شاهين شات العالمي" class="share-btn">تويتر</a>
    </div>
    """, unsafe_allow_html=True)

# عرض العنوان فقط
st.markdown('<h1 class="stTitle">🦅 شاهين شات</h1>', unsafe_allow_html=True)

# 3. نظام الأمان المطور (تنظيف المفتاح من أي أخطاء نسخ)
try:
    # جلب المفتاح وحذف أي علامات تنصيص أو مسافات قد تسبب خطأ 401
    API_KEY = st.secrets["OPENROUTER_API_KEY"].strip().replace('"', '').replace("'", "")
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
            # بروتوكول اتصال معزز لتجنب أخطاء المزود العالمي
            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://github.com/Tawafuq2026/Shaheen-Chat-System",
                "X-Title": "Shaheen Chat Professional"
            }
            payload = {
                "model": "google/gemini-2.0-flash-001",
                "messages": [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            }
            try:
                response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, data=json.dumps(payload), timeout=45)
                if response.status_code == 200:
                    res_content = response.json()['choices'][0]['message']['content']
                    st.markdown(res_content)
                    st.session_state.messages.append({"role": "assistant", "content": res_content})
                else:
                    # تشخيص دقيق للمشكلة (قد يكون الحساب يحتاج تأكيد بريد أو رصيد إضافي)
                    st.error(f"تنبيه تقني ({response.status_code}): المزود العالمي يرفض الطلب. يرجى التأكد من تفعيل الرصيد (الرصيد الحالي: 20.98$).")
            except Exception as e:
                st.error(f"عطل في الاتصال العالمي: {e}")
else:
    # واجهة الدفع (ROI)
    st.warning("⚠️ انتهت المحاولات المجانية.")
    st.info("للاستمرار في استخدام شاهين شات العالمي، اشترك بـ 12 ريالاً قطرياً فقط.")
    st.markdown(f'<a href="https://paypal.me/MOHDSHAHEEN" target="_blank"><button style="width:100%; height:50px; background-color:#800000; color:white; border-radius:10px; cursor:pointer; font-weight:bold;">تفعيل الاشتراك (12 ريال)</button></a>', unsafe_allow_html=True)
