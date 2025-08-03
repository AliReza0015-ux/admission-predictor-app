import joblib

def load_model():
    return joblib.load("admission_model.pkl")

def predict_admission(model, input_df):
    expected_cols = ["GRE_Score", "TOEFL_Score", "University_Rating", "SOP", "LOR", "CGPA", "Research"]
    input_df = input_df[expected_cols]
    return model.predict(input_df)[0]
