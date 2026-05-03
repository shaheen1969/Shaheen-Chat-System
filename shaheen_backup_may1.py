import streamlit as st
import requests
import json
import os

# 1. إعدادات الهوية والواجهة العالمية
st.set_page_config(page_title="شاهين شات", page_icon="🦅", layout="wide")

# 2. التنسيق الاحترافي الجديد (الهوية على اليمين)
st.markdown("""
    <style>
    .main .block-container { padding-left: 20% !important; padding-right: 20% !important; max-width: 100%; }
    .header-container { display: flex; flex-direction: column; align-items: flex-end; width: 100%; margin-bottom: 30px; }
    .stTitle { color: #000000 !important; font-family: 'Segoe UI', sans-serif; font-size: 36px; font-weight: bold; margin: 0; text-align: right; }
    .social-btns-container { display: flex; flex-direction: row-reverse; gap: 10px; margin-top: 15px; }
    .social-btn { padding: 6px 12px; background-color: #ffffff; color: #000000 !important; border: 1.5px solid #800000; border-radius: 8px; text-decoration: none !important; font-size: 12px; font-weight: bold; }
    .stChatMessage { border: 3px solid #800000 !important; border-radius: 15px; background-color: #ffffff !important; color: #000000 !important; }
    .stChatInputContainer { border: 2.5px solid #800000 !important; border-radius: 12px; }
    [data-testid="stSidebar"] { display: none; }
    </style>
    """, unsafe_allow_html=True)

# 3. بناء الهوية البصرية (الجهة اليمنى)
st.markdown('<div class="header-container">', unsafe_allow_html=True)
# البحث عن شعارك الشخصي المرفق
logo_file = "شاهين.jpeg"
if not os.path.exists(logo_file):
    for file in os.listdir("."):
        if (file.startswith("لقطة") or file.startswith("شاهين")) and file.lower().endswith((".png", ".jpg", ".jpeg")):
            logo_file = file
            break

if os.path.exists(logo_file):
    st.image(logo_file, width=130)
else:
    st.markdown('<h2 style="color:#800000;">🦅</h2>', unsafe_allow_html=True)

st.markdown('<h1 class="stTitle">شاهين شات</h1>', unsafe_allow_html=True)

# أزرار التواصل الاجتماعي تحت العنوان مباشرة
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
try:
    API_KEY = st.secrets["OPENROUTER_API_KEY"].strip()
    PAYPAL_ID = st.secrets["PAYPAL_CLIENT_ID"].strip()
except Exception as e:
    st.error(f"⚠️ خطأ في الخزنة: يرجى إضافة المفاتيح المطلوبة. ({e})")
    st.stop()

# 5. إدارة المحادثة والربح
if "messages" not in st.session_state: st.session_state.messages = []
if "msg_count" not in st.session_state: st.session_state.msg_count = 0
if "is_paid" not in st.session_state: st.session_state.is_paid = False

for message in st.session_state.messages:
    with st.chat_message(message["role"]): st.markdown(message["content"])

# 6. منطق التشغيل والربح التلقائي
if st.session_state.msg_count < 5 or st.session_state.is_paid:
    if prompt := st.chat_input("تحدث مع شاهين العالمي..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.msg_count += 1
        with st.chat_message("user"): st.markdown(prompt)
        
        with st.chat_message("assistant"):
            headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
            payload = {"model": "google/gemini-2.0-flash-001", "messages": [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]}
            try:
                response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, data=json.dumps(payload), timeout=45)
                res = response.json()['choices'][0]['message']['content']
                st.markdown(res)
                st.session_state.messages.append({"role": "assistant", "content": res})
            except: st.error("عطل اتصال، يرجى المحاولة لاحقاً.")
else:
    st.warning("⚠️ انتهت المحاولات المجانية. استمر بـ 12 ريال قطري فقط.")
    paypal_html = f"""
    <div id="paypal-button-container"></div>
    <script src="https://www.paypal.com/sdk/js?client-id={PAYPAL_ID}&currency=USD"></script>
    <script>
        paypal.Buttons({{
            createOrder: function(data, actions) {{ return actions.order.create({{ purchase_units: [{{ amount: {{ value: '3.30' }} }}] }}); }},
            onApprove: function(data, actions) {{ 
                return actions.order.capture().then(function(details) {{ 
                    alert('تم الدفع بنجاح! شكراً لك.');
                    location.reload(); 
                }}); 
            }}
        }}).render('#paypal-button-container');
    </script>
    """
    st.components.v1.html(paypal_html, height=350)
