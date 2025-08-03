import pandas as pd

def preprocess_input(gre, toefl, university_rating, sop, lor, cgpa, research):
    data = {
        "GRE Score": [gre],
        "TOEFL Score": [toefl],
        "University Rating": [university_rating],
        "SOP": [sop],
        "LOR": [lor],
        "CGPA": [cgpa],
        "Research": [research]
    }
    return pd.DataFrame(data)
