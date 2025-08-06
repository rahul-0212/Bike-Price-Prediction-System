# 🚴‍♂️ BikeQ – Bike Price Prediction System

[![Flask](https://img.shields.io/badge/Built%20with-Flask-blue.svg)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-brightgreen.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)]()
[![Status](https://img.shields.io/badge/Status-Active-green.svg)]()

**BikeQ** is a futuristic neon-themed web application built with **Flask** that predicts the price of used bikes using machine learning. The model is trained on a cleaned dataset with relevant features and presented through a fully responsive and modern UI.

---

## ✨ Features

- 📈 Predicts bike resale price based on:
  - Brand
  - Engine power (cc)
  - Age of the bike
  - Type of ownership
  - Kilometers driven
- 💡 Neon-theamed modern web interface
- 📑 Tracks prediction history automatically
- 📊 Jupyter notebook included for data exploration
- ⚙️ Easy to deploy and extend for future improvements

---

## 📁 Project Structure

```bash
bikes/
│
├── app.py                  # Main Flask backend
├── model.joblib            # Trained machine learning model
├── Used_Bikes.csv          # Original raw dataset
├── clean_bike_data.csv     # Cleaned dataset used for training
├── cleaned_bikes.csv       # (Optional) extra-cleaned file
├── prediction_history.csv  # Stores all user prediction logs
├── bikes.ipynb             # Jupyter notebook for EDA & ML
│
├── requirements.txt        # List of Python dependencies
├── README.md               # Project documentation
│
├── static/
│   └── images/             # Contains all bike images
│
└── templates/
    ├── index.html          # Home page
    ├── about.html          # About the project
    ├── contact.html        # Contact form
    ├── history.html        # History of predictions
    └── project.html        # Input form for prediction
```

---

## 🚀 How to Run the Project

1. **Install required packages**

   Make sure you have Python installed (version 3.10 or above). Then install all required libraries:

   ```bash
   pip install -r requirements.txt
   ```

2. **Start the Flask server**

   ```bash
   python app.py
   ```

3. **Open your browser and visit:**

   ```
   http://127.0.0.1:5000/
   ```

---

## 📌 Important Notes

- All HTML templates are located inside the `templates/` folder.
- Static assets like CSS, images, and JS files go inside the `static/` folder.
- For images inside HTML, use the `url_for()` function like this:

  ```html
  <img src="{{ url_for('static', filename='images/yourimage.png') }}" alt="Bike Image">
  ```

- All prediction history is saved to `prediction_history.csv` in real time.

---

## 🌄 Demo Preview

> _Add a screenshot or GIF of your working project UI here for better presentation._

```
Home PAGE
<img width="1919" height="908" alt="image" src="https://github.com/user-attachments/assets/1f639eb4-e84e-4379-aac8-aea3150db472" />
---

## 🙋‍♂️ Developed By

**Rahul Parihar**  
🎓 B-tech Student @ BTU University, Bikaner
📍 India  
🔗 [GitHub](https://github.com/rahul-0212) | [LinkedIn](https://www.linkedin.com/in/rahul-parihar-5927bb30a)

---

## 📃 License

This project is released under the [MIT License](LICENSE). You are free to use, distribute, and modify it with proper attribution.
