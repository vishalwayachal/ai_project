# AI Modules

This project provides a FastAPI-based service for text rephrasing using machine learning models. It is designed for easy integration, robust logging, and standardized API responses.

## Features
- **Rephrase Service**: Rephrase text using a transformers-based model.
- **Standardized API Responses**: All API responses follow a consistent format.
- **Logging**: Environment-specific logging with support for file and console outputs.
- **Middleware**: Includes middleware for logging request details and execution time.

## Project Structure
```
README.md
requirements.txt
run.py
app/
    main.py
    api/
        v1/
            rephrase_endpoints.py
    core/
        config.py
    logging/
        logger.py
    models/
        rephrase.py
    services/
        rephrase_service.py
    utils/
        image_utils.py
        request_logger.py
        response_utils.py
tests/
    test_rephrase.py
```

## Setup

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)

### Creating a Virtual Environment
It is recommended to use a virtual environment to manage dependencies and avoid conflicts:

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
2. Activate the virtual environment:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
3. (Optional) To deactivate the virtual environment:
   ```bash
   deactivate
   ```

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Environment Variables
Create a `.env` file in the root directory and configure the following variables:
```
APP_NAME=AI-Module
VERSION=1.0.0
HOST=0.0.0.0
PORT=8000
LOG_FILE_PATH=/var/log/riavera/{env}/ai-module.log
```

## Running the Application
Start the FastAPI application:
```bash
python run.py
```

The application will be available at `http://<HOST>:<PORT>`.

## API Documentation
FastAPI automatically generates interactive API documentation. Access it at:
- Swagger UI: `http://<HOST>:<PORT>/docs`
- ReDoc: `http://<HOST>:<PORT>/redoc`

## Endpoints

### Rephrase Endpoint
- **URL**: `/api/v1/rephrase`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "text": "string"
  }
  ```
- **Response**:
  ```json
  {
    "status": "ok",
    "data": {
      "rephrased_text": "string"
    }
  }
  ```

## Testing
Run the test suite using:
```bash
pytest tests/
```

## Logging
Logs are stored in environment-specific files. Configure the log file path in the `.env` file.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push the branch.
4. Open a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.