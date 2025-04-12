# Local Development Server

This project sets up a local development server that handles redirects for testing purposes. It is built using Flask (or FastAPI) and listens on port 8000.

## Getting Started

### Prerequisites

Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone the repository:

   ```
   git clone <repository-url>
   cd local-dev-server
   ```

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

### Running the Server

To start the local development server, run the following command:

```
python src/server.py
```

The server will start and listen on `http://localhost:8000`. You can access the callback route at `http://localhost:8000/callback`.

### Usage

Once the server is running, you can test the redirect functionality by navigating to the `/callback` endpoint in your web browser or by using tools like Postman or curl.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.