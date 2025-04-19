<details>
<summary>📋 Click to Expand the Markdown</summary>

# 🧠 E-Commerce Purchase Prediction API

This project is a **machine learning-powered Flask API** that predicts whether a user will purchase something based on their browsing behavior on an e-commerce platform.

### 🚀 Live Demo
➡️ [Try the API on Render](https://ecommerce-ml-api-8116.onrender.com/predict)

---

## 📦 Features

- Trained a **Random Forest Classifier** on real e-commerce behavioral data
- Built feature-engineered dataset from raw event logs (views, cart, purchase, category)
- Deployed the model with a lightweight **Flask API**
- Hosted for free using **Render**

---

## 🧠 How It Works

You send user behavior data like this:

```json
{
  "num_views": 12,
  "num_cart_adds": 3,
  "unique_categories": 4
}
```

And get back a prediction:

```json
{
  "prediction": 1
}
```
Where:
	•	1 = User is likely to purchase
	•	0 = Not likely to purchase
---

## 🔧 API Usage
📌 Endpoint

POST /predict
URL: https://ecommerce-ml-api-8116.onrender.com/predict
Headers: Content-Type: application/json

🧪 Example curl Request
``` bash
curl -X POST https://ecommerce-ml-api-8116.onrender.com/predict \
-H "Content-Type: application/json" \
-d '{"num_views": 12, "num_cart_adds": 3, "unique_categories": 4}'
```

🧱 Project Structure

ecommerce-ml-api/

├── app.py                # Flask app with /predict route

├── model.pkl             # Trained ML model (RandomForest)

├── requirements.txt      # Python dependencies

├── .gitignore            # Ignored files/folders

├── README.md             # You're here!


📁 Tech Stack
	•	Python 3.11
	•	Flask – for the web server / API
	•	scikit-learn – for the machine learning model
	•	NumPy & Joblib – for prediction & model loading
	•	Render – for free deployment and hosting


