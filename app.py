import streamlit as st

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="Mammogram Analysis Result", layout="centered")

# إضافة الستايل الخاص (CSS) لتنسيق الألوان والأزرار باللون الوردي المعتمد بدقة
st.markdown("""
    <style>
    /* تغيير خلفية التطبيق بأكمله إلى الأبيض */
    .stApp {
        background-color: #FFFFFF;
    }
    
    /* حاوية مخصصة لتوسط الأزرار عمودياً في الشاشة */
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 40vh;
        margin-top: 50px;
    }
    
    /* تنسيق أزرار الخيارات الأساسية (Normal / Abnormal) */
    div.stButton > button {
        width: 100%;
        border-radius: 25px; /* حواف دائرية ناعمة تتناسق مع واجهاتك السابقة */
        font-size: 20px !important;
        font-weight: bold !important;
        padding: 12px 35px !important;
        transition: all 0.3s ease;
    }
    
    /* زر NORMAL (خلفية بيضاء وحدود وردية) */
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) button {
        border: 2px solid #E6A2C5 !important;
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) button:hover {
        background-color: #E6A2C5 !important;
        color: #FFFFFF !important;
    }
    
    /* زر ABNORMAL (خلفية وردية كاملة والكتابة سوداء أو بيضاء حسب رغبتك) */
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) button {
        background-color: #E6A2C5 !important;
        color: #FFFFFF !important;
        border: 2px solid #E6A2C5 !important;
    }
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) button:hover {
        background-color: #D185A6 !important;
        border-color: #D185A6 !important;
    }
    
    /* أزرار التنقل السفلي (Back و Next) */
    .nav-container {
        display: flex;
        justify-content: space-between;
        margin-top: 100px;
        width: 100%;
    }
    
    .nav-btn button {
        background-color: #E6A2C5 !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 20px !important;
        padding: 8px 30px !important;
        font-size: 16px !important;
    }
    .nav-btn button:hover {
        background-color: #D185A6 !important;
    }
    </style>
""", unsafe_allow_html=True)

# بداية الحاوية لتوسيط العناصر
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# عرض أزرار الحالة (NORMAL و ABNORMAL) متجاورين في المنتصف
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("NORMAL"):
        st.success("تم اختيار: طبيعي (NORMAL)")

with col2:
    if st.button("ABNORMAL"):
        st.warning("تم اختيار: غير طبيعي (ABNORMAL)")

st.markdown('</div>', unsafe_allow_html=True)


# إضافة أزرار التحكم السفلي (Back و Next) متباعدين على الأطراف كما في واجهاتك السابقة
st.write("") 
nav_col1, nav_col2 = st.columns([1, 1])

with nav_col1:
    st.markdown('<div class="nav-btn">', unsafe_allow_html=True)
    if st.button("« Back"):
        st.info("الرجوع للواجهة السابقة...")
    st.markdown('</div>', unsafe_allow_html=True)

with nav_col2:
    # لتوجيه زر Next إلى أقصى اليمين
    st.markdown('<div class="nav-btn" style="text-align: right; display: flex; justify-content: flex-end;">', unsafe_allow_html=True)
    if st.button("Next »"):
        st.info("الانتقال للواجهة التالية...")
    st.markdown('</div>', unsafe_allow_html=True)
