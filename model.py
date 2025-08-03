import joblib

def load_model(path="model/admission_model.pkl"):
    return joblib.load(path)

def predict_admission(model, input_df):
    return model.predict(input_df)[0]
