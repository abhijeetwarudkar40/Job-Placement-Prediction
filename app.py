import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("placement_model.pkl", "rb"))

st.set_page_config(page_title="Placement Predictor", layout="centered")

st.title("🎓 Student Placement Prediction System")
st.markdown("### Enter Student Details")

#INPUTS
cgpa = st.slider("CGPA", 0.0, 10.0, 7.0)
internships = st.number_input("Internships Completed", 0, 10)
projects = st.number_input("Projects Completed", 0, 10)

coding = st.slider("Coding Skill Rating (1-10)", 1, 10, 5)
communication = st.slider("Communication Skill (1-10)", 1, 10, 5)
aptitude = st.slider("Aptitude Skill (1-10)", 1, 10, 5)

certifications = st.number_input("Certifications", 0, 10)
backlogs = st.number_input("Backlogs", 0, 10)

branch = st.selectbox("Branch", ["CSE", "IT", "ECE", "ME", "Other"])

#ENCODING
branch_CSE = 1 if branch == "CSE" else 0

#FEATURE ARRAY
features = np.array([[
    cgpa,
    internships,
    projects,
    coding,
    communication,
    aptitude,
    certifications,
    backlogs,
    branch_CSE
]])

#PREDICTION
if st.button("Predict Placement"):
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("✅ Student is likely to be Placed")
    else:
        st.error("❌ Student is NOT likely to be Placed")