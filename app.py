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
        gap: 20px; /* المسافة بين العنصرين */
        margin-top: 50px;
    }
    
    /* عنوان النتيجة قبل القيمة */
    .result-title {
        font-size: 24px;
        font-weight: bold;
        color: #333333;
        margin-bottom: 10px;
    }
    
    /* تنسيق كارت النتيجة النهائي الدائري */
    .status-display {
        width: 280px;
        border-radius: 25px;
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        padding: 12px 0;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.05);
    }
    
    /* ستايل النتيجة الطبيعية (حدود وردية وخلفية بيضاء) */
    .normal-result {
        border: 2px solid #a85585;
        background-color: #FFFFFF;
        color: #a85585;
    }
    
    /* ستايل النتيجة غير الطبيعية (خلفية وردية كاملة) */
    .abnormal-result {
        background-color: #a85585;
        color: #FFFFFF;
        border: 2px solid #a85585;
    }
    
    /* أزرار التنقل السفلي (Back و Next) الفاتحة كباقي الواجهات */
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


# --- جزء العرض (حالياً يعرض الإثنين معاً لمعاينة الشكل واللون) ---
st.markdown('<div class="result-container">', unsafe_allow_html=True)
st.markdown('<div class="result-title">Analysis Result:</div>', unsafe_allow_html=True)

# عرض النتيجة الأولى: NORMAL
st.markdown('<div class="status-display normal-result">NORMAL</div>', unsafe_allow_html=True)

# عرض النتيجة الثانية: ABNORMAL
st.markdown('<div class="status-display abnormal-result">ABNORMAL</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# --- 💡 ملاحظة لك للمستقبل عند ربط الخوارزمية 💡 ---
# لما تكمل الخوارزمية، راح تمسح السطرين اللي فوك (سطور عرض NORMAL و ABNORMAL معاً) وتستبدلهم بـ if وطباعة وحدة بس مثل هيج:
#
# if ai_result == "NORMAL":
#     st.markdown('<div class="status-display normal-result">NORMAL</div>', unsafe_allow_html=True)
# else:
#     st.markdown('<div class="status-display abnormal-result">ABNORMAL</div>', unsafe_allow_html=True)


# مسافة عزل قبل أزرار التنقل السفلية
st.write("<br><br><br>", unsafe_allow_html=True) 

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
