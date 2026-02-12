import streamlit as st

# --- Styles for crisp text inside the heart ---
st.markdown("""
<style>
.heart-wrap{
  display:inline-block;
  width:min(520px, 90vw);
  aspect-ratio: 1 / 1;
  position:relative;
  filter: drop-shadow(0 10px 28px rgba(255,90,165,.35));
}
.heart-text{
  font-weight: 750;
  fill: #fff;                 /* text color inside the pink heart */
  text-shadow: 0 2px 6px rgba(0,0,0,.12);
  font-family: ui-rounded, system-ui, -apple-system, Segoe UI, Roboto, "Helvetica Neue", Arial, sans-serif;
}
.heart-small{ font-size: 16px; letter-spacing:.4px; opacity:.95; }
.heart-big{ font-size: 24px; }
</style>
""", unsafe_allow_html=True)

# --- Your SVG heart with words inside ---
st.markdown("""
<div class="heart-wrap">
  <svg viewBox="0 0 100 100" role="img" aria-label="Heart" xmlns="http://www.w3.org/2000/svg">
    <defs>
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
""", unsafe_allow_html=True)
