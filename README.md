# Food Waste Prediction System 🍽️

## Overview
The **Food Waste Prediction System** is a web-based application designed to predict food waste in restaurants, hotels, and institutions using **machine learning**. The system helps managers reduce waste, optimize inventory, and improve sustainability.

The project uses **Random Forest** as the primary machine learning algorithm, along with data preprocessing, feature engineering, and evaluation metrics like **MAE** (Mean Absolute Error) for prediction accuracy.

---

## Features
- Predict food waste (kg) based on factors like:
  - Temperature
  - Meals served
  - Staff experience
  - Inventory and ingredients
- Compare different machine learning models (Random Forest, Decision Tree, ANN)
- Display predicted waste with visualizations
- User-friendly web interface built with **Streamlit**

---

## Technologies Used
- Python 3.x
- Streamlit (Web Interface)
- Pandas, NumPy (Data handling)
- Scikit-learn (Machine Learning)
- Matplotlib & Seaborn (Visualizations)

---
## Run Application
streamlit run app.py
Model Evaluation

Random Forest selected as the best model based on performance.

Metrics used: MAE, RMSE, R² score.

Allows comparison with Decision Tree and ANN models.

Future Enhancements

Add real-time data input for restaurants.

Include advanced ML models (XGBoost, LightGBM).

Integrate alerts and notifications for excessive waste.

Expand dataset with regional and seasonal variations.
