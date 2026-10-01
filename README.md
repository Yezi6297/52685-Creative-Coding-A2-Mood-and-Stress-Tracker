# Mood and Stress Tracker in Python

# Project Overview

This project is a simple Mood and Stress Tracker created using Python.

The program allows users to record their daily commute time, stress level and mood level. It stores data for multiple days and then analyses the information.

The final version combines data recording, analysis, CSV storage and visualisation to help users understand weekly patterns.

# Prototype Versions

## Prototype Version 1 - Basic Input and Output
- Created basic user input and output.
- Allowed the user to enter commute time, stress level and mood level.
- Displayed the entered information back to the user.

## Prototype Version 2 - Multiple Days and Lists
- Added multiple-day data recording.
- Used lists to store daily commute, stress and mood data.
- Used loops to collect information for several days.
- Allowed the users to create a weekly record.

## Prototype Version 3 - Data Analysis + CSV Storage + Multiple Weeks
- Calculates the average commute time, stress level and mood level.
- Identifies the day with the highest stress level.
- Identifies the day with the lowest mood level.
- Saves weekly data into a CSV file.
- Loads previously saved records from the CSV file.
- Allows data from multiple weeks to be stored without deleting earlier records.

## Prototype Version 4 - Data Visualisation and Final Refinement
- Added input validation for week number, commute time, stress level and mood level.
- Improved handling of invalid inputs and tied values.
- Added longest commute analysis.
- Kept CSV storage and saved-record loading from Version 3.
- Added Matplotlib visualisation for weekly stress and mood levels.

# Final Version

Version 4 is the final version because it includes all the main functions developed in the previous versions. It can record data for multiple days and weeks, analyse the data, save and load records using a CSV file, validate week number, commute time, stress and mood inputs, and create visualisations using Matplotlib.

## How to Run
1. Make sure Python is installed on the computer.
2. Install Matplotlib before running the program.
3. Open the file:

   `Prototype Version 4 - Data Visualisation and Final Refinement.py`

4. Run the Python file in Visual Studio Code or another Python environment.
5. Enter the requested information, including:
   - week number
   - daily commute time
   - stress level
   - mood level
6. The program will store and analyse the weekly data.
7. The data will be saved to "mood_stress_data.csv".
8. The program will display the saved records and create a chart showing weekly stress and mood levels.

## Requirements

The project uses:

- Python
- Matplotlib

Version 3 and Version 4 also use Python's built-in `csv` and `os` modules, so no extra installation is required for them.

Install Matplotlib with:

`pip install matplotlib`


## Project Files

- `Prototype Version 1 - Basic Input and Output.py`
  - Contains the basic input and output functions.

- `Prototype Version 2 - Multiple Days and Lists.py`
  - Records data for multiple days using lists and loops.

- `Prototype Version 3 - Data Analysis + CSV Storage + Multiple Weeks.py`
  - Analyses the recorded data, calculates averages, highest stress and lowest mood.

- `Prototype Version 4 - Data Visualisation and Final Refinement.py`
  - The final version with input validation, longest commute analysis and Matplotlib visualisation.


## Screenshots

The `screenshots` folder contains evidence showing the development and testing of the project.

It includes:

- Prototype Version 1 - Basic Input and Output.png
- Prototype Version 2 - Multiple Days and Lists.png
- Prototype Version 3 - Data Analysis + CSV Storage + Multiple Weeks.png
- Prototype Version 4 - Running Successfully.png
- Prototype Version 4 - Final Visualisation.png

These screenshots show how the prototype developed from a basic program into the final version.

## Limitations

- The program does not prevent the same week number from being entered more than once.
- Commute time, stress level and mood level are all self-reported by the user, so the data may not always be completely accurate.
- This program is designed for personal tracking only and is not a medical or mental health diagnosis tool.
- The current version only records data from Monday to Friday.
- The analysis is based on a small amount of data, so it may not represent long-term patterns.
- The program only uses simple averages and basic comparisons.

## References / Acknowledgements

The following resources were used to support the development of this project:

- Python Documentation  
  https://docs.python.org/3/

- Matplotlib Documentation  
  https://matplotlib.org/stable/

These resources helped with Python syntax, lists, loops, input validation and data visualisation using Matplotlib.

## Author / Student ID
Yezi Yang
Student ID: 14734242
