import streamlit as st
import base64

# 1. إعدادات الصفحة العالمية الاحترافية
st.set_page_config(page_title="ShaheenChat | Global AI", layout="wide")

# دالة لتحميل الصورة وضمان ظهورها كأيقونة وشعار (استبدل logo.jpg باسم ملفك الصحيح)
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return ""

# تحميل الشعار الرسمي (رقم 1)
img_base64 = get_base64_image("logo.jpg")
logo_html = f"data:image/png;base64,{img_base64}"

# إدارة عدد المحاولات (7 محاولات مجانية لرفع الرضا)
if 'usage_count' not in st.session_state:
    st.session_state.usage_count = 0

# --- 2. القائمة الجانبية (الشعار والأقسام الجديدة) ---
with st.sidebar:
    if img_base64:
        st.image(f"data:image/png;base64,{img_base64}", width=180)
    st.title("شاهين شات")
    st.write("---")
    
    # القائمة الرئيسية المحدثة بأيقونات
    menu = st.radio("انتقل إلى:", 
                    ["🤖 الدردشة الذكية", 
                     "📝 المدونة (Insights)", 
                     "💎 باقات الاشتراك", 
                     "🤝 تطبيق توافق (قريباً)", 
                     "📞 تواصل معنا"])
    
    st.write("---")
    # مساحة إعلانية احترافية
    st.markdown("### 📢 مساحة إعلانية")
    st.info("مساحة مخصصة للابتكارات والشركات العالمية.")
    st.write("للتواصل: tawafuq.app2026@gmail.com")

# --- 3. قسم الدردشة الذكية (بأيقونة الشعار الرسمي) ---
if menu == "🤖 الدردشة الذكية":
    st.header("شاهين شات | ShaheenChat")
    st.success("🎯 **إعلان:** حلول الذكاء الاصطناعي التي تبني مستقبل الأعمال عالمياً.")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # عرض المحادثة (أيقونة المساعد هي نفس شعارك الرسمي)
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar=logo_html if message["role"] == "assistant" else None):
            st.markdown(message["content"])

    if prompt := st.chat_input("تحدث مع شاهين شات..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        if st.session_state.usage_count < 7:
            with st.chat_message("assistant", avatar=logo_html):
                response = f"مرحباً بك في شاهين شات. بصفتي محركك الذكي، يسعدني دعم رؤيتك العالمية. كيف يمكنني مساعدتك؟"
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.session_state.usage_count += 1
        else:
            with st.chat_message("assistant", avatar=logo_html):
                st.error("⚠️ وصلت للحد الأقصى للمحاولات المجانية.")
                st.info("يرجى الانتقال لصفحة باقات الاشتراك للوصول غير المحدود.")

# --- 4. المدونة والاشتراكات وتوافق ---
elif menu == "📝 المدونة (Insights)":
    st.header("📚 رؤى عالمية")
    st.write("مقالات حصرية حول مستقبل التكنولوجيا والإدارة الرقمية.")
    st.button("استكشف المقالات")

elif menu == "💎 باقات الاشتراك":
    st.header("💎 باقات التميز")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("الاحترافية")
        st.write("- $9 / شهرياً")
        st.write("- محاولات غير محدودة")
        st.button("اشترك الآن")
    with c2:
        st.subheader("الأعمال")
        st.write("- تواصل معنا للتسعير")
        st.write("- خصوصية بيانات فائقة")
        st.button("طلب عرض سعر")

elif menu == "🤝 تطبيق توافق (قريباً)":
    st.header("🤝 تطبيق توافق")
    st.info("مشروعنا القادم لتعزيز الترابط والنمو الذكي.. قريباً جداً.")
    st.image(logo_html, width=100) # أيقونة رمزية حالياً

elif menu == "📞 تواصل معنا":
    st.header("🌐 تواصل عالمي")
    st.write("📧 البريد الإلكتروني: tawafuq.app2026@gmail.com")
    st.write("🔗 LinkedIn | Twitter | Instagram")

# --- 5. التذييل العالمي ---
st.write("---")
st.caption("ShaheenChat.com © 2026 | المنصة العالمية للذكاء الاصطناعي والابتكار")
