# Weather Dashboard

A minimal Flask-based Weather Dashboard that pulls current weather and a 5-day forecast from OpenWeatherMap and displays it in a Bootstrap-styled page.

---

## 🚀 Features

- Current weather for any city (temperature, “feels like,” humidity, wind, pressure, description, icon)
- 5-day forecast (date, high/low temps, icon, description)
- Responsive layout with Bootstrap 5
- Easy deployment to Heroku via Gunicorn

---

## 📋 Prerequisites

- Python 3.8+  
- pip  
- (Optional) virtualenv or venv  
- An OpenWeatherMap API key (free signup at [openweathermap.org](https://openweathermap.org/))

---

## 🛠️ Installation & Setup

1. **Clone this repository**
   ```bash
   git clone https://github.com/your-username/weather-dashboard.git
   cd weather-dashboard
2. **Create a virtual environment**
   '''bash
   python3 -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\Scripts\activate         # Windows
  
     
4. **Install dependencies**
   pip install -r requirements.txt

6. **Environment variables**
   - Create a .env file in the project root with:
     OWM_API_KEY=your_openweathermap_api_key
     FLASK_SECRET_KEY=your_flask_secret_key
   -Or copy the example:
    cp .env.example .env

## ▶️ Running Locally
