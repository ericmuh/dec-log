# Decision Log - Lesson 2: Dynamic Routes and HTTP Responses

This branch is a standalone stage of the Decision Log application focused on dynamic routing and response handling in Flask.

## What Was Built

- A Flask app in `app.py`
- Dynamic route using an integer converter:
  - `GET /decisions/<int:decision_id>`
- Dynamic route using a string converter:
  - `GET /member/<string:username>`
- Server-rendered pages with Jinja templates in `templates/`
- HTTP response examples:
  - Standard successful response with a custom header (`/lesson-response`)
  - Redirect response (`/go-home`)
  - Not found response with status code `404` when a decision ID does not exist

## Key Concepts Introduced

- Variable parts in URLs (`<int:...>`, `<string:...>`)
- Passing dynamic route values into view functions
- Returning different HTTP responses in Flask
- Returning template responses with custom status codes
- URL building with `url_for`

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

4. Open these routes in your browser:
   - `http://127.0.0.1:5000/`
   - `http://127.0.0.1:5000/decisions/1`
   - `http://127.0.0.1:5000/member/alice`
   - `http://127.0.0.1:5000/lesson-response`
   - `http://127.0.0.1:5000/go-home`
