import streamlit as st

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="Mammogram Analysis Result", layout="centered")

# إضافة الستايل الخاص (CSS) مع إجبار الألوان الوردية الصارخة 100%
st.markdown("""
    <style>
    /* تغيير خلفية التطبيق بأكمله إلى الأبيض */
    .stApp {
        background-color: #FDF8FB !important;
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
        color: #C2185B !important;
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
        border: 4px solid #E91E8C !important;
        background-color: ##FDF8FB !important;
        color: #FFFFFF !important;
    }
    
    /* ستايل النتيجة غير الطبيعية (خلفية وردية صارخة صلبة) */
    .abnormal-result {
        background-color: #C73B8A !important;
        color: #FFFFFF !important;
        border: 4px solid #E91E8C !important;
    }
    
    /* --- إجبار أزرار التحكم (Back و Next) على اللون الوردي الصارخ وطرد البنفسجي --- */
    div.stButton > button {
        background-color: #E91E8C !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 12px 40px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        width: 140px !important;
        box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.1) !important;
        transition: all 0.2s ease !important;
    }
    
    /* تأثير حركي عند تمرير الماوس على أزرار باك ونيكست */
    div.stButton > button:hover {
        background-color: #A32D6F !important;
        color: #C2185B !important;
        border: none !important;
    }
    
    /* إلغاء أي تأثير للون البنفسجي عند الضغط أو التركيز على الأزرار */
    div.stButton > button:focus {
        background-color: #C73B8A !important;
        color: #C2185B !important;
        border: none !important;
        box-shadow: 0px 3px 8px rgba(0, 0, 0, 0.1) !important;
    }
    </style>
""", unsafe_allow_html=True)


# --- عرض النتائج في المنتصف ---
st.markdown('<div class="result-container">', unsafe_allow_html=True)
st.markdown('<div class="result-title">Analysis Result:</div>', unsafe_allow_html=True)

# النتيجة الأولى: NORMAL مع المسافة المطلوبة والحدود الوردية
st.markdown('<div class="status-display normal-result">NORMAL</div>', unsafe_allow_html=True)

# النتيجة الثانية: ABNORMAL باللون الوردي الصارخ الكامل
st.markdown('<div class="status-display abnormal-result">ABNORMAL</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# مسافة صغيرة للترتيب قبل أزرار التحكم
st.write("<br>", unsafe_allow_html=True) 


# --- أزرار التحكم (Back و Next) متقاربة باللون الوردي الصارخ الإجباري ---
nav_col1, nav_col2, nav_col3, nav_col4 = st.columns([1.3, 1, 1, 1.3])

with nav_col2:
    # تم محاذاة حاوية الزر لليمين لتقريبه من النيكست
    st.markdown('<div style="display: flex; justify-content: flex-end;">', unsafe_allow_html=True)
    if st.button("« Back"):
        st.write("") # مكان الأكشن للرجوع
    st.markdown('</div>', unsafe_allow_html=True)

with nav_col3:
    # تم محاذاة حاوية الزر لليسار لتقريبه من الباك
    st.markdown('<div style="display: flex; justify-content: flex-start;">', unsafe_allow_html=True)
    if st.button("Next »"):
        st.write("") # مكان الأكشن للتالي
    st.markdown('</div>', unsafe_allow_html=True)
