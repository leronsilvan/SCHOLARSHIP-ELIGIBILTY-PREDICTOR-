import streamlit as st
import pickle
import numpy as np
import os

# Page title
st.set_page_config(page_title="Scholar Outcome Predictor", layout="centered")
st.title("🎓 Scholar Outcome Predictor")
st.markdown("Fill the form below to predict if the scholar will have a successful outcome.")

# Load model
model_path = "Scholarship.pkl"
if not os.path.exists(model_path):
    st.error("❌ Model file not found. Please ensure 'model.pkl' is in the same folder.")
    st.stop()

model = pickle.load(open(model_path, "rb"))

# Input fields
schlarship_name=st.selectbox("Name",["INSPIRE Scholarship 2022-23 ? Scholarship for Higher Education (SHE)",
 'Abdul Kalam Technology Innovation National Fellowship',
 'AAI Sports Scholarship Scheme in India 2022-23',
 'Glow and lovely Career Foundation Scholarship',
 'National Fellowship for Persons with Disabilities',
 'ONGC Sports Scholarship Scheme 2022-23',
 'Pragati Scholarship ? AICTE-Scholarship Scheme to Girl Child',
 'Dr. Ambedkar post matric Scholarship',
 'Indira Gandhi Scholarship for Single Girl Child UGC Scholarship for PG Programmes',
 "National Overseas Scholarship Scheme 2021-22"])
edu_qual = st.selectbox("Education Qualification", ["Undergraduate"])
gender = st.selectbox("Gender", ["Male", "Female"])
community = st.selectbox("Community", ["General", "OBC", "SC", "ST"])
religion = st.selectbox("Religion", ["Hindu", "Muslim", "Christian", "Other"])
exservice = st.selectbox("Ex-Service Men", ["Yes", "No"])
disability = st.selectbox("Disability", ["Yes", "No"])
sports = st.selectbox("Sports Participation", ["Yes", "No"])
percentage = st.selectbox("Annual Percentage", ["Below 60", "60-70", "70-80", "80-90", "90-100"])
income = st.selectbox("Family Income", ["Upto 1.5L", "1.5L-3L", "3L-6L", "6L+"])
country=st.selectbox("India", ["In", 'Out'])

# Encode input
def encode_input():
    mapping = {
        "Name":{"INSPIRE Scholarship 2022-23 ? Scholarship for Higher Education (SHE)":0,
        'Abdul Kalam Technology Innovation National Fellowship':1,
        'AAI Sports Scholarship Scheme in India 2022-23':2,
        'Glow and lovely Career Foundation Scholarship':3,
        'National Fellowship for Persons with Disabilities':4,
        'ONGC Sports Scholarship Scheme 2022-23':5,
        'Pragati Scholarship ? AICTE-Scholarship Scheme to Girl Child':6,
        'Dr. Ambedkar post matric Scholarship':7,
        'Indira Gandhi Scholarship for Single Girl Child UGC Scholarship for PG Programmes':8,
        "National Overseas Scholarship Scheme 2021-22":9},
        "Education Qualification": {"Undergraduate": 0},
        "Gender": {"Male": 1, "Female": 0},
        "Community": {"General": 0, "OBC": 1, "SC": 2, "ST": 3},
        "Religion": {"Hindu": 0, "Muslim": 1, "Christian": 2, "Other": 3},
        "Exservice-men": {"Yes": 1, "No": 0},
        "Disability": {"Yes": 1, "No": 0},
        "Sports": {"Yes": 1, "No": 0},
        "Annual-Percentage": {
            "Below 60": 0, "60-70": 1, "70-80": 2, "80-90": 3, "90-100": 4
        },
        "Income": {
            "Upto 1.5L": 0, "1.5L-3L": 1, "3L-6L": 2, "6L+": 3
        },
        "India":{"In":0,"Out":1}
    }

    return np.array([[
        mapping["Name"][schlarship_name],
        mapping["Education Qualification"][edu_qual],
        mapping["Gender"][gender],
        mapping["Community"][community],
        mapping["Religion"][religion],
        mapping["Exservice-men"][exservice],
        mapping["Disability"][disability],
        mapping["Sports"][sports],
        mapping["Annual-Percentage"][percentage],
        mapping["Income"][income],
        mapping["India"][country]
    ]])

# Prediction
if st.button("Predict"):
    features = encode_input()
    prediction = model.predict(features)[0]

    if prediction == 1:
        st.success("✅ Scholarship Eligible.")
    else:
        st.error("❌ Scolarship Not Eligible.")