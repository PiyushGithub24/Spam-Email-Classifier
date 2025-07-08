<H1>"End to end spam email classification project "</H1>
# 📧 Spam Email Classifier

A machine learning-based web application that detects whether a given email is **spam or not spam** using **Natural Language Processing (NLP)** and **Multinomial Naive Bayes**. Achieved **97.3% accuracy** and **100% precision**, and deployed using **Flask** and **Render**.

---

## 🔍 Overview

Spam emails are not only annoying but also pose serious security threats. This project aims to automate spam detection using supervised machine learning and NLP techniques. The trained model is integrated into a web application where users can input an email and receive a prediction in real time.

---

## 🚀 Live Demo

🔗 [View the App](https://spam-email-classifier.onrender.com)  
*(Replace this link with your actual Render deployment URL)*

---

## 📊 Model Highlights

- **Algorithm**: Multinomial Naive Bayes
- **Text Processing**: TF-IDF Vectorization
- **Accuracy**: 97.3%
- **Precision**: 100%
- **Dataset**: Real-world labeled spam/ham emails

---

## 🧰 Tech Stack

- **Language**: Python
- **Libraries**: Pandas, Scikit-learn, NumPy, NLTK
- **NLP Techniques**: Tokenization, Stop-word removal, TF-IDF
- **Framework**: Flask
- **Deployment**: Render
- **Version Control**: Git & GitHub

---

## 📁 Folder Structure

Spam-Email-Classifier/
│
├── static/ # CSS styling
│ └── style.css
│
├── templates/ # HTML template
│ └── index.html
│
├── model/ # Serialized model
│ └── spam_model.pkl
│
├── utils.py # Text cleaning and preprocessing functions
├── data_transformation.py# TF-IDF vectorization
├── app.py # Flask app
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## 💡 Features

- Clean and process input email text
- Predict spam/ham using ML model
- Simple web interface for user interaction
- Hosted on Render for public use

---

## 🛠 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/PiyushGithub24/Spam-Email-Classifier.git
cd Spam-Email-Classifier

