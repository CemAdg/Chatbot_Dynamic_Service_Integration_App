# IoT Hackathon

## ZRoom App - Two worlds, one room

The IoT Hackathon has the goal to find solutions for the typical problems during hybrid-lectures, e.g. the professor "forgets" the remote students or the professor has to interrupt the lecture on site and carry out additional activities in order to interact with remote students. More details about the problems and our concept can be found in the [Wiki](https://gitlab.reutlingen-university.de/SCCA/ZRoom_App/-/wikis/home).

## About the Stack

As a MVP for our concept, we implemented a full stack web application with different software environments and components for the frontend and backend. More conceptional details about the software architecture and the prototyp can be also found in the [Wiki](https://gitlab.reutlingen-university.de/SCCA/ZRoom_App/-/wikis/home) under Chapter 3.

### Backend

The `./backend` directory contains a Flask web server with API endpoints, running on a RaspberryPi that is wired with some LEDs through the GPIO Pins. The API are activating the LEDs when getting API requests from the ZRoom App Client / frontend.

[View the README.md within ./backend for more details.](https://gitlab.reutlingen-university.de/SCCA/ZRoom_App/-/tree/main/backend)

### Frontend

The `./frontend` directory contains a React frontend with buttons (representing different reactions) to send HTTP requests to the API endpoints of the Flask server to manipulate the corresponding lamps.

[View the README.md within ./frontend for more details.](https://gitlab.reutlingen-university.de/SCCA/ZRoom_App/-/tree/main/frontend)
