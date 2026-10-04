# City Weather Reporter

This project is a command-line Python application that retrieves live weather data for a city using the OpenWeatherMap API. The program validates user input, connects to the API, displays a formatted weather report, saves the data to a CSV file, and reads the saved data back to summarize the cities currently stored.

## Features

- Prompts the user to enter a city name
- Validates that the city name is not empty
- Retrieves live weather data from OpenWeatherMap
- Displays:
    - City name
    - Country code
    - Temperature in Celsius
    - Humidity percentage
    - Weather description
- Handles invalid city names and API errors
- Saves weather data to `city_data.csv`
- Appends new city data without overwriting existing records
- Reads the CSV file and reports:
    - The number of saved cities
    - Each city name
    - Each saved temperature

## Project Files

- `reporter.py` contains the main Python program.
- `README.md` contains project documentation and instructions.
- `.gitignore` prevents sensitive or unnecessary files from being uploaded to GitHub.
- `city_data.csv` stores the weather data collected by the program.
- `api_key.txt` stores the OpenWeatherMap API key locally and should not be uploaded to GitHub.

## Requirements

This project uses Python and the following libraries:

- `csv`
- `json`
- `requests`

The `csv` and `json` modules are included with Python.

The `requests` library may need to be installed by running:

```bash
python -m pip install requests
```

## OpenWeatherMap API Key

This program requires a free OpenWeatherMap API key.

1. Go to https://openweathermap.org/ and create or sign in to your account.
2. Open the API Keys section of your account.
3. Copy your API key.
4. In the project folder, create a file named `api_key.txt`.
5. Paste your API key into that file on a single line.
6. Save the file.

Do not place the API key directly inside `reporter.py`.

The `api_key.txt` file should remain private and should not be uploaded to GitHub.

## .gitignore

The `.gitignore` file includes:

```text
api_key.txt
__pycache__/
```

This keeps the API key and automatically genertaed Python cache files out of the GitHub repository.

## How to Run

1. Open the project folder in VS Code.
2. Open the terminal.
3. Make sure the terminal is inside the project folder.
4. Run:

```bash
python reporter.py
```

5. Enter a city name when prompted.

Example:

```text
Enter a City name: Rochester
```

The program will retrieve the current weather data, display the report, save the information to 'city_data.csv', and then display a summary of the cities currently stored in the CSV file.

## Example Output

```text
Weather Report
City: Rochester
Country: US
Temperature: 17.23 degrees Celsius
Humidity: 67%
Description: broken clouds

Weather data saved to city_data.csv.

Cities currently in file: 1
Rochester: 17.23 degrees Celsius
```

## Input Validation and Error Handling

The program includes validation and error handling for situations such as:

- Empty city input
- Invalid city names
- Invalid or inactive API keys
- Network or connection problems
- Missing local files
- CSV file read/write errors
- Invalid API response data

## Screencast

https://www.loom.com/share/3e2965a58da74e1c8db57cbd54274d36

## AI Assistance

I used ChatGPT as a learning and debugging aid during this project. It helped me review concepts, troubleshoot errors, and improve my understanding of the code. I wrote, tested, and reviewed the final code myself.