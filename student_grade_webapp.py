import streamlit as st
import joblib
import numpy as np

# Load model, scaler, and feature names
def load_artifacts():
    model = joblib.load('student_grade_model.pkl')
    scaler = joblib.load('scaler.pkl')
    feature_names = joblib.load('feature_names.pkl')
    return model, scaler, feature_names

# Add a sidebar with project info
st.sidebar.title('About')
st.sidebar.info('''\
**Student Grade Classifier**

Predict whether a student will PASS or FAIL based on 15 important features. Built for the Fundamentals of AI course.\n\nDeveloped with scikit-learn & Streamlit.
''')

# Update the header to match the desired futuristic design
st.markdown('''
    <style>
        body {
            background-color: #0d1117;
            color: #c9d1d9;
        }
        .main-header {
            background: linear-gradient(90deg, #6f42c1 0%, #8a63d2 100%);
            padding: 30px 10px;
            border-radius: 20px;
            margin-bottom: 30px;
            box-shadow: 0 8px 20px rgba(111, 66, 193, 0.2);
        }
        .main-header h2 {
            color: white;
            text-align: center;
            font-size: 2.5rem;
            margin: 0;
            font-weight: bold;
        }
        .feature-list {
            background: #161b22;
            border-radius: 10px;
            padding: 15px 20px;
            margin-bottom: 20px;
            font-size: 1.1rem;
            color: #8b949e;
        }
        .stButton>button {
            background: linear-gradient(90deg, #6f42c1 0%, #8a63d2 100%);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 0.8em 2.5em;
            font-size: 1.2rem;
            font-weight: bold;
            margin-top: 15px;
            box-shadow: 0 4px 12px rgba(111, 66, 193, 0.3);
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .stButton>button:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 16px rgba(111, 66, 193, 0.4);
        }
        .input-card {
            background: #161b22;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 4px 16px rgba(24, 24, 27, 0.2);
        }
    </style>
    <div class="main-header"><h2>Student Grade Classifier</h2></div>
''', unsafe_allow_html=True)

model, scaler, feature_names = load_artifacts()

# Update the input card and feature list to match the futuristic design
st.markdown('<div class="input-card">', unsafe_allow_html=True)
st.markdown('<div class="feature-list"><b>Features used for prediction:</b><br>' + ', '.join(feature_names) + '</div>', unsafe_allow_html=True)

# Create input fields for each feature
# Update input fields to leave Yes/No radio buttons unselected by default
user_input = []
for feature in feature_names:
    if feature in ['G1', 'G2', 'age']:
        value = st.number_input(f'{feature}', min_value=0, max_value=20 if feature.startswith('G') else 25, value=0, key=feature)  # Default to 0
    elif feature in ['Walc']:
        value = st.slider(f'{feature} (1=very low, 5=very high)', 1, 5, key=feature)  # No default value selected
    else:
        value = st.radio(f'{feature}', [None, 0, 1], format_func=lambda x: 'Yes' if x == 1 else ('No' if x == 0 else 'Select'), horizontal=True, key=feature)  # Default to unselected
    user_input.append(value if value is not None else 0)  # Treat unselected as 0

if st.button('Predict'):
    X = np.array(user_input).reshape(1, -1)
    X_scaled = scaler.transform(X)
    prediction = model.predict(X_scaled)[0]
    result = 'PASS' if prediction == 1 else 'FAIL'
    st.success(f'Prediction: {result}')

st.markdown('</div>', unsafe_allow_html=True)

# Update the footer to match the futuristic design
st.markdown('<hr style="margin-top:30px;">', unsafe_allow_html=True)
st.markdown('<div style="text-align:center;color:#8b949e;font-size:14px;">Fundamentals of AI Project &copy; 2025</div>', unsafe_allow_html=True)
