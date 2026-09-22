"""Starter code for the Building REST APIs with FastAPI assignment."""

from fastapi import FastAPI

app = FastAPI(title="Task API")


@app.get("/health")
def health_check():
    """Return the current API status."""
    return {"status": "ok"}


# TODO: Create a Pydantic model for a task.
# TODO: Add an in-memory collection and an ID counter.
# TODO: Implement GET, POST, PUT/PATCH, and DELETE endpoints for /tasks.
# TODO: Add validation and appropriate HTTP status codes.


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
