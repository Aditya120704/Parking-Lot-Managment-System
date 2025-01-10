# Parking System Application

## Introduction
This project is a parking system application built using Flask. It allows users to park and remove vehicles, as well as check the status of the parking lot.

## Problem Domain
With the increasing number of vehicles, managing parking spaces efficiently has become a significant challenge. This application addresses the need for an effective parking management system.

## Solution Domain
The solution is implemented as a web application using Flask, providing a RESTful API for parking management. Users can park vehicles, remove them, and check the current status of the parking lot.

## Software Used
- Python: The programming language used for development.
- Flask: A lightweight WSGI web application framework in Python.
- HTML/CSS: For the front-end user interface.

## Techniques Required
- Basic knowledge of Python programming.
- Understanding of Flask framework and RESTful API design.

## Data Structures Used
-The project uses lists to manage parking slots and waitlists. The parking_slots list tracks parked vehicles, while the waitlist operates as a queue for vehicles waiting for available spaces.

## Methodology
The project was created using a structured approach, starting with requirement gathering and analysis. The design phase involved outlining the core functionalities of the parking system, followed by the implementation of the Flask application. Testing was conducted iteratively to ensure that each feature worked as intended before moving on to the next.

## Conclusion
The parking system application provides a simple yet effective way to manage parking spaces. Future improvements could include user authentication, a more sophisticated waitlist management system, and a user-friendly front-end interface.

## Getting Started
1. Run the application:
   ```bash
   python app.py
   ```
2. Open your web browser and go to `http://127.0.0.1:5000/` to access the main page.

## API Endpoints
- **Park a Vehicle:** Use the `/api/park` endpoint with a POST request to park a vehicle.
- **Remove a Vehicle:** Use the `/api/remove` endpoint with a POST request to remove a vehicle.
- **Get Status:** Use the `/api/status` endpoint with a GET request to check the parking status.

