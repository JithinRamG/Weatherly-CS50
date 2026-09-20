# Design Document — Weatherly 🌦️

## Overview

Weatherly is a simple weather web application created as my CS50x Final Project.

The application allows users to search for a city and view its current weather and five-day forecast. Users can also save cities for quick access later.

## Technology Choices

### Python and Flask

Python is used for the backend because it is one of the languages covered in CS50x.

Flask handles the web routes and connects the frontend with the weather API and SQLite database.

### SQLite

SQLite is used to store saved cities.

The database contains a `cities` table with:

- `id` — unique identifier
- `name` — saved city name

### HTML and CSS

HTML provides the structure of the webpage, while CSS provides the visual design.

### Open-Meteo API

Mausam uses Open-Meteo to retrieve geographical information and weather data.

## Application Flow

1. The user enters a city name.
2. Flask receives the request.
3. The application uses the geocoding API to find the city.
4. The city's coordinates are sent to the weather API.
5. Weather information is returned.
6. Flask sends the data to the HTML template.
7. The webpage displays the current weather and five-day forecast.

## Saved Cities

When a user saves a city, Flask checks whether it already exists in the SQLite database.

If it does not exist, the city is inserted into the database.

Users can also delete saved cities.

## Error Handling

If a city cannot be found or the weather request fails, the application displays an error message instead of displaying invalid weather data.

## Future Improvements

Possible future improvements include:

- User accounts
- More detailed weather information
- Weather alerts
- Interactive weather maps
- Better mobile responsiveness
- Offline support

## Conclusion

Weatherly was designed as a small and practical project that combines Python, Flask, SQLite, HTML, CSS, and an external API into one working web application.