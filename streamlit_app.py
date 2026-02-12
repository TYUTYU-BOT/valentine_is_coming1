import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

st.set_page_config(page_title="Be My Valentine", page_icon="💗", layout="centered")

# Optional: center the Streamlit container content
st.markdown("<div style='text-align:center;'></div>", unsafe_allow_html=True)

html = r'''
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
body {
  margin: 0;
}
.stApp {
  background: radial-gradient(1200px 600px at 50% -10%, var(--pink-1), var(--pink-bg));
  color: var(--ink);
  font-family: ui-rounded, system-ui, -apple-system, Segoe UI, Roboto, "Helvetica Neue", Arial, sans-serif;
}

/* Wrapper */
.wrapper {
  margin: 6vh auto 4vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 18px;
  position: relative;
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
  opacity: .85;
  animation-name: fall;
  animation-timing-function: linear;
  animation-iteration-count: infinite;
  filter: drop-shadow(0 2px 2px rgba(255,46,146,.35));
}
@keyframes fall {
  0%   { transform: translateY(-10vh) rotate(0deg); opacity: .95; }
  100% { transform: translateY(110vh) rotate(360deg); opacity: .95; }
}

/* Main heart stage (above falling hearts) */
.heart-stage {
  position: relative;
  z-index: 1;
  display: grid;
  place-items: center;
}

/* CSS heart (square + two circles, rotated) */
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
     0 0 48px rgba(255, 46, 146, .28),
     inset 0 -10px 40px rgba(0,0,0,.12);
  animation: glow 2.2s ease-in-out infinite;
}
.heart:before,
.heart:after {
  content: "";
  position: absolute;
  width: 280px;
  height: 280px;
  background: inherit;              /* matches gradient */
  border-radius: 50%;
  box-shadow:
     0 0 24px rgba(255, 90, 165, .35),
     0 0 48px rgba(255, 46, 146, .22);
}
.heart:before {
  top: -50%;
  left: 0;
}
.heart:after {
  left: 50%;
  top: 0;
}

@keyframes glow {
  0%, 100% { box-shadow:
     0 0 24px rgba(255, 90, 165, .40),
     0 0 48px rgba(255, 46, 146, .25),
     inset 0 -10px 40px rgba(0,0,0,.10); }
  50% { box-shadow:
     0 0 32px rgba(255, 90, 165, .55),
     0 0 64px rgba(255, 46, 146, .35),
     inset 0 -12px 48px rgba(0,0,0,.14); }
}

/* Text inside the heart */
.heart-text {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  padding: 22px;
  transform: rotate(45deg); /* counter the heart's -45deg */
}

.heart-text .text-box {
  text-align: center;
  color: #fff8fb;
  text-shadow:
    0 1px 2px rgba(0,0,0,.20),
    0 0 10px rgba(255, 46, 146, .35);
  line-height: 1.35;
  max-width: 70%;
  margin-top: -6px; /* slight visual centering */
}

.line1 {
  font-weight: 500;
  font-size: 1.0rem;
  opacity: .95;
}
.line2 {
  margin-top: 6px;
  font-weight: 700;
  font-size: 1.15rem;
}
.line3 {
  margin-top: 10px;
  font-weight: 600;
  font-size: .95rem;
  opacity: .95;
}

/* Header and footer */
h1.title {
  margin: 0;
  font-size: clamp(26px, 3.2vw, 40px);
  color: #ad0e6b;
  text-shadow: 0 1px 0 #fff, 0 2px 12px rgba(255,46,146,.25);
}

.smallnote {
  margin-top: 12px;
  color: #8a3a62;
  font-size: 0.9rem;
}
</style>

<div class="fall" id="fall-layer" aria-hidden="true"></div>

<div class="wrapper">
  <h1 class="title">Be My Valentine 💗</h1>

  <div class="heart-stage">
    <div class="heart">
      <div class="heart-text">
        <div class="text-box">
          <div class="line1">I’ve been thinking of you…</div>
          <div class="line2">Would you be my Valentine, please?</div>
          <div class="line3">Love, Asekhona</div>
        </div>
      </div>
    </div>
  </div>

  <div class="smallnote">Made with a lot of 💕 on {today}</div>
</div>

<script>
(function(){
  // Generate falling hearts
  const container = document.getElementById('fall-layer');
  if (!container) return;

  const HEARTS = 40; // number of hearts on screen
  const symbols = ['❤','💗','💖','💘','💝','💞','💓'];

  function makeHeart() {
    const span = document.createElement('span');
    span.textContent = symbols[Math.floor(Math.random() * symbols.length)];

    const left = Math.random() * 100;                        // vw
    const duration = 6 + Math.random() * 8;                 // 6–14s
    const delay = Math.random() * 6;                        // 0–6s
    const size = 14 + Math.random() * 18;                   // 14–32px
    const hue = 330 + Math.floor(Math.random() * 20);       // slight hue variance

    span.style.left = left + 'vw';
    span.style.fontSize = size + 'px';
    span.style.color = `hsl(${hue} 100% 65%)`;
    span.style.animationDuration = duration + 's';
    span.style.animationDelay = delay + 's';
    span.style.opacity = 0.85;

    container.appendChild(span);

    // Remove and re-add after a full cycle to keep the sky populated
    const total = (duration + delay) * 1000;
    setTimeout(() => {
      span.remove();
      makeHeart();
    }, total);
  }

  for (let i = 0; i < HEARTS; i++) {
    setTimeout(makeHeart, Math.random() * 2000);
  }
})();
</script>
'''.replace("{today}", datetime.now().strftime("%B %d, %Y"))

# Render embedded HTML/CSS/JS in Streamlit
components.html(html, height=800, scrolling=False)
.heart:before,
.heart:after {
  content: "";
  width: 280px;
