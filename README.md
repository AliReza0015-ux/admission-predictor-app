#  UCLA Admission Predictor

This project predicts the likelihood of admission to UCLA based on academic metrics using a neural network model.

##  Features

- Input GRE, TOEFL, SOP, LOR, CGPA, and Research Experience
- Streamlit web app with intuitive UI
- Predicts admission (0 = Not Admitted, 1 = Admitted)

## Dataset

The model was trained on the [Admission.csv](Admission.csv) dataset, containing anonymized records of past applicants with the following features:
- GRE Score
- TOEFL Score
- University Rating
- SOP
- LOR
- CGPA
- Research (Yes/No)

##  How to Run

### Local
```bash
git clone https://github.com/AliReza0015-ux/admission-predictor-app.git
cd admission-predictor-app
pip install -r requirements.txt
streamlit run app.py
Cloud
Hosted on Streamlit Cloud
Launch App
 Model
•	MLPClassifier from sklearn.neural_network
•	Hidden layers: 100 units
•	Trained using StandardScaler normalized features
 File Structure
├── app.py               # Streamlit frontend
├── model.py             # Model loading and prediction
├── admission_model.pkl  # Trained model
├── requirements.txt     # Python dependencies
└── README.md            # Project summary
 Author
Mohammad Alireza
Student, CST2216, Algonquin College
GitHub: @AliReza0015-ux
