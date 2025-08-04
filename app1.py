import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# ----------------- Page Setup -----------------
st.set_page_config(
    page_title="Food Waste Predictor",
    layout="centered",
    initial_sidebar_state="auto",
    page_icon="🍽️"
)

# ----------------- Dark Theme + Background -----------------
st.markdown("""
    <style>
    /* Set background image */
    .stApp {
        background-image: url('https://i.pinimg.com/736x/4c/4c/10/4c4c107c7d98edc0d036534f4c652de5.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: #ffffff;
    }

  .stMarkdown, .stSlider, .stSelectbox, .stNumberInput {
        background-color: rgba(0, 0, 0, 0.6) !important;
        padding: 10px;
        border-radius: 10px;
        color: white !important;
    }

    /* Title */
    h1, h3, h5 {
        color: #00ffcc !important;
    }

    /* Predict button highlight */
    div.stButton > button {
        background-color: #00b894;
        color: white;
        border-radius: 10px;
        height: 3em;
        font-weight: bold;
        width: 100%;
        transition: background-color 0.3s ease;
    }

    div.stButton > button:hover {
        background-color: #00cec9;
        color: black;
    }
     label {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- Title -----------------
st.markdown("<h1 style='text-align: center;'>🍽️ Smart Food Waste Prediction</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>Reduce waste, optimize cafeteria performance</h5>", unsafe_allow_html=True)
st.markdown("---")

# ----------------- Input Section -----------------
st.markdown("### 📋 Enter Cafeteria Details")

col1, col2 = st.columns(2)

with col1:
    meals_served = st.number_input("🍱 Meals Served", min_value=50, max_value=5000, value=250)
    kitchen_staff = st.number_input("👨‍🍳 Kitchen Staff", min_value=1, max_value=20, value=10)
    temperature_C = st.slider("🌡️ Temperature (°C)", 5.0, 40.0, 25.0)
    humidity_percent = st.slider("💧 Humidity (%)", 30.0, 90.0, 60.0)

with col2:
    day_of_week = st.selectbox("📅 Day of Week", list(range(7)),
                               format_func=lambda x: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][x])
    special_event = st.selectbox("🎉 Special Event", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    past_waste_kg = st.number_input("♻️ Past Waste (kg)", min_value=0.0, max_value=100.0, value=25.0)
    staff_experience = st.selectbox("🧠 Staff Experience", ["beginner", "intermediate", "expert"])
    waste_category = st.selectbox("🗑️ Waste Category", ["dairy", "grains", "meat", "vegetables"])

st.markdown("---")

# ----------------- Prediction -----------------
if st.button("🔍 Predict Food Waste", use_container_width=True):
    input_df = pd.DataFrame([{
        "meals_served": meals_served,
        "kitchen_staff": kitchen_staff,
        "temperature_C": np.clip(temperature_C, 5, 40),
        "humidity_percent": humidity_percent,
        "day_of_week": day_of_week,
        "special_event": special_event,
        "past_waste_kg": past_waste_kg,
        "staff_experience_expert": int(staff_experience == "expert"),
        "staff_experience_intermediate": int(staff_experience == "intermediate"),
        "waste_category_grains": int(waste_category == "grains"),
        "waste_category_meat": int(waste_category == "meat"),
        "waste_category_vegetables": int(waste_category == "vegetables"),
    }])

    # Scale numeric fields
    numeric_cols = ['meals_served', 'kitchen_staff', 'temperature_C',
                    'humidity_percent', 'past_waste_kg']
    input_df[numeric_cols] = scaler.transform(input_df[numeric_cols])

    # Predict
    prediction = model.predict(input_df)[0]

    # Result Card
    st.markdown(f"""
    <div style='padding: 20px; border-radius: 10px; background-color: rgba(0,255,128,0.1); text-align: center; border: 2px solid #00e676;'>
        <h3 style='color: #00e676;'>📦 Estimated Food Waste:</h3>
        <h1 style='color: #00ffcc;'>{prediction:.2f} kg</h1>
    </div>
    """, unsafe_allow_html=True)

# ----------------- Footer -----------------
st.markdown("---")
st.markdown("<p style='text-align: center; color: #ccc;'>Made with ❤️ by Melani Dahanayaka</p>", unsafe_allow_html=True)
