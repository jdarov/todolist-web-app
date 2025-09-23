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
```bash
# Clone the repository
git clone https://github.com/your-username/Todo-List-Web-App.git
cd Todo-List-Web-App

# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate    # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create the database (PostgreSQL)
createdb todo_list_web_app

# Initialize schema
psql -d todo_list_web_app -f schema.sql

# Set environment variables
export FLASK_APP=app.py
export FLASK_ENV=development
export DATABASE_URL="postgresql://username:password@localhost/todo_list_web_app"
# On Windows (PowerShell):
# $env:FLASK_APP="app.py"; $env:FLASK_ENV="development"; $env:DATABASE_URL="postgresql://username:password@localhost/todo_list_web_app"

# Run the app
flask run
```

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
  description TEXT NOT NULL,
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
DATABASE_URL=postgresql://username:password@localhost/todo_list_web_app
```

Minimal `requirements.txt`:
```txt
Flask>=3.0.0
psycopg2-binary>=2.9.0
python-dotenv>=1.0.0
```

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
