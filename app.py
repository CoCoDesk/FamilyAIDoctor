import streamlit as st

# Page Setup
st.set_page_config(page_title="Family AI Doctor", layout="wide")

# -------------------- HEADER --------------------
st.markdown("""
<div style='text-align:center; padding:25px; background:#003566; color:white; border-radius:12px; margin-bottom:30px;'>
    <h1 style='margin:0; font-size:60px;'>🩺 FAMILY AI DOCTOR</h1>
    <p style='color:orange;margin-top:8px; font-size:28px;'>Your Smart Multi-Disease Screening Assistant</p>
</div>
""", unsafe_allow_html=True)

# -------------------- INTRO SECTION --------------------
st.markdown("""
<div style='color: white;text-align:center; font-size:20px; margin-bottom:20px;'>
Select a disease below to check your health status.
</div>
""", unsafe_allow_html=True)

# Background style
st.markdown(
    """
    <style>
    .disease-card {
        background: black;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
        text-align: center;
        transition: 0.3s;
        border: 2px solid #f0f0f0;
    }
    .disease-card:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 25px rgba(0,0,0,0.25);
        border-color: #003566;
    }
    .button-custom {
        background-color: #003566 !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        font-size: 16px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------- DISEASE CARDS --------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='disease-card'>🩸 <h3>Diabetes</h3>", unsafe_allow_html=True)
    if st.button("Open Diabetes Page", key="db", use_container_width=True):
        st.switch_page("pages/Diabetes.py")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='disease-card'>🧬 <h3>Cancer</h3>", unsafe_allow_html=True)
    if st.button("Open Cancer Page", key="cancer", use_container_width=True):
        st.switch_page("pages/Cancer.py")
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='disease-card'>❤️ <h3>Heart Disease</h3>", unsafe_allow_html=True)
    if st.button("Open Heart Disease Page", key="heart", use_container_width=True):
        st.switch_page("pages/Heart_Disease.py")
    st.markdown("</div>", unsafe_allow_html=True)

# Row 2
col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("<div class='disease-card'>🩺 <h3>Kidney Disease</h3>", unsafe_allow_html=True)
    if st.button("Open Kidney Disease Page", key="kidney", use_container_width=True):
        st.switch_page("pages/Kidney_Disease.py")
    st.markdown("</div>", unsafe_allow_html=True)

with col5:
    st.markdown("<div class='disease-card'>🫁 <h3>Liver Disease</h3>", unsafe_allow_html=True)
    if st.button("Open Liver Disease Page", key="liver", use_container_width=True):
        st.switch_page("pages/Liver_Disease.py")
    st.markdown("</div>", unsafe_allow_html=True)

with col6:
    st.markdown("<div class='disease-card'>🧠 <h3>Parkinson's Disease</h3>", unsafe_allow_html=True)
    if st.button("Open Parkinson's Page", key="parkinson", use_container_width=True):
        st.switch_page("pages/Parkinsons.py")
    st.markdown("</div>", unsafe_allow_html=True)


# -------------------- FOOTER --------------------
st.markdown("""
<hr>
<div style='text-align:center; padding:15px; color:gray;'>
    <p>© 2025 Family AI Doctor — All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)
