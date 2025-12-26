import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# =========================
# 1️⃣ PAGE CONFIG + STYLING
# =========================
st.set_page_config("Chai Taste Intelligence v3", "🫖", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

/* Global Styles */
.main { 
    padding: 2rem 4rem;
    font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #fdfbfb 0%, #f7f4ed 100%);
}

h1 { 
    margin-bottom: 0.2rem;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 700;
    font-size: 3rem !important;
}

h2, h3 {
    color: #2d3748;
    font-weight: 600;
}

/* Metric Card with Gradient */
.metric-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 20px;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
    color: white;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.metric-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 40px rgba(102, 126, 234, 0.4);
}

.metric-card h3, .metric-card h2 {
    color: white !important;
}

/* Result Box with Enhanced Design */
.result-box {
    background: #ffffff;
    border-radius: 20px;
    padding: 2rem;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    border: 1px solid rgba(102, 126, 234, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.result-box:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 32px rgba(0,0,0,0.12);
}

/* Enhanced Tags */
.tag {
    display: inline-block;
    padding: 8px 16px;
    border-radius: 25px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    margin-right: 8px;
    margin-top: 8px;
    font-weight: 500;
    font-size: 0.9rem;
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.25);
    transition: transform 0.2s ease;
}

.tag:hover {
    transform: scale(1.05);
}

/* Survey Section Styling */
.stSlider {
    padding: 0.5rem 0;
}

/* Button Enhancement */
.stButton > button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    padding: 0.75rem 2.5rem;
    border-radius: 30px;
    font-weight: 600;
    font-size: 1.1rem;
    box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 28px rgba(102, 126, 234, 0.4);
}

/* Divider Enhancement */
hr {
    margin: 2rem 0;
    border: none;
    height: 2px;
    background: linear-gradient(90deg, transparent, #667eea, transparent);
}

/* Caption Styling */
.css-1629p8f, [data-testid="stCaptionContainer"] {
    color: #718096;
    font-size: 1.1rem;
    font-weight: 500;
}

/* Success Box Enhancement */
.stSuccess {
    background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
    color: white;
    border-radius: 15px;
    padding: 1rem;
    font-weight: 600;
    font-size: 1.2rem;
}

/* Section Headers */
.section-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 700;
    margin-top: 1.5rem;
}

/* Animation */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.result-box, .metric-card {
    animation: fadeIn 0.6s ease-out;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🫖 Chai Taste Intelligence</h1>", unsafe_allow_html=True)
st.caption("✨ AI-driven flavor profiling • Psychometric survey • Smart tea recommendation ✨")
st.divider()

# =========================
# 2️⃣ PSYCHOMETRIC SURVEY
# =========================
st.header("📝 Flavor & Preference Survey")

def trait_block(title, questions):
    st.markdown(f'<h3 class="section-header">{title}</h3>', unsafe_allow_html=True)
    scores = [st.slider(q, 1, 10, 5, key=f"{title}_{i}") for i, q in enumerate(questions)]
    return np.mean(scores) / 10  # normalize 0–1

capsaicin = trait_block("🌶️ Spice Sensitivity", [
    "I enjoy chili-based foods",
    "I seek spicy options on menus",
    "I tolerate strong spice heat well"
])

sweet = trait_block("🍯 Sweet Preference", [
    "I enjoy sweet drinks",
    "Desserts are important to me",
    "I like sugar in beverages"
])

lactose = trait_block("🥛 Dairy Comfort", [
    "I enjoy milk-heavy drinks",
    "Creamy textures feel comforting",
    "Milk-based beverages suit me"
])

bitter = trait_block("🍃 Bitterness Tolerance", [
    "I enjoy dark chocolate",
    "Black coffee tastes good to me",
    "Bitter flavors don't bother me"
])

aroma = trait_block("🌿 Aroma Sensitivity", [
    "Smell strongly affects taste for me",
    "I love fragrant food",
    "Aromas matter when choosing drinks"
])

thermal = trait_block("🔥 Thermal Preference", [
    "I enjoy hot beverages",
    "Warm drinks feel satisfying",
    "Cold drinks are less appealing"
])

neophilia = trait_block("🚀 Food Neophilia", [
    "I enjoy trying new flavors",
    "I seek unfamiliar cuisines",
    "I like experimenting with food"
])

culture = trait_block("🌍 Cultural Flavor Exposure", [
    "I eat foods from many cultures",
    "I'm familiar with Indian spices",
    "I enjoy global cuisine"
])

texture = trait_block("🧈 Texture Preference", [
    "Mouthfeel matters to me",
    "I enjoy thick creamy drinks",
    "I dislike watery beverages"
])

caffeine = trait_block("☕ Caffeine Comfort", [
    "Caffeine affects me mildly",
    "I enjoy caffeinated drinks",
    "Tea/coffee suits my body well"
])

# =========================
# 3️⃣ FEATURE ENGINEERING
# =========================
X = np.array([capsaicin, sweet, lactose, bitter, aroma, thermal,
              neophilia, culture, texture, caffeine])

# Derived features
flavor_complexity = np.mean([neophilia, aroma, bitter])
spice_dairy_balance = capsaicin * lactose
comfort_index = np.mean([thermal, texture, sweet])
cultural_adaptability = np.mean([culture, neophilia])

X_eng = np.concatenate([X, [flavor_complexity, spice_dairy_balance, comfort_index, cultural_adaptability]])

# =========================
# 4️⃣ PROBABILITY MODEL
# =========================
W = np.array([1.4,1.1,1.2,0.8,1.0,1.3,1.2,1.1,1.0,0.9, 1.3,1.0,1.4,1.2])
b = -4.2
z = np.dot(W, X_eng) + b
prob_like = 1 / (1 + np.exp(-z))

# =========================
# 5️⃣ TEA RECOMMENDATION
# =========================
tea_profiles = {
    "Masala Chai 🔥": np.array([0.9,0.4,0.6,0.6,0.8,0.9,0.7,0.7,0.6,0.5]),
    "Ginger Chai 🌿": np.array([0.7,0.3,0.6,0.5,0.6,0.8,0.6,0.5,0.5,0.5]),
    "Cardamom Chai 🍯": np.array([0.4,0.8,0.7,0.3,0.9,0.7,0.4,0.6,0.6,0.4]),
    "Classic Chai 🥛": np.array([0.3,0.6,0.9,0.3,0.5,0.8,0.3,0.5,0.8,0.5]),
    "Iced Chai 🧊": np.array([0.2,0.7,0.4,0.2,0.6,0.3,0.6,0.6,0.4,0.4])
}

def similarity(a,b):
    return np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))

