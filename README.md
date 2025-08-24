# Sample Python API

A simple RESTful API built with FastAPI and Python.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd sample-python-api
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

To start the API server:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

## API Documentation

Once the server is running, you can access:
- Interactive API documentation (Swagger UI) at `http://localhost:8000/docs`
- Alternative API documentation (ReDoc) at `http://localhost:8000/redoc`

## Docker Support

The project includes Docker support. To build and run using Docker:

```bash
# Build the Docker image
docker build -t sample-python-api .

# Run the container
docker run -p 8000:8000 sample-python-api
```

## Dependencies

- FastAPI (>= 0.103.0) - Modern, fast web framework for building APIs
- Uvicorn (>= 0.23.0) - Lightning-fast ASGI server implementation

## License

[MIT License](LICENSE)