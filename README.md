# Weather App

A command-line weather application developed in Python using the Open-Meteo API.

This project was created to practice API consumption, Object-Oriented Programming (OOP), data persistence, modular architecture, and error handling.

## Features

* Search weather information by city
* Automatic geocoding (city to coordinates)
* Current weather conditions
* Multi-day weather forecast
* Persistent search history using JSON
* Weather statistics and analytics
* Object-Oriented design
* Modular project structure
* Error handling for network failures and corrupted data

## Technologies

* Python 3
* Requests
* Open-Meteo API
* JSON
* Object-Oriented Programming (OOP)

## Project Structure

```text
python-weather-app/
│
├── main.py
├── api.py
├── historico.py
├── historico.json
├── requirements.txt
├── README.md
│
├── models/
│   └── consulta_clima.py
```

## How to Run

Clone the repository:

```bash
git clone git@github.com:patrickoliveira-dev/python-weather-app.git
```

Navigate to the project directory:

```bash
cd python-weather-app
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

## Available Statistics

The application records and displays:

* Total number of searches
* Most searched city
* Average recorded temperature
* Highest recorded temperature
* Lowest recorded temperature
* First search performed
* Most recent search performed
* Top 3 most searched cities

## Learning Objectives

This project was built to practice:

* REST API consumption
* JSON manipulation
* Classes and objects
* Data persistence
* Exception handling
* Modularization
* Git and GitHub workflow

## Future Improvements

* Export history to CSV
* Export reports to PDF
* Weather condition icons
* Favorite cities
* Search filters
* Graphical user interface (GUI)
* Database integration

## Author

Patrick Barboza Oliveira