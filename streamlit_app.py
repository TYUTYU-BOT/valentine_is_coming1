import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Be My Valentine", page_icon="💗", layout="centered")

# Center everything
st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)

# ================== THEME, HEART, ANIMATION ==================
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
