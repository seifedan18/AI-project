# Student Grade Classifier

This project is a machine learning application designed to predict whether a student will PASS or FAIL based on 15 important features. It is built as part of the Fundamentals of AI course and includes both a CLI tool and a web app for deployment.

## Features
- **CLI Tool**: A command-line interface for making predictions.
- **Web App**: A modern, user-friendly web interface built with Streamlit.
- **Machine Learning Pipeline**: Includes data preprocessing, model training, evaluation, and deployment.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd Fundamental-of-AI-Project
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### CLI Tool
Run the CLI tool to make predictions:
```bash
python student_grade_cli.py
```
Follow the prompts to input feature values.

### Web App
Launch the Streamlit web app:
```bash
streamlit run student_grade_webapp.py
```
Open the provided URL in your browser to access the app.

## Files
- `Student_Grade_Classifier.ipynb`: Jupyter notebook containing the full AI pipeline.
- `student_grade_cli.py`: CLI tool for predictions.
- `student_grade_webapp.py`: Streamlit web app for predictions.
- `student-mat.csv`: Dataset used for training the model.
- `student_grade_model.pkl`: Trained machine learning model.
- `scaler.pkl`: Scaler used for feature normalization.
- `feature_names.pkl`: List of features used in the model.

## Project Structure
```
Fundamental-of-AI-Project/
├── Student_Grade_Classifier.ipynb
├── student_grade_cli.py
├── student_grade_webapp.py
├── student-mat.csv
├── student_grade_model.pkl
├── scaler.pkl
├── feature_names.pkl
└── README.md
```

## License
This project is licensed under the MIT License.