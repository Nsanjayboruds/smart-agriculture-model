import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
import os
from PIL import Image
import warnings
warnings.filterwarnings('ignore')

# ──────────────────────────────────────────
# Page Config
# ──────────────────────────────────────────
st.set_page_config(
    page_title="SmartFarm — Crop Recommendation",
    page_icon="🌾",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ──────────────────────────────────────────
# Custom CSS
# ──────────────────────────────────────────
st.markdown("""
<style>
/* ── Google Font ── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

/* ── Root Variables ── */
:root {
    --green-50:  #f0fdf4;
    --green-100: #dcfce7;
    --green-200: #bbf7d0;
    --green-400: #4ade80;
    --green-500: #22c55e;
    --green-600: #16a34a;
    --green-700: #15803d;
    --green-800: #166534;
    --green-900: #14532d;
    --amber-500: #f59e0b;
    --slate-50:  #f8fafc;
    --slate-100: #f1f5f9;
    --slate-200: #e2e8f0;
    --slate-600: #475569;
    --slate-700: #334155;
    --slate-800: #1e293b;
    --slate-900: #0f172a;
}

/* ── Global ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
}

.stApp {
    background: linear-gradient(165deg, #f0fdf4 0%, #ecfdf5 30%, #f0f9ff 70%, #f8fafc 100%);
}

/* ── Hide default Streamlit elements ── */
#MainMenu, footer, header {visibility: hidden;}
.stDeployButton {display: none;}

/* ── Hero Header ── */
.hero {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem;
}
.hero-icon {
    font-size: 3.5rem;
    margin-bottom: 0.25rem;
    display: inline-block;
    animation: float 3s ease-in-out infinite;
}
@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-8px); }
}
.hero h1 {
    font-size: 2rem;
    font-weight: 800;
    color: var(--green-800);
    margin: 0.25rem 0 0.5rem;
    letter-spacing: -0.5px;
}
.hero p {
    font-size: 1.05rem;
    color: var(--slate-600);
    max-width: 520px;
    margin: 0 auto;
    line-height: 1.6;
}

/* ── Section Labels ── */
.section-label {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.85rem;
    font-weight: 600;
    color: var(--green-700);
    text-transform: uppercase;
    letter-spacing: 1.2px;
    margin-bottom: 0.75rem;
    padding-left: 2px;
}
.section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, var(--green-200), transparent);
}

/* ── Input Cards ── */
div[data-testid="stNumberInput"] label {
    font-weight: 500 !important;
    color: var(--slate-700) !important;
    font-size: 0.9rem !important;
}

/* ── Prediction Button ── */
div.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, var(--green-600), var(--green-700)) !important;
    color: white !important;
    border: none !important;
    padding: 0.85rem 2rem !important;
    font-size: 1.1rem !important;
    font-weight: 700 !important;
    border-radius: 12px !important;
    letter-spacing: 0.3px;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 14px rgba(22, 163, 74, 0.35) !important;
    margin-top: 0.5rem;
}
div.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(22, 163, 74, 0.45) !important;
    background: linear-gradient(135deg, var(--green-500), var(--green-600)) !important;
}
div.stButton > button:active {
    transform: translateY(0) !important;
}

/* ── Result Card ── */
.result-card {
    background: linear-gradient(135deg, var(--green-50), #ffffff);
    border: 2px solid var(--green-200);
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    margin-top: 1.5rem;
    animation: slideUp 0.5s ease-out;
    box-shadow: 0 8px 30px rgba(22, 163, 74, 0.1);
}
@keyframes slideUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}
.result-emoji {
    font-size: 4rem;
    margin-bottom: 0.5rem;
    display: inline-block;
    animation: pop 0.4s ease-out 0.2s both;
}
@keyframes pop {
    from { transform: scale(0); }
    50% { transform: scale(1.2); }
    to { transform: scale(1); }
}
.result-label {
    font-size: 0.85rem;
    color: var(--slate-600);
    text-transform: uppercase;
    letter-spacing: 1.5px;
    font-weight: 600;
    margin-bottom: 0.25rem;
}
.result-crop {
    font-size: 2.2rem;
    font-weight: 800;
    color: var(--green-700);
    margin: 0.25rem 0;
    letter-spacing: -0.5px;
}
.result-note {
    font-size: 0.9rem;
    color: var(--slate-600);
    margin-top: 0.75rem;
    line-height: 1.5;
}

/* ── Divider ── */
.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--green-200), transparent);
    margin: 2rem 0;
}

/* ── Footer ── */
.app-footer {
    text-align: center;
    padding: 1.5rem 0 1rem;
    color: var(--slate-600);
    font-size: 0.8rem;
}
.app-footer a {
    color: var(--green-600);
    text-decoration: none;
    font-weight: 600;
}

/* ── Expander styling ── */
div[data-testid="stExpander"] {
    border: 1px solid var(--green-200) !important;
    border-radius: 12px !important;
    background: white !important;
}
</style>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────
# Crop → Emoji Mapping
# ──────────────────────────────────────────
CROP_EMOJI = {
    "rice": "🌾", "wheat": "🌾", "maize": "🌽", "corn": "🌽",
    "chickpea": "🫘", "kidneybeans": "🫘", "pigeonpeas": "🫛",
    "mothbeans": "🫘", "mungbean": "🫛", "blackgram": "🫘", "lentil": "🫘",
    "pomegranate": "🍎", "banana": "🍌", "mango": "🥭",
    "grapes": "🍇", "watermelon": "🍉", "muskmelon": "🍈",
    "apple": "🍏", "orange": "🍊", "papaya": "🥭",
    "coconut": "🥥", "cotton": "🧶", "jute": "🪢", "coffee": "☕",
}

CROP_TIPS = {
    "rice": "Thrives in warm, humid climates with plenty of water.",
    "maize": "Prefers well-drained soils with moderate rainfall.",
    "chickpea": "Grows best in cool, dry conditions with loamy soil.",
    "kidneybeans": "Needs moderate temperatures and well-drained soil.",
    "pigeonpeas": "Drought-tolerant; suited for semi-arid regions.",
    "mothbeans": "Extremely drought-resistant; ideal for arid zones.",
    "mungbean": "Short growing season; prefers warm weather.",
    "blackgram": "Grows well in both kharif and summer seasons.",
    "lentil": "Cool-season crop; thrives in well-drained loamy soil.",
    "pomegranate": "Loves hot, dry summers and well-drained soil.",
    "banana": "Requires tropical climate with consistent moisture.",
    "mango": "Best in tropical/subtropical regions with dry winters.",
    "grapes": "Prefers warm days, cool nights, and well-drained soil.",
    "watermelon": "Needs long warm seasons and sandy loam soil.",
    "muskmelon": "Thrives in hot weather with moderate humidity.",
    "apple": "Requires cold winters for proper dormancy (chilling hours).",
    "orange": "Subtropical fruit; needs warm days and cool nights.",
    "papaya": "Fast-growing tropical fruit; frost-sensitive.",
    "coconut": "Coastal tropical crop; loves humidity and sandy soil.",
    "cotton": "Warm-season crop; needs 6+ months of frost-free weather.",
    "jute": "Requires warm, humid climate with heavy rainfall.",
    "coffee": "Grows best in tropical highlands with shade.",
}


def get_crop_emoji(crop_name):
    return CROP_EMOJI.get(crop_name.lower(), "🌱")


def get_crop_tip(crop_name):
    return CROP_TIPS.get(crop_name.lower(), "A great choice for your soil and climate conditions!")


# ──────────────────────────────────────────
# Load Data & Model  (cached)
# ──────────────────────────────────────────
@st.cache_data
def load_data():
    csv_path = os.path.join(os.path.dirname(__file__), 'Crop_recommendation.csv')
    if not os.path.exists(csv_path):
        st.error("❌ Dataset file not found.")
        st.stop()
    return pd.read_csv(csv_path)


@st.cache_resource
def load_model(df):
    model_path = os.path.join(os.path.dirname(__file__), 'RF.pkl')
    X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
    y = df['label']
    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        return model
    except Exception:
        Xtrain, _, Ytrain, _ = train_test_split(X, y, test_size=0.3, random_state=42)
        model = RandomForestClassifier(n_estimators=20, random_state=5)
        model.fit(Xtrain, Ytrain)
        with open(model_path, 'wb') as f:
            pickle.dump(model, f)
        return model


df = load_data()
model = load_model(df)

# ──────────────────────────────────────────
# Hero Section
# ──────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-icon">🌾</div>
    <h1>Crop Recommendation</h1>
    <p>Enter your soil nutrients and weather conditions below — our AI model will recommend the best crop for your farm.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ──────────────────────────────────────────
# Input Section — Soil Nutrients
# ──────────────────────────────────────────
st.markdown('<div class="section-label">🧪 Soil Nutrients</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    nitrogen = st.number_input("Nitrogen (N)", min_value=0.0, max_value=140.0, value=50.0, step=1.0, help="Ratio of nitrogen content in soil")
with col2:
    phosphorus = st.number_input("Phosphorus (P)", min_value=0.0, max_value=145.0, value=50.0, step=1.0, help="Ratio of phosphorus content in soil")
with col3:
    potassium = st.number_input("Potassium (K)", min_value=0.0, max_value=205.0, value=50.0, step=1.0, help="Ratio of potassium content in soil")

st.markdown("")

# ──────────────────────────────────────────
# Input Section — Weather Conditions
# ──────────────────────────────────────────
st.markdown('<div class="section-label">🌤️ Weather & Environment</div>', unsafe_allow_html=True)

col4, col5 = st.columns(2)
with col4:
    temperature = st.slider("🌡️ Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0, step=0.5)
with col5:
    humidity = st.slider("💧 Humidity (%)", min_value=0.0, max_value=100.0, value=50.0, step=0.5)

col6, col7 = st.columns(2)
with col6:
    ph = st.slider("⚗️ Soil pH Level", min_value=0.0, max_value=14.0, value=6.5, step=0.1)
with col7:
    rainfall = st.number_input("🌧️ Rainfall (mm)", min_value=0.0, max_value=500.0, value=100.0, step=1.0, help="Average rainfall in mm")

st.markdown("")

# ──────────────────────────────────────────
# Predict Button
# ──────────────────────────────────────────
predict_clicked = st.button("🌾  Get Crop Recommendation")

# ──────────────────────────────────────────
# Result Display
# ──────────────────────────────────────────
if predict_clicked:
    input_data = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)[0]
    emoji = get_crop_emoji(prediction)
    tip = get_crop_tip(prediction)

    st.markdown(f"""
    <div class="result-card">
        <div class="result-emoji">{emoji}</div>
        <div class="result-label">Recommended Crop</div>
        <div class="result-crop">{prediction.capitalize()}</div>
        <div class="result-note">💡 {tip}</div>
    </div>
    """, unsafe_allow_html=True)

    # Show input summary
    st.markdown("")
    with st.expander("📋 Your Input Summary"):
        summary_df = pd.DataFrame({
            "Parameter": ["Nitrogen", "Phosphorus", "Potassium", "Temperature", "Humidity", "pH", "Rainfall"],
            "Value": [nitrogen, phosphorus, potassium, f"{temperature}°C", f"{humidity}%", ph, f"{rainfall} mm"],
            "Icon": ["🧪", "🧪", "🧪", "🌡️", "💧", "⚗️", "🌧️"]
        })
        st.dataframe(summary_df, hide_index=True, use_container_width=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ──────────────────────────────────────────
# Dataset Preview
# ──────────────────────────────────────────
with st.expander("📊 Explore Training Dataset"):
    st.dataframe(df.head(15), hide_index=True, use_container_width=True)
    st.caption(f"Dataset contains **{len(df):,}** samples across **{df['label'].nunique()}** crop types.")

# ──────────────────────────────────────────
# Footer
# ──────────────────────────────────────────
st.markdown("""
<div class="app-footer">
    Built with 💚 by <a href="#">Team SmartFarm</a> · Powered by Random Forest ML
</div>
""", unsafe_allow_html=True)
