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
   ```shell
   git clone https://github.com/your-username/weather-dashboard.git
   cd weather-dashboard
   ```
   
2. **Create a virtual environment**
   ```shell
   python3 -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\Scripts\activate         # Windows
   ```
     
4. **Install dependencies**
   ```shell
   pip install -r requirements.txt
   ```
   
6. **Environment variables**
   - Create a .env file in the project root with:
     OWM_API_KEY=your_openweathermap_api_key
     FLASK_SECRET_KEY=your_flask_secret_key
     
   - Or copy the example:
    ```shell
    cp .env.example .env
    ```

   ---

## ▶️ Running Locally

1. Ensure your virtual environment is active.
2. Start the Flask development server:
   ```shell
   flask run
   ```
3. Open your browser at http://127.0.0.1:5000/.
4. Enter a city name and hit Get Weather to see current conditions and a 5-day forecast.

   ---

## ☁️ Deployment to Heroku
1. Ensure you have the Heroku CLI installed (brew install heroku/brew/heroku on macOS, or see devcenter.heroku.com).
2. Log in & create app
   ```shell
   heroku login
   heroku create your-app-name
   ```
3. Push to Heroku
   ```shell
   git push heroku main   # or master
   ```
4. Set config vars on Heroku
   ```shell
   heroku config:set OWM_API_KEY=your_openweathermap_api_key
   heroku config:set FLASK_SECRET_KEY=your_flask_secret_key
   ```
5. Open your live dashboard
   ```shell
   heroku open
   ```

   ---

## 📁 Project Structure
   ```shell
   weather-dashboard/
   ├── .env                 # local environment vars (ignored by git)
   ├── .env.example         # template for .env
   ├── .gitignore
   ├── Procfile             # Heroku process file
   ├── README.md
   ├── requirements.txt
   ├── runtime.txt          # Python version on Heroku
   ├── app.py               # Flask application
   ├── templates/
   │   ├── base.html        # Main layout (Bootstrap CSS/JS)
   │   └── dashboard.html   # Search form & weather display
   └── static/
       └── css/
           └── style.css    # Custom styles
   ```

   ---

## 🤝 Contributing
1. Fork the repo
2. Create a branch (git checkout -b feature-name)
3. Commit your changes (git commit -m "Add feature")
4. Push to your fork (git push origin feature-name)
5. Open a Pull Request

   ---

## 📄 License
This project is MIT-licensed. See [LICENSE](https://github.com/samiller1109/weather_dashboard/blob/main/LICENSE) for details.
