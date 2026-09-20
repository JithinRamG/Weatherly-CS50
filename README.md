# Weatherly 🌦️

#### Video Demo:
https://youtu.be/hX6fqGwkyGk?si=Hd2-REliGAN0Gea9

#### Description:

Weatherly is a simple weather web application created as my CS50x Final Project. The application allows users to search for a city and view its current weather conditions as well as a five-day forecast. Users can also save cities that they frequently check and remove them whenever they want.

I created Weatherly to build a practical application while applying concepts that I learned throughout CS50x. The project combines Python, Flask, SQLite, HTML, CSS, and external APIs into one working web application.

### Features

Weatherly provides several simple features:

- Search for weather by city
- View the current temperature
- View humidity
- View wind speed
- View a five-day forecast
- View daily maximum and minimum temperatures
- View the probability of precipitation
- Save frequently used cities
- Load weather for saved cities
- Delete saved cities

### How Weatherly Works

When a user enters a city name, the Flask application receives the request from the webpage. Weatherly first uses the Open-Meteo Geocoding API to search for the requested city.

The geocoding service provides the geographical coordinates of the city. Weatherly then uses those coordinates to request weather information from the Open-Meteo Forecast API.

The application retrieves the current temperature, relative humidity, wind speed, and daily forecast information. Flask then passes this information to the HTML template, where it is displayed to the user.

If a city cannot be found or the weather request does not return usable information, Weatherly displays an error message instead of displaying incorrect information.

### Saved Cities

Weatherly also allows users to save cities that they frequently want to check.

Saved cities are stored in a local SQLite database called `mausam.db`. The database contains a `cities` table with an automatically generated ID and the name of each saved city.

Before inserting a city, the application checks whether that city is already present in the database. This prevents duplicate saved cities.

Users can click the weather icon beside a saved city to load its weather information. They can also remove a saved city using the delete option.

The database file itself is not included in the GitHub repository because it is local application data and is excluded using `.gitignore`.

### Files

#### `app.py`

This is the main Python file for Weatherly. It creates the Flask application and defines the application's routes.

It handles city searches, communication with the Open-Meteo APIs, retrieving saved cities from SQLite, saving new cities, deleting cities, and passing information to the webpage.

#### `templates/index.html`

This file contains the main HTML structure of the application.

It uses Flask's Jinja templating system to dynamically display weather information returned by the Python application. It also contains the forms used for searching, saving, and deleting cities.

#### `static/style.css`

This file contains the CSS used to style Weatherly. It controls the layout, colors, buttons, input fields, weather sections, spacing, and overall appearance of the application.

#### `DESIGN.md`

This document explains the design and technical decisions behind Weatherly. It describes the technologies used, the application flow, database design, API usage, and possible future improvements.

#### `.gitignore`

The `.gitignore` file prevents files such as the local SQLite database, Python cache files, virtual environments, and environment files from being uploaded to GitHub.

### Technologies Used

Weatherly was built using:

- Python
- Flask
- SQLite
- HTML
- CSS
- Open-Meteo Geocoding API
- Open-Meteo Forecast API

Python and Flask are used for the backend, SQLite is used for persistent storage of saved cities, and HTML and CSS provide the frontend interface.

### Design Choices

I chose Flask because it provides a simple way to connect Python backend logic with HTML templates. SQLite was selected because the application only needs a small local database for storing saved cities.

I also chose to use Open-Meteo for weather data because it provides the required weather and geocoding functionality without requiring an API key for this project.

The interface was intentionally kept simple so that the main functionality is easy to understand and use.

### Future Improvements

Weatherly could be expanded in the future with features such as weather alerts, more detailed weather information, interactive weather maps, user accounts, better mobile responsiveness, and additional weather-based recommendations.

### Conclusion

Weatherly is a small but complete web application that demonstrates how a Python backend, database, frontend, and external API can work together.

Building the project gave me an opportunity to apply concepts from CS50x in a practical application and understand the process of taking an idea from code to a functioning web project.
