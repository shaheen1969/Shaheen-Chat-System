import streamlit as st
import base64

# 1. إعدادات الصفحة العالمية - إخفاء القوائم غير الضرورية للزوار
st.set_page_config(page_title="ShaheenChat | Global AI Platform", layout="wide", initial_sidebar_state="expanded")

# دالة ذكية لتحويل الشعار إلى كود برمجي لضمان ثباته كأيقونة محادثة
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

# تحميل الشعار الرسمي (تأكد أن الملف اسمه logo.jpg في GitHub)
img_data = get_base64_image("logo.jpg")
logo_html = f"data:image/png;base64,{img_data}" if img_data else None

# إدارة المحاولات (7 محاولات مجانية)
if 'usage_count' not in st.session_state:
    st.session_state.usage_count = 0

# --- 2. القائمة الجانبية الاحترافية ---
with st.sidebar:
    if logo_html:
        st.image(logo_html, width=180)
    st.title("شاهين شات")
    st.write("---")
    
    menu = st.radio("القائمة الرئيسية:", 
                    ["🤖 الدردشة الذكية", "📚 المدونة (Blog)", "💎 باقات الاشتراك", "🤝 تطبيق توافق", "📞 تواصل معنا"])
    
    st.write("---")
    # مساحة إعلانية عالمية
    st.markdown("### 📢 مساحة إعلانية")
    st.info("مساحة مخصصة للابتكارات والشركات التقنية الكبرى.")
    st.write("للتواصل: tawafuq.app2026@gmail.com")

# --- 3. قسم الدردشة الذكية (بأيقونة الشعار الرسمي) ---
if menu == "🤖 الدردشة الذكية":
    st.header("شاهين شات | ShaheenChat")
    
    # عرض المحادثة باستخدام شعارك كأيقونة (Avatar) للردود
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar=logo_html if message["role"] == "assistant" else None):
            st.markdown(message["content"])

    if prompt := st.chat_input("كيف يمكن لـ شاهين شات مساعدتك اليوم؟"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        if st.session_state.usage_count < 7:
            with st.chat_message("assistant", avatar=logo_html):
                response = f"أهلاً بك في شاهين شات. بصفتي محركك الذكي العالمي، يسعدني دعم رؤيتك المبدعة. بخصوص سؤالك: {prompt}"
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.session_state.usage_count += 1
        else:
            with st.chat_message("assistant", avatar=logo_html):
                st.error("⚠️ وصلت للحد الأقصى للمحاولات المجانية لهذا اليوم.")
                st.info("يرجى مراجعة 'باقات الاشتراك' للحصول على وصول غير محدود.")

# --- 4. الأقسام الجديدة المكتملة ---
elif menu == "📚 المدونة (Blog)":
    st.header("📚 مدونة شاهين شات العالمية")
    st.write("استكشف أحدث المقالات التقنية والإدارية التي ترسم معالم المستقبل الرقمي.")
    st.markdown("- **مستقبل الذكاء الاصطناعي في الأعمال.**")
    st.markdown("- **إستراتيجيات الابتكار الرقمي العابر للحدود.**")

elif menu == "💎 باقات الاشتراك":
    st.header("💎 باقات التميز العالمي")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("باقة الأفراد")
        st.write("• محاولات غير محدودة • دعم فني 24/7 • توليد صور عالية الدقة")
        st.button("اشترك بـ $9/شهرياً")
    with c2:
        st.subheader("باقة الشركات")
        st.write("• ربط برمجيات (API) • تحليل بيانات ضخمة • تشفير متقدم")
        st.button("تواصل للتسعير الخاص")

elif menu == "🤝 تطبيق توافق":
    st.header("🤝 تطبيق توافق")
    st.markdown("### **قريباً**")
    st.write("مشروعنا القادم لتعزيز الترابط والذكاء المؤسسي الموحد.")
    if logo_html:
        st.image(logo_html, width=120)

elif menu == "📞 تواصل معنا":
    st.header("🌐 ابقَ على تواصل")
    st.write("للملاحظات أو طلبات الإعلان العالمية:")
    st.markdown("📩 البريد الإلكتروني: [tawafuq.app2026@gmail.com](mailto:tawafuq.app2026@gmail.com)")
    st.write("LinkedIn | Twitter | Instagram")

# --- 5. التذييل العالمي ---
st.write("---")
st.caption("ShaheenChat.com © 2026 | بوابة الذكاء الاصطناعي والابتكار الرقمي العالمي")
