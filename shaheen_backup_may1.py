import streamlit as st
import base64

# 1. الإعدادات التقنية العالمية وتثبيت الهوية البصرية
st.set_page_config(page_title="ShaheenChat | Global AI", layout="wide", initial_sidebar_state="expanded")

# تقنية Base64 لضمان ثبات الشعار ومنع اختفائه أو تبدله
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

# تحميل شعارك الرسمي (تأكد من وجود ملف باسم logo.jpg في مستودع GitHub الخاص بك)
img_data = get_base64_image("logo.jpg")
logo_html = f"data:image/png;base64,{img_data}" if img_data else None

# عداد الاستخدام (7 محاولات مجانية لزيادة ولاء المستخدمين)
if 'usage_count' not in st.session_state:
    st.session_state.usage_count = 0

# --- 2. هندسة الواجهة الجانبية (الأقسام الاحترافية) ---
with st.sidebar:
    if logo_html:
        st.image(logo_html, width=180) # الشعار الجديد في القمة
    st.title("شاهين شات")
    st.write("---")
    
    # القائمة المحدثة بالقسم الجديد "توافق"
    menu = st.radio("انتقل إلى:", 
                    ["🤖 الدردشة الذكية", 
                     "📝 المدونة العالمية (Blog)", 
                     "💎 باقات الاشتراك", 
                     "🤝 تطبيق توافق", 
                     "📞 تواصل معنا"])
    
    st.write("---")
    # مساحة إعلانية احترافية ثابتة
    st.markdown("### 📢 مساحة إعلانية")
    st.info("مساحة مخصصة للابتكارات والشركات التقنية العالمية.")
    st.write("للتواصل: tawafuq.app2026@gmail.com") # البريد الإلكتروني المعتمد

# --- 3. الدردشة الذكية (استبدال الروبوت الأصفر بشعارك) ---
if menu == "🤖 الدردشة الذكية":
    st.header("شاهين شات | ShaheenChat")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # استخدام شعارك كأيقونة (Avatar) للردود بدلاً من الروبوت الأصفر
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar=logo_html if message["role"] == "assistant" else None):
            st.markdown(message["content"])

    if prompt := st.chat_input("كيف يمكن لـ شاهين شات مساعدتك اليوم؟"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        if st.session_state.usage_count < 7:
            with st.chat_message("assistant", avatar=logo_html):
                response = f"أهلاً بك في شاهين شات. بصفتي محركك الذكي، يسعدني دعم رؤيتك المبدعة عالمياً. بخصوص سؤالك: {prompt}"
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.session_state.usage_count += 1
        else:
            with st.chat_message("assistant", avatar=logo_html):
                st.error("⚠️ استنفدت المحاولات المجانية لهذا اليوم.")
                st.info("للوصول غير المحدود، يرجى مراجعة 'باقات الاشتراك'.")

# --- 4. قسم تطبيق توافق (الجديد) ---
elif menu == "🤝 تطبيق توافق":
    st.header("🤝 تطبيق توافق")
    if logo_html:
        st.image(logo_html, width=120)
    st.markdown("### **قريباً**") # إضافة كلمة قريباً بوضوح
    st.write("مشروعنا القادم لتعزيز الترابط والذكاء المؤسسي الموحد.")

# --- 5. المدونة والاشتراكات (تنظيم احترافي) ---
elif menu == "📝 المدونة (Blog)":
    st.header("📚 مدونة شاهين شات العالمية")
    st.write("مقالات حصرية في التكنولوجيا والإدارة الرقمية.")
    st.button("تصفح المقالات")

elif menu == "💎 باقات الاشتراك":
    st.header("💎 باقات التميز")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("باقة الأفراد")
        st.write("• وصول غير محدود • دعم فني")
        st.button("اشترك الآن - $9")
    with c2:
        st.subheader("باقة الشركات")
        st.write("• حلول مخصصة • تشفير متقدم")
        st.button("طلب تسعير")

elif menu == "📞 تواصل معنا":
    st.header("🌐 تواصل عالمي")
    st.markdown(f"📩 **البريد الإلكتروني:** [tawafuq.app2026@gmail.com](mailto:tawafuq.app2026@gmail.com)")

# --- 6. التذييل العالمي ---
st.write("---")
st.caption("ShaheenChat.com © 2026 | بوابة الذكاء الاصطناعي والابتكار الرقمي العالمي")
