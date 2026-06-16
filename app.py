import streamlit as st

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="Mammogram Analysis Result", layout="centered")

# إضافة الستايل الخاص (CSS) لتنسيق الألوان لعرض النتيجة والتحكم
st.markdown("""
    <style>
    /* تغيير خلفية التطبيق بأكمله إلى الأبيض */
    .stApp {
        background-color: #FFFFFF;
    }
    
    /* حاوية مخصصة لتوسط النتيجة في الشاشة */
    .result-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-top: 50px;
    }
    
    /* عنوان النتيجة قبل القيمة */
    .result-title {
        font-size: 26px;
        font-weight: bold;
        color: #333333;
        margin-bottom: 25px;
    }
    
    /* تنسيق كارت النتيجة النهائي الدائري */
    .status-display {
        width: 320px;
        border-radius: 25px;
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        padding: 15px 0;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.05);
        margin-bottom: 25px; /* إضافة مسافة واضحة بين الكارتين */
    }
    
    /* ستايل النتيجة الطبيعية (حدود وردية واضحة وخلفية بيضاء) */
    .normal-result {
        border: 3px solid #C43785;
        background-color: #FFFFFF;
        color: #C43785;
    }
    
    /* ستايل النتيجة غير الطبيعية (خلفية وردية صلبة كاملة) */
    .abnormal-result {
        background-color: #C43785;
        color: #FFFFFF;
        border: 3px solid #C43785;
    }
    
    /* حاوية مخصصة لتقريب أزرار التنقل السفلي في المنتصف */
    .nav-container {
        display: flex;
        justify-content: center;
        gap: 20px; /* مسافة قريبة بين زر باك ونيكست */
        margin-top: 40px;
        width: 100%;
    }
    
    /* أزرار التنقل باللون الوردي الصارخ/الصلب مثل الواجهات السابقة */
    .nav-btn button {
        background-color: #C43785 !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 12px 40px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        width: 130px !important;
        transition: all 0.3s ease;
    }
    .nav-btn button:hover {
        background-color: #A12669 !important;
    }
    </style>
""", unsafe_allow_html=True)


# --- جزء العرض المركزي للنتائج ---
st.markdown('<div class="result-container">', unsafe_allow_html=True)
st.markdown('<div class="result-title">Analysis Result:</div>', unsafe_allow_html=True)

# عرض النتيجة الأولى: NORMAL وبينهما مسافة
st.markdown('<div class="status-display normal-result">NORMAL</div>', unsafe_allow_html=True)

# عرض النتيجة الثانية: ABNORMAL
st.markdown('<div class="status-display abnormal-result">ABNORMAL</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# مسافة عزل صغيرة لتنسيق الواجهة
st.write("<br>", unsafe_allow_html=True) 


# --- أزرار التحكم (Back و Next) متقاربة باللون الوردي الصارخ في المنتصف ---
nav_col1, nav_col2, nav_col3, nav_col4 = st.columns([1.5, 1, 1, 1.5])

with nav_col2:
    st.markdown('<div class="nav-btn" style="display: flex; justify-content: flex-end;">', unsafe_allow_html=True)
    if st.button("« Back"):
        st.info("الرجوع...")
    st.markdown('</div>', unsafe_allow_html=True)

with nav_col3:
    st.markdown('<div class="nav-btn" style="display: flex; justify-content: flex-start;">', unsafe_allow_html=True)
    if st.button("Next »"):
        st.info("التالي...")
    st.markdown('</div>', unsafe_allow_html=True)
