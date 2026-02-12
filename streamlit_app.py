import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Be Asekhona’s Valentine?", page_icon="💘", layout="centered")

# Soft gradient background + subtle card
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fff0f6 0%, #ffe3ec 30%, #e3f2ff 60%, #f3e8ff 100%);
    background-attachment: fixed;
    color: #1f1f1f;
    font-family: ui-rounded, system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
}
.card {
    max-width: 640px; margin: 10vh auto 6vh; padding: 2rem 2.2rem;
    background: rgba(255,255,255,0.70); border: 1px solid rgba(255,105,180,.25);
    border-radius: 18px; backdrop-filter: blur(10px);
    box-shadow: 0 10px 30px rgba(255,105,180,.25);
}
h1.title {
    font-weight: 800; font-size: 2.1rem; margin: 0 0 .35rem 0;
    background: linear-gradient(90deg,#db2777 0%,#7c3aed 40%,#2563eb 100%);
    -webkit-background-clip: text; background-clip: text; color: transparent;
}
p.sub { margin:.25rem 0 1.1rem; color:#374151 }
.cta { display:flex; gap:.75rem; flex-wrap:wrap }
.stButton>button {
    padding:.75rem 1.25rem; border-radius:999px; font-weight:700; letter-spacing:.2px;
}
.stButton>button.yes {
    background: linear-gradient(90deg,#db2777,#7c3aed); color:#fff; border:none;
    box-shadow: 0 6px 18px rgba(219,39,119,.35);
}
.stButton>button.yes:hover { filter:brightness(1.08); transform:translateY(-1px); transition:.15s }
.stButton>button.maybe {
    background:#fff; color:#7c3aed; border:2px solid #7c3aed;
}
.stButton>button.maybe:hover { background:rgba(124,58,237,.08) }
.footer { text-align:center; color:#4b5563; margin-top:1rem; font-size:.9rem }
blockquote {
    border-left:4px solid #db2777; padding:.6rem 1rem; margin: .5rem 0 1.25rem;
    background: rgba(255,0,102,0.06); border-radius:8px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown('<h1 class="title">Hey there 💌</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub">I made this just for you.</p>', unsafe_allow_html=True)
st.markdown('<blockquote><strong>Can you please be Asekhona’s Valentine?</strong></blockquote>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])
with col1:
    yes = st.button("Yes 💖", key="yes", help="Say yes!", use_container_width=True)
with col2:
    maybe = st.button("Maybe… 🤭", key="maybe", use_container_width=True)

# Add classes to buttons after render (tiny tweak)
st.markdown("""
<script>
const btns = window.parent.document.querySelectorAll('button');
if (btns && btns.length >= 2){
  btns[0].classList.add('yes');
  btns[1].classList.add('maybe');
}
</script>
""", unsafe_allow_html=True)

if yes:
    st.success("Yay! Date locked for 14 Feb 🎉")
    st.balloons()
    st.toast("See you soon! 💖", icon="🎯")
elif maybe:
    st.info("No rush. Coffee first? ☕️🙂")
    st.toast("Totally okay — take your time 💫", icon="⏳")
else:
    st.info("Choose an answer above — I’m rooting for ‘Yes’ 😉")

st.markdown(
    f'<div class="footer">Built with ❤️ by Asekhona · {datetime.now().strftime("%d %b %Y")}</div>',
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)
