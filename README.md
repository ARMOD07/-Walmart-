 
# Walmart

Walmart Sales Predictor This project is a full-stack machine learning application designed to predict weekly sales for Walmart stores. It includes:
## Screenshots
https://github.com/user-attachments/assets/031d7fa8-d308-4137-8787-2b067f40e559

<img width="650" alt="image" src="https://github.com/user-attachments/assets/031d7fa8-d308-4137-8787-2b067f40e559" />
## Demo
 

🔍 Data exploration & modeling in a Jupyter notebook

 

🤖 A trained RandomForestRegressor saved as a .pkl model
 

⚙️ A FastAPI backend for real-time predictions
 

🌐 A simple HTML/JS frontend to interact with the model
 

🔁 A sample JSON request to test the API
 

🚀 Quick Start
 




##📂 Project Structure

```javascript
walmart-sales-predictor/
├── app.py                  # 🚀 FastAPI backend
├── sales_model.pkl         # 🤖 Trained ML model (RandomForestRegressor)
├── notebooks.ipynb         # 📓 Jupyter Notebook (EDA + Training)
│
├── backend_api/            # 📦 Backend folder
│   └── static/
│       └── index.html      # 🌐 Frontend HTML + JavaScript
│
├── requirements.txt        # 📄 Python dependencies
├── venv/                   # 🧪 (Optional) Virtual environment
└── README.md               # 📘 Project documentation

```

 
 

## Installation

1.Clone the project

```bash
git clone https://github.com/<YOUR_USERNAME>/walmart-sales-predictor.git cd walmart-sales-predictor
```
 

2.Create a virtual environment (optional)
```bash
python -m venv venv source venv/bin/activate # For Linux/Mac venv\Scripts\activate # For Windows 
```
3.Install dependencies
```bash 
pip install -r requirements.txt
 
```
4.Run the FastAPI backend 
```bash 
bash uvicorn app:app --reload
```

## Roadmap
📒 1. Jupyter Notebook (_notebooks.ipynb) The notebook covers:
 

📊 Data loading and preprocessing
 

📈 Exploratory Data Analysis (EDA)
 

🧪 Feature engineering (date parsing, holiday flag, etc.)
 

🏗️ Model training using RandomForestRegressor
 

📉 Evaluation using RMSE, MAE, R²
 

💾 Model export using joblib as sales_model.pkl
 

⚙️ 2. FastAPI Backend (app.py) Loads the trained model sales_model.pkl
 

Accepts input via POST request at /predict
 

Preprocesses the input (similar to the notebook)
 

Returns a prediction (Weekly_Sales_Predicted)
 

🌍 3. Web Frontend The backend_api/static/index.html file:
 

Presents a user-friendly form
 

Sends user input to the API using JavaScript fetch
 

Displays the prediction dynamically on the page
 

 

## 📛 Badges

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95.1-green?logo=fastapi)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/status-Active-brightgreen)
![Model](https://img.shields.io/badge/model-RandomForestRegressor-orange)
![Notebook](https://img.shields.io/badge/Jupyter-Notebook-F37626.svg?logo=jupyter)
![Platform](https://img.shields.io/badge/Platform-Local%20host-blueviolet)



uvicorn backend_api.app:app --reload
http://127.0.0.1:8000/static/index.html
 
