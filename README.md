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
<pre> ```bash
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
 ``` </pre>

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
 ```

---

### 2. Install Dependencies
```bash
pip install -r requirements.txt
 ```

---

### 3. Run the App
```bash
python app.py
 ```
Then open http://127.0.0.1:5000/ in your browser.

---

### 🧪 Usage
Enter a sample email or message in the text area

Click Predict

Instantly see if it's classified as spam or not spam

---

### 🖼️ Screenshots
![App Homepage](screenshots/home.png)

---

🙋‍♂️ Author
Piyush Kumar
📧 piyushrana3612@gmail.com
🔗 GitHub
🔗 LinkedIn

---

🌟 Acknowledgements
- Scikit-learn
- NLTK
- Render
- Flask

---
