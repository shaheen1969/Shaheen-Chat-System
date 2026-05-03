import streamlit as st
import base64

# 1. إعدادات المنصة العالمية وإخفاء شريط الإدارة للزوار
st.set_page_config(
    page_title="ShaheenChat | Global AI Platform", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# تقنية الحقن البرمجي لضمان ثبات الشعار رقم 1
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception:
        return None

# تحميل الشعار الرسمي (تأكد أن الملف باسم logo.jpg في GitHub)
img_data = get_base64_image("logo.jpg")
logo_html = f"data:image/png;base64,{img_data}" if img_data else None

# إدارة عداد الاستخدام (7 محاولات مجانية)
if 'usage_count' not in st.session_state:
    st.session_state.usage_count = 0

# --- 2. القائمة الجانبية المكتملة بالأيقونات ---
with st.sidebar:
    if logo_html:
        st.image(logo_html, width=180)
    st.title("شاهين شات")
    st.write("---")
    
    menu = st.radio("القائمة الرئيسية:", 
                    ["🤖 الدردشة الذكية", 
                     "📝 المدونة العالمية (Blog)", 
                     "💎 باقات الاشتراك", 
                     "🤝 تطبيق توافق (قريباً)"])
    
    st.write("---")
    # قسم تواصل معنا بأيقونات احترافية
    st.markdown("### 🌐 تابعنا وتواصل معنا")
    st.markdown("[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/yournumber)")
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/yourprofile)")
    st.markdown("[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/yourprofile)")
    
    st.write("---")
    st.markdown("### 📢 مساحة إعلانية")
    st.write("للتواصل: tawafuq.app2026@gmail.com")

# --- 3. قسم الدردشة (الشعار الجديد هو أيقونة الرد) ---
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
                response = "أهلاً بك في شاهين شات. أنا محركك الذكي العالمي، كيف يمكنني مساعدتك؟"
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.session_state.usage_count += 1
        else:
            with st.chat_message("assistant", avatar=logo_html):
                st.error("⚠️ استنفدت المحاولات المجانية.")
                st.info("راجع 'باقات الاشتراك' للوصول غير المحدود.")

# --- 4. قسم تطبيق توافق (قريباً) ---
elif menu == "🤝 تطبيق توافق (قريباً)":
    st.header("🤝 تطبيق توافق")
    if logo_html:
        st.image(logo_html, width=120)
    st.markdown("### **قريباً جداً**")
    st.write("رؤيتنا القادمة لتعزيز النمو المؤسسي الذكي.")

# --- 5. المدونة والاشتراكات ---
elif menu == "📝 المدونة العالمية (Blog)":
    st.header("📚 مدونة شاهين شات (Insights)")
    st.button("تصفح المقالات")

elif menu == "💎 باقات الاشتراك":
    st.header("💎 باقات التميز")
    st.write("• باقة الأفراد: $9/شهرياً")
    st.write("• باقة الأعمال: تواصل معنا عبر البريد المعتمد")

# --- 6. التذييل ---
st.write("---")
st.caption("ShaheenChat.com © 2026 | بوابة الذكاء الاصطناعي العالمية")
