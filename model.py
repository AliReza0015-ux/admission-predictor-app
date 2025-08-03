import joblib

def load_model():
    return joblib.load("admission_model.pkl")

def predict_admission(model, input_df):
    # Ensure the input columns match the training data
    expected_cols = ['GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR', 'CGPA', 'Research']
    input_df = input_df[expected_cols]
    return model.predict(input_df)[0]
