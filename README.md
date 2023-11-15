# Player Stats Calculator API - Levi9 5 Days in Cloud hackathon

This API was written for the entry round of the Levi9 5 Days in Cloud hackathon. It reads through a provided CSV file and using the information read creates traditional and advanced stats for each player in the CSV.
The API provides an endpoint where each player can be searched for. The endpoint will provide data on the player in a JSON format.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Implementation](#implementation)

## Installation

- **Clone the repository**
    
    Create a directory for the project:
    Use `mkdir <directory_name>` and enter the folder using `cd <directory_name>`
    Use `git clone git@github.com:MarkizCar20/levi9_5duo.git` to clone the repository

- **Create virtual environment**

    Create virtual environment:
    Use command `python3 -m venv myEnv`
    Activate virtual environment:
    Use command `source myEnv/bin/activate`

- **Installing dependencies**

    To install required dependencies:
    Use command `pip3 install -r requirements.txt`

- **Validating installation**

    To validate source code integrity:
    Use command `python3 src/test.py`; If all tests pass you've succesfully built the project and it's ready to be run

##Usage

- **Running the API**

    To run the project:
    Use command `python3 app.py`. If you're getting the following response in the terminal, the app has been launched successfully:
    ```
    * Serving Flask app 'routes'
    * Debug mode: on
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 596-577-563
    ```

- **Getting the Player Stats**

    Navigate to your browser to url `http://127.0.0.1:5000/stats/player/<player_name>`, where <player_name> is the name of the Player whose stats you're searching for
    
    The response will be a json format data packet, where all the stats will be listed.

##Implementation

- **Tech stack used**

    In this project I used **Python** as the base language, with the **Flask** and **Flask-Restful** modules for creating the API


- The project consists of 3 different modules:

    app.py - Used to start up the API
    routes.py - Used to create routes and add them to the flask ap
    test.py - Used to test the API and the models module

    The app which contains the API firstly reads the csv file and creates all the Players Stats sheets, which are stored in an in-memory **volatile** dictionary and used to calculate all the traditional and advanced stats for each player over all of his appearances.

    The API exposes  the `http://127.0.0.1:5000/stats/player/<player_name>` endpoint where all of the players stats can be accessed.
    In case the endpoint isn't provided with a name of a player from the csv file, it will return an error message, with the status code 404, otherwise it will return code 200 with the json data of the player.