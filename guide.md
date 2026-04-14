Create a full production-ready Flask RESTful API application called "Decision Journal API".

The system should be well-structured, modular, and follow best practices for Flask backend architecture.

---

## 🔥 Tech Stack

- Flask (REST API only, no HTML rendering except Swagger docs)
- Flask-RESTful for API resources
- Flask-SQLAlchemy for ORM
- Flask-Migrate for database migrations
- Marshmallow for serialization + validation
- Flask-Login for authentication/session management
- python-dotenv for environment variables
- Pillow (PIL) for image processing (profile picture upload + resize)
- Swagger / OpenAPI (flasgger or similar)
- Blueprint-based architecture

---

## 🗄️ DATABASE (IMPORTANT)

Use PostgreSQL (Neon database).

DO NOT hardcode credentials in code.

Put this in `.env`:

DATABASE_URL=postgresql://neondb_owner:npg_7amevQoZsf2O@ep-shiny-snow-amp5rfi7-pooler.c-5.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require

SECRET_KEY=your-secret-key

Then configure Flask-SQLAlchemy like this:

- SQLALCHEMY_DATABASE_URI must read from environment variable DATABASE_URL
- SQLALCHEMY_TRACK_MODIFICATIONS = False

---

## 👤 USER SYSTEM

Build full authentication system:

- Register user
- Login user
- Logout user
- Password hashing using Werkzeug
- Flask-Login session handling
- User profile endpoint
- Profile picture upload + update (using Pillow resize to 300x300)

User fields:
- id
- username
- email
- password_hash
- profile_picture
- created_at

---

## 🧠 DECISION SYSTEM

Create Decision model:

- id
- title
- reason
- confidence_level (integer 1–10)
- outcome
- lesson
- created_at
- user_id (ForeignKey → User)

Rules:
- Each user only sees their own decisions
- All decision routes must be protected (login required)

---

## 📡 API ENDPOINTS

### Auth
- POST /api/auth/register
- POST /api/auth/login
- POST /api/auth/logout

### Users
- GET /api/user/profile
- PUT /api/user/profile
- POST /api/user/profile/picture

### Decisions (CRUD)
- GET /api/decisions
- GET /api/decisions/<id>
- POST /api/decisions
- PUT /api/decisions/<id>
- DELETE /api/decisions/<id>

---

## 🏗 PROJECT STRUCTURE (VERY IMPORTANT)

Use clean modular architecture:

app/
  __init__.py (app factory)
  config.py
  extensions.py

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
    image_helper.py

  blueprints/
    auth.py
    user.py
    decision.py

  static/uploads/

  swagger/
    swagger_config.py

migrations/
.env
run.py
requirements.txt

---

## ⚙️ CONFIGURATION

- Use application factory pattern (create_app)
- Load environment variables using python-dotenv
- Use Config class for DevelopmentConfig and ProductionConfig
- Use os.getenv() everywhere sensitive values are needed

---

## 🧾 MARSHMALLOW REQUIREMENTS

- Validate all input data
- Serialize all output data
- Return clear validation error messages

---

## 🧠 SQLALCHEMY REQUIREMENTS

- Proper relationships between User and Decision
- Use back_populates or backref
- Add created_at timestamps
- Ensure cascade delete for user decisions

---

## 🖼 IMAGE UPLOAD (PILLOW)

- Allow users to upload profile pictures
- Resize images to 300x300
- Save with UUID filename
- Store path in database

---

## 📘 SWAGGER DOCUMENTATION

- Document all endpoints
- Group endpoints:
  - Auth
  - Users
  - Decisions
- Include request/response schemas

---

## 🧪 BEST PRACTICES

- Use try/except error handling
- Return consistent JSON format:

{
  "success": true,
  "message": "",
  "data": {}
}

- Use decorators for authentication
- Protect all decision routes
- Keep code clean and commented per section

---

## 🎯 GOAL

Generate a production-level Flask backend API with:
- Clean architecture
- Authentication
- PostgreSQL (Neon)
- File uploads
- Swagger docs
- Modular design
- Real-world scalability