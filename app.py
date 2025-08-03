import streamlit as st
import pandas as pd
from model import load_model, predict_admission

def main():
    st.title("🎓 UCLA Admission Predictor")

    st.subheader("Enter Your Academic Profile:")

    gre = st.number_input("GRE Score", min_value=0, max_value=340)
    toefl = st.number_input("TOEFL Score", min_value=0, max_value=120)
    university_rating = st.selectbox("University Rating", [1, 2, 3, 4, 5])
    sop = st.slider("Statement of Purpose (SOP)", 1.0, 5.0, 3.0, step=0.5)
    lor = st.slider("Letter of Recommendation (LOR)", 1.0, 5.0, 3.0, step=0.5)
    cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1)
    research = st.selectbox("Research Experience", ["No", "Yes"])

    if st.button("Predict Admission"):
        try:
            research_binary = 1 if research == "Yes" else 0

            input_df = pd.DataFrame([{
                "GRE Score": gre,
                "TOEFL Score": toefl,
                "University Rating": university_rating,
                "SOP": sop,
                "LOR": lor,
                "CGPA": cgpa,
                "Research": research_binary
            }])

            model = load_model()
            result = predict_admission(model, input_df)

            st.success(f"🎯 Admission Prediction: {'✅ Likely Admitted' if result == 1 else '❌ Not Admitted'}")

        except Exception as e:
            st.error(f"Something went wrong: {e}")

if __name__ == '__main__':
    main()
