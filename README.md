# Pink Morsel Sales Visualizer

[![Run tests](https://github.com/scientistdanyal/quantium/actions/workflows/tests.yml/badge.svg)](https://github.com/scientistdanyal/quantium/actions/workflows/tests.yml)

A data processing and visualization project completed as part of the Quantium Software Engineering Job Simulation on Forage.

The project combines three Soul Foods transaction datasets, filters them to Pink Morsel sales, and presents the results in an interactive Dash application. The visualizer helps answer whether sales were higher before or after the Pink Morsel price increase on January 15, 2021.

## Features

- Combines and processes multiple CSV datasets
- Calculates sales from price and quantity
- Displays sales over time in an interactive line chart
- Filters sales by north, south, east, west, or all regions
- Includes automated browser tests
- Runs the test suite automatically with GitHub Actions

## Technologies

- Python
- pandas
- Dash
- Plotly
- pytest
- Bash
- GitHub Actions
- uv

## Run the project

Clone the repository and install its dependencies:

```bash
git clone https://github.com/scientistdanyal/quantium.git
cd quantium
uv sync
```

Start the Dash application:

```bash
uv run app.py
```

Then open <http://127.0.0.1:8050/> in your browser.

## Run the tests

The test script activates the project virtual environment, runs the browser tests, and returns an appropriate exit code:

```bash
./run_tests.sh
```

The tests require Google Chrome and ChromeDriver.

## Project structure

```text
data/                           Raw Soul Foods transaction data
main.py                         Data processing script
pink_morsel_sales.csv           Processed Pink Morsel sales data
app.py                          Dash visualization
test_pink_morsel_visualizer.py  Automated application tests
run_tests.sh                    Test runner used by CI
.github/workflows/tests.yml     GitHub Actions workflow
```

## Certificate

I completed the Quantium Software Engineering Job Simulation through Forage in July 2026.

[View my certificate of completion](jhiG2W9K8KLZK8nXP_32A6DqtsbF7LbKdcq_6a303d82bd9ce96fb90bb4f1_1784140702523_completion_certificate.pdf)
