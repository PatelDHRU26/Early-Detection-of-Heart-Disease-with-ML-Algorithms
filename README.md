# ❤️ Heart Disease Prediction Using Machine Learning

This project is a machine learning-based web application that predicts the likelihood of heart disease using patient health data. It uses several ML models and provides a simple frontend built with **Streamlit** for user interaction.

---

## 📌 Features

- Predicts heart disease using health indicators like age, blood pressure, cholesterol, etc.
- User-friendly web interface built with **Streamlit**
- Trained using multiple ML models:
  - **Gaussian Naive Bayes**
  - **Support Vector Machine**
  - **Logistic Regression**
  - **Random Forest**
  - **K-Nearest Neighbors**
  - **Decision Tree**

---

## 🧠 Machine Learning Models Used

- **Gaussian Naive Bayes**
- **Support Vector Machine (SVM)**
- **Logistic Regression**
- **Random Forest Classifier**
- **K-Nearest Neighbors**
- **Decision Tree**

---

## 📁 Project Structure

```
Heart_Disease_Prediction/
├── app.py                # Streamlit frontend
├── model.pkl             # Trained Random Forest model
├── hearts.csv            # Dataset
├── training_script.py    # Python code to train the model
└── README.md             # This file
```

---

## 💻 How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/heart-disease-prediction.git
cd heart-disease-prediction
```

### Step 2: Install Required Libraries

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install pandas numpy scikit-learn streamlit
```

### Step 3: Run the Web App

```bash
streamlit run app.py
```

---

## 📊 Inputs Used for Prediction

- Age
- Gender
- Resting Blood Pressure
- Cholesterol
- Chest Pain Type
- Resting ECG
- Maximum Heart Rate
- Exercise-Induced Angina
- Oldpeak
- ST Slope
- Fasting Blood Sugar

---

## ✅ Output

- Displays: **“Positive for Heart Disease”** or **“No Heart Disease”**

---

## 🛠️ Tools & Libraries

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit

---

## 🙌 Credits

Dataset from [Kaggle: Heart Disease UCI](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)

---

## 📌 License

This project is open source and free to use under the MIT License.
