import streamlit as st
from model import load_model, predict_admission
from utils import preprocess_input

def main():
    st.title("🎓 UCLA Admission Predictor")

    gre = st.number_input("GRE Score", 0, 340)
    toefl = st.number_input("TOEFL Score", 0, 120)
    rating = st.selectbox("University Rating", [1, 2, 3, 4, 5])
    sop = st.slider("Statement of Purpose (SOP)", 1.0, 5.0, step=0.5)
    lor = st.slider("Letter of Recommendation (LOR)", 1.0, 5.0, step=0.5)
    cgpa = st.number_input("CGPA", 0.0, 10.0, step=0.1)
    research = st.selectbox("Research Experience", [0, 1])

    if st.button("Predict Admission"):
        input_df = preprocess_input(gre, toefl, rating, sop, lor, cgpa, research)
        model = load_model()
        result = predict_admission(model, input_df)
        st.success(f"🎯 Admission Status: {result} (1 = Admitted, 0 = Not Admitted)")

if __name__ == '__main__':
    main()
