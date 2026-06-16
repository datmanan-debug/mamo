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
        margin-top: 60px;
    }
    
    /* عنوان النتيجة قبل القيمة */
    .result-title {
        font-size: 24px;
        font-weight: bold;
        color: #333333;
        margin-bottom: 15px;
    }
    
    /* تنسيق كارت النتيجة النهائي الدائري */
    .status-display {
        width: 280px;
        border-radius: 25px;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        padding: 15px 0;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.05);
    }
    
    /* ستايل النتيجة إذا كانت طبيعية */
    .normal-result {
        border: 3px solid #a85585;
        background-color: #FFFFFF;
        color: #a85585;
    }
    
    /* ستايل النتيجة إذا كانت غير طبيعية */
    .abnormal-result {
        background-color: #a85585;
        color: #FFFFFF;
        border: 3px solid #a85585;
    }
    
    /* أزرار التنقل السفلي (Back و Next) */
    .nav-btn button {
        background-color: #D692BA !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 10px 35px !important;
        font-size: 18px !important;
        font-weight: bold !important;
    }
    .nav-btn button:hover {
        background-color: #bd7fa3 !important;
    }
    </style>
""", unsafe_allow_html=True)


# --- هنا الربط مع الخوارزمية ---
# افتراضياً، هنا الخوارزمية مالتك رح تنطي النتيجة (إما "NORMAL" أو "ABNORMAL")
# حالياً خليتها "ABNORMAL" كمثال، وتكدر تغيرها إلى "NORMAL" لتجربة الشكلين
ai_result = "ABNORMAL" 


# عرض النتيجة المباشرة تلقائياً داخل الحاوية
st.markdown('<div class="result-container">', unsafe_allow_html=True)
st.markdown('<div class="result-title">Analysis Result:</div>', unsafe_allow_html=True)

if ai_result == "NORMAL":
    # يعرض مربع طبيعي (حدود وردية وخلفية بيضاء) تلقائياً بدون ضغط
    st.markdown('<div class="status-display normal-result">NORMAL</div>', unsafe_allow_html=True)
else:
    # يعرض مربع غير طبيعي (خلفية وردية كاملة) تلقائياً بدون ضغط
    st.markdown('<div class="status-display abnormal-result">ABNORMAL</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# مسافة عزل قبل أزرار التنقل السفلية
st.write("<br><br><br><br>", unsafe_allow_html=True) 

# أزرار التحكم (Back و Next) متباعدين على الأطراف بنفس التنسيق المستقر للواجهات السابقة
nav_col1, nav_col2 = st.columns([1, 1])

with nav_col1:
    st.markdown('<div class="nav-btn">', unsafe_allow_html=True)
    if st.button("« Back"):
        st.info("الرجوع للواجهة السابقة...")
    st.markdown('</div>', unsafe_allow_html=True)

with nav_col2:
    st.markdown('<div class="nav-btn" style="display: flex; justify-content: flex-end;">', unsafe_allow_html=True)
    if st.button("Next »"):
        st.info("الانتقال للواجهة التالية...")
    st.markdown('</div>', unsafe_allow_html=True)
