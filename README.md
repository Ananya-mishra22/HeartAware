# ❤️ HeartAware – AI-Based Cardiac Risk Prediction System
📌 Overview

HeartAware is an AI-powered health analytics system designed to predict the risk of heart attacks and cardiac arrest using multiple medical indicators and machine learning models.

The system analyzes different types of health data such as lifestyle factors, ECG reports, blood test reports, and cardiac imaging data to detect early signs of cardiovascular risk. The goal of HeartAware is to support early diagnosis, preventive healthcare, and clinical decision-making.

🚀 Features
1️⃣ Lifestyle-Based Heart Risk Prediction

Predicts the probability of heart attack based on factors such as:

Age

Smoking habits

Physical activity

Blood pressure

Cholesterol levels

Diabetes history

BMI and lifestyle habits

Uses machine learning models to classify individuals into low, medium, or high risk categories.

2️⃣ Cardiac Arrest Prediction using Blood Markers

Uses the White Blood Cell and Platelet Ratio (WPR) along with other blood parameters to detect possible cardiac arrest risks.

Analyzes:

WBC count

Platelet count

Inflammatory markers

This helps identify hidden cardiovascular stress conditions.

3️⃣ ECG-Based Prediction

Analyzes ECG signals of ICU patients to detect abnormalities that may lead to:

Heart attack

Cardiac arrest

Arrhythmias

The system extracts features from ECG signals and uses machine learning models to detect risk patterns.

4️⃣ Cardiac Imaging Analysis (2D Echo / CAG)

Processes cardiac imaging reports such as:

2D Echo

Coronary Angiography (CAG)

to detect:

Blockages

Heart muscle abnormalities

Reduced pumping efficiency

This module helps predict heart blockage and possible heart attack risk.

🧠 Machine Learning Models Used

The project explores multiple ML algorithms including:

Convolutional Neural Networks (for signal/image data)

Model selection is based on accuracy.

🤖 LLM-Assisted Explanation

Multiple Large Language Models are integrated to provide:

Human-readable explanations of prediction results

Risk interpretation

Preventive health suggestions

Summary of patient health insights

This helps transform raw ML predictions into clear medical insights.

🛠️ Tech Stack
Backend (Django & ML Integration): 

Django (Python-based web framework) 

TensorFlow/Keras (for CNN models) 

Scikit-Learn (for classification model) 

NumPy & Pandas (for data handling) 

Frontend (Basic Web UI) 

Database & Storage 

SQLite (if small-scale or for prototyping) 

Django ORM (for database interaction) 


Cloud & IoT Integration 

Google Cloud (IOT integration)

📂 Project Structure
HeartAware/
│
├── frontend/                # React/Next.js frontend
│
├── backend/
│   ├── models/              # ML models
│   ├── preprocessing/       # Data preprocessing scripts
│   ├── api/                 # Django APIs
│
├── datasets/                # Training datasets
│
├── notebooks/               # Model training notebooks
│
├── results/                 # Model outputs and evaluation
│
└── README.md

⚙️ Installation

1️⃣ Clone the repository

git clone https://github.com/yourusername/HeartAware.git

cd HeartAware

2️⃣ Install dependencies

pip install -r requirements.txt

3️⃣ Run the backend

python manage.py runserver

4️⃣ Run the frontend

npm install

npm run dev

📊 Model Evaluation

🎯 Applications

Early detection of cardiovascular diseases

Hospital ICU monitoring systems

Preventive healthcare analytics

AI-assisted clinical decision systems

⚠️ Disclaimer

This system is designed for research and educational purposes only and should not replace professional medical diagnosis.

👩‍💻 Authors

Ananya Mishra, Kirti More, Rutuja Manore, Kinjal Paradkar

