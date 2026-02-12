import streamlit as st

st.set_page_config(page_title="Valentine", page_icon="❤️", layout="centered")

# Center everything
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)

# --- Simple Red Heart with White Text ---
heart_html = """
<style>
.heart-container {
    display: flex;
    justify-content: center;
    margin-top: 40px;
}

.heart {
    width: 260px;
    height: 260px;
    background-color: red;
    position: relative;
    transform: rotate(-45deg);
    margin: 20px;
}

.heart:before,
.heart:after {
    content: "";
    width: 260px;
    height: 260px;
    background-color: red;
    border-radius: 50%;
    position: absolute;
}

.heart:before {
    top: -130px;
    left: 0;
}

.heart:after {
    left: 130px;
    top: 0;
}

.heart-text {
    position: absolute;
    top: 48%;
    left: 50%;
    transform: translate(-50%, -50%) rotate(45deg);
    color: white;
    font-size: 18px;
    font-weight: bold;
    width: 180px;
    text-align: center;
    line-height: 1.3;
}
</style>

<div class="heart-container">
    <div class="heart">
        <div class="heart-text">
            Can you be my<br>
            Valentine?<br><br>
            Love, Asekhona
        </div>
    </div>
</div>
"""

st.markdown(heart_html, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
