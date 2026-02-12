import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Be Asekhona’s Valentine", page_icon="💗", layout="centered")

# -------------------- Global Styles (all pink) --------------------
st.markdown("""
<style>
:root{
  --pink1:#ffecf3; --pink2:#ffd3e3; --pink3:#ff9bc2; --pink4:#ff5aa5; --ink:#2b2b2b;
}
.stApp{
  background: radial-gradient(1200px 600px at 50% -10%, var(--pink2), var(--pink1));
  color: var(--ink);
  font-family: ui-rounded, system-ui, -apple-system, Segoe UI, Roboto, "Helvetica Neue", Arial, sans-serif;
}
.wrapper{ max-width: 780px; margin: 8vh auto 5vh; text-align:center; }

.heart-wrap{
  display:inline-block;
  width:min(520px, 90vw);
  aspect-ratio: 1 / 1;
  position:relative;
  filter: drop-shadow(0 10px 28px rgba(255,90,165,.35));
}

/* Make the SVG fill the container */
.heart-wrap svg{ width:100%; height:100%; display:block; }

/* Centered text inside the heart */
.heart-text{
  font-weight: 750;
  fill: #fff; /* text color inside the pink heart */
  text-shadow: 0 2px 6px rgba(0,0,0,.12);
}

/* Two sizes for a cute hierarchy */
.heart-small{ font-size: 16px; letter-spacing:.4px; opacity:.95; }
.heart-big{ font-size: 24px; }

/* Buttons area */
.actions{ margin-top: 18px; display:flex; gap:12px; justify-content:center; flex-wrap:wrap; }
.stButton>button{
  padding:.75rem 1.25rem; border-radius:999px; font-weight:700; letter-spacing:.2px;
}
.stButton>button.yes{
  background: linear-gradient(90deg, var(--pink4), var(--pink3));
  color:#fff; border:none; box-shadow:0 6px 18px rgba(255,90,165,.35);
}
.stButton>button.yes:hover{ filter:brightness(1.07); transform:translateY(-1px); transition:.15s; }
.stButton>button.maybe{
  background:#fff; color:var(--pink4); border:2px solid var(--pink4);
}
.stButton>button.maybe:hover{ background: rgba(255,90,165,.08); }

/* Footer */
.footer{ margin-top: 10px; color:#6b7280; font-size:.92rem; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="wrapper">', unsafe_allow_html=True)

# -------------------- Heart with all the words inside --------------------
# Using an SVG heart path, with text centered inside.
heart_svg = f"""
<div class="heart-wrap">
  <svg viewBox="0 0 100 100" role="img" aria-label="Heart">
    <defs>
      <!-- Pink glossy gradient -->
      <linearGradient id="g" x1="0" x2="1" y1="0" y2="1">
        <stop offset="0%" stop-color="#ff7ab8"/>
        <stop offset="60%" stop-color="#ff5aa5"/>
        <stop offset="100%" stop-color="#ff2e92"/>
      </linearGradient>
      <filter id="shine" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur in="SourceAlpha" stdDeviation="1.2" result="blur"/>
        <feOffset in="blur" dx="0" dy="0" result="offset"/>
        <feMerge>
          <feMergeNode in="offset"/>
          <feMergeNode in="SourceGraphic"/>
        </feMerge>
      </filter>
    </defs>

    <!-- Heart shape -->
    <path d="M50 18
             C42 5, 20 7, 20 28
             C20 44, 35 56, 50 68
             C65 56, 80 44, 80 28
             C80 7, 58 5, 50 18 Z"
          fill="url(#g)" filter="url(#shine)" />

    <!-- All words live inside the heart -->
    <text x="50" y="38" text-anchor="middle" class="heart-text heart-small">Hey there 💌</text>
    <text x="50" y="52" text-anchor="middle" class="heart-text heart-big">Can you please be</text>
    <text x="50" y="66" text-anchor="middle" class="heart-text heart-big">Asekhona’s Valentine?</text>
  </svg>
</div>
"""
st.markdown(heart_svg, unsafe_allow_html=True)

# -------------------- Buttons (just below the heart) --------------------
c1, c2 = st.columns([1,1])
with c1:
  yes = st.button("Yes 💖", key="yes", use_container_width=True)
with c2:
  maybe = st.button("Maybe… 🤭", key="maybe", use_container_width=True)

# Add the custom classes to the two Streamlit buttons
st.markdown("""
<script>
const btns = window.parent.document.querySelectorAll('button');
if (btns && btns.length >= 2){
  btns[0].classList.add('yes');
  btns[1].classList.add('maybe');
}
</script>
""", unsafe_allow_html=True)

# -------------------- Reactions --------------------
if yes:
    st.success("Yay! Date locked for 14 Feb 🎉")
    st.balloons()
    st.toast("See you soon! 💗", icon="🎯")
elif maybe:
    st.info("No rush. Coffee first? ☕️🙂")
    st.toast("Take your time — I’ll ask again cutely. 💫", icon="⏳")

# -------------------- Footer --------------------
st.markdown(
    f'<div class="footer">Built with 💗 by Asekhona · {datetime.now().strftime("%d %b %Y")}</div>',
    unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)
