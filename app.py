import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# =========================
# 1️⃣ PAGE CONFIG + STYLING
# =========================
st.set_page_config("Chai Taste Intelligence v3", "🫖", layout="wide")

st.markdown("""
<style>
.main { padding: 2rem 4rem; }
h1 { margin-bottom: 0.2rem; }
.metric-card {
    background: #f7f7f7;
    border-radius: 16px;
    padding: 1.5rem;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
.result-box {
    background: #ffffff;
    border-radius: 16px;
    padding: 1.5rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
.tag {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 20px;
    background: #f1f3f5;
    margin-right: 6px;
    margin-top: 6px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🫖 Chai Taste Intelligence</h1>", unsafe_allow_html=True)
st.caption("AI-driven flavor profiling • Psychometric survey • Smart tea recommendation")
st.divider()

# =========================
# 2️⃣ PSYCHOMETRIC SURVEY
# =========================
st.header("📝 Flavor & Preference Survey")

def trait_block(title, questions):
    st.subheader(title)
    scores = [st.slider(q, 1, 10, 5) for q in questions]
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
if st.button("🔮 Reveal My Chai Profile"):
    st.divider()

    col1, col2 = st.columns([1, 1.2])

    # --- Left Column: Metrics & Tea Recommendation
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Chai Compatibility", f"{prob_like*100:.1f}%")
        verdict = "😍 Chai is made for you" if prob_like > 0.7 else "🙂 You may enjoy chai" if prob_like > 0.45 else "😅 Chai may not suit your taste"
        st.subheader(verdict)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.subheader("🫖 Recommended Tea")
        st.success(best_tea)
        st.markdown("</div>", unsafe_allow_html=True)

    # --- Right Column: Radar Chart
    with col2:
        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.subheader("🧬 Your Flavor Personality")

        labels = ["Spice","Sweet","Dairy","Bitter","Aroma","Thermal","Novelty","Culture","Texture","Caffeine"]
        fig, ax = plt.subplots(subplot_kw=dict(polar=True))
        angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
        values = np.append(X, X[0])
        angles = np.append(angles, angles[0])
        ax.plot(angles, values)
        ax.fill(angles, values, alpha=0.25)
        ax.set_thetagrids(angles[:-1]*180/np.pi, labels)
        ax.set_ylim(0,1)
        st.pyplot(fig)
        st.markdown("</div>", unsafe_allow_html=True)

    # --- Key Taste Drivers
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("✨ Key Taste Drivers")
    drivers = [labels[i] for i,v in enumerate(X) if v > 0.65]
    for d in drivers:
        st.markdown(f'<span class="tag">{d}</span>', unsafe_allow_html=True)

