# 🎓 Student Placement Prediction System

## 📌 Overview

This project is a Machine Learning-based application that predicts whether a student is likely to be placed based on academic performance, skills, and other factors.

## 📌 Overview

This project is a **Machine Learning-based system** that predicts:

* ✅ **Student Placement Status** (Placed / Not Placed)
* 💰 **Expected Salary (LPA)**

It uses real-world student data including academic performance, skills, and activities.

---

## 🚀 Features

* 🎯 Placement Prediction using **Random Forest Classifier**
* 💰 Salary Prediction using **Regression Model**
* 📈 Placement Probability Visualization
* 🧠 Feature Engineering (skill_score, profile_score)
* 🖥️ Interactive UI using **Streamlit**

---

## 🧠 Machine Learning Models

### 🔹 Placement Model

* Algorithm: Random Forest Classifier
* Accuracy: ~89%
* Output: Placement + Probability

### 🔹 Salary Model

* Algorithm: XGBoost Regressor
* R² Score: ~0.77
* Output: Salary in LPA

---

## 📊 Features Used

### Placement Features:

* CGPA
* Internships
* Projects
* Coding Skill
* Communication Skill
* Aptitude
* Certifications
* Backlogs
* Branch (CSE)

### Salary Features:

* CGPA
* 10th Percentage
* 12th Percentage
* Internships & Projects
* Skills (Coding, Communication, Aptitude)
* Certifications & Hackathons
* Attendance
* Branch
* Engineered Features (skill_score, profile_score)

---

## 🛠️ Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* XGBoost
* Streamlit
* Matplotlib / Seaborn

---

## ▶️ How to Run

### 1️⃣ Clone the repository

```
git clone https://github.com/abhijeetwarudkar40/Job-Placement-Prediction.git
cd Job-Placement-Prediction
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the application

```
streamlit run app.py
```

### 4️⃣ Open in browser

```
http://localhost:8501
```

---

## 📁 Project Structure

```
Job-Placement-Prediction/
│── app.py
│── placement_model.pkl
│── salary_model.pkl
│── notebook.ipynb
│── requirements.txt
│── README.md
```

---

## 📈 Results

* Placement Model Accuracy: **~89%**
* Salary Model R² Score: **~0.77**
* MAE: ~1 LPA

---

## 🔮 Future Improvements

* Add more real-world features (company, location)
* Improve salary prediction accuracy
* Deploy app online (Streamlit Cloud)
---
