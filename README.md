# Decision Journal API

Production-ready Flask REST API for user authentication, profile management, and personal decision journaling.

## Features

- Flask application factory + modular blueprint architecture
- PostgreSQL (Neon) via Flask-SQLAlchemy
- Flask-Migrate migrations (Alembic)
- Marshmallow validation + serialization
- Session auth with Flask-Login
- Profile picture upload + resize to 300x300 with Pillow
- Swagger UI docs via Flasgger
- Consistent JSON response format:

```json
{
  "success": true,
  "message": "",
  "data": {}
}
```

## Project Structure

```text
app/
  __init__.py
  config.py
  extensions.py
  blueprints/
    auth.py
    user.py
    decision.py
  models/
    user.py
    decision.py
  resources/
    auth.py
    user.py
    decision.py
  schemas/
    user_schema.py
    decision_schema.py
  utils/
    auth.py
    image_helper.py
    response.py
  static/uploads/
  swagger/
    swagger_config.py
migrations/
.env
run.py
requirements.txt
```

## Prerequisites

- Python 3.13+
- PostgreSQL connection (Neon is already configured in `.env`)
- `pip`

## Environment Variables

Create/update `.env` in project root:

```env
DATABASE_URL=postgresql://.../neondb?sslmode=require&channel_binding=require
SECRET_KEY=your-secret-key
```

## Installation

```bash
python -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```

## Database Setup

Initialize migrations (already done in this workspace, run only if needed):

```bash
./myenv/bin/python -m flask --app run.py db init
```

Create migration and apply:

```bash
./myenv/bin/python -m flask --app run.py db migrate -m "initial schema"
./myenv/bin/python -m flask --app run.py db upgrade
```

## Run the API

```bash
./myenv/bin/python run.py
```

Server starts at:

- `http://127.0.0.1:5000`

## API Docs (Swagger)

- Swagger UI: `http://127.0.0.1:5000/swagger/`
- OpenAPI JSON: `http://127.0.0.1:5000/apispec.json`

## How To Access Endpoints

This API uses **session-based authentication** (Flask-Login). After login, send the session cookie on subsequent requests.

### Option A: Postman / Insomnia

1. Register or login.
2. Ensure cookie jar is enabled.
3. Call protected endpoints using the same session.

### Option B: curl with cookie jar

Use `-c cookies.txt` to store cookies and `-b cookies.txt` to send them.

#### 1) Register

```bash
curl -X POST http://127.0.0.1:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "username":"alice",
    "email":"alice@example.com",
    "password":"StrongPass123"
  }'
```

#### 2) Login (save session cookie)

```bash
curl -X POST http://127.0.0.1:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -c cookies.txt \
  -d '{
    "email":"alice@example.com",
    "password":"StrongPass123"
  }'
```

#### 3) Get Profile (authenticated)

```bash
curl -X GET http://127.0.0.1:5000/api/user/profile \
  -b cookies.txt
```

#### 4) Update Profile (authenticated)

```bash
curl -X PUT http://127.0.0.1:5000/api/user/profile \
  -H "Content-Type: application/json" \
  -b cookies.txt \
  -d '{"username":"alice_updated"}'
```

#### 5) Upload Profile Picture (authenticated)

```bash
curl -X POST http://127.0.0.1:5000/api/user/profile/picture \
  -b cookies.txt \
  -F "profile_picture=@/absolute/path/to/photo.jpg"
```

#### 6) Create Decision (authenticated)

```bash
curl -X POST http://127.0.0.1:5000/api/decisions \
  -H "Content-Type: application/json" \
  -b cookies.txt \
  -d '{
    "title":"Move to a new city",
    "reason":"Career growth",
    "confidence_level":8,
    "outcome":"Pending",
    "lesson":"Gather more data first"
  }'
```

#### 7) List Decisions (authenticated)

```bash
curl -X GET http://127.0.0.1:5000/api/decisions \
  -b cookies.txt
```

#### 8) Get One Decision (authenticated)

```bash
curl -X GET http://127.0.0.1:5000/api/decisions/1 \
  -b cookies.txt
```

#### 9) Update Decision (authenticated)

```bash
curl -X PUT http://127.0.0.1:5000/api/decisions/1 \
  -H "Content-Type: application/json" \
  -b cookies.txt \
  -d '{"confidence_level":9,"outcome":"Good decision"}'
```

#### 10) Delete Decision (authenticated)

```bash
curl -X DELETE http://127.0.0.1:5000/api/decisions/1 \
  -b cookies.txt
```

#### 11) Logout

```bash
curl -X POST http://127.0.0.1:5000/api/auth/logout \
  -b cookies.txt
```

## Endpoint Summary

### Auth

- `POST /api/auth/register`
- `POST /api/auth/login`
- `POST /api/auth/logout`

### User

- `GET /api/user/profile`
- `PUT /api/user/profile`
- `POST /api/user/profile/picture`

### Decisions

- `GET /api/decisions`
- `GET /api/decisions/<id>`
- `POST /api/decisions`
- `PUT /api/decisions/<id>`
- `DELETE /api/decisions/<id>`

## Notes

- `GET /api/decisions` and `GET /api/decisions/` are both accepted.
- Profile images are stored under `app/static/uploads`.
- Passwords are hashed using Werkzeug; plaintext passwords are never stored.
