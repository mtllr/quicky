# Quicky

Quicky is a Dockerized FastAPI project template for any Hugging Face task. The project allows for easy deployment and configuration through environment variables.

## Setup

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd quicky
    ```

2. Create a `.env` file in the `app` directory with your Hugging Face task, model, token, and port:
    ```plaintext
    HUGGINGFACE_TASK=summarization  # Change to your desired task, e.g., translation, text-classification, etc.
    HUGGINGFACE_MODEL=facebook/bart-large-cnn  # Change to your desired model
    HUGGINGFACE_TOKEN=your_hugging_face_token_here
    APP_PORT=8000  # Change to your desired port
    ```

3. Build the Docker image:
    ```sh
    docker build -t quicky_app ./app
    ```

4. Run the Docker container:
    ```sh
    docker run --env-file ./app/.env -p $APP_PORT:$APP_PORT quicky_app
    ```

5. Access the API at `http://localhost:<YOUR_CONFIGURED_PORT>/process`.

## Verification and tests

1. **Build the Docker image**:
    ```sh
    docker build -t quicky_app ./app
    ```

2. **Run the Docker container**:
    ```sh
    docker run --env-file ./app/.env -p $APP_PORT:$APP_PORT quicky_app
    ```

3. **Run the tests**:
    ```sh
    docker build -t quicky_test --target test ./app
    docker run --env-file ./app/.env quicky_test
    ```

## Usage

Send a POST request to `http://localhost:<YOUR_CONFIGURED_PORT>/process` with a JSON payload containing the text you want to process. For example:
```json
{
    "text": "Your text here..."
}