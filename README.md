# HackerNews API with FastAPI

This project is a FastAPI-based API that interacts with the HackerNews API to fetch and serve the top, new, best, show, and job stories. It provides endpoints that allow users to retrieve these stories in real-time with essential details like the title, author, URL, score, and time (in a human-readable format). The project includes error handling to manage potential issues, such as when the HackerNews API is down or unreachable.

## Key Features
> **Real-time Data :** Fetches live data from the HackerNews API.  
> **Multiple Story Types :** Supports fetching different types of stories, including:
    > - New Stories
    > - Top Stories
    > - Best Stories
    > - Show Stories
    > - Job Stories
>
> **Data Formatting :** Returns story details such as:
    > - Title
    > - Author
    > - URL
    > - Score
    > - Time
>
> **Error Handling :** Handles various error scenarios:
    > - If the HackerNews API is down
    > - Connection errors or timeouts
    > - Invalid responses from the API

> ## Example
> ```JSON
>   [
>     {
>       "title": "Example Title",
>       "author": "example_author",
>       "url": "https://example.com",
>       "score": 100,
>       "time": "2024-09-15 12:30:45"
>     },
>     ...
>   ]
> ```




---
## Project Structure

    hackernews_api/

        ├── app/
        │   ├── __init__.py
        │   ├── main.py
        │   ├── api/
        │   │   ├── __init__.py
        │   │   └── routes.py
        │   ├── models/
        │   │   ├── __init__.py
        │   │   └── story.py
        │   ├── services/
        │   │   ├── __init__.py
        │   │   └── hackernews_service.py
        │   └── utils/
        │       ├── __init__.py
        │       └── helpers.py
        ├── requirements.txt
        └── README.md




## Setup

### Prerequisites

- Python `3.8` or higher
- `pip` (Python package installer)
- Docker (for containerization)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Abhishekkumar021/hackernews-api-fastapi.git

    cd HackerNewsAPI-Backend
    ```


2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Create a `.env` file** in the root directory and add the following environment variables:

    ```
    BASE_HN_URL=https://hacker-news.firebaseio.com/v0
    ORIGIN=http://localhost:5173
    Allow_Methods=GET
    ```

4. **Run the application:**

    ```bash
    uvicorn app.main:app --reload
    ```

    Your FastAPI application will be running on `http://127.0.0.1:8000`.

### API Endpoints

- **GET** `/new-stories` - Fetches new stories.
- **GET** `/top-stories` - Fetches top stories.
- **GET** `/best-stories` - Fetches best stories (Higher scored stories).
- **GET** `/show-stories` - Fetches show stories.
- **GET** `/job-stories` - Fetches job stories.

### Dockerization

1. **Build the Docker image:**

    ```bash
    docker build -t HackerNewsAPI-Backend .
    ```

2. **Run the Docker container:**

    ```bash
    docker run -d -p 8000:8000 --env-file .env HackerNewsAPI-Backend
    ```

    Your FastAPI application will be accessible at `http://localhost:8000` inside the Docker container.

### Contributing

Feel free to open issues or submit pull requests. Contributions are welcome!
