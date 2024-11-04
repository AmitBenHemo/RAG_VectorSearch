# Setup Instructions

## Prerequisites

- Docker installed on your machine.
- Basic knowledge of Docker commands and environment files (.env).
- `.env` files set up for both backend and frontend as outlined below.

---

## Backend Setup

1. **Create a `.env` file** in the root directory of the backend folder with the following content:

    ```plaintext
    DB_URI=***
    OPEN_AI_KEY=***
    ```

2. **Build the Docker image** from the backend folder:

    ```bash
    docker build -t evolink-api .
    ```

3. **Run the Docker container** with the `.env` file:

    ```bash
    docker run -p 8000:8000 --env-file .env evolink-api
    ```

4. Alternatively, **start the backend with Docker Compose**:

    ```bash
    docker-compose up --build
    ```

---

## Frontend Setup

1. **Create a `.env` file** in the root directory of the frontend folder with the following content:

    ```plaintext
    VITE_API_BASE_URL=http://127.0.0.1:8000
    ```

2. **Build the Docker image** for the frontend:

    ```bash
    docker build -t evolink-fe .
    ```

3. **Run the Docker container** for the frontend:

    ```bash
    docker run -p 3000:3000 evolink-fe
    ```

---

## Access the Application

After both backend and frontend containers are running, open your browser and navigate to:

```plaintext
http://localhost:3000/
```

This will take you to the frontend, which communicates with the backend at `http://127.0.0.1:8000`.

---

## Notes

- Ensure you are running each command from the correct folder (`backend` or `frontend`).
- The `.env` files must be set up in the root directory of each respective folder.

