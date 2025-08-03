import pandas as pd

def preprocess_input(gre, toefl, rating, sop, lor, cgpa, research):
    return pd.DataFrame([{
        "GRE Score": gre,
        "TOEFL Score": toefl,
        "University Rating": rating,
        "SOP": sop,
        "LOR": lor,
        "CGPA": cgpa,
        "Research": research
    }])
