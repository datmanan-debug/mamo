import streamlit as st

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="Mammogram Analysis Result", layout="centered")

# إضافة الستايل الخاص (CSS) لتطابق الألوان 100% مع الواجهات السابقة
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
    
    /* عنوان النتيجة قبل القيمة بنفس لون الخط الداكن عندك */
    .result-title {
        font-size: 26px;
        font-weight: bold;
        color: #70264E;
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
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.08);
        margin-bottom: 25px; /* المسافة بين الكارتين */
    }
    
    /* ستايل النتيجة الطبيعية (حدود وردية صارخة وخلفية بيضاء) */
    .normal-result {
        border: 3.5px solid #C73B8A;
        background-color: #FFFFFF;
        color: #C73B8A;
    }
    
    /* ستايل النتيجة غير الطبيعية (خلفية وردية صارخة صلبة) */
    .abnormal-result {
        background-color: #C73B8A;
        color: #FFFFFF;
        border: 3.5px solid #C73B8A;
    }
    
    /* أزرار التنقل السفلي (Back و Next) باللون الوردي الصارخ مية بالمية */
    .nav-btn button {
        background-color: #C73B8A !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 12px 40px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        width: 140px !important;
        transition: all 0.2s ease;
        box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.1);
    }
    .nav-btn button:hover {
        background-color: #A32D6F !important; /* تغميق بسيط عند تمرير الماوس */
    }
    </style>
""", unsafe_allow_html=True)


# --- عرض النتائج في المنتصف ---
st.markdown('<div class="result-container">', unsafe_allow_html=True)
st.markdown('<div class="result-title">Analysis Result:</div>', unsafe_allow_html=True)

# النتيجة الأولى: NORMAL مع المسافة المطلوبة
st.markdown('<div class="status-display normal-result">NORMAL</div>', unsafe_allow_html=True)

# النتيجة الثانية: ABNORMAL بنفس اللون الوردي الصارخ
st.markdown('<div class="status-display abnormal-result">ABNORMAL</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# مسافة صغيرة للترتيب قبل أزرار التحكم
st.write("<br>", unsafe_allow_html=True) 


# --- أزرار التحكم (Back و Next) متقاربة باللون الوردي الصارخ في المنتصف ---
nav_col1, nav_col2, nav_col3, nav_col4 = st.columns([1.3, 1, 1, 1.3])

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
