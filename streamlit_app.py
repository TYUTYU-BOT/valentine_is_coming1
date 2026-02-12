import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Be My Valentine", page_icon="💗", layout="centered")

# Wrap everything in a centered container
st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)

# ================== THEME, HEART, ANIMATION ==================
# NOTE: We keep this as ONE triple-quoted string to avoid unterminated-string errors.
html = """
<style>
:root{
  --pink-bg: #ffe4ef;
  --pink-1: #ffc1da;
  --pink-2: #ff8fbf;
  --pink-3: #ff5aa5;
  --pink-4: #ff2e92;
  --ink: #2b2b2b;
}

/* Page background - soft pink gradient */
.stApp {
  background: radial-gradient(1200px 600px at 50% -10%, var(--pink-1), var(--pink-bg));
  color: var(--ink);
  font-family: ui-rounded, system-ui, -apple-system, Segoe UI, Roboto, "Helvetica Neue", Arial, sans-serif;
}

/* Container */
.wrapper {
  margin: 6vh auto 2vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 18px;
}

/* Falling hearts layer (behind the main heart) */
.fall {
  position: fixed;
  inset: 0;
  overflow: hidden;
  pointer-events: none;
  z-index: 0;
}
.fall span {
  position: absolute;
  top: -10vh;
  color: #ff5aa5;
  font-size: 16px;
  opacity: .8;
  animation-name: fall;
  animation-timing-function: linear;
  animation-iteration-count: infinite;
}
@keyframes fall {
  0%   { transform: translateY(-10vh) rotate(0deg); opacity: .9; }
  100% { transform: translateY(110vh) rotate(360deg); opacity: 0.9; }
}

/* Main heart container (above falling hearts) */
.heart-stage {
  position: relative;
  z-index: 1;
}

/* CSS-drawn glowing heart */
.heart {
  width: 280px;
  height: 280px;
  position: relative;
  transform: rotate(-45deg);
  margin: 20px auto 4px;
  background: radial-gradient(circle at 30% 30%, #ff6aa9 0%, #ff2e92 70%, #d91d79 100%);
  border-radius: 8px;
  box-shadow:
     0 0 24px rgba(255, 90, 165, .45),
     0 0 48px rgba(255, 46, 146, .28);
  animation: glow 2.2s ease-in-out infinite;
}
.heart:before,
.heart:after {
  content: "";
  width: 280px;
  height: 280px;
  background: radial-gradient(circle at 30% 30%, #ff6aa9 0%, #ff2e92 70%, #d91d79 100%);
  border-radius: 50%;
  position: absolute;
}
.heart:before { top: -140px; left: 0; }
.heart:after  { left: 140px; top: 0; }

@keyframes glow {
  0%, 100% {
    box-shadow:
      0 0 18px rgba(255, 90, 165, .38),
      0 0 36px rgba(255, 46, 146, .20);
    filter: brightness(1);
  }
  50% {
    box-shadow:
      0 0 26px rgba(255, 90, 165, .55),
      0 0 60px rgba(255, 46, 146, .35);
    filter: brightness(1.06);
  }
}

/* White text inside the tilted heart */
.heart-text {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 200px;
  transform: translate(-50%, -50%) rotate(45deg);
  color: #fff;
  text-align: center;
  font-weight: 800;
  line-height: 1.25;
  text-shadow: 0 2px 6px rgba(0,0,0,.18);
}
.heart-text .line1 { font-size: 18px; letter-spacing: .3px; opacity: .95; }
.heart-text .line2 { font-size: 24px; margin-top: 4px; }
.heart-text .line3 { font-size: 14px; margin-top: 10px; opacity: .95; }

/* Footer */
.footer { color:#6b7280; font-size:.92rem; margin-top: 6px; }
</style>

<div class="wrapper">

  <!-- Falling hearts (12 spans) -->
  <div class="fall">
    <span style="left:5%;  animation-duration:6.0s; animation-delay:0.2s;">💗</span>
    <span style="left:12%; animation-duration:7.5s; animation-delay:1.0s;">💗</span>
    <span style="left:20%; animation-duration:8.2s; animation-delay:0.6s;">💗</span>
    <span style="left:28%; animation-duration:6.8s; animation-delay:1.4s;">💗</span>
    <span style="left:36%; animation-duration:7.0s; animation-delay:0.1s;">💗</span>
    <span style="left:44%; animation-duration:6.2s; animation-delay:0.9s;">💗</span>
    <span style="left:52%; animation-duration:7.8s; animation-delay:0.5s;">💗</span>
    <span style="left:60%; animation-duration:6.6s; animation-delay:1.3s;">💗</span>
    <span style="left:68%; animation-duration:8.0s; animation-delay:0.3s;">💗</span>
    <span style="left:76%; animation-duration:7.2s; animation-delay:1.1s;">💗</span>
    <span style="left:84%; animation-duration:6.4s; animation-delay:0.7s;">💗</span>
    <span style="left:92%; animation-duration:7.6s; animation-delay:0.4s;">💗</span>
  </div>

  <!-- Main glowing heart -->
  <div class="heart-stage">
    <div class="heart"></div>
    <div class="heart-text">
      <div class="line1">Can you be my</div>
      <div class="line2">Valentine?</div>
      <div class="line3">Love, Asekhona</div>
    </div>
  </div>

</div>
"""

# Inject HTML/CSS
st.markdown(html, unsafe_allow_html=True)

# ================== BUTTONS (YES / MAYBE) ==================
c1, c2 = st.columns([1, 1])
with c1:
    yes_clicked = st.button("Yes 💖", use_container_width=True)
with c2:
    no_clicked = st.button("Maybe later 💭", use_container_width=True)

# Responses
if yes_clicked:
    st.success("Yay! See you on the 14th 🎉")
    st.balloons()
    st.toast("Date locked in! 💗", icon="🎯")
elif no_clicked:
    st.info("All good — coffee first? ☕️🙂")
    st.toast("No rush. I’ll ask again, but cuter. ✨", icon="⏳")

# Footer
st.markdown(
    f"<div class='footer'>Built with 💗 by Asekhona • {datetime.now().strftime('%d %b %Y')}</div>",
    unsafe_allow_html=True
)
st.markdown("</div>", unsafe_allow_html=True)
