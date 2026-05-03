import streamlit as st

# 1. إعدادات الصفحة العالمية
st.set_page_config(page_title="ShaheenChat | Global AI Platform", layout="wide")

# 2. الهوية الرسمية (تأكد من وجود الملف logo.jpg في GitHub)
SHAHEEN_LOGO = "logo.jpg" 

# إدارة المحاولات المجانية
if 'usage_count' not in st.session_state:
    st.session_state.usage_count = 0

# --- 3. القائمة الجانبية (الشعار والروابط) ---
with st.sidebar:
    st.image(SHAHEEN_LOGO, width=200)
    st.title("شاهين شات")
    st.write("---")
    menu = st.radio("انتقل إلى:", ["الدردشة الذكية", "المدونة العالمية", "باقات الاشتراك", "تواصل معنا"])
    
    st.write("---")
    st.markdown("### 📢 مساحة إعلانية")
    st.info("مساحة مخصصة للشركات والابتكارات الرقمية.")
    st.write("للتواصل: tawafuq.app2026@gmail.com")

# --- 4. الدردشة الذكية ---
if menu == "الدردشة الذكية":
    col_logo, col_text = st.columns([1, 5])
    with col_logo:
        st.image(SHAHEEN_LOGO, width=80)
    with col_text:
        st.header("شاهين شات | ShaheenChat")
    
    st.success("🎯 **إعلان:** اكتشف الحلول الذكية التي ترسم مستقبل الأعمال عالمياً.")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        avatar_img = SHAHEEN_LOGO if message["role"] == "assistant" else None
        with st.chat_message(message["role"], avatar=avatar_img):
            st.markdown(message["content"])

    if prompt := st.chat_input("تحدث مع شاهين شات..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        if st.session_state.usage_count < 7:
            with st.chat_message("assistant", avatar=SHAHEEN_LOGO):
                response = f"مرحباً بك في شاهين شات. أنا محركك الذكي للإبداع والابتكار. كيف يمكنني مساعدتك؟"
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.session_state.usage_count += 1
        else:
            with st.chat_message("assistant", avatar=SHAHEEN_LOGO):
                st.error("⚠️ وصلت للحد الأقصى للمحاولات المجانية لهذا اليوم.")
                st.write("انتقل لصفحة 'باقات الاشتراك' للحصول على وصول غير محدود.")

# --- 5. باقات الاشتراك (محدثة بمحتوى كامل) ---
elif menu == "باقات الاشتراك":
    st.header("💎 اختر باقتك في شاهين شات")
    st.write("حلول مرنة تناسب احتياجاتك الفردية والمؤسسية.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### الباقة الأساسية
        **مجاناً**
        - 7 محاولات ذكية يومياً
        - وصول للمحرك الأساسي
        - دعم عبر البريد الإلكتروني
        """)
        st.button("الباقة الحالية", disabled=True, key="free")
        
    with col2:
        st.markdown("""
        ### الباقة الاحترافية
        **$9 / شهرياً**
        - محاولات غير محدودة
        - أولوية في المعالجة
        - توليد صور عالية الدقة
        """)
        st.button("اشترك الآن", key="pro")
        
    with col3:
        st.markdown("""
        ### باقة الأعمال
        **تواصل معنا**
        - تكامل مع أنظمة الشركات
        - تحليل بيانات ضخمة
        - خصوصية وتشفير متقدم
        """)
        st.button("طلب استشارة", key="biz")

# --- 6. تواصل معنا (أيقونات التواصل المحدثة) ---
elif menu == "تواصل معنا":
    st.header("🌐 ابقَ على تواصل")
    st.write("يسعدنا الرد على استفساراتكم بخصوص شاهين شات أو تطبيق توافق القادم.")
    
    st.markdown("📩 **البريد الإلكتروني:** [tawafuq.app2026@gmail.com](mailto:tawafuq.app2026@gmail.com)")
    
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.markdown("💼 **LinkedIn:** [ShaheenChat Official](#)")
        st.markdown("🐦 **Twitter (X):** [@ShaheenChat](#)")
    with col_t2:
        st.markdown("📸 **Instagram:** [@ShaheenChat](#)")
        st.markdown("💬 **WhatsApp:** [تواصل مباشر](#)")

# --- 7. المدونة العالمية ---
elif menu == "المدونة العالمية":
    st.header("📚 مدونة شاهين شات (Insights)")
    st.write("استكشف آخر توجهات الذكاء الاصطناعي والابتكار الرقمي.")
    st.info("سيتم إضافة المقالات الحصرية قريباً...")

# --- 8. التذييل ---
st.write("---")
st.caption("ShaheenChat.com © 2026 | المنصة العالمية للذكاء الاصطناعي والابتكار الرقمي")
