# Decision Log - Lesson 5: Blueprints and Organizing Flask Application

This branch is a standalone stage of the Decision Log project focused on organizing the app with blueprints and adding a User model.

## What Was Built

- App factory setup in app/__init__.py
- Extension setup in app/extensions.py
- Models in app/models.py:
  - User model
  - Decision model linked to User (one-to-many)
- Blueprints:
  - main blueprint for home and about
  - users blueprint for user pages
  - decisions blueprint for decision CRUD pages
- Server-rendered templates organized by feature folders
- Static stylesheet in app/static/css/style.css

## Key Concepts Introduced

- Blueprint route organization with url_prefix
- Application factory pattern (create_app)
- Separating extensions and models into modules
- SQLAlchemy relationships between models
- Keeping template-based flows while scaling project structure

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

3. Run migration setup (first time):
   ```bash
   flask --app run db init
   flask --app run db migrate -m "create user and decision tables"
   flask --app run db upgrade
   ```

4. Start the app:
   ```bash
   python run.py
   ```

5. Open in browser:
   - http://127.0.0.1:5000/
   - http://127.0.0.1:5000/users/
   - http://127.0.0.1:5000/decisions/
# Decision Log - Lesson 4: Extensions (Flask-SQLAlchemy, Flask-Migrate) + Databases

This branch is a standalone stage of the Decision Log application focused on using Flask extensions to persist data in a database.

## What Was Built

- A Flask app in app.py
- Flask-SQLAlchemy configured as the ORM extension
- Flask-Migrate configured for migration workflow
- A database model for decisions (Decision table)
- Server-rendered CRUD routes now backed by SQLite database storage
- Basic templates and static CSS for the same Decision Log flow

## Key Concepts Introduced

- Flask extension setup and initialization
- SQLAlchemy model definition with columns and defaults
- Database CRUD operations with db.session
- Using Flask-Migrate commands to manage schema changes
- Keeping template-based pages while moving from in-memory data to database data

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

3. Initialize and apply migrations (first time only):
   ```bash
   flask --app app db init
   flask --app app db migrate -m "create decision table"
   flask --app app db upgrade
   ```

4. Start the app:
   ```bash
   python app.py
   ```

5. Open in browser:
   - http://127.0.0.1:5000/
   - http://127.0.0.1:5000/decisions/new

Note: app.py also calls db.create_all() when run directly so the lesson remains beginner-friendly even before migrations are run.
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
