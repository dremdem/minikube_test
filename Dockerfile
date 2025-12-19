FROM python:3.12-slim
WORKDIR /app
COPY app.py .
RUN pip install fastapi uvicorn
ARG APP_VERSION=dev
ENV APP_VERSION=${APP_VERSION}
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
