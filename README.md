# 🧮 BMI Calculator (Body Mass Index)

**Stanford - Code in Place 2025** - _Final Project by Wanda van den Hoogen_

This is a simple BMI Calculator web application built using **Python 3** and the **Flask web framework**. 
The backend is deployed on Render, and the frontend is hosted on **GitHub Pages**.

It calculates the Body Mass Index based on the user's input and provides a textual interpretation of the result (e.g., "normal", "underweight", "obese", etc.).

---

## 🌐 Live Demo

**Frontend**: [https://wvdh.github.io/bmi-calculator](https://wvdh.github.io/bmi-calculator)  _It's a free plan on render.com so it takes a moment for the application to start._

- Enter your height and weight
- Get your BMI score and interpretation instantly
- Stylish and responsive interface
- Possibility to do a new calculation
---

![ScreenshotBMI](https://github.com/user-attachments/assets/2a4c3e8f-3e7e-4809-a41d-fdd1ce4828d9)

---

## 🚀 Features

- Clean and responsive user interface (HTML + CSS)
- Dynamic BMI calculation via Flask API
- Server-side logic and BMI classification written in **Python 3**
- Full support for client-side navigation
- Persistent display of results using `localStorage`
- Hosted on GitHub Pages (frontend) and Render (backend)

---

## 📐 How BMI is calculated

The formula is:

```
BMI = weight (kg) / (height in meters)^2
```

For example:  
A person who weighs 70 kg and is 1.75 m tall will have a BMI of:
```
70 / (1.75^2) = 22.86
```

---

## 💡 BMI Categories

| BMI Range        | Interpretation         |
|------------------|------------------------|
| ≤ 18.4           | You are underweight.   |
| 18.5 – 24.9      | Your weight is normal. |
| 25.0 – 29.9      | You are slightly overweight. |
| 30.0 – 34.9      | You are severely overweight. |
| 35.0 – 39.9      | You are obese.         |
| ≥ 40.0           | You are severely obese. |

---

## 🔧 Technologies Used

- **Python 3** – used for backend logic, BMI calculation, and HTTP API handling
- **Flask** – lightweight Python web framework for routing
- **flask-cors** – enables cross-origin requests from GitHub Pages
- **HTML/CSS** – for frontend structure and styling
- **JavaScript** – handles form submission and API interaction
- **GitHub Pages** – static hosting for frontend
- **Render.com** – cloud hosting for the Python backend

---

##  🧪 What is Flask?

Flask is a lightweight web framework for Python. It allows you to build web applications quickly and with minimal code. In this project, Flask is used to:

- Handle routing (e.g., showing the form and result pages)
- Process user input (height and weight)
- Render HTML templates with dynamic content (like the BMI result)

Flask is ideal for small to medium-sized projects due to its simplicity and flexibility.

---

## 🗂️ Project Structure

```
📁 bmi-calculator/
│
├── app.py                  # Flask backend
├── requirements.txt        # Python dependencies
│
├── index.html              # GitHub Pages frontend (independent)
├── result.html             # GitHub Pages result display (independent)
├── index.css               # Frontend CSS
├── assets/                 # Icons and images
├── site.webmanifest
└── README.md
```

---

## 📡 API Usage

**Endpoint**: `POST /api/calculate`  
**URL**: `https://bmi-calculator-vgwl.onrender.com/api/calculate`

**Request (JSON):**
```json
{
  "weight": 70,
  "height": 1.75
}
```

**Response (JSON):**
```json
{
  "bmi": 22.86,
  "interpretation": "Your weight is normal."
}
```

---

## 📝 License

This project is open-source and free to use under the MIT license.

---

## 🙋‍♂️ Author

Created by **WvdH**    
GitHub: [https://github.com/wvdh](https://github.com/wvdh)

---

![bmi](https://github.com/user-attachments/assets/3331e893-4401-420c-93ca-40d731de3f66)
