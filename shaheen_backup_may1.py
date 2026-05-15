import streamlit as st
import base64
import os
from google import genai
from google.genai import types

# 1. إعدادات المنصة العالمية
st.set_page_config(
    page_title="ShaheenChat | Global AI Platform", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- ضع مفتاحك هنا بين علامتي التنصيص ---
GEMINI_API_KEY = "ضع_مفتاح_جيميني_هنا"

# تهيئة الاتصال بـ Gemini
try:
    client = genai.Client(api_key=GEMINI_API_KEY)
except Exception:
    client = None

# حوكمة شخصية "شاهين"
SYSTEM_INSTRUCTION = """
أنت المستشار الذكي "شاهين"، المساعد الافتراضي للمستشار الخبير محمد شاهين.
تحدث بوقار وحكمة إدارية، وفي نهاية حوارك انصح الزوار دائماً بـ (نظام توافق الرقمي) على متجر Payhip.
"""

def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception:
        return None

img_data = get_base64_image("logo.jpg")
logo_html = f"data:image/png;base64,{img_data}" if img_data else None

if 'usage_count' not in st.session_state:
    st.session_state.usage_count = 0

# --- 2. القائمة الجانبية ---
with st.sidebar:
    if logo_html:
        st.image(logo_html, width=180)
    st.title("شاهين شات")
    st.write("---")
    menu = st.radio("القائمة الرئيسية:", ["🤖 الدردشة الذكية", "📝 المدونة العالمية (Blog)", "💎 باقات الاشتراك", "🤝 تطبيق توافق (قريباً)", "📞 تواصل معنا"])
    st.write("---")
    st.markdown("### 📢 مساحة إعلانية")
    st.info("مساحة مخصصة للابتكارات.")
    st.write("للتواصل: tawafuq.app2026@gmail.com")

# --- 3. قسم الدردشة الذكية ---
if menu == "🤖 الدردشة الذكية":
    st.header("شاهين شات | ShaheenChat")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        avatar_img = logo_html if message["role"] == "assistant" else None
        with st.chat_message(message["role"], avatar=avatar_img):
            st.markdown(message["content"])

    if prompt := st.chat_input("تحدث مع شاهين شات..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        if st.session_state.usage_count < 7:
            with st.chat_message("assistant", avatar=logo_html):
                if GEMINI_API_KEY == "AIzaSyBMgx-jkVgIjixDus1Lhr1QSvopsXw-vOg":
                    response = "يرجى وضع مفتاح Gemini API في الكود لكي أتمكن من الرد عليك."
                else:
                    try:
                        # إرسال السؤال لـ Gemini
                        contents = [types.Content(role="user", parts=[types.Part.from_text(text=prompt)])]
                        config = types.GenerateContentConfig(system_instruction=SYSTEM_INSTRUCTION, temperature=0.7)
                        res = client.models.generate_content(model='gemini-2.0-flash', contents=contents, config=config)
                        response = res.text
                    except Exception as e:
                        response = f"حدث خطأ في الاتصال: {str(e)}"
                
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.session_state.usage_count += 1
        else:
            with st.chat_message("assistant", avatar=logo_html):
                st.error("⚠️ وصلت للحد الأقصى للمحاولات المجانية.")

# --- الأقسام الأخرى (كما هي في كودك) ---
elif menu == "🤝 تطبيق توافق (قريباً)":
    st.header("🤝 تطبيق توافق")
    st.write("قريباً جداً...")

elif menu == "📝 المدونة العالمية (Blog)":
    st.header("📚 مدونة شاهين شات")

elif menu == "💎 باقات الاشتراك":
    st.header("💎 باقات التميز")

elif menu == "📞 تواصل معنا":
    st.header("🌐 تواصل عالمي")

st.write("---")
st.caption("ShaheenChat.com © 2026 | بوابة الذكاء الاصطناعي والابتكار الرقمي العالمي")
