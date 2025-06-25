# Use official Python image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy requirements if exists, else install FastAPI and Uvicorn
COPY app.py ./

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn

# Expose port
EXPOSE 8000

# Run the app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"] 