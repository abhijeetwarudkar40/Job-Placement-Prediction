# 🎓 Student Placement Prediction System

## 📌 Overview

This project is a Machine Learning-based application that predicts whether a student is likely to be placed based on academic performance, skills, and other factors.

It uses a **Random Forest Classifier** trained on student data and provides predictions through an interactive user interface.

---

## 🚀 Features

* Predicts student placement (Placed / Not Placed)
* Uses real-world student attributes like CGPA, internships, skills, etc.
* Interactive UI built using **Streamlit**
* Feature selection for improved accuracy
* Model evaluation using accuracy and cross-validation

---

## 🧠 Machine Learning Model

* Algorithm: **Random Forest Classifier**
* Accuracy: ~89%
* Evaluation Metrics:

  * Accuracy Score
  * Cross Validation Score

---

## 📊 Features Used

* CGPA
* Internships Completed
* Projects Completed
* Coding Skill Rating
* Communication Skill Rating
* Aptitude Skill Rating
* Certifications Count
* Backlogs
* Branch

---

## 🛠️ Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit
* Matplotlib / Seaborn

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <https://github.com/abhijeetwarudkar40/Job-Placement-Prediction>
cd <project-folder>
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run app.py
```

### 4. Open in browser

```
http://localhost:8501
```

---

## 📁 Project Structure

```
project/
│── app.py
│── placement_model.pkl
│── Placement_Predictor.ipynb
│── README.md
```

---

## 📈 Future Improvements

* Add more features for better accuracy
* Deploy the app online
* Improve UI/UX design
* Use advanced models like XGBoost

---
