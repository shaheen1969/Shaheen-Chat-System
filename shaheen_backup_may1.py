import streamlit as st
import base64

# 1. إعدادات المنصة العالمية المتقدمة
st.set_page_config(
    page_title="ShaheenChat | Global AI Platform", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# تقنية الحقن البرمجي لضمان ثبات الشعار الجديد (logo.jpg) في كل مكان
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception:
        return None

# تحميل الشعار الرسمي (تأكد أن الملف باسم logo.jpg في GitHub)
img_data = get_base64_image("logo.jpg")
logo_html = f"data:image/png;base64,{img_data}" if img_data else None

# إدارة الجلسة والردود المتغيرة
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'usage_count' not in st.session_state:
    st.session_state.usage_count = 0

# --- 2. القائمة الجانبية الاحترافية ---
with st.sidebar:
    if logo_html:
        st.image(logo_html, width=150)
    st.title("شاهين شات")
    st.write("---")
    
    menu = st.radio("القائمة الرئيسية:", 
                    ["🤖 الدردشة الذكية", 
                     "📝 المدونة العالمية (Blog)", 
                     "💎 باقات الاشتراك", 
                     "🤝 تطبيق توافق (قريباً)"])
    
    st.write("---")
    # أيقونات التواصل الاجتماعي المختصرة (رموز فقط)
    st.markdown("### 🌐 تواصل معنا")
    col_social1, col_social2, col_social3 = st.columns(3)
    with col_social1:
        st.markdown("[![WA](https://img.shields.io/badge/-WA-25D366?style=flat&logo=whatsapp&logoColor=white)](https://wa.me/yournumber)")
    with col_social2:
        st.markdown("[![LI](https://img.shields.io/badge/-LI-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/yourprofile)")
    with col_social3:
        st.markdown("[![X](https://img.shields.io/badge/-X-000000?style=flat&logo=x&logoColor=white)](https://twitter.com/yourprofile)")
    
    st.write("---")
    st.markdown("### 📢 مساحة إعلانية")
    st.caption("للتواصل الشراكات:")
    st.write("tawafuq.app2026@gmail.com")

# --- 3. قسم الدردشة (الردود المتغيرة وأيقونة الشعار) ---
if menu == "🤖 الدردشة الذكية":
    st.header("شاهين شات | ShaheenChat")
    
    # عرض تاريخ المحادثة
    for message in st.session_state.messages:
        avatar_img = logo_html if message["role"] == "assistant" else None
        with st.chat_message(message["role"], avatar=avatar_img):
            st.markdown(message["content"])

    # إدخال المستخدم
    if prompt := st.chat_input("تحدث مع شاهين شات..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # توليد رد متغير بناءً على مدخلات المستخدم
        if st.session_state.usage_count < 7:
            with st.chat_message("assistant", avatar=logo_html):
                # رد ذكي متغير بدلاً من الرد الثابت
                full_response = f"أهلاً بك في شاهين شات. لقد استلمت رسالتك بخصوص '{prompt}'. كيف يمكنني مساعدتك في هذا الأمر بشكل أعمق؟"
                st.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                st.session_state.usage_count += 1
        else:
            with st.chat_message("assistant", avatar=logo_html):
                st.error("⚠️ استنفدت المحاولات المجانية.")
                st.info("راجع 'باقات الاشتراك' للوصول غير المحدود.")

# --- 4. تطبيق توافق (قريباً) ---
elif menu == "🤝 تطبيق توافق (قريباً)":
    st.header("🤝 تطبيق توافق")
    st.markdown("### **قريباً جداً**")
    if logo_html:
        st.image(logo_html, width=120)
    st.write("مشروعنا القادم لتعزيز النمو المؤسسي الذكي.")

# الأقسام الأخرى (المدونة والاشتراكات)
elif menu == "📝 المدونة العالمية (Blog)":
    st.header("📚 مدونة شاهين شات (Insights)")
    st.write("مقالات حصرية في التكنولوجيا العالمية.")

elif menu == "💎 باقات الاشتراك":
    st.header("💎 باقات التميز")
    st.write("باقة الأفراد: $9/شهرياً | باقة الأعمال: تواصل معنا.")

# --- 5. التذييل ---
st.write("---")
st.caption("ShaheenChat.com © 2026 | بوابة الذكاء الاصطناعي العالمية")
