
# Django Task Manager Application

A Django-based REST API for managing tasks (create, read, update, delete). This project features a Dockerized setup and a CI/CD pipeline with GitHub Actions.

## Quick Start

### Using Docker

1. **Build the Docker image:**
   ```bash
   docker build -t django-task-manager .
   ```

2. **Run the Docker container:**
   ```bash
   docker run -d --name task_manager -p 8000:8000 django-task-manager
   ```

3. **Run tests inside the container:**
   ```bash
   docker exec task_manager python manage.py test
   ```

4. **Stop and remove the container:**
   ```bash
   docker stop task_manager && docker rm task_manager
   ```

### Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  
   pip install -r requirements.txt
   ```

3. **Run migrations and start the server:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
   Access the app at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## API Endpoints

- **GET** `/api/tasks/` – Retrieve all tasks
- **POST** `/api/tasks/` – Create a new task
- **GET** `/api/tasks/{id}/` – Retrieve a specific task by ID
- **PUT** `/api/tasks/{id}/` – Update a task
- **DELETE** `/api/tasks/{id}/` – Delete a task

## CI/CD Pipeline

A GitHub Actions workflow is configured to automatically build the Docker image, run tests, and clean up containers on pushes and pull requests to the `main` and `akash` branches.

## License

This project is licensed under the [MIT License](LICENSE).
```