# ❤️ Heart Disease Prediction Using Machine Learning

This project uses various machine learning algorithms to predict the presence of heart disease based on patient clinical data. It includes data preprocessing, model training, and performance evaluation using popular classifiers such as Naive Bayes, SVM, Logistic Regression, Random Forest, K-Nearest Neighbors, and Decision Tree.

---

## 📁 Dataset

- **File Used**: `hearts.csv`
- **Features**:
  - Gender
  - ChestPainType
  - RestingECG
  - ExerciseAngina
  - ST_Slope
  - and other numerical medical attributes
- **Target Variable**: `HeartDisease` (0 = No, 1 = Yes)

---

## 🔧 Technologies & Libraries

- **Language**: Python
- **Libraries**:
  - `pandas` – Data manipulation
  - `numpy` – Numerical operations
  - `scikit-learn` – Machine learning models & preprocessing
  - `warnings` – Suppress warnings

---

## ⚙️ Installation

```bash
pip install pandas numpy scikit-learn
**
## 🧠 Machine Learning Models Used

1. **Gaussian Naive Bayes**
2. **Support Vector Machine (SVM)**
3. **Logistic Regression**
4. **Random Forest Classifier**
5. **K-Nearest Neighbors (KNN)**
6. **Decision Tree Classifier**



📊 Model Evaluation
All models are evaluated using accuracy score on a test set (20% of the data). Each model's performance is printed in the console.

Output:
GaussionNB Accuracy is 0.85
SVC Accuracy is 0.89
LogisticRegression Accuracy is 0.88
RandomForestClassifier Accuracy is 0.91
KNeighborsClassifier Accuracy is 0.86
DecisionTreeClassifier Accuracy is 0.87


📂 Project Structure
heart-disease-prediction/
├── hearts.csv
├── heart_disease_prediction.py
├── README.md




