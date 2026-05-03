import streamlit as st
import base64
import time

# 1. إعدادات المنصة الاحترافية (Dark Mode & Responsive)
st.set_page_config(
    page_title="ShaheenChat | Global AI Platform",
    page_icon="🦅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تقنية الحقن البرمجي لضمان ثبات شعار (رأس الصقر) في كل مكان
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception:
        return None

# تحميل الشعار الرسمي (تأكد أن الملف باسم logo.jpg في مستودع GitHub الخاص بك)
img_data = get_base64_image("logo.jpg")
logo_html = f"data:image/png;base64,{img_data}" if img_data else None

# --- إدارة الذاكرة والردود (لمنع التكرار) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 2. الشريط الجانبي (Sidebar) بتصميم SaaS ---
with st.sidebar:
    if logo_html:
        st.image(logo_html, width=150)
    st.title("شاهين شات")
    st.markdown("---")
    
    # قائمة التنقل
    menu = st.radio("القائمة:", ["🏠 الرئيسية", "💬 المحادثات", "🤝 التوافق", "⚙️ الإعدادات", "📞 تواصل معنا"])
    
    if menu == "🤝 التوافق":
        st.info("🤝 **تطبيق توافق**\n\n(قريبًا)")

    st.markdown("---")
    # أيقونات التواصل المختصرة (رموز فقط)
    st.markdown("### 🌐 تواصل معنا")
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.markdown("[![WA](https://img.shields.io/badge/-WA-25D366?style=flat&logo=whatsapp&logoColor=white)](https://wa.me/yournumber)")
    with col2: st.markdown("[![TG](https://img.shields.io/badge/-TG-26A5E4?style=flat&logo=telegram&logoColor=white)](https://t.me/yourusername)")
    with col3: st.markdown("[![IG](https://img.shields.io/badge/-IG-E4405F?style=flat&logo=instagram&logoColor=white)](https://instagram.com/yourprofile)")
    with col4: st.markdown("[![Mail](https://img.shields.io/badge/-Mail-D14836?style=flat&logo=gmail&logoColor=white)](mailto:tawafuq.app2026@gmail.com)")

# --- 3. الواجهة الرئيسية والدردشة ---
if menu == "🏠 الرئيسية" or menu == "💬 المحادثات":
    st.markdown(f"<div style='text-align: center;'><img src='{logo_html}' width='100'></div>" if logo_html else "", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>كيف يمكنني مساعدتك اليوم؟</h1>", unsafe_allow_html=True)
    
    # عرض فقاعات المحادثة بتصميم حديث
    for message in st.session_state.messages:
        avatar_img = logo_html if message["role"] == "assistant" else None
        with st.chat_message(message["role"], avatar=avatar_img):
            st.markdown(message["content"])

    # صندوق الإدخال (صندوق المحادثة في المنتصف)
    if prompt := st.chat_input("اكتب رسالتك هنا..."):
        # إضافة رسالة المستخدم للذاكرة
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # تأثير الكتابة التدريجي للرد (Typing Effect)
        with st.chat_message("assistant", avatar=logo_html):
            message_placeholder = st.empty()
            full_response = ""
            
            # محاكاة رد ذكي متغير (Backend Ready)
            assistant_response = f"بصفتي شاهين شات، قمت بتحليل طلبك بخصوص '{prompt}'. هذا يتطلب استجابة تقنية متقدمة، كيف تود أن نبدأ؟"
            
            for chunk in assistant_response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
            
        # إضافة رد النظام للذاكرة
        st.session_state.messages.append({"role": "assistant", "content": full_response})

# --- 4. قسم التوافق (بطاقة أنيقة) ---
elif menu == "🤝 التوافق":
    st.markdown("---")
    st.subheader("🤝 التوافق")
    st.success("هذا القسم يتم تجهيزه ليكون منصة الربط الكبرى الخاصة بك.")
    st.markdown("### **قريبًا**")

# --- 5. تواصل معنا ---
elif menu == "📞 تواصل معنا":
    st.header("🌐 منصة شاهين العالمية")
    st.write("للاستفسارات التجارية أو التقنية، يرجى التواصل عبر البريد المعتمد:")
    st.code("tawafuq.app2026@gmail.com")

# --- 6. Footer (حقوق النشر والسياسات) ---
st.markdown("---")
col_f1, col_f2, col_f3 = st.columns(3)
with col_f1: st.caption("ShaheenChat.com © 2026")
with col_f2: st.caption("[سياسة الخصوصية](#) | [الشروط](#)")
with col_f3: st.caption("صنع بكل فخر لدعم الابتكار العالمي")
