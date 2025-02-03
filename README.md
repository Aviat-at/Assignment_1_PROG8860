# project Title
# Django Task Manager Application

## Overview
This is a Django-based Task Manager application with a REST API, built using Django Rest Framework (DRF). The application allows users to create, read, update, and delete tasks.

## Features
- Create a task with title, description, and status.
- Retrieve all tasks or a specific task.
- Update task details.
- Delete a task.
- Includes unit tests for API endpoints.

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Setup Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3. Install Dependencies
```bash
pip install django djangorestframework
```

### 4. Run Migrations
```bash
python manage.py makemigrations
target_title="Task Manager"
python manage.py migrate
```

### 5. Run the Server
```bash
python manage.py runserver
```
- Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## API Endpoints
| Method | Endpoint         | Description         |
|--------|-----------------|---------------------|
| GET    | /api/tasks/     | Retrieve all tasks |
| POST   | /api/tasks/     | Create a new task  |
| GET    | /api/tasks/{id}/ | Retrieve a task by ID |
| PUT    | /api/tasks/{id}/ | Update a task |
| DELETE | /api/tasks/{id}/ | Delete a task |

## Running Tests
```bash
python manage.py test
```

## Contributing
1. Fork the repository.
2. Create a new branch (`feature-branch`):
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```bash
   git commit -m "Added new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-branch
   ```
5. Create a Pull Request.

## License
This project is licensed under the MIT License.

