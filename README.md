# Weatherly 🌦️

#### Video Demo:
https://youtu.be/hX6fqGwkyGk?si=Hd2-REliGAN0Gea9

#### Description:

Weatherly is a simple weather web application built as my CS50x Final Project.

The application allows users to search for a city and view its current weather conditions and a five-day forecast. Users can also save cities that they frequently check and remove them whenever they want.

The project was designed to demonstrate concepts learned throughout CS50x, including Python, Flask, SQL, HTML, CSS, and working with APIs.

### Features

- 🔎 Search for weather by city
- 🌡️ View current temperature
- 💧 View humidity
- 💨 View wind speed
- 📅 View a five-day forecast
- 🌧️ View daily precipitation probability
- ⭐ Save frequently used cities
- ❌ Remove saved cities
- 🌦️ Quickly load weather for saved cities

### Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- Open-Meteo API

### Files

#### `app.py`

The main Flask application.

It handles:
- Web routes
- City searches
- Weather API requests
- Saving cities
- Deleting cities
- Database operations

#### `templates/index.html`

Contains the main webpage and uses Jinja templates to display weather information dynamically.

#### `static/style.css`

Contains the styling for the application.

#### `weatherly.db`

SQLite database used to store saved cities.

### How It Works

When a user searches for a city, Mausam first uses the Open-Meteo geocoding API to find the city's latitude and longitude.

The application then sends those coordinates to the Open-Meteo weather API and retrieves current weather and five-day forecast information.

The results are displayed on the webpage using Flask and Jinja.

Saved cities are stored in a local SQLite database.

### Purpose

I created Weatherly to build a practical application while applying concepts from CS50x. The project combines a backend written in Python with a simple frontend and an external weather API.

The main goal was to create a small but functional weather application that demonstrates how different web-development concepts work together.