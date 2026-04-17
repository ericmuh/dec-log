# Decision Log - Lesson 3: Jinja Templates, Static Files, and CRUD

This branch is a standalone stage of the Decision Log application focused on Jinja template structure, shared layouts, static styling, and full CRUD operations.

## What Was Built

- A Flask app in app.py
- Server-rendered pages with reusable Jinja templates
- Template inheritance with templates/base.html
- A design style based on the reference images using static/css/style.css
- Full in-memory CRUD flows for decisions
- Screens included in this stage:
   - GET /
   - GET /about
   - GET /decisions/<int:decision_id>
   - GET/POST /decisions/new (Create)
   - GET/POST /decisions/<int:decision_id>/edit (Update)
   - POST /decisions/<int:decision_id>/delete (Delete)
- A template-based 404 response for unknown decision IDs

## Key Concepts Introduced

- Reusable layouts with extends and block tags
- Passing Python dictionaries into templates
- Jinja loops for rendering decision rows and details
- URL generation inside templates with url_for
- Serving static CSS from the static folder
- Handling form submissions with request.form
- Redirects after successful create/update/delete actions

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
   - `http://127.0.0.1:5000/about`
   - `http://127.0.0.1:5000/decisions/1`
   - `http://127.0.0.1:5000/decisions/new`
   - `http://127.0.0.1:5000/decisions/1/edit`
