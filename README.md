# Todo-List-Web-App

A Flask web application with PostgreSQL persistence, built to manage task lists and todos. Implements a relational schema with lists and associated todos, ensuring data is stored and retrievable even after the app is closed.

---

## Contents
- [Quick Start](#quick-start)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Database Schema](#database-schema)
- [Environment](#environment)
- [Usage](#usage)
- [Goals](#goals)
- [Contributing](#contributing)
- [License](#license)

---

## Quick Start

### Option A, use existing virtual environment
If this repo already includes a `.venv` folder with an environment named `webdev`, you can activate it directly.

```bash
# macOS or Linux
source .venv/webdev/bin/activate

# Windows PowerShell
.venv\webdev\Scripts\Activate.ps1

# Set environment variables
export FLASK_APP=app.py
export FLASK_ENV=development
export DATABASE_URL="postgresql://username:password@localhost/todos"
# On Windows PowerShell:
# $env:FLASK_APP="app.py"; $env:FLASK_ENV="development"; $env:DATABASE_URL="postgresql://username:password@localhost/todos"

# Create the database, then initialize schema
createdb todos
psql -d todos -f schema.sql

# Run the app
flask run
```

### Option B, use Poetry for dependency management
If you prefer Poetry, or you do not have the `webdev` venv, set up Poetry and install deps.

```bash
# Install Poetry if needed
# Recommended, pipx
pipx install poetry
# Alternative
pip install --user poetry

# Install project dependencies
poetry install

# Create the database, then initialize schema
createdb todos
psql -d todos -f schema.sql

# Run the app via Poetry
poetry run flask run
```

> Notes
> - This project uses Flask and psycopg2. If you use Option A, those should already be installed in `webdev`. If not, install them with Poetry: `poetry add flask psycopg2-binary`.
> - If you are not using `DATABASE_URL`, update your app configuration accordingly.

---

## Features
- Create and manage **lists** of tasks  
- Add, edit, and delete **todos** within each list  
- **Persistence** with PostgreSQL via **psycopg2**  
- Clean, minimal **Flask** interface  
- Relational integrity between lists and todos, supports cascading deletes  

---

## Tech Stack
- [Flask](https://flask.palletsprojects.com/) , Web framework  
- [PostgreSQL](https://www.postgresql.org/) , Relational database  
- [psycopg2](https://www.psycopg.org/) , PostgreSQL adapter for Python  
- [Poetry](https://python-poetry.org/) , Dependency and environment management  
- [HTML/CSS](https://developer.mozilla.org/en-US/docs/Web/HTML) , Frontend structure and styling  

---

## Database Schema
```sql
-- lists table
CREATE TABLE IF NOT EXISTS lists (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL
);

-- todos table
CREATE TABLE IF NOT EXISTS todos (
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  completed BOOLEAN DEFAULT FALSE,
  list_id INTEGER NOT NULL REFERENCES lists(id) ON DELETE CASCADE
);
```

---

## Environment
You can optionally use a `.env` file and a loader like `python-dotenv`.

```env
FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL=postgresql://username:password@localhost/todos
```

If you are using Poetry, you can set environment variables per shell session with `poetry run`, or export them in your shell as shown in Quick Start.

---

## Usage
- Visit the home page to view all lists  
- Create a new list, then add todos to it  
- Toggle completion status or delete todos  
- Delete a list to remove it and all associated todos  

---

## Goals
- Demonstrate full CRUD across a relational schema  
- Showcase pragmatic backend skills with Flask and PostgreSQL  
- Present a clean, interview-ready portfolio project  

---

## Contributing
Issues and PRs are welcome. Please open an issue to discuss substantial changes.  

---

## License
MIT License , see `LICENSE` for details.