best_tea = max(tea_profiles, key=lambda t: similarity(X, tea_profiles[t]))

# =========================
# 6️⃣ DISPLAY RESULTS
# =========================
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🔮 Reveal My Chai Profile", use_container_width=True):
    st.divider()

    col1, col2 = st.columns([1, 1.2], gap="large")

    # --- Left Column: Metrics & Tea Recommendation
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.markdown(f'<h2 style="color: white; font-size: 3.5rem; margin: 0;">{prob_like*100:.1f}%</h2>', unsafe_allow_html=True)
        st.markdown('<p style="color: rgba(255,255,255,0.9); font-size: 1.1rem; margin-top: 0.5rem;">Chai Compatibility Score</p>', unsafe_allow_html=True)
        verdict = "😍 Chai is made for you!" if prob_like > 0.7 else "🙂 You may enjoy chai" if prob_like > 0.45 else "😅 Chai may not suit your taste"
        st.markdown(f'<h3 style="color: white; margin-top: 1rem;">{verdict}</h3>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.markdown('<h3 style="color: #2d3748; margin-bottom: 1rem;">🫖 Your Perfect Match</h3>', unsafe_allow_html=True)
        st.success(best_tea)
        similarity_score = similarity(X, tea_profiles[best_tea])
        st.markdown(f'<p style="color: #718096; margin-top: 1rem;">Match Score: {similarity_score*100:.1f}%</p>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # --- Right Column: Radar Chart
    with col2:
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.markdown('<h3 style="color: #2d3748; margin-bottom: 1rem;">🧬 Your Flavor Personality</h3>', unsafe_allow_html=True)

        labels = ["Spice","Sweet","Dairy","Bitter","Aroma","Thermal","Novelty","Culture","Texture","Caffeine"]
        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
        fig.patch.set_facecolor('white')
        angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
        values = np.append(X, X[0])
        angles = np.append(angles, angles[0])
        
        # Enhanced radar chart styling
        ax.plot(angles, values, 'o-', linewidth=2.5, color='#667eea', label='Your Profile')
        ax.fill(angles, values, alpha=0.25, color='#764ba2')
        ax.set_thetagrids(angles[:-1]*180/np.pi, labels, fontsize=11, fontweight='600')
        ax.set_ylim(0, 1)
        ax.grid(color='#e2e8f0', linewidth=1.5)
        ax.set_facecolor('#fafafa')
        
        st.pyplot(fig)
        st.markdown("</div>", unsafe_allow_html=True)

    # --- Key Taste Drivers
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="result-box">', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #2d3748; margin-bottom: 1rem;">✨ Your Dominant Flavor Traits</h3>', unsafe_allow_html=True)
    drivers = [labels[i] for i,v in enumerate(X) if v > 0.65]
    if drivers:
        for d in drivers:
            st.markdown(f'<span class="tag">{d}</span>', unsafe_allow_html=True)
    else:
        st.markdown('<p style="color: #718096;">Your flavor profile is well-balanced across all traits!</p>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # --- Additional Insights
    st.markdown("<br>", unsafe_allow_html=True)
    col3, col4, col5 = st.columns(3)
    
    with col3:
        st.markdown('<div class="result-box" style="text-align: center;">', unsafe_allow_html=True)
        st.markdown(f'<h4 style="color: #667eea;">🎯 Flavor Complexity</h4>', unsafe_allow_html=True)
        st.markdown(f'<h2 style="color: #2d3748;">{flavor_complexity*100:.0f}%</h2>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="result-box" style="text-align: center;">', unsafe_allow_html=True)
        st.markdown(f'<h4 style="color: #667eea;">🌡️ Comfort Index</h4>', unsafe_allow_html=True)
        st.markdown(f'<h2 style="color: #2d3748;">{comfort_index*100:.0f}%</h2>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col5:
        st.markdown('<div class="result-box" style="text-align: center;">', unsafe_allow_html=True)
        st.markdown(f'<h4 style="color: #667eea;">🌍 Cultural Openness</h4>', unsafe_allow_html=True)
        st.markdown(f'<h2 style="color: #2d3748;">{cultural_adaptability*100:.0f}%</h2>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

