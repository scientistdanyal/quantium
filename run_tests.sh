#! /bin/bash


VENV_PATH=".venv/bin/activate"
if [[ ! -f "$VENV_PATH" ]]; then
    echo "Error: virtual environment not found."
    echo "Run 'uv sync' first"
    exit 1
fi

source "$VENV_PATH"

if python -m pytest test_pink_morsel_visualizer.py -v --headless --webdriver Chrome; then
    echo "Tests passed"
    exit 0
else
    echo "Tests failed"
    exit 1
fi