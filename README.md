# Decision Log - Lesson: Introduction to Flask Fundamentals

This branch contains the first working stage of the Decision Log application using server-rendered pages.

## What Was Built

- A minimal Flask application in `app.py`
- Template rendering with Jinja2 from the `templates/` folder
- Basic routes:
  - `GET /` renders the Decision Log home page (`templates/index.html`)
  - `GET /about` renders the lesson about page (`templates/about.html`)
- A small in-memory list of sample decisions displayed in HTML

## Key Concepts Introduced

- Creating a Flask app (`Flask(__name__)`)
- Running a Flask app in debug mode
- Route decorators for view functions
- Server-rendered responses with `render_template`
- Basic Jinja template looping to display data

## Setup Requirements

- Python 3.10+
- Virtual environment (recommended)

## How to Run

1. Create and activate a virtual environment:
   - macOS/Linux:
     ```bash
     python -m venv env
     source env/bin/activate
     ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the app:
   ```bash
   python app.py
   ```

4. Open in your browser:
   - `http://127.0.0.1:5000/`
   - `http://127.0.0.1:5000/about`

This lesson focuses on building a strong Flask foundation through app setup, routing, views, and server-rendered templates.
