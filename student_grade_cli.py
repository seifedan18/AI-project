import joblib
import numpy as np

# Load the trained model, scaler, and feature names
def load_artifacts():
    model = joblib.load('student_grade_model.pkl')
    scaler = joblib.load('scaler.pkl')
    feature_names = joblib.load('feature_names.pkl')
    return model, scaler, feature_names

def get_user_input(feature_names):
    print('Enter student features as prompted:')
    user_data = []
    for feature in feature_names:
        value = input(f'{feature}: ')
        try:
            value = float(value)
        except ValueError:
            pass  # Keep as string if not convertible
        user_data.append(value)
    return np.array(user_data).reshape(1, -1)

def main():
    model, scaler, feature_names = load_artifacts()
    user_input = get_user_input(feature_names)
    user_input_scaled = scaler.transform(user_input)
    prediction = model.predict(user_input_scaled)[0]
    result = 'PASS' if prediction == 1 else 'FAIL'
    print(f'Prediction: {result}')

if __name__ == '__main__':
    main()
