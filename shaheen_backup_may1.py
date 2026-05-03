import streamlit as st

# إعدادات الصفحة الاحترافية مع أيقونة الصقر
st.set_page_config(page_title="ShaheenChat | AI Business Insights", layout="wide")

# الرابط المباشر لصورة الصقر التي أرسلتها (سنستخدمها كأفاتار)
SHAHEEN_LOGO = "logo.jpg"
# إدارة عدد المحاولات المجانية في الجلسة
if 'usage_count' not in st.session_state:
    st.session_state.usage_count = 0

# القائمة الجانبية (مدونة وإعلانات)
with st.sidebar:
    st.image(SHAHEEN_LOGO, width=100)
    st.title("🦅 ShaheenChat")
    st.write("---")
    menu = st.radio("انتقل إلى:", ["الدردشة الذكية", "مدونة الخبراء", "باقات الاشتراك"])
    
    st.write("---")
    st.info("📢 إعلان: مساحة مخصصة لشركات التكنولوجيا والمقاولات")
    st.write("للتواصل: ads@shaheenchat.com")

# --- القسم الأول: الدردشة الذكية مع صورة الصقر ---
if menu == "الدردشة الذكية":
    st.header("🤖 مساعد شاهين الذكي")
    
    # مساحة إعلانية علوية
    st.warning("🎯 إعلان: خدمات استشارية متخصصة لمصانع الألومنيوم والـ UPVC")

    # عرض المحادثة بأسلوب الأفاتار
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar=SHAHEEN_LOGO if message["role"] == "assistant" else None):
            st.markdown(message["content"])

    if prompt := st.chat_input("كيف يمكنني مساعدتك اليوم؟"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # منطق التحقق من المحاولات المجانية (7 محاولات)
        if st.session_state.usage_count < 7:
            with st.chat_message("assistant", avatar=SHAHEEN_LOGO):
                response = f"أهلاً بك في ShaheenChat. أنا هنا لدعم رؤيتك المهنية. بخصوص استفسارك: {prompt}"
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.session_state.usage_count += 1
        else:
            with st.chat_message("assistant", avatar=SHAHEEN_LOGO):
                st.error("⚠️ لقد استنفدت المحاولات المجانية لهذا اليوم.")
                st.write("لتفعيل الوصول غير المحدود وتوليد الصور والملفات الكبيرة:")
                st.button("تفعيل الباقة الاحترافية (15 ريال قطري)")

# --- القسم الثاني: المدونة (SEO) ---
elif menu == "مدونة الخبراء":
    st.header("📚 مدونة رؤى الشاهين (Insights)")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("الذكاء الاصطناعي في مصانع قطر")
        st.write("كيف تساهم الأتمتة في تقليل الهالك في إنتاج الـ UPVC؟")
        st.button("اقرأ المقال", key="b1")
    with col2:
        st.subheader("إدارة الموارد البشرية 2026")
        st.write("إستراتيجيات جذب الكفاءات في قطاع العمليات والتشغيل.")
        st.button("اقرأ المقال", key="b2")

# إعلان في تذييل الصفحة
st.write("---")
st.caption("ShaheenChat.com © 2026 | مدعوم بالذكاء الاصطناعي العالمي")
