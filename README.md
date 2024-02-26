Weather App

This is a simple weather application built using Python and the OpenWeatherMap API. It allows users to retrieve current weather information by providing a zip code. The backend is implemented in Python, utilizing the requests library to interact with the OpenWeatherMap API, while the frontend can be implemented using any technology capable of making HTTP requests, such as React.js.

Features

Retrieve current weather information based on zip code input.
Utilizes the OpenWeatherMap API to fetch weather data.
Prerequisites

Before running the application, make sure you have the following installed:

Python 3.x
requests library (Install using pip install requests)
OpenWeatherMap API key (Sign up and obtain an API key from OpenWeatherMap)

Installation
1. Clone this repository to your local machine:
   git clone https://github.com/your-username/weather-app.git
2. Navigate to the project directory:
   cd weather-app
3. Create a config.ini file in the project directory and add your OpenWeatherMap API key:
   [openweathermap]
   api = YOUR_API_KEY
4. Install dependencies:
   pip install -r requirements.txt

Usage

To run the application, execute the following command:
  python app.py

The application will prompt you to enter a zip code. After providing the zip code, it will fetch and display the current weather information.

Frontend Integration

If you want to integrate this backend with a frontend application, you can make HTTP POST requests to the backend API endpoint /weather with the following JSON payload:
  {
  "zip_code": "95129"
  }




