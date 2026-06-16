import streamlit as st

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="Mammogram Analysis Result", layout="centered")

# إضافة الستايل الخاص (CSS) لتنسيق الألوان والأزرار والحدود الوردية بدقة
st.markdown("""
    <style>
    /* تغيير خلفية التطبيق بأكمله إلى الأبيض */
    .stApp {
        background-color: #FFFFFF;
    }
    
    /* تنسيق حاوية الصورة الدائرية الحواف باللون الوردي المعتمد */
    .img-box {
        border: 2px solid #E6A2C5;
        border-radius: 15px;
        padding: 15px;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: #FFF5F9; /* خلفية وردية خفيفة جداً داخل إطار الصورة */
        margin: 0 auto 30px auto;
        max-width: 250px;
    }
    
    /* تنسيق أزرار الخيارات (Normal / Abnormal) */
    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        font-size: 18px !important;
        font-weight: bold !important;
        padding: 10px 25px !important;
        transition: all 0.3s ease;
    }
    
    /* زر Normal (خلفية بيضاء وحدود وردية) */
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) button {
        border: 2px solid #E6A2C5 !important;
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) button:hover {
        background-color: #E6A2C5 !important;
        color: #FFFFFF !important;
    }
    
    /* زر Abnormal (خلفية وردية كاملة) */
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) button {
        background-color: #E6A2C5 !important;
        color: #FFFFFF !important;
        border: 2px solid #E6A2C5 !important;
    }
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) button:hover {
        background-color: #D185A6 !important;
        border-color: #D185A6 !important;
    }
    
    /* زر Next في أسفل اليمين */
    .next-container {
        display: flex;
        justify-content: flex-end;
        margin-top: 50px;
    }
    .next-container button {
        background-color: #E6A2C5 !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 5px !important;
        padding: 8px 25px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 1. عرض الصورة داخل صندوق التنسيق الوردي (كما في image_4.png)
st.markdown('<div class="img-box">', unsafe_allow_html=True)
# استبدل "mamo_img.png" باسم ملف الصورة الحقيقي المرفوع عندك في الفولدر
st.image("mamo_img.png", width=180) 
st.markdown('</div>', unsafe_allow_html=True)

# مساحة للفصل
st.write("")

# 2. عرض أزرار الحالة (NORMAL و ABNORMAL) متجاورين بدقة
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("NORMAL"):
        st.success("تم اختيار: طبيعي")

with col2:
    if st.button("ABNORMAL"):
        st.warning("تم اختيار: غير طبيعي")

# 3. زر التالي (Next) متموضع في الجانب السفلي
st.markdown('<div class="next-container">', unsafe_allow_html=True)
if st.button("Next »"):
    st.info("الانتقال للواجهة التالية...")
st.markdown('</div>', unsafe_allow_html=True)