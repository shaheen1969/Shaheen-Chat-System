import streamlit as st

# 1. إعدادات الصفحة الاحترافية
st.set_page_config(page_title="ShaheenChat | AI Business Insights", layout="wide", page_icon="🦅")

# استخدمنا أيقونة الصقر كشعار مؤقت يظهر في كل المتصفحات بلا استثناء
SHAHEEN_ICON = "🦅"

# إدارة عدد المحاولات المجانية (7 محاولات لرضا الزوار)
if 'usage_count' not in st.session_state:
    st.session_state.usage_count = 0

# --- 2. القائمة الجانبية (المدونة والإعلانات) ---
with st.sidebar:
    st.markdown(f"<h1 style='text-align: center;'>{SHAHEEN_ICON}</h1>", unsafe_allow_html=True)
    st.title("ShaheenChat")
    st.write("---")
    menu = st.radio("انتقل إلى:", ["الدردشة الذكية", "مدونة الخبراء (Insights)", "باقات الاشتراك"])
    
    st.write("---")
    st.markdown("### 📢 مساحة إعلانية")
    st.info("فرصة للمعلنين: استهدف نخبة الصناعيين والمدراء في قطر.")
    st.write("للتواصل: ads@shaheenchat.com")

# --- 3. القسم الأول: الدردشة الذكية ---
if menu == "الدردشة الذكية":
    st.header(f"{SHAHEEN_ICON} مساعد شاهين الذكي")
    
    # مساحة إعلان علوية (Banner)
    st.success("🎯 **إعلان:** حلول متكاملة لمصانع الألومنيوم والـ UPVC - استشارات تقنية وإدارية.")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # عرض المحادثة
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar=SHAHEEN_ICON if message["role"] == "assistant" else None):
            st.markdown(message["content"])

    if prompt := st.chat_input("كيف يمكنني مساعدتك اليوم؟"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        if st.session_state.usage_count < 7:
            with st.chat_message("assistant", avatar=SHAHEEN_ICON):
                response = f"أهلاً بك في ShaheenChat. بصفتي مساعدك الذكي، يسعدني دعم رؤيتك المهنية. بخصوص سؤالك: {prompt}"
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.session_state.usage_count += 1
        else:
            with st.chat_message("assistant", avatar=SHAHEEN_ICON):
                st.error("⚠️ استنفدت المحاولات المجانية (7/7).")
                st.write("لدعم المنصة والحصول على ميزات غير محدودة:")
                st.button("تفعيل الباقة الاحترافية (15 ريال قطري)")

# --- 4. القسم الثاني: المدونة (SEO & Traffic) ---
elif menu == "مدونة الخبراء (Insights)":
    st.header("📚 مدونة رؤى الشاهين الصناعية")
    st.write("مقالات حصرية تدمج بين الخبرة الميدانية والذكاء الاصطناعي.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("الذكاء الاصطناعي في مصانع قطر")
        st.write("كيف تساهم الأتمتة في تقليل الهالك وتحسين جودة إنتاج الـ UPVC.")
        st.button("قراءة المقال كاملاً", key="blog_1")
        
    with col2:
        st.subheader("مستقبل إدارة الموارد البشرية")
        st.write("إستراتيجيات جذب الكفاءات الفنية والقيادية في قطاع العمليات.")
        st.button("قراءة المقال كاملاً", key="blog_2")

# --- 5. تذييل الصفحة ---
st.write("---")
st.caption("ShaheenChat.com © 2026 | بوابة الذكاء الاصطناعي الرائدة في الدوحة")
