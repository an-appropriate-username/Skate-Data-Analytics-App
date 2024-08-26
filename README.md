# Skateboarding Trick Visualization and Analysis

## Overview
This project is a Python application designed to analyze and visualize skateboarding trick data from professional skateboarding parts. The application reads data from an Excel file (`skate_data.csv`) and provides detailed skater information, along with visualizations of their trick distribution by stance and obstacle type.

## Features
- **Skater Overview**: Displays detailed information about selected skateboarders, including name, stance, board size, birth year, country, and the name of the skate part.
- **Stance Visualization**: Generates pie charts to visualize the distribution of tricks performed in different stances (Regular, Switch, Nollie, Fakie) by each skateboarder.
- **Obstacle Visualization**: Creates pie charts to represent the distribution of tricks performed across various obstacles (Rail, Hubba, Ledge, etc.) for each skater.
- **The Numbers**: Displays a bar graph that breaks down the trick counts across various categories, including total tricks, flips, spins, and different stance types.

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - `Pandas` for data manipulation
  - `Matplotlib` for data visualization
  - `OS` for file management

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/an-appropriate-username/Skate-Data-Analytics-App
    ```
2. Navigate to the project directory
    ```
3. Install the required Python libraries:
    ```bash
    pip install pandas matplotlib
    ```
4. Ensure that the `skate_data.csv` file is present in the project directory.

## Usage
1. Run the main script:
    ```bash
    python skate_data_main.py
    ```
2. Follow the on-screen menu to select a skateboarder and view their details or visualizations.

3. To generate and save visualizations for all skaters:
    - Enter `111` at the menu prompt.
