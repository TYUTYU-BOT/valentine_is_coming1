import streamlit as st
from datetime import datetime

# ---------- Page Setup ----------
st.set_page_config(
    page_title="Valentine Ask",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------- Custom CSS (Colours + Layout) ----------
st.markdown("""
<style>
/* Background gradient */
.stApp {
    background: linear-gradient(135deg, #fff0f6 0%, #ffe3ec 30%, #e3f2ff 60%, #f3e8ff 100%);
    background-attachment: fixed;
    color: #1f1f1f;
}

/* Glass card container */
.card {
    max-width: 720px;
    margin: 6vh auto 4vh auto;
    padding: 2.2rem 2rem;
    background: rgba(255,255,255,0.65);
    border: 1px solid rgba(255, 105, 180, 0.2);
    border-radius: 18px;
    backdrop-filter: blur(10px);
    box-shadow: 0 10px 30px rgba(255, 105, 180, 0.25);
}

/* Title styling */
h1.title {
    font-family: ui-rounded, system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
    font-weight: 800;
    font-size: 2.2rem;
    letter-spacing: .3px;
    margin: 0 0 .25rem 0;
    background: linear-gradient(90deg, #db2777 0%, #7c3aed 40%, #2563eb 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
}

/* Subtitle */
.subtitle {
    margin: 0 0 1rem 0;
    color: #374151;
    font-size: 1rem;
}

/* Quoted line */
blockquote {
    border-left: 4px solid #db2777;
    padding: .6rem 1rem;
    margin: 1rem 0 1.25rem 0;
    background: rgba(255, 0, 102, 0.06);
    border-radius: 8px;
}

/* Button row */
.btn-row {
    display: flex;
    gap: .75rem;
    flex-wrap: wrap;
    margin-top: .5rem;
}

/* Primary button style (Yes) */
.stButton > button.primary {
    background: linear-gradient(90deg, #db2777, #7c3aed);
    color: #fff;
    border: none;
    padding: .75rem 1.25rem;
    border-radius: 999px;
    font-weight: 700;
    letter-spacing: .2px;
    box-shadow: 0 6px 18px rgba(219,39,119,.35);
}
.stButton > button.primary:hover {
    filter: brightness(1.08);
    transform: translateY(-1px);
    transition: .15s ease;
}

/* Secondary button style (Not yet) */
.stButton > button.ghost {
    background: transparent;
    color: #7c3aed;
    border: 2px solid #7c3aed;
    padding: .73rem 1.2rem;
    border-radius: 999px;
    font-weight: 700;
}
.stButton > button.ghost:hover {
    background: rgba(124,58,237,0.08);
}

/* Footer note */
.footer {
    margin-top: 1rem;
    font-size: .9rem;
    color: #4b5563;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------- Content Card ----------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown('<h1 class="title">Hey [Their Name] 💌</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">I built this just for you.</p>', unsafe_allow_html=True)

st.markdown("""
<blockquote>
<strong>Our synergy is bug-free, our roadmap aligned.</strong>
</blockquote>
""", unsafe_allow_html=True)

# A little context / charm
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("**Why you?**")
    st.write("- You turn ordinary moments into highlight reels.")
    st.write("- Our conversations flow like clean, well-documented code.")
    st.write("- I’m excited about where this story can go.")
with col2:
    st.markdown("**Plan for 14 Feb**")
    st.write("- A relaxed walk and great conversation.")
    st.write("- Your favourite treat (you choose).")
    st.write("- A playlist we make together.")

st.write("")  # spacing

# ---------- Buttons ----------
c1, c2 = st.columns([1, 1])

with c1:
    yes_clicked = st.button("Yes, be my Valentine ❤️", key="yes", type="primary")
with c2:
    notyet_clicked = st.button("Not yet—ask me nicely 😅", key="nope")

# Apply CSS classes to buttons (post-render tweak)
st.markdown("""
<script>
const btns = window.parent.document.querySelectorAll('button[kind="primary"]');
if (btns && btns.length){
  btns[0].classList.add('primary');
}
const allBtns = window.parent.document.querySelectorAll('button');
if (allBtns && allBtns.length > 1){
  allBtns[1].classList.add('ghost');
}
</script>
""", unsafe_allow_html=True)

# ---------- Reactions ----------
if yes_clicked:
    st.success("Yes! 🎉 Can't wait for the 14th.")
    # Fun effects
    st.balloons()
    st.toast("Date locked in! 💖", icon="🎯")
elif notyet_clicked:
    st.info("I hear you. How about a coffee, a smile, and a second ask? ☕️🙂")
    st.toast("Challenge accepted — iterating request v2.0…", icon="🛠️")
else:
    st.info("Click a button — there’s only one right answer 😉")

# Footer / timestamp
st.markdown(
    f'<div class="footer">Built with ❤️ in Streamlit · {datetime.now().strftime("%d %b %Y")}</div>',
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)
