FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Default to auth if not specified
ARG APP_NAME=auth
ENV MODULE_NAME=${APP_NAME}

EXPOSE 80
CMD uvicorn ${MODULE_NAME}:app --host 0.0.0.0 --port 80