# Flask CRUD Operations Demo

This repository contains a simple Flask web application that demonstrates CRUD (Create, Read, Update, Delete) operations. It includes a basic SQLite database for storing employee information.

## Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the application:**

    ```bash
    python app.py
    ```

    The app will be accessible at [http://127.0.0.1:5000/create](http://127.0.0.1:5000/create).

6. **Access the application in your web browser:**

    Open your web browser and go to [http://127.0.0.1:5000/create](http://127.0.0.1:5000/create) to start interacting with the CRUD application.

## Usage

- The initial page is the employee creation form at [http://127.0.0.1:5000/create](http://127.0.0.1:5000/create).
- Create, read, update, and delete employee records using the provided forms and listing page.

