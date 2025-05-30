# Final Report: Student Grade Classifier

---

## 1. Project Overview
The Student Grade Classifier is a machine learning application developed as part of the Fundamentals of AI course. The project aims to predict whether a student will PASS or FAIL based on 15 important features derived from the dataset. It includes a complete AI pipeline, from data preprocessing to deployment, and provides both a CLI tool and a web app for user interaction.

---

## 2. Objectives
1. **Develop a predictive model** to classify students as PASS or FAIL.
2. **Implement a complete AI pipeline**, including data preprocessing, feature selection, model training, evaluation, and deployment.
3. **Provide user-friendly interfaces** for predictions via a CLI tool and a web app.
4. **Ensure interpretability** by using a reduced set of 15 features.

---

## 3. Methodology

### 3.1 Data Loading and Inspection
- **Dataset**: `student-mat.csv` containing student performance data.
- **Objective**: Understand the dataset structure, identify missing values, and explore feature distributions.
- **Outcome**: Dataset loaded successfully with no missing values.

### 3.2 Data Preprocessing
- **Steps**:
  - Handled categorical variables using one-hot encoding.
  - Scaled numerical features using `StandardScaler`.
  - Split data into training and testing sets (80% train, 20% test).
- **Outcome**: Cleaned and prepared dataset ready for modeling.

### 3.3 Feature Selection
- **Methodology**: Used model coefficients from Logistic Regression to identify the top 15 most important features.
- **Outcome**: Reduced feature set to 15 features for improved interpretability and efficiency.

### 3.4 Model Development
- **Algorithm**: Logistic Regression.
- **Hyperparameter Tuning**: Used `GridSearchCV` to optimize hyperparameters.
- **Outcome**: Trained and optimized Logistic Regression model with high accuracy and balanced precision/recall.

### 3.5 Model Evaluation
- **Metrics**:
  - Accuracy
  - Precision
  - Recall
  - F1-Score
  - Confusion Matrix
- **Outcome**: Model achieved an accuracy of 85% on the test set.

### 3.6 Deployment
- **CLI Tool**:
  - Developed `student_grade_cli.py` for command-line predictions.
  - Loads the trained model, scaler, and feature names.
- **Web App**:
  - Built `student_grade_webapp.py` using Streamlit.
  - Features a modern, user-friendly interface with a futuristic design.
  - Displays the 15 features used for prediction and provides input fields for user data.
- **Outcome**: Both deployment methods tested and verified for accurate predictions.

---

## 4. Key Decisions
1. **Feature Selection**: Reduced to 15 features for better interpretability.
2. **Algorithm Choice**: Logistic Regression for its simplicity and effectiveness in binary classification.
3. **Deployment**: Provided both CLI and web app options to cater to different user preferences.

---

## 5. Outcomes
- Successfully developed a predictive model with high accuracy.
- Delivered user-friendly interfaces for predictions.
- Achieved project objectives within the scope of the Fundamentals of AI course.

---

## 6. Project Inventory

### 6.1 Files and Their Purpose
- **`Student_Grade_Classifier.ipynb`**: Jupyter notebook containing the full AI pipeline, from data preprocessing to model training and evaluation.
- **`student_grade_cli.py`**: CLI tool for making predictions.
- **`student_grade_webapp.py`**: Streamlit web app for making predictions via a modern interface.
- **`student-mat.csv`**: Dataset used for training and testing the model.
- **`student_grade_model.pkl`**: Trained Logistic Regression model saved for deployment.
- **`scaler.pkl`**: Scaler used for feature normalization.
- **`feature_names.pkl`**: List of the 15 features used in the model.
- **`README.md`**: Documentation for the project, including installation and usage instructions.
- **`Final_Report.md`**: Comprehensive report summarizing the project.

---

## 7. Conclusion
The Student Grade Classifier project successfully demonstrates the application of machine learning techniques to solve a real-world problem. The project follows a structured AI pipeline and provides user-friendly deployment options, making it a valuable learning experience and a practical tool for predicting student performance.

---

## 8. License
This project is licensed under the MIT License.
