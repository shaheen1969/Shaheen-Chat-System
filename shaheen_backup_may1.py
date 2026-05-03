import streamlit as st
import base64

# 1. إعدادات المنصة العالمية وإخفاء العناصر غير الضرورية
st.set_page_config(
    page_title="ShaheenChat | Global AI Platform", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# تقنية الحقن البرمجي لضمان ثبات الشعار الجديد ومنع ظهور الأيقونات الافتراضية
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception:
        return None

# تحميل الشعار الرسمي (يجب أن يكون الملف باسم logo.jpg في GitHub)
img_data = get_base64_image("logo.jpg")
logo_html = f"data:image/png;base64,{img_data}" if img_data else None

# إدارة عداد الاستخدام (7 محاولات مجانية)
if 'usage_count' not in st.session_state:
    st.session_state.usage_count = 0

# --- 2. هندسة القائمة الجانبية (الأقسام الاحترافية) ---
with st.sidebar:
    if logo_html:
        st.image(logo_html, width=180)
    st.title("شاهين شات")
    st.write("---")
    
    # القائمة المحدثة بالقسم الجديد "تطبيق توافق"
    menu = st.radio("انتقل إلى:", 
                    ["🤖 الدردشة الذكية", 
                     "📝 المدونة العالمية (Blog)", 
                     "💎 باقات الاشتراك", 
                     "🤝 تطبيق توافق (قريباً)", 
                     "📞 تواصل معنا"])
    
    st.write("---")
    # مساحة إعلانية احترافية ثابتة
    st.markdown("### 📢 مساحة إعلانية")
    st.info("مساحة مخصصة للابتكارات والشركات التقنية العالمية.")
    st.write("للتواصل: tawafuq.app2026@gmail.com")

# --- 3. قسم الدردشة (استبدال الروبوت الأصفر بشعارك الجديد) ---
if menu == "🤖 الدردشة الذكية":
    st.header("شاهين شات | ShaheenChat")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # عرض المحادثة (أيقونة المساعد هي شعارك الرسمي حصراً)
    for message in st.session_state.messages:
        avatar_img = logo_html if message["role"] == "assistant" else None
        with st.chat_message(message["role"], avatar=avatar_img):
            st.markdown(message["content"])

    if prompt := st.chat_input("كيف يمكن لـ شاهين شات مساعدتك اليوم؟"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        if st.session_state.usage_count < 7:
            with st.chat_message("assistant", avatar=logo_html):
                response = f"أهلاً بك في شاهين شات. أنا محركك الذكي للإبداع والابتكار العالمي. كيف يمكنني مساعدتك؟"
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.session_state.usage_count += 1
        else:
            with st.chat_message("assistant", avatar=logo_html):
                st.error("⚠️ استنفدت المحاولات المجانية لهذا اليوم.")
                st.info("يرجى مراجعة 'باقات الاشتراك' للوصول غير المحدود.")

# --- 4. قسم تطبيق توافق (قريباً) ---
elif menu == "🤝 تطبيق توافق (قريباً)":
    st.header("🤝 تطبيق توافق")
    if logo_html:
        st.image(logo_html, width=120)
    st.markdown("### **قريباً جداً**")
    st.write("رؤيتنا القادمة لتعزيز الترابط والنمو المؤسسي الذكي.")

# --- 5. تنظيم المساحات (المدونة والاشتراكات) ---
elif menu == "📝 المدونة العالمية (Blog)":
    st.header("📚 مدونة شاهين شات (Insights)")
    st.write("استكشف آفاق التكنولوجيا من منظور عالمي.")
    st.button("تصفح المقالات")

elif menu == "💎 باقات الاشتراك":
    st.header("💎 باقات التميز")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("باقة الأفراد")
        st.write("• وصول غير محدود • دعم فني • توليد صور")
        st.button("اشترك الآن - $9")
    with c2:
        st.subheader("باقة الأعمال")
        st.write("• حلول مخصصة • تشفير متقدم • API")
        st.button("طلب تسعير")

elif menu == "📞 تواصل معنا":
    st.header("🌐 تواصل عالمي")
    st.markdown(f"📩 **البريد الإلكتروني المعتمد:** [tawafuq.app2026@gmail.com](mailto:tawafuq.app2026@gmail.com)")

# --- 6. التذييل العالمي ---
st.write("---")
st.caption("ShaheenChat.com © 2026 | بوابة الذكاء الاصطناعي والابتكار الرقمي العالمي")
